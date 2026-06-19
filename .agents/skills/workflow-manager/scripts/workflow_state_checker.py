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

SCaffold_STATE = "not started"
ACTIVE_ARTIFACT_MARKERS = ("- Active artifact paths:", "- Active Artifacts:")

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


def _find_status_block(lines: list[str]) -> int:
    for index in range(len(lines) - 1, -1, -1):
        if lines[index].strip() == "## Status":
            return index
    return -1


def _extract_field_value(line: str, prefix: str) -> str | None:
    stripped = line.strip()
    if stripped.startswith("-"):
        stripped = stripped.removeprefix("-").strip()
    if stripped.startswith(prefix + ":"):
        return stripped.split(":", 1)[1].strip()
    return None


def _field_prefix(line: str) -> str | None:
    stripped = line.strip()
    for key in STATUS_KEYS:
        if stripped.startswith(f"- {key}:"):
            return key
    return None


def parse_current_status(text: str) -> StatusSnapshot:
    lines = text.splitlines()
    start = _find_status_block(lines)
    if start == -1:
        raise ValueError("missing ## Status section")

    current_phase = ""
    current_substep = ""
    latest_action = ""
    blockers = ""
    next_recommended_step = ""
    active_artifact_paths: list[str] = []
    active_paths_mode = False
    blockers_mode = False
    next_step_mode = False

    def finalize_modes() -> None:
        nonlocal active_paths_mode, blockers_mode, next_step_mode, blockers, next_recommended_step
        active_paths_mode = False
        if blockers_mode:
            blockers_mode = False
            if not blockers and blockers_values:
                blockers = "; ".join(blockers_values)
        if next_step_mode:
            next_step_mode = False
            if not next_recommended_step and next_step_values:
                next_recommended_step = "; ".join(next_step_values)

    blockers_values: list[str] = []
    next_step_values: list[str] = []

    for line in lines[start + 1 :]:
        stripped = line.strip()
        if stripped.startswith("## "):
            finalize_modes()
            break
        if not stripped:
            finalize_modes()
            continue

        if stripped.startswith(ACTIVE_ARTIFACT_MARKERS):
            finalize_modes()
            active_paths_mode = True
            continue

        marker = _field_prefix(line)
        if marker is not None:
            finalize_modes()
            value = _extract_field_value(line, marker)
            if marker == "Current phase" and value is not None:
                current_phase = value
            elif marker == "Current substep" and value is not None:
                current_substep = value
            elif marker == "Latest action" and value is not None:
                latest_action = value
            elif marker == "Blockers" and value is not None:
                if value:
                    blockers = value
                else:
                    blockers_mode = True
                    blockers_values = []
            elif marker == "Next recommended step" and value is not None:
                if value:
                    next_recommended_step = value
                else:
                    next_step_mode = True
                    next_step_values = []
            continue

        if line.startswith(" ") and stripped.startswith("-"):
            item = stripped.removeprefix("-").strip()
            if item.startswith("`") and item.endswith("`"):
                item = item[1:-1]
            if active_paths_mode:
                active_artifact_paths.append(item)
                continue
            if blockers_mode:
                blockers_values.append(item)
                continue
            if next_step_mode:
                next_step_values.append(item)
                continue

    finalize_modes()

    return StatusSnapshot(
        current_phase=current_phase,
        current_substep=current_substep,
        latest_action=latest_action,
        active_artifact_paths=tuple(active_artifact_paths),
        blockers=blockers,
        next_recommended_step=next_recommended_step,
    )


def infer_phase_key(current_phase: str) -> str | None:
    normalized = current_phase.strip().lower()
    if not normalized or normalized == SCaffold_STATE:
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
