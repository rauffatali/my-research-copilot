# Experiment Journal

## Purpose

This file is the chronological index of experiment activity.

It should not replace:

- `docs/agent/experiment_plan.md`
- `docs/agent/run_registry.md`
- `docs/agent/baseline_ledger.md`
- `docs/agent/ablation_matrix.md`
- `docs/agent/dataset_card.md`
- `docs/agent/leakage_audit.md`

Use this file to preserve the execution path, failed attempts, pivots, blockers, and next actions.

For each meaningful execution step, link the durable evidence artifacts involved and record execution verification separately from interpretation. This journal preserves chronology and decisions; it does not assign claim support.

## Status

- draft
- Allowed values: draft, frozen, superseded

## Journal

| Date | Stage | Queue item | Experiment ID | Linked plan | Linked runs | Evidence references | Verification status | Summary | Issue / blocker | Decision / next action |
|---|---|---|---|---|---|---|---|---|---|---|
| YYYY-MM-DD | main_experiment | `docs/agent/experiment_queue.md#...` | EXP-001 | `docs/agent/experiment_plan.md#exp-001` | `docs/agent/run_registry.md#run-001` | | not started / partial / complete / blocked | | | |

## Suggested Stages

- `preliminary_investigation`
- `sanity_check`
- `baseline_replication`
- `main_experiment`
- `ablation_study`
- `hyperparameter_tuning`
- `failure_analysis`
- `rerun`
- `aggregation`
- `cancelled`

## Usage Rules

- Record the smallest meaningful experiment step.
- Keep failed, buggy, cancelled, or inconclusive runs visible.
- Link to configs, logs, plots, checkpoints, and outputs instead of embedding them here.
- Use durable paths for evidence references; raw chat, lookup output, or unrecorded tool output is not evidence.
- Keep verification status consistent with the linked run registry entry and use it to describe execution checks, not claim support.
- Do not use this file as the only evidence for a manuscript claim.
- If a run changes the research direction, mark the decision and route back to Phase 1 or `backfill_required`.

## Next Step

- [State the next experiment action.]
