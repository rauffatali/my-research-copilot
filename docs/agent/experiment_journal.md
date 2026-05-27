# Experiment Journal

This file tracks Phase 2 experimentation in a compact, reviewable form.

Use one entry per experiment stage so the execution path and outcomes remain visible.

## Suggested fields

- `stage`
- `experiment_id`
- `plan_summary`
- `code_or_config_path`
- `dataset_or_split`
- `seed`
- `metric_or_signal`
- `result_summary`
- `issue_or_blocker`
- `next_action`

## Suggested stages

- `preliminary_investigation`
- `hyperparameter_tuning`
- `research_execution`
- `ablation_study`
- `replication`
- `aggregation`

## Suggested table

| Stage | Experiment ID | Metric | Result summary | Issue / blocker | Next action |
|---|---|---|---|---|---|
| preliminary_investigation |  |  |  |  |  |

## Usage notes

- Record the smallest meaningful step, not only the final run.
- Keep failed or buggy runs visible so later agents can avoid repeating them.
- Link to configs, logs, plots, and outputs instead of embedding them here.
- Use the journal to explain why the next step changed.
