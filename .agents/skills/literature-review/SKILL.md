---
name: literature-review
description: Use for AI/ML/CV literature synthesis, closest-prior-work analysis, research-gap mapping, baseline/dataset/benchmark comparison, and citation-backed support for introduction, background, motivation, related work, or literature review sections. Best used after research-lookup has produced source artifacts or when selected papers must be synthesized. For source discovery use research-lookup. For polished prose use scientific-writing. For BibTeX/reference hygiene use citation-management.
---

# Literature Review

## Overview

Literature review is the synthesis layer of the research workflow.

Use this skill to turn source artifacts, selected papers, prior-work notes, and citation candidates into structured research understanding.

The goal is not merely to summarize papers one by one. The goal is to identify themes, method families, baselines, datasets, benchmarks, evaluation protocols, limitations, contradictions, research gaps, and implications for the current project.

For this repository, `research-lookup` should usually perform source discovery first. This skill should then synthesize the found sources into usable research context.

This skill may support manuscript sections such as:

- introduction;
- background;
- motivation;
- related work;
- literature review;
- research gap framing;
- contribution positioning.

It should not replace `scientific-writing` for polished prose or `claim-auditor` for final claim support checks.

---

## Preferred Source Artifacts

Prefer synthesizing from:

- saved lookup artifacts under `sources/`;
- `sources/paper_cards/`;
- `sources/literature_matrix.md`;
- `sources/baseline_candidates.md`;
- `sources/citation_intent_map.md`.

When paper cards are missing for sources that drive novelty, baseline, or claim decisions, recommend creating paper cards before strong synthesis.

---

## When to Use This Skill

Use this skill when:

- synthesizing saved source artifacts from `sources/`;
- reviewing a set of papers selected by the user or another agent;
- identifying closest prior work;
- comparing method families;
- mapping research themes or trends;
- identifying research gaps or unresolved limitations;
- preparing citation-backed context for introduction, background, or motivation;
- preparing related work or literature review structure;
- identifying standard baselines, datasets, benchmarks, and evaluation protocols;
- checking whether a proposed contribution is already covered by prior work;
- preparing literature context for peer review, claim auditing, experiment planning, or paper writing.

Do not use this skill as the primary tool for:

- discovering sources from the web; use `research-lookup`;
- formatting BibTeX, DOI metadata, or references; use `citation-management`;
- drafting polished manuscript prose; use `scientific-writing`;
- checking final manuscript claims against repo evidence; use `claim-auditor`;
- adversarial methodology critique; use `scientific-critical-thinking`;
- reviewer-style critique; use `peer-review`;
- creating visual artifacts; use `scientific-schematics` or `generate-image`.

---

## Relationship to Research Gates

This skill supports the following gates in `docs/research_gates.md`:

- Research Direction Gate
- Research Change Gate
- Experiment Decision Gate
- Evaluation and Result Interpretation Gate
- Claim Support Gate
- Paper Writing Gate
- Red-Team Review Gate

Use this skill to provide literature context before accepting a research direction, strengthening a novelty claim, choosing baselines, designing evaluation, or writing literature-dependent manuscript sections.

A literature review does not by itself prove novelty or claim support. It provides structured evidence and context that should be checked by the relevant gate or downstream skill.

---

## Relationship to Other Skills

Use the smallest relevant skill combination.

| Need | Use |
|---|---|
| Find external papers, datasets, benchmarks, or citation candidates | `research-lookup` |
| Synthesize selected sources into themes, gaps, and comparisons | `literature-review` |
| Clean BibTeX, DOI, citation style, and reference metadata | `citation-management` |
| Draft or revise polished paper text | `scientific-writing` |
| Audit whether manuscript claims are supported | `claim-auditor` |
| Pressure-test methodology, novelty, or experiment design | `scientific-critical-thinking` |
| Simulate external reviewer judgment | `peer-review` |
| Create taxonomy diagrams, timelines, or visual maps | `scientific-schematics` |

Recommended paper-writing flow:

```text
research-lookup
    → literature-review
    → scientific-writing
    → claim-auditor
```

For peer-review context:

```text
research-lookup
    → literature-review
    → scientific-critical-thinking
    → peer-review
```

---

## Review Modes

Choose the smallest review mode that fits the task.

Do not perform a full systematic review when a quick source synthesis or closest-prior-work comparison is enough.

### 1. Quick Source Synthesis

Use when the agent has a saved lookup artifact, a small source list, or a limited set of papers.

Output:

- main themes;
- strongest or most relevant sources;
- how sources relate to the current project;
- missing evidence;
- next lookup, reading, or synthesis step.

Good for:

- orienting the project quickly;
- deciding whether deeper review is needed;
- summarizing a newly generated `research-lookup` artifact.

### 2. Closest Prior Work Review

Use when assessing novelty, contribution positioning, or overlap with existing work.

Output:

- closest papers;
- what each paper does;
- overlap with the current project;
- differences from the current project;
- whether the proposed novelty is weakened, supported, or unresolved;
- evidence needed before making a novelty or contribution claim.

Critical questions:

1. What prior work is closest?
2. Is the difference technical, empirical, dataset-related, evaluation-related, or application-specific?
3. Is the difference meaningful?
4. Is the contribution new to the field or only new to the project?
5. What claim wording is safe?

### 3. Baseline and Benchmark Review

Use when planning experiments, reviewing comparison strength, or preparing evaluation context.

Output:

- common baselines;
- strong simple baselines;
- datasets and benchmarks;
- metrics and evaluation protocols;
- expected ablations;
- missing comparisons reviewers may expect;
- which comparisons are essential versus optional.

Good for:

- Experiment Decision Gate;
- Research Change Gate;
- peer-review preparation;
- deciding whether current evaluation is convincing.

### 4. Dataset and Evaluation Literature Review

Use when the project depends on dataset choice, annotation protocol, benchmark design, or evaluation validity.

Output:

- dataset sources;
- label schema and annotation formats;
- split conventions;
- known leakage or bias risks;
- metric conventions;
- evaluation limitations;
- domain-shift or held-out-domain considerations.

For CV tasks, consider:

- image, video, sequence, or multimodal input;
- classification, detection, segmentation, tracking, or retrieval outputs;
- bounding-box, mask, keypoint, or caption annotation formats;
- object size, rare classes, annotation noise, and domain shift;
- train/validation/test split policy.

### 5. Research Gap Map

Use when developing hypotheses, contribution targets, or future work.

Output:

- known directions;
- saturated areas;
- unresolved limitations;
- weakly supported assumptions;
- open questions;
- possible project-fit gaps;
- risks that the gap is too broad, too incremental, or already addressed.

A research gap must be grounded in sources. Do not invent gaps only because they sound plausible.

### 6. Introduction and Motivation Support

Use when preparing or revising the introduction, background, motivation, or problem-framing sections of a manuscript.

Output:

- key background claims that need citations;
- high-level motivation sources;
- evidence for problem importance;
- prior-work context needed before the contribution statement;
- gap or limitation statements supported by literature;
- conservative citation-backed wording;
- claims that should be sent to `claim-auditor` before final paper use.

Use this mode to support manuscript framing, not to write polished prose directly.

For final drafting or style revision, use `scientific-writing`.

### 7. Related Work or Literature Review Synthesis

Use when preparing the related work, literature review, or background section of a paper.

Output:

- thematic organization;
- method-family grouping;
- citation clusters;
- contrastive positioning;
- prior-work comparison table if useful;
- safe transition from prior work to project contribution;
- citation-backed statements;
- citations needing verification.

For a standard paper structure, the second major section is often Related Work or Literature Review. Before drafting that section, use this skill to organize sources into themes, method families, gaps, datasets, baselines, and citation-backed comparisons.

For final prose, use `scientific-writing`.

### 8. Full Systematic or Scoping Review

Use only when explicitly requested.

Output may include:

- review question;
- database/search strategy;
- inclusion and exclusion criteria;
- screening flow;
- extracted evidence table;
- quality assessment;
- synthesis method;
- limitations of the review.

Do not impose full systematic-review machinery on ordinary related-work or project-context tasks.

---

## Inputs

Use the smallest relevant inputs.

Possible inputs include:

- saved `sources/*.md` or `sources/*.json` artifacts from `research-lookup`;
- selected papers provided by the user;
- paper PDFs or notes;
- existing `docs/research_context.md`;
- `docs/current_status.md`;
- `docs/PROJECT_PLAN.md`;
- manuscript sections under `paper/`;
- citation candidate lists;
- experiment plans needing baseline or evaluation context.

When using saved lookup artifacts, preserve the path in the output so later agents can trace the synthesis.

---

## Core Workflow

Use this workflow for substantial literature review tasks.

### 1. Define the review purpose

State what the review is for:

- research direction;
- novelty check;
- baseline selection;
- dataset or benchmark understanding;
- evaluation planning;
- introduction support;
- related work synthesis;
- claim support;
- peer-review context.

Avoid reviewing literature without a clear purpose.

### 2. Identify the source base

State what sources were used:

- saved lookup artifacts;
- user-provided papers;
- existing project documents;
- manuscript sections;
- citation files.

If source discovery is insufficient, use or request `research-lookup`.

Do not pretend the source base is complete when it is narrow.

### 3. Classify the literature

Organize sources by meaningful dimensions.

Possible dimensions:

- method family;
- dataset or benchmark;
- evaluation metric;
- task type;
- contribution type;
- limitation addressed;
- architecture family;
- training or adaptation strategy;
- domain or application setting;
- chronological development;
- evidence strength.

Do not merely list papers chronologically unless chronology is the point.

### 4. Compare sources

For each important source or group, identify:

- what problem it addresses;
- what method or evidence it uses;
- what dataset or benchmark it uses;
- what metric or evaluation protocol it reports;
- what limitation it acknowledges;
- how it relates to the current project;
- whether it is a baseline, closest prior work, background source, or citation candidate.

### 5. Identify gaps and limitations

Identify gaps only when supported by the source base.

Label each gap as one of:

- well-supported gap;
- possible gap;
- project-local gap;
- needs more lookup;
- not supported.

Avoid strong gap claims when literature coverage is incomplete.

### 6. Extract project implications

Translate the literature into project-useful conclusions:

- what baseline should be considered;
- what dataset or benchmark matters;
- what metric should be reported;
- what evaluation slice may be important;
- what claim should be weakened;
- what citation is needed;
- what method idea is already covered;
- what experiment would clarify the gap.

### 7. Prepare downstream handoff

End with a useful next step:

- use `research-lookup` for missing sources;
- use `scientific-critical-thinking` to critique the research gap;
- use `citation-management` to clean citations;
- use `scientific-writing` to draft related work or introduction text;
- use `claim-auditor` to verify final manuscript claims;
- use `peer-review` for reviewer-style critique.

---

## Synthesis Dimensions for AI/ML/CV

When relevant, synthesize along these dimensions.

### Task and Problem Formulation

- What is the input?
- What is the output?
- What assumptions are made?
- What problem setting is studied?
- What deployment or research constraint matters?

### Methods

- architecture family;
- loss or objective;
- augmentation or preprocessing;
- training strategy;
- adaptation strategy;
- postprocessing;
- foundation-model usage;
- classical versus deep learning baseline.

### Data and Benchmarks

- dataset source;
- label schema;
- split policy;
- annotation protocol;
- known biases;
- leakage risks;
- dataset size and diversity;
- held-out-domain or cross-domain settings.

### Evaluation

- metrics;
- thresholds;
- postprocessing;
- test-time augmentation;
- baselines;
- ablations;
- statistical reporting;
- qualitative failure analysis;
- slice-based analysis.

### Claims and Evidence

- novelty claims;
- performance claims;
- robustness claims;
- generalization claims;
- efficiency claims;
- real-world readiness claims;
- limitations.

### Research Gaps

- unsupported assumptions;
- untested domains;
- missing baselines;
- missing ablations;
- weak evaluation;
- unstudied failure modes;
- dataset limitations;
- annotation issues.

---

## Output Formats

Choose the output format that matches the task.

---

### Quick Synthesis Output

Use for small source sets.

```md
## Review Purpose

## Source Base

## Main Themes

## Most Relevant Sources

## Project Implications

## Missing Evidence

## Next Step
```

---

### Closest Prior Work Output

Use for novelty or contribution positioning.

```md
## Review Purpose

## Source Base

## Closest Prior Work

| Source | What it does | Overlap | Difference | Implication |
|---|---|---|---|---|

## Novelty Risk

## Safe Contribution Framing

## Missing Sources or Checks

## Next Step
```

---

### Baseline and Benchmark Output

Use for experiment planning.

```md
## Review Purpose

## Source Base

## Baseline Candidates

| Baseline | Source | Why relevant | Essential or optional | Notes |
|---|---|---|---|---|

## Datasets and Benchmarks

## Metrics and Protocols

## Missing Comparisons

## Experiment Implications

## Next Step
```

---

### Research Gap Map Output

Use for hypothesis or contribution development.

```md
## Review Purpose

## Source Base

## Literature Themes

## Known Limitations

## Candidate Gaps

| Gap | Support | Project fit | Risk | Evidence needed |
|---|---|---|---|---|

## Recommended Research Direction

## Next Step
```

---

### Introduction / Motivation Support Output

Use for introduction, background, or motivation sections.

```md
## Review Purpose

## Source Base

## Background Claims Needing Citations

| Claim | Candidate sources | Strength | Notes |
|---|---|---|---|

## Problem Importance Evidence

## Prior-Work Context Before Contribution

## Supported Gap or Limitation Statements

## Conservative Wording Suggestions

## Claims Needing Claim Audit

## Next Step
```

---

### Related Work Synthesis Output

Use before drafting or revising related work.

```md
## Review Purpose

## Source Base

## Thematic Structure

## Source Clusters

| Theme | Sources | Shared idea | Difference from project |
|---|---|---|---|

## Contrastive Positioning

## Citation-Backed Statements

## Claims Needing Verification

## Suggested Section Outline

## Next Step
```

---

## Citation Handling

This skill may identify citation needs and candidate sources, but it should not be the final citation hygiene tool.

Do:

- identify which claim a source supports;
- distinguish strong support from weak support;
- flag missing citations;
- preserve source paths or metadata;
- mark uncertain citation support as `needs citation` or `needs verification`.

Do not:

- invent citations;
- fabricate DOI, venue, author, or year metadata;
- treat a source as supporting a claim without checking relevance;
- perform final BibTeX cleanup when `citation-management` is available.

Use `citation-management` for:

- BibTeX generation;
- DOI validation;
- reference formatting;
- duplicate reference cleanup;
- citation style consistency.

---

## Visual Artifacts

Do not generate schematics by default.

If the review would benefit from a taxonomy, timeline, benchmark map, method comparison diagram, citation map, or research-gap map, recommend using `scientific-schematics` separately.

Visual artifacts are optional and should be created only when they improve understanding or communication.

---

## Quality and Scope Controls

### Avoid Source Dumping

Do not provide a long list of paper summaries unless the user explicitly asks.

Prefer synthesis over enumeration.

### Avoid Unsupported Gap Claims

Do not claim a gap exists unless the reviewed sources support it.

If coverage is incomplete, label the gap as `possible` or `needs more lookup`.

### Avoid Overclaiming Novelty

Literature review can identify novelty risk, but it should not declare field-level novelty unless evidence is strong.

Use conservative language:

- appears underexplored in the reviewed sources;
- not observed in the current source set;
- requires broader lookup;
- may indicate a gap;
- needs confirmation against closest prior work.

### Avoid Mixing Writing and Evidence

This skill can suggest citation-backed wording, but polished prose belongs to `scientific-writing`.

### Preserve Traceability

When possible, cite or reference:

- source artifact path;
- paper title;
- DOI;
- arXiv ID;
- URL;
- saved lookup file;
- manuscript section.

---

## Optional Utilities and References

This skill may include helper files such as:

- `assets/review_template.md`
- `references/citation_styles.md`
- `references/database_strategies.md`
- `scripts/generate_pdf.py`

Legacy utilities, if present under `scripts/legacy/`, should not be used by default. They are retained only for historical reference or manual migration.

Use helper files only when relevant.

Do not let helper scripts override the current workflow:

- source discovery should usually use `research-lookup`;
- citation verification should usually use `citation-management`;
- polished manuscript prose should usually use `scientific-writing`;
- visual artifacts should use `scientific-schematics`;
- PDF generation is optional and should be used only when a shareable or archival review artifact is requested.

If a helper script is outdated, in `scripts/legacy/`, or mismatched to the current task, do not use it by default.

---

## Final Checklist

Before finalizing a literature review task, check:

1. [ ] The review purpose is clear.
2. [ ] The source base is identified.
3. [ ] The review mode is appropriate for the task.
4. [ ] Sources are synthesized, not merely listed.
5. [ ] Closest prior work is identified when novelty matters.
6. [ ] Baselines, datasets, benchmarks, or metrics are extracted when experiments matter.
7. [ ] Gaps are labeled according to evidence strength.
8. [ ] Introduction or related-work support is citation-aware when manuscript framing matters.
9. [ ] Citation needs are flagged without inventing metadata.
10. [ ] Claims are kept proportional to evidence.
11. [ ] Missing evidence or missing lookup is stated.
12. [ ] The next downstream skill or action is recommended.

---

## Remember

A good literature review helps the project answer:

- What has already been done?
- What is closest to our work?
- What baselines would a reviewer expect?
- What datasets, benchmarks, and metrics define the area?
- What gaps are actually supported by the literature?
- What claims can be safely made?
- What still needs citation, lookup, or auditing?
- How should the introduction or related work be framed?

The output should make later research decisions, experiments, paper writing, and claim auditing more reliable.
