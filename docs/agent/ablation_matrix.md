# Ablation Matrix

## Status

- draft
- Allowed values: draft, frozen, superseded

## Purpose

This file records which components, assumptions, or design choices must be isolated.

Ablations should test the contribution mechanism, not just fill a paper table.

## Ablation Index

| Ablation ID | Linked experiment | Component isolated | Baseline/control | Expected finding | Required? | Status | Decision impact |
|---|---|---|---|---|---|---|---|
| ABL-001 | EXP-001 | | | | yes / no | planned / running / completed / cancelled | |

---

## ABL-001: [Ablation Name]

### Linked Experiment

- Experiment: `docs/agent/experiment_plan.md#exp-001`
- Hypothesis: `docs/agent/hypotheses.md#hyp-001`

### Component or Assumption Isolated

[What exactly is being removed, replaced, frozen, randomized, or controlled?]

### Why This Ablation Matters

[What mechanism or claim does it test?]

### Baseline or Control

[What is the comparison condition?]

### Expected Result if Contribution Mechanism Is Real

[What should happen?]

### Expected Result if Contribution Mechanism Is Not Real

[What would weaken or refute the mechanism?]

### Required Runs

| Run condition | Config | Seed(s) | Output path | Status |
|---|---|---|---|---|
| full method | | | | |
| without component | | | | |

### Decision Impact

Choose one:

- required_for_claim
- useful_for_diagnosis
- optional
- cancelled

### Claim Dependency

Which claim depends on this ablation?

- Claim ID:
- Claim text:
- Claim status if ablation fails:

### Outcome

- Result:
- Interpretation:
- Decision:
- Follow-up: