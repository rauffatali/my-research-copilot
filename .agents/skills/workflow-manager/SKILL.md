---
name: workflow-manager
description: Use for managing the repository's agentic workflow skeleton, including phase routing, workflow-state decisions, current-status checks, phase-template validation, and canonical workflow-example usage. Use when a task asks how the workflow should progress, whether a phase change is allowed, whether docs/current_status.md is coherent, or whether workflow templates need validation.
---

# Workflow Manager

Use this skill to manage the repository's workflow skeleton, not to fabricate project state.

## Core sources

- `docs/workflow_state_machine.md`
- `docs/current_status.md`
- `docs/agent/`
- `paper/agent/`

## References

- `references/example_workflow.md`
- `references/artifact_naming_conventions.md`
- `references/phase_ownership_matrix.md`
- `references/workflow_maintenance_checklist.md`

## Operating sequence

1. Classify the task into the correct workflow phase or skeleton-maintenance task.
2. Read `references/example_workflow.md` when the phase flow is unclear or when using the skeleton for the first time in a thread.
3. Read `references/artifact_naming_conventions.md` when naming or placing workflow artifacts is unclear.
4. Read `references/phase_ownership_matrix.md` when deciding which phase may create or modify a file.
5. Read `references/workflow_maintenance_checklist.md` when reviewing workflow guidance and references.
6. Read `docs/workflow_state_machine.md` before deciding any phase transition.
7. Use `docs/current_status.md` as the live pointer only when the task is actually advancing or checking workflow state.
8. Keep `docs/current_status.md` at the scaffold state unless the user is genuinely moving a real project forward.
9. Use the bundled validator when phase templates or required headings change.
10. Use the bundled state checker when `docs/current_status.md` changes or when workflow coherence needs to be checked.

## Bundled resources

- `scripts/workflow_validator.py`
- `scripts/workflow_state_checker.py`

## Rules

- Do not invent evidence, experiments, or manuscript claims.
- Do not silently skip a workflow phase.
- Do not treat the validator or state checker as proof of scientific progress.
- Prefer the skeleton example and state machine over ad hoc interpretation when the workflow is ambiguous.
