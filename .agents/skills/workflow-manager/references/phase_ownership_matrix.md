# Phase Ownership / Do-Not-Write Matrix

This matrix defines the default file ownership for the workflow skeleton.
Use it to decide which phase may create or modify a file, and when a task should stop.

## Ownership matrix

Phase ownership describes ordinary phase-level write scope. Role permissions still apply independently.
`independent_reviewer` is read-only regardless of phase. The protected main manuscript may be changed
only through the separately human-authorized `integration_agent` path defined in
`.agents/guidance/manuscript-writing.md`; Phase 4 ownership of `paper/draft/` does not itself grant
main-manuscript write permission.

| Phase | Owns | May touch | Must not touch | Stop / block condition |
|---|---|---|---|---|
| Phase 1 | Research debate, evidence-backed brainstorming, novelty framing, hypothesis shaping | `docs/agent/` phase-1 artifacts, `sources/` evidence notes | `src/`, `tests/`, `runs/`, `outputs/`, `paper/` draft text | Stop if the idea lacks evidence review, user clarification, baseline, metric, failure mode, or validation path |
| Phase 2 | Implementation, experiment setup, controlled execution | `src/`, `tests/`, `scripts/`, `runs/`, `outputs/` | `paper/` prose, `paper/agent/` review artifacts, Phase 1 direction unless a revision is explicitly requested | Block if the approved plan, frozen direction, or required inputs are missing |
| Phase 3 | Result consolidation, evidence labeling, claim support status | `docs/agent/` result artifacts, `outputs/`, read-only access to `runs/` | `src/` implementation logic, `paper/` prose, Phase 1 frozen direction except to cite it | Block if the evidence package is incomplete, unstable, or not traceable to the run artifacts |
| Phase 4 | Manuscript writing-slice drafting, embedded review, citation shaping | `paper/draft/`, `paper/agent/` manuscript-support artifacts, cited evidence artifacts, read-only access to the integrated manuscript, `docs/agent/`, `outputs/`, and `sources/` | Protected main manuscript as ordinary scratch space, `src/` implementation logic, `runs/` experiment state, unsupported claim expansion | Block if the supporting evidence, citations, or claim ledger is missing |
| Phase 5 | Formal broader manuscript/coherent-unit review, critique, revision planning, response drafting | `paper/agent/` review and revision artifacts through writable roles; read-only access to `paper/`, `docs/agent/`, `outputs/`, and `sources/` | Silent revision of manuscript prose, protected main manuscript, `src/` implementation, `runs/` regeneration unless a fix is explicitly approved | Block if the broader review target, evidence package, or review context is missing |

## Shared rules

- Active phases may read earlier artifacts, but should not silently rewrite them.
- Later phases may request upstream work, but should not overwrite upstream ownership.
- If a task touches two phases, do the earliest required phase first.
- If the needed upstream artifact does not exist, mark the task as `blocked`.
- If a task asks for a file outside the owning phase, stop and route it to the correct phase first.

## Practical examples

- Phase 1 can describe a proposed change, but should not edit implementation files or freeze the direction before the user approves the evidence-backed proposal.
- Phase 2 can implement the approved plan, but should not draft the paper.
- Phase 3 can label claims, but should not invent new experiment evidence.
- Phase 4 can prepare provisional writing slices from evidence-bound briefs; it does not integrate into the protected manuscript.
- Phase 5 can recommend revisions, but should not silently apply them to the manuscript.
