# Sources

## Purpose

This directory stores external evidence artifacts used by the research workflow.

It includes:

- source discovery outputs from `research-lookup`;
- paper reading notes;
- literature matrices;
- baseline and benchmark candidates;
- citation-intent notes;
- source material used for research direction, experiments, claims, writing, and review.

`research-lookup` finds candidate sources.
Paper cards record deep reading of selected sources.
`literature-review` synthesizes selected sources into research context.

## Source Workflow

Preferred flow:

`research-lookup` -> `reading_queue.md` -> `paper_cards/` -> `literature_matrix.md` -> `literature-review` -> downstream research decisions

Do not treat lookup results as deeply read papers.

Do not treat paper abstracts as enough evidence for novelty, baseline, or claim decisions.

Do not cite a paper in manuscript prose only because it appeared in a lookup result.

## Literature Evidence Rule

A lookup result is not a read paper.

A paper should become a paper card before it is used as strong evidence for novelty, baseline selection, dataset choice, evaluation protocol, claim support, or manuscript citation.

Preferred chain:

`research-lookup` -> `reading_queue.md` -> `paper_cards/` -> `literature_matrix.md` -> `literature-review` -> downstream research decisions

Do not skip directly from search results to strong research claims.

## Main Artifacts

- `reading_queue.md` — papers or sources selected for triage or reading.
- `paper_cards/` — structured reading notes for individual papers.
- `literature_matrix.md` — cross-paper comparison table.
- `baseline_candidates.md` — candidate baselines, controls, benchmarks, and expected reviewer comparisons.
- `citation_intent_map.md` — maps citation candidates to the claims or paper sections they may support.

## Rules

- Every deeply used paper should have a paper card.
- Every strong novelty, baseline, dataset, or method-positioning claim should trace to paper cards or saved source artifacts.
- Every citation candidate should have a citation intent before it is used in writing.
- If a source is only discovered but not read, mark it as `discovered`, not `read`.
- If a source is only skimmed, mark it as `skimmed`, not `deeply_read`.