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

If refreshed live status still disagrees with frozen artifacts, treat the task as `blocked` until the conflict is resolved.

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