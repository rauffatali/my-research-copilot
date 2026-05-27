# Citation Use and Style Reference

This reference supports the `literature-review` skill.

Use it when a literature review needs citation-aware synthesis, candidate citation organization, or manuscript-section support.

For final BibTeX generation, DOI validation, duplicate reference cleanup, and venue-specific bibliography formatting, use the `citation-management` skill.

---

## 1. Role in the Literature Review Workflow

The literature-review skill should use citations to support synthesis, not to perform final bibliography maintenance.

Use this reference to:

- identify which source supports which claim;
- distinguish strong citation support from weak support;
- organize candidate citations for introduction, related work, and literature review sections;
- avoid unsupported background, novelty, or gap claims;
- prepare citation notes for `scientific-writing`;
- flag references that need cleanup by `citation-management`.

Do not use this reference to:

- invent citations;
- fabricate DOI, venue, author, or year metadata;
- finalize BibTeX records;
- enforce venue-specific formatting when `citation-management` is available;
- treat a citation as support without checking relevance.

---

## 2. Citation Support Categories

When reviewing literature, classify citation support by strength.

| Label | Meaning | Action |
|---|---|---|
| `strong support` | Source directly supports the statement or comparison | Candidate for manuscript use |
| `moderate support` | Source supports part of the statement or provides related evidence | Use carefully or combine with another source |
| `weak support` | Source is background only or only loosely related | Do not use for strong claims |
| `needs citation` | Statement needs literature support, but no source is identified | Use `research-lookup` |
| `needs verification` | Metadata, DOI, venue, or relevance must be checked | Use `citation-management` |
| `not suitable` | Source does not support the intended statement | Do not cite for this claim |

---

## 3. Claim-to-Citation Mapping

Use this table when preparing introduction, motivation, related work, or literature review support.

| Claim / statement | Candidate source | Support strength | Notes | Next action |
|---|---|---|---|---|
| [Claim] | [Source] | [strong/moderate/weak] | [Why it supports or does not support the claim] | [keep / verify / lookup more / remove] |

Examples of claim types:

- problem importance;
- task definition;
- dataset or benchmark background;
- method-family description;
- prior-work limitation;
- baseline expectation;
- evaluation metric convention;
- research gap;
- novelty positioning;
- motivation for current project.

---

## 4. Citation Use by Manuscript Section

### Introduction / Background / Motivation

Use citations for:

- importance of the problem;
- known limitations of existing approaches;
- benchmark or dataset relevance;
- real-world or scientific motivation;
- high-level method context;
- gap framing before the contribution statement.

Avoid:

- overloading the introduction with too many technical citations;
- citing weakly related sources for broad motivation;
- making novelty claims without closest-prior-work support.

### Related Work / Literature Review

Use citations for:

- grouping prior work into themes;
- comparing method families;
- identifying baselines;
- explaining dataset and benchmark history;
- contrasting the current project with closest prior work;
- supporting gap statements.

Avoid:

- paper-by-paper summaries with no synthesis;
- citing sources only because they are highly cited;
- citing unrelated work to inflate coverage.

### Methods / Experiments

Use citations for:

- model families;
- losses or training strategies;
- preprocessing or augmentation choices;
- dataset papers;
- metric definitions;
- baseline implementations;
- evaluation protocols.

Avoid:

- citing a method paper without matching the actual implementation;
- citing a metric without specifying the metric variant;
- citing a dataset without confirming split or label protocol.

### Discussion / Limitations

Use citations for:

- known failure modes;
- domain shift;
- dataset bias;
- leakage risks;
- annotation uncertainty;
- limitations shared with prior work;
- future-work directions grounded in literature.

Avoid:

- using citations to hide unsupported speculation;
- making broader conclusions than the cited evidence supports.

---

## 5. Common Citation Styles

Use these examples only for orientation. Final formatting should be handled by `citation-management` or the venue template.

### IEEE Style

Common in engineering, computer vision, and conference papers.

**Journal article**

```text
[1] A. Author, B. Author, and C. Author, "Title of article," Journal Name, vol. 12, no. 3, pp. 10-20, 2024.
```

**Conference paper**

```text
[2] A. Author and B. Author, "Title of paper," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), 2024, pp. 100-110.
```

**arXiv preprint**

```text
[3] A. Author, B. Author, and C. Author, "Title of preprint," arXiv:2401.00001, 2024.
```

### ACM Style

Common in computer science.

```text
A. Author and B. Author. 2024. Title of paper. In Proceedings of Conference Name. ACM, 1-12.
```

### APA Style

Common in social science and interdisciplinary writing.

```text
Author, A., & Author, B. (2024). Title of article. Journal Name, 12(3), 10-20. https://doi.org/...
```

### Nature Style

Common in Nature-family journals.

```text
Author, A. & Author, B. Title of article. Journal Name 12, 10-20 (2024).
```

---

## 6. AI/ML/CV Citation Metadata Checklist

Before using a source in a literature review or manuscript, check:

- [ ] title is correct;
- [ ] author list is correct enough for citation use;
- [ ] year is correct;
- [ ] venue or source is correct;
- [ ] DOI, arXiv ID, or URL is available when possible;
- [ ] publication type is clear: journal, conference, workshop, preprint, dataset paper, benchmark page, technical report;
- [ ] source actually supports the claim;
- [ ] if it is a preprint, peer-review status is not overstated;
- [ ] if it is a benchmark or leaderboard page, date accessed is recorded when relevant;
- [ ] if it is software/model documentation, version or release date is recorded when relevant.

Use `citation-management` for final metadata cleanup.

---

## 7. DOI and Identifier Guidance

Prefer stable identifiers when available.

| Identifier | Use for |
|---|---|
| DOI | Published journal/conference papers |
| arXiv ID | Preprints and arXiv-hosted versions |
| ACL Anthology ID | NLP/CL papers |
| OpenReview URL | ICLR-style submissions/reviews |
| DBLP entry | CS bibliographic disambiguation |
| GitHub URL | Code artifacts, when cited as software |
| Dataset URL / DOI | Dataset and benchmark artifacts |

Best practices:

- Use `https://doi.org/...` for DOI URLs.
- Keep arXiv version information when version matters.
- Do not cite a GitHub repository as evidence for a scientific claim unless the claim is about software availability or implementation.
- Do not treat benchmark leaderboard entries as peer-reviewed papers.

---

## 8. Citation Density Guidance

Citation density should serve clarity.

### Introduction

Use enough citations to establish:

- problem importance;
- existing work;
- gap or limitation;
- contribution context.

Avoid citation overload in every sentence.

### Related Work

Citation density is usually higher because the section compares prior work.

Group citations thematically:

```text
Early CNN-based approaches studied [...], while recent transformer-based methods focus on [...].
```

### Methods

Cite canonical method, dataset, metric, and implementation sources.

### Results / Discussion

Cite prior results only when comparing fairly and when protocols are compatible.

---

## 9. Warning Signs

Be careful when:

- a source is cited only because it is famous;
- a source is from a different task or dataset;
- a source is a preprint but described as established evidence;
- a survey is cited for a specific empirical result from another paper;
- citation metadata comes only from an LLM summary;
- a claim has only weak background citations;
- a novelty claim lacks closest prior work;
- a related-work paragraph lists papers but does not synthesize them.

---

## 10. Handoff to Other Skills

Use `citation-management` when:

- BibTeX is needed;
- DOI validation is needed;
- duplicate references must be cleaned;
- citation style must match a venue;
- references must be inserted into LaTeX.

Use `claim-auditor` when:

- final manuscript claims must be checked against evidence;
- claim strength must be downgraded;
- a paper section may overclaim.

Use `scientific-writing` when:

- citation-backed notes must become polished prose.

Use `research-lookup` when:

- a claim is marked `needs citation`;
- closer prior work may be missing;
- source coverage is too narrow.

---

## Final Reminder

In literature review work, citation style matters less than citation truth.

A cleanly formatted citation is not useful if it does not support the statement.
