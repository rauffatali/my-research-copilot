# Error Analysis

## Purpose

This file records where, how, and why the method fails.

Error analysis should identify failure modes, not just bad examples.

Use this file when:

- aggregate metrics hide important behavior;
- qualitative examples reveal systematic failures;
- reviewer-facing robustness claims are possible;
- a result card needs explanation;
- a method improves average performance but fails on important slices.

## Status

- draft
- Allowed values: draft, in_progress, completed, superseded

## Error Analysis Index

| Error ID | Linked result | Failure mode | Severity | Status | Claim impact |
|---|---|---|---|---|---|
| ERR-001 | RES-001 | | low / medium / high | draft / completed | |

---

## ERR-001: [Failure Mode Name]

### Linked Artifacts

- Result card:
- Experiment:
- Run(s):
- Output path:
- Prediction examples:
- Figure/table:

### Failure Mode

[Describe the failure mode.]

### Evidence

[Link examples, slices, metrics, or qualitative observations.]

### Frequency

- Number of observed failures:
- Percentage, if known:
- Slice/subgroup:
- Whether this is systematic or anecdotal:

### Severity

Choose one:

- low
- medium
- high
- paper_critical

### Likely Cause

Possible causes:

- data issue;
- model limitation;
- metric mismatch;
- preprocessing issue;
- label ambiguity;
- distribution shift;
- baseline artifact;
- implementation bug;
- prompt/template issue;
- unknown.

### Alternative Explanations

[What else might explain this failure?]

### Claim Impact

Which claims are affected?

| Claim ID | Impact | Required change |
|---|---|---|
| CL-XXX | weaken / remove / caveat / no_change | |

### Follow-Up

Choose one:

- no_action
- add_caveat
- run_slice_analysis
- run_ablation
- fix_bug
- change_method
- collect_more_data
- update_claim_ledger

### Next Step

[Concrete next action.]