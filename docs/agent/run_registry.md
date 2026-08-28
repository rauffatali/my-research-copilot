# Run Registry

## Status

- draft
- Allowed values: draft, frozen, superseded

## Purpose

This file records concrete experiment executions.

An experiment plan describes what should be run.
The run registry records what was actually run.

Do not use this file for interpretation. Use it to make runs reproducible and auditable.

The registry records whether execution produced the intended artifacts and whether the execution was verified. A completed run is not interpreted evidence or claim support until Phase 3 consolidates it into a result card and a result-to-claim mapping.

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

### Evidence Binding

- Intended evidence target: [Link to the evidence target in the approved experiment plan.]
- Scope and claim boundary: [State what this run may support and what it cannot establish.]
- Expected evidence artifacts: [List the durable artifacts this run is intended to produce.]
- Execution verification status: not started / partial / complete / blocked
- Verification record: [State how code state, configuration, dataset/split, execution, metrics, and output artifacts were checked.]

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
- Evidence artifact paths:

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
