# Reporting Standards for AI/ML/CV Peer Review

Use this reference with the `peer-review` skill when checking whether an AI/ML/CV manuscript reports enough information for scientific evaluation and reproducibility.

This file prioritizes AI/ML/CV reporting. General biomedical standards such as CONSORT, STROBE, and PRISMA are included only as optional extensions when the manuscript type requires them.

---

## 1. Core AI/ML/CV Reporting Standard

A paper should report enough detail for reviewers to understand:

- what was done;
- why it was done;
- how it was evaluated;
- whether the comparison is fair;
- what evidence supports the claims;
- what limitations remain;
- whether the work can be reproduced.

---

## 2. Problem and Task Reporting

Report:

- task definition;
- input and output;
- prediction unit;
- label schema;
- assumptions;
- scope boundaries;
- intended use or research setting;
- what is not being claimed.

Reviewer checks:

- Is the task clear?
- Is the output measurable?
- Are claims aligned with the task?
- Is domain context sufficient for applied work?

---

## 3. Dataset Reporting

Report:

- dataset name and version;
- source;
- collection process;
- sample count;
- class distribution;
- annotation process;
- label schema;
- annotator agreement or quality notes if available;
- split policy;
- train/validation/test sizes;
- known biases and limitations.

For CV, also report when relevant:

- image/video resolution;
- camera/source variation;
- scene/location/domain distribution;
- object size distribution;
- weather/lighting/occlusion conditions;
- near-duplicate or source-level leakage checks.

---

## 4. Preprocessing and Augmentation Reporting

Report:

- resizing/cropping;
- normalization;
- filtering;
- patch/frame extraction;
- train-only fitting for preprocessing;
- augmentations;
- augmentation probabilities;
- label transformations;
- test-time preprocessing;
- postprocessing.

Reviewer checks:

- Could preprocessing leak test information?
- Is train/test behavior consistent?
- Are augmentations appropriate for the task/domain?

---

## 5. Model and Method Reporting

Report:

- architecture;
- pretrained weights;
- input resolution;
- loss functions;
- optimization method;
- learning rate schedule;
- batch size;
- epochs/steps;
- regularization;
- inference procedure;
- postprocessing;
- implementation framework;
- code/config availability if applicable.

Reviewer checks:

- Is the method reproducible?
- Are new components justified?
- Is complexity tied to a hypothesis or failure mode?

---

## 6. Baseline Reporting

Report:

- baseline names;
- baseline source or implementation;
- training protocol;
- hyperparameters;
- tuning effort;
- data/split used;
- metric used;
- whether baselines were rerun or copied from literature.

Reviewer checks:

- Are baselines fair?
- Are comparisons protocol-compatible?
- Is a simple baseline included?
- Is a strong baseline included?

---

## 7. Evaluation Reporting

Report:

- primary metric;
- secondary metrics;
- exact metric definitions;
- threshold selection;
- validation/test distinction;
- confidence intervals or seed variance when relevant;
- per-class or per-slice metrics when relevant;
- failure analysis;
- qualitative examples.

For detection:

- mAP convention;
- IoU thresholds;
- AP50/AP75;
- per-class AP;
- recall/precision;
- small/medium/large object metrics if relevant.

For segmentation:

- mIoU;
- Dice/F1;
- boundary metrics if relevant.

Reviewer checks:

- Does metric match claim?
- Are comparisons under the same protocol?
- Are claims broader than metrics?

---

## 8. Ablation Reporting

Report:

- component removed or changed;
- baseline variant;
- controlled conditions;
- metric effect;
- expected mechanism;
- negative or ambiguous results.

Reviewer checks:

- Does ablation isolate the claim?
- Are multiple components changed at once?
- Is the mechanism actually tested?

---

## 9. Reproducibility Reporting

Report:

- code version;
- data version;
- config files;
- random seeds;
- environment;
- hardware;
- training time;
- inference time if relevant;
- checkpoint selection;
- saved artifacts;
- result table source.

Reviewer checks:

- Could another researcher reproduce the result?
- Are enough details available to audit the claim?

---

## 10. Claim and Limitation Reporting

Report:

- exact contribution;
- claim scope;
- evidence for each main claim;
- limitations;
- failure modes;
- deployment assumptions;
- ethical or societal risks when relevant.

Reviewer checks:

- Are claims proportional?
- Are limitations specific?
- Does conclusion introduce unsupported claims?

---

## 11. Applied AI / Domain Reporting

For applied AI/CV papers, report:

- domain problem definition;
- domain label meaning;
- annotation protocol;
- domain-specific metrics or slices;
- real-world constraints;
- deployment assumptions;
- domain limitations;
- practical significance of errors.

Reviewer checks:

- Does the technical evaluation matter in the domain?
- Are domain-specific failure modes considered?
- Does the paper avoid claiming impact from metric gain alone?

---

## 12. Optional Standards for Special Manuscript Types

Use these only when appropriate.

### PRISMA

Use for systematic reviews or meta-analyses.

Check:

- search strategy;
- inclusion/exclusion criteria;
- screening flow;
- extraction;
- synthesis;
- limitations.

### CONSORT

Use for randomized clinical trials.

Not normally relevant to AI/CV method papers unless the manuscript is a clinical trial.

### STROBE

Use for observational epidemiological studies.

Relevant only for clinical/observational study designs.

### TRIPOD / CLAIM / DECIDE-AI

May be relevant for clinical prediction models or medical AI reporting.

Use only when the manuscript domain requires it.

---

## 13. Reporting Checklist

Before approving manuscript reporting quality:

- [ ] task is clear;
- [ ] dataset and split are documented;
- [ ] preprocessing and augmentation are described;
- [ ] model/training details are sufficient;
- [ ] baselines are described fairly;
- [ ] metrics are defined;
- [ ] evaluation protocol is reproducible;
- [ ] ablations support component claims;
- [ ] failure analysis or limitations are included;
- [ ] claim scope is clear;
- [ ] domain-specific reporting is included when relevant;
- [ ] special reporting standards are used only when appropriate.

---

## Final Reminder

Reporting quality is not formatting polish.

A paper is well reported when a reviewer can trace claims back to methods, data, experiments, and limitations.
