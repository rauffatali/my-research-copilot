# Citation Use in Scientific Writing

This reference supports the `scientific-writing` skill.

Use it when deciding where citations are needed in prose and how to write citation-aware manuscript text.

For BibTeX cleanup, DOI/arXiv verification, citation-key hygiene, or hallucinated-reference detection, use `citation-management`.

For checking whether a cited source supports the sentence, use `claim-auditor`.

---

## 1. Purpose

Scientific writing should use citations to support claims, not to decorate paragraphs.

This reference helps writers decide:

- which sentences need citations;
- where citations should appear;
- how to avoid citation overuse;
- how to avoid citation misuse;
- when to hand off to `citation-management` or `claim-auditor`.

---

## 2. What Needs a Citation?

A sentence usually needs a citation when it states:

- prior work behavior;
- what existing methods do;
- what most studies assume;
- known limitations;
- research gaps;
- problem importance;
- dataset or benchmark facts;
- metric or evaluation conventions;
- field trends;
- domain facts external to the project;
- comparison to existing methods;
- claims about real-world impact from external sources.

Example needing citation:

```text
Most recent road damage detection systems formulate the task as object detection or semantic segmentation.
```

Example needing citation:

```text
The RDD datasets have been widely used to benchmark road damage detection models.
```

---

## 3. What May Not Need a Citation?

A sentence may not need a citation when it states:

- this paper’s goal;
- this paper’s method;
- this paper’s experiment setup;
- this paper’s result, if backed by tables/figures/run artifacts;
- a transition sentence;
- a definition introduced by the paper;
- a limitation directly observed in the project.

Example:

```text
In this work, we evaluate a detection pipeline under a fixed train-test split.
```

No external citation is needed, but the claim still needs project evidence.

---

## 4. Citation Placement

Place citations close to the claim they support.

Weak:

```text
Road damage detection is challenging. Cracks are thin and low contrast. Many methods use object detection. [1-5]
```

Better:

```text
Road damage detection is challenging because cracks may be thin, low contrast, or partially occluded [1,2]. Recent studies often formulate the task as object detection or segmentation [3-5].
```

Do not place one citation at the end of a paragraph if it only supports one sentence.

---

## 5. Citation Density

Citation density depends on section.

### Introduction

Use citations for problem importance, prior work, and gap framing.

Avoid citation overload.

### Related Work

Citation density is usually higher.

Group citations by theme and explain why each group matters.

### Method

Cite method families, datasets, metrics, and baseline implementations.

### Results

Cite prior results only when comparison is protocol-compatible.

### Discussion

Cite prior findings when comparing interpretation, limitations, or failure modes.

---

## 6. Citation Misuse Patterns

Avoid:

- citing a survey for a specific empirical result from another paper;
- citing a dataset paper as evidence that a model works;
- citing a benchmark page as peer-reviewed evidence;
- using a preprint as settled consensus;
- citing a real paper that does not support the sentence;
- using citations to make unsupported claims look supported;
- inventing citation keys.

If a citation may be wrong, use `claim-auditor`.

If a reference may be fake or malformed, use `citation-management`.

---

## 7. Citation Key Handling

Scientific writing may preserve or insert known verified citation keys.

Do not invent citation keys.

Acceptable:

```latex
Prior studies have evaluated road damage detection using object detection models~\cite{arya2020rdd}.
```

If the key is not known:

```text
TODO: needs citation for road damage detection object-detection framing.
```

Do not write:

```latex
\cite{smith2024roadDamageSurvey}
```

unless that key exists and has been verified.

---

## 8. Citation-Aware Related Work

Related work should synthesize.

Weak:

```text
Smith et al. used YOLO. Wang et al. used Faster R-CNN. Lee et al. used segmentation.
```

Better:

```text
Prior work has explored both detection-based and segmentation-based formulations. Detection-based methods localize damage instances with bounding boxes, while segmentation-based methods provide denser spatial predictions at higher annotation cost.
```

Then cite each group.

Use `literature-review` before writing this section.

---

## 9. Citation TODO Labels

Use clear TODOs:

```text
TODO: needs citation
TODO: needs stronger citation
TODO: citation may not support claim
TODO: needs closest prior work citation
TODO: needs dataset paper citation
TODO: needs metric definition citation
TODO: needs citation-management verification
```

These TODOs help downstream agents route work correctly.

---

## 10. Final Checklist

Before finalizing citation-aware writing:

- [ ] external claims have citations or TODOs;
- [ ] citation keys are not invented;
- [ ] citations are close to supported claims;
- [ ] broad claims are not supported by weak citations;
- [ ] related work uses synthesis, not citation dumping;
- [ ] suspicious references are routed to `citation-management`;
- [ ] citation-support questions are routed to `claim-auditor`.

---

## Final Reminder

A citation is not decoration.

It is a claim-support pointer.
