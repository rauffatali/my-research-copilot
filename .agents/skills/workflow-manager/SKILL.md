---
name: workflow-manager
description: Use for managing the repository's agentic workflow skeleton, including phase routing, workflow-state decisions, current-status checks, phase-template validation, and canonical workflow-example usage. Use when a task asks how the workflow should progress, whether a phase change is allowed, whether docs/current_status.md is coherent, or whether workflow templates need validation.
---

# Workflow Manager

Use this skill to manage the repository's workflow skeleton, not to fabricate project state.

## Core sources

- `docs/workflow_state_machine.md` — phase transitions
- `docs/current_status.md` — live workflow state
- `docs/project_profile.md` — operational project configuration when relevant
- `docs/agent/agent_role_profile.md` — role and writer configuration when relevant
- `docs/copilot_upstream.md` — provenance only for kernel or upstream maintenance
- `.agents/guidance/manuscript-writing.md` — canonical manuscript workflow
- `docs/agent/` — research workflow artifacts
- `paper/agent/` — manuscript-support and review artifacts

Do not load every source for every task. For manuscript workflow decisions, follow
`.agents/guidance/manuscript-writing.md`; together with `docs/workflow_state_machine.md` and
`.agents/workflow/policies/agent_role_policy.md`, it outranks stale examples or generic assumptions.
Load `docs/project_profile.md` when operational configuration affects the task, and load
`docs/agent/agent_role_profile.md` when role or writer configuration affects it. Load
`docs/copilot_upstream.md` and `.agents/workflow/policies/upstream_sync_policy.md` only for
kernel/upstream synchronization or update work.

When role permissions matter, follow `.agents/workflow/policies/agent_role_policy.md`. When tool use or
durable-output behavior matters, follow `.agents/workflow/policies/tool_workflow_policy.md`. When
operational project configuration matters, follow
`.agents/workflow/policies/project_configuration_policy.md`.

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
9. Use the bundled validator after project initialization, or after creating required active artifacts from templates.
10. Use the bundled state checker when `docs/current_status.md` changes or when workflow coherence needs to be checked.

## Bundled resources

- `scripts/workflow_validator.py`
- `scripts/workflow_state_checker.py`

## Rules

- Do not invent evidence, experiments, or manuscript claims.
- Do not silently skip a workflow phase.
- Do not treat the validator or state checker as proof of scientific progress.
- Prefer the skeleton example and state machine over ad hoc interpretation when the workflow is ambiguous.

## Role-aware durable output

Writable roles follow the normal durable-artifact requirements in the tool policy. When the active role is `independent_reviewer`, its strict read-only boundary overrides a skill's ordinary write or status-update behavior: return workflow findings in the response and do not write review artifacts or status files. A writable role may later record accepted or adjudicated findings.

## Candidate-writer configuration

For substantive semantic Phase 4 candidate production, read `docs/agent/agent_role_profile.md` and
enforce `candidate_writers_required`, `candidate_independence_required`, and
`candidate_cross_visibility_before_comparison`. Do not invent missing assignments or silently reduce the
configured count. A temporary reduction requires explicit `human_researcher` authorization for the
current slice. Candidate slots remain project-local identifiers, and the strict `independent_reviewer`
read-only carve-out remains in force.

## Tool Workflow Policy

Follow `.agents/workflow/policies/tool_workflow_policy.md`.

For writable roles, useful workflow-changing output must be recorded in the appropriate durable repository
artifact rather than left only in chat. `independent_reviewer` remains response-only under the role policy
and does not write workflow artifacts.

When this skill changes workflow state, active artifacts, blockers, claim status, experiment status, manuscript state, or next step, update `docs/current_status.md`.
