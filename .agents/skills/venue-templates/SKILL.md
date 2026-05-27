---
name: venue-templates
description: Use for venue-specific LaTeX templates, formatting requirements, submission constraints, page limits, section rules, bibliography style, poster formats, grant formats, and camera-ready checks. This skill handles formatting and venue compliance, not scientific claim support, writing style adaptation, source discovery, citation verification, result interpretation, or figure generation.
---

# Venue Templates

## Overview

Venue Templates is the formatting and submission-constraint layer of the research workflow.

Use this skill when preparing a manuscript, poster, report, grant, or camera-ready artifact for a specific publication venue, conference, journal, funder, workshop, or template.

This skill helps answer:

```text
What format does this venue require?
Which LaTeX template or structure should be used?
What are the page, abstract, figure, table, reference, appendix, and supplement constraints?
What formatting checks are needed before submission?
```

This skill should not decide scientific claims, invent content, generate figures by default, or verify whether evidence supports manuscript statements.

---

## Core Responsibility

This skill owns:

- venue-specific LaTeX templates;
- conference/journal/grant/poster format constraints;
- page limits;
- abstract limits;
- section requirements;
- bibliography style requirements;
- figure/table placement constraints;
- supplement and appendix rules;
- anonymization and double-blind formatting rules;
- camera-ready formatting checks;
- generic template customization;
- format validation helpers;
- submission-readiness formatting checklists.

This skill does not own:

- scientific writing content;
- author style adaptation;
- claim support;
- reference metadata verification;
- literature discovery;
- result interpretation;
- experiment design;
- technical diagram generation;
- general image generation.

---

## Relationship to Other Skills

Use the smallest relevant skill combination.

| Need | Use |
|---|---|
| Draft or revise manuscript prose | `scientific-writing` |
| Adapt prose to the author’s prior-paper style | `prior-style-adapter` |
| Find sources, papers, datasets, or baselines | `research-lookup` |
| Synthesize related work or literature context | `literature-review` |
| Verify references, BibTeX, DOI/arXiv metadata, or hallucinated references | `citation-management` |
| Check whether claims are supported by evidence | `claim-auditor` |
| Prepare result table scaffolds | `results-scaffold` |
| Critique research logic or experiment decisiveness | `scientific-critical-thinking` |
| Simulate reviewer critique | `peer-review` |
| Create technical diagrams or scientific schematics | `scientific-schematics` |
| Generate general non-technical images | `generate-image` |

Recommended submission workflow:

```text
scientific-writing
    → claim-auditor
    → citation-management
    → venue-templates
    → peer-review
```

For style-sensitive manuscripts:

```text
scientific-writing
    → prior-style-adapter
    → claim-auditor
    → venue-templates
```

For visual-heavy manuscripts:

```text
results-scaffold / scientific-schematics
    → venue-templates
```

---

## When to Use This Skill

Use this skill when:

- targeting a specific journal;
- targeting a specific conference;
- preparing a workshop paper;
- preparing a poster;
- preparing a grant proposal;
- adapting LaTeX to a venue template;
- checking page limits;
- checking abstract limits;
- checking anonymization rules;
- checking supplement/appendix rules;
- preparing camera-ready formatting;
- validating figure/table sizing against format;
- creating a generic manuscript/report template;
- comparing venue requirements;
- deciding which local template asset to use.

---

## Do Not Use This Skill For

Do not use this skill to:

- invent manuscript content;
- revise scientific arguments;
- make claims stronger;
- decide whether results support claims;
- generate final citations;
- verify DOI or BibTeX metadata;
- find papers;
- write related work;
- generate figures by default;
- create diagrams unless routed to `scientific-schematics`;
- generate general images unless routed to `generate-image`;
- replace official venue instructions.

Venue compliance should not override evidence integrity.

---

## Official Requirement Verification

Venue requirements can change.

Local templates and reference files are useful starting points, but they may become stale.

Before final submission, always verify current requirements from the official source:

- official conference website;
- official journal author instructions;
- official LaTeX/Word template;
- official submission system;
- official call for papers;
- official camera-ready instructions;
- official funder solicitation.

If current official requirements are unavailable, say so and mark:

```text
TODO: verify current venue requirements from official source.
```

Do not claim final compliance based only on old local references.

---

## Venue Types

Choose the relevant venue type before applying guidance.

---

### 1. AI/ML/CV Conferences

Examples:

- NeurIPS;
- ICML;
- ICLR;
- CVPR;
- ICCV;
- ECCV;
- WACV;
- ACL/EMNLP/NAACL when NLP-relevant;
- AAAI/IJCAI.

Check:

- paper length;
- review format;
- anonymization;
- supplementary material;
- checklist requirements;
- ethics/reproducibility statements;
- appendix policy;
- references excluded/included in page limit;
- camera-ready changes.

Use references such as:

- `references/ml_conference_style.md`;
- `references/cs_conference_style.md`;
- `references/conferences_formatting.md`.

---

### 2. Journals

Examples:

- IEEE journals;
- ACM journals;
- Elsevier journals;
- Springer journals;
- Nature portfolio;
- Science;
- PLOS;
- Cell Press;
- domain-specific journals.

Check:

- article type;
- word limits;
- abstract structure;
- figure/table limits;
- reference style;
- graphical abstract requirements;
- highlights;
- data/code availability statements;
- ethics/competing interest statements;
- supplementary material format.

Use references such as:

- `references/journals_formatting.md`;
- `references/nature_science_style.md`;
- `references/cell_press_style.md`.

Domain-specific journal references, such as medical journal styles, should be used only when relevant.

---

### 3. Posters

Use for:

- conference posters;
- research showcases;
- lab presentations;
- internal/external project posters.

Check:

- poster size;
- orientation;
- section structure;
- font size;
- figure resolution;
- QR code/link policy;
- institutional branding;
- author/affiliation formatting;
- readability from distance.

Use:

- `references/posters_guidelines.md`;
- poster assets under `assets/posters/`.

---

### 4. Grants

Use for:

- NSF;
- NIH;
- DOE;
- DARPA;
- other funder proposals;
- internal funding proposals.

Check:

- solicitation;
- page limits;
- required sections;
- biosketch rules;
- budget justification rules;
- data management plan;
- broader impacts;
- intellectual merit;
- facilities/resources;
- review criteria.

Use:

- `references/grants_requirements.md`;
- grant assets under `assets/grants/`.

Do not apply grant format rules to manuscripts unless explicitly requested.

---

## Formatting Workflow

Use this workflow for venue formatting tasks.

### Step 1: Identify Target Venue

Determine:

- venue name;
- year/cycle;
- article type;
- submission stage;
- review or camera-ready;
- anonymized or non-anonymized;
- LaTeX/Word/poster/grant format.

If the venue is unknown, use generic formatting and mark venue-specific checks as TODO.

---

### Step 2: Locate Template and Local References

Use local assets and references as starting points:

- `assets/journals/`;
- `assets/posters/`;
- `assets/grants/`;
- `assets/examples/`;
- relevant files in `references/`;
- helper scripts in `scripts/`.

Do not assume local files are current.

---

### Step 3: Verify Current Official Requirements

For final or submission-facing work, verify:

- official template;
- page limit;
- abstract length;
- reference policy;
- appendix/supplement policy;
- double-blind/anonymization;
- required declarations;
- figure/table rules;
- PDF compliance rules.

If online verification is not possible, mark TODOs.

---

### Step 4: Apply Format Constraints

Apply:

- document class;
- package constraints;
- margins;
- font size;
- section headings;
- abstract structure;
- bibliography style;
- author block rules;
- line numbering if needed;
- anonymization;
- figure/table placement rules.

Avoid unnecessary template modifications.

---

### Step 5: Run Approximate Checks

Use helper scripts when useful.

Examples:

```text
scripts/query_template.py
scripts/customize_template.py
scripts/validate_format.py
```

Treat script output as approximate.

A local script cannot guarantee final compliance with a submission system.

---

### Step 6: Produce Formatting Report

Summarize:

- venue;
- template used;
- requirements checked;
- unresolved TODOs;
- changes made;
- remaining risks;
- official verification status.

---

## Visual and Figure Policy

Do not generate figures by default.

Venue Templates may identify required or useful visual artifacts, but creation should be routed.

Use:

```text
scientific-schematics
```

for:

- method diagrams;
- architecture figures;
- workflows;
- pipelines;
- scientific schematics;
- flowcharts.

Use:

```text
generate-image
```

for:

- general illustrations;
- non-technical visual assets;
- concept art;
- general-purpose images.

Use:

```text
results-scaffold
```

for:

- result tables;
- ablation tables;
- robustness tables;
- result placeholders.

Venue Templates may check figure sizes, placement, resolution, caption style, and numbering after the artifact exists.

---

## Citation and Bibliography Policy

Venue Templates may identify citation style requirements, such as:

- numeric;
- author-year;
- IEEE;
- ACM;
- APA-like;
- Vancouver;
- BibTeX style file;
- bibliography included/excluded from page limit.

But reference integrity belongs to `citation-management`.

Use `citation-management` for:

- BibTeX cleanup;
- DOI/arXiv verification;
- citation-key hygiene;
- hallucinated references;
- duplicate references;
- missing metadata.

Use `claim-auditor` when the question is whether a citation supports a claim.

---

## Writing and Style Policy

Venue Templates may identify structural or format requirements, such as:

- required sections;
- abstract headings;
- contribution statement placement;
- impact statement;
- ethics statement;
- data availability statement;
- checklist;
- limitations section.

But prose drafting belongs to `scientific-writing`.

Author style belongs to `prior-style-adapter`.

Do not rewrite content only to fit venue style if doing so changes technical meaning or claim strength.

---

## Result Table Policy

Venue Templates may check:

- table width;
- font size;
- caption placement;
- table numbering;
- whether tables fit page/column layout;
- supplement placement.

But table content and placeholders belong to `results-scaffold`.

Do not invent results to satisfy a table layout.

---

## Common Venue Checks

Depending on the venue, check:

- page limit;
- word limit;
- abstract limit;
- title length;
- author format;
- anonymization;
- acknowledgments hidden for review;
- supplementary material allowed;
- appendix policy;
- reference page policy;
- line numbers;
- font size;
- margins;
- column format;
- figure/table placement;
- caption style;
- bibliography style;
- required statements;
- checklist requirements;
- ethics statement;
- reproducibility statement;
- data/code availability statement;
- conflict-of-interest statement;
- funding statement;
- author contribution statement;
- graphical abstract/highlights, if relevant.

---

## Helper Scripts

This skill may include helper scripts:

- `scripts/query_template.py`;
- `scripts/customize_template.py`;
- `scripts/validate_format.py`.

Use helper scripts to:

- find available local templates;
- generate a customized starting point;
- run approximate checks;
- summarize formatting gaps.

Important:

```text
Helper scripts are not authoritative.
```

They cannot replace official venue instructions or submission-system validation.

If a script result conflicts with official venue instructions, follow the official instructions.

---

## Assets and References

This skill may include:

```text
assets/examples/
assets/grants/
assets/journals/
assets/posters/
references/
scripts/
```

Use local assets as starting points.

Do not assume asset examples are current, complete, or compliant for the current submission cycle.

When adapting templates, preserve licensing and attribution requirements.

Do not share or expose font files.

---

## Output Formats

Choose the smallest useful output.

---

### Venue Requirement Summary

```md
## Venue Requirement Summary

### Venue

[name, year/cycle, submission type]

### Official Source Status

- [verified / needs verification / unavailable]

### Key Requirements

| Requirement | Value | Source / Status |
|---|---|---|
| Page limit | [value] | [source/status] |
| Abstract limit | [value] | [source/status] |
| Format | [value] | [source/status] |
| Bibliography style | [value] | [source/status] |
| Supplement policy | [value] | [source/status] |

### Required Handoffs

- [scientific-writing / citation-management / results-scaffold / scientific-schematics]
```

---

### Template Selection Output

```md
## Template Selection

### Target Venue

[venue]

### Selected Local Template

[path]

### Why This Template

[reason]

### Required Manual Verification

- [official template]
- [page limits]
- [submission rules]

### Next Step

[action]
```

---

### Formatting Compliance Report

```md
## Formatting Compliance Report

### Files Checked

- [file]

### Checks Performed

| Check | Status | Notes |
|---|---|---|
| Page limit | [pass/fail/TODO] | [notes] |
| Abstract length | [pass/fail/TODO] | [notes] |
| Anonymization | [pass/fail/TODO] | [notes] |
| Bibliography style | [pass/fail/TODO] | [notes] |
| Figure/table constraints | [pass/fail/TODO] | [notes] |

### Remaining Risks

- [risk]

### Required Official Verification

- [item]
```

---

### Template Patch Summary

```md
## Template Patch Summary

### Files Changed

- [file]

### Changes Made

- [change]

### Not Changed

- [reason]

### Remaining TODOs

- [TODO]
```

---

## Important Rules

- Verify current official venue requirements before final submission.
- Do not treat local references as authoritative if they may be stale.
- Do not generate figures by default.
- Do not invent manuscript content to satisfy a format.
- Do not invent citations or references.
- Do not change scientific meaning to fit a template.
- Do not remove caveats, limitations, or required evidence markers.
- Do not make unsupported claims sound venue-ready.
- Do not treat helper-script checks as final compliance.
- Do not expose or share font files.
- Preserve licenses, template notices, and attribution where required.

---

## Good Outputs

Good outputs include:

- venue requirement summaries;
- template recommendations;
- LaTeX template patch plans;
- formatting compliance reports;
- page/abstract/figure/table constraint checks;
- camera-ready TODO lists;
- clear handoffs to writing, citation, result, and visual skills.

Bad outputs include:

- unsupported claims about final compliance;
- outdated venue instructions presented as current;
- generated figures not requested;
- prose rewriting that changes science;
- invented references;
- fake result values;
- removing important TODOs to make the paper look complete.

---

## Final Checklist

Before completing a venue-template task:

1. [ ] Target venue and submission stage are identified.
2. [ ] Local template/reference source is identified.
3. [ ] Current official requirements are verified or marked TODO.
4. [ ] Page/word/abstract limits are checked or marked TODO.
5. [ ] Bibliography style requirements are checked or routed to `citation-management`.
6. [ ] Appendix/supplement policy is checked or marked TODO.
7. [ ] Anonymization/camera-ready status is checked when relevant.
8. [ ] Figure/table constraints are checked when relevant.
9. [ ] Visual creation needs are routed to `scientific-schematics` or `generate-image`.
10. [ ] Result table content needs are routed to `results-scaffold`.
11. [ ] Prose needs are routed to `scientific-writing` or `prior-style-adapter`.
12. [ ] Claim support needs are routed to `claim-auditor`.
13. [ ] Helper scripts are treated as approximate.
14. [ ] Remaining risks and TODOs are reported.

---

## Final Reminder

Venue Templates makes the work fit the venue.

It does not make the science true, the claims supported, the citations real, or the figures complete.
