# AI/ML/CV Literature Database Strategies

This reference supports the `literature-review` skill.

Use it when planning source discovery, documenting search traceability, choosing databases/APIs, or deciding whether a review needs lightweight synthesis or full systematic/scoping review rigor.

For automated source discovery, use the `research-lookup` skill first.

---

## 1. Role in the Workflow

`research-lookup` is the preferred source discovery layer.

`literature-review` uses this reference to:

- design search strategies;
- document search and selection trace;
- choose appropriate databases;
- understand source strengths and limitations;
- plan systematic or scoping review searches;
- decide when additional lookup is needed.

Do not manually search every database by default. Select the smallest source set that supports the review purpose.

---

## 2. Scalable Search Strategy

Use scalable rigor.

### Lightweight Review

Use for quick source synthesis, closest-prior-work checks, introduction support, or related-work planning.

Typical source base:

- one or more `research-lookup` artifacts;
- selected papers;
- project context documents;
- citation candidates.

Expected traceability:

- query;
- backend/API;
- date;
- filters;
- saved artifact path;
- source coverage limitations.

### Formal Systematic or Scoping Review

Use only when explicitly requested or when publication expectations require it.

Expected traceability:

- protocol or review question;
- databases/APIs searched;
- exact search strings;
- date ranges;
- inclusion/exclusion criteria;
- screening log;
- deduplication;
- quality assessment;
- evidence extraction table;
- synthesis method;
- review limitations.

---

## 3. AI/ML/CV Search Question Framework

For AI and machine learning reviews, define the question using:

- **Task**: What problem is being solved?
- **Approach**: What method family, architecture, training strategy, or system type is being studied?
- **Data**: What datasets, benchmarks, domains, or environments matter?
- **Evaluation**: What metrics, baselines, constraints, or failure modes matter?
- **Findings**: What tradeoffs, gains, limitations, or open problems are being examined?

Example:

```text
How have retrieval-augmented generation methods evolved for enterprise question answering, and what tradeoffs do they show across accuracy, faithfulness, latency, and cost?
```

For biomedical, clinical, or intervention-style reviews, PICO may be used when appropriate, but it is not the default for AI/CV literature.

---

## 4. Core Literature Sources for AI/ML/CV

### OpenAlex

**Best for**:

- broad scholarly discovery;
- metadata;
- citation counts;
- DOI discovery;
- source/venue information;
- citation-network exploration.

**Use when**:

- starting broad;
- checking prior work;
- finding citation candidates;
- validating metadata.

**Limitations**:

- metadata can be incomplete;
- search relevance can drift toward highly cited broad papers;
- venue and type metadata should be verified for important claims.

---

### arXiv

**Best for**:

- recent AI/ML/CV preprints;
- fast-moving methods;
- emerging benchmark or model-release papers.

**Relevant categories**:

- `cs.CV`
- `cs.LG`
- `cs.AI`
- `cs.CL`
- `cs.RO`
- `stat.ML`

**Use when**:

- reviewing recent developments;
- looking for preprints before formal publication;
- tracking fast-moving AI/CV topics.

**Limitations**:

- not peer reviewed by default;
- API may rate-limit or timeout;
- preprints may later change or be superseded.

---

### Semantic Scholar

**Best for**:

- citation graph exploration;
- related-paper discovery;
- influential paper detection;
- finding papers connected to a seed work.

**Use when**:

- a seed paper is known;
- citation-network expansion is needed;
- related work may be missed by keyword search.

**Limitations**:

- unauthenticated API can rate-limit;
- citation influence metrics are helpful but not definitive;
- metadata still needs verification.

---

### Crossref

**Best for**:

- DOI metadata;
- publication records;
- bibliographic verification;
- journal/conference metadata.

**Use when**:

- preparing citation candidates;
- validating publication information;
- resolving DOI metadata.

**Limitations**:

- weaker for semantic discovery;
- may miss preprints or AI workshop papers.

---

### DBLP

**Best for**:

- computer science bibliographic disambiguation;
- author and venue publication history;
- conference/journal publication records.

**Use when**:

- author names are ambiguous;
- venue histories matter;
- CS bibliographic verification is needed.

**Limitations**:

- abstract/content search is limited;
- not a full semantic discovery engine.

---

### ACL Anthology

**Best for**:

- NLP;
- computational linguistics;
- language models;
- speech/language technology;
- evaluation and prompting literature.

**Use when**:

- the topic is NLP/LLM-focused.

---

### OpenReview

**Best for**:

- ICLR-style venues;
- submissions and reviews;
- workshop literature;
- review-context analysis.

**Use when**:

- understanding reviewer concerns;
- checking accepted vs submitted status;
- finding recent workshop or conference-stage work.

**Limitations**:

- distinguish accepted papers, rejected submissions, and workshop papers clearly.

---

### Papers with Code

**Best for**:

- benchmark mapping;
- dataset discovery;
- leaderboard-linked papers;
- code availability;
- baseline discovery.

**Use when**:

- experiments require standard baselines;
- benchmark context matters;
- implementation availability matters.

**Limitations**:

- leaderboard rank is not the same as scientific contribution;
- benchmark settings may vary;
- code availability does not prove reproducibility.

---

### Google Scholar

**Best for**:

- supplementary recall;
- highly cited papers;
- hard-to-locate references;
- broad cross-field discovery.

**Use when**:

- other sources miss known papers;
- manual recall expansion is needed.

**Limitations**:

- no official public API;
- metadata quality varies;
- rate limiting;
- not ideal for automated reproducibility.

---

## 5. Domain Extension Sources

Use these only when the AI/ML/CV topic extends into another scientific domain.

### Biomedical / Clinical AI

Use when the topic involves clinical ML, medical imaging, biomedical NLP, computational biology, or healthcare deployment.

Sources:

- PubMed / PubMed Central;
- bioRxiv / medRxiv;
- clinical trial registries when relevant.

Notes:

- Use MeSH when the topic is genuinely biomedical.
- Distinguish clinical evidence from model-development evidence.
- Use PRISMA, CONSORT, STROBE, QUADAS-2, GRADE, or related frameworks only when the review type requires them.

### Chemistry / Drug Discovery AI

Sources:

- ChEMBL;
- PubChem;
- CAS or domain-specific sources when available;
- relevant chemistry journals and preprints.

### Protein / Structural Biology AI

Sources:

- UniProt;
- PDB;
- AlphaFold Database;
- bioRxiv;
- domain-specific journals.

### Remote Sensing / Geospatial AI

Sources:

- IEEE Xplore;
- ISPRS;
- Remote Sensing journals;
- Earth observation dataset portals;
- benchmark pages.

### Robotics / Autonomous Driving

Sources:

- IEEE Xplore;
- ICRA/IROS;
- arXiv;
- OpenReview where relevant;
- benchmark and dataset pages.

Domain sources are extensions, not defaults for general AI/CV review.

---

## 6. Search Term Development

### Primary Concepts

Identify 2–4 main concepts.

Example for road damage detection:

- road damage / pavement distress / road crack;
- object detection / segmentation / YOLO;
- benchmark / dataset / mAP;
- domain shift / weather / camera variation.

Example for RAG:

- retrieval-augmented generation / grounded generation;
- question answering / enterprise QA;
- faithfulness / hallucination / citation grounding;
- latency / cost / retrieval quality.

### Synonyms and Variants

Include:

- acronyms;
- dataset names;
- method family names;
- benchmark names;
- common spelling variations;
- application-domain synonyms.

### Boolean Strategy

Use Boolean search when a database supports it.

```text
("road damage" OR "pavement distress" OR "road crack")
AND ("object detection" OR YOLO OR segmentation)
AND (benchmark OR dataset OR mAP)
```

### Fielded Search

Use title/abstract fields when broad search drifts.

Examples:

```text
title:"road damage" AND YOLO
```

```text
abs:"domain shift" AND "computer vision"
```

---

## 7. Search Execution Workflow

### Phase 1: Pilot Search

1. Run a broad lookup with `research-lookup`.
2. Inspect top results for relevance drift.
3. Identify better synonyms, datasets, venues, and method terms.
4. Refine query and filters.

### Phase 2: Focused Search

1. Search with refined terms.
2. Use mode-specific lookup:
   - `prior-work`
   - `baseline-scout`
   - `dataset-benchmark`
   - `citation-candidates`
   - `recent-developments`
3. Save artifacts under `sources/`.

### Phase 3: Expansion

Use when more coverage is needed:

- forward citation search;
- backward citation search;
- related-paper search;
- dataset/benchmark page search;
- author or group search;
- venue-specific search.

### Phase 4: Screening

Screen sources by:

- task relevance;
- method relevance;
- dataset/benchmark relevance;
- evaluation relevance;
- claim support relevance;
- full-text availability when needed.

### Phase 5: Synthesis

Move from search to `literature-review`.

Synthesize by:

- themes;
- method families;
- closest prior work;
- baselines;
- datasets;
- evaluation protocols;
- gaps;
- claim support.

---

## 8. Citation Chaining

### Backward Citation Search

Use references of key papers to find foundational work.

Good for:

- seminal methods;
- original dataset papers;
- metric definitions;
- historical context.

### Forward Citation Search

Use citing papers to find follow-up work.

Good for:

- newer improvements;
- criticism or limitations;
- benchmark updates;
- related applications.

### Seed Paper Expansion

Start with 3–5 high-relevance seed papers.

Expand through:

- cited references;
- citing papers;
- related papers;
- papers using the same dataset;
- papers comparing against the same baseline.

Do not expand indefinitely. Stop when the review purpose is satisfied.

---

## 9. Quality and Relevance Assessment

Quality is not only venue rank or citation count.

For AI/ML/CV literature, assess:

- task match;
- dataset relevance;
- baseline fairness;
- ablation quality;
- metric alignment;
- reproducibility;
- code/config availability;
- leakage risk;
- domain-shift handling;
- compute disclosure;
- clarity of limitations;
- follow-up influence.

### Venue and Citation Signals

Venue and citation count are useful signals, but not sufficient.

Prefer:

- directly relevant papers over famous but tangential papers;
- fair baselines over impressive numbers;
- reproducible protocols over vague claims;
- source-specific relevance over generic surveys.

### Common Strong AI/ML/CV Venues

Examples include:

- CVPR, ICCV, ECCV, WACV, BMVC;
- NeurIPS, ICML, ICLR, AISTATS, UAI;
- ACL, EMNLP, NAACL;
- KDD, WWW, SIGIR;
- ICRA, IROS, CoRL;
- JMLR, TMLR, TPAMI, IJCV, JAIR.

Venue lists should guide review, not replace relevance judgment.

---

## 10. Inclusion and Exclusion Criteria

Use explicit criteria for substantial reviews.

### Possible Inclusion Criteria

- directly relevant task;
- relevant method family;
- relevant dataset or benchmark;
- relevant evaluation protocol;
- publication year range;
- peer-reviewed or preprint depending on review goal;
- full text available;
- empirical evidence provided;
- benchmark or dataset paper.

### Possible Exclusion Criteria

- unrelated task/domain;
- no method or evaluation details;
- opinion-only article;
- duplicate or superseded version;
- benchmark setting incompatible with review goal;
- no accessible metadata;
- weakly relevant application-only paper;
- source does not support intended claim.

---

## 11. Search Documentation Template

Use this for traceable reviews.

```markdown
## Search Strategy

### Query 1
- Source: research-lookup / OpenAlex / arXiv / Semantic Scholar / other
- Date searched: YYYY-MM-DD
- Query:
  ```text
  [query]
  ```
- Filters:
  - year:
  - quality:
  - venue:
  - boost phrases:
- Results saved to: `sources/...md`
- Notes:
  - [coverage or relevance notes]

### Query 2
...
```

---

## 12. Common Pitfalls

### Search Drift

Problem:

- broad APIs return high-citation but irrelevant papers.

Mitigation:

- refine query;
- use title/abstract terms;
- add synonyms;
- use `--boost-phrase` in `research-lookup`;
- inspect top results before synthesis.

### Single-Database Bias

Problem:

- one source misses important papers.

Mitigation:

- combine OpenAlex, arXiv, Semantic Scholar, Crossref, DBLP, ACL Anthology, or Papers with Code depending on the task.

### Preprint Overconfidence

Problem:

- arXiv results are treated as established findings.

Mitigation:

- label preprints clearly;
- check for published versions;
- use cautious wording.

### Venue Prestige Bias

Problem:

- famous venues dominate despite weak task relevance.

Mitigation:

- prioritize relevance, evaluation match, and evidence quality.

### Leaderboard Bias

Problem:

- benchmark rank is mistaken for scientific contribution.

Mitigation:

- inspect protocol, baselines, compute, data, and ablations.

### Dataset Leakage Blindness

Problem:

- prior results are trusted without checking split or contamination risks.

Mitigation:

- extract split policy, dataset construction, and evaluation protocol.

### Citation Metadata Errors

Problem:

- metadata from APIs or LLM summaries is incomplete or wrong.

Mitigation:

- use `citation-management` for final reference hygiene.

---

## 13. Handoff to Literature Review

After search, prepare:

- source artifact paths;
- query strings;
- filters;
- inclusion/exclusion notes;
- strongest sources;
- suspected gaps;
- unresolved coverage issues.

Then use `literature-review` to synthesize.

---

## Final Checklist

Before completing a search strategy, check:

- [ ] review purpose is clear;
- [ ] search terms include synonyms and variants;
- [ ] source choice fits the domain and task;
- [ ] search trace is documented;
- [ ] inclusion/exclusion logic is stated;
- [ ] source coverage limitations are visible;
- [ ] high-relevance sources are prioritized over merely high-citation sources;
- [ ] preprints and peer-reviewed sources are distinguished;
- [ ] dataset, benchmark, and metric sources are captured when relevant;
- [ ] next synthesis step is clear.
