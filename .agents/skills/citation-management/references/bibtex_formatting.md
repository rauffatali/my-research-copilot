# BibTeX Formatting Reference

This reference supports the `citation-management` skill.

Use it when formatting, normalizing, and cleaning BibTeX entries for AI/ML/CV research projects.

For source discovery, use `research-lookup`.  
For metadata verification, use `citation_validation.md` and `metadata_extraction.md`.  
For checking whether a cited source supports a manuscript claim, use `claim-auditor`.

---

## 1. Purpose

BibTeX formatting ensures that references are syntactically valid, readable, consistent, and compatible with LaTeX manuscript workflows.

Formatting should not change scientific meaning.

Do not use formatting as a substitute for metadata verification. A clean BibTeX entry can still be fake, wrong, duplicated, or unrelated to the cited claim.

---

## 2. General Formatting Principles

Good BibTeX entries should be:

- syntactically valid;
- consistently indented;
- easy to inspect;
- minimally but sufficiently complete;
- source-backed;
- stable across manuscript revisions;
- compatible with the target venue or template.

Recommended style:

```bibtex
@inproceedings{redmon2016yolo,
  author    = {Redmon, Joseph and Divvala, Santosh and Girshick, Ross and Farhadi, Ali},
  title     = {You Only Look Once: Unified, Real-Time Object Detection},
  booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2016},
  pages     = {779--788},
  doi       = {10.1109/CVPR.2016.91}
}
```

Use:

- two-space indentation;
- aligned fields when convenient;
- one field per line;
- braces around field values;
- stable citation keys;
- no duplicate fields.

---

## 3. Entry Type Selection

Choose the entry type based on the real source type.

| Source type | Preferred BibTeX type |
|---|---|
| Journal article | `@article` |
| Conference paper | `@inproceedings` |
| Workshop paper | `@inproceedings` or `@misc` |
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

If the target BibTeX processor does not support `@software` or `@dataset`, use `@misc` with clear `note`, `url`, `version`, and access date.

---

## 4. Required and Recommended Fields

### Journal Article

```bibtex
@article{key,
  author  = {...},
  title   = {...},
  journal = {...},
  year    = {...},
  volume  = {...},
  number  = {...},
  pages   = {...},
  doi     = {...}
}
```

Required in practice:

- `author`
- `title`
- `journal`
- `year`

Recommended when available:

- `volume`
- `number`
- `pages` or article number
- `doi`
- `url`

---

### Conference Paper

```bibtex
@inproceedings{key,
  author    = {...},
  title     = {...},
  booktitle = {...},
  year      = {...},
  pages     = {...},
  doi       = {...}
}
```

Required in practice:

- `author`
- `title`
- `booktitle`
- `year`

Recommended when available:

- `pages`
- `doi`
- `url`

---

### arXiv Preprint

```bibtex
@misc{key,
  author        = {...},
  title         = {...},
  year          = {...},
  eprint        = {...},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV},
  url           = {https://arxiv.org/abs/...},
  note          = {arXiv preprint}
}
```

Required in practice:

- `author`
- `title`
- `year`
- `eprint`
- `archivePrefix`

Recommended:

- `primaryClass`
- `url`
- `note`

Do not label as journal or conference unless a published version is verified.

---

### Dataset Page

```bibtex
@misc{key,
  author = {{Dataset Maintainers}},
  title  = {{DatasetName}: Dataset and Benchmark},
  year   = {2024},
  url    = {https://example.org/dataset},
  note   = {Dataset, version 1.0. Accessed 2026-05-22}
}
```

Include:

- dataset name;
- maintainers or organization;
- year or date;
- version if available;
- URL or DOI;
- access date for dynamic pages.

---

### Software Repository

```bibtex
@software{key,
  author  = {{Software Authors or Organization}},
  title   = {{SoftwareName}: Description},
  year    = {2024},
  version = {1.2.0},
  url     = {https://github.com/example/project},
  note    = {Software repository. Accessed 2026-05-22}
}
```

If `@software` is unsupported:

```bibtex
@misc{key,
  author = {{Software Authors or Organization}},
  title  = {{SoftwareName}: Description},
  year   = {2024},
  url    = {https://github.com/example/project},
  note   = {Software, version 1.2.0. Accessed 2026-05-22}
}
```

---

### Model Card or Model Release

```bibtex
@misc{key,
  author = {{Model Team or Organization}},
  title  = {{ModelName}: Model Card and Release Notes},
  year   = {2025},
  url    = {https://example.org/model},
  note   = {Model card. Accessed 2026-05-22}
}
```

---

### Benchmark Leaderboard

```bibtex
@misc{key,
  author = {{Benchmark Maintainers}},
  title  = {{BenchmarkName} Leaderboard},
  year   = {2025},
  url    = {https://example.org/benchmark},
  note   = {Benchmark leaderboard. Accessed 2026-05-22}
}
```

Do not cite a leaderboard as if it were a peer-reviewed paper.

---

## 5. Citation Key Formatting

Good citation keys are:

- unique;
- readable;
- stable;
- short enough for LaTeX;
- based on first author, year, and a keyword.

Recommended pattern:

```text
firstAuthorYearKeyword
```

Examples:

```bibtex
redmon2016yolo
he2016resnet
lin2014coco
dosovitskiy2021vit
kirillov2023sam
example2025method
```

Avoid:

- random IDs;
- full titles;
- spaces;
- special characters;
- duplicate keys;
- misleading keys;
- keys that change unnecessarily.

When changing keys:

1. update all manuscript `.tex` citations;
2. record old key to new key mapping;
3. validate no citation commands are broken.

---

## 6. Author Formatting

BibTeX authors should be separated by `and`.

Good:

```bibtex
author = {Redmon, Joseph and Divvala, Santosh and Girshick, Ross and Farhadi, Ali}
```

Organization author:

```bibtex
author = {{Example Benchmark Maintainers}}
```

Use double braces for organizations so BibTeX does not parse them as personal names.

Avoid:

```bibtex
author = {Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi}
```

Avoid `et al.` in BibTeX author fields unless a venue or style explicitly requires it.

---

## 7. Title Capitalization and Protected Terms

BibTeX styles may lowercase titles. Protect acronyms, model names, dataset names, and proper nouns with braces.

Examples:

```bibtex
title = {{YOLO}: You Only Look Once}
title = {{Microsoft COCO}: Common Objects in Context}
title = {An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale}
title = {{BDD100K}: A Diverse Driving Dataset}
```

Common AI/ML/CV protected terms:

```text
{AI}
{ML}
{CNN}
{R-CNN}
{Faster R-CNN}
{YOLO}
{DETR}
{ViT}
{CLIP}
{SAM}
{COCO}
{ImageNet}
{Cityscapes}
{BDD100K}
{mAP}
{IoU}
{AP50}
{AP75}
```

Do not over-brace entire titles unless required. Prefer protecting only terms that must retain capitalization.

---

## 8. DOI Formatting

Prefer DOI without URL prefix in the `doi` field:

```bibtex
doi = {10.1109/CVPR.2016.91}
```

Avoid:

```bibtex
doi = {https://doi.org/10.1109/CVPR.2016.91}
doi = {doi:10.1109/CVPR.2016.91}
```

If useful, include DOI URL separately:

```bibtex
url = {https://doi.org/10.1109/CVPR.2016.91}
```

Always verify that the DOI resolves to the same work.

---

## 9. URL Formatting

Use URLs for:

- arXiv preprints;
- dataset pages;
- software repositories;
- model cards;
- benchmark pages;
- documentation;
- technical reports;
- official project pages.

Example:

```bibtex
url = {https://arxiv.org/abs/2304.02643}
```

For dynamic pages, include access date in `note`:

```bibtex
note = {Documentation. Accessed 2026-05-22}
```

Avoid citing unstable or unofficial URLs when DOI, publisher, or archival URLs are available.

---

## 10. arXiv Formatting

Recommended:

```bibtex
@misc{key,
  author        = {...},
  title         = {...},
  year          = {...},
  eprint        = {2304.02643},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV},
  url           = {https://arxiv.org/abs/2304.02643},
  note          = {arXiv preprint}
}
```

If the paper has a verified published version, prefer the published citation unless the arXiv version is specifically relevant.

Do not keep duplicate arXiv and published entries unless there is a reason.

---

## 11. Venue Formatting

Use full venue names unless the target venue prefers abbreviations.

Conference examples:

```bibtex
booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}
booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)}
booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)}
booktitle = {Advances in Neural Information Processing Systems (NeurIPS)}
booktitle = {International Conference on Learning Representations (ICLR)}
booktitle = {International Conference on Machine Learning (ICML)}
```

Journal examples:

```bibtex
journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence}
journal = {International Journal of Computer Vision}
journal = {Journal of Machine Learning Research}
journal = {Transactions on Machine Learning Research}
```

Distinguish:

- main conference vs workshop;
- journal article vs preprint;
- proceedings paper vs technical report;
- dataset page vs dataset paper.

---

## 12. Page, Article Number, and Volume Formatting

Page ranges:

```bibtex
pages = {779--788}
```

Use double hyphen `--`.

Article number:

```bibtex
pages = {112618}
```

or if the style supports it:

```bibtex
articleno = {112618}
```

Use the format required by the target venue or BibTeX style.

---

## 13. Special Characters and LaTeX Escaping

Escape characters that can break BibTeX or LaTeX.

Common cases:

| Character | Escape |
|---|---|
| `&` | `\\&` |
| `%` | `\\%` |
| `_` | `\\_` |
| `#` | `\\#` |
| `$` | `\\$` |

Accents may be represented with LaTeX commands when needed:

```bibtex
Doll{\\'a}r, Piotr
```

Do not over-escape URLs; most BibTeX styles handle URL fields.

---

## 14. Sorting and Organization

Sort entries when useful, but do not prioritize sorting over correctness.

Common sorting options:

- citation key alphabetical;
- first author/year;
- cited order, if managed by style;
- grouped by source type for maintenance.

For active manuscripts, key alphabetical sorting is usually easiest to maintain.

---

## 15. Duplicate Formatting

When duplicate entries exist:

1. verify which entry has better metadata;
2. merge fields carefully;
3. keep one citation key;
4. update manuscript citations if keys change;
5. remove duplicate entry;
6. record the merge.

Do not merge:

- preprint and journal extension if they are meaningfully different;
- conference and extended journal version if both are cited for distinct reasons;
- dataset paper and dataset page if both are needed.

---

## 16. Comments and Notes

Use comments sparingly.

Useful comments:

```bibtex
% Verified against Crossref on 2026-05-22.
% Published version of arXiv:2304.02643 not found as of 2026-05-22.
```

Avoid clutter:

```bibtex
% cool paper
% maybe useful
% added by AI
```

For uncertain references, prefer a cleanup report rather than hiding uncertainty in comments.

---

## 17. Hallucinated Reference Formatting

Do not try to make hallucinated references look clean.

If a reference is suspicious and cannot be verified:

- mark it in a report;
- label it as `needs manual check` or `hallucinated`;
- remove it only when requested;
- do not fabricate missing fields.

Temporary marker example:

```bibtex
@misc{smith2024fakeReference,
  title = {HALLUCINATED_REFERENCE: Unverified AI-generated reference},
  note  = {No reliable metadata found. Do not use in manuscript.}
}
```

Use this only as a temporary marker if removal is not yet allowed.

---

## 18. Formatting Workflow

Recommended workflow:

1. Parse `.bib` file.
2. Detect duplicate keys.
3. Detect duplicate works.
4. Validate DOI/arXiv/URL metadata where possible.
5. Correct entry types.
6. Normalize citation keys if requested.
7. Protect acronyms and proper nouns.
8. Normalize DOI and URL fields.
9. Remove duplicate fields.
10. Validate LaTeX citation commands.
11. Produce a cleanup report.

Do not start with cosmetic formatting if reference reality is uncertain.

---

## 19. Common Anti-Patterns

Avoid:

```bibtex
@article{unknown2024,
  title={A Novel Method for Computer Vision},
  author={Smith et al.},
  journal={International Journal of AI},
  year={2024}
}
```

Problems:

- vague title;
- incomplete author list;
- possibly fake venue;
- no DOI/URL/arXiv;
- likely hallucinated.

Avoid:

```bibtex
doi = {https://doi.org/...}
```

Prefer:

```bibtex
doi = {...}
```

Avoid:

```bibtex
author = {Example Research Team}
```

Prefer:

```bibtex
author = {{Example Research Team}}
```

Avoid:

```bibtex
title = {Yolo based object detection on coco}
```

Prefer:

```bibtex
title = {{YOLO}-Based Object Detection on {COCO}}
```

---

## 20. Final Formatting Checklist

Before finalizing:

- [ ] BibTeX syntax is valid.
- [ ] Entry types match source types.
- [ ] Required fields are present.
- [ ] DOI fields are normalized.
- [ ] arXiv fields are normalized.
- [ ] URLs are stable and useful.
- [ ] Access dates are included for dynamic web sources when needed.
- [ ] Author names are correctly formatted.
- [ ] Organization authors use double braces.
- [ ] Acronyms/model/dataset names are protected.
- [ ] Venue names are consistent.
- [ ] Page ranges use `--`.
- [ ] Duplicate keys are removed.
- [ ] Duplicate works are handled.
- [ ] Citation keys are stable.
- [ ] LaTeX citations resolve.
- [ ] Hallucinated or unverified references are not silently kept.
- [ ] Any key changes are reported.

---

## Final Reminder

BibTeX formatting should make verified references cleaner.

It should never make unverified, hallucinated, or mismatched references look trustworthy.
