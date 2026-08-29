# Canonical Example Workflow

This is a project-neutral Research Copilot v2 example. It demonstrates phase routing, separation of
roles and permissions, evidence-state discipline, candidate-writer configuration, draft-first
manuscript writing, human integration authority, and formal broader review.

This is an explanatory example, not a second policy source. Where this example and the canonical
policies differ, the canonical policies win.

## Example Request

Compare a baseline approach with one proposed change under a shared evaluation protocol, then prepare an
evidence-bound manuscript writing slice from the consolidated result.

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

Phase 4 examples are bounded writing-slice requests. They do not imply direct mutation of a protected
main manuscript.

- "Draft the claim-bearing paragraph that explains this result."
- "Prepare the method sentence that describes this verified implementation detail."
- "Draft a limitations paragraph from the current evidence package."
- "Revise this writing slice without strengthening the claims."
- "Prepare a table narrative from `evidence_ready` results."
- "Draft this slice in the provisional manuscript workspace."
- "Polish this evidence-bound writing slice after the scientific brief is resolved."

### Phase 5: Formal Broader Review / Red-Team

Phase 5 examples target a broader integrated manuscript or coherent manuscript unit, not every
paragraph or slice.

- "Perform formal review of this integrated manuscript."
- "Review this coherent results section as a skeptical reviewer."
- "Create a revision plan from the broader manuscript review."
- "Audit whether the integrated claims match the evidence package."
- "Prepare a response-to-reviewers outline from the completed review."

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

- "Implement this idea and draft a writing slice."
- "Analyze the results and revise the abstract."
- "Review the manuscript and identify whether the defect is prose, evidence, or direction."
- "Find related work and prepare an introduction slice."
- "Run the ablation and update the result support artifacts."
- "Change the dataset split and update the claims."
- "Improve the method."
- "Make the paper stronger."
- "Turn this idea into a publishable workflow."
- "Do the next step end to end."

## Phase 1: Research Formalization

### Goal
Turn the request into a debated, evidence-backed, user-approved direction.

### Example artifacts

- `docs/agent/brainstorming_brief.md`
- `docs/agent/idea_archive.md`
- `docs/agent/research_direction.md`
- `docs/agent/hypotheses.md`
- `docs/agent/novelty_risk_matrix.md`

### Example content

- Evidence briefing: the agent shows relevant papers, baselines, datasets, benchmarks, or saved source artifacts before finalizing the direction.
- Debate rounds: the agent challenges the idea, asks clarifying questions, records user responses, and updates the interpretation.
- Research question: does the proposed change improve the target failure mode relative to the baseline?
- Idea archive: candidate directions are scored and kept so rejected or deferred ideas are not lost.
- Baseline: the simplest accepted reference method.
- Failure mode: the weakness the proposal is meant to address.
- Expected mechanism: why the proposed idea should address the failure mode.
- Metric: the decision signal that will determine whether the idea is worth implementing.
- Ablation or isolation plan: the minimum comparison needed to isolate the contribution.
- Publication worthiness: why the direction is worth pursuing, revising, deferring, or stopping.
- User approval: the explicit proceed, revise, defer, or stop decision.
- Decision: `frozen` only after evidence has been shown, main questions have been answered or deferred, and the user approves the final direction.

## Phase 2: Implementation / Experimentation

### Goal
Implement the approved plan through an explicit task breakdown and validate it narrowly.

### Example artifacts

- `docs/agent/experiment_queue.md`
- `docs/agent/experiment_plan.md`
- `docs/agent/run_registry.md`
- `docs/agent/experiment_journal.md`
- `docs/agent/implementation_notes.md`
- `docs/PROJECT_PLAN.md`
- `scripts/`
- `tests/`
- `runs/`
- `outputs/`

### Example content

- Objective: one sentence stating the implementation goal.
- Scope and assumptions: what is included, excluded, and what must already be true.
- Workstreams: the major execution blocks for the project.
- Task breakdown: numbered tasks with subtasks, validation, and artifact paths for each task.
- Dependencies and order: upstream artifacts, file dependencies, and sequencing constraints.
- Validation plan: unit tests, smoke tests, or experiment checks mapped to the relevant task.
- Risks / blockers: implementation risks, missing inputs, and known uncertainties.
- Exit criteria: what must be true before Phase 2 can freeze.
- Decision: `frozen` once the approved change is implemented, validated, and documented at the task level or explicitly deferred.
- Experiment queue: candidate experiments are prioritized by decision enabled, expected information gain, cost, risk, and status.
- Experiment promotion: only the selected queue item becomes an approved experiment plan.
- Experiment journal: records what actually happened after planning and execution.

## Phase 3: Result Consolidation

### Goal
Convert raw outputs into interpreted evidence and claim-support decisions.

### Example artifacts

- `docs/agent/result_cards/`
- `docs/agent/result_interpretation.md`
- `docs/agent/figure_review.md`
- `docs/agent/result_to_claim_map.md`
- `docs/agent/claim_ledger.md`
- `outputs/`

### Evidence-state example

The relevant result dependency follows the evidence lifecycle only after the required interpretation and
review work:

```text
experiment_planned
        →
result_pending
        →
evidence_ready
```

An output or completed run can remain `result_pending` while interpretation, verification, scope and
limitations, result-to-claim mapping, or evidence review is incomplete. A completed run is not
automatically `evidence_ready`.

```text
run completed != evidence_ready
evidence_ready != supported
```

`support_status` is evaluated separately for each exact claim. `evidence_ready` means that the evidence
dependency is ready for claim evaluation; it does not mean that the claim is `supported`. The claim may
instead be `preliminary`, `partially_supported`, `unsupported`, or another canonical support status.

### Example content

- Evaluation context: split, metric, and protocol.
- Main findings: what changed relative to the baseline.
- Figure review: plots are aggregated, checked for caption alignment, and fixed when misleading or unclear.
- Claim support: only claims whose exact wording is backed by the interpreted evidence and verification.
- Weak claims: anything needing more evidence or a narrower wording.
- Decision: `frozen` once the evidence package and claim labels are stable enough for writing.

## Phase 4: Writing / Manuscript Drafting

### Goal
Turn resolved scientific and evidence context into provisional, evidence-bound writing slices, review
them locally, and prepare accepted slices for separately authorized integration.

### Example artifacts

- `paper/draft/`
- `paper/agent/claim_support.md`
- `paper/agent/claim_audit.md`
- `paper/agent/section_notes.md`
- `paper/agent/citation_support.md`
- `paper/agent/figure_support.md`
- `paper/agent/style_notes.md`

### Writing-slice boundary

A writing slice may be:

- part of a sentence;
- one sentence;
- one paragraph;
- a caption;
- a table narrative;
- a subsection; or
- a larger coherent unit when the scientific risk and surrounding context require it.

The workflow does not assume that a whole section is the atomic unit. The human selects or authorizes
the boundary, and the support package must keep the slice's evidence, claims, citations, review state,
and acceptance state understandable.

### Candidate-writer configuration

Before substantive semantic candidate production, resolve the project-local configuration in
`docs/agent/agent_role_profile.md`:

```text
candidate_writers_required = N
candidate_independence_required = true or false
candidate_cross_visibility_before_comparison = true or false
```

The example uses symbolic `N`; the reusable kernel does not universally require two candidates. A project
template may default to 2, but that default is not a canonical fixed count. Do not invent agent, model,
provider, or harness assignments.

The configured flow is:

```text
N configured candidate outputs
        →
research_lead comparison and adjudication
        →
one final prose owner for the writing slice
```

When `candidate_independence_required = true`, initial candidates use separate invocations and do not
co-author or coordinate toward one initial answer. When `candidate_cross_visibility_before_comparison =
false`, they do not inspect one another's provisional drafts before the first lead comparison.

### Provisional staging and local review

Semantic or scientific-risk writing is staged as:

```text
semantic/scientific-risk writing
        →
paper/draft/
```

The protected main manuscript is not ordinary scratch space. Candidates and resolved prose remain
provisional until accepted. A slice may be scientifically accepted or frozen while still remaining
provisional and not integrated.

```text
scientific readiness
        !=
human authorization
        !=
integration execution
```

### Optional style and text-hygiene paths

After scientific resolution, the optional prose-refinement sequence is:

```text
resolved scientific candidate
        → project or prior style when needed
        → academic-humanizer when useful
        → differential claim/evidence audit
        → citation validation when relevant
```

`academic-humanizer` is optional. `watermark-hygiene` remains outside this automatic prose chain as an
optional inspection-first Unicode or text-transfer hygiene workflow; it is not a detector-evasion,
provenance-stripping, or general humanization tool.

### Protected integration

The separate integration path is:

```text
research_lead
        → scientific readiness
human_researcher
        → explicit protected-integration authorization
integration_agent
        → bounded integration action
```

Immediately before integration, revalidate mutable evidence-state dependencies and applicable
`support_status` and citation relationships, resolve `docs/project_profile.md` → `main_manuscript_path`,
and confirm a focused diff or rollback mechanism. A configured path is not write authority. If the target
is `UNASSIGNED`, missing, invalid, or otherwise unresolved, drafting in `paper/draft/` may continue but
integration stops; do not guess a manuscript filename.

### Example content

- Writing-slice notes: purpose, evidence used, context, and draft notes for the bounded slice.
- Claim support: each important claim with a support status and rewrite decision.
- Citation support: each citation with the claim it supports and the reason it is included.
- Figure support: each scientific figure has source context, communicative intent, references, specification, style plan, and critique notes.
- Style notes: the prose traits being applied from the prior-paper style template.
- Decision: a slice is `frozen` when its draft and support decisions are stable and reviewable; this does
  not authorize or execute integration.

## Phase 5: Formal Broader Review / Red-Team

### Goal
Stress-test an integrated manuscript or coherent manuscript unit after a broader review target is ready.
Formal Phase 5 review is not the ordinary review loop for every paragraph or writing slice.

`independent_reviewer` is a permission role and remains strictly read-only. It returns findings in its
response. A writable, authorized role may later record accepted or adjudicated review findings in the
appropriate artifact.

`Method`, `Domain`, `Hybrid`, and `Meta` are optional review lenses or modes. They are not agent roles
and cannot grant write authority. A review lens must not be confused with the `independent_reviewer`
permission role.

### Example artifacts

- `paper/agent/review_context.md`
- `paper/agent/review_method.md`
- `paper/agent/review_domain.md`
- `paper/agent/review_hybrid.md`
- `paper/agent/review_meta.md`
- `paper/agent/revision_plan.md`
- `paper/agent/claim_audit.md`
- `paper/agent/review_notes.md`

### Review routing

Material findings route to the phase that owns the defect:

```text
prose problem
        → Phase 4
evidence problem
        → Phase 3
research-direction problem
        → Phase 1
```

Phase 5 does not repeat the candidate-writing production loop and does not silently revise manuscript
prose during review.

### Example content

- Review context: compresses the manuscript summary, claim map, closest baseline context, a question engine, and the reviewer questions that should guide critique.
- Method, Domain, Hybrid, and Meta lenses challenge protocol, positioning, evidence/claim support, and overall decision risk as applicable.
- Material findings record the affected section or claim, evidence reference or missing-evidence record, severity, required action, and closure state.
- Decision: revise, hold, or archive depending on the review outcome.

## Canonical Flow

The flow depends on whether the repository is new or already contains research artifacts:

```text
new project
        → intake
        → Phase 1
        → Phase 2
        → Phase 3
        → Phase 4 writing slices
        → Phase 5 when a broader review target is ready

existing project
        → intake
        → bootstrap_existing_project
        → latest valid active phase

missing handoff
        → backfill_required
        → minimum required context
        → selected active phase
```

The new-project path is normally sequential, but an existing project may bootstrap to its latest valid
phase. Backfill reconstructs only the minimum missing context and must not pretend that reconstructed
context was originally approved. A frozen Phase 4 slice does not automatically enter Phase 5; formal
review begins only when the broader manuscript or coherent-unit target and its prerequisites are ready.

## What This Example Shows

- Phase and role are orthogonal: roles define permissions and responsibilities, while phases define
  workflow location.
- Evidence lifecycle and exact-claim support are separate axes.
- Candidate count and independence are project-configured rather than universal kernel law.
- Semantic writing is draft-first and reviewable before protected integration.
- Scientific readiness, human authorization, and integration execution are separate decisions.
- Formal broader review is distinct from embedded Phase 4 slice-local review and can route work backward.
