# Experiment Plan

## Status

- draft
- Allowed values: draft, approved, running, completed, cancelled, superseded

## Purpose

This file records planned experiments before they are run.

An experiment should not be considered approved unless it states:

- the research question;
- the decision the experiment will enable;
- the baseline or control;
- the experimental change;
- the metric or failure mode;
- the minimal viable version;
- what would support or refute the hypothesis;
- required output artifacts;
- the evidence to be produced;
- the verification method;
- the scope and claim boundary.

## Experiment Index

| Experiment ID | Status | Linked hypothesis | Decision enabled | Baseline/control | Target metric/failure mode | Priority | Next action |
|---|---|---|---|---|---|---|---|
| EXP-001 | draft | HYP-001 | | | | high / medium / low | |

---

## EXP-001: [Experiment Name]

### Status

- draft
- Allowed values: draft, approved, running, completed, cancelled, superseded

### Linked Research Direction

- Research direction: `docs/agent/research_direction.md`
- Hypothesis: `docs/agent/hypotheses.md#hyp-001`
- Project plan item: `docs/PROJECT_PLAN.md#...`

### Queue Source

- Queue item: `docs/agent/experiment_queue.md#...`
- Queue decision: proposed / approved_for_planning / promoted / bypassed
- Reason for promotion:
- Reason for bypassing queue, if bypassed:

### Research Question

[What exact research question does this experiment answer?]

### Decision Enabled

[What will we do differently depending on the result?]

Examples:

- proceed with method;
- reject method;
- change loss;
- add ablation;
- change dataset split;
- weaken paper claim;
- stop this line of work.

### Evidence Target and Verification

- Evidence to be produced: [State exactly what the experiment should establish, measure, or rule out.]
- Verification method: [State how the resulting evidence will be checked.]
- Scope and claim boundary: [State what this experiment may support and what it cannot establish.]
- Missing evidence or failure condition: [State what would make the evidence incomplete or unusable.]

### Baseline or Control

[What is the comparison point?]

Required details:

- baseline name;
- baseline source or implementation path;
- baseline config;
- baseline metric;
- whether baseline was reproduced, reused, or imported from literature.

### Experimental Change

[What exactly changes compared with the baseline/control?]

Be specific:

- model component:
- loss:
- data:
- training schedule:
- inference/postprocessing:
- evaluation protocol:
- prompt/template:
- other:

### Dataset / Split / Evaluation Setting

- Dataset:
- Version:
- Split:
- Evaluation subset:
- Preprocessing:
- Postprocessing:
- Any tuning on validation/test data:

Link:

- Dataset card: `docs/agent/dataset_card.md`
- Leakage audit: `docs/agent/leakage_audit.md`

### Metric or Failure Mode Targeted

- Primary metric:
- Secondary metrics:
- Target failure mode:
- Slice/subgroup of interest:
- Practical significance threshold:

### Expected Result if Hypothesis Is True

[What should happen if the hypothesis is correct?]

### Expected Result if Hypothesis Is False

[What would refute, weaken, or complicate the hypothesis?]

### Minimal Viable Experiment

[Smallest version that can change the decision.]

### Stop Condition

[When should we stop running, tuning, or extending this experiment?]

Examples:

- after N seeds;
- after budget limit;
- after baseline parity is impossible;
- after sanity check fails;
- after leakage is detected;
- after result is not decision-changing.

### Compute / Time / Cost Budget

- Expected runtime:
- Maximum acceptable runtime:
- Hardware:
- Storage:
- External API cost:
- Risk if interrupted:

### Required Output Artifacts

Before running, define the expected artifacts:

- Config path:
- Run directory:
- Log file:
- Metrics file:
- Checkpoint path:
- Plot/table path:
- Summary path:
- Registry entry:
- Result interpretation entry:
- Verification record:

### Validation Before Full Run

- [ ] Config loads.
- [ ] Data loader sanity check passes.
- [ ] Small subset run completes.
- [ ] Metric script runs.
- [ ] Baseline comparison is valid.
- [ ] Leakage risk checked.
- [ ] Outputs are saved to durable paths.
- [ ] Evidence target, verification method, and claim boundary are defined.

### Risks and Alternative Explanations

| Risk | Why it matters | Mitigation |
|---|---|---|
| | | |

### Approval

- Approved by:
- Approval date:
- Approval status: not approved / approved / explicitly deferred

### Outcome

Fill after execution.

- Result summary:
- Linked runs:
- Linked outputs:
- Linked result interpretation:
- Evidence verification result:
- Phase 3 handoff: ready / incomplete / blocked
- Decision:
- Follow-up experiment: