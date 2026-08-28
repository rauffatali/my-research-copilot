# Workflow memory layout

This repository uses file-backed workflow memory. Chat is for interaction, but durable research context must be written to repository artifacts.

- `docs/current_status.md` is the short shared live state pointer across all phases. It should record the current phase, current substep, latest action, active artifact paths, blockers, open questions, and next recommended step.
- `docs/current_status_protocol.md` defines how `docs/current_status.md` should be updated, when it is stale, and how to handle template-default or backfilled state.
- `.agents/workflow/policies/tool_workflow_policy.md` defines how tool, skill, MCP, lookup, retrieval, and code-execution outputs become durable workflow state.
- `docs/agent/` stores agent-generated research workflow artifacts such as brainstorming briefs, research direction notes, hypotheses, novelty-risk notes, planning notes, and result-interpretation notes.
- `paper/agent/` stores agent-generated manuscript-support artifacts such as claim audits, review rounds, revision plans, and response-to-reviewers drafts.
- `sources/` stores external evidence artifacts gathered from search, APIs, papers, dataset pages, benchmark pages, and technical documentation. These are source-trace artifacts, not manuscript prose.
- `sources/reading_queue.md` tracks papers and external sources selected for triage or reading.
- `sources/paper_cards/` stores structured reading notes for individual papers and source artifacts.
- `sources/literature_matrix.md` compares selected papers across task, method, dataset, metric, baseline, limitation, and project relevance.
- `sources/baseline_candidates.md` tracks literature-suggested baselines before promotion into `docs/agent/baseline_ledger.md`.
- `sources/citation_intent_map.md` maps citation candidates to the claims or manuscript sections they may support.

Use these directories with clear separation:

- `sources/` = external evidence gathered from outside the repository.
- `docs/agent/` = project reasoning, decisions, and phase outputs.
- `paper/agent/` = manuscript-support and review artifacts.
- `paper/` main files = human-facing manuscript sources.

## External source saving rule

When an agent performs external source discovery, lookup, benchmark search, dataset search, or citation candidate gathering, it must save the result under `sources/` instead of leaving it only in chat history.

Before performing a new external lookup, check whether a relevant saved artifact already exists in `sources/` and reuse it when it is still adequate for the task.

When a new `sources/` artifact is created or an existing one becomes the current source base for a task, record its path in `docs/current_status.md`.

Do not treat chat-only search output as durable project evidence.

## Source Reading Discipline

Lookup results are not the same as read papers.

Use `research-lookup` for discovery.
Use `sources/reading_queue.md` to triage what should be read.
Use `sources/paper_cards/` for deep reading.
Use `sources/literature_matrix.md` for cross-paper comparison.
Use `literature-review` for synthesis after relevant papers have been selected or read.

Do not treat a paper as deeply understood only because it appears in a lookup result.

Do not use a paper as closest prior work, baseline evidence, dataset evidence, evaluation-protocol evidence, claim support, or manuscript citation support unless it has a paper card or equivalent durable source artifact.

Do not treat lookup results as deeply read evidence. For novelty, baseline, dataset, evaluation, claim, or citation decisions, promote important sources through `sources/reading_queue.md`, `sources/paper_cards/`, and `sources/literature_matrix.md` before relying on them.

## Claim Status Discipline

Use one shared support-status vocabulary across claim-related artifacts.

Allowed support statuses:

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

Do not invent local claim-status labels.

Use decision labels separately from support-status labels.

Examples:

- `supported` is a support status.
- `remove` is a decision.
- `weaken_claim` is a decision.
- `run_ablation` is a decision.
- `needs_more_evidence` is a decision or next action, not a support status.

`docs/agent/claim_ledger.md` is the source of truth for final claim support status.

Use the shared claim support-status vocabulary in all claim-related artifacts. Keep support status separate from decisions and next actions.

## Early Red-Team Discipline

Do not reserve red-team critique only for Phase 5 manuscript review.

Use early red-team artifacts when critique is needed before accepting a direction, experiment, result interpretation, or claim.

Use:

- `docs/agent/pre_mortem.md` before freezing high-impact or uncertain research directions.
- `docs/agent/experiment_red_team.md` before expensive, claim-critical, or direction-changing experiments.
- `docs/agent/evidence_review.md` before turning interpreted results into manuscript claims.
- `docs/agent/red_team_issue_ledger.md` when critique creates concrete issues that must be tracked across phases.

Use `paper/agent/` review artifacts for manuscript-stage review.

Keep early critique decision-oriented: every issue should lead to a fix, caveat, experiment, claim update, accepted risk, or phase rollback.

Use early red-team artifacts before freezing directions, running expensive experiments, or turning evidence into strong claims.

## Tool Workflow Discipline

Use `.agents/workflow/policies/tool_workflow_policy.md` as the canonical policy for tool, skill, MCP, retrieval, lookup, code-execution, and automated-helper use.

Do not treat tool output as durable project memory until it is written to the appropriate repository artifact.

Before using a meaningful tool, identify:

- the current workflow phase;
- the upstream artifacts that must be read first;
- the output class the tool is expected to produce;
- the durable artifact that must be updated afterward.

After using a meaningful tool, update the relevant artifact and, when the tool changes project state, update `docs/current_status.md`.

Use `docs/agent/tool_routing_matrix.md` to choose tools for workflow situations.

Use `docs/agent/tool_use_log.md` to record meaningful tool-assisted actions that affect direction, implementation, experiments, evidence, claims, manuscript text, or review decisions.

Do not log trivial helper calls that have no project consequence.

Do not promote chat-only lookup, execution output, retrieval output, or model-generated analysis into claims, experiments, or manuscript prose until the appropriate durable artifact exists.
