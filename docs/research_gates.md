# Research Gates

This document defines mandatory checkpoints for high-impact research workflow decisions.

Use these gates before major research direction, implementation, experiment, evaluation, or paper-claim changes.

The goal is not to slow down progress. The goal is to prevent shallow ideas, unnecessary implementation, weak experiments, leakage, unsupported claims, and paper text that is stronger than the evidence.

Use the smallest relevant gate. Do not apply every gate by default.

Gates are grouped by research decision type, not one-to-one with workflow phases.

Core gates:

- Gate 1: Research Direction Gate
- Gate 2: Paper Reading Gate
- Gate 3: Research Change Gate
- Gate 4: Implementation Gate
- Gate 5: Dataset and Leakage Gate
- Gate 6: Experiment Decision Gate
- Gate 7: Evaluation and Result Interpretation Gate
- Gate 8: Result-to-Claim Gate
- Gate 9: Claim Support Gate
- Gate 10: Red-Team Review Gate
- Gate 11: Paper Writing Gate
- Gate 12: Final Handoff Gate

The canonical transition rules for moving between phases live in `docs/workflow_state_machine.md`.

---

## When to use this document

Apply a gate when the task involves one or more of the following:

- changing the research question or contribution target;
- proposing a new method, model, loss, augmentation, training strategy, or evaluation protocol;
- changing dataset assumptions, split logic, preprocessing, labels, or metrics;
- running an expensive or time-consuming experiment;
- interpreting results;
- editing paper claims;
- preparing figures, tables, or result summaries;
- making novelty, robustness, superiority, or generalization claims.

For small code cleanup, formatting, typo fixes, or local refactors with no research meaning, this document may be skipped.

---

## Gate 1: Research Direction Gate

Use this before proposing or accepting a new research direction, hypothesis, method idea, or contribution target.

A research direction must state:

1. Current project scope.
2. Target limitation, gap, or failure mode.
3. Baseline, reference point, or prior work comparison.
4. Proposed change or hypothesis.
5. Expected mechanism of improvement.
6. Minimal evidence needed before implementation.
7. Success metric or evaluation signal.
8. Risk, tradeoff, or reason the idea may fail.
9. Evidence briefing shown to the user.
10. Clarifying questions asked and user responses incorporated.
11. Publication-worthiness decision: proceed, revise, defer, or stop.

Do not proceed if the proposal cannot identify a concrete failure mode, baseline, and validation path.

Do not freeze Phase 1 from the first user idea alone. Phase 1 must include at least one evidence-backed debate round unless the user explicitly requests a narrow no-research sketch.

### Output artifact

Prefer one of:

- `docs/agent/research_direction.md`
- `docs/agent/brainstorming_brief.md`
- `docs/agent/hypotheses.md`
- a short section in `docs/current_status.md`
- a task-specific planning note

---

## Gate 2: Paper Reading Gate

Use this before treating a discovered source as evidence for novelty, baseline selection, dataset choice, evaluation protocol, claim support, or manuscript citation.

### Required checks

The source must answer:

- Why was this source selected?
- Was it discovered, skimmed, partially read, or deeply read?
- What task, method, dataset, benchmark, metric, or claim does it relate to?
- Is it closest prior work, a baseline source, a dataset/benchmark source, a method reference, a limitation source, or only background?
- What are the paper’s own claims?
- What evidence supports those claims?
- What are the paper’s limitations?
- How does it overlap with or differ from the current project?
- Does it support, weaken, or complicate the current research direction?
- Does it suggest a required baseline, dataset, metric, ablation, or caveat?
- What citation role, if any, should it have?

### Required output artifacts

For source triage:

- `sources/reading_queue.md`

For deeply used papers:

- `sources/paper_cards/`

For cross-paper comparison:

- `sources/literature_matrix.md`

When relevant, also update:

- `sources/baseline_candidates.md`
- `sources/citation_intent_map.md`
- `docs/agent/research_direction.md`
- `docs/agent/experiment_queue.md`
- `docs/agent/baseline_ledger.md`
- `docs/agent/claim_ledger.md`

### Stop rule

Do not treat lookup results as deeply read papers.

Do not use a source as strong novelty, baseline, or claim evidence unless it has a paper card or equivalent durable source artifact.

Do not cite a paper for a claim unless its citation intent is recorded or the citation role is otherwise explicit.

---

## Gate 3: Research Change Gate

Use this before model, loss, augmentation, training, or evaluation changes.

The agent must state:

1. why it fits the current project scope,
2. what baseline it is compared against,
3. what metric or failure mode it targets,
4. how it will be ablated,
5. what risk it introduces.

If any item is missing, do not implement the change yet.

For detailed expectations, use the smallest relevant guidance file:

- `.agents/guidance/cv-researcher.md`
- `.agents/guidance/cv-dev.md`
- `.agents/guidance/ai-ml-research-dev.md`
- `.agents/guidance/python-dev.md`

### Output artifact

For proposed research changes that are not yet approved to run, prefer:

- `docs/agent/experiment_queue.md`
- `docs/agent/implementation_notes.md`

For approved implementation work, prefer:

- `docs/PROJECT_PLAN.md`
- `docs/agent/experiment_plan.md`
- `runs/<experiment_or_run_id>/config.*`
- `runs/<experiment_or_run_id>/README.md`
- `outputs/<experiment_or_run_id>/summary.md`

A proposed method, loss, augmentation, training strategy, or evaluation protocol should enter `experiment_queue.md` when it is one candidate among several or when its priority is not yet clear.

---

## Gate 4: Implementation Gate

Use this before implementing research-related code.

The agent must define:

1. Intended artifact type:
   - code,
   - test,
   - config,
   - script,
   - notebook,
   - dataset metadata,
   - evaluation output,
   - documentation,
   - paper artifact.
2. Files expected to change.
3. Behavior expected to change.
4. Validation to run after the change.
5. Compatibility or reproducibility risk.
6. Whether the change affects paper claims, metrics, or previous results.

Do not mix unrelated artifact types unless explicitly requested.

Do not edit `paper/` during code-only tasks unless explicitly requested.

---

## Gate 5: Dataset and Leakage Gate

Use this before changing dataset loading, preprocessing, labels, splits, metadata, augmentation, or evaluation data.

The agent must check or explicitly document:

1. Dataset source or version.
2. Label schema and annotation format.
3. Train/validation/test split policy.
4. Whether repeated scenes, roads, videos, cameras, timestamps, or locations may cross splits.
5. Whether duplicate or near-duplicate samples may cross splits.
6. Whether augmented copies may leak across splits.
7. Whether filenames, metadata, or folder structure encode labels.
8. Whether preprocessing changes affect label coordinates, masks, or class meanings.
9. Whether evaluation data was used for tuning, prompt iteration, threshold selection, or visual cherry-picking.

Do not claim “no leakage” unless supported by an audit artifact or explicit reasoning.

### Required output artifacts

When dataset, split, preprocessing, label, or evaluation-data assumptions matter, create or update:

- `docs/agent/dataset_card.md`
- `docs/agent/leakage_audit.md`

When automated checks are run, save outputs under:

- `outputs/leakage/split_overlap_summary.json`
- `outputs/leakage/duplicate_report.csv`
- `outputs/leakage/hash_report.*`
- `outputs/leakage/metadata_leakage_report.*`

A short dataset note in `docs/current_status.md` is allowed only as a pointer to durable artifacts. It must not be the only dataset or leakage record for a serious experiment.

---

## Gate 6: Experiment Decision Gate

Use this before running expensive, long, or high-importance experiments.

If there are multiple possible experiments, limited compute, unclear priority, or an exploratory “what should we run next?” question, first update:

- `docs/agent/experiment_queue.md`

The queue should record candidate experiments, priority, decision enabled, expected information gain, cost, risk, and status.

Promote a queue item to an experiment plan only when it is specific enough to run.

A promoted experiment plan must state:

1. Research question.
2. Decision this experiment will enable.
3. Baseline or control.
4. Experimental change.
5. Metric or failure mode targeted.
6. Minimal viable version of the experiment.
7. Expected result if the hypothesis is true.
8. Expected result if the hypothesis is false.
9. Stop condition.
10. Compute, time, or cost risk.
11. Cheaper alternative, if available.
12. Required output artifacts.

Do not run the experiment if it will not change a decision.

### Required output artifacts

For experiment selection or prioritization, create or update:

- `docs/agent/experiment_queue.md`

For approved serious experiments, create or update:

- `docs/agent/experiment_plan.md`

Before execution, the experiment plan must define:

- linked hypothesis or research direction;
- decision enabled;
- baseline/control;
- experimental change;
- dataset/split/evaluation setting;
- metric or failure mode;
- minimal viable experiment;
- expected true/false outcomes;
- stop condition;
- compute/time/cost budget;
- required output artifacts.

During or after execution, create or update:

- `docs/agent/run_registry.md`
- `docs/agent/experiment_journal.md`
- `runs/<experiment_or_run_id>/`
- `outputs/experiments/<experiment_or_run_id>/`

When the experiment depends on a dataset, split, benchmark, or evaluation protocol, also create or update:

- `docs/agent/dataset_card.md`
- `docs/agent/leakage_audit.md`

When the experiment supports a comparison claim, also create or update:

- `docs/agent/baseline_ledger.md`

When the experiment supports a mechanism or component claim, also create or update:

- `docs/agent/ablation_matrix.md`

Do not treat a queued experiment as approved.
Do not treat chat-only experiment selection as a durable decision.
Do not run the experiment if it will not change a decision.

---

## Gate 7: Evaluation and Result Interpretation Gate

Use this before interpreting results, comparing methods, or summarizing findings.

The agent must state:

1. Evaluation split.
2. Metric implementation.
3. Preprocessing and postprocessing used during evaluation.
4. Thresholds, NMS settings, prompts, or decoding settings when relevant.
5. Baseline comparison.
6. Whether the result is single-run or multi-seed.
7. Relevant slices or failure modes.
8. Qualitative evidence, if useful.
9. Known limitations.
10. Whether the result supports a claim, a hypothesis, or only a preliminary observation.

Do not present exploratory or notebook-only results as final evidence unless the supporting outputs and configs are saved.

### Output artifact

For decision-relevant results, prefer:

- `docs/agent/result_cards/`
- `docs/agent/result_interpretation.md`
- `docs/agent/error_analysis.md`
- `docs/agent/negative_results.md`

For claim-facing results, also update:

- `docs/agent/result_to_claim_map.md`
- `docs/agent/claim_ledger.md`

Raw output artifacts may live under:

- `outputs/results_*`
- `outputs/ablation_*`
- `outputs/failure_analysis.md`
- `outputs/qualitative_examples/`

---

## Gate 8: Result-to-Claim Gate

Use this before turning results into claims, manuscript text, figures, tables, abstracts, or conclusions.

### Required checks

The result must answer:

- Which experiment plan produced this result?
- Which run registry entries support it?
- Which outputs, logs, metrics, predictions, or figures support it?
- What baseline/control is used?
- Is the comparison valid, conditionally valid, invalid, or unknown?
- What dataset/split/evaluation setting was used?
- Is leakage status passed, partial, failed, unknown, or not applicable?
- Is the result stable across seeds or only preliminary?
- What failure modes or slices were checked?
- What alternative explanations could explain the result?
- What claim does this result support, weaken, or refute?
- What wording is allowed?
- What wording is not allowed?

### Required output artifacts

Before a result can support a strong claim, create or update:

- `docs/agent/result_cards/`
- `docs/agent/result_to_claim_map.md`
- `docs/agent/claim_ledger.md`

When relevant, also create or update:

- `docs/agent/error_analysis.md`
- `docs/agent/negative_results.md`
- `docs/agent/figure_review.md`

### Stop rule

Do not turn raw metrics directly into manuscript claims.

If a result lacks a result card, claim mapping, or baseline/evaluation support, mark the claim as:

- `preliminary`
- `partially_supported`
- `needs_manual_check`
- `unsupported`

rather than supported.

---

## Gate 9: Claim Support Gate

Use this before writing, editing, or strengthening manuscript/report claims.

Every important claim must be classified as one of:

- supported,
- preliminary,
- hypothesis,
- needs citation,
- unsupported,
- contradicted.

A claim must identify its support:

- cited literature,
- experiment result,
- documented limitation,
- documented assumption,
- dataset or leakage audit,
- prior approved project context.

Do not use strong claim language unless the claim is supported.

### Strong language requiring evidence

Avoid these unless directly supported:

- novel,
- first,
- state-of-the-art,
- outperforms,
- robust,
- generalizes,
- eliminates,
- proves,
- demonstrates conclusively.

### Safer language

Prefer these when evidence is limited:

- we investigate,
- we evaluate,
- we compare,
- we test,
- preliminary results suggest,
- under this setting,
- in our experiments,
- this indicates,
- this may suggest.

### Output artifact

Prefer one of:

- `docs/agent/claim_ledger.md`
- `paper/agent/claim_support.md`
- a claim table in the manuscript notes

---

## Gate 10: Red-Team Review Gate

Use this before accepting major plans, conclusions, experiments, or paper claims.

A critic agent, reviewer agent, or separate pass must answer:

1. What is the weakest assumption?
2. What would make this result meaningless?
3. What baseline is missing?
4. What leakage risk remains?
5. What simpler explanation could explain the result?
6. What reviewer criticism is likely?
7. What evidence is missing?
8. What should be tested before believing the conclusion?
9. What claim should be weakened or removed?

The proposing agent should not be the only reviewer of its own research plan.

### Relevant skills

Use when helpful:

- `scientific-critical-thinking`
- `peer-review`
- `claim-auditor`

### Output artifact

Prefer one of:

- `paper/agent/review_context.md`
- `paper/agent/review_method.md`
- `paper/agent/review_domain.md`
- `paper/agent/review_hybrid.md`
- `paper/agent/review_meta.md`
- `paper/agent/revision_plan.md`
- `paper/agent/response_to_reviewers_draft.md`
- `paper/agent/claim_audit.md`
- `paper/agent/review_notes.md`

---

## Gate 11: Paper Writing Gate

Use this before drafting or revising manuscript text.

The agent must identify:

1. Section being edited.
2. Purpose of the edit.
3. Claims being introduced or modified.
4. Evidence supporting each claim.
5. Citations needed.
6. Results, figures, or tables referenced.
7. Uncertainty or limitations that must remain visible.
8. Whether the writing changes meaning or only improves clarity.

Do not polish uncertainty away.

Do not add claims only because they sound academically natural.

### Relevant skills

Use when helpful:

- `scientific-writing`
- `claim-auditor`
- `citation-management`
- `prior-style-adapter`
- `venue-templates`

### Output artifact

Prefer one of:

- `paper/agent/section_notes.md`
- `paper/agent/claim_support.md`
- `paper/agent/style_notes.md`
- manuscript files under `paper/`

---

## Gate 12: Final Handoff Gate

Use this at the end of substantial research, code, experiment, or writing tasks.

The final response must include:

1. Task stage.
2. Context checked.
3. Guidance or skills used.
4. Files changed.
5. Validation performed.
6. Evidence or artifacts produced.
7. Remaining uncertainty or risks.
8. Next recommended step.

For small tasks, this can be shortened, but changed files and validation should still be stated when applicable.

---

## Default rule

When uncertain, prefer the smallest gate that prevents the highest risk.

Do not apply gates mechanically.

A gate is passed only when the required information is specific enough that another agent or human can review it.

If a gate is passed but the live state in `docs/current_status.md` does not match the frozen artifacts, resolve the state mismatch before proceeding.
