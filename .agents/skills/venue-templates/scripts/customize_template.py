#!/usr/bin/env python3
"""Copy and lightly customize a local venue template.

This helper supports the venue-templates skill.

It is intentionally conservative:
- copies a local template to an output path;
- replaces explicit placeholders only;
- preserves template notices and licensing;
- inserts TODOs rather than inventing missing content;
- never claims official compliance.

Final venue compliance must be verified against official venue instructions.

Examples:
    python scripts/customize_template.py --template nature_article.tex --output paper/main.tex
    python scripts/customize_template.py --template neurips.tex --title "My Paper" --authors "Anonymous Authors" --output paper/main.tex
    python scripts/customize_template.py --template poster.tex --output poster.tex --dry-run
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import dataclass, asdict
from pathlib import Path


PLACEHOLDER_PATTERNS: dict[str, list[str]] = {
    "title": [
        r"\bINSERT\s+TITLE\b",
        r"\bTITLE\s+HERE\b",
        r"\bYour\s+Title\s+Here\b",
        r"\bInsert\s+Your\s+Title\s+Here\b",
    ],
    "authors": [
        r"\bAUTHOR\(S\)\b",
        r"\bAUTHORS\s+HERE\b",
        r"\bFirst\s+Author.*Second\s+Author\b",
        r"\bAnonymous\s+Author\(s\)\b",
    ],
    "affiliations": [
        r"\bAFFILIATION\(S\)\b",
        r"\bAFFILIATIONS\s+HERE\b",
        r"\bDepartment\s+Name,\s*Institution\s+Name\b",
    ],
    "email": [
        r"\bEMAIL\s+HERE\b",
        r"\bfirst\.author@university\.edu\b",
        r"\bemail@example\.com\b",
    ],
}


@dataclass
class Replacement:
    """Replacement record."""

    field: str
    applied: bool
    pattern: str | None = None
    value_preview: str | None = None


@dataclass
class CustomizationReport:
    """Customization report."""

    template: str
    output: str
    dry_run: bool
    replacements: list[Replacement]
    warnings: list[str]


def skill_root() -> Path:
    """Return venue-templates skill root."""
    return Path(__file__).resolve().parent.parent


def find_template(template: str) -> Path | None:
    """Find template by path or by name under assets."""
    direct = Path(template)
    if direct.exists():
        return direct.resolve()

    assets = skill_root() / "assets"
    if not assets.exists():
        return None

    matches = [path for path in assets.rglob("*") if path.is_file() and path.name == template]
    if len(matches) == 1:
        return matches[0].resolve()

    if len(matches) > 1:
        # Prefer .tex templates if ambiguous.
        tex_matches = [path for path in matches if path.suffix.lower() == ".tex"]
        if len(tex_matches) == 1:
            return tex_matches[0].resolve()

    return None


def preview(value: str | None) -> str | None:
    """Preview replacement value."""
    if value is None:
        return None
    value = value.replace("\n", " ").strip()
    return value[:80] + ("..." if len(value) > 80 else "")


def replace_placeholders(content: str, values: dict[str, str | None]) -> tuple[str, list[Replacement]]:
    """Replace explicit placeholders only."""
    replacements: list[Replacement] = []
    updated = content

    for field, patterns in PLACEHOLDER_PATTERNS.items():
        value = values.get(field)
        if not value:
            replacements.append(Replacement(field=field, applied=False))
            continue

        applied = False
        used_pattern = None
        for pattern in patterns:
            if re.search(pattern, updated, flags=re.IGNORECASE | re.DOTALL):
                updated = re.sub(pattern, value, updated, count=1, flags=re.IGNORECASE | re.DOTALL)
                applied = True
                used_pattern = pattern
                break

        replacements.append(
            Replacement(
                field=field,
                applied=applied,
                pattern=used_pattern,
                value_preview=preview(value),
            )
        )

    return updated, replacements


def add_header_notice(content: str, template_path: Path) -> str:
    """Add a conservative generated-from notice if not already present."""
    notice = (
        "% Generated from a local venue-templates asset.\n"
        "% Verify current official venue requirements before submission.\n"
        f"% Source template: {template_path.name}\n\n"
    )
    if "Verify current official venue requirements" in content:
        return content
    return notice + content


def customize(
    *,
    template: Path,
    output: Path,
    title: str | None = None,
    authors: str | None = None,
    affiliations: str | None = None,
    email: str | None = None,
    dry_run: bool = False,
    no_notice: bool = False,
) -> CustomizationReport:
    """Customize template safely."""
    warnings: list[str] = []
    content = template.read_text(encoding="utf-8", errors="replace")

    if not no_notice and template.suffix.lower() == ".tex":
        content = add_header_notice(content, template)

    content, replacements = replace_placeholders(
        content,
        {
            "title": title,
            "authors": authors,
            "affiliations": affiliations,
            "email": email,
        },
    )

    if not any(rep.applied for rep in replacements):
        warnings.append("No placeholders were replaced. Template was copied/customized only with the optional notice.")

    warnings.append("Official venue requirements must still be verified manually.")
    warnings.append("Do not treat this customized file as submission-compliant until checked against the official template.")

    if not dry_run:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(content, encoding="utf-8")

    return CustomizationReport(
        template=str(template),
        output=str(output),
        dry_run=dry_run,
        replacements=replacements,
        warnings=warnings,
    )


def print_report(report: CustomizationReport) -> None:
    """Print text report."""
    print("Template Customization Report")
    print("=" * 36)
    print(f"Template: {report.template}")
    print(f"Output:   {report.output}")
    print(f"Dry run:  {report.dry_run}")
    print()
    print("Replacements:")
    for rep in report.replacements:
        status = "applied" if rep.applied else "not applied"
        print(f"- {rep.field}: {status}")
        if rep.applied:
            print(f"  value: {rep.value_preview}")
    print()
    print("Warnings:")
    for warning in report.warnings:
        print(f"- {warning}")
    print()
    print("Recommended next steps:")
    print("- Verify current official venue instructions.")
    print("- Use citation-management for bibliography/reference checks.")
    print("- Use claim-auditor for claim support.")
    print("- Use validate_format.py only for approximate local checks.")


def parse_args() -> argparse.Namespace:
    """Parse CLI args."""
    parser = argparse.ArgumentParser(
        description="Copy and lightly customize a local venue template.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/customize_template.py --template nature_article.tex --output paper/main.tex
  python scripts/customize_template.py --template neurips.tex --title "My Paper" --authors "Anonymous Authors" --output paper/main.tex
  python scripts/customize_template.py --template poster.tex --output poster.tex --dry-run --json
        """,
    )
    parser.add_argument("--template", required=True, help="Template path or local template filename under assets/.")
    parser.add_argument("--output", required=True, help="Output file path.")
    parser.add_argument("--title", help="Title replacement for explicit title placeholders.")
    parser.add_argument("--authors", help="Author replacement for explicit author placeholders.")
    parser.add_argument("--affiliations", help="Affiliation replacement for explicit affiliation placeholders.")
    parser.add_argument("--email", help="Email replacement for explicit email placeholders.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without writing output.")
    parser.add_argument("--no-notice", action="store_true", help="Do not insert venue verification notice.")
    parser.add_argument("--json", action="store_true", help="Print JSON report.")
    return parser.parse_args()


def main() -> int:
    """Run CLI."""
    args = parse_args()

    template = find_template(args.template)
    if not template:
        print(f"Error: template not found: {args.template}")
        print("Search local templates with: python scripts/query_template.py --list-all")
        return 1

    report = customize(
        template=template,
        output=Path(args.output),
        title=args.title,
        authors=args.authors,
        affiliations=args.affiliations,
        email=args.email,
        dry_run=args.dry_run,
        no_notice=args.no_notice,
    )

    if args.json:
        print(json.dumps(asdict(report), indent=2))
    else:
        print_report(report)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
