"""Check workflow-state consistency for the repository skeleton.

This checker validates the live status file against the workflow skeleton
rules. It is intentionally tolerant of the current scaffold state and does
not require a real project to exist.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


STATUS_KEYS = (
    "Current phase",
    "Current substep",
    "Latest action",
    "Blockers",
    "Next recommended step",
)

SCAFFOLD_PHASES = {"intake", "not started", "bootstrap_existing_project", "backfill_required"}


PHASE_REQUIRED_ARTIFACTS: dict[str, tuple[str, ...]] = {
    "phase_1": (
        "docs/agent/brainstorming_brief.md",
        "docs/agent/research_direction.md",
        "docs/agent/hypotheses.md",
        "docs/agent/novelty_risk_matrix.md",
    ),
    "phase_2": (
        "docs/agent/implementation_notes.md",
        "docs/PROJECT_PLAN.md",
    ),
    "phase_3": (
        "docs/agent/result_interpretation.md",
        "docs/agent/claim_ledger.md",
    ),
    "phase_4": (
        "paper/agent/claim_support.md",
        "paper/agent/section_notes.md",
        "paper/agent/style_notes.md",
    ),
    "phase_5": (
        "paper/agent/review_context.md",
        "paper/agent/review_method.md",
        "paper/agent/review_domain.md",
        "paper/agent/review_hybrid.md",
        "paper/agent/review_meta.md",
        "paper/agent/revision_plan.md",
        "paper/agent/response_to_reviewers_draft.md",
        "paper/agent/review_notes.md",
    ),
}


@dataclass(frozen=True)
class StatusSnapshot:
    current_phase: str
    current_substep: str
    latest_action: str
    active_artifact_paths: tuple[str, ...]
    blockers: str
    next_recommended_step: str


@dataclass(frozen=True)
class ValidationIssue:
    path: str
    message: str


def repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def _strip_inline_code(value: str) -> str:
    value = value.strip()
    if value.startswith("`") and value.endswith("`"):
        return value[1:-1].strip()
    return value


def _section_map(lines: list[str]) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current: str | None = None

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## "):
            current = stripped.removeprefix("## ").strip()
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line)

    return sections


def _field_from_section(section: list[str], key: str) -> str:
    prefix = f"- {key}:"
    for line in section:
        stripped = line.strip()
        if stripped.startswith(prefix):
            return _strip_inline_code(stripped.split(":", 1)[1].strip())
    return ""


def _bullet_values(section: list[str]) -> tuple[str, ...]:
    values: list[str] = []
    for line in section:
        stripped = line.strip()
        if stripped.startswith("- "):
            values.append(_strip_inline_code(stripped.removeprefix("- ").strip()))
    return tuple(values)


def parse_current_status(text: str) -> StatusSnapshot:
    sections = _section_map(text.splitlines())

    if "Phase" not in sections:
        raise ValueError("missing ## Phase section")
    if "Latest Action" not in sections:
        raise ValueError("missing ## Latest Action section")
    if "Active Artifacts" not in sections:
        raise ValueError("missing ## Active Artifacts section")
    if "Blockers" not in sections:
        raise ValueError("missing ## Blockers section")
    if "Next Step" not in sections:
        raise ValueError("missing ## Next Step section")

    latest_action = "; ".join(_bullet_values(sections["Latest Action"]))
    active_artifact_paths = _bullet_values(sections["Active Artifacts"])
    blockers = "; ".join(_bullet_values(sections["Blockers"]))
    next_recommended_step = "; ".join(_bullet_values(sections["Next Step"]))

    return StatusSnapshot(
        current_phase=_field_from_section(sections["Phase"], "Current phase"),
        current_substep=_field_from_section(sections["Phase"], "Current substep"),
        latest_action=latest_action,
        active_artifact_paths=active_artifact_paths,
        blockers=blockers,
        next_recommended_step=next_recommended_step,
    )


def infer_phase_key(current_phase: str) -> str | None:
    normalized = current_phase.strip().lower()
    if not normalized or normalized in SCAFFOLD_PHASES:
        return None
    if normalized in {"blocked", "archived"}:
        return normalized

    match = re.search(r"phase[_\s-]*([1-5])", normalized)
    if match:
        return f"phase_{match.group(1)}"
    return None


def validate_current_status(root: Path) -> list[ValidationIssue]:
    status_path = root / "docs/current_status.md"
    issues: list[ValidationIssue] = []
    if not status_path.exists():
        return [ValidationIssue("docs/current_status.md", "missing current status file")]

    text = status_path.read_text(encoding="utf-8")
    try:
        snapshot = parse_current_status(text)
    except ValueError as exc:
        return [ValidationIssue("docs/current_status.md", str(exc))]

    field_values = {
        "Current phase": snapshot.current_phase,
        "Current substep": snapshot.current_substep,
        "Latest action": snapshot.latest_action,
        "Active artifact paths": ", ".join(snapshot.active_artifact_paths),
        "Blockers": snapshot.blockers,
        "Next recommended step": snapshot.next_recommended_step,
    }
    for key in STATUS_KEYS:
        if not field_values[key]:
            issues.append(ValidationIssue("docs/current_status.md", f"missing required field: {key}"))

    for artifact in snapshot.active_artifact_paths:
        if not (root / artifact).exists():
            issues.append(ValidationIssue("docs/current_status.md", f"active artifact path does not exist: {artifact}"))

    phase_key = infer_phase_key(snapshot.current_phase)
    if phase_key in PHASE_REQUIRED_ARTIFACTS:
        for artifact in PHASE_REQUIRED_ARTIFACTS[phase_key]:
            if artifact not in snapshot.active_artifact_paths:
                issues.append(
                    ValidationIssue(
                        "docs/current_status.md",
                        f"missing required active artifact for {phase_key}: {artifact}",
                    )
                )

    return issues


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check workflow-state consistency.")
    parser.add_argument(
        "--root",
        type=Path,
        default=repo_root(),
        help="Repository root to validate. Defaults to the parent of the scripts directory.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = args.root.resolve()
    issues = validate_current_status(root)

    if issues:
        print("Workflow state check failed:")
        for issue in issues:
            print(f"- {issue.path}: {issue.message}")
        return 1

    print("Workflow state check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
