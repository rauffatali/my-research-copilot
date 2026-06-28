# Phase 4 Contract: Writing / Manuscript Drafting

Phase 4 turns the evidence package into a manuscript through collaborative, section-by-section drafting.

## Input

- Stable Phase 3 evidence artifacts in `docs/agent/` and `outputs/`.
- Relevant source artifacts in `sources/`.
- Manuscript-specific rules in `paper/AGENTS.md`.
- Sample prior-paper style material in `paper/style/`.

## Actions

1. Read `paper/AGENTS.md` before drafting or revising manuscript prose in `paper/`.
2. Before writing literature-dependent manuscript text, check `sources/paper_cards/`, `sources/literature_matrix.md`, and `sources/citation_intent_map.md`.
3. Use `sources/citation_intent_map.md` to ensure each citation has a role and supports the intended claim or context.
4. Do not cite a source in polished manuscript prose only because it appeared in a lookup result.
5. If a needed citation does not have a paper card or verified source artifact, mark the claim as `needs_citation` rather than inventing support.
6. Before drafting claim-heavy prose, check `docs/agent/claim_ledger.md` and `docs/agent/result_to_claim_map.md`.
7. Before drafting strong abstract, introduction, results, or conclusion claims, check `docs/agent/evidence_review.md` and `docs/agent/red_team_issue_ledger.md`.
8. Do not write around unresolved red-team issues; either resolve them, caveat the claim, narrow the wording, or mark the issue as accepted risk.
9. Do not draft polished manuscript claims from claims marked `unsupported`, `contradicted`, `out_of_scope`, or `needs_manual_check`.
10. Claims marked `preliminary`, `partially_supported`, or `needs_citation` may be used only with conservative wording, explicit caveats, or TODO markers.
11. Draft incrementally: one section, subsection, or paragraph group at a time rather than the entire paper at once.
12. Use `literature-review` when introduction, motivation, or related-work context must be synthesized before prose is written.
13. Use `results-scaffold` when result tables, placeholders, comparison structures, or evidence layouts are needed before drafting.
14. Use `scientific-writing` to draft manuscript content from the available evidence.
15. Use `citation-management` when touched sections need citation hygiene, metadata verification, or bibliography cleanup.
16. Use `prior-style-adapter` in one of two modes:
    * if `paper/style/prior_paper_style.md` exists, use style-adaptation mode;
    * if it does not exist, check `paper/style/*.pdf`, generate `paper/style/prior_paper_style.md`, then continue with style-adaptation mode.
17. Use `claim-auditor` after drafting or style adaptation to ensure claims remain proportional to evidence.
18. Use `venue-templates` when venue-specific structure, formatting, limits, or submission requirements are relevant.
19. Update `docs/current_status.md` after each meaningful manuscript step with the active section, touched evidence, claim-status concerns, and next writing action.

## Required skills

- `scientific-writing`
- `claim-auditor`
- `citation-management`
- `literature-review` when literature-backed framing is needed
- `prior-style-adapter`
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
- manuscript sections do not ignore unresolved red-team issues relevant to their claims;
- accepted red-team risks are visible as caveats, limitations, or conservative wording where needed;
- `docs/current_status.md` reflects the manuscript state and next review or revision step.

Do not write the paper as one monolithic pass. Keep drafting incremental, evidence-bound, and reviewable.