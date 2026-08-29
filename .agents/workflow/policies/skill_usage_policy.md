# Skill usage policy

Use skills as task tools, not as general background instructions.

Select the smallest relevant skill or skill combination.

Examples:

- Use `literature-review` for structured paper analysis and research mapping.
- Use `research-lookup` for targeted external research or citation discovery.
- Use `citation-management` for BibTeX, references, and citation hygiene.
- Use `claim-auditor` for checking whether manuscript or report claims are supported.
- Use `scientific-critical-thinking` for hypothesis critique, novelty risk, and methodological weakness analysis.
- Use `theoretical-lens` when a failure mode or design choice may have a load-bearing mathematical framing worth adopting; use sparingly, not by default.
- Use `peer-review` for reviewer-style criticism.
- Use `results-scaffold` for preparing result tables, experiment summaries, and output organization.
- Use `scientific-writing` for manuscript drafting or revision.
- Use `prior-style-adapter` only when adapting text to an established writing style.
- Use `academic-humanizer` only for optional, bounded naturalness refinement after scientific resolution and style adaptation when needed.
- Use `watermark-hygiene` only for optional read-only inspection of invisible Unicode or text-transfer artifacts; it is not a prose-rewrite stage.
- Use `venue-templates` only when targeting a specific venue or journal format.
- Use `scientific-schematics` or `generate-image` only for visual artifacts.
- Use `workflow-manager` for workflow skeleton routing, state checks, and template validation.
- Use `zotero` for direct Zotero Desktop helper operations when a local library must be queried or updated.

Do not invoke writing, venue, or image skills during code-only tasks unless explicitly requested.

## Manuscript skill routing

For manuscript work, follow `.agents/guidance/manuscript-writing.md` for writing-slice orchestration and role boundaries rather than duplicating them here.

The optional transformation chain is:

```text
scientifically resolved writing slice
    -> scientific-writing / selected candidate_writer
    -> project style or prior-style-adapter when needed
    -> academic-humanizer when useful
    -> differential claim/evidence validation
    -> citation-management when relevant
```

`academic-humanizer` is not mandatory. `watermark-hygiene` is outside the automatic writing chain and remains inspection-first. Use `peer-review` for reviewer-style critique, with formal broader Phase 5 use when appropriate.

Active role permissions override any skill's ordinary write or durable-output behavior. In particular, `independent_reviewer` remains strictly read-only and returns findings in its response instead of writing artifacts.
