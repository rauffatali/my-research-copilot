#!/usr/bin/env python3
"""Extract and normalize citation metadata.

This script supports the citation-management skill.

It extracts metadata from:
- DOI values
- arXiv IDs or URLs
- BibTeX files
- plain text reference strings
- URL lists

It can optionally verify DOI metadata through Crossref and arXiv metadata
through the arXiv API.

This script is not a broad literature discovery tool. Use research-lookup for
finding candidate papers and sources.

Examples:
    python scripts/extract_metadata.py --doi 10.1109/CVPR.2016.91

    python scripts/extract_metadata.py --arxiv 2304.02643

    python scripts/extract_metadata.py --bib paper/references.bib --output metadata.json

    python scripts/extract_metadata.py --text references.txt --format markdown
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class MetadataRecord:
    """Normalized metadata record."""

    source_input: str
    source_type: str
    status: str
    title: str | None = None
    authors: list[str] = field(default_factory=list)
    year: int | None = None
    date: str | None = None
    venue: str | None = None
    entry_type: str | None = None
    doi: str | None = None
    arxiv_id: str | None = None
    url: str | None = None
    abstract: str | None = None
    publisher: str | None = None
    version: str | None = None
    citation_key: str | None = None
    message: str | None = None
    raw: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Normalization helpers
# ---------------------------------------------------------------------------

def normalize_doi(value: str | None) -> str | None:
    """Normalize DOI from raw DOI, URL, or prefixed string."""
    if not value:
        return None
    doi = value.strip().strip("<>.,; ")
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.IGNORECASE)
    doi = re.sub(r"^DOI\s+", "", doi, flags=re.IGNORECASE)
    doi = doi.strip().rstrip(".")
    if re.match(r"^10\.\d{4,9}/\S+$", doi):
        return doi
    return None


def normalize_arxiv_id(value: str | None) -> str | None:
    """Normalize arXiv identifier from ID or URL."""
    if not value:
        return None
    text = value.strip().strip("<>.,; ")
    text = re.sub(r"^arXiv:\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^https?://arxiv\.org/(abs|pdf)/", "", text, flags=re.IGNORECASE)
    text = text.replace(".pdf", "")
    text = text.strip()
    if re.match(r"^\d{4}\.\d{4,5}(v\d+)?$|^[a-z-]+(\.[A-Z]{2})?/\d{7}(v\d+)?$", text, re.IGNORECASE):
        return text
    return None


def normalize_title(value: str | None) -> str:
    """Normalize title for comparison or key generation."""
    if not value:
        return ""
    text = re.sub(r"[{}\\]", "", value.lower())
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def safe_year(value: Any) -> int | None:
    """Parse year safely."""
    try:
        if value is None:
            return None
        text = str(value)
        match = re.search(r"\b(19|20)\d{2}\b", text)
        if not match:
            return None
        return int(match.group(0))
    except Exception:
        return None


def make_citation_key(authors: list[str], year: int | None, title: str | None) -> str | None:
    """Generate a simple candidate citation key."""
    if not authors and not title:
        return None

    first = "unknown"
    if authors:
        first_author = authors[0]
        # Handle either "Family, Given" or "Given Family".
        if "," in first_author:
            first = first_author.split(",", 1)[0]
        else:
            parts = first_author.split()
            first = parts[-1] if parts else first_author

    first = re.sub(r"[^A-Za-z0-9]+", "", first).lower() or "unknown"
    year_part = str(year) if year else "nd"

    keyword = ""
    title_norm = normalize_title(title)
    stopwords = {
        "the", "and", "for", "with", "from", "using", "based", "towards",
        "toward", "learning", "deep", "machine", "study", "approach",
        "method", "methods", "analysis", "review"
    }
    for token in title_norm.split():
        if len(token) > 3 and token not in stopwords:
            keyword = token
            break

    return f"{first}{year_part}{keyword}"


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def http_get(url: str, *, headers: dict[str, str] | None = None, timeout: int = 20, retries: int = 1) -> bytes:
    """GET URL with lightweight retry."""
    request = urllib.request.Request(url, headers=headers or {})
    last_error: Exception | None = None

    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code in {429, 500, 502, 503, 504} and attempt < retries:
                time.sleep(2.0 * (attempt + 1))
                continue
            raise
        except Exception as exc:
            last_error = exc
            if "timed out" in str(exc).lower() and attempt < retries:
                time.sleep(2.0 * (attempt + 1))
                continue
            raise

    raise RuntimeError(f"Request failed after retries: {last_error}")


# ---------------------------------------------------------------------------
# Crossref and arXiv extraction
# ---------------------------------------------------------------------------

def extract_from_doi(value: str) -> MetadataRecord:
    """Extract metadata from DOI via Crossref."""
    doi = normalize_doi(value)
    if not doi:
        return MetadataRecord(
            source_input=value,
            source_type="doi",
            status="invalid_doi",
            message="Input is not a valid DOI.",
        )

    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}"
    try:
        raw = http_get(url, headers={"User-Agent": "citation-management-extract-metadata/1.0"})
        data = json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return MetadataRecord(
                source_input=value,
                source_type="doi",
                status="not_found",
                doi=doi,
                message="DOI not found in Crossref.",
            )
        return MetadataRecord(
            source_input=value,
            source_type="doi",
            status="error",
            doi=doi,
            message=f"Crossref HTTP error: {exc}",
        )
    except Exception as exc:
        return MetadataRecord(
            source_input=value,
            source_type="doi",
            status="error",
            doi=doi,
            message=f"Crossref lookup failed: {exc}",
        )

    message = data.get("message", {})
    titles = message.get("title") or []
    title = titles[0] if titles else None
    authors = crossref_authors(message)
    year = crossref_year(message)
    venue = crossref_venue(message)
    entry_type = crossref_to_bibtex_type(message.get("type"))
    publisher = message.get("publisher")
    resolved_url = message.get("URL") or f"https://doi.org/{doi}"

    return MetadataRecord(
        source_input=value,
        source_type="doi",
        status="verified",
        title=title,
        authors=authors,
        year=year,
        date=crossref_date(message),
        venue=venue,
        entry_type=entry_type,
        doi=doi,
        url=resolved_url,
        publisher=publisher,
        citation_key=make_citation_key(authors, year, title),
        raw=message,
    )


def crossref_authors(metadata: dict[str, Any]) -> list[str]:
    """Extract Crossref authors."""
    authors: list[str] = []
    for author in metadata.get("author", []) or []:
        given = author.get("given", "")
        family = author.get("family", "")
        if family and given:
            authors.append(f"{family}, {given}")
        elif family:
            authors.append(family)
        elif given:
            authors.append(given)
    return authors


def crossref_year(metadata: dict[str, Any]) -> int | None:
    """Extract Crossref year."""
    for field_name in ["published-print", "published-online", "published", "created"]:
        parts = metadata.get(field_name, {}).get("date-parts")
        if parts and parts[0]:
            return safe_year(parts[0][0])
    return None


def crossref_date(metadata: dict[str, Any]) -> str | None:
    """Extract Crossref date as YYYY-MM-DD-ish string."""
    for field_name in ["published-print", "published-online", "published", "created"]:
        parts = metadata.get(field_name, {}).get("date-parts")
        if parts and parts[0]:
            nums = [str(part).zfill(2) if idx > 0 else str(part) for idx, part in enumerate(parts[0])]
            return "-".join(nums)
    return None


def crossref_venue(metadata: dict[str, Any]) -> str | None:
    """Extract Crossref venue."""
    container = metadata.get("container-title") or []
    if container:
        return container[0]
    return metadata.get("publisher")


def crossref_to_bibtex_type(crossref_type: str | None) -> str | None:
    """Map Crossref type to BibTeX type."""
    mapping = {
        "journal-article": "article",
        "proceedings-article": "inproceedings",
        "book-chapter": "incollection",
        "book": "book",
        "posted-content": "misc",
        "report": "techreport",
        "dataset": "dataset",
    }
    if not crossref_type:
        return None
    return mapping.get(crossref_type, "misc")


def extract_from_arxiv(value: str) -> MetadataRecord:
    """Extract metadata from arXiv API."""
    arxiv_id = normalize_arxiv_id(value)
    if not arxiv_id:
        return MetadataRecord(
            source_input=value,
            source_type="arxiv",
            status="invalid_arxiv_id",
            message="Input is not a valid arXiv identifier.",
        )

    url = f"http://export.arxiv.org/api/query?id_list={urllib.parse.quote(arxiv_id)}"

    try:
        raw = http_get(url, headers={"User-Agent": "citation-management-extract-metadata/1.0"}, timeout=15, retries=1)
    except Exception as exc:
        return MetadataRecord(
            source_input=value,
            source_type="arxiv",
            status="error",
            arxiv_id=arxiv_id,
            message=f"arXiv lookup failed: {exc}",
        )

    try:
        root = ET.fromstring(raw.decode("utf-8"))
    except Exception as exc:
        return MetadataRecord(
            source_input=value,
            source_type="arxiv",
            status="error",
            arxiv_id=arxiv_id,
            message=f"Could not parse arXiv response: {exc}",
        )

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entry = root.find("atom:entry", ns)

    if entry is None:
        return MetadataRecord(
            source_input=value,
            source_type="arxiv",
            status="not_found",
            arxiv_id=arxiv_id,
            message="arXiv ID not found.",
        )

    title = clean_text(entry.findtext("atom:title", default="", namespaces=ns))
    abstract = clean_text(entry.findtext("atom:summary", default="", namespaces=ns))
    published = entry.findtext("atom:published", default="", namespaces=ns)
    updated = entry.findtext("atom:updated", default="", namespaces=ns)
    authors = [
        clean_text(author.findtext("atom:name", default="", namespaces=ns))
        for author in entry.findall("atom:author", ns)
    ]
    authors = [author for author in authors if author]

    category = None
    category_node = entry.find("atom:category", ns)
    if category_node is not None:
        category = category_node.attrib.get("term")

    year = safe_year(published)

    return MetadataRecord(
        source_input=value,
        source_type="arxiv",
        status="verified",
        title=title,
        authors=authors,
        year=year,
        date=published[:10] if published else None,
        venue="arXiv",
        entry_type="misc",
        arxiv_id=arxiv_id,
        url=f"https://arxiv.org/abs/{arxiv_id}",
        abstract=abstract,
        version=updated[:10] if updated else None,
        citation_key=make_citation_key(authors, year, title),
        raw={"primary_class": category, "published": published, "updated": updated},
    )


def clean_text(value: str | None) -> str | None:
    """Normalize whitespace."""
    if not value:
        return None
    return re.sub(r"\s+", " ", value).strip()


# ---------------------------------------------------------------------------
# BibTeX extraction
# ---------------------------------------------------------------------------

def extract_from_bibtex_file(path: Path) -> list[MetadataRecord]:
    """Extract records from BibTeX file with lightweight parser."""
    text = path.read_text(encoding="utf-8")
    records: list[MetadataRecord] = []

    for raw_entry, entry_type, key, fields in parse_bibtex_entries(text):
        title = fields.get("title")
        authors = parse_bibtex_authors(fields.get("author"))
        year = safe_year(fields.get("year"))
        doi = normalize_doi(fields.get("doi"))
        arxiv_id = normalize_arxiv_id(fields.get("eprint") or fields.get("arxiv") or fields.get("url"))
        url = fields.get("url")
        venue = fields.get("journal") or fields.get("booktitle") or fields.get("publisher") or fields.get("institution")

        status = "extracted"
        message = None
        if not title:
            status = "metadata_incomplete"
            message = "Missing title."
        elif not doi and not arxiv_id and not url:
            status = "metadata_incomplete"
            message = "No DOI, arXiv ID, or URL."

        records.append(
            MetadataRecord(
                source_input=str(path),
                source_type="bibtex",
                status=status,
                title=title,
                authors=authors,
                year=year,
                venue=venue,
                entry_type=entry_type,
                doi=doi,
                arxiv_id=arxiv_id,
                url=url,
                citation_key=key,
                message=message,
                raw={"fields": fields, "raw_entry": raw_entry},
            )
        )

    return records


def parse_bibtex_entries(text: str) -> list[tuple[str, str, str, dict[str, str]]]:
    """Parse BibTeX entries enough for metadata extraction."""
    entries: list[tuple[str, str, str, dict[str, str]]] = []
    index = 0

    while True:
        at = text.find("@", index)
        if at == -1:
            break

        match = re.match(r"@([A-Za-z]+)\s*[{(]", text[at:])
        if not match:
            index = at + 1
            continue

        entry_type = match.group(1).lower()
        open_index = at + match.end() - 1
        open_char = text[open_index]
        close_char = "}" if open_char == "{" else ")"

        depth = 0
        end = None
        for pos in range(open_index, len(text)):
            char = text[pos]
            if char == open_char:
                depth += 1
            elif char == close_char:
                depth -= 1
                if depth == 0:
                    end = pos
                    break

        if end is None:
            break

        raw = text[at : end + 1]
        body = text[open_index + 1 : end].strip()

        if "," in body:
            key, fields_text = body.split(",", 1)
            fields = parse_bibtex_fields(fields_text)
            entries.append((raw, entry_type, key.strip(), fields))

        index = end + 1

    return entries


def parse_bibtex_fields(text: str) -> dict[str, str]:
    """Parse fields from a BibTeX body."""
    fields: dict[str, str] = {}
    i = 0
    n = len(text)

    while i < n:
        while i < n and text[i] in " \t\r\n,":
            i += 1
        if i >= n:
            break

        match = re.match(r"([A-Za-z][A-Za-z0-9_-]*)\s*=", text[i:])
        if not match:
            i += 1
            continue

        name = match.group(1).lower()
        i += match.end()

        while i < n and text[i].isspace():
            i += 1

        value = ""
        if i < n and text[i] == "{":
            start = i + 1
            i += 1
            depth = 1
            while i < n and depth > 0:
                if text[i] == "{":
                    depth += 1
                elif text[i] == "}":
                    depth -= 1
                i += 1
            value = text[start : i - 1].strip()
        elif i < n and text[i] == '"':
            start = i + 1
            i += 1
            while i < n and text[i] != '"':
                i += 1
            value = text[start:i].strip()
            i += 1
        else:
            start = i
            while i < n and text[i] not in ",\n":
                i += 1
            value = text[start:i].strip()

        fields[name] = value

    return fields


def parse_bibtex_authors(value: str | None) -> list[str]:
    """Parse BibTeX author field into list."""
    if not value:
        return []
    return [clean_text(author) or "" for author in value.split(" and ") if clean_text(author)]


# ---------------------------------------------------------------------------
# Text extraction
# ---------------------------------------------------------------------------

def extract_identifiers_from_text(path: Path) -> list[str]:
    """Extract DOI/arXiv/URL-like identifiers from text file."""
    text = path.read_text(encoding="utf-8")
    values: list[str] = []

    doi_pattern = re.compile(r"(?:https?://(?:dx\.)?doi\.org/|doi:\s*)?(10\.\d{4,9}/[^\s<>{}\"']+)", re.IGNORECASE)
    for match in doi_pattern.finditer(text):
        values.append(match.group(0).rstrip(".,;)"))

    arxiv_pattern = re.compile(r"(?:arXiv:\s*|https?://arxiv\.org/(?:abs|pdf)/)?(\d{4}\.\d{4,5}(?:v\d+)?)", re.IGNORECASE)
    for match in arxiv_pattern.finditer(text):
        candidate = match.group(0).rstrip(".,;)")
        if normalize_arxiv_id(candidate):
            values.append(candidate)

    url_pattern = re.compile(r"https?://[^\s<>{}\"']+")
    for match in url_pattern.finditer(text):
        url = match.group(0).rstrip(".,;)")
        if "doi.org" not in url and "arxiv.org" not in url:
            values.append(url)

    # Preserve order while deduping.
    seen: set[str] = set()
    unique: list[str] = []
    for value in values:
        if value not in seen:
            unique.append(value)
            seen.add(value)
    return unique


def extract_from_url(value: str) -> MetadataRecord:
    """Create metadata placeholder for URL.

    This does not scrape pages. It records stable URL metadata for manual or
    downstream verification.
    """
    url = value.strip()
    title = infer_title_from_url(url)
    return MetadataRecord(
        source_input=value,
        source_type="url",
        status="metadata_incomplete",
        title=title,
        url=url,
        entry_type="misc",
        message="URL recorded; page metadata not scraped. Verify manually if used in manuscript.",
    )


def infer_title_from_url(url: str) -> str | None:
    """Infer a rough title from URL path."""
    try:
        parsed = urllib.parse.urlparse(url)
        path = parsed.path.strip("/")
        if not path:
            return parsed.netloc
        slug = path.split("/")[-1]
        slug = re.sub(r"[-_]+", " ", slug)
        slug = re.sub(r"\.\w+$", "", slug)
        return slug.strip().title() if slug else parsed.netloc
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def extract_records(args: argparse.Namespace) -> list[MetadataRecord]:
    """Extract metadata records from CLI args."""
    records: list[MetadataRecord] = []

    for doi in args.doi or []:
        records.append(extract_from_doi(doi))

    for arxiv_id in args.arxiv or []:
        records.append(extract_from_arxiv(arxiv_id))

    for url in args.url or []:
        if normalize_doi(url):
            records.append(extract_from_doi(url))
        elif normalize_arxiv_id(url):
            records.append(extract_from_arxiv(url))
        else:
            records.append(extract_from_url(url))

    for bib_path in args.bib or []:
        records.extend(extract_from_bibtex_file(bib_path))

    for text_path in args.text or []:
        identifiers = extract_identifiers_from_text(text_path)
        for identifier in identifiers:
            if normalize_doi(identifier):
                records.append(extract_from_doi(identifier))
            elif normalize_arxiv_id(identifier):
                records.append(extract_from_arxiv(identifier))
            else:
                records.append(extract_from_url(identifier))

    return records


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def format_json(records: list[MetadataRecord]) -> str:
    """Format records as JSON."""
    return json.dumps(
        {
            "count": len(records),
            "records": [asdict(record) for record in records],
        },
        indent=2,
        ensure_ascii=False,
    )


def format_markdown(records: list[MetadataRecord]) -> str:
    """Format records as Markdown report."""
    lines: list[str] = []
    lines.append("# Metadata Extraction Report")
    lines.append("")
    lines.append(f"- Records: `{len(records)}`")
    lines.append("")

    status_counts: dict[str, int] = {}
    for record in records:
        status_counts[record.status] = status_counts.get(record.status, 0) + 1

    if status_counts:
        lines.append("## Status Summary")
        lines.append("")
        lines.append("| Status | Count |")
        lines.append("|---|---:|")
        for status, count in sorted(status_counts.items()):
            lines.append(f"| `{status}` | {count} |")
        lines.append("")

    lines.append("## Records")
    lines.append("")
    lines.append("| Status | Type | Key | Title | Year | DOI | arXiv | URL |")
    lines.append("|---|---|---|---|---:|---|---|---|")
    for record in records:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{record.status}`",
                    f"`{record.source_type}`",
                    f"`{record.citation_key or ''}`",
                    escape_table(record.title or ""),
                    str(record.year or ""),
                    f"`{record.doi or ''}`",
                    f"`{record.arxiv_id or ''}`",
                    record.url or "",
                ]
            )
            + " |"
        )
    lines.append("")

    issues = [record for record in records if record.status not in {"verified", "extracted"} or record.message]
    if issues:
        lines.append("## Issues / Manual Checks")
        lines.append("")
        for record in issues:
            lines.append(f"- `{record.source_input}` → `{record.status}`: {record.message or 'Check metadata.'}")
        lines.append("")

    lines.append("## Next Step")
    lines.append("")
    lines.append("- Use `validate_citations.py` after metadata is inserted into `.bib` files.")
    lines.append("- Use `research-lookup` if a real replacement source is needed.")
    lines.append("- Use `claim-auditor` to verify whether citations support manuscript claims.")
    lines.append("")

    return "\n".join(lines)


def format_bibtex_skeleton(records: list[MetadataRecord]) -> str:
    """Format extracted metadata as BibTeX skeleton entries."""
    entries: list[str] = []
    for record in records:
        key = record.citation_key or "needsKey"
        entry_type = record.entry_type or "misc"
        fields: list[tuple[str, str | None]] = [
            ("author", " and ".join(record.authors) if record.authors else None),
            ("title", record.title),
            ("year", str(record.year) if record.year else None),
        ]

        if entry_type == "article":
            fields.append(("journal", record.venue))
        elif entry_type == "inproceedings":
            fields.append(("booktitle", record.venue))
        elif record.venue:
            fields.append(("note", record.venue))

        fields.extend(
            [
                ("doi", record.doi),
                ("eprint", record.arxiv_id),
                ("archivePrefix", "arXiv" if record.arxiv_id else None),
                ("url", record.url),
            ]
        )

        lines = [f"@{entry_type}{{{key},"]
        included = [(name, value) for name, value in fields if value]
        for idx, (name, value) in enumerate(included):
            comma = "," if idx < len(included) - 1 else ""
            lines.append(f"  {name} = {{{value}}}{comma}")
        lines.append("}")
        entries.append("\n".join(lines))

    return "\n\n".join(entries) + ("\n" if entries else "")


def escape_table(value: str) -> str:
    """Escape Markdown table content."""
    return value.replace("|", "\\|").replace("\n", " ")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line args."""
    parser = argparse.ArgumentParser(
        description="Extract and normalize citation metadata.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/extract_metadata.py --doi 10.1109/CVPR.2016.91

  python scripts/extract_metadata.py --arxiv 2304.02643

  python scripts/extract_metadata.py --bib paper/references.bib --output metadata.json

  python scripts/extract_metadata.py --text references.txt --format markdown

  python scripts/extract_metadata.py --doi 10.1109/CVPR.2016.91 --format bibtex
        """,
    )

    parser.add_argument("--doi", nargs="*", help="DOI(s) or DOI URL(s).")
    parser.add_argument("--arxiv", nargs="*", help="arXiv ID(s) or arXiv URL(s).")
    parser.add_argument("--url", nargs="*", help="URL(s) to record as metadata placeholders.")
    parser.add_argument("--bib", nargs="*", type=Path, help="BibTeX file(s) to extract metadata from.")
    parser.add_argument("--text", nargs="*", type=Path, help="Text file(s) to scan for DOI/arXiv/URL identifiers.")
    parser.add_argument(
        "--format",
        choices=["json", "markdown", "bibtex"],
        default="json",
        help="Output format. Default: json.",
    )
    parser.add_argument("-o", "--output", type=Path, help="Output path. Defaults to stdout.")

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = parse_args(argv)

    has_input = any([args.doi, args.arxiv, args.url, args.bib, args.text])
    if not has_input:
        print("Error: provide at least one input source: --doi, --arxiv, --url, --bib, or --text.", file=sys.stderr)
        return 1

    records = extract_records(args)

    if args.format == "json":
        output = format_json(records)
    elif args.format == "markdown":
        output = format_markdown(records)
    else:
        output = format_bibtex_skeleton(records)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
        print(f"[citation-management] wrote output: {args.output}", file=sys.stderr)
    else:
        print(output)

    if not records:
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
