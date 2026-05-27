# Phase Ownership / Do-Not-Write Matrix

This matrix defines the default file ownership for the workflow skeleton.
Use it to decide which phase may create or modify a file, and when a task should stop.

## Ownership matrix

| Phase | Owns | May touch | Must not touch | Stop / block condition |
|---|---|---|---|---|
| Phase 1 | Research direction, novelty framing, hypothesis shaping | `docs/agent/` phase-1 artifacts, `sources/` evidence notes | `src/`, `tests/`, `runs/`, `outputs/`, `paper/` draft text | Stop if the idea lacks a baseline, metric, failure mode, or validation path |
| Phase 2 | Implementation, experiment setup, controlled execution | `src/`, `tests/`, `scripts/`, `runs/`, `outputs/` | `paper/` prose, `paper/agent/` review artifacts, Phase 1 direction unless a revision is explicitly requested | Block if the approved plan, frozen direction, or required inputs are missing |
| Phase 3 | Result consolidation, evidence labeling, claim support status | `docs/agent/` result artifacts, `outputs/`, read-only access to `runs/` | `src/` implementation logic, `paper/` prose, Phase 1 frozen direction except to cite it | Block if the evidence package is incomplete, unstable, or not traceable to the run artifacts |
| Phase 4 | Manuscript drafting, section writing, citation shaping | `paper/`, `paper/agent/`, cited evidence artifacts, read-only access to `docs/agent/` and `outputs/` | `src/` implementation logic, `runs/` experiment state, unsupported claim expansion | Block if the supporting evidence, citations, or claim ledger is missing |
| Phase 5 | Review, critique, revision planning, response drafting | `paper/agent/`, read-only access to `paper/`, `docs/agent/`, `outputs/`, `sources/` | `src/` implementation, `runs/` regeneration unless a fix is explicitly approved | Block if the manuscript draft, evidence package, or review target is missing |

## Shared rules

- Active phases may read earlier artifacts, but should not silently rewrite them.
- Later phases may request upstream work, but should not overwrite upstream ownership.
- If a task touches two phases, do the earliest required phase first.
- If the needed upstream artifact does not exist, mark the task as `blocked`.
- If a task asks for a file outside the owning phase, stop and route it to the correct phase first.

## Practical examples

- Phase 1 can describe a proposed change, but should not edit implementation files.
- Phase 2 can implement the approved plan, but should not draft the paper.
- Phase 3 can label claims, but should not invent new experiment evidence.
- Phase 4 can write claims, but only from supported evidence.
- Phase 5 can recommend revisions, but should not silently apply them to the manuscript.
