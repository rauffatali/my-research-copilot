# Literature Review Template

**Title**: [Review / synthesis title]  
**Project**: [Project or paper name]  
**Author / Agent**: [Name or agent role]  
**Date**: [YYYY-MM-DD]  
**Review Mode**: [Quick Source Synthesis / Closest Prior Work / Baseline & Benchmark / Dataset & Evaluation / Research Gap Map / Introduction Support / Related Work Synthesis / Systematic or Scoping Review]  
**Source Base**: [Saved lookup artifact paths, selected papers, PDFs, project docs, manuscript sections]  
**Purpose**: [Why this review is being done]

---

## Scalable Rigor Rule

This template is formal by default, but not every literature task needs full systematic-review machinery.

For ordinary AI/ML/CV research synthesis, complete the **Core Review Sections** and the relevant **Mode-Specific Sections**.

For a formal systematic or scoping review, also complete the **Formal Systematic / Scoping Review Extension**.

Do not skip rigor. Scale the rigor to the decision being made.

---

# Core Review Sections

Complete these sections for every substantial literature review.

---

## 1. Review Purpose

State the specific purpose of this review.

Examples:

- support research direction selection;
- check closest prior work;
- identify baselines for experiments;
- understand datasets and benchmarks;
- support introduction or motivation;
- prepare related work structure;
- identify research gaps;
- support claim auditing or peer review.

**Review question / focus**:

> [Write the review question or synthesis focus here.]

**Intended downstream use**:

- [ ] research planning
- [ ] experiment planning
- [ ] introduction / motivation support
- [ ] related work / literature review writing
- [ ] paper claim support
- [ ] peer-review context
- [ ] rebuttal / revision support
- [ ] systematic or scoping review
- [ ] other: [describe]

**Decision this review should support**:

> [What decision, claim, section, experiment, or research direction this review will support.]

---

## 2. Source Base

List the sources used for this synthesis.

### 2.1 Source Artifacts

| Artifact | Type | Date | Notes |
|---|---|---:|---|
| `sources/...md` | research-lookup result | [date] | [topic / query] |
| `sources/...json` | metadata | [date] | [optional] |

### 2.2 Selected Papers / Sources

| Source | Year | Venue / Source | Type | Why included |
|---|---:|---|---|---|
| [Paper title] | [Year] | [Venue] | [paper/dataset/survey/benchmark/docs] | [Reason] |

### 2.3 Coverage Notes

State limitations of the source base.

Examples:

- source list is from one lookup only;
- recent papers may be missing;
- non-English sources were not reviewed;
- full text was unavailable for some papers;
- citation metadata is incomplete;
- no formal systematic search was performed;
- no citation graph expansion was performed;
- venue or peer-review status still needs verification.

---

## 3. Search / Selection Trace

Use this section to make even lightweight reviews traceable.

For a quick synthesis, this can be short. For a systematic review, use the full extension later.

| Query / Selection Source | Backend / Database | Date | Filters | Result artifact |
|---|---|---:|---|---|
| [Query or source list] | [research-lookup/OpenAlex/arXiv/etc.] | [Date] | [Filters] | [Path] |

**Inclusion logic**:

- [Why sources were considered relevant.]

**Exclusion logic**:

- [What was ignored and why.]

---

## 4. Executive Synthesis

Briefly summarize what the literature says.

**Main takeaways**:

1. [Takeaway 1]
2. [Takeaway 2]
3. [Takeaway 3]

**Most relevant sources**:

- [Source 1] — [why it matters]
- [Source 2] — [why it matters]
- [Source 3] — [why it matters]

**Implication for current project**:

> [What this literature changes or clarifies for the project.]

**Confidence level**:

- [ ] high: multiple directly relevant sources support the synthesis
- [ ] medium: relevant sources exist, but coverage is incomplete
- [ ] low: early synthesis; more lookup or full-text reading needed

---

## 5. Literature Themes

Organize sources by theme, not as isolated paper summaries.

### Theme 1: [Theme name]

**Summary**: [What this theme covers.]

**Representative sources**:

| Source | Main idea | Evidence / method | Relevance to project |
|---|---|---|---|
| [Source] | [Idea] | [Evidence] | [Relevance] |

**Consensus**: [Where sources agree.]  
**Disagreement / uncertainty**: [Where sources differ or evidence is weak.]  
**Project implication**: [How this theme affects the project.]

---

### Theme 2: [Theme name]

**Summary**: [What this theme covers.]

**Representative sources**:

| Source | Main idea | Evidence / method | Relevance to project |
|---|---|---|---|
| [Source] | [Idea] | [Evidence] | [Relevance] |

**Consensus**: [Where sources agree.]  
**Disagreement / uncertainty**: [Where sources differ or evidence is weak.]  
**Project implication**: [How this theme affects the project.]

---

## 6. Evidence Strength and Relevance

Use this table to prevent weak or irrelevant sources from being treated as strong support.

| Source | Directness to project | Evidence strength | Main limitation | Use in project |
|---|---|---|---|---|
| [Source] | [Direct / partial / background] | [Strong / moderate / weak] | [Limitation] | [Baseline / citation / context / gap / avoid] |

**Notes**:

- [Which sources are strongest?]
- [Which sources are only background?]
- [Which sources should not support strong claims?]

---

# Mode-Specific Sections

Complete only the sections relevant to the selected review mode.

---

## 7. Closest Prior Work

Use this section when novelty or contribution positioning matters.

| Source | What it does | Overlap with current project | Difference | Novelty implication |
|---|---|---|---|---|
| [Paper] | [Summary] | [Overlap] | [Difference] | [Weakens/supports/unclear] |

### Novelty Risk

Classify the novelty risk.

- [ ] low risk: closest prior work is clearly different
- [ ] medium risk: overlap exists but difference may be meaningful
- [ ] high risk: closest prior work appears very similar
- [ ] unresolved: more lookup or full-text reading needed

**Safe contribution framing**:

> [Conservative wording for how the project differs from prior work.]

**Claims to avoid for now**:

- [Unsupported novelty claim]
- [Unsupported superiority claim]

---

## 8. Baselines, Benchmarks, and Evaluation Protocols

Use this section when the literature review supports experiment planning or reviewer readiness.

### 8.1 Baseline Candidates

| Baseline | Source | Why relevant | Essential / Optional | Notes |
|---|---|---|---|---|
| [Baseline] | [Source] | [Reason] | [Essential/Optional] | [Notes] |

### 8.2 Datasets and Benchmarks

| Dataset / Benchmark | Source | Task | Labels | Split / Protocol | Notes |
|---|---|---|---|---|---|
| [Dataset] | [Source] | [Task] | [Labels] | [Protocol] | [Notes] |

### 8.3 Metrics

| Metric | Used for | Sources | Notes |
|---|---|---|---|
| [Metric] | [Task / claim] | [Sources] | [Notes] |

### 8.4 Missing Comparisons

List comparisons reviewers may expect.

- [Missing baseline or ablation]
- [Missing dataset]
- [Missing metric]
- [Missing failure analysis]

---

## 9. Dataset, Annotation, and Leakage Considerations

Use this section when the project involves AI/ML/CV datasets or evaluation.

### Dataset / Annotation Findings

- **Data source**: [What sources say]
- **Label schema**: [Classes, boxes, masks, keypoints, captions, etc.]
- **Annotation quality**: [Known noise, ambiguity, missing labels]
- **Split policy**: [Random, group, temporal, source-based, unknown]
- **Known limitations**: [Limitations reported in literature]

### Leakage / Bias Risks

| Risk | Evidence from literature | Relevance to project | Action |
|---|---|---|---|
| [Duplicate leakage] | [Source/notes] | [Impact] | [Check/action] |
| [Domain/source bias] | [Source/notes] | [Impact] | [Check/action] |
| [Annotation inconsistency] | [Source/notes] | [Impact] | [Check/action] |

---

## 10. Research Gaps and Open Problems

Identify only literature-supported gaps.

| Gap / limitation | Supporting sources | Evidence strength | Project fit | Risk |
|---|---|---|---|---|
| [Gap] | [Sources] | [well-supported / possible / weak] | [High/Medium/Low] | [Risk] |

### Gap Classification

- **Well-supported gap**: supported by multiple relevant sources.
- **Possible gap**: appears in current source base but needs more lookup.
- **Project-local gap**: gap in this project’s current implementation/evaluation, not necessarily the field.
- **Unsupported gap**: plausible but not supported by reviewed sources.

### Recommended Gap Statement

> [Conservative gap statement that can be used later with citation support.]

---

## 11. Introduction / Motivation Support

Use this section when supporting the introduction, background, or motivation.

### Background Claims Needing Citations

| Claim | Candidate sources | Support strength | Notes |
|---|---|---|---|
| [Claim] | [Sources] | [Strong/Moderate/Weak] | [Notes] |

### Problem Importance Evidence

- [Evidence about importance, prevalence, cost, impact, benchmark relevance, or research need]
- [Source]

### Prior-Work Context Before Contribution

Summarize what the introduction should establish before stating the contribution.

1. [Context point]
2. [Context point]
3. [Context point]

### Conservative Motivation Wording

> [Suggested citation-backed wording for motivation or gap framing.]

### Claims Needing Claim Audit

- [Claim that should be checked by `claim-auditor` before final paper use]

---

## 12. Related Work / Literature Review Structure

Use this section before writing the related work or literature review section.

### Suggested Thematic Structure

1. **[Theme / subsection title]**
   - Sources: [Source list]
   - Purpose: [Why this group matters]

2. **[Theme / subsection title]**
   - Sources: [Source list]
   - Purpose: [Why this group matters]

3. **[Theme / subsection title]**
   - Sources: [Source list]
   - Purpose: [Why this group matters]

### Source Clusters

| Theme | Sources | Shared idea | Difference from current project |
|---|---|---|---|
| [Theme] | [Sources] | [Shared idea] | [Difference] |

### Contrastive Positioning

Explain how the current project should be positioned against prior work.

> [Positioning statement.]

### Citation-Backed Statements

List statements that can later be used by `scientific-writing`.

- [Statement] — [candidate sources]
- [Statement] — [candidate sources]

---

# Formal Systematic / Scoping Review Extension

Complete this section only when the review mode is **Systematic or Scoping Review**, or when the user explicitly asks for formal search traceability.

This section makes the review more rigorous and auditable, but it is not required for every ordinary related-work or project-context task.

---

## 13. Protocol

**Review type**:

- [ ] systematic review
- [ ] scoping review
- [ ] mapping review
- [ ] rapid review
- [ ] narrative review with formal search traceability

**Protocol / registration**:

- [ ] OSF
- [ ] PROSPERO
- [ ] internal protocol only
- [ ] not registered
- [ ] not applicable

**Protocol link or path**: [URL/path]

**Research question**:

> [Formal review question.]

**Population / domain / task**: [If applicable]  
**Intervention / method / exposure**: [If applicable]  
**Comparison**: [If applicable]  
**Outcome / evaluation target**: [If applicable]

For AI/ML/CV reviews, define:

- task;
- input/output;
- dataset or benchmark scope;
- model/method families;
- metrics;
- application domain;
- time range.

---

## 14. Formal Search Strategy

### Databases / APIs

| Source | Used? | Notes |
|---|---:|---|
| OpenAlex | [yes/no] | [Notes] |
| arXiv | [yes/no] | [Notes] |
| Semantic Scholar | [yes/no] | [Notes] |
| Crossref | [yes/no] | [Notes] |
| IEEE Xplore | [yes/no] | [Notes] |
| ACM Digital Library | [yes/no] | [Notes] |
| SpringerLink | [yes/no] | [Notes] |
| ScienceDirect | [yes/no] | [Notes] |
| Google Scholar | [yes/no] | [Notes] |
| Other | [yes/no] | [Notes] |

### Search Strings

| Database / API | Query | Filters | Date searched | Results |
|---|---|---|---:|---:|
| [Source] | `[query]` | [filters] | [date] | [count] |

### Search Limits

- Year range: [range]
- Language: [language]
- Publication type: [articles/conference/preprints/etc.]
- Domain/task filters: [filters]
- Venue filters: [if any]

---

## 15. Inclusion and Exclusion Criteria

### Inclusion Criteria

- [Criterion]
- [Criterion]
- [Criterion]

### Exclusion Criteria

- [Criterion]
- [Criterion]
- [Criterion]

### Screening Rules

State how ambiguous cases are handled.

- [Rule]
- [Rule]

---

## 16. Screening Log

| Stage | Count | Notes |
|---|---:|---|
| Records identified | [n] | [Notes] |
| Duplicates removed | [n] | [Notes] |
| Title/abstract screened | [n] | [Notes] |
| Full text assessed | [n] | [Notes] |
| Included in synthesis | [n] | [Notes] |
| Excluded with reasons | [n] | [Notes] |

### Exclusion Reasons

| Reason | Count | Examples |
|---|---:|---|
| Not relevant task/domain | [n] | [Examples] |
| No empirical evidence | [n] | [Examples] |
| Duplicate / superseded | [n] | [Examples] |
| Insufficient details | [n] | [Examples] |
| Out of scope | [n] | [Examples] |

---

## 17. Evidence Extraction Table

| Source | Task | Method | Dataset | Metric | Main finding | Limitation | Relevance |
|---|---|---|---|---|---|---|---|
| [Source] | [Task] | [Method] | [Dataset] | [Metric] | [Finding] | [Limitation] | [Relevance] |

For AI/ML/CV reviews, also consider extracting:

- model architecture;
- training data;
- pretrained weights;
- split policy;
- baseline;
- augmentation;
- inference/postprocessing;
- compute;
- code availability;
- reproducibility notes.

---

## 18. Quality / Risk-of-Bias Assessment

Use a quality assessment appropriate to the review type.

For AI/ML/CV reviews, consider:

| Source | Split validity | Baseline fairness | Metric alignment | Reproducibility | Leakage risk | Overall confidence |
|---|---|---|---|---|---|---|
| [Source] | [High/Med/Low] | [High/Med/Low] | [High/Med/Low] | [High/Med/Low] | [High/Med/Low] | [High/Med/Low] |

For biomedical or clinical reviews, use field-specific tools only when relevant, such as:

- Cochrane Risk of Bias;
- ROBINS-I;
- QUADAS-2;
- GRADE;
- CONSORT;
- STROBE;
- PRISMA.

Do not force biomedical frameworks onto AI/ML/CV reviews unless the manuscript type requires them.

---

## 19. Formal Synthesis Method

State how evidence was synthesized.

- [ ] thematic synthesis
- [ ] narrative synthesis
- [ ] vote counting
- [ ] evidence mapping
- [ ] meta-analysis
- [ ] benchmark comparison
- [ ] taxonomy construction
- [ ] other: [describe]

**Synthesis method details**:

> [Explain how conclusions were derived.]

**Heterogeneity / variation**:

- [Dataset differences]
- [Metric differences]
- [Task differences]
- [Model differences]
- [Evaluation protocol differences]

---

## 20. Formal Review Limitations

State limitations of the formal review.

- [Database coverage limitations]
- [Search-term limitations]
- [Screening limitations]
- [Publication bias]
- [Venue bias]
- [Language bias]
- [Metadata quality limitations]
- [Full-text access limitations]
- [Time cutoff]
- [Reproducibility limitations]

---

# Final Interpretation and Handoff

Complete these sections for all substantial reviews.

---

## 21. Limitations of This Review

State what this review does not establish.

Examples:

- not a systematic review;
- limited source base;
- no full-text screening;
- no formal quality assessment;
- no citation graph expansion;
- recent papers may be missing;
- some sources may need citation verification;
- benchmark results were not independently reproduced.

If the Formal Systematic / Scoping Review Extension was completed, summarize remaining limitations from Section 20.

---

## 22. Project Implications

Translate the synthesis into concrete project decisions.

### Research Direction

- [Implication]

### Implementation / Experiment Planning

- [Implication]

### Evaluation

- [Implication]

### Paper Writing

- [Implication]

### Claim Strength

| Claim / idea | Status | Evidence | Action |
|---|---|---|---|
| [Claim] | [supported/preliminary/needs citation/unsupported] | [Sources] | [Action] |

---

## 23. Recommended Next Step

Choose one or more.

- [ ] use `research-lookup` for missing sources
- [ ] use `citation-management` to verify references
- [ ] use `scientific-critical-thinking` to critique the gap or experiment plan
- [ ] use `scientific-writing` to draft introduction / related work prose
- [ ] use `claim-auditor` before finalizing manuscript claims
- [ ] use `peer-review` for reviewer-style critique
- [ ] update `docs/research_context.md`
- [ ] update `docs/current_status.md`
- [ ] prepare an experiment plan
- [ ] complete the Formal Systematic / Scoping Review Extension

Recommended next action:

> [Specific next action.]

---

## Final Quality Checklist

Before using this review downstream, check:

- [ ] Review purpose is clear.
- [ ] Source base is listed.
- [ ] Search or selection trace is documented.
- [ ] Sources are synthesized by theme, not merely listed.
- [ ] Evidence strength and relevance are assessed.
- [ ] Closest prior work is identified when novelty matters.
- [ ] Baselines and benchmarks are extracted when experiments matter.
- [ ] Dataset, split, metric, or leakage issues are noted when relevant.
- [ ] Literature-supported gaps are separated from possible or unsupported gaps.
- [ ] Introduction / related work support is citation-aware.
- [ ] Claims needing citation or audit are marked.
- [ ] Limitations of the review are visible.
- [ ] Formal systematic/scoping extension is completed if required.
- [ ] Recommended next step is specific.
- [ ] export to PDF with `scripts/generate_pdf.py` if a shareable or archival artifact is requested
