#!/usr/bin/env python3
"""Format and normalize BibTeX files safely.

This script supports the citation-management skill.

It performs formatting and lightweight normalization:
- parses BibTeX entries;
- standardizes indentation and field ordering;
- normalizes DOI fields;
- optionally normalizes arXiv fields;
- protects common AI/ML/CV acronyms in titles;
- sorts entries by citation key;
- detects duplicate keys;
- writes formatted BibTeX and optional report.

It does not verify that references exist.
Run validate_citations.py for reference validation and hallucinated-reference checks.

Examples:
    python scripts/format_bibtex.py paper/references.bib --output paper/references_formatted.bib

    python scripts/format_bibtex.py paper/references.bib --in-place --report reports/bibtex_format_report.md

    python scripts/format_bibtex.py paper/references.bib --sort --protect-ai-terms
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path


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
    comments_before: list[str] = field(default_factory=list)


@dataclass
class FormatChange:
    """Formatting change report item."""

    key: str
    category: str
    message: str


# ---------------------------------------------------------------------------
# Formatting config
# ---------------------------------------------------------------------------

FIELD_ORDER = [
    "author",
    "editor",
    "title",
    "journal",
    "booktitle",
    "series",
    "publisher",
    "institution",
    "school",
    "year",
    "date",
    "volume",
    "number",
    "pages",
    "articleno",
    "chapter",
    "edition",
    "doi",
    "eprint",
    "archivePrefix",
    "primaryClass",
    "url",
    "version",
    "note",
    "abstract",
    "keywords",
]

FIELD_CANONICAL = {
    "archiveprefix": "archivePrefix",
    "primaryclass": "primaryClass",
    "eprinttype": "eprinttype",
    "eprintclass": "eprintclass",
    "doi": "doi",
    "url": "url",
}

COMMON_AI_TERMS = [
    "AI",
    "ML",
    "CNN",
    "R-CNN",
    "Faster R-CNN",
    "YOLO",
    "DETR",
    "ViT",
    "CLIP",
    "SAM",
    "COCO",
    "ImageNet",
    "Cityscapes",
    "BDD100K",
    "mAP",
    "IoU",
    "AP50",
    "AP75",
    "ResNet",
    "Transformer",
    "Transformers",
]


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_bibtex(text: str) -> tuple[list[BibEntry], list[str]]:
    """Parse BibTeX entries and preserve top-level comments loosely."""
    entries: list[BibEntry] = []
    warnings: list[str] = []

    index = 0
    pending_comments: list[str] = []

    while index < len(text):
        at = text.find("@", index)

        if at == -1:
            trailing = text[index:].strip()
            if trailing:
                pending_comments.append(trailing)
            break

        between = text[index:at].strip()
        if between:
            pending_comments.append(between)

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
            warnings.append(f"Unclosed entry starting near character {at}.")
            break

        raw = text[at:end + 1]
        body = text[open_index + 1:end].strip()

        if "," not in body:
            warnings.append(f"Entry near character {at} has no key/field separator.")
            index = end + 1
            continue

        key, fields_text = body.split(",", 1)
        key = key.strip()
        fields = parse_fields(fields_text)

        entries.append(
            BibEntry(
                entry_type=entry_type,
                key=key,
                fields=fields,
                raw=raw,
                comments_before=pending_comments,
            )
        )
        pending_comments = []
        index = end + 1

    return entries, warnings


def parse_fields(text: str) -> dict[str, str]:
    """Parse BibTeX fields with nested braces support."""
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

        name = canonical_field_name(match.group(1))
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
            value = text[start:i - 1].strip()
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

        fields[name] = normalize_whitespace(value)

    return fields


def canonical_field_name(name: str) -> str:
    """Canonicalize field names while preserving common BibTeX names."""
    lower = name.lower()
    return FIELD_CANONICAL.get(lower, lower)


def normalize_whitespace(value: str) -> str:
    """Normalize non-URL whitespace in field values."""
    if "\n" not in value:
        return re.sub(r"\s+", " ", value).strip()
    return re.sub(r"\s+", " ", value).strip()


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------

def normalize_entry(entry: BibEntry, *, protect_ai_terms: bool = True) -> tuple[BibEntry, list[FormatChange]]:
    """Normalize one entry and return changes."""
    changes: list[FormatChange] = []
    fields = dict(entry.fields)

    if "doi" in fields:
        original = fields["doi"]
        normalized = normalize_doi(original)
        if normalized and normalized != original:
            fields["doi"] = normalized
            changes.append(FormatChange(entry.key, "doi", f"Normalized DOI from `{original}` to `{normalized}`."))

    if "eprint" in fields:
        original = fields["eprint"]
        normalized = normalize_arxiv_id(original)
        if normalized and normalized != original:
            fields["eprint"] = normalized
            changes.append(FormatChange(entry.key, "arxiv", f"Normalized arXiv/eprint from `{original}` to `{normalized}`."))

    if "url" in fields:
        original = fields["url"]
        normalized = original.strip().rstrip(".")
        if normalized != original:
            fields["url"] = normalized
            changes.append(FormatChange(entry.key, "url", "Trimmed URL punctuation/whitespace."))

    if protect_ai_terms and "title" in fields:
        original = fields["title"]
        protected = protect_terms(original)
        if protected != original:
            fields["title"] = protected
            changes.append(FormatChange(entry.key, "title", "Protected common AI/ML/CV acronyms or names in title."))

    normalized_entry_type = normalize_entry_type(entry.entry_type, fields)
    if normalized_entry_type != entry.entry_type:
        changes.append(
            FormatChange(
                entry.key,
                "entry_type",
                f"Normalized entry type from @{entry.entry_type} to @{normalized_entry_type}.",
            )
        )

    return (
        BibEntry(
            entry_type=normalized_entry_type,
            key=entry.key,
            fields=fields,
            raw=entry.raw,
            comments_before=entry.comments_before,
        ),
        changes,
    )


def normalize_entry_type(entry_type: str, fields: dict[str, str]) -> str:
    """Normalize entry type only for safe cases."""
    if entry_type == "conference":
        return "inproceedings"

    # Do not automatically convert article with arXiv journal to misc; that is
    # metadata-sensitive and should be handled by validation.
    if entry_type == "data":
        return "misc"

    return entry_type


def normalize_doi(value: str) -> str | None:
    """Normalize DOI field."""
    doi = value.strip().strip("{}").strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.IGNORECASE)
    doi = doi.strip().rstrip(".")
    if re.match(r"^10\.\d{4,9}/\S+$", doi):
        return doi
    return None


def normalize_arxiv_id(value: str) -> str | None:
    """Normalize arXiv ID for eprint fields."""
    text = value.strip().strip("{}").strip()
    text = re.sub(r"^arXiv:\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^https?://arxiv\.org/(abs|pdf)/", "", text, flags=re.IGNORECASE)
    text = text.replace(".pdf", "").strip()
    if re.match(r"^\d{4}\.\d{4,5}(v\d+)?$|^[a-z-]+(\.[A-Z]{2})?/\d{7}(v\d+)?$", text, re.IGNORECASE):
        return text
    return None


def protect_terms(title: str) -> str:
    """Protect common AI/ML/CV terms in a title without double-bracing."""
    protected = title

    for term in sorted(COMMON_AI_TERMS, key=len, reverse=True):
        # Skip if already appears in braces.
        already = re.compile(r"\{" + re.escape(term) + r"\}")
        if already.search(protected):
            continue

        # Replace standalone term.
        pattern = re.compile(r"(?<![A-Za-z0-9{])" + re.escape(term) + r"(?![A-Za-z0-9}])")
        protected = pattern.sub("{" + term + "}", protected)

    return protected


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def format_entries(entries: list[BibEntry], *, sort_entries: bool = False, keep_comments: bool = True) -> str:
    """Format BibTeX entries."""
    formatted_entries: list[str] = []

    if sort_entries:
        entries = sorted(entries, key=lambda entry: entry.key.lower())

    for entry in entries:
        parts: list[str] = []

        if keep_comments and entry.comments_before:
            for comment in entry.comments_before:
                if comment.strip():
                    parts.append(comment.strip())
            if parts:
                parts.append("")

        parts.append(format_entry(entry))
        formatted_entries.append("\n".join(parts).rstrip())

    return "\n\n".join(formatted_entries).rstrip() + "\n"


def format_entry(entry: BibEntry) -> str:
    """Format one BibTeX entry."""
    ordered_fields = order_fields(entry.fields)

    max_name_len = max((len(name) for name in ordered_fields), default=0)
    lines = [f"@{entry.entry_type}{{{entry.key},"]

    for idx, (name, value) in enumerate(ordered_fields):
        comma = "," if idx < len(ordered_fields) - 1 else ""
        padding = " " * (max_name_len - len(name))
        lines.append(f"  {name}{padding} = {{{value}}}{comma}")

    lines.append("}")
    return "\n".join(lines)


def order_fields(fields: dict[str, str]) -> list[tuple[str, str]]:
    """Order fields by preferred order, then alphabetically."""
    known: list[tuple[str, str]] = []
    unknown: list[tuple[str, str]] = []

    order_index = {name: index for index, name in enumerate(FIELD_ORDER)}

    for name, value in fields.items():
        if name in order_index:
            known.append((name, value))
        else:
            unknown.append((name, value))

    known.sort(key=lambda item: order_index[item[0]])
    unknown.sort(key=lambda item: item[0].lower())
    return known + unknown


# ---------------------------------------------------------------------------
# Reports and checks
# ---------------------------------------------------------------------------

def detect_duplicate_keys(entries: list[BibEntry]) -> list[FormatChange]:
    """Detect duplicate citation keys."""
    counts = Counter(entry.key for entry in entries)
    changes: list[FormatChange] = []
    for key, count in counts.items():
        if count > 1:
            changes.append(
                FormatChange(
                    key=key,
                    category="duplicate_key",
                    message=f"Citation key appears {count} times. Formatting did not resolve this.",
                )
            )
    return changes


def format_report(changes: list[FormatChange], warnings: list[str], output_path: Path | None = None) -> str:
    """Format Markdown report."""
    lines: list[str] = []
    lines.append("# BibTeX Formatting Report")
    lines.append("")
    if output_path:
        lines.append(f"- Output: `{output_path}`")
    lines.append(f"- Changes / warnings: `{len(changes) + len(warnings)}`")
    lines.append("")

    if warnings:
        lines.append("## Parser Warnings")
        lines.append("")
        for warning in warnings:
            lines.append(f"- {warning}")
        lines.append("")

    if changes:
        lines.append("## Changes and Findings")
        lines.append("")
        lines.append("| Key | Category | Message |")
        lines.append("|---|---|---|")
        for change in changes:
            lines.append(f"| `{change.key}` | `{change.category}` | {escape_table(change.message)} |")
        lines.append("")
    else:
        lines.append("No formatting changes were needed.")
        lines.append("")

    lines.append("## Next Step")
    lines.append("")
    lines.append("- Run `scripts/validate_citations.py` to check reference reality, duplicates, missing fields, and hallucination warnings.")
    lines.append("- Use `claim-auditor` to check whether citations support manuscript claims.")
    lines.append("- Do not treat formatting as verification.")
    lines.append("")
    return "\n".join(lines)


def escape_table(value: str) -> str:
    """Escape Markdown table text."""
    return value.replace("|", "\\|").replace("\n", " ")


# ---------------------------------------------------------------------------
# Main formatting pipeline
# ---------------------------------------------------------------------------

def format_bibtex_text(
    text: str,
    *,
    sort_entries: bool = False,
    protect_ai_terms: bool = True,
    keep_comments: bool = True,
) -> tuple[str, list[FormatChange], list[str]]:
    """Format a BibTeX document."""
    entries, warnings = parse_bibtex(text)

    all_changes: list[FormatChange] = []
    normalized_entries: list[BibEntry] = []

    for entry in entries:
        normalized, changes = normalize_entry(entry, protect_ai_terms=protect_ai_terms)
        normalized_entries.append(normalized)
        all_changes.extend(changes)

    all_changes.extend(detect_duplicate_keys(normalized_entries))

    formatted = format_entries(normalized_entries, sort_entries=sort_entries, keep_comments=keep_comments)
    return formatted, all_changes, warnings


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI args."""
    parser = argparse.ArgumentParser(
        description="Format and normalize BibTeX files safely.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/format_bibtex.py paper/references.bib --output paper/references_formatted.bib

  python scripts/format_bibtex.py paper/references.bib --in-place --report reports/bibtex_format_report.md

  python scripts/format_bibtex.py paper/references.bib --sort --protect-ai-terms
        """,
    )

    parser.add_argument("bib_file", type=Path, help="BibTeX file to format.")
    parser.add_argument("-o", "--output", type=Path, help="Output BibTeX path.")
    parser.add_argument("--in-place", action="store_true", help="Overwrite input file.")
    parser.add_argument("--sort", action="store_true", help="Sort entries by citation key.")
    parser.add_argument(
        "--protect-ai-terms",
        action="store_true",
        default=True,
        help="Protect common AI/ML/CV acronyms and names in titles. Enabled by default.",
    )
    parser.add_argument(
        "--no-protect-ai-terms",
        action="store_false",
        dest="protect_ai_terms",
        help="Disable automatic protection of common AI/ML/CV terms.",
    )
    parser.add_argument(
        "--drop-comments",
        action="store_true",
        help="Drop comments found between BibTeX entries.",
    )
    parser.add_argument("--report", type=Path, help="Optional Markdown report path.")
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Do not write formatted output; report whether changes would be made.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return non-zero if duplicate keys or parser warnings are found.",
    )

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = parse_args(argv)

    if not args.bib_file.exists():
        print(f"Error: BibTeX file not found: {args.bib_file}", file=sys.stderr)
        return 1

    if args.output and args.in_place:
        print("Error: use either --output or --in-place, not both.", file=sys.stderr)
        return 1

    original = args.bib_file.read_text(encoding="utf-8")
    formatted, changes, warnings = format_bibtex_text(
        original,
        sort_entries=args.sort,
        protect_ai_terms=args.protect_ai_terms,
        keep_comments=not args.drop_comments,
    )

    output_path: Path | None = None
    if args.in_place:
        output_path = args.bib_file
    elif args.output:
        output_path = args.output

    if args.check_only:
        if formatted != original:
            print("[citation-management] formatting changes would be made.", file=sys.stderr)
        else:
            print("[citation-management] no formatting changes needed.", file=sys.stderr)
    elif output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(formatted, encoding="utf-8")
        print(f"[citation-management] wrote formatted BibTeX: {output_path}", file=sys.stderr)
    else:
        print(formatted)

    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(format_report(changes, warnings, output_path), encoding="utf-8")
        print(f"[citation-management] wrote report: {args.report}", file=sys.stderr)

    if args.strict:
        has_duplicate_key = any(change.category == "duplicate_key" for change in changes)
        if warnings or has_duplicate_key:
            return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
