# Figures and Tables in Scientific Writing

This reference supports the `scientific-writing` skill.

Use it when writing figure/table captions, referring to visual evidence in manuscript prose, or deciding whether a visual artifact is needed.

For technical diagrams, use `scientific-schematics`.

For general non-technical images, use `generate-image`.

For result table scaffolding, use `results-scaffold`.

For venue-specific figure/table rules, use `venue-templates`.

---

## 1. Core Principle

Figures and tables should support claims.

Do not describe a figure, table, or visual artifact as existing unless it exists or is explicitly being created.

If a visual is needed but missing, mark:

```text
TODO: needs figure
TODO: needs result table
TODO: needs schematic
TODO: needs qualitative examples
```

---

## 2. When to Use Tables

Use tables for:

- numeric results;
- baseline comparisons;
- ablations;
- robustness subsets;
- dataset statistics;
- hyperparameters;
- model variants;
- failure mode counts.

Use `results-scaffold` when final values are not ready.

Do not invent table values.

---

## 3. When to Use Figures

Use figures for:

- model architecture;
- method pipeline;
- data-processing flow;
- qualitative examples;
- failure cases;
- dataset examples;
- metric trends;
- domain workflow;
- taxonomy.

Use `scientific-schematics` for technical diagrams.

Use `generate-image` only for general visual assets.

---

## 4. Caption Writing

A good caption should explain:

1. what is shown;
2. what the reader should notice;
3. what setup or metric is used;
4. what limitation applies, if relevant.

Weak caption:

```text
Results of the method.
```

Better caption:

```text
Detection examples on the test split. Green boxes indicate correct detections, while red boxes indicate missed or false-positive instances.
```

Do not use captions to introduce unsupported claims.

---

## 5. Referring to Figures and Tables

In prose, refer to figures/tables by their role.

Example:

```text
Table 2 compares the proposed model with the evaluated baselines under the same split and mAP protocol.
```

Example:

```text
Figure 4 shows representative false positives caused by shadows and lane markings.
```

Avoid:

```text
As shown in Figure 4, the model is robust.
```

unless the figure actually supports robustness.

---

## 6. Results Tables

For result tables, include:

- method names;
- baseline identifiers;
- dataset/split;
- metric names;
- units;
- best/second-best formatting only when appropriate;
- notes about protocol differences.

Do not compare methods under incompatible protocols without marking it.

---

## 7. Ablation Tables

Ablation tables should isolate changes.

Include:

- full model;
- baseline model;
- each removed/changed component;
- same dataset/split;
- same metric;
- notes about controlled conditions.

Avoid ablation tables where many variables change at once.

---

## 8. Dataset Tables

Dataset tables may include:

- number of images/videos/samples;
- class counts;
- split sizes;
- source/domain breakdown;
- annotation type;
- label quality notes;
- limitations.

For applied AI/CV, dataset tables can make domain validity clearer.

---

## 9. Qualitative Figures

Qualitative figures should not cherry-pick only successful examples.

Include when possible:

- successes;
- failures;
- difficult cases;
- false positives;
- false negatives;
- domain-specific edge cases.

Captions should identify what the examples demonstrate and what they do not demonstrate.

---

## 10. Visual Artifact Handoff

Use:

```text
scientific-schematics
```

for:

- architecture diagrams;
- method pipelines;
- experimental workflows;
- flowcharts;
- scientific schematics.

Use:

```text
generate-image
```

for:

- general illustrations;
- conceptual artwork;
- non-technical visual assets.

Use:

```text
results-scaffold
```

for:

- result tables;
- ablation tables;
- robustness tables;
- result placeholders.

---

## 11. Figure/Table Checklist

Before finalizing figure/table prose:

- [ ] the artifact exists or is marked as TODO;
- [ ] caption accurately describes the artifact;
- [ ] no unsupported claim is introduced;
- [ ] metric/protocol is clear;
- [ ] comparisons are fair;
- [ ] qualitative examples are not misleading;
- [ ] result values are verified;
- [ ] venue-specific format is checked if needed.

---

## Final Reminder

Figures and tables are evidence, not decoration.

They should make the manuscript easier to verify.
