---
name: research-lookup
description: Use for targeted external research lookup, prior-work discovery, baseline scouting, dataset/benchmark lookup, citation candidate discovery, local Zotero library discovery, and verification of scientific or technical claims. Best for finding and saving source material before literature review, peer review, claim auditing, experiment planning, or paper writing. For synthesis across papers use literature-review. For BibTeX and citation hygiene use citation-management.
---

# Research Lookup

## Overview

Research lookup is the targeted discovery of external evidence.

Use this skill to find papers, methods, datasets, benchmarks, baselines, technical documentation, citation candidates, and recent developments relevant to a specific research task.

For this repository, the skill should support AI/ML and computer vision research workflows. It should help agents avoid shallow novelty claims, weak baselines, outdated comparisons, unsupported citations, and reviewer-sensitive omissions.

This skill is primarily for **search and source discovery**.

It also serves as the repo's primary path for working with a local Zotero library when the user's references live there instead of in a web source.

It should not replace:

- `literature-review` for synthesis and research mapping;
- `citation-management` for BibTeX, DOI resolution, and reference hygiene;
- `claim-auditor` for checking manuscript claims against repository evidence;
- `peer-review` for reviewer-style critique;
- `scientific-critical-thinking` for adversarial methodology critique.

When a task involves a local Zotero library, use this skill as the entry point for discovery, search, export, or import routing. Keep `citation-management` for BibTeX metadata cleanup, DOI verification, and reference hygiene after source discovery.

---

## Automation-First Backend Strategy

Research lookup should prefer structured, automatable APIs when available.

For paper discovery, citation candidate lookup, baseline scouting, dataset lookup, benchmark lookup, and external claim verification, use scholarly metadata APIs before general web search when possible.

The goal is not only to find sources, but to preserve source metadata so later agents can audit, synthesize, cite, and reuse the results.

Preferred backend order for paper-oriented lookup:

1. **OpenAlex**
   - Use for broad scholarly discovery across works, authors, venues, institutions, concepts, and topics.
   - Good default for initial paper search, research mapping, and broad prior-work discovery.

2. **Semantic Scholar**
   - Use for citation graph exploration, related papers, influential papers, and paper metadata.
   - Good when starting from a known seed paper or when looking for closest related work.

3. **arXiv**
   - Use for recent AI/ML/CV preprints and arXiv IDs.
   - Good for fast-moving areas where papers may not yet have DOI, venue, or indexed metadata.

4. **Crossref**
   - Use for DOI metadata, publication metadata, and bibliographic cleanup.
   - Good for verifying citation records and filling missing metadata.

5. **Perplexity, Parallel API, or general web search**
   - Use as a supplement or fallback for recent web context, benchmark pages, official project pages, model releases, blogs, documentation, and synthesis across non-paper sources.
   - Do not rely on LLM-generated summaries as final evidence.

For each lookup, preserve as much structured metadata as possible:

- query;
- backend;
- timestamp;
- title;
- authors;
- year or date;
- venue or source;
- URL;
- DOI, arXiv ID, or other identifier;
- abstract or snippet;
- citation count when available;
- relevance note;
- uncertainty or missing metadata.

Do not treat API output as automatically correct. APIs may have incomplete records, duplicate entries, stale metadata, or missing venue information.

---

## Recommended Free Paper Search Backend

When implementing or improving this skill, prefer a free scholarly search stack:

1. **OpenAlex** as the default broad paper discovery API.
2. **Semantic Scholar** for citation graph and related-paper exploration.
3. **arXiv** for AI/ML/CV preprint discovery.
4. **Crossref** for DOI and publication metadata cleanup.

Paid or LLM-mediated search tools such as Perplexity can remain optional fallback or synthesis backends, but should not be the only paper-search mechanism.

If the repository has an existing lookup script, improve it incrementally instead of replacing it wholesale.

---

## When to Use This Skill

Use this skill when you need to:

- find closest prior work;
- identify standard or missing baselines;
- find datasets, benchmarks, metrics, or evaluation protocols;
- verify whether a technical or scientific claim has external support;
- find citation candidates for a paper section;
- check recent developments in a method area;
- search a local Zotero library for papers, attachments, or citation candidates;
- export BibTeX or draft citation material from a local Zotero library;
- import bibliographic records only when the task is explicitly about the local library;
- support context-aware peer review;
- gather source material before a literature review;
- compare a proposed method against related work;
- verify current tool, library, model, or benchmark information.

Do not use this skill for:

- broad unfocused exploration;
- generating paper prose;
- formatting citations;
- auditing repo-internal claims;
- replacing human judgment about novelty;
- creating visual artifacts by default.

For direct Zotero Desktop operations, treat Zotero as a local-library mode of this skill rather than a separate discovery path.

---

## Relationship to Research Gates

This skill is most relevant to the following gates in `docs/research_gates.md`:

- Research Direction Gate
- Research Change Gate
- Experiment Decision Gate
- Evaluation and Result Interpretation Gate
- Claim Support Gate
- Red-Team Review Gate
- Paper Writing Gate

Use this skill to gather external evidence before judging novelty, selecting baselines, designing experiments, strengthening claims, or performing context-aware peer review.

A lookup result does not by itself prove a claim. It provides candidate evidence that must be interpreted, cited, synthesized, or audited by the relevant downstream skill.

---

## Role in the Agentic Workflow

Use `research-lookup` as the source discovery layer.

Typical flow:

```text
research-lookup
    -> find candidate sources, baselines, benchmarks, datasets, or technical references

literature-review
    -> synthesize sources into themes, gaps, comparisons, and research context

scientific-critical-thinking
    -> pressure-test methodology, novelty, experiment design, and interpretation

claim-auditor
    -> check whether manuscript claims are supported by repo evidence and citation artifacts

peer-review
    -> produce reviewer-style critique using internal and external context
```

For context-aware peer review, use this skill before final peer-review synthesis when external context is needed.

---

## Visual Artifacts

Do not generate schematics by default.

If lookup results reveal that a visual comparison, taxonomy, timeline, benchmark map, or method diagram would help, recommend using `scientific-schematics` separately.

---

## Lookup Modes

Choose the smallest lookup mode that fits the task.

---

### 1. Closest Prior Work Lookup

Use when assessing novelty, contribution positioning, or related work.

Search for:

- papers solving the same task;
- papers using similar methods;
- papers using the same dataset or benchmark;
- recent surveys;
- foundation or seminal papers;
- strong adjacent-domain methods.

Return:

1. likely closest prior work;
2. why each source is relevant;
3. what aspect overlaps with the project;
4. what difference may remain;
5. whether the source weakens, supports, or complicates the novelty claim.

Avoid claiming novelty from absence of evidence. A failed lookup is not proof that no prior work exists.

---

### 2. Baseline and Benchmark Scouting

Use when planning experiments, reviewing a paper, or checking whether comparisons are sufficient.

Search for:

- standard baselines in the task area;
- strong simple baselines;
- current commonly used architectures or methods;
- datasets and benchmark leaderboards when available;
- evaluation metrics and protocols;
- prior papers using the same dataset;
- missing comparisons reviewers may expect.

Return:

1. recommended baseline candidates;
2. expected evaluation metrics;
3. relevant datasets or benchmarks;
4. comparison protocols;
5. missing or risky comparisons;
6. which baselines are essential versus optional.

For AI/CV research, always consider whether the proposed method should be compared against:

- the current project baseline;
- a simple strong baseline;
- a recent standard method;
- an ablation or no-change control;
- a pretrained or frozen-feature baseline when relevant.

---

### 3. Dataset and Benchmark Lookup

Use when validating dataset choice, split policy, evaluation protocol, or benchmark relevance.

Search for:

- dataset papers;
- benchmark descriptions;
- label schemas;
- train/validation/test split conventions;
- known leakage issues;
- known limitations;
- standard metrics;
- related datasets for external validation.

Return:

1. dataset or benchmark source;
2. task and label format;
3. standard split and metric;
4. known limitations;
5. leakage or bias warnings;
6. relevance to the current project.

---

### 4. Citation Candidate Lookup

Use when a paper section needs supporting citations.

Search for sources that support a specific claim type:

- background claim;
- method claim;
- dataset claim;
- evaluation claim;
- limitation claim;
- motivation claim;
- comparison claim.

Return:

1. candidate citation;
2. claim it may support;
3. strength of support;
4. citation metadata if available;
5. whether the source should be checked by `citation-management`.

Do not insert citations automatically unless the user requested writing or editing.

Do not cite sources that were not actually found or verified.

---

### 5. Technical Verification Lookup

Use when checking technical facts, tool behavior, library support, model release details, standards, or current documentation.

Search for:

- official documentation;
- release notes;
- model cards;
- dataset cards;
- benchmark pages;
- repository documentation;
- authoritative technical references.

Return:

1. answer;
2. source;
3. version/date when relevant;
4. uncertainty or compatibility risk;
5. whether the information may become stale.

Prefer primary sources for technical claims.

---

### 6. Recent Developments Lookup

Use when the task depends on current information.

Search for:

- recent papers;
- recent benchmark results;
- recent model releases;
- updated datasets;
- changed APIs or libraries;
- current best practices.

Return:

1. what changed recently;
2. why it matters;
3. source and date;
4. whether it affects the current project;
5. whether deeper literature review is needed.

---

## Query Discipline

Before searching, define the lookup target.

Good lookup queries should include:

1. task or domain;
2. method or concept;
3. dataset or benchmark if relevant;
4. timeframe if recency matters;
5. desired source type.

Examples:

```text
road damage detection computer vision benchmark datasets mAP baseline YOLO
```

```text
small object detection road crack damage detection false negative recall augmentation baseline
```

```text
vision transformer road damage detection comparison CNN YOLO baseline
```

```text
latest CVPR ECCV ICCV road damage detection dataset benchmark
```

Avoid vague queries such as:

```text
AI papers
```

```text
best computer vision method
```

```text
road damage novelty
```

---

## Paper Quality and Source Prioritization

Prefer high-quality and directly relevant sources.

For AI/ML/CV, prioritize:

1. papers from relevant top venues when directly related;
2. papers using the same dataset or task;
3. benchmark or dataset papers;
4. surveys and systematic reviews when mapping a field;
5. well-maintained official repositories or documentation;
6. model cards and dataset cards;
7. recent papers when recency matters;
8. foundational papers when historical context matters.

High citation count is useful but not sufficient.

A highly cited paper may be less relevant than a lower-cited paper that uses the same task, dataset, or evaluation protocol.

Do not over-prioritize venue prestige over task relevance.

---

## AI/ML/CV-Specific Lookup Checklist

When looking up sources for AI/ML/CV work, consider whether you need evidence about:

1. task definition;
2. dataset and label schema;
3. split policy;
4. leakage risks;
5. baseline methods;
6. current standard architectures;
7. evaluation metrics;
8. ablation expectations;
9. failure analysis practices;
10. domain shift or robustness;
11. compute and training details;
12. reproducibility artifacts;
13. known limitations;
14. closest prior work.

Do not search all of these by default. Select only what the current task requires.

---

## Backend Selection

This skill supports both free scholarly APIs and optional paid or LLM-assisted search backends.

### OpenAlex

Use for:

- broad scholarly discovery;
- initial prior-work search;
- author, venue, institution, topic, or concept lookup;
- finding papers across disciplines;
- identifying related works at scale.

Best default for paper discovery when no seed paper is available.

### Semantic Scholar

Use for:

- citation graph exploration;
- related-paper discovery;
- influential paper lookup;
- metadata enrichment;
- finding papers connected to a known seed paper.

Best when citation relationships matter.

### arXiv

Use for:

- recent AI/ML/CV preprints;
- arXiv ID lookup;
- fast-moving research areas;
- papers not yet indexed elsewhere.

Best for recent computer vision, machine learning, and AI papers.

### Crossref

Use for:

- DOI metadata lookup;
- publication metadata verification;
- journal or proceedings metadata;
- citation cleanup before BibTeX generation.

Best for bibliographic verification.

### Perplexity / Parallel API / General Web Search

Use for:

- recent web synthesis;
- official benchmark pages;
- project pages;
- documentation;
- model release pages;
- blogs or technical reports;
- cases where structured scholarly APIs miss relevant context.

Use as a supplement, not the sole source of scholarly evidence.

---

## Current Backend Integration

If the current implementation uses `Parallel API`, `Perplexity`, `OpenRouter`, or another configured backend, preserve it unless the task explicitly asks for a backend refactor.

### Environment Variables

Optional existing paid or hosted backends may use:

```bash
export PARALLEL_API_KEY="your_parallel_api_key"
export OPENROUTER_API_KEY="your_openrouter_api_key"
```

Free scholarly APIs may not require API keys, but still require responsible usage, rate-limit handling, and metadata validation.

### Command-Line Usage

Always save lookup results.

```bash
python research_lookup.py "your query" -o sources/research_YYYYMMDD_HHMMSS_<topic>.md
```

Force a backend when supported by the implementation:

```bash
python research_lookup.py "your query" --force-backend openalex -o sources/papers_<topic>.md
python research_lookup.py "your query" --force-backend semanticscholar -o sources/papers_<topic>.md
python research_lookup.py "your query" --force-backend arxiv -o sources/papers_<topic>.md
python research_lookup.py "your query" --force-backend crossref -o sources/metadata_<topic>.md
python research_lookup.py "your query" --force-backend parallel -o sources/research_<topic>.md
python research_lookup.py "your query" --force-backend perplexity -o sources/papers_<topic>.md
```

JSON output is preferred when metadata matters:

```bash
python research_lookup.py "your query" --json -o sources/research_<topic>.json
```

Batch lookup:

```bash
python research_lookup.py --batch "query 1" "query 2" "query 3" -o sources/batch_research_<topic>.md
```

If a listed backend is not implemented yet, do not pretend it was used. State that the backend is recommended but not currently wired.

---

## Mandatory Saving Policy

Every research lookup result must be saved to the project’s `sources/` folder.

Research lookup results are source artifacts. They support reproducibility, context recovery, citation tracing, and later claim auditing.

### Saving Rules

| Lookup type | Target pattern |
|---|---|
| General research | `sources/research_YYYYMMDD_HHMMSS_<topic>.md` |
| Academic papers | `sources/papers_YYYYMMDD_HHMMSS_<topic>.md` |
| Baseline scouting | `sources/baselines_YYYYMMDD_HHMMSS_<topic>.md` |
| Dataset/benchmark lookup | `sources/datasets_YYYYMMDD_HHMMSS_<topic>.md` |
| Batch lookup | `sources/batch_research_YYYYMMDD_HHMMSS_<topic>.md` |
| JSON metadata | `sources/research_YYYYMMDD_HHMMSS_<topic>.json` |

Before making a new lookup, check whether a relevant saved source already exists:

```bash
ls sources/
```

If an existing source covers the same topic and is not stale for the task, reuse it instead of querying again.

Saved files must preserve:

- source URLs;
- titles;
- authors when available;
- dates;
- venues or sources when available;
- DOIs, arXiv IDs, or other identifiers when available;
- snippets, abstracts, or summaries;
- query text;
- backend used;
- lookup timestamp.

### Reading Queue Handoff

When lookup finds sources that may affect novelty, baselines, datasets, experiment design, claims, or manuscript citations, add them to:

- `sources/reading_queue.md`

Do not mark lookup results as deeply read.

A lookup result may become a paper card only after the source is actually read or inspected enough to fill the paper-card fields.

---

## Output Format

When reporting lookup results, use this structure:

1. **Lookup target**
   - What question or evidence need was searched.

2. **Search strategy**
   - Query terms, backend, filters, and source type.

3. **Key findings**
   - Short summary of what was found.

4. **Candidate sources**
   - Source title, year/date, venue/source, URL or DOI when available, and relevance.

5. **Baseline / dataset / benchmark implications**
   - Include when relevant.

6. **Novelty or claim implications**
   - State whether findings support, weaken, or complicate the project claim.

7. **Uncertainty**
   - What may be missing, stale, inaccessible, or unresolved.

8. **Saved artifact**
   - Path to the saved lookup result in `sources/`.

For small lookups, keep the output concise while preserving source traceability.

---

## Error Handling and Limitations

Known limitations:

- external APIs may miss paywalled or restricted sources;
- academic search may not access full text;
- citation counts may be stale or unavailable;
- metadata may be incomplete or duplicated;
- venue prestige does not guarantee relevance;
- web summaries may misrepresent papers;
- absence of a source is not proof of absence of prior work;
- pretrained model data contamination may be hard to verify;
- LLM-mediated search may synthesize unsupported statements.

If lookup results are insufficient:

1. rephrase the query;
2. narrow or broaden the task terms;
3. search by dataset, benchmark, or method name;
4. search for surveys;
5. search for papers that cite or are cited by a known source;
6. use multiple backends;
7. escalate to `literature-review` if synthesis is needed.

---

## Complementary Skills

| Need | Use |
|---|---|
| Targeted source discovery | `research-lookup` |
| Synthesis across papers | `literature-review` |
| BibTeX, DOI, reference hygiene | `citation-management` |
| Reviewer-style critique | `peer-review` |
| Internal methodology critique | `scientific-critical-thinking` |
| Claim support audit | `claim-auditor` |
| Manuscript drafting | `scientific-writing` |
| Visual diagrams or schematics | `scientific-schematics` |

---

## Final Checklist

Before finalizing a research lookup task, check:

1. [ ] The lookup target is specific.
2. [ ] The search strategy is stated.
3. [ ] Structured scholarly APIs were preferred for paper discovery when available.
4. [ ] Sources are relevant to the task, not merely high-profile.
5. [ ] Closest prior work is identified when novelty is involved.
6. [ ] Baselines or benchmarks are identified when experiments are involved.
7. [ ] Dataset or metric details are identified when evaluation is involved.
8. [ ] Citation candidates are not treated as verified manuscript support until checked.
9. [ ] Results are saved under `sources/`.
10. [ ] Uncertainty or missing coverage is stated.
11. [ ] The next downstream skill is identified when needed.

---

## Remember

Research lookup should make later research decisions better.

It should help agents answer:

- What prior work is closest?
- What baseline would a reviewer expect?
- What dataset or benchmark defines the task?
- What metric should support the claim?
- What citation could support this statement?
- What current evidence changes the plan?
- What uncertainty remains?

Do not use lookup as a substitute for synthesis, critique, claim auditing, or human research judgment.
