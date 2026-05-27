from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import unittest


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".agents" / "skills" / "workflow-manager" / "scripts"))

from workflow_state_checker import parse_current_status, validate_current_status  # noqa: E402


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

            status = "\n".join(
                [
                    "# Current Status",
                    "",
                    "## Status",
                    "",
                    "- Current phase: not started",
                    "- Current substep: repository scaffold setup",
                    "- Latest action: created workflow memory scaffold files",
                    "- Active artifact paths:",
                    "  - `docs/current_status.md`",
                    "  - `docs/agent/README.md`",
                    "  - `paper/agent/README.md`",
                    "  - `sources/README.md`",
                    "- Blockers:",
                    "  - phase-to-file contract not yet defined",
                    "- Next recommended step:",
                    "  - define per-phase artifact ownership and transition rules",
                ]
            )
            (root / "docs/current_status.md").write_text(status, encoding="utf-8")

            issues = validate_current_status(root)

        self.assertEqual(issues, [])

    def test_phase_specific_state_requires_phase_artifacts(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            for path in [
                "docs/current_status.md",
                "docs/agent/brainstorming_brief.md",
                "docs/agent/research_direction.md",
                "docs/agent/hypotheses.md",
                "docs/agent/novelty_risk_matrix.md",
            ]:
                file_path = root / path
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.write_text("placeholder", encoding="utf-8")

            status = "\n".join(
                [
                    "# Current Status",
                    "",
                    "## Status",
                    "",
                    "- Current phase: phase_1_active",
                    "- Current substep: research direction definition",
                    "- Latest action: drafted the research direction",
                    "- Active artifact paths:",
                    "  - `docs/agent/brainstorming_brief.md`",
                    "  - `docs/agent/research_direction.md`",
                    "  - `docs/agent/hypotheses.md`",
                    "  - `docs/agent/novelty_risk_matrix.md`",
                    "- Blockers:",
                    "  - none",
                    "- Next recommended step:",
                    "  - freeze the Phase 1 artifact package",
                ]
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

            status = "\n".join(
                [
                    "# Current Status",
                    "",
                    "## Status",
                    "",
                    "- Current phase: phase_1_active",
                    "- Current substep: research direction definition",
                    "- Latest action: drafted the research direction",
                    "- Active artifact paths:",
                    "  - `docs/agent/brainstorming_brief.md`",
                    "  - `docs/agent/research_direction.md`",
                    "  - `docs/agent/hypotheses.md`",
                    "- Blockers:",
                    "  - none",
                    "- Next recommended step:",
                    "  - freeze the Phase 1 artifact package",
                ]
            )
            (root / "docs/current_status.md").write_text(status, encoding="utf-8")

            issues = validate_current_status(root)

        self.assertTrue(
            any("missing required active artifact for phase_1" in issue.message for issue in issues)
        )

    def test_parse_current_status_extracts_fields(self) -> None:
        status = "\n".join(
            [
                "# Current Status",
                "",
                "## Status",
                "",
                "- Current phase: not started",
                "- Current substep: repository scaffold setup",
                "- Latest action: created workflow memory scaffold files",
                "- Active artifact paths:",
                "  - `docs/current_status.md`",
                "- Blockers:",
                "  - phase-to-file contract not yet defined",
                "- Next recommended step:",
                "  - define per-phase artifact ownership and transition rules",
            ]
        )

        snapshot = parse_current_status(status)

        self.assertEqual(snapshot.current_phase, "not started")
        self.assertEqual(snapshot.current_substep, "repository scaffold setup")
        self.assertEqual(snapshot.active_artifact_paths, ("docs/current_status.md",))


if __name__ == "__main__":
    unittest.main()
