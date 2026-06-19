# Dataset Card

## Status

- draft
- Allowed values: draft, frozen, superseded

## Purpose

This file records the dataset, split, preprocessing, labels, and evaluation assumptions used by the project.

Use this for local project data, benchmark data, generated data, synthetic data, or external datasets.

## Dataset Index

| Dataset ID | Name | Version | Split policy | Task | Status | Leakage audit |
|---|---|---|---|---|---|---|
| DATA-001 | | | | | draft / active / deprecated | `docs/agent/leakage_audit.md` |

---

## DATA-001: [Dataset Name]

### Status

- draft
- Allowed values: draft, active, deprecated, superseded

### Source

- Dataset name:
- Dataset version:
- Source URL or local path:
- License/usage notes:
- Download or generation method:
- Date accessed or generated:

### Task Definition

- Input:
- Output:
- Label schema:
- Class definitions:
- Unit of prediction:
- Evaluation target:

### Splits

| Split | Size | Source | Notes |
|---|---:|---|---|
| train | | | |
| validation | | | |
| test | | | |

### Split Policy

[Explain how train/validation/test are separated.]

Check when relevant:

- [ ] scene-level split
- [ ] video-level split
- [ ] subject-level split
- [ ] patient/user-level split
- [ ] document-level split
- [ ] temporal split
- [ ] location/camera/device-level split
- [ ] random split
- [ ] benchmark-provided split
- [ ] unknown

### Preprocessing

- Input preprocessing:
- Label preprocessing:
- Filtering:
- Normalization:
- Augmentation:
- Tokenization / feature extraction:
- Resizing/cropping:
- Missing data handling:

### Evaluation Protocol

- Metric(s):
- Thresholds:
- Postprocessing:
- Decoding settings:
- Aggregation:
- Slice analysis:
- Qualitative evaluation:

### Known Risks

- Leakage:
- Label noise:
- Class imbalance:
- Distribution shift:
- Annotation ambiguity:
- Duplicate or near-duplicate samples:
- Benchmark mismatch:
- Ethical/safety issue:

### Linked Artifacts

- Leakage audit:
- Experiment plans:
- Run registry:
- Output summaries:

### Next Step

- [State whether dataset is ready, needs audit, needs cleaning, or should not be used.]