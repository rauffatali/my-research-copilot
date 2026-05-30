"""Validate workflow skeleton templates.

This script checks structural template rules only. It does not validate a
real project state, experiment output, or manuscript claim content.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ALLOWED_STATUSES = {"draft", "frozen", "superseded"}
TERMINAL_HEADINGS = {"Next Step", "Recommendation"}
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


@dataclass(frozen=True)
class TemplateSpec:
    path: str
    required_headings: tuple[str, ...]


@dataclass(frozen=True)
class ValidationIssue:
    path: str
    message: str


DEFAULT_SPECS: tuple[TemplateSpec, ...] = (
    TemplateSpec(
        "docs/agent/research_direction.md",
        (
            "Status",
            "Research Question",
            "Scope",
            "Closest Prior Work",
            "Baseline or Reference Point",
            "Failure Mode",
            "Metric or Decision Signal",
            "Risk / Tradeoff",
            "Next Step",
        ),
    ),
    TemplateSpec(
        "docs/agent/brainstorming_brief.md",
        (
            "Status",
            "Input Idea",
            "Working Summary",
            "Candidate Sources",
            "Open Questions",
            "Decision",
            "Next Step",
        ),
    ),
    TemplateSpec(
        "docs/agent/hypotheses.md",
        (
            "Status",
            "Hypothesis",
            "Expected Mechanism",
            "What Would Support It",
            "What Would Refute It",
            "Next Step",
        ),
    ),
    TemplateSpec(
        "docs/agent/novelty_risk_matrix.md",
        ("Status", "Notes", "Next Step"),
    ),
    TemplateSpec(
        "docs/agent/project_plan.md",
        (
            "Status",
            "Objective",
            "Scope and Assumptions",
            "Workstreams",
            "Task Breakdown",
            "Dependencies and Order",
            "Validation Plan",
            "Risks / Blockers",
            "Exit Criteria",
            "Next Step",
        ),
    ),
    TemplateSpec(
        "docs/agent/implementation_notes.md",
        (
            "Status",
            "Current Step",
            "Files Changed",
            "Changes Made",
            "Validation Run",
            "Outputs",
            "Blockers",
            "Next Step",
        ),
    ),
    TemplateSpec(
        "docs/agent/result_interpretation.md",
        (
            "Status",
            "Evaluation Context",
            "Main Findings",
            "Supported Claims",
            "Weak or Unsupported Claims",
            "Limitations",
            "Next Step",
        ),
    ),
    TemplateSpec(
        "docs/agent/claim_ledger.md",
        ("Status", "Notes", "Next Step"),
    ),
    TemplateSpec(
        "paper/agent/claim_support.md",
        ("Status", "Next Step"),
    ),
    TemplateSpec(
        "paper/agent/claim_audit.md",
        ("Status", "Next Step"),
    ),
    TemplateSpec(
        "paper/agent/section_notes.md",
        ("Status", "Section", "Purpose", "Evidence Used", "Draft Notes", "Next Step"),
    ),
    TemplateSpec(
        "paper/agent/style_notes.md",
        ("Status", "Style Source", "Key Style Traits", "Adaptation Notes", "Next Step"),
    ),
    TemplateSpec(
        "paper/agent/review_context.md",
        (
            "Status",
            "Review Round",
            "Manuscript Under Review",
            "Paper Summary",
            "Claim Map",
            "Baseline and Context",
            "Question Engine",
            "Review Probes",
            "Context Expansion",
            "Evidence Hooks",
            "Escalation Rules",
            "Suggested Reviewer Focus",
            "Open Questions",
            "Next Step",
        ),
    ),
    TemplateSpec(
        "paper/agent/review_method.md",
        ("Status", "Round 1", "Summary", "Strengths", "Major Concerns", "Minor Concerns", "Required Fixes", "Recommendation"),
    ),
    TemplateSpec(
        "paper/agent/review_domain.md",
        ("Status", "Round 1", "Summary", "Strengths", "Major Concerns", "Minor Concerns", "Required Fixes", "Recommendation"),
    ),
    TemplateSpec(
        "paper/agent/review_hybrid.md",
        ("Status", "Round 1", "Summary", "Strengths", "Major Concerns", "Minor Concerns", "Required Fixes", "Recommendation"),
    ),
    TemplateSpec(
        "paper/agent/review_meta.md",
        (
            "Status",
            "Round 1",
            "Consensus Strengths",
            "Consensus Weaknesses",
            "Reviewer Disagreements",
            "Must-Fix Issues",
            "Optional Improvements",
            "Recommendation",
        ),
    ),
    TemplateSpec(
        "paper/agent/revision_plan.md",
        ("Status", "Must-Fix Issues", "Optional Improvements", "Planned Changes", "Next Step"),
    ),
    TemplateSpec(
        "paper/agent/response_to_reviewers_draft.md",
        ("Status", "Reviewer 1", "Reviewer 2", "Reviewer 3", "Meta-Reviewer", "Next Step"),
    ),
    TemplateSpec(
        "paper/agent/review_notes.md",
        ("Status", "Review Round", "Key Objections", "Planned Response", "Next Step"),
    ),
)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def extract_headings(text: str) -> list[str]:
    headings: list[str] = []
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            headings.append(match.group(2).strip())
    return headings


def extract_status(text: str) -> str | None:
    in_status = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            in_status = stripped == "## Status"
            continue
        if in_status and stripped.startswith("-"):
            value = stripped.removeprefix("-").strip()
            if value.startswith("Allowed values:"):
                continue
            return value
    return None


def validate_template(root: Path, spec: TemplateSpec) -> list[ValidationIssue]:
    file_path = root / spec.path
    issues: list[ValidationIssue] = []

    if not file_path.exists():
        return [ValidationIssue(spec.path, "missing required template file")]

    text = file_path.read_text(encoding="utf-8")
    headings = extract_headings(text)
    heading_set = set(headings)

    for required in spec.required_headings:
        if required not in heading_set:
            issues.append(ValidationIssue(spec.path, f"missing required heading: {required}"))

    status = extract_status(text)
    if status is None:
        issues.append(ValidationIssue(spec.path, "missing Status value"))
    elif status not in ALLOWED_STATUSES:
        issues.append(
            ValidationIssue(
                spec.path,
                f"invalid Status value: {status!r}; allowed values: {', '.join(sorted(ALLOWED_STATUSES))}",
            )
        )

    if not headings:
        issues.append(ValidationIssue(spec.path, "contains no markdown headings"))
    elif headings[-1] not in TERMINAL_HEADINGS:
        issues.append(
            ValidationIssue(
                spec.path,
                f"last heading must be one of: {', '.join(sorted(TERMINAL_HEADINGS))}",
            )
        )

    return issues


def validate_specs(root: Path, specs: tuple[TemplateSpec, ...] = DEFAULT_SPECS) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for spec in specs:
        issues.extend(validate_template(root, spec))
    return issues


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate workflow skeleton templates.")
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
    issues = validate_specs(root)

    if issues:
        print("Workflow template validation failed:")
        for issue in issues:
            print(f"- {issue.path}: {issue.message}")
        return 1

    print(f"Workflow template validation passed for {len(DEFAULT_SPECS)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
