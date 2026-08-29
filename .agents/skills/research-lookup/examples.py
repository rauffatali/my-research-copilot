#!/usr/bin/env python3
"""Example commands for the research lookup skill.

This file is intentionally simple. It does not import or call the lookup
implementation directly.

Agents should usually call:

    python lookup.py "<query>" --mode <mode>

The examples below are command templates for common research lookup tasks
across AI/ML/CV and adjacent domains.
"""

from __future__ import annotations


EXAMPLES: list[tuple[str, str]] = [
    (
        "Closest prior work",
        'python lookup.py "small object detection aerial imagery benchmark" '
        "--mode prior-work --limit 10",
    ),
    (
        "Broad AI/CV prior work",
        'python lookup.py "transformer versus CNN image classification benchmark" '
        "--mode prior-work --limit 10",
    ),
    (
        "Baseline scouting",
        'python lookup.py "object detection YOLO benchmark mAP" '
        "--mode baseline-scout --limit 10",
    ),
    (
        "Domain-focused baseline scouting with boost phrases",
        'python lookup.py "image segmentation benchmark" '
        '--mode baseline-scout '
        '--boost-phrase "medical imaging" '
        '--boost-phrase "annotation protocol" '
        "--limit 10",
    ),
    (
        "Dataset and benchmark lookup",
        'python lookup.py "medical image segmentation dataset annotation protocol" '
        "--mode dataset-benchmark --limit 10",
    ),
    (
        "Citation candidates",
        'python lookup.py "domain shift in computer vision evaluation" '
        "--mode citation-candidates --limit 10",
    ),
    (
        "Recent developments",
        'python lookup.py "foundation models for object detection" '
        "--mode recent-developments --recent-years 3 --limit 10",
    ),
    (
        "Proceedings-style filter",
        'python lookup.py "transformer object detection" '
        "--mode prior-work --quality proceedings --year-from 2020 --limit 20",
    ),
    (
        "Venue-specific lookup",
        'python lookup.py "object detection transformer" '
        "--mode prior-work --venue CVPR --limit 10",
    ),
    (
        "High-citation citation candidates",
        'python lookup.py "domain shift computer vision evaluation" '
        "--mode citation-candidates --year-from 2018 --min-citations 50 --limit 20",
    ),
    (
        "Force OpenAlex only",
        'python lookup.py "time series anomaly detection benchmark" '
        "--mode prior-work --backend openalex --limit 10",
    ),
    (
        "Print without saving",
        'python lookup.py "small object detection benchmark" '
        "--mode baseline-scout --limit 10 --no-save",
    ),
    (
        "Save Markdown and JSON",
        'python lookup.py "domain shift computer vision evaluation" '
        "--mode citation-candidates "
        "--out sources/citations_domain_shift.md "
        "--json-out sources/citations_domain_shift.json",
    ),
]


def main() -> None:
    """Print example commands."""
    print("# Research Lookup Examples")
    print()
    print("Run these commands from `.agents/skills/research-lookup/`.")
    print()

    for title, command in EXAMPLES:
        print(f"## {title}")
        print()
        print("```bash")
        print(command)
        print("```")
        print()


if __name__ == "__main__":
    main()
