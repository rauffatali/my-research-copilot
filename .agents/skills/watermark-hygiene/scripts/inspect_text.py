#!/usr/bin/env python3
"""Inspect text for invisible Unicode and space-homoglyph artifacts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

# Allow running as script from any cwd
sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import emit_json, read_text_input
from text_unicode import human_report, inspect_text


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("path", nargs="?", default="-", help="Text file path, or - for stdin")
    p.add_argument("--json", action="store_true", help="JSON report")
    p.add_argument(
        "--aggressive",
        action="store_true",
        help="Also flag Latin confusable / fullwidth lookalikes",
    )
    p.add_argument(
        "--strip-emoji-glue",
        action="store_true",
        help="Paranoid: flag all load-bearing invisibles too (emoji glue, script joiners, flag tags, same-script fillers/selectors, orthographic Cf)",
    )
    p.add_argument(
        "--force-text",
        action="store_true",
        help="Scan even when the input looks like a binary container",
    )
    p.add_argument(
        "--audit",
        action="store_true",
        help="Detect-only Unicode audit: emit a structured flagged-span list",
    )
    args = p.parse_args()

    # read_text_input raises SystemExit(2) on unreadable/oversized/non-regular input.
    text = read_text_input(args.path, allow_binary=args.force_text)

    report = inspect_text(
        text,
        aggressive=args.aggressive,
        strip_emoji_glue=args.strip_emoji_glue,
    )

    if args.audit:
        flagged: list[dict[str, Any]] = []
        for hit in report.to_dict()["hits"]:
            flagged.append(
                {
                    "detector": "unicode",
                    "kind": hit["kind"],
                    "label": hit["label"],
                    "count": hit["count"],
                    "sample_offsets": hit["sample_offsets"],
                    "severity": hit["confidence"],
                }
            )
        audit: dict[str, Any] = {
            "path": "<stdin>" if args.path == "-" else args.path,
            "flagged_count": len(flagged),
            "flagged": flagged,
        }
        emit_json(audit)
    elif args.json:
        emit_json(report.to_dict())
    else:
        print(human_report(report))

    exit_code = 0
    if report.suspicious_total > 0:
        exit_code = 1

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
