---
name: citation-management
description: Use for reference verification, BibTeX cleanup, DOI/arXiv metadata repair, duplicate detection, citation-key hygiene, LaTeX citation checks, and hallucinated-reference cleanup. Best used after research-lookup or literature-review has identified candidate sources, or before finalizing manuscript references. For source discovery use research-lookup. For claim support auditing use claim-auditor.
---

# Citation Management

## Overview

Citation management is the reference integrity layer of the research workflow.

Use this skill to verify that references exist, metadata is correct, BibTeX entries are valid, citation keys are consistent, duplicates are removed, and AI-generated or hallucinated references are detected and cleaned.

This skill should make the bibliography auditable and safe for manuscript use.

It should not be used as the primary source-discovery skill. Use `research-lookup` to find candidate sources, then use this skill to verify, clean, normalize, and maintain the references.

---

## Core Responsibility

This skill answers:

- Does this reference exist?
- Is the title correct?
- Are authors, year, venue, DOI, arXiv ID, and URL correct?
- Is the reference duplicated under multiple citation keys?
- Is the citation key stable and meaningful?
- Is the BibTeX entry valid?
- Is a preprint incorrectly described as peer-reviewed?
- Is an AI-generated reference hallucinated?
- Are manuscript citation commands pointing to valid bibliography entries?
- Are bibliography entries unused or missing?
- Is a reference metadata issue serious enough to block manuscript use?

This skill verifies reference reality and metadata quality.

For whether a source supports a manuscript claim, use `claim-auditor`.

---

## Relationship to Other Skills

Use the smallest relevant skill combination.

| Need | Use |
|---|---|
| Find papers, datasets, benchmarks, or citation candidates | `research-lookup` |
| Synthesize sources into themes, gaps, and paper context | `literature-review` |
| Verify references and clean bibliography metadata | `citation-management` |
| Draft or revise manuscript prose | `scientific-writing` |
| Check whether claims are supported by evidence | `claim-auditor` |
| Critique methodology, novelty, or experiment design | `scientific-critical-thinking` |
| Reviewer-style critique | `peer-review` |

Recommended citation workflow:

```text
research-lookup
    → literature-review
    → citation-management
    → scientific-writing
    → claim-auditor
```

For final manuscript cleanup:

```text
paper/*.tex + paper/*.bib
    → citation-management
    → claim-auditor
```

---

## When to Use This Skill

Use this skill when:

- cleaning `.bib` files;
- validating DOI, arXiv, URL, venue, author, or year metadata;
- checking whether references actually exist;
- removing duplicate BibTeX entries;
- normalizing citation keys;
- checking LaTeX citation commands against bibliography entries;
- detecting unused or missing references;
- converting DOI, arXiv, or metadata records into BibTeX;
- checking AI-generated references for hallucinations;
- preparing references before submission;
- changing venue or citation style;
- repairing references after paper drafting;
- validating citation candidates from `research-lookup`;
- cleaning citations after `literature-review`;
- checking suspicious references created by an AI writing assistant.

Do not use this skill as the primary tool for:

- broad literature discovery; use `research-lookup`;
- literature synthesis; use `literature-review`;
- manuscript prose generation; use `scientific-writing`;
- claim-evidence auditing; use `claim-auditor`;
- reviewer-style critique; use `peer-review`;
- visual artifacts; use `scientific-schematics` or `generate-image`.

---

## Relationship to Research Gates

This skill supports the following gates in `docs/research_gates.md`:

- Claim Support Gate
- Paper Writing Gate
- Red-Team Review Gate
- Final Handoff Gate

Use this skill before finalizing manuscript sections that contain citations, especially introduction, related work, method background, results comparison, discussion, and conclusion.

A clean reference does not prove that the source supports a claim. It only proves that the reference metadata is valid enough to use. Use `claim-auditor` for claim support.

---

## Active Inputs

This skill may operate on:

- `paper/*.tex`;
- `paper/*.bib`;
- `references.bib`;
- `paper/references.bib`;
- `sources/*.md`;
- `sources/*.json`;
- literature-review outputs;
- citation candidate tables;
- AI-generated drafts;
- DOI lists;
- arXiv ID lists;
- manually pasted references.

When editing bibliography files, keep changes small, reviewable, and traceable.

---

## Citation Management Modes

Choose the smallest mode that fits the task.

---

### 1. Reference Verification

Use when checking whether references exist and metadata is correct.

Check:

1. title;
2. authors;
3. year;
4. venue or source;
5. DOI;
6. arXiv ID;
7. URL;
8. publication type;
9. preprint versus peer-reviewed status;
10. whether the reference is the intended work.

Classify each reference as:

- `verified`;
- `corrected`;
- `metadata incomplete`;
- `needs manual check`;
- `not found`;
- `hallucinated`.

Do not silently keep unverifiable references.

---

### 2. Hallucinated Reference Cleanup

Use when references may have been generated or modified by AI.

AI-generated references often look plausible but may be fake, mixed, or mismatched.

Check each suspicious reference for:

1. whether the paper exists;
2. whether title, authors, year, venue, DOI, arXiv ID, and URL match;
3. whether the citation key points to the correct work;
4. whether the source is a journal article, conference paper, workshop paper, preprint, dataset, software artifact, or webpage;
5. whether a preprint is incorrectly described as peer-reviewed;
6. whether two references are duplicates or near-duplicates;
7. whether the cited work is unrelated to the nearby manuscript citation context.

Classify each reference as:

- `verified`;
- `corrected`;
- `duplicate`;
- `metadata incomplete`;
- `needs manual check`;
- `hallucinated`;
- `wrong citation for claim`.

For hallucinated references:

- do not silently keep them;
- remove them only when requested or when the task explicitly includes cleanup;
- otherwise mark them as `HALLUCINATED_REFERENCE`;
- suggest a real replacement only if a verified source exists;
- never invent a replacement citation.

A possible report format:

```md
| Citation key | Status | Problem | Correction / action |
|---|---|---|---|
| smith2024road | hallucinated | no matching title/DOI found | remove or replace after research-lookup |
| wang2025rdd | corrected | DOI mismatch | update DOI |
| yolo2024survey | verified | metadata matches | keep |
```

---

### 3. BibTeX Cleanup

Use when cleaning `.bib` files.

Check:

1. valid BibTeX syntax;
2. required fields for each entry type;
3. consistent casing;
4. protected capitalization for model names, datasets, acronyms, and proper nouns;
5. duplicate entries;
6. missing DOI, arXiv, URL, or venue fields;
7. invalid characters;
8. broken braces;
9. inconsistent entry types;
10. unnecessary fields.

Common fixes:

- normalize entry types;
- fix title capitalization while preserving acronyms;
- standardize author formatting;
- add missing DOI/arXiv/URL when verified;
- remove duplicate fields;
- merge duplicate entries;
- normalize venue names;
- sort entries when useful;
- preserve comments only when they are meaningful.

Do not alter scientific meaning while formatting.

---

### 4. DOI / arXiv / Metadata Completion

Use when a reference has partial metadata.

Sources to check, depending on the identifier:

- DOI resolver;
- Crossref;
- OpenAlex;
- arXiv;
- Semantic Scholar;
- DBLP;
- ACL Anthology;
- official publisher pages;
- dataset/model/software pages.

Metadata completion should be source-backed.

If metadata cannot be verified, mark it as `needs manual check`.

Do not guess missing metadata.

---

### 5. Duplicate Detection

Use when a bibliography may contain repeated entries.

Duplicates may differ by:

- citation key;
- title casing;
- author abbreviation;
- arXiv versus published version;
- conference versus journal extension;
- DOI formatting;
- preprint and accepted version.

Classify duplicates as:

- exact duplicate;
- same work with different metadata;
- preprint and published version;
- related but distinct works;
- unclear.

When merging duplicates:

1. preserve the best verified metadata;
2. update citation keys in manuscript files if needed;
3. avoid breaking existing citations;
4. record changed keys.

---

### 6. Citation Key Normalization

Use when citation keys are inconsistent or unstable.

Good citation keys are:

- readable;
- stable;
- unique;
- short enough for LaTeX;
- based on first author, year, and keyword.

Examples:

```bibtex
@article{wang2025roadDamage,
@inproceedings{redmon2016yolo,
@article{dosovitskiy2021vit,
@inproceedings{lin2014coco,
```

Avoid:

- random keys;
- keys generated from full titles;
- keys that change after minor metadata edits;
- duplicate keys;
- keys with spaces or special characters;
- misleading keys that point to the wrong paper.

When changing keys, update all manuscript citation commands.

---

### 7. LaTeX Citation Hygiene

Use when checking `paper/*.tex` citation commands.

Check:

1. every `\\cite{...}`, `\\citep{...}`, `\\citet{...}`, `\\autocite{...}`, or related command resolves to a `.bib` entry;
2. every `.bib` entry is either cited or intentionally retained;
3. citation keys are not duplicated;
4. citation commands use the correct keys;
5. removed references do not leave broken citations;
6. multi-citation commands are valid;
7. bibliography file path is correct;
8. citation package style matches the template.

Report:

- missing keys;
- unused entries;
- duplicate keys;
- suspicious citations;
- keys needing rename;
- references needing metadata verification.

---

### 8. Venue / Style Readiness

Use before submission or when changing venue.

Check:

1. required bibliography style;
2. numeric versus author-year citations;
3. conference/journal naming convention;
4. arXiv/preprint handling;
5. DOI/URL policy;
6. page or article-number formatting;
7. capitalization conventions;
8. max reference count if applicable;
9. venue-specific requirements.

Use `venue-templates` when the target venue has specific formatting rules.

Do not overfit references to a venue before the target venue is known.

---

## Hallucinated Reference Warning Signs

Flag references that show any of the following:

- title cannot be found in Crossref, OpenAlex, arXiv, Semantic Scholar, DBLP, or publisher pages;
- DOI resolves to a different title;
- authors do not match the title;
- year does not match the publication record;
- venue does not exist or is implausible;
- conference name is wrong for the year;
- arXiv ID is malformed or points to a different paper;
- paper title sounds plausible but has no search footprint;
- citation key appears in text but not in `.bib`;
- bibliography entry exists but is unrelated to the manuscript sentence;
- source is a preprint but manuscript calls it a peer-reviewed article;
- multiple real papers appear blended into one fake citation.

When uncertain, classify as `needs manual check`, not verified.

---

## Reference Status Labels

Use these labels consistently.

| Status | Meaning | Action |
|---|---|---|
| `verified` | Metadata matches a reliable source | Keep |
| `corrected` | Metadata had errors and was fixed | Keep with correction note |
| `duplicate` | Same or near-same work appears more than once | Merge or remove duplicate |
| `metadata incomplete` | Exists but important metadata is missing | Complete if possible |
| `needs manual check` | Could not verify confidently | Do not use for strong claims yet |
| `hallucinated` | No credible evidence that reference exists | Remove or mark |
| `wrong citation for claim` | Reference exists but does not support local claim | Send to `claim-auditor` or replace after lookup |
| `preprint only` | Exists only as preprint | Do not describe as peer-reviewed |
| `superseded` | Better published or newer version exists | Consider replacing or noting version |

---

## Evidence Sources for Verification

Prefer authoritative or structured sources:

1. DOI resolver / publisher page;
2. Crossref;
3. OpenAlex;
4. arXiv;
5. Semantic Scholar;
6. DBLP;
7. ACL Anthology;
8. PubMed, only for biomedical/clinical sources;
9. official dataset/model/software pages;
10. saved `sources/*.md` or `sources/*.json` lookup artifacts.

Avoid relying only on:

- LLM-generated citation text;
- unsourced manuscript prose;
- copied references from unknown documents;
- incomplete Google Scholar snippets;
- citation strings with no stable identifier.

---

## Active Scripts and Utilities

Use helper scripts only when relevant.

Likely active utilities include:

- `scripts/doi_to_bibtex.py`
- `scripts/extract_metadata.py`
- `scripts/format_bibtex.py`
- `scripts/validate_citations.py`

Use these for:

- DOI-to-BibTeX conversion;
- metadata extraction;
- BibTeX formatting;
- citation validation.

Legacy search utilities, if present under `scripts/legacy/`, should not be used by default.

Source discovery belongs to `research-lookup`.

---

## Assets and References

This skill may include:

- `assets/bibtex_template.bib`
- `assets/citation_checklist.md`
- `references/bibtex_formatting.md`
- `references/citation_validation.md`
- `references/metadata_extraction.md`

Domain-specific or legacy search references, if present, should be treated as optional background and not as the default workflow.

---

## Output Formats

Choose the smallest useful output.

---

### Reference Verification Report

```md
## Reference Verification Report

### Scope

- Files checked:
- Sources used:
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

### Findings

| Citation key | Status | Issue | Action |
|---|---|---|---|
| [key] | [status] | [issue] | [action] |

### Remaining Risks

### Next Step
```

---

### Hallucinated Reference Cleanup Report

```md
## Hallucinated Reference Cleanup Report

### Scope

- File(s):
- Suspected source of references:
- Verification sources:

### Findings

| Citation key | Status | Evidence checked | Action |
|---|---|---|---|
| [key] | hallucinated | no DOI/arXiv/OpenAlex/Crossref match | remove or replace after lookup |

### References Marked for Removal

### Real Replacement Candidates

### Needs Manual Check

### Next Step
```

---

### BibTeX Cleanup Report

```md
## BibTeX Cleanup Report

### Files Changed

### Corrections Made

| Citation key | Change | Reason |
|---|---|---|
| [key] | [change] | [reason] |

### Duplicate Handling

### Missing Metadata

### Citation Key Changes

### Validation Result
```

---

### LaTeX Citation Hygiene Report

```md
## LaTeX Citation Hygiene Report

### Files Checked

### Missing Citation Keys

### Unused Bibliography Entries

### Duplicate Keys

### Suspicious Citation Contexts

### Recommended Fixes
```

---

## Editing Rules

When editing references:

- make minimal, traceable changes;
- preserve existing citation keys unless key cleanup is requested;
- if changing keys, update all LaTeX citations;
- never fabricate missing metadata;
- prefer verified metadata over memory;
- preserve capitalization for acronyms and proper nouns;
- do not silently remove references unless the task explicitly requests cleanup;
- report uncertain references;
- keep source URLs, DOI, or arXiv IDs when useful;
- separate metadata cleanup from claim support auditing.

---

## Quality Checklist

Before finalizing citation-management work, check:

1. [ ] Scope is clear.
2. [ ] Files checked are listed.
3. [ ] Verification sources are stated.
4. [ ] Hallucinated references are flagged.
5. [ ] DOI/arXiv/URL metadata is verified where possible.
6. [ ] BibTeX syntax is valid.
7. [ ] Duplicate keys and duplicate works are handled.
8. [ ] Citation keys are stable and consistent.
9. [ ] LaTeX citation commands resolve.
10. [ ] Preprints are not mislabeled as peer-reviewed papers.
11. [ ] Unverified references are marked as `needs manual check`.
12. [ ] Claim-support issues are handed off to `claim-auditor`.
13. [ ] Source discovery gaps are handed off to `research-lookup`.
14. [ ] Any file edits are summarized.

---

## Final Reminder

Citation management protects the bibliography from silent corruption.

A reference can be:

- real but incorrectly formatted;
- correctly formatted but unrelated to the claim;
- real but duplicated;
- real as a preprint but mislabeled as peer reviewed;
- plausible-looking but hallucinated.

Do not reward citation fluency. Verify reference reality.
