# Phase 4 Contract: Writing / Manuscript Drafting

Phase 4 transforms stable evidence into provisional manuscript writing slices, reviews them, and determines scientific readiness while protecting integrated manuscript sources behind a separate human-authorized integration gate.

## Canonical manuscript workflow

Follow `.agents/guidance/manuscript-writing.md` for the detailed writing-slice, staging, review, acceptance, and integration contract. This phase contract summarizes its routing points and does not replace the evidence, source, claim-status, citation, workflow-state, or agent-role policies.

## Evidence-state discipline

Inspect the applicable `evidence_state` for every implementation, result, citation, or placeholder dependency and carry it into the scientific writing brief and support package. Pending or placeholder dependencies may guide explicit TODO, planned, or otherwise permitted provisional wording, but must not become polished final assertions. Recheck mutable evidence states before scientific readiness and keep the separate canonical `support_status` for claim strength.

```text
result_pending   -> TODO or planned language, not a final result assertion
placeholder_only -> scaffold structure, not a scientific finding
```

## Input

- Stable Phase 3 evidence artifacts in `docs/agent/` and `outputs/`.
- Relevant source artifacts in `sources/`.
- Manuscript-specific rules in `paper/AGENTS.md`.
- Sample prior-paper style material in `paper/style/`.

## Actions

1. Read `paper/AGENTS.md` and `.agents/guidance/manuscript-writing.md` before manuscript work.
2. Identify or confirm the user-authorized writing slice; do not assume that a whole section is the working unit.
3. Classify semantic/scientific risk. Risk, not word count, line count, diff size, or a “small” label controls staging; ambiguous classification fails closed.
4. Inspect the relevant Phase 3 evidence, claim ledger/maps, source artifacts, citation support, manuscript context, project style material, and applicable evidence states for each dependency.
5. Construct and resolve the bounded scientific writing brief before semantic prose is produced, carrying evidence states and separate support status where a claim already exists.
6. Before candidate generation for a substantive semantic writing slice, read `docs/agent/agent_role_profile.md`, resolve the positive-integer `candidate_writers_required` and the corresponding `candidate_writer` slots or assignments, verify `candidate_independence_required` and `candidate_cross_visibility_before_comparison`, and record the configured count and actual slots in the writing brief or support record. Stage every candidate in `paper/draft/`. Do not silently use fewer than the configured count; a temporary lower count requires explicit `human_researcher` authorization for this slice and must record the configured count, effective count, authority, and scope without changing `docs/agent/agent_role_profile.md`. Initial candidates obey the configured independence and cross-visibility rules, remain provisional, and are compared by `research_lead`; one selected `candidate_writer` remains the final prose owner.
7. Preserve evidence, claim, citation, terminology, and LaTeX boundaries; do not write unsupported claims or silently change scientific direction.
8. Use an assigned `independent_reviewer` for read-only challenge when required, and have `research_lead` adjudicate findings. If none is assigned, the lead performs explicit adversarial self-checking without inventing an assignment.
9. Review sufficient surrounding manuscript context, recheck applicable evidence states, perform claim/evidence/citation checks, and keep candidate and resolved prose provisional.
10. Distinguish `research_lead` scientific readiness from `human_researcher` integration authorization. Do not automatically copy or merge draft prose into the protected main manuscript.
11. Update `docs/current_status.md` when manuscript state, active artifacts, blockers, or next action changes.

Trivial maintenance may bypass the full candidate-writing loop only for the closed, nonsemantic class defined in the canonical workflow. It does not bypass protected integration requirements.

Embedded writing-slice review remains inside `phase_4_active`; it does not require or cause a transition to Phase 5 for every slice. If a broader manuscript or coherent-unit review target is ready, Phase 5 is entered through the state-machine prerequisites.

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

Phase 4 outputs are provisional and should primarily use:

- `paper/draft/` for semantic/scientific-risk writing slices;
- `paper/agent/` for section notes, claim support, citation support, figure support, and other manuscript-support artifacts; and
- relevant read-only evidence and source artifacts.

The protected main manuscript target is not an ordinary Phase 4 output. If an integration is authorized, describe it as a separate gated action performed by an `integration_agent`, not as normal draft production.

## Exit condition

Phase 4 is complete or frozen for a writing slice only when:

- the writing-slice draft and its support package are stable and reviewable;
- important claims trace back to literature, experiment artifacts, result tables, or approved project context;
- literature-dependent content is grounded in paper cards, literature matrix entries, or verified source artifacts;
- citation intent, claim support, verification, scope, limitations, and required changes are recorded where relevant;
- style or other transformations preserve scientific meaning and receive appropriate validation;
- unsupported, contradicted, out-of-scope, and manually unchecked claims are not presented as polished assertions;
- unresolved red-team issues are resolved, caveated, narrowed, or recorded as accepted risk;
- surrounding context has been checked for coherence; and
- `docs/current_status.md` reflects the manuscript state and next action.

`phase_4_frozen` means that the writing slice and support decisions are stable and reviewable. `phase_4_frozen` does not imply integration. Integration remains separately gated by current evidence, rollback/diff readiness, explicit human authorization, and the `integration_agent` role.
