# Citation Management Checklist

Use this checklist when cleaning references, validating `.bib` files, checking LaTeX citations, or detecting AI-generated / hallucinated references.

This checklist supports the `citation-management` skill.

For source discovery, use `research-lookup`.  
For literature synthesis, use `literature-review`.  
For checking whether a citation supports a manuscript claim, use `claim-auditor`.

---

## 1. Scope

Before starting, define the scope.

- [ ] Files to check are identified.
- [ ] Bibliography file is identified, such as `paper/references.bib`.
- [ ] Manuscript files are identified, such as `paper/*.tex`.
- [ ] Saved source artifacts are identified, such as `sources/*.md` or `sources/*.json`.
- [ ] Task type is clear.

Task type:

- [ ] reference verification
- [ ] hallucinated-reference cleanup
- [ ] BibTeX cleanup
- [ ] DOI / arXiv / metadata completion
- [ ] duplicate detection
- [ ] citation key normalization
- [ ] LaTeX citation hygiene
- [ ] venue / style readiness
- [ ] final submission cleanup

---

## 2. Reference Reality Check

For each reference, verify that the work exists.

Check against one or more reliable sources:

- [ ] DOI resolver or publisher page
- [ ] Crossref
- [ ] OpenAlex
- [ ] arXiv
- [ ] Semantic Scholar
- [ ] DBLP
- [ ] ACL Anthology
- [ ] official dataset / model / software page
- [ ] saved `sources/*.md` or `sources/*.json` artifact
- [ ] PubMed only when biomedical / clinical context is relevant

For each reference:

- [ ] Title exists and matches.
- [ ] Authors match.
- [ ] Year matches.
- [ ] Venue or source matches.
- [ ] DOI resolves to the same work.
- [ ] arXiv ID points to the same work.
- [ ] URL is reachable or plausibly stable.
- [ ] Publication type is clear.
- [ ] Preprint status is clear.
- [ ] Peer-reviewed status is not overstated.

Status label:

- [ ] `verified`
- [ ] `corrected`
- [ ] `metadata incomplete`
- [ ] `needs manual check`
- [ ] `not found`
- [ ] `hallucinated`

---

## 3. Hallucinated Reference Cleanup

Use this section when references may have been created or modified by AI.

Flag references that show any of the following:

- [ ] Title cannot be found in reliable sources.
- [ ] DOI resolves to a different title.
- [ ] Authors do not match the title.
- [ ] Year does not match the publication record.
- [ ] Venue does not exist or is implausible.
- [ ] Conference name is wrong for the year.
- [ ] arXiv ID is malformed.
- [ ] arXiv ID points to a different paper.
- [ ] Citation key exists in text but not in `.bib`.
- [ ] `.bib` entry exists but seems unrelated to the manuscript sentence.
- [ ] Source is a preprint but is described as peer-reviewed.
- [ ] Reference appears to blend multiple real papers.
- [ ] Reference has no credible search footprint.

For each suspicious reference, classify:

- [ ] `verified`
- [ ] `corrected`
- [ ] `duplicate`
- [ ] `metadata incomplete`
- [ ] `needs manual check`
- [ ] `hallucinated`
- [ ] `wrong citation for claim`

Actions:

- [ ] Do not silently keep hallucinated references.
- [ ] Do not invent replacement citations.
- [ ] Remove only when cleanup is explicitly requested.
- [ ] Otherwise mark as `HALLUCINATED_REFERENCE`.
- [ ] Suggest replacement only if a verified real source exists.
- [ ] Send `wrong citation for claim` cases to `claim-auditor`.

Recommended report table:

| Citation key | Status | Evidence checked | Problem | Action |
|---|---|---|---|---|
| [key] | [status] | [sources checked] | [problem] | [action] |

---

## 4. BibTeX Syntax and Structure

For each `.bib` file:

- [ ] BibTeX parses without syntax errors.
- [ ] Braces are balanced.
- [ ] Quotes are balanced.
- [ ] Each entry has a unique citation key.
- [ ] Each entry has exactly one entry type.
- [ ] Required fields are present for the entry type.
- [ ] Duplicate fields are removed.
- [ ] Invalid characters are fixed.
- [ ] LaTeX-sensitive characters are escaped when needed.
- [ ] Entries are consistently formatted.

Common required fields:

| Entry type | Typical required fields |
|---|---|
| `@article` | author, title, journal, year |
| `@inproceedings` | author, title, booktitle, year |
| `@misc` | author or organization, title, year or date, url or note |
| `@techreport` | author, title, institution, year |
| `@software` | author or organization, title, version/date, url |
| `@dataset` | author or organization, title, year/date, DOI or URL |

---

## 5. Metadata Completeness

Check whether important metadata is missing.

- [ ] DOI is present when available.
- [ ] arXiv ID is present for arXiv preprints.
- [ ] URL is present for webpages, software, datasets, and reports.
- [ ] Venue or publisher is present.
- [ ] Year is present.
- [ ] Author list is present.
- [ ] Pages, article number, or proceedings information is present when relevant.
- [ ] Access date is present for web pages when required.
- [ ] Version is present for software, datasets, models, or technical docs when relevant.

Do not guess missing metadata. Verify it from a reliable source.

---

## 6. BibTeX Content Quality

Check formatting and scientific correctness.

- [ ] Titles are accurate.
- [ ] Acronyms are protected with braces, such as `{YOLO}`, `{CNN}`, `{ViT}`, `{COCO}`.
- [ ] Dataset names are protected when needed.
- [ ] Model names are protected when needed.
- [ ] Proper nouns are protected when needed.
- [ ] Author names are formatted consistently.
- [ ] Venue names are normalized.
- [ ] arXiv preprints are not labeled as journal articles.
- [ ] Conference papers use `@inproceedings` when appropriate.
- [ ] Journal papers use `@article` when appropriate.
- [ ] Dataset/software/model artifacts use suitable entry types or clear `@misc` entries.
- [ ] Publisher or organization is included when useful.
- [ ] DOI format is normalized.
- [ ] URL format is normalized.

---

## 7. Duplicate Detection

Check for duplicates.

Duplicate patterns:

- [ ] Same DOI under different keys.
- [ ] Same arXiv ID under different keys.
- [ ] Same title with different casing.
- [ ] Same paper as preprint and published version.
- [ ] Same work with abbreviated authors.
- [ ] Same work with conference and journal extension.
- [ ] Same dataset/software artifact cited multiple ways.

Classify duplicates:

- [ ] exact duplicate
- [ ] same work with different metadata
- [ ] preprint and published version
- [ ] related but distinct works
- [ ] unclear

When merging duplicates:

- [ ] Keep the best verified metadata.
- [ ] Preserve the citation key most used in manuscript unless key cleanup is requested.
- [ ] Update all manuscript citations if keys change.
- [ ] Record removed or merged keys.
- [ ] Do not merge preprint and journal extension if they are meaningfully different works.

---

## 8. Citation Key Hygiene

Check citation keys.

Good keys are:

- [ ] unique
- [ ] readable
- [ ] stable
- [ ] short enough for LaTeX
- [ ] based on first author, year, and keyword
- [ ] not misleading

Avoid keys that are:

- [ ] random IDs
- [ ] full titles
- [ ] too long
- [ ] duplicated
- [ ] inconsistent
- [ ] unrelated to the paper
- [ ] changed unnecessarily

Example key style:

```bibtex
redmon2016yolo
dosovitskiy2021vit
lin2014coco
example2025method
```

If changing keys:

- [ ] Update all `paper/*.tex` citations.
- [ ] Report old key → new key mapping.
- [ ] Check that no broken citations remain.

---

## 9. LaTeX Citation Hygiene

Check manuscript citations.

Citation commands may include:

- `\cite{...}`
- `\citep{...}`
- `\citet{...}`
- `\autocite{...}`
- `\parencite{...}`
- `\textcite{...}`
- `\citeauthor{...}`
- `\citeyear{...}`

Checklist:

- [ ] Every citation key in `.tex` exists in `.bib`.
- [ ] Every `.bib` entry is cited or intentionally retained.
- [ ] Multi-citation commands are valid.
- [ ] Citation keys are spelled consistently.
- [ ] Removed entries do not leave broken citations.
- [ ] Renamed keys are updated everywhere.
- [ ] Bibliography file path is correct.
- [ ] Bibliography style or package matches the paper template.
- [ ] No placeholder citations remain, such as `TODO`, `ref`, `citation-needed`.

Report:

| Issue type | Key / file | Problem | Action |
|---|---|---|---|
| missing key | [key] | cited in `.tex` but absent from `.bib` | add verified entry or replace |
| unused entry | [key] | present in `.bib` but not cited | keep/remove decision |
| duplicate key | [key] | repeated in `.bib` | merge/fix |
| suspicious context | [key] | citation may not support sentence | send to `claim-auditor` |

---

## 10. Citation Context Sanity Check

Citation-management does not fully audit claim support, but it should flag suspicious contexts.

Flag cases where:

- [ ] citation is attached to a claim outside the paper’s topic;
- [ ] cited paper exists but is about a different task/dataset/method;
- [ ] survey is cited for a specific result from another paper;
- [ ] preprint is cited as established evidence;
- [ ] citation appears after a strong claim such as “state-of-the-art,” “robust,” or “generalizes”;
- [ ] citation is used for a claim that needs experimental evidence from this project;
- [ ] source is real but seems like the wrong citation.

Action:

- [ ] Mark as `wrong citation for claim` or `needs claim audit`.
- [ ] Send to `claim-auditor`.
- [ ] Use `research-lookup` if a replacement source is needed.

---

## 11. Preprint, Workshop, Dataset, and Software Handling

Check publication type carefully.

### Preprints

- [ ] Mark arXiv/bioRxiv/medRxiv sources as preprints unless a published version is verified.
- [ ] Do not describe preprints as peer-reviewed unless verified.
- [ ] Prefer published version when appropriate.
- [ ] Keep arXiv ID if the arXiv version is cited.

### Workshop Papers

- [ ] Identify workshop status clearly when relevant.
- [ ] Do not imply main-conference acceptance unless verified.

### Dataset / Benchmark Papers

- [ ] Cite the dataset paper or official dataset page.
- [ ] Include DOI or URL when available.
- [ ] Record access date for dynamic benchmark pages when required.
- [ ] Do not cite a leaderboard as if it were a peer-reviewed paper.

### Software / Model Artifacts

- [ ] Cite official paper when one exists.
- [ ] Cite software/model page when the claim is about implementation or availability.
- [ ] Include version, release date, or commit when relevant.
- [ ] Do not use GitHub as scientific evidence unless the claim is about code availability.

---

## 12. Venue / Style Readiness

Before submission or venue conversion:

- [ ] Target venue is known.
- [ ] Citation style is known: numeric, author-year, or footnote.
- [ ] Bibliography style file is correct.
- [ ] Venue naming is normalized.
- [ ] DOI/URL policy is followed.
- [ ] arXiv/preprint policy is followed.
- [ ] Page limits or reference limits are considered.
- [ ] Capitalization policy is followed.
- [ ] Conference and journal abbreviations are acceptable.
- [ ] References compile correctly in the target template.

If venue-specific formatting is needed, use `venue-templates`.

---

## 13. Cleanup Report

After cleanup, produce a short report.

```md
## Citation Cleanup Report

### Scope

- Files checked:
- Bibliography files:
- Manuscript files:
- Verification sources:

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

### Files Changed

- [file]

### Key Fixes

| Citation key | Change | Reason |
|---|---|---|
| [key] | [change] | [reason] |

### Remaining Risks

- [risk]

### Required Handoffs

- [ ] `research-lookup` for missing real sources
- [ ] `claim-auditor` for suspicious citation contexts
- [ ] `venue-templates` for venue-specific formatting
```

---

## 14. Final Checklist

Before finishing citation-management work:

- [ ] Scope is clear.
- [ ] Files checked are listed.
- [ ] Verification sources are stated.
- [ ] Hallucinated references are flagged.
- [ ] DOI/arXiv/URL metadata is verified where possible.
- [ ] BibTeX syntax is valid.
- [ ] Required fields are present.
- [ ] Duplicate keys and duplicate works are handled.
- [ ] Citation keys are stable and consistent.
- [ ] LaTeX citation commands resolve.
- [ ] Unused entries are reported.
- [ ] Preprints are not mislabeled as peer-reviewed papers.
- [ ] Dataset/software/model citations are handled appropriately.
- [ ] Unverified references are marked as `needs manual check`.
- [ ] Claim-support issues are handed off to `claim-auditor`.
- [ ] Source discovery gaps are handed off to `research-lookup`.
- [ ] Any file edits are summarized.

---

## Final Reminder

A bibliography can fail silently.

Do not trust references because they look academic. Verify that they exist, that their metadata is correct, and that they are safe to use before manuscript submission.
