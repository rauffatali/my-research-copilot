# Research Lookup Skill

This skill provides agent-friendly research lookup for AI/ML/CV workflows.

It is designed to help agents find:

- closest prior work;
- baseline candidates;
- datasets and benchmarks;
- citation candidates;
- local Zotero library records and citations when the user's references live there;
- recent papers or developments;
- technical references and official documentation.

The main implementation is:

```text
scripts/research_lookup.py
```

The agent-friendly entry point is:

```text
lookup.py
```

Use `lookup.py` by default unless you have a reason to call the script directly.

For local Zotero library work, treat this skill as the primary entry point and use the Zotero compatibility wrapper only if a task specifically needs the local helper commands.

---

## Design Principles

Research lookup should be:

1. **Automated**
   - Agents should use structured APIs where possible instead of manual browsing.

2. **Source-preserving**
   - Results should be saved under `sources/` so later agents can audit, synthesize, cite, or review them.

3. **Broad but focusable**
   - The tool should work across AI/ML/CV topics.
   - Domain-specific focus should come from the query and optional `--boost-phrase`, not hardcoded assumptions.

4. **Evidence-aware**
   - Lookup results are candidate evidence.
   - They still need synthesis, citation checking, or claim auditing before becoming paper support.

5. **Backend-flexible**
   - Prefer free scholarly APIs first.
   - Use paid/synthesis APIs only when useful or explicitly requested.

---

## Backend Strategy

Default paper discovery should prefer free structured scholarly APIs.

Recommended priority:

1. **OpenAlex**
   - Broad scholarly discovery.
   - Good default for prior work, baselines, datasets, and citation candidates.

2. **arXiv**
   - Recent AI/ML/CV preprints.
   - Useful for recent-developments or preprint-focused searches.
   - May rate-limit or timeout; this is handled as a warning, not a hard failure.

3. **Crossref**
   - DOI and publication metadata.
   - Useful for citation candidates and bibliographic verification.

4. **Semantic Scholar**
   - Citation graph, related papers, paper metadata.
   - Optional by default because unauthenticated usage may be rate-limited.
   - Set `SEMANTIC_SCHOLAR_API_KEY` if available.

5. **Parallel / Perplexity**
   - Optional synthesis or web/context fallback.
   - Useful for technical verification, official pages, benchmark pages, documentation, or when scholarly APIs miss context.

Do not rely on LLM-generated summaries as final evidence. Preserve primary source metadata and URLs.

---

## Optional Environment Variables

The free scholarly backends can work without paid keys.

Optional keys:

```bash
export SEMANTIC_SCHOLAR_API_KEY="your_semantic_scholar_key"
export PARALLEL_API_KEY="your_parallel_key"
export OPENROUTER_API_KEY="your_openrouter_key"
```

Backend requirements:

| Backend | Key required? | Notes |
|---|---:|---|
| OpenAlex | No | Default scholarly search |
| arXiv | No | May rate-limit or timeout |
| Crossref | No | Good DOI/publication metadata |
| Semantic Scholar | Optional | API key reduces rate-limit issues |
| Parallel | Yes | Optional synthesis fallback |
| Perplexity via OpenRouter | Yes | Optional synthesis fallback |

---

## Optional Google Scholar Legacy Utility

A legacy Google Scholar script may be kept under `scripts/legacy/` and `references/legacy/` for manual fallback search. It is not part of the default backend router because Google Scholar automation can be fragile, rate-limited, and less reproducible than structured scholarly APIs.

Prefer OpenAlex, arXiv, Crossref, and Semantic Scholar first.

---

## Basic Usage

Run from the skill folder:

```bash
python lookup.py "small object detection aerial imagery benchmark" --mode prior-work --limit 10
```

Print results without saving:

```bash
python lookup.py "object detection YOLO benchmark" --mode baseline-scout --limit 10 --no-save
```

Save default Markdown artifact under `sources/`:

```bash
python lookup.py "vision transformer object detection" --mode recent-developments --recent-years 3
```

Save explicit Markdown and JSON:

```bash
python lookup.py "domain shift in computer vision evaluation" \
  --mode citation-candidates \
  --out sources/citations_domain_shift.md \
  --json-out sources/citations_domain_shift.json
```

---

## Lookup Modes

Choose the smallest mode that matches the task.

| Mode | Use when you need |
|---|---|
| `prior-work` | Closest related papers and prior methods |
| `baseline-scout` | Baselines, comparison methods, metrics, benchmark expectations |
| `dataset-benchmark` | Dataset papers, benchmark protocols, labels, splits, metrics |
| `citation-candidates` | Candidate sources for paper claims or background statements |
| `technical-verification` | Official docs, technical references, tool/model/library facts |
| `recent-developments` | Recent papers, preprints, benchmark updates, model releases |

Examples:

```bash
python lookup.py "masked autoencoders vision transformers" --mode prior-work --limit 10
```

```bash
python lookup.py "small object detection benchmark YOLO mAP" --mode baseline-scout --limit 10
```

```bash
python lookup.py "medical image segmentation dataset annotation protocol" --mode dataset-benchmark --limit 10
```

```bash
python lookup.py "domain shift computer vision evaluation" --mode citation-candidates --limit 10
```

```bash
python lookup.py "latest object detection foundation models" --mode recent-developments --recent-years 3 --limit 10
```

---

## Backend Selection

By default, use:

```bash
--backend auto
```

Force one backend when needed:

```bash
python lookup.py "time series anomaly detection" --backend openalex --mode prior-work
```

```bash
python lookup.py "vision transformer object detection" --backend arxiv --mode recent-developments
```

```bash
python lookup.py "domain shift computer vision" --backend crossref --mode citation-candidates
```

```bash
python lookup.py "medical image segmentation benchmark" --backend semantic-scholar --mode baseline-scout
```

Use paid/synthesis backends only when configured:

```bash
python lookup.py "official YOLO documentation benchmark evaluation" --backend parallel --mode technical-verification
```

```bash
python lookup.py "recent benchmark pages for enterprise question answering" --backend perplexity --mode technical-verification
```

---

## Recency, Quality, and Venue Filters

The script supports generic filters that work across broad AI/CV topics.

### Recent works

```bash
python lookup.py "vision-language models for detection" \
  --mode recent-developments \
  --recent-years 3 \
  --limit 20
```

### Year range

```bash
python lookup.py "transformer object detection" \
  --mode prior-work \
  --year-from 2020 \
  --year-to 2026 \
  --limit 20
```

### Peer-reviewed or venue-like filtering

```bash
python lookup.py "object detection benchmark" \
  --mode baseline-scout \
  --quality peer-reviewed \
  --limit 20
```

```bash
python lookup.py "image segmentation transformer" \
  --mode prior-work \
  --quality proceedings \
  --limit 20
```

### Venue filter

```bash
python lookup.py "object detection transformer" \
  --mode prior-work \
  --venue CVPR \
  --limit 10
```

### Citation filter

```bash
python lookup.py "domain shift computer vision evaluation" \
  --mode citation-candidates \
  --year-from 2018 \
  --min-citations 50 \
  --limit 20
```

Important: quality filters are metadata-based heuristics. Verify venue and peer-review status before using results as evidence.

---

## Boost Phrases

Use `--boost-phrase` when the query is broad but the agent wants results ranked toward a target domain.

Example:

```bash
python lookup.py "object detection YOLO benchmark" \
  --mode baseline-scout \
  --boost-phrase "medical imaging" \
  --boost-phrase "annotation protocol" \
  --limit 10
```

Boost phrases affect ranking only. They do not hard-filter results.

This keeps the script broad for AI/CV while allowing task-specific prioritization.

Use boost phrases for domains such as:

- medical imaging;
- remote sensing;
- autonomous driving;
- industrial defect detection;
- document understanding;
- video tracking;
- multimodal retrieval.

---

## Saving Policy

By default, the script saves Markdown artifacts under:

```text
sources/
```

Default naming pattern:

```text
sources/<mode-prefix>_<timestamp>_<query-slug>.md
```

Examples:

```text
sources/papers_20260521_120000_object_detection_yolo.md
sources/baselines_20260521_120000_small_object_detection.md
sources/datasets_20260521_120000_medical_image_segmentation.md
sources/citations_20260521_120000_domain_shift_cv.md
```

Use `--no-save` only for quick debugging.

Saved artifacts are useful for:

- `literature-review`;
- `citation-management`;
- `claim-auditor`;
- `scientific-critical-thinking`;
- `peer-review`;
- future context recovery.

---

## Output Format

A lookup report includes:

- original query;
- expanded query;
- mode;
- backend(s);
- timestamp;
- filters;
- boost phrases when used;
- backend warnings;
- normalized results;
- suggested next skill or workflow step.

Each result may include:

- title;
- year;
- authors;
- venue;
- work type;
- DOI;
- arXiv ID;
- URL;
- abstract/snippet;
- citation count when available;
- source backend.

---

## Agent Workflow Integration

Typical use:

```text
research-lookup
    → find candidate sources, baselines, datasets, benchmarks, or technical references

literature-review
    → synthesize sources into themes, gaps, comparisons, and research context

scientific-critical-thinking
    → pressure-test methodology, novelty, experiment design, and interpretation

citation-management
    → verify BibTeX, DOI, and reference metadata

claim-auditor
    → check manuscript claims against repository evidence and citation artifacts

peer-review
    → produce reviewer-style critique using internal and external context
```

For context-aware peer review, use research lookup before final peer-review synthesis when external context is needed.

---

## Troubleshooting

### arXiv timeout or 429

arXiv may rate-limit or timeout.

Try:

```bash
python lookup.py "your query" --mode prior-work --backend openalex --limit 10
```

or avoid recent/preprint-heavy modes temporarily.

### Semantic Scholar 429

Semantic Scholar may rate-limit unauthenticated requests.

Options:

```bash
export SEMANTIC_SCHOLAR_API_KEY="your_key"
```

or use:

```bash
python lookup.py "your query" --backend openalex --mode prior-work
```

### Results are too broad

Try:

```bash
--boost-phrase "your domain phrase"
```

or make the query more specific.

Example:

```bash
python lookup.py "YOLO benchmark object detection" \
  --mode baseline-scout \
  --boost-phrase "medical imaging"
```

### Results are too narrow

Remove boost phrases or strict filters such as:

```text
--venue
--min-citations
--quality peer-reviewed
```

### No results after filtering

Relax one or more of:

```text
--quality
--venue
--min-citations
--year-from
--recent-years
```

### Paid backend key missing

Only needed for optional backends:

```text
parallel
perplexity
```

Free scholarly backends should still work without these keys.

---

## Good Queries

Good queries include task, method, dataset, benchmark, or metric terms.

Examples:

```text
small object detection aerial imagery
small object detection YOLO benchmark mAP
vision transformer object detection benchmark
domain shift computer vision evaluation
medical image segmentation dataset annotation protocol
foundation models image segmentation benchmark
```

Avoid overly vague queries:

```text
AI papers
best computer vision method
time series anomaly detection novelty
```

---

## Limitations

- API metadata may be incomplete.
- Peer-review status is metadata-based and should be verified.
- Citation counts may be stale or unavailable.
- arXiv and Semantic Scholar may rate-limit.
- Absence of a result is not proof that no prior work exists.
- LLM synthesis backends can summarize incorrectly.
- Lookup is not a replacement for literature review or claim auditing.

---

## Recommended Next Step After Lookup

Use the saved artifact with:

- `literature-review` for synthesis;
- `citation-management` for BibTeX and reference hygiene;
- `scientific-critical-thinking` for methodology critique;
- `claim-auditor` for paper-claim support;
- `peer-review` for reviewer-style critique.
