# Workflow State Machine

This document is the canonical source of truth for workflow transitions.

## Purpose

The repository workflow is not just five phases in sequence. It is a state machine with explicit entry conditions, exit conditions, and permitted backward transitions.

Use this document when deciding:

- which phase is active;
- whether an artifact is draft or frozen;
- whether a task may move forward;
- whether a review or failure forces a step back.

## Canonical States

| State | Meaning | Exit condition |
|---|---|---|
| `intake` | New request has been classified but not yet routed | A phase is selected |
| `bootstrap_existing_project` | The repo already contains research/code/results/paper artifacts, but the live phase is not yet known | Existing artifacts have been inspected and the correct active phase is selected |
| `backfill_required` | The requested phase is clear, but one or more required upstream artifacts are missing and must be reconstructed from existing project context | Missing prerequisite artifacts are created or explicitly marked unavailable |
| `phase_1_active` | Research direction is being debated and formed | Frozen Phase 1 artifact package exists after evidence review, user questioning, and approval |
| `phase_2_active` | Implementation or experiment work is being executed | Approved plan implemented and validated or explicitly deferred |
| `phase_3_active` | Results are being consolidated into evidence | Stable evidence package and claim labels exist |
| `phase_4_active` | Provisional writing-slice drafting or revision with embedded pre-integration review | Writing-slice draft and support decisions are stable and reviewable |
| `phase_5_active` | Formal broader manuscript or coherent-manuscript-unit review | Revision decision is clear |
| `blocked` | Work cannot proceed because a required dependency, artifact, or decision is missing | Return to the previous active state after the blocker is resolved |
| `archived` | Workflow for the current thread is complete and closed | Start a new intake if new work is needed |

## Frozen States

Each active phase may be frozen once its required artifact package is complete:

- `phase_1_frozen`
- `phase_2_frozen`
- `phase_3_frozen`
- `phase_4_frozen`

Frozen means the phase output is reviewable and should not be silently redefined during downstream work.

## Allowed Transitions

| From | To | When |
|---|---|---|
| `intake` | `bootstrap_existing_project` | The workspace already contains project artifacts, but the current research phase is unknown or `docs/current_status.md` is missing, stale, or inconsistent |
| `intake` | `phase_1_active` | The user is asking for idea formation, problem framing, novelty exploration, research direction selection, or the project has no usable frozen direction |
| `intake` | `phase_2_active` | The user is asking for implementation, experiment setup, code changes, or benchmark execution, and a usable research direction exists or can be backfilled |
| `intake` | `phase_3_active` | The user is asking for result analysis, metric interpretation, table building, error analysis, or claim-status updates, and run/output artifacts exist |
| `intake` | `phase_4_active` | The user is asking for manuscript drafting, section rewriting, citation-supported writing, or paper polishing, and a stable evidence or claim package exists |
| `intake` | `phase_5_active` | The user is asking for review, red-team critique, rebuttal planning, revision planning, or reviewer simulation, and a manuscript or reviewable draft exists |
| `intake` | `backfill_required` | The requested phase is clear, but required upstream artifacts are missing and can likely be reconstructed from existing code, outputs, sources, or manuscript files |
| `intake` | `blocked` | The requested phase is clear, but required upstream artifacts are missing and cannot be reconstructed without user input |
| `bootstrap_existing_project` | `phase_1_active` | No usable research direction, hypothesis, baseline, metric, or evaluation target can be found |
| `bootstrap_existing_project` | `phase_2_active` | A usable research direction exists, but implementation or experiment work is the next active task |
| `bootstrap_existing_project` | `phase_3_active` | Run artifacts, metrics, logs, outputs, or evaluation tables exist and need consolidation |
| `bootstrap_existing_project` | `phase_4_active` | A stable evidence package exists and manuscript drafting or revision is the next active task |
| `bootstrap_existing_project` | `phase_5_active` | A manuscript draft or review package exists and critique, revision, or rebuttal planning is the next active task |
| `bootstrap_existing_project` | `backfill_required` | The likely target phase is identifiable, but required handoff artifacts are missing |
| `bootstrap_existing_project` | `blocked` | The project state cannot be determined from available files |
| `backfill_required` | `phase_1_active` | The missing artifact is a research direction or novelty/evaluation framing that cannot be reconstructed safely |
| `backfill_required` | `phase_2_active` | Minimal Phase 1 handoff has been reconstructed and implementation or experiment work can proceed |
| `backfill_required` | `phase_3_active` | Minimal Phase 1/2 handoff has been reconstructed and existing results can be interpreted |
| `backfill_required` | `phase_4_active` | Minimal evidence and claim handoff has been reconstructed and writing can proceed |
| `backfill_required` | `phase_5_active` | Minimal manuscript/review context has been reconstructed and review can proceed |
| `backfill_required` | `blocked` | Backfill requires unavailable files, missing user decisions, or unavailable experiment outputs |
| `phase_1_active` | `phase_1_frozen` | Direction is concrete enough to support baseline, metric, risk, and validation criteria, and the user has approved proceeding after an evidence-backed debate round |
| `phase_1_frozen` | `phase_2_active` | Implementation is authorized |
| `phase_2_active` | `phase_2_frozen` | Plan is implemented and validation is complete or deferred with reason |
| `phase_2_frozen` | `phase_3_active` | Results exist and need consolidation |
| `phase_3_active` | `phase_3_frozen` | Evidence package and claim labels are stable |
| `phase_3_frozen` | `phase_4_active` | Manuscript drafting can begin |
| `phase_4_active` | `phase_4_frozen` | Writing-slice draft and support decisions are stable and reviewable; no main-manuscript integration is implied |
| `phase_4_frozen` | `phase_5_active` | A broader manuscript or coherent-unit review target is ready and prerequisites are satisfied; not every frozen slice enters Phase 5 |
| `phase_5_active` | `phase_4_active` | Review requires revision of the manuscript |
| `phase_5_active` | `phase_3_active` | Review exposes a missing or weak evidence package |
| `phase_5_active` | `phase_1_active` | Review invalidates the research direction itself |
| `phase_5_active` | `archived` | Review cycle is complete and no further action is required |
| any state | `blocked` | A dependency, blocker, or missing artifact prevents progress |
| `blocked` | previous active state | The blocker is resolved |

## Transition Rules

1. Do not skip required prerequisites. However, an existing project may enter directly into Phase 2, 3, 4, or 5 if the required upstream context already exists or can be backfilled.
2. When a user request targets an existing project, route by the requested work and available artifacts, not by the new-project canonical sequence.
3. If the target phase is clear but required upstream artifacts are missing, use `backfill_required` instead of forcing a restart from Phase 1.
4. Use `blocked` only when the missing information cannot be reconstructed from repository files, saved sources, outputs, runs, or manuscript artifacts.
5. Backfilled artifacts must be marked as reconstructed, not frozen, unless the user explicitly approves them.
6. Do not silently invent missing upstream decisions during backfill. Record uncertainty and ask only for the smallest missing decision if progress is impossible without it.
7. Do not silently move from one phase to another without updating `docs/current_status.md`.
8. Do not overwrite a frozen artifact when downstream work depends on it; create a revision note instead.
9. If a review changes the research direction, move back to Phase 1 rather than patching Phase 4 text.
10. If a review only exposes missing evidence, move back to Phase 3 rather than rewriting claims first.
11. If work stalls because of missing information or files, mark the state as `blocked`.

## Blocked, Archived, and Rollback Rules

1. Use `blocked` only when progress is prevented by a concrete missing dependency, artifact, or decision.
2. Keep the task in its current phase when the issue is only an open question; do not overuse `blocked`.
3. Return from `blocked` to the same active state that was interrupted once the blocker is resolved.
4. Treat `archived` as terminal for the current thread.
5. If new work appears after `archived`, start a new intake rather than reopening archived work in place.
6. After review, use these rollback paths:
   - `phase_5_active` -> `phase_4_active` when the manuscript needs revision but the evidence package is still valid.
   - `phase_5_active` -> `phase_3_active` when the evidence package is incomplete, weak, or misaligned with the claim.
   - `phase_5_active` -> `phase_1_active` when the research direction itself is wrong or materially refuted.
   - `phase_5_active` -> `blocked` when external work is required before any revision can continue.
7. Do not rewrite claims in Phase 4 if the evidence package itself is the problem; fix the upstream phase first.

## Existing Project Detection

During `bootstrap_existing_project`, inspect the repository for these signals:

| Signal | Likely phase |
|---|---|
| No clear research question, no direction file, no hypothesis, no baseline, no metric | Phase 1 |
| Frozen or usable research direction exists and implementation, code, configuration, or experiment setup is still incomplete or actively being developed | Phase 2 |
| Runs, metrics, logs, outputs, or other executed-result artifacts exist and require consolidation, interpretation, verification, or claim mapping | Phase 3 |
| Stable evidence package, claim ledger, result interpretation, paper outline, or provisional manuscript writing slices exist and manuscript drafting/revision is the active task | Phase 4 |
| A broader integrated manuscript or coherent manuscript-unit review target exists together with formal review activity such as reviewer feedback, rebuttal work, meta-review, or broader revision planning | Phase 5 |

Artifact signals are not absolute. Choose the latest phase whose actual prerequisites are satisfied.

Code or configuration existence alone does not imply Phase 3; if implementation or experiment setup is
still active or incomplete, the project remains in Phase 2. A manuscript draft alone does not imply
Phase 5; provisional manuscript drafting or revision normally remains in Phase 4. Phase 5 requires a
broader formal review target consistent with the canonical Phase 5 contract.

If the latest phase has weak or missing prerequisites, enter `backfill_required`.

## Backfill Discipline

Backfill is allowed when the project clearly contains enough evidence to reconstruct missing handoff artifacts.

Examples:

- Existing code and experiment configs can backfill part of Phase 2 planning.
- Existing metrics and logs can backfill a result summary.
- Existing paper claims can backfill a draft claim ledger, but unsupported claims must be marked.
- Existing related-work notes can backfill source context, but missing citations must be marked.

Backfill must not pretend that reconstructed context was originally approved.

Use these labels in backfilled artifacts:

- `reconstructed`
- `assumed`
- `needs_user_confirmation`
- `needs_evidence`
- `safe_to_use`

A backfilled artifact may support progress, but it should not become frozen until reviewed or approved.

## Artifact Discipline

- `docs/agent/` stores Phase 1 to Phase 3 working artifacts.
- `paper/agent/` stores Phase 4 to Phase 5 manuscript-support artifacts.
- `sources/` stores external evidence artifacts.
- `docs/research_context.md` stores the stable, high-level project snapshot created in Phase 1; it is a framing reference, not a decision log.
- `docs/current_status.md` stores the live state pointer.

## Tool Workflow Discipline

Tool use does not create a workflow state by itself.

Tools, skills, MCP servers, lookup systems, retrieval systems, code execution, and automated helpers must operate inside the current workflow state.

If tool output changes the research direction, implementation plan, experiment state, result interpretation, claim support, manuscript state, review status, blocker, or next step, update `docs/current_status.md`.

If tool output reveals that the current state lacks required prerequisites, route to the earliest valid prerequisite state, such as `backfill_required`, `phase_1_active`, `phase_2_active`, or `phase_3_active`.

Do not use tool success as evidence that a workflow phase is complete.

A phase is complete only when the required durable artifacts and exit conditions are satisfied.

### Experiment Queue Discipline

`docs/agent/experiment_queue.md` is a Phase 2 triage artifact.

Use it when:

- multiple candidate experiments exist;
- compute, time, or cost is limited;
- the next experiment is unclear;
- a proposed change needs prioritization before implementation;
- a reviewer or result analysis suggests several possible follow-up experiments.

A queue item is not an approved experiment.
A queue item becomes runnable only after it is promoted to `docs/agent/experiment_plan.md`.

Queued experiments may be:

- proposed;
- approved_for_planning;
- deferred;
- cancelled;
- superseded;
- promoted.

Do not move from a vague queue item directly to execution.
Do not treat a queue item as evidence for a claim.

## Current Status Freshness

`docs/current_status.md` is the live state pointer, but it may be stale when the scaffold is first cloned into an existing project or when project artifacts have changed without a status update.

A status file should be treated as stale when:

- `Status type` is `template_default` but project-specific artifacts exist;
- listed active artifacts do not exist;
- listed blockers have already been resolved;
- the status phase is earlier than the latest valid project evidence;
- the status conflicts with frozen artifacts, run outputs, claim ledgers, or manuscript artifacts.

When status is stale:

1. Do not use stale status as project truth.
2. Inspect durable artifacts.
3. Route through `intake`, `bootstrap_existing_project`, or `backfill_required`.
4. Rewrite `docs/current_status.md` before continuing downstream work.

Use `blocked` only when the conflict cannot be resolved from available artifacts.

## Canonical Flows

### New project flow

Use this when the repo starts from a broad idea or empty research scaffold:

`intake` -> `phase_1_active` -> `phase_1_frozen` -> `phase_2_active` -> `phase_2_frozen` -> `phase_3_active` -> `phase_3_frozen` -> `phase_4_active` -> `phase_4_frozen` -> (when a broader review target is ready) `phase_5_active` -> `archived`

### Existing project bootstrap flow

Use this when the scaffold is cloned into a project that already has code, runs, outputs, sources, or paper files:

`intake` -> `bootstrap_existing_project` -> selected active phase

The selected active phase may be Phase 1, 2, 3, 4, or 5 depending on available artifacts.

### Existing project with missing handoff artifacts

Use this when the user is clearly asking for a downstream task, but the required handoff artifacts are incomplete:

`intake` -> `backfill_required` -> selected active phase

Backfill should reconstruct only the minimum context needed to proceed.

## Manuscript review boundary and integration gate

Slice-local review is an embedded Phase 4 loop. It is writing-slice-local and pre-integration, remains within `phase_4_active`, and does not cause a transition to Phase 5 for every slice. Phase 5 is formal broader review of an integrated manuscript or coherent manuscript unit and is entered only when that target and its prerequisites are ready.

`research_lead` may determine that a writing slice is scientifically ready, but that readiness does not authorize integration. `human_researcher` must explicitly authorize protected main-manuscript integration, and `integration_agent` performs the separate protected action.

Immediately before integration, revalidate changeable implementation, experiment, result, citation, external-evidence, and claim-support dependencies. Keep `evidence_state` (the lifecycle or readiness of a dependency) separate from `support_status` (support for the exact claim wording): a completed run is not necessarily `evidence_ready`, and `evidence_ready` is not necessarily `supported`. Confirm that an adequate rollback or focused-diff mechanism exists. If no adequate mechanism exists, block integration but allow drafting in `paper/draft/` to continue.

Resolve the protected manuscript target through the project-local configuration source:

```text
docs/project_profile.md
→ main_manuscript_path
```

- A configured valid project-relative path is the protected integration target.
- `UNASSIGNED`, a missing value, or an invalid path means do not guess; drafting in `paper/draft/` may continue, but protected integration cannot.
- `NOT_APPLICABLE` means protected integration is not part of normal project configuration.
- An explicit human task-scoped target may resolve the current operation without changing the profile unless the human requests a permanent update.

This target-resolution rule does not grant write authority. The separate `human_researcher` authorization
gate and `integration_agent` role remain required.

For substantive semantic Phase 4 candidate production, resolve `candidate_writers_required`,
`candidate_independence_required`, and `candidate_cross_visibility_before_comparison` from
`docs/agent/agent_role_profile.md`. Missing or invalid required writer configuration fails closed for
candidate production rather than being guessed. The state machine does not impose a universal candidate
count or add a workflow state for writer configuration.

Formal Phase 5 review does not reproduce the ordinary candidate-writing loop. If it requires prose revision, return to Phase 4; if it exposes evidence failure, return to Phase 3; if it invalidates the research direction, return to Phase 1.

## Notes

- The workflow is linear only for new projects.
- Existing projects should resume from the latest valid research state.
- Do not reset to Phase 1 unless the research direction is missing, invalid, or materially changed.
- Review can still send work backward to Phase 4, Phase 3, or Phase 1.
- The current state should always be recoverable from `docs/current_status.md` plus available frozen, draft, or reconstructed artifacts.
