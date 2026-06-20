# Agent Artifacts

This directory stores agent-generated research workflow artifacts.

Examples include:

- brainstorming briefs
- evidence-backed debate rounds
- user clarification and decision records
- idea archive entries
- research direction notes
- hypotheses
- novelty-risk notes
- experiment journals
- implementation notes
- result interpretation notes
- figure review notes
- claim ledgers
- canonical end-to-end workflow example

These are workflow and reasoning artifacts, not manuscript files.

Phase 1 brainstorming artifacts should preserve the discussion path, not only the final idea. Keep evidence found, questions asked, user responses, unresolved assumptions, and the final proceed/revise/defer/stop decision traceable.

## Common templates

### Phase 1: Research formalization

- `research_direction.md`
- `brainstorming_brief.md`
- `idea_archive.md`
- `hypotheses.md`
- `novelty_risk_matrix.md`

### Phase 2: Implementation and experimentation

- `project_plan.md`
- `implementation_notes.md`
- `experiment_queue.md`
- `experiment_plan.md`
- `experiment_journal.md`
- `run_registry.md`
- `baseline_ledger.md`
- `ablation_matrix.md`
- `dataset_card.md`
- `leakage_audit.md`

### Phase 3: Result consolidation

- `result_cards/` — one structured interpretation per major result, run group, table, or decision-relevant finding
- `result_interpretation.md` — synthesis across result cards
- `error_analysis.md` — systematic failure modes and slice-level weaknesses
- `negative_results.md` — failed, inconclusive, or abandoned experiments
- `result_to_claim_map.md` — bridge from interpreted results to paper-safe claims
- `figure_review.md` — figure/table accuracy and claim-safety audit
- `claim_ledger.md` — final claim status registry

Use these as the durable handoff files for Phases 1 to 3.

## Source and Literature Artifacts

External literature artifacts live under `sources/`.

Use:

- `sources/reading_queue.md` for source triage;
- `sources/paper_cards/` for individual paper reading;
- `sources/literature_matrix.md` for cross-paper comparison;
- `sources/baseline_candidates.md` for literature-suggested baselines;
- `sources/citation_intent_map.md` for citation role tracking.

Relationship to workflow artifacts:

- Phase 1 uses paper cards and literature matrix entries for research direction and novelty.
- Phase 2 uses baseline candidates and paper cards for experiment design.
- Phase 3 uses paper cards and citation intent when external evidence affects claim support.
- Phase 4 uses citation intent and paper cards for literature-dependent writing.
- Phase 5 uses literature matrix and closest-prior-work notes for reviewer-risk analysis.

## Phase 3 evidence chain

Use this chain after experiments:

`run_registry.md` -> `result_cards/` -> `result_interpretation.md` -> `result_to_claim_map.md` -> `claim_ledger.md`

Supporting artifacts:

- `error_analysis.md` for failure modes;
- `negative_results.md` for failed or inconclusive experiments;
- `figure_review.md` for table/figure safety.

Do not convert raw metrics directly into manuscript claims.

## Experiment artifact chain

For serious experiments, use this chain:

`hypotheses.md` -> `experiment_queue.md` -> `experiment_plan.md` -> `run_registry.md` -> `experiment_journal.md` -> `result_interpretation.md` -> `claim_ledger.md`

Use `experiment_queue.md` when there are multiple possible experiments, uncertain priority, limited compute, or a need to choose the next decision-changing run.

Use `experiment_plan.md` only after a queue item has been promoted into a concrete runnable experiment.

Supporting artifacts:

- `baseline_ledger.md` for comparison validity;
- `ablation_matrix.md` for mechanism/component isolation;
- `dataset_card.md` for dataset and split assumptions;
- `leakage_audit.md` for evaluation trustworthiness.

Do not treat a queued experiment as approved, run, or evidence-bearing.
