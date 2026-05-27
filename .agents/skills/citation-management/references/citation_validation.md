# Citation Validation Reference

This reference supports the `citation-management` skill.

Use it when validating reference reality, checking BibTeX metadata, detecting hallucinated references, repairing DOI/arXiv metadata, and checking whether manuscript citation commands resolve.

For source discovery, use `research-lookup`.  
For claim-evidence support, use `claim-auditor`.

---

## 1. Purpose

Citation validation ensures that bibliography entries are real, correct, usable, and safe for manuscript submission.

Validation checks:

- whether references exist;
- whether metadata is correct;
- whether DOI/arXiv/URL identifiers resolve;
- whether BibTeX syntax is valid;
- whether required fields are present;
- whether duplicate entries exist;
- whether citation keys are valid and stable;
- whether LaTeX citation commands resolve;
- whether AI-generated references are hallucinated or mismatched.

A reference can be well-formatted but still wrong. Citation validation must check both **format** and **reality**.

---

## 2. Validation Levels

Use the smallest level that fits the task.

### Level 1: Syntax Validation

Checks whether `.bib` files parse and have valid structure.

Use for:

- quick cleanup;
- pre-commit checks;
- early draft hygiene.

### Level 2: Metadata Validation

Checks whether title, authors, year, venue, DOI, arXiv ID, and URL are plausible and complete.

Use for:

- paper drafting;
- related work preparation;
- bibliography cleanup.

### Level 3: Reference Reality Validation

Checks whether the cited work actually exists in reliable metadata sources.

Use for:

- AI-generated references;
- suspicious bibliography entries;
- final submission cleanup;
- hallucinated-reference cleanup.

### Level 4: Citation Context Validation

Checks whether the reference is likely appropriate for the nearby manuscript claim.

This overlaps with `claim-auditor`.

Use citation-management to flag suspicious citation contexts, then use `claim-auditor` for final claim-support auditing.

---

## 3. Reference Reality Checks

For each reference, verify the work against reliable sources.

Preferred sources:

1. DOI resolver / publisher page;
2. Crossref;
3. OpenAlex;
4. arXiv;
5. Semantic Scholar;
6. DBLP;
7. ACL Anthology;
8. PubMed only for biomedical or clinical references;
9. official dataset, model, software, or benchmark page.

Check:

- title;
- authors;
- year;
- venue;
- DOI;
- arXiv ID;
- URL;
- publication type;
- preprint or peer-reviewed status;
- whether the reference is the intended work.

Do not rely only on:

- LLM-generated references;
- copied bibliography text from unknown sources;
- incomplete Google Scholar snippets;
- unsourced Markdown/LaTeX drafts;
- citation keys alone.

---

## 4. Hallucinated Reference Detection

AI-generated references may be fake, blended, or mismatched.

Flag references that show any of these signs:

- title cannot be found in reliable sources;
- DOI resolves to a different paper;
- arXiv ID points to a different paper;
- author list does not match the title;
- year does not match metadata records;
- venue does not exist;
- venue and year combination is impossible or unlikely;
- paper appears only in the manuscript and nowhere else;
- title combines terms from real papers but no exact work exists;
- entry mixes real DOI with fake title;
- entry mixes real title with wrong authors;
- citation key appears real but points to the wrong source;
- preprint is described as peer-reviewed without evidence;
- duplicate entries disagree on important metadata.

Classification:

| Status | Meaning | Action |
|---|---|---|
| `verified` | Work exists and metadata matches | Keep |
| `corrected` | Work exists but metadata was repaired | Keep with correction note |
| `metadata incomplete` | Work exists but metadata is missing | Complete if possible |
| `needs manual check` | Could not verify confidently | Do not use for strong claims |
| `hallucinated` | No credible evidence the work exists | Remove or mark |
| `wrong citation for claim` | Work exists but appears unrelated to local claim | Send to `claim-auditor` |

Do not invent replacement references. Use `research-lookup` if a replacement source is needed.

---

## 5. DOI Validation

### DOI Format

A DOI usually starts with `10.`.

Examples:

```text
10.1109/CVPR.2016.91
10.1007/978-3-319-10602-1_48
10.48550/arXiv.2304.02643
```

In BibTeX, prefer:

```bibtex
doi = {10.1109/CVPR.2016.91}
```

Avoid:

```bibtex
doi = {doi:10.1109/CVPR.2016.91}
doi = {https://doi.org/10.1109/CVPR.2016.91}
```

The URL form may be used separately:

```bibtex
url = {https://doi.org/10.1109/CVPR.2016.91}
```

### DOI Resolution

Check:

- DOI resolves through `https://doi.org/<doi>`;
- resolved page corresponds to the same work;
- title matches;
- year matches;
- authors are compatible;
- venue matches.

### DOI Mismatch Cases

Common problems:

- DOI belongs to a different article;
- DOI has typo;
- DOI points to a preprint or dataset, not the cited paper;
- DOI metadata is correct but BibTeX title is wrong;
- DOI omitted for a modern paper that has one.

Actions:

- correct DOI if verified;
- remove DOI if it is wrong and no verified DOI is found;
- mark as `needs manual check` if uncertain.

---

## 6. arXiv Validation

Check arXiv entries for:

- valid arXiv ID;
- title match;
- author match;
- year/date match;
- primary category when relevant;
- version if version matters;
- whether a published version exists.

Typical BibTeX pattern:

```bibtex
@misc{example2025arxiv,
  author        = {Author, Alice and Researcher, Bob},
  title         = {Title of the Preprint},
  year          = {2025},
  eprint        = {2501.00001},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV},
  url           = {https://arxiv.org/abs/2501.00001},
  note          = {arXiv preprint}
}
```

Do not treat arXiv as peer-reviewed unless a peer-reviewed version is verified.

If both preprint and published versions exist:

- prefer the published version for manuscript references when appropriate;
- keep arXiv if the preprint version is specifically discussed;
- avoid duplicate references to the same work unless necessary.

---

## 7. Required Fields by Entry Type

Required fields depend on venue and style, but these are practical defaults.

| Entry type | Required / expected fields |
|---|---|
| `@article` | author, title, journal, year |
| `@inproceedings` | author, title, booktitle, year |
| `@misc` | author or organization, title, year/date, URL/DOI/arXiv ID |
| `@techreport` | author, title, institution, year |
| `@book` | author/editor, title, publisher, year |
| `@incollection` | author, title, booktitle, publisher, year |
| `@phdthesis` | author, title, school, year |
| `@software` | author/organization, title, version/date, URL |
| `@dataset` | author/organization, title, year/date, DOI/URL |

Missing required fields should be classified as `metadata incomplete`.

Do not guess missing fields.

---

## 8. Author Name Validation

Check:

- names match reliable metadata;
- author order is correct;
- names are not truncated incorrectly;
- organizations are wrapped in double braces when needed;
- particles and prefixes are preserved;
- accents are handled consistently.

Examples:

```bibtex
author = {Redmon, Joseph and Divvala, Santosh and Girshick, Ross and Farhadi, Ali}
```

Organization author:

```bibtex
author = {{Example Benchmark Maintainers}}
```

Avoid:

```bibtex
author = {Example Benchmark Maintainers}
```

because BibTeX may parse it as a personal name.

---

## 9. Title and Capitalization Validation

Check:

- title exactly matches the source or accepted citation form;
- capitalization is not accidentally lowercased;
- acronyms are protected;
- dataset/model names are protected;
- proper nouns are protected;
- punctuation is accurate.

Examples:

```bibtex
title = {{YOLO}: You Only Look Once}
title = {{Microsoft COCO}: Common Objects in Context}
title = {An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale}
```

Common protected terms:

```text
{AI}, {ML}, {CNN}, {R-CNN}, {YOLO}, {ViT}, {DETR}, {CLIP}, {SAM}, {COCO}, {ImageNet}, {Cityscapes}, {BDD100K}, {mAP}, {IoU}
```

---

## 10. Venue and Publication Type Validation

Check that entry type matches publication type.

| Source type | Preferred BibTeX type |
|---|---|
| journal article | `@article` |
| conference paper | `@inproceedings` |
| workshop paper | `@inproceedings` or `@misc`, depending on venue |
| arXiv preprint | `@misc` |
| dataset paper | `@article` or `@inproceedings` |
| dataset page | `@misc` or `@dataset` |
| software / code | `@software` or `@misc` |
| benchmark leaderboard | `@misc` |
| technical report | `@techreport` |
| thesis | `@phdthesis` or `@mastersthesis` |

Flag:

- arXiv preprints stored as journal articles without publication evidence;
- workshop papers labeled as main-conference papers;
- benchmark pages labeled as papers;
- software repositories cited as scientific evidence.

---

## 11. Duplicate Validation

Detect duplicates by:

- DOI;
- arXiv ID;
- normalized title;
- normalized author/year/title combination;
- URL;
- citation key similarity.

Duplicate categories:

| Category | Meaning | Action |
|---|---|---|
| exact duplicate | same work, same metadata | remove one |
| same work, better metadata available | one entry incomplete | merge into best entry |
| preprint and published version | same work has two versions | prefer one or keep both with reason |
| related but distinct | extension or follow-up paper | keep both |
| unclear | uncertain relationship | mark for manual check |

When merging:

- keep the citation key already used in the manuscript when possible;
- update all LaTeX citations if the key changes;
- report old key to new key mapping.

---

## 12. LaTeX Citation Validation

Check manuscript files for citation commands.

Common commands:

```latex
\cite{key}
\citep{key}
\citet{key}
\autocite{key}
\parencite{key}
\textcite{key}
```

Validate:

- every cited key exists in the `.bib`;
- every duplicate key is resolved;
- unused entries are reported;
- renamed keys are updated in `.tex`;
- placeholder citations are removed;
- bibliography file path is correct;
- citation style matches the template.

Placeholder warning signs:

```text
TODO
citation-needed
ref
missingcitation
unknown2024
smith2024
```

A common report table:

| Issue | Key | File | Action |
|---|---|---|---|
| missing key | `key` | `paper/main.tex` | add verified reference or replace |
| unused entry | `key` | `references.bib` | keep/remove decision |
| duplicate key | `key` | `references.bib` | merge/rename |
| suspicious context | `key` | `paper/intro.tex` | send to claim-auditor |

---

## 13. Citation Context Sanity Validation

Citation-management should not fully audit claims, but it should flag suspicious citation contexts.

Flag when:

- a source is real but clearly from another topic;
- a citation follows a strong claim but source is only background;
- a survey is cited for a specific empirical result;
- a benchmark source is used to support a model superiority claim;
- a dataset paper is cited as if it proves method performance;
- a preprint is used to support a settled consensus claim;
- a citation appears after “state-of-the-art,” “robust,” “generalizes,” “solves,” or similar strong wording.

Action:

- mark as `wrong citation for claim` or `needs claim audit`;
- send to `claim-auditor`;
- use `research-lookup` to find better support if needed.

---

## 14. URL and Web Source Validation

Use web references carefully.

Check:

- URL is official or stable;
- access date is included when required;
- page title matches citation;
- organization/author is clear;
- version or release date is recorded when relevant.

Use web references for:

- software documentation;
- model cards;
- dataset pages;
- benchmark leaderboards;
- release notes;
- official project pages.

Avoid using webpages as support for scientific claims when peer-reviewed or archival sources are available.

---

## 15. Validation Report Format

Use this format for substantial citation validation tasks.

```md
## Citation Validation Report

### Scope

- Bibliography files:
- Manuscript files:
- Verification sources:
- Date:

### Summary

| Status | Count |
|---|---:|
| verified | 0 |
| corrected | 0 |
| duplicate | 0 |
| metadata incomplete | 0 |
| needs manual check | 0 |
| hallucinated | 0 |
| wrong citation for claim | 0 |

### Findings

| Citation key | Status | Problem | Evidence checked | Action |
|---|---|---|---|---|
| [key] | [status] | [problem] | [sources] | [action] |

### File Changes

| File | Change |
|---|---|
| [file] | [change] |

### Remaining Risks

- [risk]

### Handoffs

- [ ] `research-lookup` needed for missing real sources
- [ ] `claim-auditor` needed for citation-context support
- [ ] `venue-templates` needed for final venue formatting
```

---

## 16. Validation Checklist

Before finalizing:

- [ ] every reference exists or is marked;
- [ ] hallucinated references are flagged;
- [ ] DOI metadata is checked where available;
- [ ] arXiv metadata is checked where relevant;
- [ ] title, authors, year, and venue match;
- [ ] entry types match publication types;
- [ ] required fields are present;
- [ ] duplicate entries are handled;
- [ ] citation keys are unique;
- [ ] LaTeX citations resolve;
- [ ] unused entries are reported;
- [ ] preprint status is not overstated;
- [ ] web/dataset/software references include stable URLs and access dates when needed;
- [ ] suspicious citation contexts are handed to `claim-auditor`;
- [ ] missing-source cases are handed to `research-lookup`.

---

## Final Reminder

Citation validation is not just formatting.

It protects the paper from:

- fake AI-generated references;
- DOI/title mismatches;
- duplicate references;
- broken LaTeX citations;
- mislabeled preprints;
- unsupported citation contexts.

A citation is safe only when the reference is real, metadata is correct, and the citation context is appropriate.
