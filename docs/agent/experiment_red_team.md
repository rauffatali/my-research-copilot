# Experiment Red-Team

## Purpose

This file records critique of planned experiments before they are run.

Use it to avoid experiments that are expensive, non-decision-changing, unfairly compared, leaky, underpowered, or unlikely to answer the research question.

## Status

- Status: `draft`
- Allowed values: `draft`, `completed`, `superseded`
- Experiment red-team recorded: `no`

## Experiment Red-Team Rule

Red-team an experiment before running it when:

- it is expensive or long-running;
- it will support a main claim;
- it affects baseline, dataset, metric, or evaluation protocol;
- it is likely to appear in the paper;
- failure would force a direction change;
- the experiment has unclear decision value.

## Red-Team Table

No experiment red-team findings have been recorded yet.

| Issue ID | Experiment ID | Concern | Severity | Required Fix | Decision |
|---|---|---|---|---|---|

## EXP-XXX: [Experiment Name]

### Linked Artifacts

- Experiment queue item:
- Experiment plan:
- Baseline ledger:
- Dataset card:
- Leakage audit:
- Ablation matrix:

### 1. What decision will this experiment change?

[Answer.]

### 2. What would make this experiment meaningless?

[Answer.]

### 3. Is the baseline/control fair?

[Answer.]

### 4. Is the dataset/split/evaluation protocol safe?

[Answer.]

### 5. What leakage risk remains?

[Answer.]

### 6. What cheaper experiment could answer the same question?

[Answer.]

### 7. What alternative explanation could explain a positive result?

[Answer.]

### 8. What reviewer criticism is likely?

[Answer.]

### 9. What must be fixed before running?

[Answer.]

## Decision

Choose one:

- `approve_to_run`
- `run_minimal_version_first`
- `revise_experiment_plan`
- `add_baseline`
- `add_ablation`
- `fix_dataset_or_leakage_issue`
- `defer`
- `cancel`

## Follow-Up Actions

| Action | Target artifact | Status |
|---|---|---|
| | | |

## Next Step

[State the next action.]