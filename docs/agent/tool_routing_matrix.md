# Tool Routing Matrix

## Purpose

This file maps workflow situations to tools, required inputs, and required durable outputs.

Use it when deciding whether a tool should be invoked and what artifact must be updated afterward.

## Routing Rule

Do not invoke tools as isolated helpers.

Every meaningful tool use should have:

1. a workflow phase;
2. an upstream context artifact;
3. a purpose;
4. a durable output artifact;
5. a next workflow decision.

## Matrix

| Situation                                                                | Preferred Tool / Skill / MCP                                   | Required Inputs                                                                                                        | Required Durable Output                                                                                                                 |
| ------------------------------------------------------------------------ | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Discover prior work, datasets, benchmarks, baselines, or source material | `research-lookup` or external search/retrieval tool            | `docs/agent/research_direction.md`, `sources/reading_queue.md` when available                                          | `sources/reading_queue.md`, `sources/paper_cards/`, `sources/literature_matrix.md`                                                      |
| Synthesize selected papers or source artifacts                           | `literature-review`                                            | `sources/paper_cards/`, `sources/literature_matrix.md`                                                                 | `sources/literature_matrix.md`, `docs/agent/research_direction.md`, `sources/citation_intent_map.md`                                    |
| Audit claim support                                                      | `claim-auditor`                                                | `docs/agent/claim_ledger.md`, `docs/agent/result_to_claim_map.md`, `paper/agent/claim_audit.md` when relevant          | `docs/agent/claim_ledger.md`, `paper/agent/claim_audit.md`                                                                              |
| Pressure-test assumptions or methodology                                 | `scientific-critical-thinking`                                 | Current phase artifacts, red-team artifacts when available                                                             | `docs/agent/pre_mortem.md`, `docs/agent/experiment_red_team.md`, `docs/agent/evidence_review.md`, `docs/agent/red_team_issue_ledger.md` |
| Implement code or debug project behavior                                 | Code execution / development tools                             | `docs/PROJECT_PLAN.md`, `docs/agent/implementation_notes.md`, relevant code/tests                                      | `src/`, `scripts/`, `tests/`, `docs/agent/implementation_notes.md`                                                                      |
| Run experiments or generate metrics                                      | Code execution / experiment tools                              | `docs/agent/experiment_plan.md`, `docs/agent/run_registry.md`, configs/data                                            | `runs/`, `outputs/`, `docs/agent/run_registry.md`, `docs/agent/experiment_journal.md`                                                   |
| Analyze results                                                          | Analysis tools / notebooks / scripts                           | `docs/agent/run_registry.md`, `runs/`, `outputs/`, `docs/agent/experiment_plan.md`                                     | `docs/agent/result_cards/`, `docs/agent/result_interpretation.md`, `docs/agent/error_analysis.md`, `docs/agent/negative_results.md`     |
| Draft manuscript text                                                    | `scientific-writing`                                           | `docs/agent/claim_ledger.md`, `docs/agent/result_to_claim_map.md`, `sources/citation_intent_map.md`, `paper/AGENTS.md` | `paper/`, `paper/agent/claim_support.md`                                                                                                |
| Clean citations or bibliography                                          | `citation-management`                                          | `sources/citation_intent_map.md`, paper source files, bibliography files                                               | updated bibliography, `sources/citation_intent_map.md`, `paper/agent/claim_support.md`                                                  |
| Simulate reviewer critique                                               | `peer-review`, `scientific-critical-thinking`, `claim-auditor` | manuscript draft, `paper/agent/review_context.md`, `docs/agent/red_team_issue_ledger.md`                               | `paper/agent/review_*.md`, `paper/agent/revision_plan.md`, `paper/agent/claim_audit.md`                                                 |
| Validate workflow skeleton or status consistency                         | `workflow-manager`                                             | `docs/current_status.md`, workflow templates, phase artifacts                                                          | validation result, `docs/current_status.md` update if needed                                                                            |

## Escalation Rule

If a tool output creates a blocker, unresolved contradiction, missing evidence, or phase mismatch:

* update the relevant artifact;
* update `docs/current_status.md`;
* route to the earliest phase needed to resolve the issue.

## No-Orphan Tool Output Rule

Do not leave important tool output only in:

* chat;
* terminal output;
* notebook display;
* temporary files;
* local scratch notes;
* unsaved external tabs.

Save the useful result into the correct durable artifact.
