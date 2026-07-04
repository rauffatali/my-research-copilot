from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import unittest


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".agents" / "skills" / "workflow-manager" / "scripts"))

from workflow_state_checker import parse_current_status, validate_current_status  # noqa: E402


def build_status(
    current_phase: str,
    current_substep: str,
    latest_actions: tuple[str, ...],
    active_artifacts: tuple[str, ...],
    blockers: tuple[str, ...],
    next_steps: tuple[str, ...],
) -> str:
    lines = [
        "# Current Status",
        "",
        "## Metadata",
        "- Status type: template_default",
        "- Project initialized: no",
        "- Last updated: YYYY-MM-DD",
        "- State source: `docs/workflow_state_machine.md`",
        "- Status protocol: `docs/current_status_protocol.md`",
        "",
        "## Phase",
        f"- Current phase: `{current_phase}`",
        f"- Current substep: {current_substep}",
        "",
        "## Latest Action",
    ]
    lines.extend(f"- {item}" for item in latest_actions)
    lines.extend(["", "## Active Artifacts"])
    lines.extend(f"- `{item}`" for item in active_artifacts)
    lines.extend(["", "## Blockers"])
    lines.extend(f"- {item}" for item in blockers)
    lines.extend(["", "## Open Questions", "- None"])
    lines.extend(["", "## Next Step"])
    lines.extend(f"- {item}" for item in next_steps)
    return "\n".join(lines)


class WorkflowStateCheckerTests(unittest.TestCase):
    def test_scaffold_state_passes_with_existing_artifacts(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            for path in [
                "docs/current_status.md",
                "docs/agent/README.md",
                "paper/agent/README.md",
                "sources/README.md",
            ]:
                file_path = root / path
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.write_text("placeholder", encoding="utf-8")

            status = build_status(
                current_phase="intake",
                current_substep="repository scaffold setup",
                latest_actions=("created workflow memory scaffold files",),
                active_artifacts=(
                    "docs/current_status.md",
                    "docs/agent/README.md",
                    "paper/agent/README.md",
                    "sources/README.md",
                ),
                blockers=("phase-to-file contract not yet defined",),
                next_steps=("define per-phase artifact ownership and transition rules",),
            )
            (root / "docs/current_status.md").write_text(status, encoding="utf-8")

            issues = validate_current_status(root)

        self.assertEqual(issues, [])

    def test_phase_specific_state_requires_phase_artifacts(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            for path in [
                "docs/current_status.md",
                "docs/research_context.md",
                "docs/agent/brainstorming_brief.md",
                "docs/agent/research_direction.md",
                "docs/agent/hypotheses.md",
                "docs/agent/novelty_risk_matrix.md",
            ]:
                file_path = root / path
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.write_text("placeholder", encoding="utf-8")

            status = build_status(
                current_phase="phase_1_active",
                current_substep="research direction definition",
                latest_actions=("drafted the research direction",),
                active_artifacts=(
                    "docs/research_context.md",
                    "docs/agent/brainstorming_brief.md",
                    "docs/agent/research_direction.md",
                    "docs/agent/hypotheses.md",
                    "docs/agent/novelty_risk_matrix.md",
                ),
                blockers=("none",),
                next_steps=("freeze the Phase 1 artifact package",),
            )
            (root / "docs/current_status.md").write_text(status, encoding="utf-8")

            issues = validate_current_status(root)

        self.assertEqual(issues, [])

    def test_missing_required_phase_artifact_is_reported(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            for path in [
                "docs/current_status.md",
                "docs/agent/brainstorming_brief.md",
                "docs/agent/research_direction.md",
                "docs/agent/hypotheses.md",
            ]:
                file_path = root / path
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.write_text("placeholder", encoding="utf-8")

            status = build_status(
                current_phase="phase_1_active",
                current_substep="research direction definition",
                latest_actions=("drafted the research direction",),
                active_artifacts=(
                    "docs/agent/brainstorming_brief.md",
                    "docs/agent/research_direction.md",
                    "docs/agent/hypotheses.md",
                ),
                blockers=("none",),
                next_steps=("freeze the Phase 1 artifact package",),
            )
            (root / "docs/current_status.md").write_text(status, encoding="utf-8")

            issues = validate_current_status(root)

        self.assertTrue(
            any("missing required active artifact for phase_1" in issue.message for issue in issues)
        )

    def test_parse_current_status_extracts_fields(self) -> None:
        status = build_status(
            current_phase="intake",
            current_substep="repository scaffold setup",
            latest_actions=("created workflow memory scaffold files",),
            active_artifacts=("docs/current_status.md",),
            blockers=("phase-to-file contract not yet defined",),
            next_steps=("define per-phase artifact ownership and transition rules",),
        )

        snapshot = parse_current_status(status)

        self.assertEqual(snapshot.current_phase, "intake")
        self.assertEqual(snapshot.current_substep, "repository scaffold setup")
        self.assertEqual(snapshot.active_artifact_paths, ("docs/current_status.md",))


if __name__ == "__main__":
    unittest.main()
