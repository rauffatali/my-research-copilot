# Tool Workflow Policy

## Purpose

This file defines how tools, MCP servers, skills, external lookups, code execution, retrieval systems, and agent helpers should be used inside the research workflow.

Tools may assist the workflow, but they do not replace workflow state.

A tool output is not durable research memory until it is written to the appropriate repository artifact.

## Core Rule

Do not treat chat-only tool output as project truth.

Every tool use that affects research direction, implementation, experiments, evidence, claims, citations, manuscript text, or review decisions must be reflected in a durable repository artifact.

## Tool Output Classes

Classify tool outputs before using them.

| Class              | Description                                                                       | Durable destination                                                                                                                                                |
| ------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `source_discovery` | Papers, websites, datasets, benchmarks, API docs, prior work, citation candidates | `sources/`                                                                                                                                                         |
| `source_reading`   | Structured reading notes, paper summaries, source comparisons                     | `sources/paper_cards/`, `sources/literature_matrix.md`                                                                                                             |
| `planning`         | Research direction, project plan, experiment selection, implementation plan       | `docs/agent/`, `docs/PROJECT_PLAN.md`, `docs/research_context.md`                                                                                                                               |
| `implementation`   | Code changes, scripts, configs, tests, engineering decisions                      | `src/`, `scripts/`, `tests/`, `configs/`, `docs/agent/implementation_notes.md`                                                                                     |
| `execution`        | Runs, logs, metrics, checkpoints, predictions, generated outputs                  | `runs/`, `outputs/`, `docs/agent/run_registry.md`                                                                                                                  |
| `analysis`         | Result interpretation, error analysis, negative results, figure/table review      | `docs/agent/result_cards/`, `docs/agent/result_interpretation.md`, `docs/agent/error_analysis.md`, `docs/agent/negative_results.md`, `docs/agent/figure_review.md` |
| `claim_support`    | Claim audits, result-to-claim mappings, support-status decisions                  | `docs/agent/result_to_claim_map.md`, `docs/agent/claim_ledger.md`, `paper/agent/claim_audit.md`                                                                    |
| `manuscript`       | Drafted prose, citation edits, review responses, revision plans                   | `paper/`, `paper/agent/`                                                                                                                                           |
| `review`           | Red-team critique, peer review, pre-mortem, evidence review                       | `docs/agent/pre_mortem.md`, `docs/agent/experiment_red_team.md`, `docs/agent/evidence_review.md`, `docs/agent/red_team_issue_ledger.md`, `paper/agent/`            |
| `status`           | Workflow routing, phase changes, blockers, next steps                             | `docs/current_status.md`                                                                                                                                           |

## Tool Use Protocol

Before using a tool:

1. Identify the current workflow phase from `docs/current_status.md`.
2. Check `docs/workflow_state_machine.md` for valid phase transitions.
3. Read the relevant upstream artifacts for the phase.
4. Decide what class of output the tool is expected to produce.
5. Identify the durable artifact that will receive the tool result.

After using a tool:

1. Summarize the result.
2. Save or update the appropriate durable artifact.
3. Record limitations, uncertainty, missing evidence, or failed tool output.
4. Update `docs/current_status.md` if the tool changed the active artifact, blocker, phase, claim status, experiment status, or next step.
5. Do not promote the tool output into claims, experiments, or manuscript prose until the required workflow artifact exists.

## Source and Lookup Tools

Use lookup tools for discovery, not final evidence.

Lookup output must go through the source workflow before supporting strong novelty, baseline, dataset, evaluation, citation, or claim decisions.

Preferred chain:

`lookup tool -> sources/reading_queue.md -> sources/paper_cards/ -> sources/literature_matrix.md -> downstream decision`

Do not cite, claim, or freeze a direction from lookup-only output unless the artifact explicitly records why deeper source processing was deferred.

## Code and Execution Tools

Use code/execution tools only with a clear workflow target.

Before code execution:

* identify the linked plan, experiment, test, or debugging task;
* check whether the task belongs to implementation, experiment execution, analysis, or validation;
* define what output should be saved.

After code execution:

* save durable outputs under `runs/`, `outputs/`, or the relevant code/test paths;
* update `docs/agent/run_registry.md` for experiment runs;
* update `docs/agent/experiment_journal.md` for experiment chronology;
* update `docs/agent/implementation_notes.md` for engineering decisions, debugging, or implementation-only work.

Do not treat console output as durable evidence.

## Claim and Writing Tools

Claim-auditing, writing, citation, and review tools must respect the canonical claim-status vocabulary.

A writing or review tool may suggest manuscript text, but it must not upgrade claim support status unless the evidence chain supports it.

Preferred chain:

`result_cards/ -> result_to_claim_map.md -> claim_ledger.md -> manuscript prose -> claim_audit.md`

## Review and Red-Team Tools

Red-team tools may be used before Phase 5.

Use early red-team artifacts for critique before accepting directions, experiments, evidence, or claims.

Preferred chain:

`pre_mortem.md -> experiment_red_team.md -> evidence_review.md -> red_team_issue_ledger.md -> paper/agent review artifacts`

Review output must create a decision:

* fix;
* narrow;
* caveat;
* run lookup;
* run experiment;
* update claim ledger;
* accept risk;
* defer;
* stop;
* route back to an earlier phase.

## Failure Handling

If a tool fails, returns incomplete output, produces conflicting evidence, or cannot access required data:

1. Record the failure in the relevant artifact.
2. Do not silently continue as if the tool succeeded.
3. Mark affected claims or decisions as `needs_manual_check`, `needs_citation`, `preliminary`, or blocked, as appropriate.
4. Update `docs/current_status.md` if the failure blocks progress.

## Tool Output Promotion Rule

Tool output can influence durable workflow state only after it is written to the appropriate artifact.

Tool output can influence manuscript claims only after it is connected to:

* source artifacts for literature/citation claims;
* experiment artifacts for empirical claims;
* result cards and result-to-claim mapping for result claims;
* claim ledger status for final support decisions.

## Minimal Checklist

Before ending a tool-assisted task, check:

* Was the relevant upstream artifact read?
* Was the tool output classified?
* Was the durable destination updated?
* Were uncertainty and failure modes recorded?
* Was `docs/current_status.md` updated if workflow state changed?
* Were claims kept separate from decisions and next actions?
