# Phase 4 Contract: Writing / Manuscript Drafting

Phase 4 turns the evidence package into a manuscript through collaborative, section-by-section drafting.

## Input

- Stable Phase 3 evidence artifacts in `docs/agent/` and `outputs/`.
- Relevant source artifacts in `sources/`.
- Manuscript-specific rules in `paper/AGENTS.md`.
- Sample prior-paper style material in `paper/style/`.

## Actions

1. Read `paper/AGENTS.md` before drafting or revising manuscript prose in `paper/`.
2. Before literature-dependent prose, check `sources/paper_cards/`, `sources/literature_matrix.md`, and `sources/citation_intent_map.md`; do not cite lookup-only sources in polished prose, and mark unsupported citation needs as `needs_citation`. Record the durable source artifact and location, what the citation supports, verification, and scope/limitations in `paper/agent/citation_support.md`.
3. Before claim-heavy prose, check `docs/agent/claim_ledger.md`, `docs/agent/result_to_claim_map.md`, `docs/agent/evidence_review.md`, and `docs/agent/red_team_issue_ledger.md`. Record `Evidence References`, `Verification`, canonical `Support Status`, `Scope And Limitations`, and any `Required Change` in `paper/agent/claim_support.md`.
4. Do not write around unresolved red-team issues; resolve them, caveat or narrow the claim, or mark the issue as accepted risk.
5. Do not draft polished manuscript claims from claims marked `unsupported`, `contradicted`, `out_of_scope`, or `needs_manual_check`.
6. Use claims marked `preliminary`, `partially_supported`, or `needs_citation` only with conservative wording, explicit caveats, or TODO markers.
7. Draft incrementally: one section, subsection, or paragraph group at a time rather than the entire paper at once.
8. Use `literature-review` for introduction, motivation, or related-work synthesis; `results-scaffold` for result tables/placeholders/layouts; `scientific-writing` for evidence-bound prose; `citation-management` for citation hygiene; and `venue-templates` for venue-specific requirements. For manuscript figures or tables, record durable evidence sources, claim IDs when applicable, verification, and scope/limitations in `paper/agent/figure_support.md`, then use `docs/agent/figure_review.md` for post-aggregation safety review.
9. Use `prior-style-adapter` when adapting to established project style; if `paper/style/prior_paper_style.md` is missing, derive it from `paper/style/*.pdf` before adapting.
10. Use `claim-auditor` after drafting or style adaptation to ensure claims remain proportional to evidence.
11. Update `docs/current_status.md` after each meaningful manuscript step with the active section, touched evidence, claim-status concerns, and next writing action.

## Relevant Skills

Use the smallest relevant set:

- `scientific-writing`
- `claim-auditor`
- `citation-management`
- `literature-review` when literature-backed framing is needed
- `prior-style-adapter` when style adaptation is needed
- `venue-templates` when venue constraints apply
- `results-scaffold` when result structure must be prepared before prose

## Outputs

Expected artifacts may include:

- `paper/*.tex`
- `paper/references.bib`
- `paper/figures/`
- `paper/tables/`
- `paper/agent/claim_support.md`
- `paper/agent/section_notes.md`
- `paper/agent/citation_support.md`
- `paper/agent/figure_support.md`

## Exit condition

Phase 4 is complete only when:

- the manuscript has been drafted collaboratively in small units;
- important claims trace back to literature, experiment artifacts, result tables, or approved project context;
- literature-dependent manuscript sections are grounded in paper cards, literature matrix entries, or verified source artifacts;
- citation candidates have citation intent recorded before final use;
- style adaptation has not changed technical meaning or overstated claims;
- touched citations and references are stable enough for the current draft stage;
- manuscript claims do not use unsupported, contradicted, out-of-scope, or manually unchecked claims as polished assertions;
- preliminary, partially supported, or citation-needed claims are written conservatively or marked with TODO/caveat language;
- claim support status remains aligned with `docs/agent/claim_ledger.md`;
- manuscript support records preserve durable evidence references, claim IDs where applicable, verification, and scope/limitations; claim records use canonical support statuses while citation and figure records keep workflow-specific statuses separate;
- manuscript sections do not ignore unresolved red-team issues relevant to their claims;
- accepted red-team risks are visible as caveats, limitations, or conservative wording where needed;
- `docs/current_status.md` reflects the manuscript state and next review or revision step.

Do not write the paper as one monolithic pass. Keep drafting incremental, evidence-bound, and reviewable.
