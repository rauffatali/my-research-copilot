# Manuscript Writing Workflow

## Purpose

This contract governs manuscript drafting, revision, writing-slice-local review, scientific acceptance, and protected integration. It refines Phase 4 and Phase 5 without replacing the evidence, source, claim-status, citation, workflow-state, or agent-role policies. Repository evidence remains authoritative over generated prose.

## Writing unit: writing slice

The canonical manuscript unit is a `writing slice`. A writing slice may be:

- part of a sentence;
- one sentence;
- one paragraph;
- several paragraphs;
- a transition;
- a subsection;
- multiple subsections;
- a complete section;
- a table or figure narrative; or
- another clearly bounded manuscript revision.

The workflow must not assume that a whole section is always the working unit. The human selects or authorizes the boundary. A large task may be divided into smaller slices when that improves reviewability, provided that argument and evidence dependencies are preserved.

## Risk-based staging

Whether a change uses the staged writing workflow is determined by semantic or scientific risk, not by word count, line count, diff size, or whether the user calls the change small.

A one-word change is a full semantic writing slice when it can affect claim strength, hedging, certainty, scientific interpretation, argument, contribution framing, limitations, methodology meaning, result narration, numeric meaning, dataset/model/task terminology, citations or citation-supported meaning, references, LaTeX labels or cross-references, or scientific scope. A tiny semantic edit must not bypass staging.

Do not use a threshold such as “new or substantially rewritten prose” as the main trigger. Meaning and scientific consequence control classification.

## Closed trivial maintenance class

Only this narrow, closed, nonsemantic class may potentially bypass the full writing-slice production loop:

- an obvious typo;
- whitespace;
- a harmless LaTeX escape correction;
- punctuation with no semantic effect; or
- clearly mechanical formatting.

This class is conservative. If classification is ambiguous, fail closed and treat the change as a normal writing slice. Bypassing the candidate-writing loop never authorizes unrestricted mutation of a protected main manuscript target. A change that touches that target still requires the applicable human authorization and integration-role requirements.

## Draft-first workspace

Every semantic or scientific-risk writing slice must first be produced under `paper/draft/`. This directory is provisional staging space and is separate from integrated or final manuscript sources.

The staging layout may support one sentence, one paragraph, several paragraphs, a transition, a subsection, multiple subsections, a complete section, a table or figure narrative, or another bounded slice. It may use one slice per file, multiple related slices per file, or another clear slice-oriented layout. It must not require one file per section; provenance and review state must remain understandable.

## Provisional-status invariant

All candidate prose created during Phase 4 remains provisional until accepted. This includes initial candidate prose, alternative candidate prose, selected-base prose, resolved prose, style-adapted prose, and corrected prose.

Writing into `paper/draft/` does not mean that the prose has been accepted. Acceptance does not mean integration. Integration is a separate protected action.

## Role responsibilities in manuscript work

Use only the generic roles defined by `.agents/workflow/policies/agent_role_policy.md`; this section specializes those roles for manuscript work without changing their global permissions.

### `human_researcher`

The human may define or confirm the writing goal, choose the writing-slice boundary, require stronger review than the project default, and authorize a specific accepted slice for integration. The human remains the final authority for protected main-manuscript integration.

```text
accepted
!=
authorized for integration
```

### `research_lead`

For manuscript work, the lead should inspect manuscript context and claims, evidence, and source artifacts; determine the slice's scientific purpose; define evidence and citation boundaries; identify unresolved dependencies; construct the scientific and argument writing brief; determine what candidate writers may decide; adjudicate reviewer findings; compare candidates; resolve ambiguity; determine scientific readiness; issue bounded correction instructions; and review the resolved slice before acceptance.

The lead is not automatically `candidate_writer` or `integration_agent` and may not silently authorize main-manuscript integration.

### `independent_reviewer`

The role remains strictly read-only during manuscript work. When assigned or required, it may independently inspect context, challenge the lead's brief or candidate prose, identify unsupported claims, missing evidence or citations, methodological or organizational weaknesses, and likely reviewer objections, and recommend corrections in its response.

It must not edit `paper/draft/`, main manuscript files, `paper/agent/`, `docs/agent/`, `docs/current_status.md`, or any other repository file. Findings remain in its response until a writable role records accepted or adjudicated findings under the role and tool policies. Do not make this workflow dependent on a particular reviewer model.

### `candidate_writer`

Candidate writers are bounded prose executors. They receive a resolved scientific brief, produce candidate prose under `paper/draft/`, preserve evidence and citation boundaries, preserve terminology and LaTeX requirements, and avoid silently changing direction or strengthening claims. Scientific ambiguity must be flagged rather than decided by the writer. A candidate writer is not a scientific adjudicator.

### `integration_agent`

Integration is a separate invocation and action. The integration agent performs an already accepted, explicitly human-authorized protected manuscript integration. The underlying agent or harness may be the same as a previous candidate writer, but the role must be explicitly changed:

```text
same underlying agent
invocation A -> candidate_writer
invocation B -> integration_agent
```

Candidate-writing activity must never silently integrate prose.

## Candidate-writer configuration and resolution

The reusable workflow supports a positive-integer number of `candidate_writer` assignments. The required
count is project-configured through `candidate_writers_required` in `docs/agent/agent_role_profile.md`;
canonical workflow policy does not impose a fixed number.

`candidate_writers_required` must be an integer greater than or equal to 1. If it is missing, non-integer,
zero, negative, or otherwise invalid, treat writer configuration as unresolved. Do not guess a writer
count, silently use 1, silently use the template default 2, or begin substantive semantic candidate
drafting. Resolve the value through an explicit agent-role-profile correction or explicit current human
instruction. An instruction such as “Use two candidate writers for this slice” resolves the current task
only and does not rewrite the permanent agent-role profile unless the human explicitly requests that change.

Before candidate generation for a substantive semantic Phase 4 writing slice:

1. Read `docs/agent/agent_role_profile.md`.
2. Resolve `candidate_writers_required` and the corresponding project-local candidate slots or assignments.
3. Verify `candidate_independence_required` and `candidate_cross_visibility_before_comparison`.
4. Confirm that the required number of usable assignments is available; do not invent missing agents,
   models, providers, or harnesses.
5. Record the configuration in the writing brief or support record, as relevant:

   ```text
   Candidate writers required: N
   Candidate writer slots: candidate_1, candidate_2, ...
   Temporary override: none / explicitly human-authorized
   ```

If the role profile remains `template_default`, explicit current user instructions may establish
assignments; defaults alone do not establish actual agents. If fewer than `N` usable assignments are
available, do not silently continue with fewer writers. Candidate production stops at that boundary
unless `human_researcher` explicitly authorizes a temporary lower count for the current writing slice.
Record the configured count, effective count, authority, and scope of that override without changing the
permanent agent-role profile. Do not apply this rule to literature search, evidence analysis, claim auditing,
Phase 1-3 work, formal review, non-manuscript tasks, or closed trivial nonsemantic manuscript maintenance.

When `candidate_independence_required: true`, initial candidates receive the same resolved brief and
authorized evidence/context as applicable, but use separate invocations or assignments and do not
co-author, share drafts, or coordinate toward one initial answer. When
`candidate_cross_visibility_before_comparison: false`, one candidate must not inspect another candidate's
provisional draft before the first `research_lead` comparison. After comparison, the lead supplies
bounded accepted decisions or correction instructions rather than an uncontrolled collage of competing
drafts.

When `candidate_writers_required: 1`, one candidate is produced and the lead evaluates it against the
resolved brief, evidence, and surrounding context without inventing a second writer. When the configured
count is greater than one, all configured candidates are produced before lead comparison. Their independence
is governed separately by `candidate_independence_required`.

## Scientific writing brief

Before semantic prose is produced, `research_lead` should define a bounded scientific control brief. As relevant, it identifies:

- writing-slice boundary;
- purpose or argument function;
- scientific claim scope;
- evidence support;
- citation or source support;
- implementation dependencies;
- experiment or result dependencies;
- relevant evidence dependency and current `evidence_state` or `Evidence State(s)`;
- current `support_status` when a claim already exists;
- wording currently claimable from those dependencies;
- wording forbidden until a pending dependency changes;
- known uncertainties;
- terminology constraints;
- LaTeX constraints;
- required caveats;
- forbidden or unsupported claims;
- surrounding manuscript context; and
- acceptance criteria.

The brief is a control artifact, not polished prose. Use existing claim and evidence artifacts. Do not create a new universal evidence-state vocabulary or invent project-specific evidence-state labels.

## Evidence-state discipline

Use the canonical `evidence_state` vocabulary from `.agents/workflow/policies/evidence_and_claim_policy.md` to describe the lifecycle or readiness of each relevant dependency. Keep it separate from the single claim-level `support_status`, which answers how strongly the current evidence supports the exact claim wording. A claim may have multiple evidence dependencies and therefore multiple `Evidence State(s)`.

Internal evidence-state tags control drafting and review decisions; they must not automatically appear in final manuscript prose. In particular:

- `implementation_pending` must not be written as a completed method detail;
- `experiment_planned` must not become an expected outcome presented as a finding;
- `result_pending` must not become a final result claim;
- `citation_pending` must not be presented as fully source-supported;
- `placeholder_only` is never evidence.

Recheck applicable evidence states at these points:

1. when `research_lead` creates or resolves the scientific brief;
2. during claim/evidence review before writing-slice acceptance; and
3. immediately before protected integration when a dependency may have changed.

If an accepted slice was based on `evidence_ready` or `implementation_defined` and its dependency becomes stale, mutable, or otherwise no longer current, do not integrate the stale slice. Return it to `research_lead` for revision and the required re-review; do not silently preserve the earlier support verdict.

## Reviewer challenge and lead adjudication

When an independent reviewer is assigned or required, use this bounded loop:

```text
research_lead brief
-> independent_reviewer read-only challenge
-> research_lead adjudication
-> resolved writing brief
```

The writer receives the resolved brief. Do not indiscriminately pass rejected reviewer reasoning into candidate-writer context. Accepted, rejected, or deferred findings may be recorded in durable support artifacts by a writable role.

If no independent reviewer is assigned and the human has not required one, do not invent an assignment. The lead still performs explicit adversarial self-checking and notes the absence of independent review when scientifically consequential. A template-default or `UNASSIGNED` role profile does not make the scaffold unusable.

## Writer ambiguity rule

If a candidate writer encounters ambiguity requiring a scientific decision, it must not silently decide. It flags the ambiguity and returns it to `research_lead`.

If candidates interpret the same brief in materially different scientific ways, do not immediately merge them. Treat the disagreement as possible brief underspecification, return to the lead, clarify the brief, and then continue.

## Candidate comparison

When multiple candidates exist, `research_lead` compares them using the criteria relevant to the slice, including resolved-brief adherence, scientific fidelity, unsupported-claim avoidance, coverage, caveat preservation, argument structure, critical synthesis, technical precision, citation handling and key integrity, LaTeX and label/reference integrity, terminology consistency, surrounding-context coherence, academic clarity, concision, and correction burden.

```text
scientific fidelity + evidence correctness
>
surface fluency
```

Do not add a rigid numeric scoring system.

## One final prose owner

Each resolved writing slice normally has one final prose owner. When several candidates contain useful ideas, the lead identifies the reasoning and structure that should survive, and one selected `candidate_writer` produces the coherent resolved version. Do not assemble the accepted slice as a mechanical sentence-by-sentence collage by default. This protects voice, argument coherence, transitions, citation continuity, and terminology. The final prose owner may differ between slices.

## Cross-slice and surrounding-context coherence

A slice must not be accepted only in isolation. Review enough surrounding context to detect paragraph inconsistency, duplicated reasoning, terminology drift, contradictory claim strength, broken transitions, citation discontinuity, LaTeX or reference breakage, and incompatibility with the enclosing subsection or section. Scale context to the slice; whole-manuscript review is not required for every sentence.

## Style and transformation boundary

Existing project style guidance, `prior-style-adapter`, `claim-auditor`, `citation-management`, `academic-humanizer`, and `watermark-hygiene` may be used where relevant. For a scientifically resolved provisional writing slice, the optional prose-refinement path is:

```text
resolved scientific prose
        ->
project style / prior-style-adapter when needed
        ->
academic-humanizer when useful
        ->
differential claim/evidence audit
        ->
citation/reference validation when relevant
```

`academic-humanizer` is optional, not mandatory for every writing slice. `watermark-hygiene` is optional inspection-first text-transfer analysis and is not part of the automatic prose-refinement chain.

Any transformation applied after scientifically resolved prose must preserve scientific meaning and must be followed by the appropriate claim, evidence, and citation validation before acceptance.

When `prior-style-adapter`, `academic-humanizer`, or another material prose transformation changes wording, preserve both the pre-transformation and post-transformation text long enough to compare them. The subsequent claim/evidence audit must check for changes in claim strength, hedging, scope, certainty, scientific interpretation, limitations or caveats, result interpretation, citation relationship, numerical content, equations or symbols, technical terminology, LaTeX commands, and labels or references. Checking only the endpoint is insufficient when wording materially changed.

Neither `prior-style-adapter`, `academic-humanizer`, nor `watermark-hygiene` may independently decide scientific claim strength. If a transformation exposes ambiguity about interpretation, hedging, scope, caveats, or technical meaning, route it to `research_lead`. The selected `candidate_writer` remains the final prose owner and applies accepted style or naturalness refinements to the provisional resolved slice.

## Acceptance versus integration

The workflow distinguishes these conceptual states without requiring a formal enum:

```text
DRAFTED
REVIEWED
ACCEPTED / SCIENTIFICALLY READY
AUTHORIZED FOR INTEGRATION
INTEGRATED
```

`research_lead` may determine that a slice is scientifically ready, but may not convert that determination into human-authorized integration. Only `human_researcher` may authorize protected main-manuscript integration, and the authorization must apply to the relevant writing slice.

## Integration-time evidence revalidation

An accepted draft is not assumed to remain valid indefinitely. Immediately before integration, recheck the current repository state for any changeable implementation, experiment, result, citation, external-evidence, or claim-support dependency.

If evidence has materially changed:

```text
DO NOT INTEGRATE
-> return the slice to research_lead
-> revise and re-review as necessary
```

A stale accepted slice must not enter the main manuscript merely because it was accepted earlier.

## Protected manuscript integration

Resolve the protected manuscript target through this sequence before integration:

1. Read `docs/project_profile.md`.
2. Inspect `main_manuscript_path`.
3. If it is configured with a valid project-relative target, use it as the protected integration target.
4. If it is `UNASSIGNED`, missing, or invalid, do not guess a filename.
5. An explicit human instruction may establish a task-scoped target.
6. A task-scoped target does not permanently update the project profile unless the human requests it.
7. If no target is resolved, work in `paper/draft/` may proceed but protected integration cannot.

If `main_manuscript_path` is `NOT_APPLICABLE`, protected manuscript integration is not part of the current
project under normal configuration unless the human changes the configuration or authorizes a clearly
scoped exception.

The protected target is not ordinary Phase 4 writable scratch space. A configured target does not grant
write authority; the normal role and explicit human-authorization integration gate remains required.

## Rollback and diff requirement

Before protected integration, an adequate mechanism must exist to inspect and reverse the integration. Examples include normal Git tracking and history, a pre-integration snapshot with a focused diff, or another explicitly approved reversible mechanism. No one mechanism is required universally, and this workflow does not change Git policy.

If no adequate rollback or diff mechanism exists, drafting is allowed but integration is blocked. The human and project workflow may choose the mechanism.

## Phase 4 and Phase 5 boundary

Embedded Phase 4 review is writing-slice-local, pre-integration, and readiness-oriented. It remains within `phase_4_active` and does not cause a transition to Phase 5 for every slice.

Phase 5 is formal broader review of an integrated manuscript or coherent manuscript unit from a skeptical external-reviewer perspective. It does not repeat the ordinary candidate-writing production loop. If formal review requires prose revision, return to Phase 4; if it exposes evidence failure, return to Phase 3; if it invalidates the research direction, return to Phase 1.

Method, Domain, Hybrid, and Meta are optional critique lenses for formal review, not canonical agent roles and not independent authorities to write files. The `independent_reviewer` role remains governed by its strict read-only contract.

## Canonical sequence

```text
human_researcher defines or requests writing slice
        ->
research_lead reconstructs context and creates scientific brief
        ->
independent_reviewer read-only challenge, when assigned or required
        ->
research_lead adjudicates and freezes resolved writing brief
        ->
configured candidate_writer assignments create the required provisional candidates in paper/draft/
        ->
research_lead compares and reviews candidates
        ->
independent_reviewer read-only challenge, when assigned or required
        ->
research_lead adjudicates
        ->
one candidate_writer owns coherent resolved prose in paper/draft/
        ->
applicable style transformation
        ->
claim, evidence, and citation validation
        ->
final scientific review
        ->
ACCEPTED / SCIENTIFICALLY READY
        ->
revalidate changeable evidence
        ->
confirm rollback or diff mechanism
        ->
human_researcher explicitly authorizes this integration
        ->
separate invocation as integration_agent
        ->
integrate into the resolved protected main-manuscript target
        ->
focused post-integration diff, build, and validation
```

When reviewers or multiple writers are not configured, degrade safely without inventing assignments. Do not silently weaken evidence validation.
