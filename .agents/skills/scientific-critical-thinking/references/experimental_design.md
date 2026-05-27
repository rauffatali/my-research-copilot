# AI/ML/CV Experimental Design

Use this reference when designing or critiquing experiments for AI, ML, and computer vision research.

The goal is to create experiments that answer research decisions, not just produce numbers.

---

## 1. Start With the Decision

Every experiment should answer:

```text
What decision will this experiment change?
```

Good decisions:

- keep or reject a method change;
- choose between baselines;
- accept or reject a hypothesis;
- justify an ablation claim;
- test a suspected failure mode;
- decide whether a larger experiment is worth running.

Weak decisions:

- see what happens;
- try the model;
- maybe improve results;
- generate more tables.

---

## 2. Define the Experimental Contract

Before running the experiment, define:

- task;
- input;
- output;
- dataset version;
- split;
- label schema;
- preprocessing;
- augmentation;
- model/config;
- baseline;
- metric;
- seed;
- hardware/compute if relevant;
- expected artifact location.

If the contract is unclear, results will be hard to audit.

---

## 3. Baseline Design

Every experiment needs a reference point.

Baseline options:

- current implementation;
- simple classical baseline;
- simple neural baseline;
- previous model version;
- prior-work baseline;
- frozen feature baseline;
- no-component ablation;
- random or majority baseline when relevant.

A baseline should be:

- fair;
- reproducible;
- not under-tuned relative to the proposed method;
- aligned with the claim.

Do not select a baseline only because it is easy to beat.

---

## 4. Controlled Comparison

A controlled experiment changes one meaningful factor at a time.

Control:

- dataset;
- split;
- metric;
- preprocessing;
- training schedule;
- augmentation;
- postprocessing;
- checkpoint selection;
- random seed or seed policy.

If multiple things change, do not claim which one caused the improvement without ablation.

---

## 5. Ablation Planning

Use ablations when claiming a component matters.

For each change, state:

1. component changed;
2. expected mechanism;
3. baseline without component;
4. metric or failure mode targeted;
5. risk/tradeoff;
6. minimum result needed to keep it.

Ablations should isolate the effect.

Bad ablation:

```text
Our full model beats baseline, so every component helps.
```

Good ablation:

```text
Full model, without dynamic convolution, and without attention are compared under the same split and training schedule.
```

---

## 6. Dataset and Split Design

Splits should match the intended claim.

Use random splits only when leakage risk is low.

Consider group-wise splits by:

- road segment;
- video;
- camera;
- location;
- user;
- patient;
- document;
- capture session;
- data source;
- time.

For CV, avoid splitting near-duplicate images, frames, patches, or scenes across train/test.

Document:

- split seed;
- split files;
- grouping rule;
- class distribution;
- source distribution;
- leakage checks.

---

## 7. Metric Design

Metrics must match the claim.

Examples:

- detection: mAP, AP50, AP75, per-class AP, recall, precision;
- segmentation: mIoU, Dice, boundary metrics;
- classification: accuracy, F1, AUROC, calibration;
- retrieval: Recall@K, MRR, nDCG;
- generation: task-specific metrics plus human/qualitative checks when needed.

Avoid metric mismatch:

```text
Claim: robust small-object detection
Metric only: overall mAP
```

Better:

```text
Report small-object AP or slice-specific recall.
```

---

## 8. Minimal Viable Experiment

Start small when possible.

Use:

- smoke tests;
- tiny-data run;
- overfit-one-batch test;
- frozen baseline;
- synthetic metric test;
- qualitative inspection;
- small ablation before full training.

Do not run expensive experiments before cheap checks remove obvious failure risks.

---

## 9. Reproducibility Requirements

For results that may support claims, save:

- config;
- seed;
- dataset version;
- split definition;
- code version;
- environment;
- run ID;
- metric definition;
- logs;
- outputs;
- result table;
- qualitative samples when relevant.

Notebook-only results should not support final claims unless artifacts are saved and documented.

---

## 10. Result Interpretation Plan

Before running, define:

- success criterion;
- failure criterion;
- ambiguous outcomes;
- what follow-up is needed;
- what claim the result can support;
- what claim it cannot support.

This prevents post-hoc overclaiming.

---

## 11. Common Design Failures

- no baseline;
- unfair baseline;
- multiple changes at once;
- missing ablation;
- metric does not match claim;
- leakage-prone split;
- cherry-picked best run;
- no saved config;
- no qualitative failure analysis;
- comparing to reported numbers under incompatible protocols;
- claiming generalization without held-out domain;
- running expensive experiments without decision value.

---

## 12. Experimental Design Checklist

Before running:

- [ ] decision is clear;
- [ ] claim to be supported is clear;
- [ ] baseline is defined;
- [ ] dataset/split is documented;
- [ ] leakage risk is considered;
- [ ] metric matches claim;
- [ ] ablation plan exists if needed;
- [ ] seed/reproducibility plan is defined;
- [ ] outputs will be saved;
- [ ] success/failure/ambiguous outcomes are defined;
- [ ] experiment cost is justified.

---

## Final Reminder

A good experiment is not the one with the most training hours.

A good experiment is the one that changes a research decision.
