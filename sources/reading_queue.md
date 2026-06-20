# Reading Queue

## Purpose

This file tracks papers and external sources that may need reading.

A source in this queue is not automatically evidence.
It becomes stronger evidence only after it is read and converted into a paper card or another structured source artifact.

## Status Values

Use:

- `discovered`
- `queued`
- `skimmed`
- `deeply_read`
- `paper_card_done`
- `deferred`
- `rejected`
- `superseded`

## Queue

| Priority | Source ID | Title | Year | Source type | Why it matters | Intended use | Status | Paper card |
|---:|---|---|---:|---|---|---|---|---|
| 1 | SRC-001 | | | paper / dataset / benchmark / repo / survey / blog / docs | | closest prior work / baseline / dataset / method / citation / limitation | discovered | |

## Intended Use Values

Use one or more:

- closest_prior_work
- baseline
- benchmark
- dataset
- method_reference
- motivation
- related_work
- limitation
- failure_mode
- evaluation_protocol
- citation_candidate
- reviewer_risk
- technical_verification

## Reading Rules

- Do not mark a source as `deeply_read` unless the method, evidence, limitations, and relevance to the project were inspected.
- Do not create manuscript claims from sources with status `discovered` only.
- If a source is important for novelty, baseline, or reviewer risk, promote it to a paper card.
- If a source is low relevance, mark it `rejected` or `deferred` with a reason.

## Next Step

[State the next source to read or triage.]