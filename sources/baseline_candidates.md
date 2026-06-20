# Baseline Candidates

## Purpose

This file tracks baselines, controls, benchmarks, and comparisons suggested by the literature.

It is a source-facing companion to `docs/agent/baseline_ledger.md`.

Use this file to decide which literature baselines should become project baselines.

## Candidate Baselines

| Candidate ID | Baseline / method | Source paper card | Task/dataset | Why reviewer may expect it | Feasibility | Priority | Decision |
|---|---|---|---|---|---|---|---|
| BASECAND-001 | | | | | easy / medium / hard / unavailable | required / useful / optional / reject | promote / defer / reject |

## Promotion Rules

Promote a candidate to `docs/agent/baseline_ledger.md` when:

- it is a standard comparison in the literature;
- it is used by closest prior work;
- reviewers are likely to expect it;
- it is necessary for a performance, robustness, or novelty claim;
- it provides a strong simple control;
- it tests whether the proposed method improves over a meaningful alternative.

Do not promote a baseline if:

- the evaluation setting is incompatible;
- implementation is unavailable and not worth reproducing;
- the baseline is weak or irrelevant;
- the comparison would be misleading;
- it is only cited for background.

## Rejected or Deferred Baselines

| Candidate ID | Reason | Future condition for reconsideration |
|---|---|---|
| | | |

## Next Step

[State which baseline candidate should be promoted, rejected, or investigated.]