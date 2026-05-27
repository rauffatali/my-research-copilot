#!/usr/bin/env python3
"""Agent-friendly entry point for the research lookup skill.

The real implementation lives in:

    scripts/research_lookup.py

Use this wrapper so agents can call:

    python lookup.py "query" --mode prior-work --limit 10
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def main() -> int:
    """Forward all command-line arguments to scripts/research_lookup.py."""
    skill_dir = Path(__file__).resolve().parent
    script = skill_dir / "scripts" / "research_lookup.py"

    if not script.exists():
        print(
            f"Error: expected implementation script not found: {script}",
            file=sys.stderr,
        )
        return 1

    cmd = [sys.executable, str(script), *sys.argv[1:]]
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main())