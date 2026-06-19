# Experiment Queue

## Status

- draft
- Allowed values: draft, frozen, superseded

## Purpose

This file prioritizes candidate experiments before they become approved experiment plans.

Use this to avoid running experiments just because they are easy.

## Queue

| Priority | Queue ID | Experiment idea | Linked hypothesis | Decision enabled | Expected information gain | Cost | Risk | Status | Promotion target |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | QUEUE-001 | | HYP-001 | | high / medium / low | high / medium / low | | proposed / approved_for_planning / promoted / deferred / cancelled / superseded | `docs/agent/experiment_plan.md#exp-001` |

## Queue Rules

This file is the triage layer for candidate experiments.

A queue item is a candidate experiment, not an approved experiment and not evidence.

Queue items are used to compare possible next experiments by:

- linked hypothesis or research direction;
- decision enabled;
- expected information gain;
- cost;
- risk;
- dependency;
- priority;
- status.

A queue item may be promoted to an experiment plan only when it has:

- a linked hypothesis or research direction;
- a decision it will enable;
- a baseline or control;
- an experimental change;
- a target metric or failure mode;
- a minimal viable version;
- expected outcomes if the hypothesis is true or false;
- a stop condition.

Promote one queue item at a time unless batch planning is explicitly needed.

Do not run a vague queue item directly.

Do not treat a queued experiment as completed work.

Do not use a queued experiment to support a paper claim.

## Rules

- Prefer experiments that change a decision.
- Prefer cheap kill-tests before expensive full runs.
- Defer experiments with low information gain.
- Cancel experiments whose decision has already been resolved.
- Promote an item to `experiment_plan.md` only when it is ready to run.

## Next Step

- [State the next experiment to plan.]