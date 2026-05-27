#!/usr/bin/env python3
"""Query local venue templates and reference metadata.

This helper supports the venue-templates skill.

It searches the local venue-templates skill pack for available templates and
summarizes approximate local metadata. It is not an official venue source.

Final submission requirements must be verified against the official venue
website, official template, call for papers, author instructions, or submission
system.

Examples:
    python scripts/query_template.py --list-all
    python scripts/query_template.py --venue neurips
    python scripts/query_template.py --type journals
    python scripts/query_template.py --keyword poster
    python scripts/query_template.py --venue cvpr --requirements
    python scripts/query_template.py --json
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


TEMPLATE_EXTENSIONS = {".tex", ".cls", ".sty", ".docx", ".pptx", ".md", ".typ"}


LOCAL_REQUIREMENTS: dict[str, dict[str, str]] = {
    "neurips": {
        "category": "ml_conference",
        "official_verification": "required",
        "notes": "Check the current NeurIPS author kit, page limit, checklist, anonymization, and supplementary policy.",
    },
    "icml": {
        "category": "ml_conference",
        "official_verification": "required",
        "notes": "Check the current ICML author kit, style file, page limit, and review/camera-ready rules.",
    },
    "iclr": {
        "category": "ml_conference",
        "official_verification": "required",
        "notes": "Check the current ICLR submission instructions, OpenReview policy, and style file.",
    },
    "cvpr": {
        "category": "cv_conference",
        "official_verification": "required",
        "notes": "Check the current CVF template, page limit, review mode, supplement policy, and camera-ready instructions.",
    },
    "iccv": {
        "category": "cv_conference",
        "official_verification": "required",
        "notes": "Check the current CVF template, page limit, review mode, supplement policy, and camera-ready instructions.",
    },
    "eccv": {
        "category": "cv_conference",
        "official_verification": "required",
        "notes": "Check the current ECCV author kit and publisher instructions.",
    },
    "nature": {
        "category": "journal",
        "official_verification": "required",
        "notes": "Check the exact Nature-family journal instructions, article type, display item limits, and reporting statements.",
    },
    "science": {
        "category": "journal",
        "official_verification": "required",
        "notes": "Check the exact Science-family journal instructions, article type, word limits, and data/code statements.",
    },
    "plos": {
        "category": "journal",
        "official_verification": "required",
        "notes": "Check the exact PLOS journal instructions and article type.",
    },
    "nsf": {
        "category": "grant",
        "official_verification": "required",
        "notes": "Check the current solicitation and PAPPG requirements.",
    },
    "nih": {
        "category": "grant",
        "official_verification": "required",
        "notes": "Check the current FOA and NIH application guide.",
    },
}


@dataclass
class TemplateRecord:
    """Local template record."""

    name: str
    path: str
    category: str
    extension: str
    matched_terms: list[str]
    official_verification_required: bool = True


def skill_root() -> Path:
    """Return venue-templates skill root, assuming this script is in scripts/."""
    return Path(__file__).resolve().parent.parent


def iter_template_files(root: Path) -> Iterable[Path]:
    """Yield local template-like files under assets/."""
    assets = root / "assets"
    if not assets.exists():
        return []

    files: list[Path] = []
    for path in assets.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEMPLATE_EXTENSIONS:
            files.append(path)
    return files


def infer_category(path: Path, root: Path) -> str:
    """Infer category from path."""
    try:
        rel = path.relative_to(root / "assets")
        return rel.parts[0] if rel.parts else "unknown"
    except ValueError:
        return "unknown"


def normalize(text: str) -> str:
    """Normalize search text."""
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def record_for(path: Path, root: Path, terms: list[str]) -> TemplateRecord:
    """Build template record."""
    category = infer_category(path, root)
    text = normalize(" ".join([path.name, str(path), category]))
    matched = [term for term in terms if term and normalize(term) in text]
    return TemplateRecord(
        name=path.name,
        path=str(path),
        category=category,
        extension=path.suffix.lower(),
        matched_terms=matched,
    )


def search_templates(
    *,
    venue: str | None = None,
    template_type: str | None = None,
    keyword: str | None = None,
) -> list[TemplateRecord]:
    """Search local templates by venue/type/keyword."""
    root = skill_root()
    terms = [term for term in [venue, template_type, keyword] if term]
    normalized_terms = [normalize(term) for term in terms]

    records: list[TemplateRecord] = []
    for path in iter_template_files(root):
        record = record_for(path, root, terms)
        haystack = normalize(" ".join([path.name, str(path), record.category]))

        if template_type and normalize(template_type) != normalize(record.category):
            continue

        if venue and normalize(venue) not in haystack:
            # Allow high-level family matches.
            venue_key = normalize(venue)
            req = LOCAL_REQUIREMENTS.get(venue_key)
            if req and normalize(req.get("category", "")) in haystack:
                pass
            else:
                continue

        if keyword and normalize(keyword) not in haystack:
            continue

        if not terms or any(term in haystack for term in normalized_terms):
            records.append(record)

    return sorted(records, key=lambda item: (item.category, item.name.lower()))


def list_all() -> list[TemplateRecord]:
    """List all local template records."""
    return search_templates()


def requirements_for(venue: str) -> dict[str, str]:
    """Return approximate local requirement note for venue."""
    key = normalize(venue).split()[0] if venue else ""
    direct = LOCAL_REQUIREMENTS.get(normalize(venue))
    if direct:
        return direct

    for name, req in LOCAL_REQUIREMENTS.items():
        if name in normalize(venue):
            return req

    return {
        "category": "unknown",
        "official_verification": "required",
        "notes": "No local requirement note found. Verify official venue instructions.",
    }


def print_records(records: list[TemplateRecord]) -> None:
    """Print records as text."""
    if not records:
        print("No local templates found.")
        print("Reminder: official venue templates may still exist online and must be verified.")
        return

    print(f"Found {len(records)} local template file(s).\n")
    for record in records:
        print(f"- {record.name}")
        print(f"  category: {record.category}")
        print(f"  path: {record.path}")
        print(f"  type: {record.extension}")
        print("  official verification: required")
        if record.matched_terms:
            print(f"  matched: {', '.join(record.matched_terms)}")
        print()


def print_requirements(venue: str) -> None:
    """Print approximate local requirement note."""
    req = requirements_for(venue)
    print(f"Venue: {venue}")
    print(f"Category: {req.get('category', 'unknown')}")
    print("Official verification: required")
    print(f"Notes: {req.get('notes', 'Verify official venue instructions.')}")
    print()
    print("This is local guidance only. Check the current official venue website, template, and submission system before final submission.")


def parse_args() -> argparse.Namespace:
    """Parse CLI args."""
    parser = argparse.ArgumentParser(
        description="Query local venue-template files. Local results are not official requirements.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/query_template.py --list-all
  python scripts/query_template.py --venue neurips
  python scripts/query_template.py --type journals
  python scripts/query_template.py --keyword poster
  python scripts/query_template.py --venue cvpr --requirements
  python scripts/query_template.py --list-all --json
        """,
    )
    parser.add_argument("--venue", help="Venue name or acronym to search for.")
    parser.add_argument("--type", dest="template_type", help="Template category, such as journals, posters, grants, examples.")
    parser.add_argument("--keyword", help="Keyword to search in local template paths.")
    parser.add_argument("--list-all", action="store_true", help="List all local template-like files.")
    parser.add_argument("--requirements", action="store_true", help="Print approximate local requirement note for --venue.")
    parser.add_argument("--json", action="store_true", help="Output JSON.")
    return parser.parse_args()


def main() -> int:
    """Run CLI."""
    args = parse_args()

    if args.requirements:
        if not args.venue:
            print("Error: --requirements requires --venue.")
            return 1
        if args.json:
            print(json.dumps({"venue": args.venue, "requirements": requirements_for(args.venue)}, indent=2))
        else:
            print_requirements(args.venue)
        return 0

    if args.list_all:
        records = list_all()
    else:
        records = search_templates(venue=args.venue, template_type=args.template_type, keyword=args.keyword)

    if args.json:
        print(json.dumps({"count": len(records), "templates": [asdict(record) for record in records]}, indent=2))
    else:
        print_records(records)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
