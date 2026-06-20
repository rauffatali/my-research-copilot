# Paper Cards

## Purpose

This directory stores structured reading notes for individual papers or source artifacts.

A paper card is deeper than a lookup result and more specific than a literature synthesis.

It should answer:

- What problem does the paper address?
- What method does it use?
- What evidence supports its claims?
- What dataset, benchmark, metric, and baseline does it use?
- What are its limitations?
- How does it overlap with or challenge the current project?
- What citation role could it play?

## Paper Card Rule

A paper should have a paper card when it is used for:

- closest prior work;
- novelty assessment;
- baseline selection;
- benchmark or dataset choice;
- method comparison;
- claim support;
- related work;
- reviewer-risk analysis;
- experiment design.

Do not treat a lookup result as a paper card.

Do not treat an abstract-only skim as deep reading.

## Naming

Use stable names:

- `2024_author_shorttitle.md`
- `2023_smith_robust_detection.md`
- `2022_lee_dataset_benchmark.md`

## Reading Depth Values

Use:

- `discovered`
- `skimmed`
- `partially_read`
- `deeply_read`
- `needs_full_text`
- `needs_verification`

## Relationship to Other Artifacts

Input artifacts:

- `sources/reading_queue.md`
- saved lookup outputs under `sources/`
- PDFs, URLs, repositories, benchmark pages, or dataset cards

Output artifacts:

- `sources/literature_matrix.md`
- `sources/baseline_candidates.md`
- `sources/citation_intent_map.md`
- `docs/agent/research_direction.md`
- `docs/agent/experiment_queue.md`
- `docs/agent/baseline_ledger.md`
- `docs/agent/result_to_claim_map.md`
- `paper/agent/citation_support.md`