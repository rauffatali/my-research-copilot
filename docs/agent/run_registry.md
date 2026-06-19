# Run Registry

## Status

- draft
- Allowed values: draft, frozen, superseded

## Purpose

This file records concrete experiment executions.

An experiment plan describes what should be run.
The run registry records what was actually run.

Do not use this file for interpretation. Use it to make runs reproducible and auditable.

## Run Index

| Run ID | Experiment ID | Status | Commit | Config | Dataset/split | Seed | Output path | Metric summary | Notes |
|---|---|---|---|---|---|---|---|---|---|
| RUN-001 | EXP-001 | planned / running / completed / failed / cancelled | | | | | | | |

---

## RUN-001

### Status

- planned
- Allowed values: planned, running, completed, failed, cancelled, superseded

### Linked Experiment

- Experiment plan: `docs/agent/experiment_plan.md#exp-001`

### Code State

- Git commit:
- Branch:
- Dirty working tree: yes / no / unknown
- Relevant files changed:
- Environment file:
- Dependency lockfile:

### Config

- Config path:
- Config hash, if available:
- Important parameters:
  - model:
  - data:
  - training:
  - evaluation:
  - seed:
  - hardware:

### Data

- Dataset:
- Dataset version:
- Split:
- Data path:
- Preprocessing:
- Dataset card:
- Leakage audit:

### Execution

- Command:
- Start time:
- End time:
- Runtime:
- Hardware:
- Exit status:

### Outputs

- Run directory:
- Log path:
- Metrics path:
- Checkpoint path:
- Prediction path:
- Figure/table path:
- Other artifacts:

### Metrics

| Metric | Value | Notes |
|---|---:|---|
| | | |

### Failure or Warning Notes

- [Record errors, warnings, instability, incomplete outputs, or suspicious behavior.]

### Reproducibility Notes

- [State what another agent/human needs to reproduce this run.]

### Next Step

- [State next action.]