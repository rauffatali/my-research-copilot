# Canonical Example Workflow

This is a generic end-to-end example of how the skeleton is meant to be used.
It is intentionally non-project-specific.

## Example Request

Compare a baseline approach against one proposed change under a shared evaluation protocol.

## Task Intake Examples

Use the earliest required phase when a prompt spans multiple phases.
Use `blocked` when the request depends on a missing upstream artifact, decision, or external dependency.

### Phase 1: Research Formalization

- "I have a rough research idea. Help me shape it into a concrete direction."
- "Is this idea strong enough to pursue, or is it too weak?"
- "What is the closest prior work to this concept?"
- "Help me define the baseline, metric, and failure mode."
- "What is missing before this proposal becomes implementable?"
- "Pressure-test the novelty of this idea."
- "Turn this loose concept into a research question."
- "Compare these two possible directions and tell me which is better."
- "What risks or tradeoffs could make this idea fail?"
- "Create a research direction note from this prompt."

### Phase 2: Implementation / Experimentation

- "Implement the approved plan."
- "Add the data pipeline described in the project plan."
- "Create the experiment config for the next run."
- "Build the training script from the frozen direction."
- "Add tests for the new preprocessing step."
- "Refactor the evaluation code without changing the metric."
- "Implement the ablation described in the plan."
- "Fix this bug in the experiment workflow."
- "Package the notebook workflow into a reusable script."
- "Update the code to match the approved hypothesis."

### Phase 3: Result Consolidation

- "Analyze the latest run outputs."
- "Create a result interpretation note from these metrics."
- "Does this result support the hypothesis or not?"
- "Build an ablation summary from the saved runs."
- "Label each claim as supported, preliminary, or unsupported."
- "Summarize the failure cases from these outputs."
- "Compare this run with the baseline."
- "Prepare a claim ledger from the current evidence."
- "Do we have enough evidence to start writing?"
- "Turn the logs into a structured evidence package."

### Phase 4: Writing / Manuscript Drafting

- "Draft the introduction from the approved direction."
- "Write the method section from the implementation notes."
- "Turn this result summary into a paper subsection."
- "Polish the related work using the saved sources."
- "Rewrite this paragraph so it is more precise."
- "Add citations to this manuscript section."
- "Adapt this text to the prior-paper style."
- "Write a limitations paragraph from the evidence."
- "Prepare the caption for this table."
- "Rewrite the abstract using only supported claims."

### Phase 5: Multi-Agent Review / Red-Team

- "Review this manuscript like a skeptical reviewer."
- "What are the biggest weaknesses in this draft?"
- "Check whether the claims are too strong."
- "Run a multi-reviewer critique of the paper."
- "What would cause rejection here?"
- "Create a revision plan from these comments."
- "Audit the novelty claim."
- "Pressure-test the evaluation section."
- "Summarize the likely reviewer decision."
- "Draft a response-to-reviewers outline."

### Blocked

- "Continue, but the approved plan is missing."
- "Write the results section, but no result artifacts exist yet."
- "Move to Phase 2, but Phase 1 is not frozen."
- "Update the paper claims, but the evidence package is incomplete."
- "Run the next experiment, but the dataset path is missing."
- "Finalize the review response, but the manuscript draft is not ready."
- "Proceed, but a required artifact is missing."
- "I want the next step, but the upstream phase is not done."

### No-op / Explanation Only

- "Explain what Phase 3 means."
- "What belongs in `docs/agent/`?"
- "What is the difference between `sources/` and `paper/agent/`?"
- "Show me the state machine."
- "Should this be Phase 1 or Phase 2?"
- "What does `blocked` mean here?"
- "Explain how the workflow skeleton is supposed to work."
- "What is the role of `docs/current_status.md`?"

### Cross-phase

- "Implement this idea and draft the paper section."
- "Analyze the results and rewrite the abstract."
- "Review the manuscript and fix the experiments."
- "Find related work and write the introduction."
- "Run the ablation and update the results table."
- "Change the dataset split and update the claims."
- "Improve the method."
- "Make the paper stronger."
- "Turn this idea into a publishable workflow."
- "Do the next step end to end."

## Phase 1: Research Formalization

### Goal
Turn the request into a reviewable direction.

### Example artifacts

- `docs/agent/brainstorming_brief.md`
- `docs/agent/idea_archive.md`
- `docs/agent/research_direction.md`
- `docs/agent/hypotheses.md`
- `docs/agent/novelty_risk_matrix.md`

### Example content

- Research question: does the proposed change improve the target failure mode relative to the baseline?
- Idea archive: candidate directions are scored and kept so rejected or deferred ideas are not lost.
- Baseline: the simplest accepted reference method.
- Failure mode: the weakness the proposal is meant to address.
- Metric: the decision signal that will determine whether the idea is worth implementing.
- Decision: `frozen` once the question, baseline, failure mode, and validation path are explicit.

## Phase 2: Implementation / Experimentation

### Goal
Implement the approved plan and validate it narrowly.

### Example artifacts

- `docs/agent/project_plan.md`
- `docs/agent/experiment_journal.md`
- `docs/agent/implementation_notes.md`
- `scripts/`
- `tests/`
- `runs/`
- `outputs/`

### Example content

- Planned steps: implement the smallest change, run a smoke test, and save outputs.
- Experiment journal: record preliminary investigation, tuning, execution, ablation, and blockers.
- Validation: unit test or smoke test plus any narrow experiment check required by the plan.
- Decision: `frozen` once the approved change is implemented and validated or explicitly deferred.

## Phase 3: Result Consolidation

### Goal
Convert raw outputs into evidence and claim labels.

### Example artifacts

- `docs/agent/result_interpretation.md`
- `docs/agent/figure_review.md`
- `docs/agent/claim_ledger.md`
- `outputs/`

### Example content

- Evaluation context: split, metric, and protocol.
- Main findings: what changed relative to the baseline.
- Figure review: plots are aggregated, checked for caption alignment, and fixed when misleading or unclear.
- Supported claims: only the claims directly backed by the outputs.
- Weak claims: anything needing more evidence or a narrower wording.
- Decision: `frozen` once the evidence package is stable enough for writing.

## Phase 4: Writing / Manuscript Drafting

### Goal
Turn evidence into manuscript text.

### Example artifacts

- `paper/agent/claim_support.md`
- `paper/agent/section_notes.md`
- `paper/agent/citation_support.md`
- `paper/agent/figure_support.md`
- `paper/agent/style_notes.md`

### Example content

- Section notes: purpose, evidence used, and draft notes for the section being written.
- Claim support: each important claim with a support status and rewrite decision.
- Citation support: each citation with the claim it supports and the reason it is included.
- Figure support: each scientific figure has source context, communicative intent, references, specification, style plan, and critique notes.
- Style notes: the prose traits being applied from the prior-paper style template.
- Decision: `frozen` when the section is traceable to evidence and citations.

## Phase 5: Multi-Agent Review / Red-Team

### Goal
Stress-test the draft after assembling a compact review context bundle.

### Example artifacts

- `paper/agent/review_context.md`
- `paper/agent/review_method.md`
- `paper/agent/review_domain.md`
- `paper/agent/review_hybrid.md`
- `paper/agent/review_meta.md`
- `paper/agent/revision_plan.md`
- `paper/agent/response_to_reviewers_draft.md`
- `paper/agent/review_score_ledger.md`
- `paper/agent/responsible_use_disclosure.md`
- `paper/agent/review_notes.md`

### Example content

- Review context: compresses the manuscript summary, claim map, closest baseline context, a question engine, and the reviewer questions that should guide critique.
- Method reviewer: checks protocol, controls, and validation logic.
- Domain reviewer: checks novelty and positioning.
- Hybrid reviewer: checks whether the evidence actually supports the claims.
- Meta-reviewer: summarizes must-fix issues and the likely decision.
- Review score ledger: keeps soundness, presentation, contribution, overall score, and confidence comparable across roles.
- Responsible-use disclosure: records approval, disclosure, and withdrawal conditions before the review cycle is finalized.
- Decision: revise, hold, or archive depending on the review outcome.

## Canonical Flow

`intake -> Phase 1 -> frozen Phase 1 -> Phase 2 -> frozen Phase 2 -> Phase 3 -> frozen Phase 3 -> Phase 4 -> frozen Phase 4 -> Phase 5 -> archived`

## What This Example Shows

- The workflow is linear by default.
- Each phase produces a distinct artifact set.
- Frozen artifacts should not be silently rewritten downstream.
- Review can move the workflow backward when evidence or direction is weak.
- The intake examples above show how to route mixed or ambiguous prompts.
