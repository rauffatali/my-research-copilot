# AI/CV Research Failure Patterns

This reference lists common failure modes in AI, ML, and computer vision research.

Use it when applying `scientific-critical-thinking` to research directions, method proposals, experiment plans, result interpretation, or paper claims.

The goal is to detect weak research reasoning before it becomes code, experiments, or manuscript text.

---

## 1. Shallow research directions

A research direction is shallow when it sounds plausible but does not identify a concrete scientific problem.

### Common signs

- The proposal is mainly “try a newer model.”
- The expected improvement is vague.
- No failure mode is named.
- No baseline is identified.
- No metric or decision criterion is defined.
- The contribution target is much larger than the experiment plan.

### Examples

Weak:

> Use a transformer-based architecture to improve object detection.

Stronger:

> Test whether adding global context reduces false negatives for small or partially occluded objects compared with the current baseline under the same evaluation protocol.

### Critical questions

1. What specific limitation is being addressed?
2. Why should this method address that limitation?
3. What simpler baseline should be tested first?
4. What evidence would make the idea worth continuing?
5. What result would make us abandon the idea?

---

## 2. Implementation progress mistaken for research progress

Research agents often create code, configs, scripts, and modules that look productive but do not improve the scientific contribution.

### Common signs

- New code does not test a hypothesis.
- Multiple features are implemented before a baseline is stable.
- Engineering complexity increases without a research decision.
- Scripts are added without saved outputs or evaluation protocol.
- Refactoring changes behavior without documenting the effect.

### Critical questions

1. What research question does this implementation help answer?
2. What decision becomes possible after this change?
3. What artifact will prove the change worked?
4. Can a smaller implementation answer the same question?
5. Does this change affect previous results or paper claims?

---

## 3. Baseline weakness

A method comparison is weak when the baseline is unfair, outdated, undertuned, or not aligned with the claim.

### Common signs

- The proposed method gets more tuning than the baseline.
- The baseline uses different preprocessing.
- The baseline is not the current strongest internal reference.
- The comparison omits a simple strong baseline.
- The baseline is selected because it is easy to beat.

### Critical questions

1. What is the simplest meaningful baseline?
2. What is the strongest practical baseline?
3. Are baseline and proposed method evaluated under the same protocol?
4. Does the baseline match the claim being made?
5. Would reviewers consider this comparison fair?

---

## 4. Ablation weakness

Ablations are weak when they cannot isolate the reason for improvement.

### Common signs

- Too many changes are introduced at once.
- The ablation removes a component but also changes compute, data, or training.
- Only positive ablations are reported.
- The ablation does not match the claimed mechanism.
- No negative or neutral result is acknowledged.

### Critical questions

1. What exact mechanism is the ablation testing?
2. Can the effect be isolated?
3. What is the minimal ablation?
4. What result would contradict the proposed explanation?
5. Are compute, parameters, data, and training budget controlled?

---

## 5. Metric mismatch

A result is weak when the metric does not measure the claimed improvement.

### Examples

- Claiming robustness but reporting only in-domain accuracy.
- Claiming better small-object detection but reporting only global mAP.
- Claiming fewer false negatives but reporting only precision.
- Claiming real-world readiness but not reporting latency or failure modes.
- Claiming better segmentation boundaries but reporting only region overlap.

### Critical questions

1. What does the claim actually require measuring?
2. Does the metric capture the target failure mode?
3. Are slice metrics needed?
4. Are qualitative examples needed?
5. Can the metric be gamed by thresholding or postprocessing?

---

## 6. Overclaiming from limited evidence

Agents may write conclusions that are stronger than the artifacts support.

### Common signs

- Single-run result becomes a general conclusion.
- In-domain validation becomes a generalization claim.
- An exploratory result becomes a demonstrated finding.
- A small improvement becomes a contribution claim.
- A method is described as robust without stress testing.

### Safer labels

Use:

- hypothesis;
- preliminary;
- exploratory;
- observed in this setting;
- suggests;
- may indicate;
- requires validation.

Avoid unless directly supported:

- proves;
- demonstrates conclusively;
- robust;
- generalizes;
- state-of-the-art;
- eliminates;
- solves.

---

## 7. Novelty misunderstanding

A contribution is not necessarily novel because an exact combination was not found.

### Common signs

- “Novel” means “new to this project.”
- Closest prior work is not identified.
- The contribution is a routine adaptation.
- The paper claims method novelty when the real contribution is evaluation or dataset analysis.
- The method is common in adjacent domains.

### Critical questions

1. What exactly is claimed as new?
2. What is the closest prior work?
3. Is the difference meaningful?
4. Is the novelty technical, empirical, dataset-related, or framing-related?
5. Is the claim safer as “we evaluate,” “we adapt,” or “we investigate”?

---

## 8. Benchmark overfitting

Benchmark overfitting happens when research choices are repeatedly optimized around a fixed validation or test setup.

### Common signs

- Many design choices are made after viewing validation/test failures.
- The same test set is used for model selection.
- Qualitative examples guide repeated tuning.
- Thresholds are tuned on the final evaluation set.
- The method performs well only on a narrow benchmark.

### Critical questions

1. Which split guided model design?
2. Was the test set inspected before final evaluation?
3. Were thresholds tuned on validation or test data?
4. Is there a held-out domain or untouched test set?
5. Are conclusions limited to the benchmark?

---

## 9. Qualitative cherry-picking

Visual examples can mislead if they are selected informally.

### Common signs

- Only successful examples are shown.
- Failure cases are omitted.
- Examples are selected after seeing results.
- No criteria are given for choosing examples.
- Worst cases or false positives/negatives are not inspected.

### Better practice

Include at least one of:

- random examples;
- best/worst examples by metric;
- false positives;
- false negatives;
- slice-specific examples;
- representative failure clusters.

---

## 10. Compute-expensive but low-information experiments

An experiment is weak if it consumes resources but will not change a decision.

### Common signs

- No decision is attached to the experiment.
- Success criterion is vague.
- The experiment changes many variables at once.
- A cheaper smoke test could reveal the same issue.
- No stop condition is defined.

### Critical question

Before running the experiment, ask:

> What decision will this experiment change?

If the answer is unclear, the experiment is not ready.
