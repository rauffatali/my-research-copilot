#!/usr/bin/env python3
"""Convert DOI identifiers to verified BibTeX entries.

This script supports the citation-management skill.

It:
- normalizes DOI strings;
- fetches BibTeX through DOI content negotiation;
- optionally fetches Crossref metadata for verification;
- flags DOI/title mismatches when an expected title is provided;
- writes BibTeX, JSON, or a Markdown conversion report;
- avoids inventing metadata when lookup fails.

Examples:
    python scripts/doi_to_bibtex.py 10.1109/CVPR.2016.91

    python scripts/doi_to_bibtex.py --input dois.txt --output references.bib

    python scripts/doi_to_bibtex.py 10.1109/CVPR.2016.91 \
        --expected-title "You Only Look Once" \
        --format markdown

    python scripts/doi_to_bibtex.py --input dois.txt \
        --format json --output reports/doi_to_bibtex.json
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
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class DOIResult:
    """Result of DOI-to-BibTeX conversion."""

    input_doi: str
    normalized_doi: str | None
    status: str
    bibtex: str | None = None
    title: str | None = None
    authors: list[str] | None = None
    year: int | None = None
    venue: str | None = None
    crossref_type: str | None = None
    url: str | None = None
    expected_title: str | None = None
    title_match: str | None = None
    message: str | None = None


# ---------------------------------------------------------------------------
# DOI and text helpers
# ---------------------------------------------------------------------------

def normalize_doi(value: str) -> str | None:
    """Normalize DOI from raw DOI, URL, or prefixed string."""
    doi = value.strip()
    doi = doi.strip("<>.,; ")
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.IGNORECASE)
    doi = re.sub(r"^DOI\s+", "", doi, flags=re.IGNORECASE)
    doi = doi.strip().rstrip(".")

    if not doi:
        return None

    if not re.match(r"^10\.\d{4,9}/\S+$", doi):
        return None

    return doi


def normalize_title(value: str | None) -> str:
    """Normalize title for comparison."""
    if not value:
        return ""
    text = re.sub(r"[{}\\]", "", value.lower())
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def title_match_status(actual: str | None, expected: str | None) -> str | None:
    """Return title match status."""
    if not expected:
        return None

    actual_norm = normalize_title(actual)
    expected_norm = normalize_title(expected)

    if not actual_norm:
        return "unknown"

    if actual_norm == expected_norm:
        return "exact"

    if expected_norm in actual_norm or actual_norm in expected_norm:
        return "partial"

    return "mismatch"


def clean_bibtex_key(bibtex: str, doi: str) -> str:
    """Ensure generated BibTeX has a non-empty citation key.

    Content negotiation sometimes returns long or inconvenient keys. This function
    only repairs missing/empty keys. It does not enforce a project-wide key style.
    """
    match = re.match(r"@([A-Za-z]+)\s*{\s*,", bibtex)
    if not match:
        return bibtex

    safe = re.sub(r"[^a-zA-Z0-9]+", "_", doi).strip("_")
    key = f"doi_{safe}"
    return re.sub(r"@([A-Za-z]+)\s*{\s*,", rf"@\1{{{key},", bibtex, count=1)


def normalize_bibtex_entry_type(bibtex: str) -> str:
    """Normalize uncommon Crossref entry types when needed."""
    # Some DOI negotiation responses return @data, which many BibTeX styles do
    # not support. Keep the entry usable but do not pretend it is a paper.
    bibtex = re.sub(r"^@data\s*{", "@misc{", bibtex.strip(), flags=re.IGNORECASE)
    return bibtex


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def http_get(
    url: str,
    *,
    headers: dict[str, str] | None = None,
    timeout: int = 20,
    retries: int = 1,
    delay: float = 2.0,
) -> bytes:
    """GET URL with lightweight retry for transient errors."""
    request = urllib.request.Request(url, headers=headers or {})
    last_error: Exception | None = None

    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code in {429, 500, 502, 503, 504} and attempt < retries:
                time.sleep(delay * (attempt + 1))
                continue
            raise
        except Exception as exc:
            last_error = exc
            if "timed out" in str(exc).lower() and attempt < retries:
                time.sleep(delay * (attempt + 1))
                continue
            raise

    raise RuntimeError(f"Request failed after retries: {last_error}")


def fetch_bibtex_for_doi(doi: str) -> str | None:
    """Fetch BibTeX through DOI content negotiation."""
    url = f"https://doi.org/{urllib.parse.quote(doi, safe='/')}"
    headers = {
        "Accept": "application/x-bibtex",
        "User-Agent": "citation-management-doi-to-bibtex/1.0",
    }

    try:
        raw = http_get(url, headers=headers, timeout=20, retries=1)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        raise

    text = raw.decode("utf-8", errors="replace").strip()
    if not text or not text.startswith("@"):
        return None

    text = normalize_bibtex_entry_type(text)
    text = clean_bibtex_key(text, doi)
    return text


def fetch_crossref_metadata(doi: str) -> dict[str, Any] | None:
    """Fetch Crossref metadata for DOI."""
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}"
    headers = {
        "User-Agent": "citation-management-doi-to-bibtex/1.0",
    }

    try:
        raw = http_get(url, headers=headers, timeout=20, retries=1)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        raise
    except Exception:
        return None

    try:
        data = json.loads(raw.decode("utf-8"))
    except json.JSONDecodeError:
        return None

    return data.get("message")


def crossref_authors(metadata: dict[str, Any]) -> list[str]:
    """Extract author names from Crossref metadata."""
    authors: list[str] = []
    for author in metadata.get("author", []) or []:
        given = author.get("given", "")
        family = author.get("family", "")
        name = " ".join(part for part in [given, family] if part).strip()
        if name:
            authors.append(name)
    return authors


def crossref_year(metadata: dict[str, Any]) -> int | None:
    """Extract year from Crossref metadata."""
    for field in ["published-print", "published-online", "published", "created"]:
        parts = metadata.get(field, {}).get("date-parts")
        if parts and parts[0]:
            try:
                return int(parts[0][0])
            except (TypeError, ValueError):
                return None
    return None


def crossref_venue(metadata: dict[str, Any]) -> str | None:
    """Extract venue/source from Crossref metadata."""
    container = metadata.get("container-title") or []
    if container:
        return container[0]
    publisher = metadata.get("publisher")
    if publisher:
        return publisher
    return None


# ---------------------------------------------------------------------------
# Conversion
# ---------------------------------------------------------------------------

def convert_doi(input_doi: str, *, expected_title: str | None = None, verify: bool = True) -> DOIResult:
    """Convert one DOI to BibTeX with optional metadata verification."""
    normalized = normalize_doi(input_doi)

    if not normalized:
        return DOIResult(
            input_doi=input_doi,
            normalized_doi=None,
            status="invalid_doi",
            expected_title=expected_title,
            message="Input is not a valid DOI.",
        )

    metadata = fetch_crossref_metadata(normalized) if verify else None

    bibtex = None
    try:
        bibtex = fetch_bibtex_for_doi(normalized)
    except Exception as exc:
        return DOIResult(
            input_doi=input_doi,
            normalized_doi=normalized,
            status="fetch_failed",
            expected_title=expected_title,
            message=f"Could not fetch BibTeX: {exc}",
        )

    if not bibtex:
        return DOIResult(
            input_doi=input_doi,
            normalized_doi=normalized,
            status="not_found",
            expected_title=expected_title,
            message="DOI did not return a BibTeX entry.",
        )

    title = None
    authors = None
    year = None
    venue = None
    crossref_type = None
    url = f"https://doi.org/{normalized}"

    if metadata:
        titles = metadata.get("title") or []
        title = titles[0] if titles else None
        authors = crossref_authors(metadata)
        year = crossref_year(metadata)
        venue = crossref_venue(metadata)
        crossref_type = metadata.get("type")
        url = metadata.get("URL") or url

    match_status = title_match_status(title, expected_title)

    status = "converted"
    message = None
    if match_status == "mismatch":
        status = "title_mismatch"
        message = "DOI metadata title does not match expected title."

    return DOIResult(
        input_doi=input_doi,
        normalized_doi=normalized,
        status=status,
        bibtex=bibtex,
        title=title,
        authors=authors,
        year=year,
        venue=venue,
        crossref_type=crossref_type,
        url=url,
        expected_title=expected_title,
        title_match=match_status,
        message=message,
    )


def read_dois_from_file(path: Path) -> list[str]:
    """Read DOI list from plain text file.

    Ignores blank lines and lines starting with #.
    """
    values: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        values.append(line)
    return values


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def format_bibtex(results: list[DOIResult]) -> str:
    """Format successful conversions as BibTeX."""
    entries = [result.bibtex for result in results if result.bibtex and result.status in {"converted", "title_mismatch"}]
    return "\n\n".join(entries).rstrip() + ("\n" if entries else "")


def format_json(results: list[DOIResult]) -> str:
    """Format conversion results as JSON."""
    payload = {
        "count": len(results),
        "converted": sum(1 for result in results if result.bibtex),
        "results": [asdict(result) for result in results],
    }
    return json.dumps(payload, indent=2, ensure_ascii=False)


def format_markdown(results: list[DOIResult]) -> str:
    """Format conversion report as Markdown."""
    lines: list[str] = []

    lines.append("# DOI to BibTeX Conversion Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Input DOIs: `{len(results)}`")
    lines.append(f"- Converted: `{sum(1 for result in results if result.bibtex)}`")
    lines.append(f"- Failed: `{sum(1 for result in results if not result.bibtex)}`")
    lines.append("")

    lines.append("## Results")
    lines.append("")
    lines.append("| DOI | Status | Title | Year | Venue | Message |")
    lines.append("|---|---|---|---:|---|---|")
    for result in results:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{result.normalized_doi or result.input_doi}`",
                    f"`{result.status}`",
                    escape_table(result.title or ""),
                    str(result.year or ""),
                    escape_table(result.venue or ""),
                    escape_table(result.message or ""),
                ]
            )
            + " |"
        )
    lines.append("")

    mismatches = [result for result in results if result.status == "title_mismatch"]
    if mismatches:
        lines.append("## Title Mismatches")
        lines.append("")
        for result in mismatches:
            lines.append(f"- `{result.normalized_doi}`")
            lines.append(f"  - Expected: {result.expected_title}")
            lines.append(f"  - Crossref: {result.title}")
        lines.append("")

    lines.append("## BibTeX Entries")
    lines.append("")
    bibtex = format_bibtex(results)
    if bibtex:
        lines.append("```bibtex")
        lines.append(bibtex.rstrip())
        lines.append("```")
    else:
        lines.append("No BibTeX entries were converted.")
    lines.append("")

    lines.append("## Next Step")
    lines.append("")
    lines.append("- Run `scripts/validate_citations.py` on the resulting `.bib` file.")
    lines.append("- Use `claim-auditor` to check whether citations support manuscript claims.")
    lines.append("- Do not use entries with title mismatches until manually verified.")
    lines.append("")

    return "\n".join(lines)


def escape_table(value: str) -> str:
    """Escape Markdown table pipes and newlines."""
    return value.replace("|", "\\|").replace("\n", " ")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert DOI(s) to BibTeX with optional Crossref verification.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/doi_to_bibtex.py 10.1109/CVPR.2016.91

  python scripts/doi_to_bibtex.py --input dois.txt --output references.bib

  python scripts/doi_to_bibtex.py 10.1109/CVPR.2016.91 \\
    --expected-title "You Only Look Once" --format markdown

  python scripts/doi_to_bibtex.py --input dois.txt \\
    --format json --output reports/doi_to_bibtex.json
        """,
    )

    parser.add_argument(
        "dois",
        nargs="*",
        help="DOI(s) to convert. DOI URLs are accepted.",
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        help="Input text file with one DOI per line.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output path. Defaults to stdout.",
    )
    parser.add_argument(
        "--format",
        choices=["bibtex", "json", "markdown"],
        default="bibtex",
        help="Output format. Default: bibtex.",
    )
    parser.add_argument(
        "--expected-title",
        default=None,
        help="Optional expected title for single DOI title-mismatch check.",
    )
    parser.add_argument(
        "--no-verify",
        action="store_true",
        help="Skip Crossref metadata verification and only fetch BibTeX.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay between DOI conversions. Default: 0.5 seconds.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return non-zero if any DOI fails or title mismatch is found.",
    )

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = parse_args(argv)

    dois: list[str] = []
    dois.extend(args.dois)

    if args.input:
        if not args.input.exists():
            print(f"Error: input file not found: {args.input}", file=sys.stderr)
            return 1
        dois.extend(read_dois_from_file(args.input))

    if not dois:
        print("Error: provide at least one DOI or --input file.", file=sys.stderr)
        return 1

    if args.expected_title and len(dois) != 1:
        print("Error: --expected-title can only be used with a single DOI.", file=sys.stderr)
        return 1

    results: list[DOIResult] = []
    for index, doi in enumerate(dois, start=1):
        print(f"[citation-management] converting DOI {index}/{len(dois)}: {doi}", file=sys.stderr)
        expected_title = args.expected_title if len(dois) == 1 else None
        result = convert_doi(doi, expected_title=expected_title, verify=not args.no_verify)
        results.append(result)

        if index < len(dois):
            time.sleep(args.delay)

    if args.format == "bibtex":
        output = format_bibtex(results)
    elif args.format == "json":
        output = format_json(results)
    else:
        output = format_markdown(results)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
        print(f"[citation-management] wrote output: {args.output}", file=sys.stderr)
    else:
        print(output)

    failed_or_mismatch = [
        result
        for result in results
        if not result.bibtex or result.status in {"title_mismatch", "invalid_doi", "not_found", "fetch_failed"}
    ]

    if args.strict and failed_or_mismatch:
        return 2

    if not any(result.bibtex for result in results):
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
