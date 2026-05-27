from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import unittest


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".agents" / "skills" / "workflow-manager" / "scripts"))

from workflow_validator import TemplateSpec, validate_specs  # noqa: E402


class WorkflowValidatorTests(unittest.TestCase):
    def test_valid_template_passes(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "template.md"
            path.write_text(
                "\n".join(
                    [
                        "# Template",
                        "",
                        "## Status",
                        "- draft",
                        "- Allowed values: draft, frozen, superseded",
                        "",
                        "## Required",
                        "- [State the required field.]",
                        "",
                        "## Next Step",
                        "- [State the next step.]",
                    ]
                ),
                encoding="utf-8",
            )

            issues = validate_specs(root, (TemplateSpec("template.md", ("Status", "Required", "Next Step")),))

        self.assertEqual(issues, [])

    def test_invalid_status_and_missing_heading_are_reported(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "template.md"
            path.write_text(
                "\n".join(
                    [
                        "# Template",
                        "",
                        "## Status",
                        "- active",
                        "",
                        "## Next Step",
                        "- [State the next step.]",
                    ]
                ),
                encoding="utf-8",
            )

            issues = validate_specs(root, (TemplateSpec("template.md", ("Status", "Required", "Next Step")),))

        messages = [issue.message for issue in issues]
        self.assertIn("missing required heading: Required", messages)
        self.assertTrue(any("invalid Status value" in message for message in messages))

    def test_terminal_heading_is_required(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "template.md"
            path.write_text(
                "\n".join(
                    [
                        "# Template",
                        "",
                        "## Status",
                        "- draft",
                        "",
                        "## Required",
                        "- [State the required field.]",
                    ]
                ),
                encoding="utf-8",
            )

            issues = validate_specs(root, (TemplateSpec("template.md", ("Status", "Required")),))

        self.assertTrue(any("last heading must be one of" in issue.message for issue in issues))


if __name__ == "__main__":
    unittest.main()
