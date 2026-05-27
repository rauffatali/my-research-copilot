#!/usr/bin/env python3
"""Approximate venue-format checks for local PDFs and LaTeX files.

This helper supports the venue-templates skill.

It performs lightweight checks such as page count, file existence, TODO markers,
basic anonymization warnings, and optional PDF font listing when tools are
available.

It is NOT an official compliance validator. Final compliance must be verified
with the official venue template, instructions, and submission system.

Examples:
    python scripts/validate_format.py --file paper.pdf --venue cvpr --check all
    python scripts/validate_format.py --file paper/main.tex --venue neurips --check latex-todos,anonymization
    python scripts/validate_format.py --file paper.pdf --venue nsf --report reports/format_check.md
    python scripts/validate_format.py --file paper.pdf --venue cvpr --json reports/format_check.json
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


APPROX_REQUIREMENTS: dict[str, dict[str, Any]] = {
    "cvpr": {"page_limit": None, "mode": "conference", "official_verification": "required"},
    "iccv": {"page_limit": None, "mode": "conference", "official_verification": "required"},
    "eccv": {"page_limit": None, "mode": "conference", "official_verification": "required"},
    "neurips": {"page_limit": None, "mode": "conference", "official_verification": "required"},
    "icml": {"page_limit": None, "mode": "conference", "official_verification": "required"},
    "iclr": {"page_limit": None, "mode": "conference", "official_verification": "required"},
    "nature": {"page_limit": None, "mode": "journal", "official_verification": "required"},
    "science": {"page_limit": None, "mode": "journal", "official_verification": "required"},
    "plos": {"page_limit": None, "mode": "journal", "official_verification": "required"},
    "nsf": {"page_limit": None, "mode": "grant", "official_verification": "required"},
    "nih": {"page_limit": None, "mode": "grant", "official_verification": "required"},
}


@dataclass
class CheckResult:
    """Format check result."""

    check: str
    status: str
    message: str
    details: dict[str, Any] | None = None


@dataclass
class ValidationReport:
    """Validation report."""

    file: str
    venue: str
    official_verification_required: bool
    checks: list[CheckResult]
    summary: dict[str, int]
    final_note: str


def normalize_venue(venue: str) -> str:
    """Normalize venue key."""
    text = re.sub(r"[^a-z0-9]+", " ", venue.lower()).strip()
    for key in APPROX_REQUIREMENTS:
        if key in text:
            return key
    return text.split()[0] if text else "unknown"


def run_command(command: list[str]) -> tuple[int, str, str]:
    """Run command safely."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError as exc:
        return 127, "", str(exc)


def pdf_page_count(path: Path) -> int | None:
    """Get PDF page count using pdfinfo if available."""
    code, stdout, _ = run_command(["pdfinfo", str(path)])
    if code != 0:
        return None

    for line in stdout.splitlines():
        if line.lower().startswith("pages:"):
            try:
                return int(line.split(":", 1)[1].strip())
            except ValueError:
                return None
    return None


def pdf_fonts(path: Path) -> list[str] | None:
    """List PDF fonts using pdffonts if available."""
    code, stdout, _ = run_command(["pdffonts", str(path)])
    if code != 0:
        return None

    fonts: list[str] = []
    for line in stdout.splitlines()[2:]:
        line = line.strip()
        if not line:
            continue
        fonts.append(line.split()[0])
    return sorted(set(fonts))


def check_file_exists(path: Path) -> CheckResult:
    """Check file exists."""
    if path.exists():
        return CheckResult("file-exists", "pass", f"File exists: {path}", {"size_bytes": path.stat().st_size})
    return CheckResult("file-exists", "fail", f"File not found: {path}")


def check_page_count(path: Path, venue_key: str) -> CheckResult:
    """Approximate page-count check."""
    if path.suffix.lower() != ".pdf":
        return CheckResult("page-count", "skip", "Page count check requires a PDF.")

    pages = pdf_page_count(path)
    if pages is None:
        return CheckResult("page-count", "skip", "Could not determine page count. Install poppler-utils/pdfinfo.")

    limit = APPROX_REQUIREMENTS.get(venue_key, {}).get("page_limit")
    if limit is None:
        return CheckResult(
            "page-count",
            "info",
            f"PDF has {pages} pages. No local page limit is encoded; verify official venue instructions.",
            {"pages": pages},
        )

    if pages <= limit:
        return CheckResult("page-count", "pass", f"PDF has {pages}/{limit} pages.", {"pages": pages, "limit": limit})

    return CheckResult("page-count", "fail", f"PDF has {pages}/{limit} pages.", {"pages": pages, "limit": limit})


def check_fonts(path: Path) -> CheckResult:
    """Approximate PDF font check."""
    if path.suffix.lower() != ".pdf":
        return CheckResult("fonts", "skip", "Font check requires a PDF.")

    fonts = pdf_fonts(path)
    if fonts is None:
        return CheckResult("fonts", "skip", "Could not list fonts. Install poppler-utils/pdffonts.")

    return CheckResult(
        "fonts",
        "info",
        "Fonts listed for manual inspection. This does not verify official compliance.",
        {"fonts": fonts},
    )


def read_text_if_possible(path: Path) -> str | None:
    """Read text file if possible."""
    if path.suffix.lower() not in {".tex", ".md", ".txt", ".bib"}:
        return None
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None


def check_latex_todos(path: Path) -> CheckResult:
    """Check TODO markers in text/LaTeX files."""
    text = read_text_if_possible(path)
    if text is None:
        return CheckResult("latex-todos", "skip", "TODO check requires a text/LaTeX file.")

    patterns = [r"\bTODO\b", r"TODO_", r"\\todo\{", r"needs citation", r"needs result", r"needs claim audit"]
    matches = []
    for pattern in patterns:
        matches.extend(re.findall(pattern, text, flags=re.IGNORECASE))

    if matches:
        return CheckResult(
            "latex-todos",
            "info",
            f"Found {len(matches)} TODO-like marker(s). Review before final submission.",
            {"count": len(matches)},
        )

    return CheckResult("latex-todos", "pass", "No TODO-like markers found.")


def check_anonymization(path: Path) -> CheckResult:
    """Heuristic anonymization check for LaTeX/text files."""
    text = read_text_if_possible(path)
    if text is None:
        return CheckResult("anonymization", "skip", "Anonymization check requires a text/LaTeX file.")

    warnings: list[str] = []
    if re.search(r"\\author\s*\{(?!\s*Anonymous)", text, flags=re.IGNORECASE | re.DOTALL):
        warnings.append("Non-anonymous \\author block may be present.")
    if re.search(r"acknowledg(e)?ments?", text, flags=re.IGNORECASE):
        warnings.append("Acknowledgments text may be present.")
    if re.search(r"github\.com/[^}\s]+", text, flags=re.IGNORECASE):
        warnings.append("GitHub link may identify authors or project.")
    if re.search(r"\\thanks\{", text):
        warnings.append("\\thanks{} may identify funding or authors.")

    if warnings:
        return CheckResult(
            "anonymization",
            "info",
            "Potential anonymization issues found. Verify official double-blind rules.",
            {"warnings": warnings},
        )

    return CheckResult("anonymization", "pass", "No obvious anonymization markers found by heuristic check.")


def check_bibliography(path: Path) -> CheckResult:
    """Heuristic bibliography check in LaTeX files."""
    text = read_text_if_possible(path)
    if text is None:
        return CheckResult("bibliography", "skip", "Bibliography check requires a text/LaTeX file.")

    has_bib = bool(re.search(r"\\bibliography\{|\\printbibliography|\\addbibresource", text))
    has_cite = bool(re.search(r"\\cite[a-zA-Z]*\{", text))

    if has_cite and not has_bib:
        return CheckResult(
            "bibliography",
            "info",
            "Citation commands found but no bibliography command detected. Verify project structure.",
        )
    if has_bib:
        return CheckResult(
            "bibliography",
            "info",
            "Bibliography command detected. Use citation-management for reference integrity.",
        )
    return CheckResult("bibliography", "info", "No bibliography command detected.")


def validate(path: Path, venue: str, checks: list[str]) -> ValidationReport:
    """Run selected checks."""
    venue_key = normalize_venue(venue)
    selected = set(checks)
    if "all" in selected:
        selected = {"file-exists", "page-count", "fonts", "latex-todos", "anonymization", "bibliography"}

    results: list[CheckResult] = []
    all_checks = {
        "file-exists": lambda: check_file_exists(path),
        "page-count": lambda: check_page_count(path, venue_key),
        "fonts": lambda: check_fonts(path),
        "latex-todos": lambda: check_latex_todos(path),
        "anonymization": lambda: check_anonymization(path),
        "bibliography": lambda: check_bibliography(path),
    }

    # Always check file existence first.
    if "file-exists" not in selected:
        selected.add("file-exists")

    for check_name in ["file-exists", "page-count", "fonts", "latex-todos", "anonymization", "bibliography"]:
        if check_name in selected:
            results.append(all_checks[check_name]())

    summary: dict[str, int] = {}
    for result in results:
        summary[result.status] = summary.get(result.status, 0) + 1

    return ValidationReport(
        file=str(path),
        venue=venue,
        official_verification_required=True,
        checks=results,
        summary=summary,
        final_note="Approximate local checks only. Verify final compliance with official venue instructions and submission system.",
    )


def format_markdown(report: ValidationReport) -> str:
    """Format report as Markdown."""
    lines: list[str] = []
    lines.append("# Venue Format Validation Report")
    lines.append("")
    lines.append(f"- File: `{report.file}`")
    lines.append(f"- Venue: `{report.venue}`")
    lines.append("- Official verification required: `yes`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---:|")
    for status, count in sorted(report.summary.items()):
        lines.append(f"| `{status}` | {count} |")
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    lines.append("| Check | Status | Message |")
    lines.append("|---|---|---|")
    for check in report.checks:
        msg = check.message.replace("|", "\\|")
        lines.append(f"| `{check.check}` | `{check.status}` | {msg} |")
    lines.append("")
    lines.append("## Final Note")
    lines.append("")
    lines.append(report.final_note)
    lines.append("")
    lines.append("## Recommended Handoffs")
    lines.append("")
    lines.append("- Use `citation-management` for references and BibTeX.")
    lines.append("- Use `claim-auditor` for claim support.")
    lines.append("- Use `results-scaffold` for result tables/placeholders.")
    lines.append("- Use official venue instructions for final compliance.")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    """Parse CLI args."""
    parser = argparse.ArgumentParser(
        description="Run approximate local venue-format checks. Not an official validator.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Checks:
  file-exists, page-count, fonts, latex-todos, anonymization, bibliography, all

Examples:
  python scripts/validate_format.py --file paper.pdf --venue cvpr --check all
  python scripts/validate_format.py --file paper/main.tex --venue neurips --check latex-todos,anonymization
  python scripts/validate_format.py --file paper.pdf --venue nsf --report reports/format_check.md
  python scripts/validate_format.py --file paper.pdf --venue cvpr --json reports/format_check.json
        """,
    )
    parser.add_argument("--file", required=True, help="PDF, LaTeX, or text file to check.")
    parser.add_argument("--venue", required=True, help="Target venue name or acronym.")
    parser.add_argument("--check", default="all", help="Comma-separated checks, or all.")
    parser.add_argument("--report", help="Write Markdown report to this path.")
    parser.add_argument("--json", dest="json_path", help="Write JSON report to this path.")
    return parser.parse_args()


def main() -> int:
    """Run CLI."""
    args = parse_args()
    path = Path(args.file)
    checks = [item.strip() for item in args.check.split(",") if item.strip()]

    report = validate(path, args.venue, checks)
    markdown = format_markdown(report)

    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(markdown, encoding="utf-8")
        print(f"[venue-templates] wrote markdown report: {report_path}")
    else:
        print(markdown)

    if args.json_path:
        json_path = Path(args.json_path)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(json.dumps(asdict(report), indent=2), encoding="utf-8")
        print(f"[venue-templates] wrote json report: {json_path}")

    if any(check.status == "fail" for check in report.checks):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
