# Baseline Ledger

## Status

- draft
- Allowed values: draft, frozen, superseded

## Purpose

This file records which baselines, controls, references, and comparison points are valid for the project.

Do not claim improvement over a baseline unless the baseline is listed here and the comparison is marked valid or conditionally valid.

## Baseline Index

| Baseline ID | Name | Type | Source | Implementation path | Dataset/split | Metric | Status | Comparison validity |
|---|---|---|---|---|---|---|---|---|
| BASE-001 | | reproduced / imported / official / literature / heuristic / human / ablation control | | | | | draft / active / deprecated | valid / conditionally_valid / invalid / unknown |

---

## BASE-001: [Baseline Name]

### Status

- draft
- Allowed values: draft, active, deprecated, superseded

### Baseline Type

Choose one:

- reproduced baseline
- official implementation
- imported reported result
- simple heuristic
- ablation control
- previous project version
- human/reference comparison
- literature-only comparison

### Source

- Paper:
- Repository:
- Model card:
- Dataset/benchmark page:
- Prior run:
- Citation/source artifact:

### Implementation

- Code path:
- Config path:
- Run path:
- Commit:
- Notes:

### Evaluation Setting

- Dataset:
- Split:
- Preprocessing:
- Postprocessing:
- Metric:
- Number of seeds:
- Hardware/runtime caveat:

### Comparison Validity

Choose one:

- valid
- conditionally_valid
- invalid
- unknown

### Why This Comparison Is or Is Not Fair

[State whether dataset, split, metric, preprocessing, tuning, and compute are comparable.]

### Known Caveats

- [List caveats.]

### Claims Allowed

Examples:

- “Comparable to BASE-001 under the same split.”
- “Improves over our reproduced baseline on metric X.”
- “Cannot claim SOTA because baseline is literature-only and settings differ.”

### Claims Not Allowed

Examples:

- “Outperforms prior work” if settings differ.
- “State-of-the-art” without complete benchmark comparison.
- “Robust” without slice or stress-test evidence.

### Next Step

- [State whether to reproduce, replace, validate, or use baseline.]