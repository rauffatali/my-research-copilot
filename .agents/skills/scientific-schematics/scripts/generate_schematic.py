#!/usr/bin/env python3
"""Evidence-aware scientific schematic generation CLI.

This is a thin, safer wrapper around generate_schematic_ai.py.

It reminds users that generated diagrams are implementation artifacts, not
scientific validation. Diagrams must be checked against manuscript/project
evidence before use.

Examples:
    python scripts/generate_schematic.py "left-to-right method pipeline: input image -> detector -> boxes" -o figures/pipeline.png

    python scripts/generate_schematic.py "training/evaluation protocol: train split -> training -> validation selection -> test evaluation" -o figures/protocol.png --doc-type conference

    python scripts/generate_schematic.py --spec figure_spec.md -o figures/method.png
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


DOC_TYPES = {
    "journal",
    "conference",
    "thesis",
    "grant",
    "preprint",
    "report",
    "poster",
    "presentation",
    "default",
}


SAFETY_SUFFIX = """

Scientific accuracy constraints:
- Use only the components and connections described above.
- Do not add extra model blocks, datasets, metrics, baselines, deployment stages, or performance numbers.
- Do not include claims such as best, robust, state-of-the-art, or significant improvement.
- Use readable labels, simple shapes, high contrast, and a clean scientific layout.
- Leave ambiguous or missing details out rather than guessing.
"""


def read_spec(path: Path) -> str:
    """Read diagram specification file."""
    return path.read_text(encoding="utf-8", errors="replace").strip()


def build_prompt(args: argparse.Namespace) -> str:
    """Build evidence-aware prompt."""
    if args.spec:
        prompt = read_spec(args.spec)
    else:
        prompt = args.description or ""

    prompt = prompt.strip()
    if not prompt:
        raise ValueError("Provide a diagram description or --spec file.")

    if args.no_safety_suffix:
        return prompt

    return prompt + SAFETY_SUFFIX


def validate_output_path(path: Path) -> None:
    """Validate output path."""
    if not path.suffix:
        raise ValueError("Output path should include an image extension, such as .png, .jpg, or .webp.")
    path.parent.mkdir(parents=True, exist_ok=True)


def run_ai_generator(prompt: str, args: argparse.Namespace) -> int:
    """Run underlying AI generator script."""
    script = Path(__file__).resolve().parent / "generate_schematic_ai.py"
    if not script.exists():
        print(f"Error: missing backend script: {script}", file=sys.stderr)
        return 1

    command = [
        sys.executable,
        str(script),
        prompt,
        "-o",
        str(args.output),
        "--iterations",
        str(args.iterations),
        "--doc-type",
        args.doc_type,
    ]

    if args.api_key:
        command.extend(["--api-key", args.api_key])
    if args.provider:
        command.extend(["--provider", args.provider])
    command.extend(["--timeout", str(args.timeout)])
    if args.verbose:
        command.append("--verbose")

    print("[scientific-schematics] Generating evidence-aware technical diagram...")
    print("[scientific-schematics] Reminder: generated diagrams require manual scientific verification.")
    return subprocess.call(command)


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Generate an evidence-aware scientific schematic.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/generate_schematic.py "left-to-right method pipeline: input image -> detector -> boxes" -o figures/pipeline.png

  python scripts/generate_schematic.py --spec figure_spec.md -o figures/method.png --doc-type conference

  python scripts/generate_schematic.py "data workflow: raw images -> annotation -> group split -> train/val/test" -o figures/data_workflow.png --iterations 1
        """,
    )
    parser.add_argument("description", nargs="?", help="Evidence-grounded diagram description.")
    parser.add_argument("--spec", type=Path, help="Markdown/text diagram specification file.")
    parser.add_argument("-o", "--output", required=True, type=Path, help="Output image path.")
    parser.add_argument("--iterations", type=int, default=1, choices=[1, 2], help="Maximum refinement iterations. Default: 1.")
    parser.add_argument("--doc-type", default="default", choices=sorted(DOC_TYPES), help="Document type for quality threshold.")
    parser.add_argument("--api-key", help="Provider API key. Prefer provider-specific environment variables.")
    parser.add_argument("--provider", default="openrouter", choices=["openrouter", "google", "openai"],
                        help="Image provider. OpenRouter preserves the iterative critic loop; direct providers generate the image and require manual review.")
    parser.add_argument("--timeout", type=int, default=300, help="HTTP read timeout in seconds. Default: 300.")
    parser.add_argument("--verbose", action="store_true", help="Verbose output.")
    parser.add_argument("--no-safety-suffix", action="store_true", help="Do not append scientific no-invention constraints.")
    return parser.parse_args()


def main() -> int:
    """CLI entry point."""
    args = parse_args()

    try:
        validate_output_path(args.output)
        prompt = build_prompt(args)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    code = run_ai_generator(prompt, args)

    if code == 0:
        print()
        print("[scientific-schematics] Next steps:")
        print("- Manually verify components, arrows, labels, and omissions against project evidence.")
        print("- Use claim-auditor for figure-caption claims.")
        print("- Use venue-templates for final figure size, format, and resolution.")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
