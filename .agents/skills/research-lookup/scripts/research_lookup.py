#!/usr/bin/env python3
"""Research lookup tool for agentic AI/ML/CV research workflows.

This is the main implementation script for the research-lookup skill.

Design goals:
- Prefer free structured scholarly APIs for paper discovery.
- Use paid/synthesis APIs only as optional fallback.
- Support mode-based lookup for prior work, baselines, datasets, citations,
  technical verification, and recent developments.
- Support recency, quality, venue, work-type, and citation filters.
- Save lookup artifacts so later agents can audit, synthesize, cite, or review them.

Recommended agent entry point:
    python .agents/skills/research-lookup/lookup.py "query" --mode prior-work

Direct script entry point:
    python .agents/skills/research-lookup/scripts/research_lookup.py "query" --mode prior-work
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VALID_MODES = {
    "prior-work",
    "baseline-scout",
    "dataset-benchmark",
    "citation-candidates",
    "technical-verification",
    "recent-developments",
}

VALID_BACKENDS = {
    "auto",
    "openalex",
    "arxiv",
    "crossref",
    "semantic-scholar",
    "parallel",
    "perplexity",
}

VALID_QUALITY_LEVELS = {
    "any",
    "scholarly",
    "peer-reviewed",
    "journal",
    "proceedings",
    "preprint",
}

FREE_SCHOLARLY_BACKENDS = {"openalex", "arxiv", "crossref", "semantic-scholar"}
OPTIONAL_SYNTHESIS_BACKENDS = {"parallel", "perplexity"}

DEFAULT_LIMIT = 10

CONFERENCE_TOKENS = {
    "cvpr",
    "iccv",
    "eccv",
    "wacv",
    "bmvc",
    "neurips",
    "nips",
    "iclr",
    "icml",
    "aaai",
    "ijcai",
    "acm multimedia",
    "mm ",
    "bmvc",
    "accv",
    "iros",
    "icra",
    "proceedings",
    "conference",
    "workshop",
    "symposium",
}


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class SearchResult:
    """Normalized lookup result across different backends."""

    title: str
    url: str | None = None
    year: int | None = None
    authors: list[str] = field(default_factory=list)
    venue: str | None = None
    work_type: str | None = None
    doi: str | None = None
    arxiv_id: str | None = None
    abstract: str | None = None
    source: str | None = None
    citation_count: int | None = None
    published_date: str | None = None
    relevance_note: str | None = None
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass
class LookupFilters:
    """Lookup filters shared across backends and post-processing."""

    year_from: int | None = None
    year_to: int | None = None
    recent_years: int | None = None
    quality: str = "any"
    work_type: str | None = None
    venue: str | None = None
    min_citations: int | None = None

    def resolved_year_from(self) -> int | None:
        """Resolve --recent-years into an effective lower publication year."""
        if self.year_from is not None:
            return self.year_from
        if self.recent_years is None:
            return None
        current_year = datetime.now().year
        return max(0, current_year - self.recent_years + 1)

    def resolved_year_to(self) -> int | None:
        """Resolve effective upper publication year."""
        return self.year_to


@dataclass
class LookupReport:
    """Structured lookup report."""

    query: str
    expanded_query: str
    mode: str
    backends: list[str]
    timestamp: str
    filters: LookupFilters
    boost_phrases: list[str]
    results: list[SearchResult]
    notes: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def _get_json(
    url: str,
    *,
    headers: dict[str, str] | None = None,
    timeout: int = 30,
) -> dict[str, Any]:
    """Fetch JSON from a URL using only the Python standard library."""
    request = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        raw = response.read().decode("utf-8")
    return json.loads(raw)


def _post_json(
    url: str,
    payload: dict[str, Any],
    *,
    headers: dict[str, str] | None = None,
    timeout: int = 90,
) -> dict[str, Any]:
    """POST JSON and return parsed JSON using only the Python standard library."""
    body = json.dumps(payload).encode("utf-8")
    request_headers = {"Content-Type": "application/json", **(headers or {})}
    request = urllib.request.Request(url, data=body, headers=request_headers, method="POST")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        raw = response.read().decode("utf-8")
    return json.loads(raw)


def _get_json_with_retry(
    url: str,
    *,
    headers: dict[str, str] | None = None,
    timeout: int = 30,
    retries: int = 2,
    base_sleep: float = 3.0,
) -> dict[str, Any]:
    """Fetch JSON with simple retry/backoff for transient rate limits.

    This is intentionally lightweight. The skill should not fail hard just
    because a public API temporarily rate-limits or stalls.
    """
    last_error: Exception | None = None

    for attempt in range(retries + 1):
        try:
            return _get_json(url, headers=headers, timeout=timeout)
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code == 429 and attempt < retries:
                time.sleep(base_sleep * (attempt + 1))
                continue
            raise
        except TimeoutError as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(base_sleep * (attempt + 1))
                continue
            raise
        except Exception as exc:
            last_error = exc
            message = str(exc).lower()
            if "timed out" in message and attempt < retries:
                time.sleep(base_sleep * (attempt + 1))
                continue
            raise

    raise RuntimeError(f"Request failed after retries: {last_error}")


def _urlopen_with_retry(
    request: urllib.request.Request,
    *,
    timeout: int = 15,
    retries: int = 1,
    base_sleep: float = 3.0,
):
    """Open URL with retry/backoff for transient 429 or timeout errors."""
    last_error: Exception | None = None

    for attempt in range(retries + 1):
        try:
            return urllib.request.urlopen(request, timeout=timeout)
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code == 429 and attempt < retries:
                time.sleep(base_sleep * (attempt + 1))
                continue
            raise
        except TimeoutError as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(base_sleep * (attempt + 1))
                continue
            raise
        except Exception as exc:
            last_error = exc
            message = str(exc).lower()
            if "timed out" in message and attempt < retries:
                time.sleep(base_sleep * (attempt + 1))
                continue
            raise

    raise RuntimeError(f"Request failed after retries: {last_error}")


def _safe_int(value: Any) -> int | None:
    """Convert value to int when possible."""
    try:
        if value is None:
            return None
        return int(value)
    except (TypeError, ValueError):
        return None


def _clean_text(value: str | None) -> str | None:
    """Normalize whitespace in optional text."""
    if not value:
        return None
    return re.sub(r"\s+", " ", value).strip()


def _dedupe_results(results: list[SearchResult]) -> list[SearchResult]:
    """Deduplicate results by DOI, arXiv ID, URL, or normalized title."""
    seen: set[str] = set()
    unique: list[SearchResult] = []

    for result in results:
        normalized_title = re.sub(r"\W+", "", result.title.lower())
        key = result.doi or result.arxiv_id or result.url or normalized_title
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(result)

    return unique

# ---------------------------------------------------------------------------
# Query expansion by mode
# ---------------------------------------------------------------------------

def build_mode_query(query: str, mode: str) -> str:
    """Add mode-specific context to the query without hiding the original intent."""
    query = query.strip()

    if mode == "prior-work":
        return f"{query}"

    if mode == "baseline-scout":
        return f"{query} baseline benchmark"

    if mode == "dataset-benchmark":
        return f"{query} dataset benchmark"

    if mode == "citation-candidates":
        return f"{query} citation source evidence paper"

    if mode == "technical-verification":
        return f"{query} official documentation technical reference"

    if mode == "recent-developments":
        return f"{query} recent latest arxiv benchmark"

    return query


# ---------------------------------------------------------------------------
# Filter helpers
# ---------------------------------------------------------------------------

def _build_openalex_filter(filters: LookupFilters) -> str | None:
    """Build OpenAlex filter query part."""
    parts: list[str] = []

    year_from = filters.resolved_year_from()
    year_to = filters.resolved_year_to()

    if year_from is not None:
        parts.append(f"from_publication_date:{year_from}-01-01")
    if year_to is not None:
        parts.append(f"to_publication_date:{year_to}-12-31")

    # OpenAlex work types are metadata-based and not always perfect.
    if filters.work_type:
        parts.append(f"type:{filters.work_type}")
    elif filters.quality == "journal":
        parts.append("type:article")
    elif filters.quality == "proceedings":
        parts.append("type:proceedings-article")
    elif filters.quality == "preprint":
        # OpenAlex may use "preprint" for some records.
        parts.append("type:preprint")

    if not parts:
        return None

    return ",".join(parts)


def _build_crossref_filter(filters: LookupFilters) -> str | None:
    """Build Crossref filter query part."""
    parts: list[str] = []

    year_from = filters.resolved_year_from()
    year_to = filters.resolved_year_to()

    if year_from is not None:
        parts.append(f"from-pub-date:{year_from}-01-01")
    if year_to is not None:
        parts.append(f"until-pub-date:{year_to}-12-31")

    if filters.work_type:
        parts.append(f"type:{filters.work_type}")
    elif filters.quality == "journal":
        parts.append("type:journal-article")
    elif filters.quality == "proceedings":
        parts.append("type:proceedings-article")

    if not parts:
        return None

    return ",".join(parts)


def _semantic_scholar_year_filter(filters: LookupFilters) -> str | None:
    """Build Semantic Scholar year filter value."""
    year_from = filters.resolved_year_from()
    year_to = filters.resolved_year_to()

    if year_from is not None and year_to is not None:
        return f"{year_from}-{year_to}"
    if year_from is not None:
        return f"{year_from}-"
    if year_to is not None:
        return f"-{year_to}"
    return None


def quality_matches(result: SearchResult, quality: str) -> bool:
    """Return whether a normalized result matches a quality preference.

    This is metadata-based and should be treated as a useful heuristic, not a
    perfect guarantee of peer-review status.
    """
    if quality == "any":
        return True

    source = (result.source or "").lower()
    venue = (result.venue or "").lower()
    work_type = (result.work_type or "").lower()

    if quality == "scholarly":
        return source in FREE_SCHOLARLY_BACKENDS

    if quality == "preprint":
        return (
            source == "arxiv"
            or "arxiv" in venue
            or result.arxiv_id is not None
            or "preprint" in work_type
            or "posted-content" in work_type
        )

    if quality == "journal":
        return (
            "journal" in venue
            or "journal-article" in work_type
            or work_type == "article"
        )

    if quality == "proceedings":
        return (
            "proceedings" in work_type
            or "proceedings-article" in work_type
            or any(token in venue for token in CONFERENCE_TOKENS)
        )

    if quality == "peer-reviewed":
        return quality_matches(result, "journal") or quality_matches(result, "proceedings")

    return True


def apply_filters(results: list[SearchResult], filters: LookupFilters) -> list[SearchResult]:
    """Apply normalized post-filters across backend results."""
    filtered: list[SearchResult] = []

    year_from = filters.resolved_year_from()
    year_to = filters.resolved_year_to()

    for result in results:
        if year_from is not None and result.year is not None and result.year < year_from:
            continue

        if year_to is not None and result.year is not None and result.year > year_to:
            continue

        if filters.venue:
            venue = (result.venue or "").lower()
            if filters.venue.lower() not in venue:
                continue

        if filters.min_citations is not None and result.citation_count is not None:
            if result.citation_count < filters.min_citations:
                continue

        if filters.work_type:
            work_type = (result.work_type or "").lower()
            if filters.work_type.lower() not in work_type:
                continue

        if not quality_matches(result, filters.quality):
            continue

        filtered.append(result)

    return filtered


def _query_terms(query: str) -> set[str]:
    """Extract useful query terms for lightweight relevance scoring."""
    stopwords = {
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "by",
        "for",
        "from",
        "in",
        "into",
        "is",
        "of",
        "on",
        "or",
        "the",
        "to",
        "using",
        "use",
        "with",
        "work",
        "works",
        "paper",
        "papers",
        "prior",
        "related",
        "method",
        "methods",
        "survey",
        "benchmark",
        "computer",
        "vision",
        "deep",
        "learning",
        "machine",
        "model",
        "models",
    }
    tokens = re.findall(r"[a-zA-Z0-9]+", query.lower())
    return {token for token in tokens if len(token) > 2 and token not in stopwords}


def relevance_score(
    result: SearchResult,
    query: str,
    *,
    boost_phrases: list[str] | None = None,
) -> int:
    """Score result relevance using generic query overlap and optional boosts.

    This function is intentionally domain-agnostic. It does not hardcode road
    damage, medical imaging, remote sensing, or any other specific AI/CV domain.

    Use --boost-phrase to prioritize project-specific phrases when needed.
    """
    terms = _query_terms(query)

    title = (result.title or "").lower()
    abstract = (result.abstract or "").lower()
    venue = (result.venue or "").lower()
    work_type = (result.work_type or "").lower()
    combined = f"{title} {abstract} {venue} {work_type}"

    score = 0

    for term in terms:
        if term in title:
            score += 5
        if term in abstract:
            score += 2
        if term in venue:
            score += 1
        if term in work_type:
            score += 1

    if boost_phrases:
        for phrase in boost_phrases:
            phrase_lower = phrase.lower().strip()
            if not phrase_lower:
                continue

            if phrase_lower in title:
                score += 12
            elif phrase_lower in combined:
                score += 6

    return score


def filter_low_relevance(
    results: list[SearchResult],
    query: str,
    *,
    boost_phrases: list[str] | None = None,
    min_score: int = 2,
) -> list[SearchResult]:
    """Remove results that barely match the query.

    The filter is intentionally light. It avoids obvious drift while preserving
    broad AI/CV usability.
    """
    terms = _query_terms(query)
    if not terms and not boost_phrases:
        return results

    kept = [
        result
        for result in results
        if relevance_score(result, query, boost_phrases=boost_phrases) >= min_score
    ]

    return kept


def rank_results(
    results: list[SearchResult],
    filters: LookupFilters,
    query: str,
    *,
    boost_phrases: list[str] | None = None,
) -> list[SearchResult]:
    """Rank results by relevance first, then quality, recency, and citations."""
    year_from = filters.resolved_year_from()

    def score(result: SearchResult) -> tuple[int, int, int, int]:
        relevance = relevance_score(result, query, boost_phrases=boost_phrases)
        quality_score = 1 if quality_matches(result, filters.quality) else 0
        citation_score = result.citation_count or 0
        year_score = result.year or 0

        if year_from is not None:
            return (relevance, quality_score, year_score, citation_score)

        return (relevance, quality_score, citation_score, year_score)

    return sorted(results, key=score, reverse=True)


# ---------------------------------------------------------------------------
# Free scholarly backends
# ---------------------------------------------------------------------------

def search_openalex(
    query: str,
    *,
    limit: int,
    filters: LookupFilters,
    title_search: bool = False,
) -> list[SearchResult]:
    """Search OpenAlex works API."""
    encoded = urllib.parse.quote(query)
    search_param = "search.title" if title_search else "search"
    url = (
        "https://api.openalex.org/works"
        f"?{search_param}={encoded}"
        f"&per-page={limit}"
        "&sort=relevance_score:desc"
    )

    filter_value = _build_openalex_filter(filters)
    if filter_value:
        url += "&filter=" + urllib.parse.quote(filter_value, safe=":,/-")

    data = _get_json(url)
    results: list[SearchResult] = []

    for item in data.get("results", []):
        title = _clean_text(item.get("title")) or "Untitled"

        authors = []
        for authorship in item.get("authorships", [])[:8]:
            author = authorship.get("author", {}).get("display_name")
            if author:
                authors.append(author)

        primary_location = item.get("primary_location") or {}
        source_info = primary_location.get("source") or {}

        doi = item.get("doi")
        if doi and doi.startswith("https://doi.org/"):
            doi = doi.replace("https://doi.org/", "")

        abstract = _openalex_abstract(item.get("abstract_inverted_index"))

        results.append(
            SearchResult(
                title=title,
                url=item.get("id") or item.get("doi"),
                year=_safe_int(item.get("publication_year")),
                authors=authors,
                venue=source_info.get("display_name"),
                work_type=item.get("type"),
                doi=doi,
                abstract=abstract,
                source="openalex",
                citation_count=_safe_int(item.get("cited_by_count")),
                published_date=item.get("publication_date"),
                raw=item,
            )
        )

    return results


def _openalex_abstract(inverted_index: dict[str, list[int]] | None) -> str | None:
    """Convert OpenAlex inverted abstract index into readable text."""
    if not inverted_index:
        return None

    positions: list[tuple[int, str]] = []
    for word, indices in inverted_index.items():
        for index in indices:
            positions.append((index, word))

    words = [word for _, word in sorted(positions)]
    return _clean_text(" ".join(words))


def search_arxiv(query: str, *, limit: int, filters: LookupFilters) -> list[SearchResult]:
    """Search arXiv API.

    arXiv returns Atom XML, parsed with the standard library.
    """
    import xml.etree.ElementTree as ET

    encoded = urllib.parse.quote(query)
    sort_by = "submittedDate" if filters.quality == "preprint" or filters.resolved_year_from() else "relevance"
    url = (
        "http://export.arxiv.org/api/query"
        f"?search_query=all:{encoded}"
        f"&start=0"
        f"&max_results={limit}"
        f"&sortBy={sort_by}"
        "&sortOrder=descending"
    )

    request = urllib.request.Request(url, headers={"User-Agent": "research-lookup-skill/1.0"})
    with _urlopen_with_retry(request, timeout=10, retries=1, base_sleep=3.0) as response:
        raw = response.read().decode("utf-8")

    root = ET.fromstring(raw)
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    results: list[SearchResult] = []

    for entry in root.findall("atom:entry", ns):
        title = _clean_text(entry.findtext("atom:title", default="", namespaces=ns)) or "Untitled"
        summary = _clean_text(entry.findtext("atom:summary", default="", namespaces=ns))
        published = entry.findtext("atom:published", default="", namespaces=ns)
        link = entry.findtext("atom:id", default="", namespaces=ns)

        authors = [
            _clean_text(author.findtext("atom:name", default="", namespaces=ns)) or ""
            for author in entry.findall("atom:author", ns)
        ]
        authors = [author for author in authors if author]

        arxiv_id = None
        if link:
            arxiv_id = link.rstrip("/").split("/")[-1]

        year = None
        if published:
            year = _safe_int(published[:4])

        results.append(
            SearchResult(
                title=title,
                url=link or None,
                year=year,
                authors=authors[:8],
                venue="arXiv",
                work_type="preprint",
                arxiv_id=arxiv_id,
                abstract=summary,
                source="arxiv",
                published_date=published[:10] if published else None,
                raw={"entry_xml": ET.tostring(entry, encoding="unicode")},
            )
        )

    # Be polite to arXiv if called repeatedly.
    time.sleep(1.00)
    return results


def search_crossref(query: str, *, limit: int, filters: LookupFilters) -> list[SearchResult]:
    """Search Crossref works API."""
    encoded = urllib.parse.quote(query)
    url = (
        "https://api.crossref.org/works"
        f"?query={encoded}"
        f"&rows={limit}"
    )

    filter_value = _build_crossref_filter(filters)
    if filter_value:
        url += "&filter=" + urllib.parse.quote(filter_value, safe=":,/-")

    data = _get_json(url, headers={"User-Agent": "research-lookup-skill/1.0"})
    items = data.get("message", {}).get("items", [])

    results: list[SearchResult] = []

    for item in items:
        title_list = item.get("title") or []
        title = _clean_text(title_list[0] if title_list else None) or "Untitled"

        authors = []
        for author in item.get("author", [])[:8]:
            given = author.get("given", "")
            family = author.get("family", "")
            name = _clean_text(f"{given} {family}")
            if name:
                authors.append(name)

        year = None
        date_parts = (
            item.get("published-print", {}).get("date-parts")
            or item.get("published-online", {}).get("date-parts")
            or item.get("published", {}).get("date-parts")
            or item.get("created", {}).get("date-parts")
            or []
        )
        if date_parts and date_parts[0]:
            year = _safe_int(date_parts[0][0])

        doi = item.get("DOI")
        url_value = item.get("URL") or (f"https://doi.org/{doi}" if doi else None)

        container = item.get("container-title") or []
        venue = container[0] if container else None

        results.append(
            SearchResult(
                title=title,
                url=url_value,
                year=year,
                authors=authors,
                venue=venue,
                work_type=item.get("type"),
                doi=doi,
                source="crossref",
                citation_count=_safe_int(item.get("is-referenced-by-count")),
                raw=item,
            )
        )

    return results


def search_semantic_scholar(query: str, *, limit: int, filters: LookupFilters) -> list[SearchResult]:
    """Search Semantic Scholar Graph API.

    API key is optional for light use. If SEMANTIC_SCHOLAR_API_KEY is present,
    it is sent as x-api-key.
    """
    encoded = urllib.parse.quote(query)
    fields = ",".join(
        [
            "title",
            "url",
            "year",
            "authors",
            "venue",
            "abstract",
            "citationCount",
            "externalIds",
            "publicationTypes",
            "publicationDate",
        ]
    )
    url = (
        "https://api.semanticscholar.org/graph/v1/paper/search"
        f"?query={encoded}"
        f"&limit={limit}"
        f"&fields={fields}"
    )

    year_filter = _semantic_scholar_year_filter(filters)
    if year_filter:
        url += f"&year={urllib.parse.quote(year_filter)}"

    headers = {"User-Agent": "research-lookup-skill/1.0"}
    api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
    if api_key:
        headers["x-api-key"] = api_key

    data = _get_json_with_retry(
        url,
        headers=headers,
        timeout=15,
        retries=1,
        base_sleep=5.0,
    )
    results: list[SearchResult] = []

    for item in data.get("data", []):
        external_ids = item.get("externalIds") or {}
        doi = external_ids.get("DOI")
        arxiv_id = external_ids.get("ArXiv")

        authors = [
            author.get("name", "")
            for author in item.get("authors", [])[:8]
            if author.get("name")
        ]

        publication_types = item.get("publicationTypes") or []
        work_type = ", ".join(publication_types) if publication_types else None

        results.append(
            SearchResult(
                title=_clean_text(item.get("title")) or "Untitled",
                url=item.get("url"),
                year=_safe_int(item.get("year")),
                authors=authors,
                venue=item.get("venue"),
                work_type=work_type,
                doi=doi,
                arxiv_id=arxiv_id,
                abstract=_clean_text(item.get("abstract")),
                source="semantic-scholar",
                citation_count=_safe_int(item.get("citationCount")),
                published_date=item.get("publicationDate"),
                raw=item,
            )
        )

    return results


# ---------------------------------------------------------------------------
# Optional paid/synthesis backends
# ---------------------------------------------------------------------------

def search_parallel(query: str, *, limit: int, filters: LookupFilters) -> list[SearchResult]:
    """Use Parallel Chat API as optional synthesis fallback.

    Returns a single synthetic SearchResult containing the generated report.
    """
    api_key = os.getenv("PARALLEL_API_KEY")
    if not api_key:
        raise RuntimeError("PARALLEL_API_KEY is not set")

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("The 'openai' package is required for Parallel backend") from exc

    filter_text = _filters_to_prompt(filters)

    client = OpenAI(api_key=api_key, base_url="https://api.parallel.ai")
    response = client.chat.completions.create(
        model="core",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a research lookup assistant. Provide concise, source-aware "
                    "findings for the query. Prioritize primary sources, official pages, "
                    "paper pages, benchmark pages, and recent evidence. Do not invent citations."
                ),
            },
            {"role": "user", "content": f"Query: {query}\n\nFilters:\n{filter_text}"},
        ],
        stream=False,
    )

    content = ""
    if response.choices:
        content = response.choices[0].message.content or ""

    return [
        SearchResult(
            title="Parallel synthesis result",
            abstract=content,
            source="parallel",
            raw={"model": "parallel-chat/core", "filters": asdict(filters)},
        )
    ][:limit]


def search_perplexity(query: str, *, limit: int, filters: LookupFilters) -> list[SearchResult]:
    """Use Perplexity sonar-pro-search via OpenRouter as optional fallback."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY is not set")

    filter_text = _filters_to_prompt(filters)

    payload = {
        "model": "perplexity/sonar-pro-search",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an academic search assistant. Find relevant scholarly sources, "
                    "baselines, datasets, benchmarks, and citations. Prefer primary sources. "
                    "Do not invent papers, DOIs, venues, or results."
                ),
            },
            {"role": "user", "content": f"Query: {query}\n\nFilters:\n{filter_text}"},
        ],
        "max_tokens": 4000,
        "temperature": 0.1,
        "search_mode": "academic",
        "search_context_size": "high",
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://research-lookup.local",
        "X-Title": "Research Lookup Skill",
    }

    data = _post_json("https://openrouter.ai/api/v1/chat/completions", payload, headers=headers)
    choices = data.get("choices", [])
    content = ""
    if choices:
        content = choices[0].get("message", {}).get("content", "")

    results = [
        SearchResult(
            title="Perplexity synthesis result",
            abstract=content,
            source="perplexity",
            raw={"model": "perplexity/sonar-pro-search", "usage": data.get("usage", {}), "filters": asdict(filters)},
        )
    ]

    search_results = data.get("search_results", [])
    for item in search_results[:limit]:
        results.append(
            SearchResult(
                title=item.get("title") or "Untitled source",
                url=item.get("url"),
                published_date=item.get("date"),
                abstract=item.get("snippet"),
                source="perplexity",
                raw=item,
            )
        )

    return results[:limit]


def _filters_to_prompt(filters: LookupFilters) -> str:
    """Format filters for synthesis backends."""
    values = []
    year_from = filters.resolved_year_from()
    year_to = filters.resolved_year_to()

    if year_from is not None:
        values.append(f"- Publication year from: {year_from}")
    if year_to is not None:
        values.append(f"- Publication year to: {year_to}")
    if filters.quality != "any":
        values.append(f"- Quality preference: {filters.quality}")
    if filters.work_type:
        values.append(f"- Work type: {filters.work_type}")
    if filters.venue:
        values.append(f"- Venue contains: {filters.venue}")
    if filters.min_citations is not None:
        values.append(f"- Minimum citations: {filters.min_citations}")

    if not values:
        return "- No explicit filters."

    values.append("- Treat filters as preferences when metadata is incomplete.")
    return "\n".join(values)


# ---------------------------------------------------------------------------
# Backend selection and lookup orchestration
# ---------------------------------------------------------------------------

def select_backends(mode: str, requested_backend: str, filters: LookupFilters) -> list[str]:
    """Select backends for a lookup mode.

    Defaults prefer stable/free APIs. Rate-limited APIs such as Semantic Scholar
    are used only when explicitly requested or when an API key is configured.
    """
    if requested_backend != "auto":
        return [requested_backend]

    has_semantic_key = bool(os.getenv("SEMANTIC_SCHOLAR_API_KEY"))
    has_parallel_key = bool(os.getenv("PARALLEL_API_KEY"))
    has_openrouter_key = bool(os.getenv("OPENROUTER_API_KEY"))

    if mode == "prior-work":
        if filters.quality == "preprint":
            return ["arxiv", "openalex"]
        return ["openalex", "arxiv"]

    if mode == "baseline-scout":
        backends = ["openalex", "arxiv"]
        if has_semantic_key:
            backends.append("semantic-scholar")
        return backends

    if mode == "dataset-benchmark":
        backends = ["openalex"]
        if has_semantic_key:
            backends.append("semantic-scholar")
        if has_parallel_key:
            backends.append("parallel")
        elif has_openrouter_key:
            backends.append("perplexity")
        return backends

    if mode == "citation-candidates":
        backends = ["openalex", "crossref"]
        if has_semantic_key:
            backends.append("semantic-scholar")
        return backends

    if mode == "technical-verification":
        backends = ["crossref", "openalex"]
        if has_parallel_key:
            backends.append("parallel")
        elif has_openrouter_key:
            backends.append("perplexity")
        return backends

    if mode == "recent-developments":
        backends = ["arxiv", "openalex"]
        if has_semantic_key:
            backends.append("semantic-scholar")
        return backends

    return ["openalex"]


def run_backend(
    backend: str,
    query: str,
    *,
    limit: int,
    filters: LookupFilters,
) -> list[SearchResult]:
    """Run one backend."""
    if backend == "openalex":
        title_search = filters.quality != "any" or False
        return search_openalex(query, limit=limit, filters=filters, title_search=title_search)
    if backend == "arxiv":
        return search_arxiv(query, limit=limit, filters=filters)
    if backend == "crossref":
        return search_crossref(query, limit=limit, filters=filters)
    if backend == "semantic-scholar":
        return search_semantic_scholar(query, limit=limit, filters=filters)
    if backend == "parallel":
        return search_parallel(query, limit=limit, filters=filters)
    if backend == "perplexity":
        return search_perplexity(query, limit=limit, filters=filters)

    raise ValueError(f"Unknown backend: {backend}")


def lookup(
    query: str,
    *,
    mode: str,
    backend: str,
    limit: int,
    filters: LookupFilters,
    boost_phrases: list[str] | None = None,
) -> LookupReport:
    """Run research lookup and return a structured report."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expanded_query = build_mode_query(query, mode)
    backends = select_backends(mode, backend, filters)
    boost_phrases = boost_phrases or []

    all_results: list[SearchResult] = []
    errors: list[str] = []
    notes: list[str] = []

    backend_limit = max(limit, min(limit * 2, 50))

    for selected_backend in backends:
        try:
            print(
                f"[research-lookup] backend={selected_backend} mode={mode} query={expanded_query[:90]}...",
                file=sys.stderr,
            )
            backend_results = run_backend(
                selected_backend,
                expanded_query,
                limit=backend_limit,
                filters=filters,
            )
            all_results.extend(backend_results)
        except Exception as exc:
            message = f"{selected_backend}: {exc}"
            errors.append(message)
            print(f"[research-lookup] warning: {message}", file=sys.stderr)

    deduped = _dedupe_results(all_results)
    filtered = apply_filters(deduped, filters)
    relevant = filter_low_relevance(
        filtered,
        query,
        boost_phrases=boost_phrases,
        min_score=2,
    )
    ranked = rank_results(
        relevant,
        filters,
        query,
        boost_phrases=boost_phrases,
    )
    results = ranked[:limit]

    if not results and deduped:
        notes.append(
            "Backend results were found, but all were removed by filters or low-relevance ranking. "
            "Try relaxing --quality, --venue, --min-citations, year filters, or use --boost-phrase for domain focus."
        )

    if not results and not deduped:
        notes.append("No results returned. Try a narrower or broader query, or use a different backend.")

    if filters.quality in {"peer-reviewed", "journal", "proceedings"}:
        notes.append(
            "Quality filters are metadata-based heuristics. Verify venue and peer-review status before using results as evidence."
        )

    return LookupReport(
        query=query,
        expanded_query=expanded_query,
        mode=mode,
        backends=backends,
        timestamp=timestamp,
        filters=filters,
        boost_phrases=boost_phrases,
        results=results,
        notes=notes,
        errors=errors,
    )


# ---------------------------------------------------------------------------
# Formatting and saving
# ---------------------------------------------------------------------------

def default_output_path(query: str, mode: str, *, suffix: str = "md") -> Path:
    """Create default sources/ output path."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", query.lower()).strip("_")[:60] or "lookup"

    prefix_by_mode = {
        "prior-work": "papers",
        "baseline-scout": "baselines",
        "dataset-benchmark": "datasets",
        "citation-candidates": "citations",
        "technical-verification": "technical",
        "recent-developments": "recent",
    }
    prefix = prefix_by_mode.get(mode, "research")

    return Path("sources") / f"{prefix}_{timestamp}_{slug}.{suffix}"


def format_markdown(report: LookupReport) -> str:
    """Format lookup report as markdown."""
    lines: list[str] = []

    lines.append("# Research Lookup Result")
    lines.append("")
    lines.append(f"- Query: `{report.query}`")
    lines.append(f"- Expanded query: `{report.expanded_query}`")
    lines.append(f"- Mode: `{report.mode}`")
    lines.append(f"- Backends: `{', '.join(report.backends)}`")
    lines.append(f"- Timestamp: `{report.timestamp}`")
    lines.append(f"- Results: `{len(report.results)}`")
    if report.boost_phrases:
        lines.append(f"- Boost phrases: `{', '.join(report.boost_phrases)}`")
    lines.append("")

    lines.append("## Filters")
    lines.append("")
    filters = report.filters
    filter_rows = [
        ("year_from", filters.resolved_year_from()),
        ("year_to", filters.resolved_year_to()),
        ("recent_years", filters.recent_years),
        ("quality", filters.quality),
        ("work_type", filters.work_type),
        ("venue", filters.venue),
        ("min_citations", filters.min_citations),
    ]
    for key, value in filter_rows:
        if value is not None and value != "any":
            lines.append(f"- {key}: `{value}`")
    if all(value is None or value == "any" for _, value in filter_rows):
        lines.append("- No explicit filters.")
    lines.append("")

    if report.notes:
        lines.append("## Notes")
        lines.append("")
        for note in report.notes:
            lines.append(f"- {note}")
        lines.append("")

    if report.errors:
        lines.append("## Backend Warnings")
        lines.append("")
        for error in report.errors:
            lines.append(f"- {error}")
        lines.append("")

    lines.append("## Results")
    lines.append("")

    for index, result in enumerate(report.results, start=1):
        lines.append(f"### {index}. {result.title}")
        lines.append("")
        metadata = []
        if result.year:
            metadata.append(str(result.year))
        if result.venue:
            metadata.append(result.venue)
        if result.work_type:
            metadata.append(f"type: {result.work_type}")
        if result.source:
            metadata.append(f"source: {result.source}")
        if result.citation_count is not None:
            metadata.append(f"citations: {result.citation_count}")

        if metadata:
            lines.append(f"- Metadata: {', '.join(metadata)}")

        if result.authors:
            author_text = ", ".join(result.authors[:8])
            if len(result.authors) > 8:
                author_text += ", et al."
            lines.append(f"- Authors: {author_text}")

        if result.doi:
            lines.append(f"- DOI: `{result.doi}`")

        if result.arxiv_id:
            lines.append(f"- arXiv: `{result.arxiv_id}`")

        if result.url:
            lines.append(f"- URL: {result.url}")

        if result.published_date:
            lines.append(f"- Date: {result.published_date}")

        if result.abstract:
            abstract = result.abstract
            if len(abstract) > 1200:
                abstract = abstract[:1200].rstrip() + "..."
            lines.append("")
            lines.append(abstract)

        lines.append("")

    lines.append("## Suggested Next Step")
    lines.append("")
    lines.append(_suggest_next_step(report.mode))
    lines.append("")

    return "\n".join(lines)


def _suggest_next_step(mode: str) -> str:
    """Suggest the next downstream skill."""
    if mode in {"prior-work", "recent-developments"}:
        return "Use `literature-review` to synthesize these sources into themes, gaps, and closest-prior-work comparisons."
    if mode == "baseline-scout":
        return "Use `scientific-critical-thinking` or `peer-review` to decide which baselines are essential versus optional."
    if mode == "dataset-benchmark":
        return "Use the Dataset and Leakage Gate before changing dataset assumptions or evaluation protocols."
    if mode == "citation-candidates":
        return "Use `citation-management` to verify BibTeX/DOI metadata before inserting citations."
    if mode == "technical-verification":
        return "Prefer primary documentation before changing code or technical claims."
    return "Review the saved lookup artifact before using it as evidence."


def save_report(
    report: LookupReport,
    *,
    markdown_path: Path | None,
    json_path: Path | None,
) -> tuple[Path | None, Path | None]:
    """Save report as markdown and/or JSON."""
    saved_md = None
    saved_json = None

    if markdown_path:
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_path.write_text(format_markdown(report), encoding="utf-8")
        saved_md = markdown_path

    if json_path:
        json_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "query": report.query,
            "expanded_query": report.expanded_query,
            "mode": report.mode,
            "backends": report.backends,
            "timestamp": report.timestamp,
            "filters": asdict(report.filters),
            "boost_phrases": report.boost_phrases,
            "notes": report.notes,
            "errors": report.errors,
            "results": [asdict(result) for result in report.results],
        }
        json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        saved_json = json_path

    return saved_md, saved_json


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Agentic research lookup tool with free scholarly API support.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/research_lookup.py "road damage detection computer vision" --mode prior-work

  python scripts/research_lookup.py "road damage detection YOLO benchmark mAP" \\
    --mode baseline-scout --limit 15 --out sources/baselines_road_damage.md

  python scripts/research_lookup.py "road crack detection dataset annotation protocol" \\
    --mode dataset-benchmark --backend auto

  python scripts/research_lookup.py "domain shift in computer vision evaluation" \\
    --mode citation-candidates --json-out sources/citations_domain_shift.json

  python scripts/research_lookup.py "road damage detection object detection benchmark" \\
    --mode recent-developments --recent-years 3 --quality peer-reviewed --limit 20

  python scripts/research_lookup.py "small object detection road damage detection" \\
    --mode baseline-scout --year-from 2020 --quality proceedings --limit 20
  
  python scripts/research_lookup.py "YOLO benchmark object detection" --mode baseline-scout \\
    --boost-phrase "road damage" --boost-phrase "pavement distress" --limit 10
        """,
    )

    parser.add_argument("query", help="Research lookup query.")
    parser.add_argument(
        "--mode",
        choices=sorted(VALID_MODES),
        default="prior-work",
        help="Lookup mode. Default: prior-work.",
    )
    parser.add_argument(
        "--backend",
        choices=sorted(VALID_BACKENDS),
        default="auto",
        help="Backend to use. Default: auto.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_LIMIT,
        help=f"Maximum normalized results to keep. Default: {DEFAULT_LIMIT}.",
    )
    parser.add_argument(
        "--year-from",
        type=int,
        default=None,
        help="Keep or prefer works published from this year onward.",
    )
    parser.add_argument(
        "--year-to",
        type=int,
        default=None,
        help="Keep or prefer works published up to this year.",
    )
    parser.add_argument(
        "--recent-years",
        type=int,
        default=None,
        help="Shortcut for filtering to works from the last N years.",
    )
    parser.add_argument(
        "--quality",
        choices=sorted(VALID_QUALITY_LEVELS),
        default="any",
        help=(
            "Metadata-based quality preference/filter. "
            "Use peer-reviewed, journal, proceedings, or preprint when needed. Default: any."
        ),
    )
    parser.add_argument(
        "--work-type",
        default=None,
        help="Backend-specific work type filter/preference, such as article or proceedings-article.",
    )
    parser.add_argument(
        "--venue",
        default=None,
        help="Keep results whose venue contains this text, such as CVPR, ICCV, ECCV, NeurIPS, or journal name.",
    )
    parser.add_argument(
        "--min-citations",
        type=int,
        default=None,
        help="Keep results with at least this many citations when citation metadata is available.",
    )
    parser.add_argument(
        "--boost-phrase",
        action="append",
        default=None,
        help=(
            "Optional phrase to boost in relevance ranking. "
            "Can be used multiple times, for example: "
            '--boost-phrase "road damage" --boost-phrase "pavement distress".'
        ),
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Markdown output path. Defaults to sources/<mode>_<timestamp>_<query>.md unless --no-save is set.",
    )
    parser.add_argument(
        "--json-out",
        type=Path,
        default=None,
        help="Optional JSON output path.",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Print markdown to stdout instead of saving by default.",
    )
    parser.add_argument(
        "--print",
        action="store_true",
        help="Also print markdown output to stdout after saving.",
    )

    return parser.parse_args(argv)


def _validate_args(args: argparse.Namespace) -> str | None:
    """Return validation error message, if any."""
    if args.limit < 1:
        return "--limit must be >= 1"

    if args.year_from is not None and args.year_from < 0:
        return "--year-from must be a positive year"

    if args.year_to is not None and args.year_to < 0:
        return "--year-to must be a positive year"

    if args.year_from is not None and args.year_to is not None and args.year_from > args.year_to:
        return "--year-from cannot be greater than --year-to"

    if args.recent_years is not None and args.recent_years < 1:
        return "--recent-years must be >= 1"

    if args.min_citations is not None and args.min_citations < 0:
        return "--min-citations must be >= 0"

    return None


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = parse_args(argv)
    validation_error = _validate_args(args)

    if validation_error:
        print(f"Error: {validation_error}", file=sys.stderr)
        return 1

    filters = LookupFilters(
        year_from=args.year_from,
        year_to=args.year_to,
        recent_years=args.recent_years,
        quality=args.quality,
        work_type=args.work_type,
        venue=args.venue,
        min_citations=args.min_citations,
    )

    report = lookup(
        args.query,
        mode=args.mode,
        backend=args.backend,
        limit=args.limit,
        filters=filters,
        boost_phrases=args.boost_phrase or [],
    )

    markdown_path: Path | None = None
    json_path: Path | None = args.json_out

    if not args.no_save:
        markdown_path = args.out or default_output_path(args.query, args.mode, suffix="md")
    elif args.out:
        markdown_path = args.out

    saved_md, saved_json = save_report(report, markdown_path=markdown_path, json_path=json_path)

    markdown = format_markdown(report)

    if args.no_save or args.print:
        print(markdown)

    if saved_md:
        print(f"[research-lookup] saved markdown: {saved_md}", file=sys.stderr)
    if saved_json:
        print(f"[research-lookup] saved json: {saved_json}", file=sys.stderr)

    if not report.results:
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
