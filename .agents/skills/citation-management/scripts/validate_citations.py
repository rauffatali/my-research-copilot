#!/usr/bin/env python3
"""Validate BibTeX and LaTeX citations for citation-management.

This script is the main citation validation utility.

It checks:
- BibTeX syntax at a practical level
- required and recommended fields
- duplicate citation keys
- duplicate works by DOI, arXiv ID, URL, or normalized title
- DOI and arXiv identifier formatting
- optional DOI resolution / Crossref metadata checks
- LaTeX citation commands against bibliography keys
- unused bibliography entries
- hallucinated-reference warning signs

It does not prove that a cited source supports a manuscript claim.
Use claim-auditor for claim-evidence support checks.

Examples:
    python scripts/validate_citations.py paper/references.bib

    python scripts/validate_citations.py paper/references.bib \
        --tex paper/main.tex paper/sections/*.tex \
        --output reports/citation_validation.md

    python scripts/validate_citations.py paper/references.bib \
        --check-dois --json reports/citation_validation.json
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
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class BibEntry:
    """Parsed BibTeX entry."""

    entry_type: str
    key: str
    fields: dict[str, str]
    raw: str
    source_file: str
    start_line: int


@dataclass
class Finding:
    """Validation finding."""

    key: str
    severity: str
    category: str
    message: str
    source_file: str | None = None
    field: str | None = None
    suggestion: str | None = None


@dataclass
class CitationCommand:
    """LaTeX citation command occurrence."""

    command: str
    keys: list[str]
    source_file: str
    line: int
    context: str


@dataclass
class ValidationReport:
    """Validation result."""

    bib_files: list[str]
    tex_files: list[str]
    entries: list[BibEntry]
    findings: list[Finding]
    citation_commands: list[CitationCommand] = field(default_factory=list)
    missing_citation_keys: dict[str, list[str]] = field(default_factory=dict)
    unused_bib_keys: list[str] = field(default_factory=list)
    doi_checks: dict[str, dict[str, Any]] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REQUIRED_FIELDS: dict[str, list[str]] = {
    "article": ["author", "title", "journal", "year"],
    "inproceedings": ["author", "title", "booktitle", "year"],
    "conference": ["author", "title", "booktitle", "year"],
    "book": ["title", "publisher", "year"],  # author OR editor handled separately
    "incollection": ["author", "title", "booktitle", "publisher", "year"],
    "phdthesis": ["author", "title", "school", "year"],
    "mastersthesis": ["author", "title", "school", "year"],
    "techreport": ["author", "title", "institution", "year"],
    "misc": ["title"],
    "software": ["title", "url"],
    "dataset": ["title", "url"],
}

RECOMMENDED_FIELDS: dict[str, list[str]] = {
    "article": ["doi"],
    "inproceedings": ["booktitle"],
    "misc": ["url"],
    "software": ["version", "url"],
    "dataset": ["url"],
}

CITATION_COMMANDS = {
    "cite",
    "citep",
    "citet",
    "citealp",
    "citealt",
    "autocite",
    "parencite",
    "textcite",
    "citeauthor",
    "citeyear",
    "footcite",
    "supercite",
}

STRONG_CLAIM_TERMS = [
    "state-of-the-art",
    "sota",
    "robust",
    "generalizes",
    "generalization",
    "solves",
    "eliminates",
    "outperforms",
    "best",
    "superior",
    "significantly",
    "novel",
]

PLACEHOLDER_KEY_PATTERNS = [
    r"todo",
    r"citation",
    r"citationneeded",
    r"missing",
    r"unknown",
    r"ref\d*",
    r"changeme",
]


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def normalize_doi(value: str | None) -> str | None:
    """Normalize DOI string."""
    if not value:
        return None

    doi = value.strip().strip("{}").strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.IGNORECASE)
    doi = doi.strip().rstrip(".")
    return doi or None


def normalize_arxiv_id(value: str | None) -> str | None:
    """Normalize arXiv identifier from field or URL."""
    if not value:
        return None

    text = value.strip().strip("{}").strip()
    text = re.sub(r"^arXiv:\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^https?://arxiv\.org/(abs|pdf)/", "", text, flags=re.IGNORECASE)
    text = text.replace(".pdf", "")
    return text.strip() or None


def normalize_title(title: str | None) -> str:
    """Normalize title for duplicate checks."""
    if not title:
        return ""
    text = re.sub(r"[{}\\]", "", title.lower())
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_url(url: str | None) -> str | None:
    """Normalize URL for duplicate checks."""
    if not url:
        return None
    text = url.strip().strip("{}").strip()
    text = text.rstrip("/")
    return text or None


def line_number_at(text: str, index: int) -> int:
    """Return 1-indexed line number for index in text."""
    return text.count("\n", 0, index) + 1


def is_placeholder_key(key: str) -> bool:
    """Return whether citation key looks like a placeholder."""
    normalized = re.sub(r"[^a-z0-9]", "", key.lower())
    return any(re.search(pattern, normalized) for pattern in PLACEHOLDER_KEY_PATTERNS)


def has_balanced_braces(text: str) -> bool:
    """Basic brace balance check."""
    depth = 0
    for char in text:
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


# ---------------------------------------------------------------------------
# BibTeX parsing
# ---------------------------------------------------------------------------

def parse_bibtex_file(path: Path) -> tuple[list[BibEntry], list[Finding]]:
    """Parse BibTeX entries from a file.

    This parser handles nested braces well enough for validation tasks.
    It is not a full BibTeX implementation.
    """
    findings: list[Finding] = []
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        return [], [
            Finding(
                key="<file>",
                severity="critical",
                category="file_read_error",
                message=f"Could not read file: {exc}",
                source_file=str(path),
            )
        ]

    entries: list[BibEntry] = []
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
            start_line = line_number_at(text, at)
            findings.append(
                Finding(
                    key="<unknown>",
                    severity="critical",
                    category="bibtex_syntax",
                    message="Unclosed BibTeX entry.",
                    source_file=str(path),
                    suggestion="Check brace/parenthesis balance.",
                )
            )
            break

        raw = text[at : end + 1]
        body = text[open_index + 1 : end].strip()
        start_line = line_number_at(text, at)

        if "," not in body:
            findings.append(
                Finding(
                    key="<unknown>",
                    severity="high",
                    category="bibtex_syntax",
                    message="Entry missing citation key or comma after key.",
                    source_file=str(path),
                    suggestion="Expected format: @type{key, field = {value}}.",
                )
            )
            index = end + 1
            continue

        key, fields_text = body.split(",", 1)
        key = key.strip()
        fields = parse_bibtex_fields(fields_text)

        entries.append(
            BibEntry(
                entry_type=entry_type,
                key=key,
                fields=fields,
                raw=raw,
                source_file=str(path),
                start_line=start_line,
            )
        )

        if not has_balanced_braces(raw):
            findings.append(
                Finding(
                    key=key,
                    severity="critical",
                    category="bibtex_syntax",
                    message="Entry has unbalanced braces.",
                    source_file=str(path),
                    suggestion="Check nested title braces and field delimiters.",
                )
            )

        index = end + 1

    return entries, findings


def parse_bibtex_fields(text: str) -> dict[str, str]:
    """Parse BibTeX fields from entry body."""
    fields: dict[str, str] = {}
    i = 0
    n = len(text)

    while i < n:
        while i < n and text[i] in " \t\r\n,":
            i += 1
        if i >= n:
            break

        name_match = re.match(r"([A-Za-z][A-Za-z0-9_-]*)\s*=", text[i:])
        if not name_match:
            i += 1
            continue

        field_name = name_match.group(1).lower()
        i += name_match.end()

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
            escaped = False
            while i < n:
                if text[i] == '"' and not escaped:
                    break
                escaped = text[i] == "\\" and not escaped
                if text[i] != "\\":
                    escaped = False
                i += 1
            value = text[start:i].strip()
            i += 1
        else:
            start = i
            while i < n and text[i] not in ",\n":
                i += 1
            value = text[start:i].strip()

        fields[field_name] = value

    return fields


# ---------------------------------------------------------------------------
# Entry validation
# ---------------------------------------------------------------------------

def validate_entry(entry: BibEntry) -> list[Finding]:
    """Validate one BibTeX entry."""
    findings: list[Finding] = []
    fields = entry.fields
    entry_type = entry.entry_type
    key = entry.key

    if not key:
        findings.append(
            Finding(
                key="<missing>",
                severity="critical",
                category="missing_key",
                message="Entry has no citation key.",
                source_file=entry.source_file,
            )
        )
    elif is_placeholder_key(key):
        findings.append(
            Finding(
                key=key,
                severity="medium",
                category="placeholder_key",
                message="Citation key looks like a placeholder.",
                source_file=entry.source_file,
                suggestion="Replace with a stable firstAuthorYearKeyword key.",
            )
        )

    required = REQUIRED_FIELDS.get(entry_type, [])
    for field in required:
        if field not in fields or not fields[field].strip():
            if entry_type == "book" and field == "author":
                if "editor" in fields and fields["editor"].strip():
                    continue
            findings.append(
                Finding(
                    key=key,
                    severity="high",
                    category="missing_required_field",
                    field=field,
                    message=f"Missing required field `{field}` for @{entry_type}.",
                    source_file=entry.source_file,
                    suggestion="Complete metadata from a verified source.",
                )
            )

    for field in RECOMMENDED_FIELDS.get(entry_type, []):
        if field not in fields or not fields[field].strip():
            findings.append(
                Finding(
                    key=key,
                    severity="low",
                    category="missing_recommended_field",
                    field=field,
                    message=f"Missing recommended field `{field}` for @{entry_type}.",
                    source_file=entry.source_file,
                )
            )

    if "year" in fields:
        year = fields["year"].strip()
        if not re.fullmatch(r"\d{4}", year):
            findings.append(
                Finding(
                    key=key,
                    severity="high",
                    category="invalid_year",
                    field="year",
                    message=f"Invalid year format: `{year}`.",
                    source_file=entry.source_file,
                    suggestion="Use a four-digit publication or release year.",
                )
            )
        else:
            year_int = int(year)
            if year_int < 1900 or year_int > 2035:
                findings.append(
                    Finding(
                        key=key,
                        severity="medium",
                        category="suspicious_year",
                        field="year",
                        message=f"Suspicious year: `{year}`.",
                        source_file=entry.source_file,
                    )
                )

    if "doi" in fields:
        doi = normalize_doi(fields["doi"])
        if not doi or not re.match(r"^10\.\d{4,9}/\S+$", doi):
            findings.append(
                Finding(
                    key=key,
                    severity="medium",
                    category="invalid_doi_format",
                    field="doi",
                    message=f"Invalid DOI format: `{fields['doi']}`.",
                    source_file=entry.source_file,
                    suggestion="Use DOI form like `10.xxxx/...`, not a URL.",
                )
            )

    arxiv_candidate = fields.get("eprint") or fields.get("arxiv") or fields.get("url")
    if arxiv_candidate and "arxiv" in arxiv_candidate.lower() or fields.get("archiveprefix", "").lower() == "arxiv":
        arxiv_id = normalize_arxiv_id(arxiv_candidate or fields.get("eprint"))
        if arxiv_id and not re.match(r"^\d{4}\.\d{4,5}(v\d+)?$|^[a-z-]+(\.[A-Z]{2})?/\d{7}(v\d+)?$", arxiv_id, re.IGNORECASE):
            findings.append(
                Finding(
                    key=key,
                    severity="medium",
                    category="invalid_arxiv_id",
                    field="eprint",
                    message=f"Suspicious arXiv identifier: `{arxiv_id}`.",
                    source_file=entry.source_file,
                )
            )

    if "pages" in fields and re.search(r"\d-\d", fields["pages"]) and "--" not in fields["pages"]:
        findings.append(
            Finding(
                key=key,
                severity="low",
                category="page_range_format",
                field="pages",
                message="Page range appears to use a single hyphen.",
                source_file=entry.source_file,
                suggestion="Use `--` for BibTeX page ranges.",
            )
        )

    if "author" in fields:
        author_value = fields["author"]
        if ";" in author_value or " & " in author_value:
            findings.append(
                Finding(
                    key=key,
                    severity="high",
                    category="author_format",
                    field="author",
                    message="Authors should be separated by `and`, not semicolon or ampersand.",
                    source_file=entry.source_file,
                )
            )

    if entry_type == "article" and fields.get("journal", "").lower().startswith("arxiv"):
        findings.append(
            Finding(
                key=key,
                severity="medium",
                category="preprint_entry_type",
                field="journal",
                message="arXiv preprint appears as @article.",
                source_file=entry.source_file,
                suggestion="Use @misc for arXiv-only preprints unless published version is verified.",
            )
        )

    if entry_type in {"misc", "software", "dataset"}:
        if "url" not in fields and "doi" not in fields and "eprint" not in fields:
            findings.append(
                Finding(
                    key=key,
                    severity="medium",
                    category="missing_stable_identifier",
                    message="Entry has no DOI, arXiv ID, or URL.",
                    source_file=entry.source_file,
                    suggestion="Add a verified stable identifier if available.",
                )
            )

    title = fields.get("title", "")
    if title and re.search(r"\b(YOLO|CNN|R-CNN|Faster R-CNN|DETR|ViT|CLIP|SAM|COCO|ImageNet|mAP|IoU)\b", title):
        # Check for some common unprotected acronyms. This is a heuristic.
        if not re.search(r"\{(YOLO|CNN|R-CNN|Faster R-CNN|DETR|ViT|CLIP|SAM|COCO|ImageNet|mAP|IoU)\}", title):
            findings.append(
                Finding(
                    key=key,
                    severity="low",
                    category="unprotected_acronym",
                    field="title",
                    message="Title may contain unprotected AI/CV acronyms or dataset names.",
                    source_file=entry.source_file,
                    suggestion="Protect acronyms/model/dataset names with braces where needed.",
                )
            )

    if looks_hallucinated(entry):
        findings.append(
            Finding(
                key=key,
                severity="high",
                category="hallucination_warning",
                message="Reference has hallucination warning signs: weak metadata and no stable identifier.",
                source_file=entry.source_file,
                suggestion="Verify with Crossref/OpenAlex/arXiv/Semantic Scholar or mark as needs manual check.",
            )
        )

    return findings


def looks_hallucinated(entry: BibEntry) -> bool:
    """Heuristic warning for plausible but weak AI-generated references."""
    fields = entry.fields
    has_identifier = any(fields.get(name) for name in ["doi", "eprint", "arxiv", "url"])
    title = fields.get("title", "")
    author = fields.get("author", "")
    venue = fields.get("journal") or fields.get("booktitle") or ""

    if has_identifier:
        return False

    if not title:
        return True

    weak_author = not author or "et al" in author.lower()
    weak_venue = not venue and entry.entry_type in {"article", "inproceedings"}
    vague_title = bool(re.search(r"\b(novel|comprehensive|advanced|efficient|robust)\b", title.lower()))

    return weak_author and (weak_venue or vague_title)


# ---------------------------------------------------------------------------
# Duplicate checks
# ---------------------------------------------------------------------------

def detect_duplicates(entries: list[BibEntry]) -> list[Finding]:
    """Detect duplicate keys and likely duplicate works."""
    findings: list[Finding] = []

    key_to_entries: dict[str, list[BibEntry]] = defaultdict(list)
    doi_to_entries: dict[str, list[BibEntry]] = defaultdict(list)
    arxiv_to_entries: dict[str, list[BibEntry]] = defaultdict(list)
    title_to_entries: dict[str, list[BibEntry]] = defaultdict(list)
    url_to_entries: dict[str, list[BibEntry]] = defaultdict(list)

    for entry in entries:
        key_to_entries[entry.key].append(entry)

        doi = normalize_doi(entry.fields.get("doi"))
        if doi:
            doi_to_entries[doi.lower()].append(entry)

        arxiv = normalize_arxiv_id(entry.fields.get("eprint") or entry.fields.get("arxiv") or "")
        if arxiv:
            arxiv_to_entries[arxiv.lower()].append(entry)

        url = normalize_url(entry.fields.get("url"))
        if url:
            url_to_entries[url.lower()].append(entry)

        title = normalize_title(entry.fields.get("title"))
        if title:
            title_to_entries[title].append(entry)

    for key, duplicates in key_to_entries.items():
        if len(duplicates) > 1:
            findings.append(
                Finding(
                    key=key,
                    severity="critical",
                    category="duplicate_key",
                    message=f"Citation key appears {len(duplicates)} times.",
                    source_file=", ".join(sorted({e.source_file for e in duplicates})),
                    suggestion="Rename or merge duplicate entries, then update LaTeX citations.",
                )
            )

    for group_name, mapping in [
        ("duplicate_doi", doi_to_entries),
        ("duplicate_arxiv", arxiv_to_entries),
        ("duplicate_url", url_to_entries),
        ("duplicate_title", title_to_entries),
    ]:
        for value, duplicates in mapping.items():
            keys = sorted({entry.key for entry in duplicates})
            if len(keys) > 1:
                findings.append(
                    Finding(
                        key=", ".join(keys),
                        severity="medium",
                        category=group_name,
                        message=f"Possible duplicate work detected by {group_name.replace('duplicate_', '')}: {value}",
                        source_file=", ".join(sorted({e.source_file for e in duplicates})),
                        suggestion="Merge duplicates or keep both only if they are distinct versions.",
                    )
                )

    return findings


# ---------------------------------------------------------------------------
# DOI verification
# ---------------------------------------------------------------------------

def fetch_crossref_metadata(doi: str, *, timeout: int = 15) -> dict[str, Any] | None:
    """Fetch Crossref metadata for a DOI."""
    encoded = urllib.parse.quote(doi)
    url = f"https://api.crossref.org/works/{encoded}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "citation-management/1.0 (mailto:example@example.com)"},
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
        return data.get("message", {})
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        raise
    except Exception:
        return None


def check_dois(entries: list[BibEntry], *, delay: float = 0.5) -> tuple[list[Finding], dict[str, dict[str, Any]]]:
    """Check DOI resolution and title consistency through Crossref."""
    findings: list[Finding] = []
    checks: dict[str, dict[str, Any]] = {}

    for entry in entries:
        doi = normalize_doi(entry.fields.get("doi"))
        if not doi:
            continue

        metadata = fetch_crossref_metadata(doi)
        time.sleep(delay)

        if not metadata:
            findings.append(
                Finding(
                    key=entry.key,
                    severity="high",
                    category="doi_not_found",
                    field="doi",
                    message=f"DOI did not resolve in Crossref: `{doi}`.",
                    source_file=entry.source_file,
                    suggestion="Verify DOI manually or remove if incorrect.",
                )
            )
            checks[entry.key] = {"doi": doi, "status": "not_found"}
            continue

        crossref_title = ""
        titles = metadata.get("title") or []
        if titles:
            crossref_title = titles[0]

        local_title = entry.fields.get("title", "")
        local_norm = normalize_title(local_title)
        crossref_norm = normalize_title(crossref_title)

        status = "verified"
        if local_norm and crossref_norm and local_norm != crossref_norm:
            # Allow partial containment for subtitle/casing differences.
            if local_norm not in crossref_norm and crossref_norm not in local_norm:
                status = "title_mismatch"
                findings.append(
                    Finding(
                        key=entry.key,
                        severity="high",
                        category="doi_title_mismatch",
                        field="doi",
                        message=f"DOI resolves, but Crossref title differs: `{crossref_title}`.",
                        source_file=entry.source_file,
                        suggestion="Check whether DOI belongs to a different paper.",
                    )
                )

        checks[entry.key] = {
            "doi": doi,
            "status": status,
            "crossref_title": crossref_title,
            "crossref_year": extract_crossref_year(metadata),
            "crossref_type": metadata.get("type"),
            "crossref_url": metadata.get("URL"),
        }

    return findings, checks


def extract_crossref_year(metadata: dict[str, Any]) -> int | None:
    """Extract year from Crossref metadata."""
    for field in ["published-print", "published-online", "published", "created"]:
        parts = metadata.get(field, {}).get("date-parts")
        if parts and parts[0]:
            try:
                return int(parts[0][0])
            except (TypeError, ValueError):
                return None
    return None


# ---------------------------------------------------------------------------
# LaTeX citation checks
# ---------------------------------------------------------------------------

def parse_tex_citations(paths: list[Path]) -> list[CitationCommand]:
    """Parse citation commands from LaTeX files."""
    commands: list[CitationCommand] = []
    command_pattern = "|".join(re.escape(command) for command in sorted(CITATION_COMMANDS, key=len, reverse=True))
    pattern = re.compile(
        rf"\\({command_pattern})(?:\[[^\]]*\]){{0,2}}\{{([^}}]+)\}}",
        flags=re.MULTILINE,
    )

    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue

        for match in pattern.finditer(text):
            command = match.group(1)
            raw_keys = match.group(2)
            keys = [key.strip() for key in raw_keys.split(",") if key.strip()]
            line = line_number_at(text, match.start())
            context = get_line_context(text, line)

            commands.append(
                CitationCommand(
                    command=command,
                    keys=keys,
                    source_file=str(path),
                    line=line,
                    context=context,
                )
            )

    return commands


def get_line_context(text: str, line_number: int) -> str:
    """Return a line of text for context."""
    lines = text.splitlines()
    if 1 <= line_number <= len(lines):
        return lines[line_number - 1].strip()
    return ""


def validate_tex_citations(commands: list[CitationCommand], entries: list[BibEntry]) -> tuple[list[Finding], dict[str, list[str]], list[str]]:
    """Validate LaTeX citation keys against bibliography entries."""
    findings: list[Finding] = []
    bib_keys = {entry.key for entry in entries}
    cited_keys: list[str] = []
    missing: dict[str, list[str]] = defaultdict(list)

    for command in commands:
        for key in command.keys:
            cited_keys.append(key)
            if key not in bib_keys:
                missing[key].append(f"{command.source_file}:{command.line}")
                findings.append(
                    Finding(
                        key=key,
                        severity="critical",
                        category="missing_bib_entry",
                        message=f"Citation key `{key}` is used in LaTeX but missing from bibliography.",
                        source_file=f"{command.source_file}:{command.line}",
                        suggestion="Add a verified BibTeX entry or replace the citation key.",
                    )
                )

            if is_placeholder_key(key):
                findings.append(
                    Finding(
                        key=key,
                        severity="high",
                        category="placeholder_citation_key",
                        message="LaTeX citation key looks like a placeholder.",
                        source_file=f"{command.source_file}:{command.line}",
                        suggestion="Replace with verified citation key.",
                    )
                )

            if any(term in command.context.lower() for term in STRONG_CLAIM_TERMS):
                findings.append(
                    Finding(
                        key=key,
                        severity="low",
                        category="needs_claim_audit",
                        message="Citation appears near a strong claim; claim support may need auditing.",
                        source_file=f"{command.source_file}:{command.line}",
                        suggestion="Use claim-auditor if this claim is manuscript-critical.",
                    )
                )

    cited_counter = Counter(cited_keys)
    unused = sorted(bib_keys - set(cited_keys)) if commands else []

    for key, count in cited_counter.items():
        if count > 10:
            findings.append(
                Finding(
                    key=key,
                    severity="low",
                    category="high_citation_reuse",
                    message=f"Citation key used {count} times.",
                    suggestion="Check whether the same citation is overused or too broadly applied.",
                )
            )

    return findings, dict(missing), unused


# ---------------------------------------------------------------------------
# Validation orchestration
# ---------------------------------------------------------------------------

def validate(
    bib_files: list[Path],
    *,
    tex_files: list[Path] | None = None,
    check_doi_metadata: bool = False,
) -> ValidationReport:
    """Validate bibliography and optional LaTeX files."""
    entries: list[BibEntry] = []
    findings: list[Finding] = []

    for path in bib_files:
        parsed, parse_findings = parse_bibtex_file(path)
        entries.extend(parsed)
        findings.extend(parse_findings)

    for entry in entries:
        findings.extend(validate_entry(entry))

    findings.extend(detect_duplicates(entries))

    doi_checks: dict[str, dict[str, Any]] = {}
    if check_doi_metadata:
        doi_findings, doi_checks = check_dois(entries)
        findings.extend(doi_findings)

    citation_commands: list[CitationCommand] = []
    missing_citation_keys: dict[str, list[str]] = {}
    unused_bib_keys: list[str] = []

    if tex_files:
        expanded_tex_files = expand_paths(tex_files)
        citation_commands = parse_tex_citations(expanded_tex_files)
        tex_findings, missing_citation_keys, unused_bib_keys = validate_tex_citations(citation_commands, entries)
        findings.extend(tex_findings)
    else:
        expanded_tex_files = []

    return ValidationReport(
        bib_files=[str(path) for path in bib_files],
        tex_files=[str(path) for path in expanded_tex_files],
        entries=entries,
        findings=findings,
        citation_commands=citation_commands,
        missing_citation_keys=missing_citation_keys,
        unused_bib_keys=unused_bib_keys,
        doi_checks=doi_checks,
    )


def expand_paths(paths: list[Path]) -> list[Path]:
    """Expand glob-like paths passed by shell or literal patterns."""
    expanded: list[Path] = []
    for path in paths:
        if any(char in str(path) for char in "*?[]"):
            expanded.extend(Path().glob(str(path)))
        else:
            expanded.append(path)
    return [path for path in expanded if path.exists()]


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def summarize_findings(findings: list[Finding]) -> dict[str, int]:
    """Summarize findings by category and severity."""
    summary: dict[str, int] = Counter()
    for finding in findings:
        summary[finding.category] += 1
    return dict(summary)


def format_markdown(report: ValidationReport) -> str:
    """Format validation report as Markdown."""
    lines: list[str] = []

    lines.append("# Citation Validation Report")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append("### BibTeX files")
    lines.append("")
    for path in report.bib_files:
        lines.append(f"- `{path}`")
    lines.append("")

    if report.tex_files:
        lines.append("### LaTeX files")
        lines.append("")
        for path in report.tex_files:
            lines.append(f"- `{path}`")
        lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Entries parsed: `{len(report.entries)}`")
    lines.append(f"- Findings: `{len(report.findings)}`")
    lines.append(f"- Citation commands parsed: `{len(report.citation_commands)}`")
    lines.append(f"- Missing citation keys: `{len(report.missing_citation_keys)}`")
    lines.append(f"- Unused bibliography entries: `{len(report.unused_bib_keys)}`")
    lines.append("")

    severity_counts = Counter(f.severity for f in report.findings)
    if severity_counts:
        lines.append("### Findings by severity")
        lines.append("")
        lines.append("| Severity | Count |")
        lines.append("|---|---:|")
        for severity in ["critical", "high", "medium", "low"]:
            lines.append(f"| {severity} | {severity_counts.get(severity, 0)} |")
        lines.append("")

    category_counts = summarize_findings(report.findings)
    if category_counts:
        lines.append("### Findings by category")
        lines.append("")
        lines.append("| Category | Count |")
        lines.append("|---|---:|")
        for category, count in sorted(category_counts.items(), key=lambda item: (-item[1], item[0])):
            lines.append(f"| `{category}` | {count} |")
        lines.append("")

    if report.findings:
        lines.append("## Findings")
        lines.append("")
        lines.append("| Severity | Category | Key | File / location | Message | Suggestion |")
        lines.append("|---|---|---|---|---|---|")
        for finding in sorted(report.findings, key=lambda f: severity_order(f.severity)):
            lines.append(
                "| "
                + " | ".join(
                    [
                        finding.severity,
                        f"`{finding.category}`",
                        f"`{finding.key}`",
                        finding.source_file or "",
                        escape_table(finding.message),
                        escape_table(finding.suggestion or ""),
                    ]
                )
                + " |"
            )
        lines.append("")

    if report.missing_citation_keys:
        lines.append("## Missing Citation Keys")
        lines.append("")
        lines.append("| Key | Locations |")
        lines.append("|---|---|")
        for key, locations in sorted(report.missing_citation_keys.items()):
            lines.append(f"| `{key}` | {', '.join(f'`{loc}`' for loc in locations)} |")
        lines.append("")

    if report.unused_bib_keys:
        lines.append("## Unused Bibliography Entries")
        lines.append("")
        for key in report.unused_bib_keys:
            lines.append(f"- `{key}`")
        lines.append("")

    if report.doi_checks:
        lines.append("## DOI Checks")
        lines.append("")
        lines.append("| Key | DOI | Status | Crossref title |")
        lines.append("|---|---|---|---|")
        for key, check in sorted(report.doi_checks.items()):
            lines.append(
                f"| `{key}` | `{check.get('doi', '')}` | `{check.get('status', '')}` | "
                f"{escape_table(check.get('crossref_title', '') or '')} |"
            )
        lines.append("")

    lines.append("## Recommended Next Step")
    lines.append("")
    lines.append("- Fix `critical` and `high` findings before manuscript submission.")
    lines.append("- Use `research-lookup` for missing real sources.")
    lines.append("- Use `claim-auditor` for citations near strong or suspicious claims.")
    lines.append("- Mark unverified or hallucinated references explicitly instead of silently keeping them.")
    lines.append("")

    return "\n".join(lines)


def severity_order(severity: str) -> int:
    """Sort order for findings."""
    return {"critical": 0, "high": 1, "medium": 2, "low": 3}.get(severity, 9)


def escape_table(value: str) -> str:
    """Escape Markdown table pipes and newlines."""
    return value.replace("|", "\\|").replace("\n", " ")


def report_to_json(report: ValidationReport) -> dict[str, Any]:
    """Convert report to JSON-serializable dict."""
    payload = asdict(report)
    return payload


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI args."""
    parser = argparse.ArgumentParser(
        description="Validate BibTeX and LaTeX citation hygiene.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/validate_citations.py paper/references.bib

  python scripts/validate_citations.py paper/references.bib \\
    --tex paper/main.tex paper/sections/*.tex \\
    --output reports/citation_validation.md

  python scripts/validate_citations.py paper/references.bib \\
    --check-dois --json reports/citation_validation.json
        """,
    )

    parser.add_argument(
        "bib_files",
        nargs="+",
        type=Path,
        help="BibTeX file(s) to validate.",
    )
    parser.add_argument(
        "--tex",
        nargs="*",
        type=Path,
        default=None,
        help="Optional LaTeX file(s) or glob patterns to check citation commands.",
    )
    parser.add_argument(
        "--check-dois",
        action="store_true",
        help="Verify DOI metadata through Crossref. Requires network access.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Write Markdown report to this path.",
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=None,
        help="Write JSON report to this path.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return non-zero if any critical/high findings are present.",
    )

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = parse_args(argv)

    bib_files = expand_paths(args.bib_files)
    if not bib_files:
        print("Error: no BibTeX files found.", file=sys.stderr)
        return 1

    report = validate(
        bib_files,
        tex_files=args.tex,
        check_doi_metadata=args.check_dois,
    )

    markdown = format_markdown(report)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(markdown, encoding="utf-8")
        print(f"[citation-management] wrote markdown report: {args.output}", file=sys.stderr)
    else:
        print(markdown)

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report_to_json(report), indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[citation-management] wrote json report: {args.json}", file=sys.stderr)

    if args.strict:
        severe = [finding for finding in report.findings if finding.severity in {"critical", "high"}]
        if severe:
            return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
