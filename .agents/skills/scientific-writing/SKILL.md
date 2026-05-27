---
name: scientific-writing
description: Use for evidence-first scientific manuscript drafting and revision, including abstracts, introductions, related work, methods, experiments, results, discussion, conclusion, limitations, rebuttals, and LaTeX-ready prose. Coordinates with research-lookup, literature-review, citation-management, claim-auditor, results-scaffold, venue-templates, prior-style-adapter, scientific-schematics, and peer-review. Do not use to invent citations, metrics, results, novelty, or unsupported claims.
---

# Scientific Writing

## Overview

Scientific writing is the evidence-first manuscript prose and revision layer of the research workflow.

Use this skill to turn validated research content into clear, conservative, publication-ready scientific text.

This skill may draft, revise, restructure, or polish:

- abstracts;
- introductions;
- background sections;
- related work or literature review sections;
- methods;
- experiment setup;
- results;
- discussion;
- limitations;
- conclusions;
- rebuttals;
- response letters;
- reports;
- LaTeX manuscript sections.

The goal is not to make claims sound stronger. The goal is to make claims clear, precise, well-supported, and proportional to the available evidence.

---

## Core Principle: Evidence-First Writing

Do not write manuscript claims first and look for support later.

Before drafting or revising a section, identify what evidence, citations, results, project context, or prior review artifacts support the section.

If support is missing, mark the sentence or paragraph with a clear TODO instead of inventing content.

Use TODO labels such as:

```text
TODO: needs citation
TODO: needs literature-review support
TODO: needs result
TODO: needs ablation
TODO: needs baseline
TODO: needs claim audit
TODO: needs citation-management verification
TODO: needs venue-template check
TODO: needs figure artifact
```

Never invent:

- citations;
- references;
- metrics;
- baselines;
- ablations;
- datasets;
- results;
- figures;
- novelty;
- conclusions;
- reviewer responses;
- venue requirements.

---

## Relationship to Other Skills

Scientific writing is an orchestrating writing skill. It should know when another skill is required before or after writing.

| Need | Use |
|---|---|
| Find candidate sources, papers, datasets, or benchmarks | `research-lookup` |
| Organize sources into themes, gaps, introduction support, or related work | `literature-review` |
| Verify references, BibTeX, DOI/arXiv metadata, or hallucinated references | `citation-management` |
| Check whether claims are supported by evidence | `claim-auditor` |
| Critique research logic, novelty, experiment design, or interpretation | `scientific-critical-thinking` |
| Simulate external reviewer critique | `peer-review` |
| Create result tables or result-section scaffolding without inventing metrics | `results-scaffold` |
| Apply venue-specific LaTeX format or submission constraints | `venue-templates` |
| Adapt prose to established project style | `prior-style-adapter` |
| Create technical diagrams, architectures, workflows, or scientific figures | `scientific-schematics` |
| Generate non-technical/general visual assets | `generate-image` |

Recommended manuscript workflow:

```text
research-lookup
    → literature-review
    → citation-management
    → scientific-writing
    → claim-auditor
    → peer-review
```

For result-heavy writing:

```text
runs/ + outputs/
    → results-scaffold
    → scientific-writing
    → claim-auditor
```

For final submission:

```text
scientific-writing
    → claim-auditor
    → citation-management
    → venue-templates
    → peer-review
```

---

## When to Use This Skill

Use this skill when:

- drafting a manuscript section from verified notes or artifacts;
- revising existing paper text for clarity and scientific tone;
- restructuring paragraphs;
- improving logical flow;
- making claims more conservative;
- turning result tables into careful prose;
- turning literature-review outputs into introduction or related work prose;
- writing method descriptions from code/config/project notes;
- writing limitations proportional to evidence;
- aligning abstract, contribution, results, and conclusion;
- preparing rebuttal or response text from verified evidence;
- converting notes into LaTeX-ready scientific prose.

Use another skill first when evidence is missing.

---

## Do Not Use This Skill For

Do not use this skill as the primary tool for:

- finding sources;
- verifying references;
- auditing whether citations support claims;
- designing experiments;
- generating final metrics;
- creating figures;
- deciding venue format;
- simulating reviewer critique;
- making unsupported claims sound polished.

Writing should not outrun evidence.

---

## Section-Specific Dependencies

Before writing, identify the section type and required support.

| Section | Required support |
|---|---|
| Abstract | project contribution, result evidence, claim-auditor check |
| Introduction | literature-review, research-lookup if needed, citation-management, claim-auditor |
| Background / Motivation | literature-review, verified citations, claim-auditor |
| Related Work / Literature Review | literature-review, research-lookup, citation-management |
| Method | code/config/project docs, implementation evidence, claim-auditor for strong method claims |
| Experiments | experiment plan, configs, dataset/split details, results-scaffold if results incomplete |
| Results | runs/outputs, result tables, results-scaffold, claim-auditor |
| Discussion | result evidence, limitations, scientific-critical-thinking, claim-auditor |
| Limitations | evidence, failure analysis, project scope, claim-auditor |
| Conclusion | supported contribution and results only, claim-auditor |
| Rebuttal | reviewer comments, verified evidence, claim-auditor |
| Venue formatting | venue-templates |
| Style adaptation | prior-style-adapter |
| Technical figures | scientific-schematics |
| General images | generate-image |

---

## Literature-Dependent Writing

Use this when writing or revising sections that depend on prior work.

This especially applies to:

- introduction;
- background;
- motivation;
- related work;
- literature review;
- problem framing;
- gap statements;
- contribution positioning;
- comparison to prior methods;
- limitations grounded in prior literature.

Rule:

```text
Use literature-review first, or confirm that a recent literature-review artifact exists.
```

Do not invent related-work claims or citations during writing.

If a claim needs literature support and no source is present, mark:

```text
TODO: needs citation
```

or route to:

```text
research-lookup → literature-review → citation-management
```

For a standard paper structure, the second major section is often Related Work or Literature Review. Before drafting that section, use `literature-review` to organize sources into themes, method families, gaps, datasets, baselines, and citation-backed comparisons.

---

## Citation-Safe Writing

Scientific writing may place citation placeholders, but it should not invent references.

Do:

- use existing verified citation keys when available;
- preserve citation keys already used correctly;
- mark missing citations clearly;
- keep citation-backed claims close to their evidence;
- use conservative language when citation support is weak.

Do not:

- fabricate citation keys;
- fabricate BibTeX entries;
- invent paper titles, authors, years, venues, or DOIs;
- cite a source without knowing what it supports;
- use one citation to support a broader claim than the source allows;
- describe preprints as peer-reviewed unless verified.

Use `citation-management` for:

- BibTeX cleanup;
- DOI/arXiv verification;
- hallucinated-reference detection;
- duplicate reference cleanup;
- citation-key hygiene.

Use `claim-auditor` for:

- checking whether the cited source supports the manuscript sentence.

---

## Result-Dependent Writing

Use this when writing results, experiments, or discussion sections.

Do not invent final values, rankings, improvements, or statistical claims.

When final results are not established, use `results-scaffold` to create:

- table layouts;
- comparison structures;
- ablation placeholders;
- robustness subset layouts;
- result-section skeletons;
- TODOs for missing metrics;
- conservative prose placeholders.

Acceptable placeholder wording:

```text
TODO: insert final metric after verified run artifact is available.
```

```text
The final comparison should report [metric] for [baseline] and [method] under the same evaluation protocol.
```

Do not write:

```text
Our method significantly outperforms all baselines.
```

unless the evidence exists and has passed claim audit.

---

## Claim-Safe Writing

Before finalizing, strong claims must pass `claim-auditor`.

High-risk words include:

- novel;
- first;
- state-of-the-art;
- robust;
- generalizes;
- significantly;
- outperforms;
- solves;
- eliminates;
- comprehensive;
- real-world ready;
- efficient;
- reliable;
- fully automated.

Use safer wording when evidence is limited.

| Strong wording | Safer wording |
|---|---|
| proves | provides evidence that |
| demonstrates | suggests / indicates, if evidence is limited |
| solves | addresses |
| eliminates | reduces / may reduce |
| generalizes | was evaluated on / showed performance on |
| robust | showed robustness under the evaluated conditions |
| state-of-the-art | competitive / strong / improved over evaluated baselines |
| significantly improves | improves, unless statistical significance is tested |
| first | avoid unless closest-prior-work evidence is strong |
| outperforms all baselines | outperforms the evaluated baselines |
| universally applicable | applicable in the evaluated setting |

Writing should make unsupported claims visible, not hide them.

---

## Venue and Format Handoff

Use `venue-templates` when preparing for:

- journal submission;
- conference submission;
- workshop paper;
- poster;
- grant proposal;
- camera-ready formatting;
- LaTeX template compliance;
- page limits;
- section constraints;
- figure/table placement rules;
- bibliography style requirements.

Scientific writing may draft content, but venue-specific formatting belongs to `venue-templates`.

Do not assume:

- section order;
- abstract length;
- page limits;
- citation style;
- required declarations;
- appendix rules;
- figure/table constraints.

If target venue is known, request or use `venue-templates`.

---

## Prior Style Handoff

Use `prior-style-adapter` when the user asks to match the project’s established writing style or when the text should align with:

```text
paper/style/prior_paper_style.md
```

Use prior style for:

- tone;
- sentence rhythm;
- paragraph flow;
- conservative claim style;
- transition patterns;
- section-level pacing.

Do not use prior style to:

- copy content;
- copy unique phrasing;
- change technical meaning;
- strengthen claims beyond evidence;
- weaken claims so much that meaning is lost.

Recommended flow:

```text
scientific-writing
    → prior-style-adapter
    → claim-auditor
```

or:

```text
prior-style-adapter
    → claim-auditor
```

when only style adaptation is requested.

---

## Visual Artifact Handoff

Do not generate visual artifacts by default.

Use `scientific-schematics` for:

- neural network architecture diagrams;
- system diagrams;
- method workflows;
- experimental pipelines;
- flowcharts;
- data-processing diagrams;
- scientific schematics;
- technical figures.

Use `generate-image` for:

- general-purpose images;
- conceptual artwork;
- illustrations that are not technical diagrams;
- visual assets not requiring schematic precision.

Use `results-scaffold` for:

- result tables;
- ablation tables;
- robustness tables;
- result-section table placeholders.

Do not describe a figure as completed unless the visual artifact exists or is explicitly requested.

If a manuscript would benefit from a figure, write:

```text
TODO: consider scientific-schematics for method pipeline figure.
```

---

## Writing Modes

Choose the smallest writing mode that fits the task.

---

### 1. Section Drafting

Use when creating a new section from evidence.

Before drafting:

1. identify section type;
2. list available evidence;
3. list missing evidence;
4. define safe claim scope;
5. draft only supported prose.

Output:

- section draft;
- citation TODOs;
- evidence TODOs;
- claim-auditor handoff notes.

---

### 2. Section Revision

Use when improving existing text.

Focus on:

- clarity;
- flow;
- concision;
- scientific tone;
- claim strength;
- citation placement;
- paragraph logic;
- consistency with evidence.

Do not introduce new claims unless evidence is available.

---

### 3. Conservative Claim Revision

Use when text overclaims.

Rewrite to:

- narrow scope;
- specify evaluated setting;
- remove unsupported certainty;
- separate hypothesis from result;
- separate motivation from evidence;
- mark missing support.

---

### 4. Introduction / Motivation Writing

Use after literature context exists.

A good introduction should:

1. introduce problem context;
2. explain why it matters;
3. summarize relevant prior work at high level;
4. identify a literature-supported gap or limitation;
5. state project objective;
6. state contribution conservatively.

Dependencies:

- `research-lookup`;
- `literature-review`;
- `citation-management`;
- `claim-auditor`.

Do not invent broad field claims.

---

### 5. Related Work Writing

Use after literature-review has organized sources.

A good related work section should:

- synthesize, not list;
- group papers by theme or method family;
- compare closest prior work;
- position the current project;
- use verified citations;
- avoid exaggerated novelty claims.

Dependencies:

- `literature-review`;
- `citation-management`;
- `claim-auditor`.

---

### 6. Method Writing

Use when method details are available from project artifacts.

A good method section should:

- define task;
- describe inputs and outputs;
- specify model/pipeline;
- state training objective;
- describe preprocessing and postprocessing;
- mention implementation details needed for reproducibility;
- avoid claiming performance before results.

Dependencies:

- code/config/project docs;
- `claim-auditor` for strong method claims.

---

### 7. Experiment Writing

Use when experiment design is known.

A good experiment section should describe:

- datasets;
- splits;
- baselines;
- metrics;
- implementation details;
- training protocol;
- evaluation protocol;
- ablations;
- hardware/compute if relevant.

Dependencies:

- experiment configs;
- result artifacts;
- `results-scaffold`;
- `claim-auditor`.

---

### 8. Results Writing

Use when verified run artifacts or result tables exist.

A good results section should:

- state what was measured;
- compare against baselines;
- report metrics accurately;
- mention evaluated setting;
- avoid unsupported generalization;
- identify meaningful patterns;
- connect figures/tables to claims.

Dependencies:

- `runs/`;
- `outputs/`;
- result tables;
- `results-scaffold`;
- `claim-auditor`.

---

### 9. Discussion and Limitations Writing

Use when interpreting results.

A good discussion should:

- explain what results suggest;
- separate evidence from speculation;
- discuss limitations specifically;
- identify failure modes;
- avoid introducing unsupported claims;
- connect future work to evidence.

Dependencies:

- result evidence;
- failure analysis;
- `scientific-critical-thinking`;
- `claim-auditor`.

---

### 10. Abstract and Conclusion Writing

Use only when main contribution and evidence are clear.

Abstract should include:

- problem;
- approach;
- key evidence;
- main contribution;
- cautious conclusion.

Conclusion should:

- summarize supported contribution;
- avoid new claims;
- state limitations or future work carefully;
- align with abstract and results.

Dependencies:

- completed or stable manuscript context;
- `claim-auditor`.

---

### 11. Rebuttal and Response Writing

Use when responding to reviewers.

Before writing:

- identify reviewer concern;
- locate evidence;
- decide whether to agree, clarify, add experiment, or revise claim;
- avoid defensive tone.

Dependencies:

- reviewer comments;
- result evidence;
- `claim-auditor`;
- `peer-review`;
- `scientific-critical-thinking`.

---

## Manuscript Outline Guidance

When asked to outline a paper, create an outline that reflects evidence and venue constraints.

A generic AI/CV paper outline may include:

1. Abstract
2. Introduction
3. Related Work
4. Method
5. Experiments
6. Results
7. Discussion / Limitations
8. Conclusion
9. References
10. Appendix / Supplementary Material

But do not force this structure when the venue or paper type differs.

For venue-specific structure, use `venue-templates`.

For literature-heavy outlines, use `literature-review`.

For result-heavy outlines, use `results-scaffold`.

For domain-specific applied AI papers, include domain framing and domain-validity evidence where appropriate.

---

## Paragraph Quality Rules

A strong scientific paragraph usually has:

1. topic sentence;
2. evidence or explanation;
3. connection to the paper’s argument;
4. cautious transition.

Avoid paragraphs that:

- list facts without synthesis;
- contain unsupported claims;
- mix methods, results, and interpretation without clarity;
- overuse citations without explaining relevance;
- end with vague importance statements;
- imply more evidence than exists.

---

## LaTeX Writing Rules

When writing LaTeX-ready prose:

- preserve citation commands;
- do not invent citation keys;
- avoid unescaped special characters when writing raw LaTeX;
- keep labels and refs stable;
- do not rename figures/tables unless requested;
- write equations only when needed;
- use consistent terminology;
- keep TODOs visible.

If exact LaTeX formatting or venue template compliance matters, use `venue-templates`.

---

## Output Formats

Choose the smallest useful output.

---

### Draft Section Output

```md
## Draft Section

[Draft text]

## Evidence Used

- [evidence/source]

## TODOs

- TODO: needs citation
- TODO: needs result
- TODO: needs claim audit

## Recommended Next Step

[claim-auditor / citation-management / literature-review / results-scaffold / venue-templates]
```

---

### Revision Output

```md
## Revised Text

[Revised text]

## Key Changes

- [change]

## Remaining Risks

- [risk]

## Next Step

[recommended skill/action]
```

---

### Section Outline Output

```md
## Proposed Section Outline

### 1. [Section/Subsection]

Purpose:
Evidence needed:
Likely citations:
Risks/TODOs:

### 2. [Section/Subsection]

Purpose:
Evidence needed:
Likely citations:
Risks/TODOs:
```

---

### Claim-Safe Rewrite Output

```md
| Original | Issue | Safer rewrite |
|---|---|---|
| [text] | [overclaim/missing citation/missing result] | [rewrite] |
```

---

## Important Rules

- Do not invent evidence.
- Do not invent citations.
- Do not invent metrics or results.
- Do not invent baselines.
- Do not invent novelty.
- Do not make planned work sound completed.
- Do not make hypotheses sound like findings.
- Do not make preprints sound peer-reviewed unless verified.
- Do not let style adaptation change technical meaning.
- Do not let formatting concerns override evidence integrity.
- Do not hide uncertainty.
- Do not finalize claim-heavy prose without `claim-auditor`.

---

## Good Outputs

Good outputs include:

- clear manuscript prose;
- conservative claim wording;
- visible TODOs for missing support;
- citation-aware paragraphs;
- LaTeX-ready sections;
- structured outlines;
- result prose tied to actual artifacts;
- limitation sections that are honest and specific;
- handoffs to the correct skill when support is missing.

Bad outputs include:

- polished unsupported claims;
- invented citations;
- invented results;
- vague “future work” filler;
- related work without literature synthesis;
- abstract claims not supported by the paper;
- conclusion claims not shown in results;
- figures described as existing when they do not.

---

## Final Checklist

Before completing a scientific-writing task:

1. [ ] Section type is identified.
2. [ ] Evidence sources are identified.
3. [ ] Literature-dependent text has literature-review support.
4. [ ] Citation-dependent text uses verified or TODO citations.
5. [ ] Result-dependent text uses actual runs/outputs or results-scaffold placeholders.
6. [ ] Claims are proportional to evidence.
7. [ ] Missing evidence is marked with TODOs.
8. [ ] No citations, metrics, baselines, or results are invented.
9. [ ] Venue-specific requirements are handed to `venue-templates`.
10. [ ] Style adaptation needs are handed to `prior-style-adapter`.
11. [ ] Technical visual needs are handed to `scientific-schematics`.
12. [ ] General image needs are handed to `generate-image`.
13. [ ] Claim-heavy text is routed to `claim-auditor`.
14. [ ] Reference hygiene issues are routed to `citation-management`.
15. [ ] Reviewer-readiness issues are routed to `peer-review`.

---

## Final Reminder

Scientific writing should make the research clearer, not stronger than the evidence.

A well-written paper is not the one with the boldest claims. It is the one where every claim has a clear reason to be believed.
