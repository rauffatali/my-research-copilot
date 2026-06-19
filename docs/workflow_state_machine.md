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
| `phase_1_active` | Research direction is being debated and formed | Frozen Phase 1 artifact package exists after evidence review, user questioning, and approval |
| `phase_2_active` | Implementation or experiment work is being executed | Approved plan implemented and validated or explicitly deferred |
| `phase_3_active` | Results are being consolidated into evidence | Stable evidence package and claim labels exist |
| `phase_4_active` | Manuscript drafting or revision is in progress | Claims are traceable to evidence and citations |
| `phase_5_active` | Review or red-team feedback is being organized | Revision decision is clear |
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
| `intake` | `phase_1_active` | A research direction, implementation task, result task, writing task, or review task has been classified |
| `phase_1_active` | `phase_1_frozen` | Direction is concrete enough to support baseline, metric, risk, and validation criteria, and the user has approved proceeding after an evidence-backed debate round |
| `phase_1_frozen` | `phase_2_active` | Implementation is authorized |
| `phase_2_active` | `phase_2_frozen` | Plan is implemented and validation is complete or deferred with reason |
| `phase_2_frozen` | `phase_3_active` | Results exist and need consolidation |
| `phase_3_active` | `phase_3_frozen` | Evidence package and claim labels are stable |
| `phase_3_frozen` | `phase_4_active` | Manuscript drafting can begin |
| `phase_4_active` | `phase_4_frozen` | Draft section or claim package is stable |
| `phase_4_frozen` | `phase_5_active` | Manuscript is ready for review |
| `phase_5_active` | `phase_4_active` | Review requires revision of the manuscript |
| `phase_5_active` | `phase_3_active` | Review exposes a missing or weak evidence package |
| `phase_5_active` | `phase_1_active` | Review invalidates the research direction itself |
| `phase_5_active` | `archived` | Review cycle is complete and no further action is required |
| any state | `blocked` | A dependency, blocker, or missing artifact prevents progress |
| `blocked` | previous active state | The blocker is resolved |

## Transition Rules

1. Do not skip phases unless the missing upstream work is truly irrelevant.
2. Do not silently move from one phase to another without updating `docs/current_status.md`.
3. Do not overwrite a frozen artifact when downstream work depends on it; create a revision note instead.
4. If a review changes the research direction, move back to Phase 1 rather than patching Phase 4 text.
5. If a review only exposes missing evidence, move back to Phase 3 rather than rewriting claims first.
6. If work stalls because of missing information or files, mark the state as `blocked`.

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

## Artifact Discipline

- `docs/agent/` stores Phase 1 to Phase 3 working artifacts.
- `paper/agent/` stores Phase 4 to Phase 5 manuscript-support artifacts.
- `sources/` stores external evidence artifacts.
- `docs/current_status.md` stores the live state pointer.

## Minimal Canonical Flow

`intake` -> `phase_1_active` -> `phase_1_frozen` -> `phase_2_active` -> `phase_2_frozen` -> `phase_3_active` -> `phase_3_frozen` -> `phase_4_active` -> `phase_4_frozen` -> `phase_5_active` -> `archived`

## Notes

- The workflow is linear by default, but review can send it backward.
- Only material scope changes should reset the work to an earlier phase.
- The current state should always be recoverable from the live status file plus the frozen artifacts.
