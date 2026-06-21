# Result Card: RES-XXX — [Short Name]

## Status

- draft
- Allowed values: draft, needs_rerun, needs_baseline_check, needs_leakage_check, needs_error_analysis, interpreted, superseded, invalid

## Summary

[One-sentence summary of the result.]

## Linked Research Context

- Research direction: `docs/agent/research_direction.md`
- Hypothesis: `docs/agent/hypotheses.md#...`
- Experiment plan: `docs/agent/experiment_plan.md#...`
- Experiment queue item, if any: `docs/agent/experiment_queue.md#...`

## Linked Execution Artifacts

- Run registry entry:
- Experiment journal entry:
- Config path:
- Run path:
- Output path:
- Metrics file:
- Predictions file:
- Figure/table path:
- Commit:
- Seed(s):

## What Was Tested

[Describe exactly what was evaluated.]

Include:

- method/component/change tested;
- baseline or control;
- dataset/split;
- metric or failure mode;
- evaluation setting.

## Baseline / Control Check

- Baseline ID:
- Baseline artifact: `docs/agent/baseline_ledger.md#...`
- Comparison validity: valid / conditionally_valid / invalid / unknown
- Notes:

Explain whether this is a fair comparison.

## Dataset and Leakage Check

- Dataset: `docs/agent/dataset_card.md#...`
- Leakage audit: `docs/agent/leakage_audit.md#...`
- Leakage status: passed / failed / partial / unknown / not_applicable
- Notes:

## Main Metrics

| Metric | Proposed | Baseline / Control | Difference | Direction | Notes |
|---|---:|---:|---:|---|---|
| | | | | improves / worsens / neutral / unclear | |

## Stability

- Number of seeds:
- Variance or confidence interval:
- Rerun needed: yes / no / unknown
- Stability status: stable / preliminary / unstable / single_run / not_applicable

## Qualitative Evidence

[Summarize representative qualitative examples.]

Do not include cherry-picked examples only.

Link examples when possible:

- Example file:
- Prediction sample:
- Visualization:

## Slice / Subgroup Analysis

| Slice | Result | Interpretation | Concern |
|---|---|---|---|
| | | | |

## Error Analysis Summary

- Linked error analysis: `docs/agent/error_analysis.md#...`
- Main failure modes:
  - 
  - 
  - 

## Negative or Inconclusive Findings

- Linked negative result, if any: `docs/agent/negative_results.md#...`
- What did not work:
- What was inconclusive:

## Alternative Explanations

What else could explain the result?

Examples:

- baseline implementation mismatch;
- data leakage;
- metric artifact;
- hyperparameter tuning;
- random seed effect;
- dataset bias;
- preprocessing difference;
- compute budget difference;
- evaluation mismatch.

## Interpretation

[What does the result actually mean?]

Be conservative.

## Supported or Affected Claims

| Claim ID | Claim | Support Status | Notes |
|---|---|---|---|
| CL-XXX | | supported / partially_supported / preliminary / hypothesis / needs_citation / wrong_citation / unsupported / contradicted / out_of_scope / needs_manual_check | |

## Claims to Update

| Claim ID | Claim | New Support Status | Reason |
|---|---|---|---|
| CL-XXX | | partially_supported / preliminary / unsupported / contradicted / out_of_scope / needs_manual_check | |

## Claim Boundaries

This result supports claims about:

- 

This result does not support claims about:

- 

## Decision

Choose one:

- proceed
- rerun
- run_ablation
- run_error_analysis
- update_claim_ledger
- weaken_claim
- reject_hypothesis
- change_direction
- stop_line_of_work

## Next Step

[Concrete next action.]