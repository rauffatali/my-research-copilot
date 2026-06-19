# Result Cards

## Purpose

This directory stores one result card per major experiment, run group, table, figure, or decision-relevant finding.

A result card converts raw outputs into interpreted evidence.

Raw metrics are not enough for manuscript claims. A claim should point to a result card, and the result card should point to runs, configs, outputs, and any relevant baseline, dataset, leakage, or ablation artifacts.

## Result Card Rule

A result is not claim-ready until it has a result card.

A result card must answer:

- What was tested?
- Which runs and outputs support it?
- What baseline or control was used?
- Whether the comparison is fair;
- What metric or failure mode was evaluated;
- Whether the result is stable, preliminary, inconclusive, or failed;
- What alternative explanations exist;
- What claim, if any, the result supports.

Do not use raw metrics directly as manuscript evidence without a result card.

## Naming

Use stable names:

- `RES-001_main_baseline_comparison.md`
- `RES-002_ablation_without_component_x.md`
- `RES-003_error_analysis_small_objects.md`
- `RES-004_negative_result_loss_variant.md`

## Status Values

Allowed result card statuses:

- `draft`
- `needs_rerun`
- `needs_baseline_check`
- `needs_leakage_check`
- `needs_error_analysis`
- `interpreted`
- `superseded`
- `invalid`

## Relationship to Other Artifacts

Input artifacts:

- `docs/agent/experiment_plan.md`
- `docs/agent/run_registry.md`
- `docs/agent/experiment_journal.md`
- `docs/agent/baseline_ledger.md`
- `docs/agent/ablation_matrix.md`
- `docs/agent/dataset_card.md`
- `docs/agent/leakage_audit.md`
- `runs/`
- `outputs/`

Output artifacts:

- `docs/agent/result_interpretation.md`
- `docs/agent/result_to_claim_map.md`
- `docs/agent/claim_ledger.md`
- `docs/agent/figure_review.md`