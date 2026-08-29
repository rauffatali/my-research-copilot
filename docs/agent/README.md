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

### Role profile

- `agent_role_profile.md` — project-local role assignments, candidate-writer count, candidate independence settings, and candidate-writer slots for actual agents, models, providers, or harnesses, with role-specific permission notes. It contains no scientific evidence or manuscript content.

## Configuration and State Source Separation

Keep these project sources distinct:

- `docs/project_profile.md` — operational project configuration
- `docs/agent/agent_role_profile.md` — role and writer configuration
- `docs/research_context.md` — scientific framing
- `docs/current_status.md` — live workflow state
- `docs/copilot_upstream.md` — upstream provenance

Among these configuration and state sources, only `agent_role_profile.md` belongs inside `docs/agent/`.
The other files remain in their canonical locations.

Phase 1 brainstorming artifacts should preserve the discussion path, not only the final idea. Keep evidence found, questions asked, user responses, unresolved assumptions, and the final proceed/revise/defer/stop decision traceable.

## Common templates

### Phase 1: Research formalization

- `research_direction.md`
- `brainstorming_brief.md`
- `idea_archive.md`
- `hypotheses.md`
- `novelty_risk_matrix.md`

Note: `docs/research_context.md` (in `docs/`, not `docs/agent/`) holds the stable, high-level project snapshot. Keep it distinct from `research_direction.md`, which holds the debated, approved decision record.

### Phase 2: Implementation and experimentation

- `../PROJECT_PLAN.md`
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

## Early Red-Team Artifacts

Use early red-team artifacts before review reaches the manuscript stage.

- `pre_mortem.md` — red-team the research direction before freezing Phase 1.
- `experiment_red_team.md` — red-team expensive or claim-critical experiments before running.
- `evidence_review.md` — red-team interpreted evidence before turning it into manuscript claims.
- `red_team_issue_ledger.md` — track red-team issues and decisions across phases.

Early red-team artifacts live in `docs/agent/`.

Manuscript-stage review artifacts live in `paper/agent/`.

Do not wait until Phase 5 to identify missing baselines, weak assumptions, leakage risk, unsupported claims, or likely reviewer objections.

## Early Red-Team Rule

Do not wait until Phase 5 to red-team the work.

Use early red-team artifacts before accepting high-impact directions, expensive experiments, claim-critical evidence, or strong manuscript claims.

Preferred chain:

`pre_mortem.md` -> `experiment_red_team.md` -> `evidence_review.md` -> `red_team_issue_ledger.md` -> manuscript-stage review in `paper/agent/`

Every red-team finding should lead to a decision: fix, caveat, test, narrow, accept risk, defer, or stop.

## Tool Workflow Artifacts

Use tool workflow artifacts to ensure tools, skills, MCP servers, lookup systems, retrieval systems, code execution, and automated helpers produce durable workflow state rather than chat-only output.

- `.agents/workflow/policies/tool_workflow_policy.md` — canonical policy for tool use and durable artifact promotion.
- `tool_routing_matrix.md` — maps workflow situations to preferred tools, required inputs, and required durable outputs.
- `tool_use_log.md` — records meaningful tool-assisted actions that affect research direction, implementation, experiments, evidence, claims, manuscript text, or review decisions.

Tool output is not project memory until it is written to the correct repository artifact.

Do not leave important source discovery, experiment execution, result analysis, claim audit, citation work, or review decisions only in chat, terminal output, notebooks, or temporary files.

## Claim Status Vocabulary

Claim-related artifacts use one shared support-status vocabulary:

- `supported`
- `partially_supported`
- `preliminary`
- `hypothesis`
- `needs_citation`
- `wrong_citation`
- `unsupported`
- `contradicted`
- `out_of_scope`
- `needs_manual_check`

Use this vocabulary in:

- `claim_ledger.md`
- `result_to_claim_map.md`
- `result_cards/`
- paper claim-support artifacts
- claim-auditor outputs

Do not introduce local variants.

Keep support status separate from decisions or next actions.

## Evidence State Vocabulary

Use exactly these dependency lifecycle/readiness states:

- `evidence_ready`
- `implementation_defined`
- `implementation_pending`
- `experiment_planned`
- `result_pending`
- `citation_pending`
- `placeholder_only`

`Evidence State(s)` describe the readiness or lifecycle of evidence dependencies. `Support Status`
remains the support verdict for the exact claim wording; the two vocabularies are separate. See
`.agents/workflow/policies/evidence_and_claim_policy.md` for the canonical definitions.

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
