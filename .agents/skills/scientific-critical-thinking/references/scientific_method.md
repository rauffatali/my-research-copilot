# Scientific Method for AI/ML/CV Research

Use this reference to keep AI/ML/CV research work scientific rather than merely technical.

---

## 1. Core Principles

### Empiricism

Claims should be grounded in observable evidence:

- experiment artifacts;
- metrics;
- qualitative outputs;
- dataset audits;
- literature sources;
- implementation records.

### Falsifiability

A research hypothesis should be testable and refutable.

Weak:

```text
Use a better model to improve performance.
```

Stronger:

```text
Adding global context will reduce false negatives for small, partially occluded objects compared with the current detector.
```

### Reproducibility

Research claims should be traceable to saved artifacts:

- configs;
- code version;
- data version;
- split;
- seed;
- metrics;
- logs;
- outputs.

### Parsimony

Prefer the simplest method that can test the hypothesis.

Add complexity only when tied to a clear mechanism, baseline, and validation plan.

---

## 2. AI/ML/CV Research Cycle

### 1. Define the Problem

Specify:

- task;
- input;
- output;
- constraints;
- target metric;
- deployment or research setting;
- baseline/reference point.

### 2. Review Prior Work

Use `research-lookup` and `literature-review` to identify:

- closest prior work;
- standard baselines;
- datasets;
- evaluation protocols;
- known limitations;
- research gaps.

### 3. Form Hypothesis

State:

- expected effect;
- mechanism;
- target failure mode;
- baseline;
- metric;
- falsifying outcome.

### 4. Design Experiment

Plan:

- controlled comparison;
- dataset/split;
- metric;
- ablation;
- seed policy;
- outputs;
- decision criterion.

### 5. Implement Carefully

Ensure:

- train/eval separation;
- data contract;
- metric correctness;
- config-driven behavior;
- saved artifacts;
- smoke tests.

### 6. Analyze Results

Check:

- baseline fairness;
- variance;
- leakage;
- failure modes;
- qualitative examples;
- alternative explanations.

### 7. State Claims Proportionally

Use `claim-auditor` before final manuscript claims.

---

## 3. Hypothesis Quality

A good AI/CV hypothesis includes:

- specific limitation;
- proposed mechanism;
- baseline;
- target metric or failure mode;
- expected direction of effect;
- ablation or isolation plan;
- risk/tradeoff.

Example:

```text
Hypothesis: multi-scale training will improve recall on small objects without reducing large-object AP by more than 1 point.
```

This is better than:

```text
Try stronger augmentation.
```

---

## 4. Scientific vs Engineering Progress

Engineering progress:

- cleaner code;
- faster training;
- new scripts;
- refactoring;
- better logging.

Scientific progress:

- clearer hypothesis;
- stronger baseline;
- decisive experiment;
- leakage-safe evaluation;
- supported claim;
- better understanding of failure modes.

Engineering work is valuable, but do not confuse it with contribution evidence.

---

## 5. Alternative Explanations

For any positive result, ask:

- Is the baseline unfair?
- Did preprocessing change?
- Did the split change?
- Was the test set leaked?
- Was postprocessing different?
- Was the metric implemented correctly?
- Was the result cherry-picked?
- Could variance explain the gain?
- Did compute or training budget differ?
- Is the improvement only on easy cases?

A claim is stronger when plausible alternatives are ruled out.

---

## 6. Negative and Null Results

Negative results can be scientifically useful when they are well designed.

Record:

- what was tested;
- why it was expected to help;
- what result occurred;
- what was ruled out;
- whether the failure was implementation, hypothesis, or data related.

Do not hide negative results if they guide research decisions.

---

## 7. Scope Discipline

Do not broaden a project because a tool can implement more.

Before expanding scope, state:

1. why it fits the project;
2. what prior work or baseline it relates to;
3. what contribution or failure mode it targets;
4. how it can be validated;
5. what risk or tradeoff it introduces.

---

## 8. Scientific Method Checklist

Before approving a research direction or experiment:

- [ ] problem is defined;
- [ ] baseline exists;
- [ ] prior work context is known enough;
- [ ] hypothesis is testable;
- [ ] metric matches claim;
- [ ] dataset/split is appropriate;
- [ ] leakage risks are considered;
- [ ] ablation plan exists for component claims;
- [ ] result interpretation plan is defined;
- [ ] claims will be audited before writing.

---

## Final Reminder

Scientific method in AI/CV is not only about running experiments.

It is about running the right experiment for the right claim under conditions that make the result interpretable.
