# Workflow Intake Policy

Use this policy only when workflow state is stale, template-default, contradictory, cross-phase, or unclear.

## When To Load

Load this file when:

- `docs/current_status.md` is `template_default`;
- `docs/current_status.md` is stale or contradicts durable artifacts;
- the user request crosses phases;
- the correct phase is unclear;
- a frozen artifact conflicts with live status;
- workflow validation or state checking is explicitly needed because workflow files changed, `docs/current_status.md` changed, or status coherence is in doubt.

Do not load this file for routine tasks where `docs/current_status.md` is current and the phase route is obvious from `AGENTS.md`.

## State Machine

Use `docs/workflow_state_machine.md` as the single source of truth for:

- allowed transitions;
- active versus frozen phase states;
- backward moves triggered by review or missing evidence;
- blocked and archived states.

## Role resolution

Normal simple tasks do not require role-configuration ceremony. When a request explicitly uses multiple agents, a reviewer, an execution agent, or a protected promotion/integration action, inspect `docs/agent/agent_role_profile.md` and the canonical contract at `.agents/workflow/policies/agent_role_policy.md`.

If the profile is still `template_default`, establish assignments only from explicit user instructions; do not invent project-specific model or harness assignments. Role selection determines the permissions for the invocation but does not itself change the workflow phase.

If refreshed live status still disagrees with frozen artifacts, treat the task as `blocked` until the conflict is resolved.

## Project-configuration resolution

When an operation depends on project-local operational configuration, read `docs/project_profile.md`.
This includes protected manuscript integration, venue-specific output behavior, project-type-sensitive
routing, and remote or hybrid execution assumptions.

Do not guess unresolved, invalid, or contradictory configuration fields. An explicit current human
instruction may resolve the current operation without rewriting permanent project configuration unless the
human explicitly asks for that change. Do not block unrelated work because an unrelated configuration
field remains unresolved. Keep role and writer configuration in `docs/agent/agent_role_profile.md`; do not
move it into the project profile.

## Candidate-writer resolution for substantive Phase 4 work

Only when intake routes a substantive semantic Phase 4 writing task that will produce candidates:

1. Read `docs/agent/agent_role_profile.md`.
2. Confirm that `candidate_writers_required` is present as an integer greater than or equal to 1. Missing, non-integer, zero, negative, or otherwise invalid values make writer configuration unresolved.
3. When writer configuration is unresolved, do not guess a writer count, silently use 1, silently use template default 2, or begin substantive semantic candidate drafting. Resolve it through an explicit agent-role-profile correction or explicit current human instruction. An instruction such as “Use two candidate writers for this slice” resolves the current task only and does not rewrite the permanent agent-role profile unless the human explicitly requests that change.
4. Resolve that many project-local `candidate_writer` assignments or slots from the profile and/or explicit current user instructions; never invent model or harness assignments.
5. Verify `candidate_independence_required` and `candidate_cross_visibility_before_comparison` before candidate generation.
6. If the profile remains `template_default`, explicit user instructions may establish assignments, but defaults alone do not establish actual agents.
7. If fewer than the configured count are usable, do not silently reduce the count. Candidate production stops at that boundary unless `human_researcher` explicitly authorizes a temporary lower count for the current slice.

Record the configured count, effective count, candidate slots, and any explicitly authorized temporary override in the writing brief or support artifact. If unresolved configuration genuinely blocks the active Phase 4 candidate-production task, record the blocker according to normal workflow policy; do not block unrelated work. Do not change `docs/agent/agent_role_profile.md` for a temporary override. Do not apply this resolution rule to literature search, evidence analysis, claim auditing, Phase 1-3 work, formal review, non-manuscript tasks, or closed trivial nonsemantic manuscript maintenance; update workflow status only when a missing assignment or unresolved configuration blocks the active candidate-production task.

## Stale Status Recovery

If `docs/current_status.md` is stale, template-default, or inconsistent:

1. Inspect the available durable artifacts.
2. Determine whether the project is uninitialized, bootstrapping, live, blocked, or archived.
3. Route through `intake`, `bootstrap_existing_project`, or `backfill_required`.
4. Update `docs/current_status.md` with active artifacts, blockers/open questions, and next step.

## Workflow Validation

Use the `workflow-manager` validator after project initialization or after required active artifacts have been created from templates.

Do not treat validator failure on a raw skeleton as a workflow bug when the failure is only that initialized-project artifacts such as `docs/PROJECT_PLAN.md` have not been generated yet.

The validator checks structure only:

- required artifact files exist;
- required headings are present;
- `Status` values use `draft`, `frozen`, or `superseded`;
- validated files end with `Next Step` or `Recommendation`.

Do not treat validation as evidence of scientific progress.

## State Consistency Checking

Use the workflow state checker when `docs/current_status.md` changes or workflow coherence needs checking.

The checker:

- tolerates the default `template_default` / `intake` scaffold state;
- checks that listed active artifact paths exist;
- checks phase-specific required artifacts for phase labels;
- does not replace claim, experiment, or manuscript validation.

## Example Workflow

Read `.agents/skills/workflow-manager/references/example_workflow.md` only when using the workflow skeleton for the first time in a thread or when phase flow is unclear.
