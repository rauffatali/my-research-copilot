# Scientific Reporting Guidelines

This reference supports the `scientific-writing` skill.

Use it when writing or revising scientific reports and manuscripts so that claims, methods, experiments, results, and limitations are reported transparently.

For venue-specific reporting rules, use `venue-templates`.

For claim support, use `claim-auditor`.

For citation/reference integrity, use `citation-management`.

---

## 1. Core Reporting Principle

A report should make the research auditable.

A reader should be able to understand:

- what was studied;
- why it matters;
- what was done;
- what data was used;
- how evaluation was performed;
- what the evidence shows;
- what the evidence does not show;
- what limitations remain.

---

## 2. Problem Reporting

Report:

- problem statement;
- task definition;
- input/output;
- target users or research setting, if relevant;
- scope boundaries;
- assumptions.

Avoid:

- broad problem claims without citations;
- deployment claims without deployment evidence;
- vague motivation.

---

## 3. Literature and Background Reporting

Report:

- prior work themes;
- closest prior work;
- gap or limitation;
- citation-backed context.

Use `literature-review`.

Do not invent citations or gap claims.

---

## 4. Dataset Reporting

For AI/ML/CV work, report:

- dataset name and version;
- source;
- collection conditions;
- number of samples;
- class distribution;
- annotation format;
- label schema;
- annotation quality notes;
- split policy;
- train/validation/test sizes;
- leakage checks;
- limitations.

For road damage detection, consider:

- road type;
- weather/lighting;
- camera perspective;
- damage classes;
- severity if available;
- geographic/source distribution;
- small or low-contrast damage cases.

---

## 5. Method Reporting

Report:

- model or pipeline;
- input preprocessing;
- training objective;
- augmentation;
- optimization;
- hyperparameters;
- inference;
- postprocessing;
- implementation details required for reproducibility.

Do not report intended behavior as demonstrated performance.

---

## 6. Experiment Reporting

Report:

- baselines;
- dataset/split;
- metrics;
- training protocol;
- evaluation protocol;
- ablation settings;
- hardware or compute when relevant;
- seed policy when relevant.

If results are not final, use `results-scaffold`.

---

## 7. Result Reporting

Report:

- exact metrics;
- comparison condition;
- evaluated setting;
- result tables;
- figures;
- qualitative examples when relevant;
- negative or ambiguous results when important.

Avoid:

- invented values;
- claiming significance without testing;
- comparing incompatible protocols;
- overgeneralizing.

---

## 8. Limitation Reporting

Report specific limitations.

Examples:

- one dataset only;
- one split only;
- no cross-domain evaluation;
- limited baseline coverage;
- no multi-seed analysis;
- annotation noise;
- class imbalance;
- deployment not tested;
- failure modes not fully characterized.

Limitations should not be generic filler.

---

## 9. Reproducibility Reporting

Report enough detail for reproduction:

- code version;
- config;
- data version;
- split files;
- seeds;
- environment;
- hardware;
- training schedule;
- checkpoint selection;
- metric implementation.

---

## 10. Ethics and Responsible Reporting

When relevant, report:

- dataset bias;
- privacy;
- fairness;
- annotation uncertainty;
- deployment risk;
- misuse potential;
- environmental/compute cost;
- limitations of automation.

Do not claim real-world readiness without evidence.

---

## 11. Optional Formal Standards

Use only when relevant.

- PRISMA: systematic/scoping reviews.
- CONSORT: randomized clinical trials.
- STROBE: observational health studies.
- TRIPOD/CLAIM/DECIDE-AI: clinical prediction or medical AI contexts.

Do not force biomedical reporting standards onto ordinary AI/CV method papers.

---

## 12. Reporting Checklist

Before finalizing a section:

- [ ] problem is clear;
- [ ] task and scope are clear;
- [ ] literature claims have citations;
- [ ] dataset and split are reported;
- [ ] method is reproducible enough;
- [ ] baselines are described;
- [ ] metrics are defined;
- [ ] results are supported by artifacts;
- [ ] limitations are specific;
- [ ] claims are proportional;
- [ ] missing evidence is marked;
- [ ] final claims are routed to `claim-auditor`.

---

## Final Reminder

Good reporting makes the paper easier to trust.

It should expose the path from evidence to claim.
