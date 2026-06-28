# Phase 3 Contract: Result Consolidation and Claim Support

## Purpose

Convert experiment outputs into interpreted evidence and claim support decisions.

Phase 3 should not merely summarize metrics. It should determine what the results actually support, what they do not support, and what claims must be strengthened, weakened, or removed.

## Inputs

Expected inputs may include:

- `docs/agent/experiment_plan.md`
- `docs/agent/run_registry.md`
- `docs/agent/experiment_journal.md`
- `docs/agent/baseline_ledger.md`
- `docs/agent/ablation_matrix.md`
- `docs/agent/dataset_card.md`
- `docs/agent/leakage_audit.md`
- Saved runs, logs, metrics, configs, checkpoints, and outputs from Phase 2 in `runs/` and `outputs/`.
- Relevant source artifacts in `sources/`.
- Frozen Phase 1 artifacts for comparison against the original research intent.

## Actions

1. Inspect the relevant experiment plans, run registry entries, logs, metrics, and outputs.
2. Create or update a result card in `docs/agent/result_cards/` for each major result or decision-relevant finding.
3. Check baseline/control validity before interpreting comparison claims.
4. Check dataset and leakage status before interpreting evaluation claims.
5. Record instability, failed runs, inconclusive results, or non-improvements in `docs/agent/negative_results.md`.
6. Perform error or slice analysis in `docs/agent/error_analysis.md` when aggregate metrics are insufficient.
7. Synthesize result cards in `docs/agent/result_interpretation.md`.
8. Map interpreted results to claims in `docs/agent/result_to_claim_map.md`.
9. Before freezing evidence or promoting results into manuscript claims, red-team the evidence in `docs/agent/evidence_review.md`.
10. Record concrete evidence-review issues in `docs/agent/red_team_issue_ledger.md` when they require follow-up.
11. If evidence review finds a missing baseline, leakage risk, unstable result, unsupported claim, or plausible alternative explanation, update the relevant result card, result-to-claim map, claim ledger, or route back to Phase 2.
12. Update `docs/agent/claim_ledger.md` using only the shared support-status vocabulary:
   * `supported`
   * `partially_supported`
   * `preliminary`
   * `hypothesis`
   * `needs_citation`
   * `wrong_citation`
   * `unsupported`
   * `contradicted`
   * `out_of_scope`
   * `needs_manual_check`
13. Keep support status separate from decisions or next actions. For example, `unsupported` is a support status, while `remove`, `rewrite`, `weaken_claim`, or `run_ablation` are decisions or next actions.
14. Review figures and tables through `docs/agent/figure_review.md` before using them in manuscript writing.
15. Update `docs/current_status.md` when the active evidence state, claim status, or next phase changes.


## Relevant Skills

Use the smallest relevant set:

- `results-scaffold` when result tables, comparison layouts, or result-section scaffolds are needed.
- `claim-auditor` when mapping interpreted results to claim support.
- `scientific-critical-thinking` when testing alternative explanations, missing baselines, leakage risk, or evidence strength.
- `literature-review` when comparison context is needed.

## Outputs

Expected Phase 3 artifacts include:

- `docs/agent/result_cards/`
- `docs/agent/result_interpretation.md`
- `docs/agent/error_analysis.md`
- `docs/agent/negative_results.md`
- `docs/agent/result_to_claim_map.md`
- `docs/agent/figure_review.md`
- `docs/agent/claim_ledger.md`

## Exit Conditions

Phase 3 can be frozen only when:

- major results have result cards;
- result cards link to runs, outputs, and relevant experiment plans;
- comparison claims have baseline/control support;
- evaluation claims have dataset/leakage support when relevant;
- important failures or inconclusive results are recorded;
- claim support is mapped in `result_to_claim_map.md`;
- `claim_ledger.md` reflects the current evidence;
- figures/tables are reviewed for traceability and claim safety;
- claim-critical results have an evidence review or an explicit reason why evidence review was deferred;
- unresolved evidence-review issues are recorded in `docs/agent/red_team_issue_ledger.md`;
- unsupported or overbroad claims are marked with canonical support statuses such as `preliminary`, `partially_supported`, `unsupported`, `contradicted`, `out_of_scope`, `needs_citation`, or `needs_manual_check`, with decisions such as `remove`, `rewrite`, or `weaken_claim` recorded separately.