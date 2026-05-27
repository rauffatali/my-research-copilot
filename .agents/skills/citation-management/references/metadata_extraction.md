# Metadata Extraction Reference

This reference supports the `citation-management` skill.

Use it when extracting, completing, or repairing bibliographic metadata for references, BibTeX entries, DOI/arXiv records, dataset citations, software citations, model cards, benchmark pages, or technical documentation.

For source discovery, use `research-lookup`.  
For final claim-support checks, use `claim-auditor`.

---

## 1. Purpose

Metadata extraction turns incomplete or messy citation information into verified, structured reference metadata.

The goal is to produce references that are:

- real;
- traceable;
- correctly typed;
- complete enough for manuscript use;
- safe from AI-generated hallucination;
- compatible with BibTeX and LaTeX workflows.

Metadata extraction should be source-backed. Do not guess missing fields.

---

## 2. Core Metadata Fields

For each reference, extract or verify:

| Field | Meaning |
|---|---|
| `title` | Exact title of the work |
| `authors` | Author list in correct order |
| `year` | Publication or release year |
| `date` | Full publication/release date when available |
| `venue` | Journal, conference, workshop, publisher, repository, or source |
| `entry_type` | BibTeX type such as `article`, `inproceedings`, `misc`, `software`, `dataset` |
| `doi` | DOI without `https://doi.org/` prefix |
| `arxiv_id` | arXiv identifier |
| `url` | Stable source URL |
| `abstract` | Optional abstract or summary |
| `pages` | Page range or article number |
| `volume` | Journal volume |
| `number` | Journal issue |
| `publisher` | Publisher or organization |
| `institution` | Institution for reports or theses |
| `version` | Software, model, dataset, or document version |
| `access_date` | Needed for dynamic web resources |
| `source_checked` | Where metadata was verified |
| `status` | verified, corrected, incomplete, needs manual check, hallucinated |

---

## 3. Metadata Sources

Prefer authoritative or structured metadata sources.

### DOI Resolver / Publisher Page

Use for:

- published journal articles;
- conference proceedings;
- official article pages;
- final publication metadata.

Best for:

- DOI;
- title;
- authors;
- journal/conference;
- volume/issue/pages;
- publisher;
- publication date.

Risk:

- publisher pages may use abbreviated or styled titles;
- access restrictions may hide details.

---

### Crossref

Use for:

- DOI lookup;
- publication metadata;
- journal/conference metadata;
- reference cleanup.

Best for:

- DOI-to-BibTeX;
- title;
- author list;
- venue;
- year;
- publisher;
- type.

Limitations:

- abstracts often missing;
- preprints and workshop metadata may be incomplete;
- some conference metadata can be noisy.

---

### OpenAlex

Use for:

- broad scholarly metadata;
- citation counts;
- source/venue metadata;
- DOI discovery;
- author/source disambiguation.

Best for:

- verifying whether a work exists;
- finding DOI when title is known;
- checking publication year;
- identifying source and citation count.

Limitations:

- search can drift;
- title/abstract metadata may be incomplete;
- source type should be verified for important references.

---

### arXiv

Use for:

- AI/ML/CV preprints;
- arXiv IDs;
- preprint title/authors/abstract/category/version.

Best for:

- arXiv ID;
- title;
- authors;
- abstract;
- primary category;
- submission/update dates.

Limitations:

- not peer reviewed by default;
- published version may exist elsewhere;
- title or authors may change across versions.

---

### Semantic Scholar

Use for:

- citation metadata;
- related papers;
- author and venue metadata;
- DOI/arXiv links;
- abstract and citation counts.

Best for:

- cross-checking metadata;
- citation graph context;
- detecting related or duplicate records.

Limitations:

- rate limits;
- metadata may be incomplete;
- venue strings can be inconsistent.

---

### DBLP

Use for:

- computer science bibliographic verification;
- author disambiguation;
- conference/journal publication records.

Best for:

- CS venue metadata;
- author names;
- conference proceedings;
- publication year.

Limitations:

- abstracts usually absent;
- DOI may not always be present;
- not ideal for general semantic discovery.

---

### ACL Anthology

Use for:

- NLP and computational linguistics papers.

Best for:

- ACL/EMNLP/NAACL metadata;
- anthology IDs;
- PDF URLs;
- venue and proceedings details.

---

### Official Dataset / Model / Software Pages

Use for:

- datasets;
- model cards;
- benchmark pages;
- software repositories;
- documentation.

Best for:

- version;
- release date;
- URL;
- access date;
- organization;
- license;
- citation instructions.

Limitations:

- dynamic pages may change;
- may not be peer-reviewed;
- often needs access date.

---

## 4. Entry Type Selection

Choose entry type based on the real source type, not the convenience of a template.

| Source type | Recommended BibTeX type |
|---|---|
| Journal article | `@article` |
| Conference paper | `@inproceedings` |
| Workshop paper | `@inproceedings` or `@misc`, depending on metadata |
| arXiv preprint | `@misc` |
| Technical report | `@techreport` |
| Book | `@book` |
| Book chapter | `@incollection` |
| Thesis | `@phdthesis` or `@mastersthesis` |
| Dataset paper | `@article` or `@inproceedings` |
| Dataset page | `@dataset` or `@misc` |
| Software repository | `@software` or `@misc` |
| Model card | `@misc` |
| Benchmark leaderboard | `@misc` |
| Documentation | `@misc` |
| Standard/specification | `@misc` or `@techreport` |

If the target BibTeX processor does not support `@software` or `@dataset`, use `@misc` with clear `note`, `url`, `version`, and `access_date`.

---

## 5. DOI Metadata Extraction

When given a DOI:

1. Normalize the DOI.
2. Resolve through `https://doi.org/<doi>`.
3. Query Crossref when possible.
4. Compare returned title, authors, year, and venue with existing entry.
5. Update metadata only when the match is clear.
6. Mark mismatch as `needs manual check`.

### DOI Normalization

Convert:

```text
https://doi.org/10.1109/CVPR.2016.91
doi:10.1109/CVPR.2016.91
DOI 10.1109/CVPR.2016.91
```

to:

```text
10.1109/CVPR.2016.91
```

### DOI Mismatch Warning

If DOI metadata returns a different title, do not keep the DOI.

Classify as:

```text
DOI_TITLE_MISMATCH
```

or:

```text
needs manual check
```

---

## 6. arXiv Metadata Extraction

When given an arXiv ID or URL:

1. Normalize the arXiv ID.
2. Query arXiv metadata.
3. Extract title, authors, year, abstract, primary category, and URL.
4. Check whether a published DOI/version exists.
5. Mark as preprint unless published status is verified.

### arXiv ID Normalization

Convert:

```text
https://arxiv.org/abs/2304.02643
arXiv:2304.02643
2304.02643v1
```

to:

```text
2304.02643
```

or preserve version when version matters:

```text
2304.02643v1
```

### Preprint Note

Use:

```bibtex
note = {arXiv preprint}
```

or equivalent when required.

Do not label an arXiv-only work as a journal or conference paper.

---

## 7. Title-Based Metadata Extraction

When only a title is available:

1. Search exact title in reliable sources.
2. Prefer exact title match over high-citation partial matches.
3. Compare authors and year.
4. Check DOI/arXiv ID.
5. Classify uncertain matches as `needs manual check`.

Reliable title lookup sources:

- Crossref;
- OpenAlex;
- Semantic Scholar;
- arXiv;
- DBLP;
- publisher page;
- ACL Anthology when NLP.

Warning signs:

- multiple similar titles;
- title appears only in AI-generated text;
- title has no search footprint;
- title matches but authors/year differ;
- title is a paraphrase rather than exact paper title.

---

## 8. Author Metadata Extraction

When extracting authors:

- preserve order;
- use full names when available;
- avoid inventing middle initials;
- preserve accents when possible;
- use `and` between authors in BibTeX;
- wrap organization authors in double braces.

Example:

```bibtex
author = {Redmon, Joseph and Divvala, Santosh and Girshick, Ross and Farhadi, Ali}
```

Organization author:

```bibtex
author = {{Example Benchmark Maintainers}}
```

Avoid truncating authors unless the bibliography style or source metadata requires it.

---

## 9. Venue Metadata Extraction

Extract the actual publication venue.

Examples:

- journal name;
- conference proceedings;
- workshop name;
- arXiv;
- technical report institution;
- dataset repository;
- model repository;
- software repository;
- documentation site.

For conferences:

```bibtex
booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}
```

For journals:

```bibtex
journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence}
```

For preprints:

```bibtex
archivePrefix = {arXiv}
```

Do not confuse:

- CVPR main conference with CVPR workshop;
- arXiv preprint with conference paper;
- benchmark page with paper;
- GitHub repository with publication venue.

---

## 10. Date and Year Extraction

Use the date that matches the cited version.

For published papers:

- use publication year;
- include full date only when needed.

For preprints:

- use arXiv submission or version year;
- check if a published version exists.

For software/datasets/model cards:

- use release year or version date;
- include access date when page is dynamic.

For webpages:

- use publication/update year when available;
- include access date.

---

## 11. Dataset, Benchmark, Software, and Model Metadata

These artifacts need more than ordinary paper metadata.

### Dataset

Extract:

- dataset name;
- authors/maintainers;
- year/date;
- version;
- DOI or URL;
- license if relevant;
- official citation recommendation;
- access date.

### Benchmark / Leaderboard

Extract:

- benchmark name;
- maintainers;
- URL;
- access date;
- version or snapshot date if available;
- associated paper if one exists.

### Software

Extract:

- software name;
- authors/organization;
- version;
- repository URL;
- release date or access date;
- DOI if archived on Zenodo or similar;
- paper if one exists.

### Model Card

Extract:

- model name;
- organization/authors;
- version/release date;
- URL;
- associated paper if available;
- access date.

---

## 12. Metadata Conflict Resolution

When sources disagree, prefer this order:

1. Publisher page or DOI landing page;
2. Crossref for DOI metadata;
3. arXiv for preprint-specific metadata;
4. DBLP for CS publication records;
5. ACL Anthology for NLP papers;
6. OpenAlex / Semantic Scholar as cross-checks;
7. official dataset/software/model page for non-paper artifacts;
8. saved lookup artifacts as context.

Record conflicts rather than silently choosing.

Conflict examples:

| Conflict | Action |
|---|---|
| DOI title differs from BibTeX title | mark mismatch, verify manually |
| arXiv and published title differ | cite version used or prefer published title |
| author order differs | check publisher/arXiv source |
| venue missing in one source | verify with publisher/DBLP |
| year differs | use publication year for published work; arXiv year for preprint |

---

## 13. Hallucinated Metadata Patterns

Flag entries that show:

- fake DOI;
- DOI from another paper;
- plausible title with no source;
- real title with wrong authors;
- real authors with fake title;
- real conference with impossible year/volume/pages;
- fabricated journal name;
- arXiv ID pointing to a different paper;
- mixed metadata from two or more real works;
- no stable identifier and no exact title match.

Classification:

- `hallucinated`;
- `metadata incomplete`;
- `needs manual check`;
- `wrong citation for claim`.

Do not repair hallucinated metadata by guessing. Use `research-lookup` to find a real replacement if needed.

---

## 14. Output Format for Metadata Extraction

Use this format for substantial metadata work.

```md
## Metadata Extraction Report

### Scope

- Input files:
- Sources checked:
- Date:

### Summary

| Status | Count |
|---|---:|
| verified | 0 |
| corrected | 0 |
| metadata incomplete | 0 |
| needs manual check | 0 |
| hallucinated | 0 |

### Metadata Findings

| Citation key | Field | Original | Verified / corrected | Source | Status |
|---|---|---|---|---|---|
| [key] | DOI | [old] | [new] | [Crossref] | corrected |

### Conflicts

| Citation key | Conflict | Sources | Action |
|---|---|---|---|
| [key] | [conflict] | [sources] | [action] |

### Remaining Manual Checks

- [item]

### Handoffs

- [ ] `research-lookup` for missing real sources
- [ ] `claim-auditor` for citation-context support
- [ ] `venue-templates` for final venue style
```

---

## 15. Metadata Extraction Checklist

Before finishing:

- [ ] DOI normalized and verified where available.
- [ ] arXiv ID normalized and verified where relevant.
- [ ] Title matches verified source.
- [ ] Authors and order match verified source.
- [ ] Year/date is correct for cited version.
- [ ] Venue/source is correct.
- [ ] Entry type matches source type.
- [ ] Dataset/software/model artifacts include version or access date when relevant.
- [ ] Web sources include stable URL and access date when required.
- [ ] Conflicts are reported.
- [ ] Unverified entries are marked.
- [ ] Hallucinated entries are flagged.
- [ ] No metadata is guessed.

---

## Final Reminder

Metadata extraction is not clerical cleanup only.

Bad metadata can create fake authority, hide hallucinated references, break LaTeX builds, misrepresent preprints as peer-reviewed work, or cause a paper to cite the wrong source.

Verify before trusting.
