# Research Gates

This document defines mandatory checkpoints for high-impact research workflow decisions.

Use these gates before major research direction, implementation, experiment, evaluation, or paper-claim changes.

The goal is not to slow down progress. The goal is to prevent shallow ideas, unnecessary implementation, weak experiments, leakage, unsupported claims, and paper text that is stronger than the evidence.

Use the smallest relevant gate. Do not apply every gate by default.

Gates 1-5 correspond to the five workflow phases:

- Gate 1 -> Phase 1: Brainstorming / Research Formalization
- Gate 2 -> Phase 2: Implementation / Experimentation
- Gate 3 -> Phase 3: Result Consolidation
- Gate 4 -> Phase 4: Writing / Manuscript Drafting
- Gate 5 -> Phase 5: Multi-Agent Review / Red-Team

Gates 6-10 are cross-cutting downstream checks that can apply across multiple phases.

The canonical transition rules for moving between these phases live in `docs/workflow_state_machine.md`.

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

## Gate 2: Research Change Gate

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

Prefer one of:

- `docs/agent/project_plan.md`
- `docs/agent/implementation_notes.md`
- `runs/<run_id>/config.*`
- `runs/<run_id>/README.md`
- `outputs/<experiment_name>/summary.md`

---

## Gate 3: Implementation Gate

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

## Gate 4: Dataset and Leakage Gate

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

### Output artifact

Prefer one of:

- `docs/agent/leakage_audit.md`
- `outputs/leakage/split_overlap_summary.json`
- `outputs/leakage/duplicate_report.csv`
- a dataset section in `docs/current_status.md`

---

## Gate 5: Experiment Decision Gate

Use this before running expensive, long, or high-importance experiments.

The experiment plan must state:

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

### Output artifact

Prefer one of:

- `docs/agent/experiment_plan.md`
- `runs/<run_id>/config.*`
- `runs/<run_id>/README.md`
- `outputs/experiments/<experiment_name>/summary.md`

---

## Gate 6: Evaluation and Result Interpretation Gate

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

Prefer one of:

- `docs/agent/result_interpretation.md`
- `docs/agent/claim_ledger.md`
- `outputs/results_*`
- `outputs/ablation_*`
- `outputs/failure_analysis.md`
- `outputs/qualitative_examples/`

---

## Gate 7: Claim Support Gate

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

## Gate 8: Red-Team Review Gate

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

## Gate 9: Paper Writing Gate

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

## Gate 10: Final Handoff Gate

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
