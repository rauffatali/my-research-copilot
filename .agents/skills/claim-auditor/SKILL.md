---
name: claim-auditor
description: Use to audit manuscript, report, or documentation claims against repository evidence, experiment artifacts, verified citations, literature-review outputs, and project scope. Use before approving abstracts, introductions, contributions, related work, results summaries, conclusions, rebuttals, or reviewer-sensitive claims. For reference metadata verification use citation-management. For source discovery use research-lookup.
---

# Claim Auditor

## Overview

Claim Auditor is the evidence-support layer of the research workflow.

Use this skill to verify whether claims in manuscripts, reports, documentation, slides, rebuttals, or summaries are supported by available evidence.

A claim is any statement that asserts something about:

- novelty;
- performance;
- robustness;
- generalization;
- efficiency;
- dataset properties;
- baselines;
- experimental results;
- method behavior;
- limitations;
- literature context;
- problem importance;
- contribution scope.

The goal is to keep scientific writing proportional to evidence.

This skill should not invent evidence, citations, metrics, baselines, ablations, datasets, or conclusions.

---

## Core Responsibility

This skill answers:

```text
What does the claim say?
What evidence supports it?
Is the evidence strong enough?
Is the wording too strong?
What safer wording should be used?
What evidence is missing?
```

The output should help the project avoid:

- overclaiming;
- unsupported novelty statements;
- inflated result claims;
- broad generalization from narrow experiments;
- citation misuse;
- hallucinated or unsupported literature claims;
- stating planned work as completed work;
- claiming evidence from incomplete or exploratory runs;
- making reviewer-sensitive claims without proof.

---

## Relationship to Other Skills

Use the smallest relevant skill combination.

| Need | Use |
|---|---|
| Find papers, datasets, benchmarks, or citation candidates | `research-lookup` |
| Synthesize literature into themes, gaps, or paper context | `literature-review` |
| Verify reference existence and BibTeX metadata | `citation-management` |
| Audit whether claims are supported by evidence | `claim-auditor` |
| Draft or polish prose after evidence is checked | `scientific-writing` |
| Critique methodology, novelty, or experiment design | `scientific-critical-thinking` |
| Reviewer-style critique | `peer-review` |

Important distinction:

```text
citation-management
→ verifies that a reference is real and metadata is correct

claim-auditor
→ verifies that the reference or evidence actually supports the claim
```

Recommended paper-safety flow:

```text
research-lookup
    → literature-review
    → citation-management
    → scientific-writing
    → claim-auditor
```

For results-sensitive claims:

```text
runs/ + outputs/ + paper/
    → claim-auditor
    → scientific-critical-thinking or peer-review if needed
```

---

## Evidence Sources

Use these as sources of truth.

### Manuscript and Writing Artifacts

- `paper/`
- manuscript section files
- abstracts
- rebuttal drafts
- response letters
- slide text
- reports
- README claims when research-facing

### Experiment Evidence

- `runs/`
- `outputs/`
- result tables
- generated figures
- logs
- metrics files
- configs
- checkpoints metadata
- ablation records
- failure case outputs
- qualitative examples

### Project Context

- `docs/PROJECT_PLAN.md`
- `docs/research_gates.md`
- `docs/research_context.md`
- `docs/current_status.md`
- `AGENTS.md`
- relevant `.agents/guidance/` files
- locked scope, approved assumptions, and known limitations

### Literature and Citation Evidence

- `sources/*.md`
- `sources/*.json`
- literature-review outputs
- verified references from `citation-management`
- `.bib` files only after citation-management has verified metadata
- cited papers or paper notes when provided

### Implementation Evidence

Use when auditing method or implementation claims:

- `src/`
- `scripts/`
- `configs/`
- `tests/`
- notebooks, only if they are part of the accepted workflow
- training/evaluation scripts
- preprocessing code
- dataset split code
- metric implementation

Do not treat code existence as experimental evidence unless the claim is about implementation availability.

---

## When to Use This Skill

Use this skill when checking:

- abstract claims;
- introduction motivation and gap claims;
- contribution statements;
- related work comparisons;
- method claims;
- dataset claims;
- evaluation claims;
- baseline claims;
- ablation claims;
- robustness or generalization claims;
- efficiency or compute claims;
- result summaries;
- conclusion claims;
- limitation statements;
- rebuttal claims;
- reviewer-sensitive statements;
- claims using strong wording such as “novel,” “state-of-the-art,” “robust,” “generalizes,” “significantly,” “outperforms,” or “first.”

Use this skill before finalizing paper text.

---

## Do Not Use This Skill For

Do not use this skill as the main tool for:

- finding new papers; use `research-lookup`;
- cleaning BibTeX or DOI metadata; use `citation-management`;
- writing polished prose from scratch; use `scientific-writing`;
- performing full literature synthesis; use `literature-review`;
- designing new experiments; use `scientific-critical-thinking`;
- simulating reviewer feedback; use `peer-review`.

This skill can recommend those next steps when missing evidence is found.

---

## Claim Types

Classify claims before auditing them.

### 1. Background / Motivation Claim

Example:

```text
Road infrastructure monitoring is important for maintenance planning.
```

Evidence needed:

- literature source;
- dataset/benchmark source;
- domain report;
- research-context document.

### 2. Literature / Prior Work Claim

Example:

```text
Most prior work focuses on supervised object detection.
```

Evidence needed:

- literature-review output;
- verified citations;
- source artifact;
- closest-prior-work table.

### 3. Novelty Claim

Example:

```text
This is the first method to...
```

Evidence needed:

- strong literature review;
- closest-prior-work analysis;
- research-lookup artifacts;
- citation audit;
- usually peer-review or scientific-critical-thinking review.

Treat novelty claims as high risk.

### 4. Method Claim

Example:

```text
The model uses multi-scale augmentation during training.
```

Evidence needed:

- code;
- config;
- training script;
- experiment log;
- method section consistency.

### 5. Dataset Claim

Example:

```text
The dataset contains diverse weather and road-surface conditions.
```

Evidence needed:

- dataset documentation;
- dataset statistics;
- preprocessing scripts;
- annotation files;
- literature source;
- data audit.

### 6. Baseline Claim

Example:

```text
We compare against the strongest YOLO-based baselines.
```

Evidence needed:

- baseline list;
- experiment configs;
- literature-review baseline review;
- result tables;
- fair comparison evidence.

### 7. Performance Claim

Example:

```text
Our method improves mAP over the baseline.
```

Evidence needed:

- result tables;
- logs;
- metric scripts;
- baseline outputs;
- exact metric definition;
- same split/protocol.

### 8. Robustness / Generalization Claim

Example:

```text
The method generalizes across domains.
```

Evidence needed:

- cross-domain evaluation;
- held-out-domain test;
- robustness slices;
- failure analysis;
- multiple seeds or datasets when relevant.

Treat as high risk unless explicitly tested.

### 9. Efficiency Claim

Example:

```text
The method is computationally efficient.
```

Evidence needed:

- runtime measurement;
- parameter count;
- FLOPs;
- memory usage;
- hardware details;
- comparison baseline.

### 10. Ablation Claim

Example:

```text
The augmentation strategy is responsible for the improvement.
```

Evidence needed:

- ablation table;
- controlled experiment;
- same training/evaluation protocol.

### 11. Limitation Claim

Example:

```text
The method may fail under severe occlusion.
```

Evidence needed:

- failure cases;
- qualitative analysis;
- literature support;
- documented limitation.

Limitation claims may be acceptable with weaker evidence if clearly framed as observed or plausible.

---

## Support Labels

Use these labels consistently.

| Label | Meaning | Action |
|---|---|---|
| `supported` | Direct evidence supports the claim as written | Keep |
| `partially supported` | Evidence supports part of the claim, but wording is too broad or incomplete | Rewrite conservatively |
| `preliminary` | Evidence exists but is limited, exploratory, single-run, or not fully validated | Mark as preliminary or weaken |
| `hypothesis` | Plausible but not yet tested | Present as hypothesis or future work |
| `needs citation` | Literature support is required but missing | Use `research-lookup` or `literature-review` |
| `wrong citation` | Citation/reference exists but does not support the claim | Replace citation or rewrite; use `claim-auditor`/`research-lookup` |
| `unsupported` | No adequate evidence found | Remove, add TODO, or rewrite as planned work |
| `contradicted` | Available evidence conflicts with the claim | Correct or remove immediately |
| `out of scope` | Claim exceeds approved project scope | Remove or narrow |
| `needs manual check` | Evidence may exist but is ambiguous or inaccessible | Do not approve yet |

Do not collapse these labels into only supported/unsupported when nuance matters.

---

## Evidence Hierarchy

Use the right evidence for the claim type.

| Claim type | Strong evidence | Weak or insufficient evidence |
|---|---|---|
| Performance | result table, logs, same metric/split, baseline run | anecdotal observation, one untracked run |
| Generalization | held-out domain/dataset, cross-domain evaluation | single test split |
| Robustness | stress tests, slices, corruption/domain tests | general intuition |
| Novelty | closest-prior-work review, source artifacts, verified citations | “we did not see it” without search trace |
| Method | code/config/logs matching manuscript | intended design only |
| Dataset | dataset docs, statistics, split files | assumptions about dataset |
| Baseline | implemented comparisons, literature baseline review | citing a method without running it |
| Citation/literature | verified source supports sentence | citation exists but is unrelated |
| Efficiency | measured runtime/params/FLOPs/hardware | subjective “lightweight” wording |

---

## What To Do

For each audit task:

1. Identify the target section or claims.
2. Break paragraphs into auditable claims.
3. Classify each claim type.
4. Locate the relevant evidence.
5. Compare wording to evidence strength.
6. Assign a support label.
7. Explain the reason briefly.
8. Provide a conservative rewrite when needed.
9. Identify missing evidence, citation, ablation, baseline, or documentation.
10. Recommend the next skill or action if the claim cannot be approved.

Prefer a TODO over invented support.

---

## Citation-Context Auditing

Use this when a manuscript claim has a citation.

Check:

1. Does the cited source exist?
2. Has `citation-management` verified the reference metadata?
3. Does the cited source actually support the local sentence?
4. Is the source direct evidence or only background?
5. Is the claim broader than the source?
6. Is a preprint being treated as established fact?
7. Is a survey cited for a specific result from another paper?
8. Is a dataset paper cited as evidence of model performance?
9. Is a benchmark page cited as if it were a peer-reviewed paper?

Labels to use:

- `supported`;
- `partially supported`;
- `wrong citation`;
- `needs citation`;
- `needs manual check`.

If the reference is fake or metadata is wrong, hand off to `citation-management`.

If the reference is real but does not support the claim, keep the issue in claim-auditor and request a better source through `research-lookup`.

---

## Citation Need Detection

Use this when auditing manuscript drafts, especially introduction, background, related work, motivation, discussion, and conclusion sections.

For each sentence or claim, decide whether it needs a citation.

A sentence usually needs a citation when it states:

- prior work behavior or limitations;
- what most existing methods do;
- a research gap;
- problem importance or real-world impact;
- dataset, benchmark, or metric facts;
- common practice in the field;
- comparison to existing methods;
- claims about trends or recent developments;
- external technical facts not produced by this project.

A sentence may not need a citation when it states:

- this paper’s own goal;
- this project’s own method, if described from implementation evidence;
- this project’s own experimental setup, if documented;
- this project’s own results, if supported by tables, figures, logs, or outputs;
- a transition sentence with no factual external claim.

Use the label `needs citation` when a claim requires literature support but no citation, source artifact, or verified reference is present.

If the sentence has a citation but the citation does not support it, use `wrong citation`.

If the needed source is missing, recommend `research-lookup`.

If the citation exists but metadata is suspicious, recommend `citation-management`.

---

## Conservative Rewrite Rules

When evidence is weak, reduce claim strength.

Use safer substitutions:

| Strong wording | Safer wording |
|---|---|
| proves | provides evidence that |
| demonstrates | suggests / indicates, if evidence is limited |
| solves | addresses |
| eliminates | reduces / may reduce |
| generalizes | was evaluated on / showed performance on |
| robust | showed robustness under the evaluated conditions |
| state-of-the-art | competitive / strong / improved over evaluated baselines |
| significantly improves | improves, unless statistical significance is tested |
| first | avoid unless closest-prior-work evidence is strong |
| outperforms all baselines | outperforms the evaluated baselines |
| universally applicable | applicable in the evaluated setting |
| reliable | performed consistently in the evaluated runs |

Do not weaken claims so much that they become vague. Keep wording precise.

---

## High-Risk Claims

Treat these as requiring extra evidence:

- “first”;
- “novel”;
- “state-of-the-art”;
- “robust”;
- “generalizes”;
- “real-world ready”;
- “significantly improves”;
- “outperforms existing methods”;
- “solves”;
- “eliminates”;
- “comprehensive”;
- “the best”;
- “works across domains”;
- “requires no labels”;
- “low-cost”;
- “efficient”;
- “fully automated.”

If evidence is missing, recommend removal or conservative rewrite.

---

## Output Formats

Choose the smallest useful output.

---

### Sentence-by-Sentence Claim Audit

```md
## Claim Audit

### Scope

- Section/file:
- Evidence checked:
- Date:

### Findings

| Claim | Type | Label | Evidence | Issue | Safer rewrite |
|---|---|---|---|---|---|
| [claim] | [type] | [label] | [source/evidence] | [issue] | [rewrite] |

### Summary

- Supported claims:
- Claims needing rewrite:
- Claims needing citation:
- Unsupported or contradicted claims:

### Required Actions

- [ ] add citation
- [ ] run ablation
- [ ] add baseline
- [ ] revise wording
- [ ] remove claim
- [ ] send to citation-management
- [ ] send to research-lookup
```

---

### Claim Support Matrix

Use for larger sections.

```md
| Claim ID | Location | Claim | Evidence source | Support label | Required action |
|---|---|---|---|---|---|
| C1 | intro paragraph 2 | [claim] | [evidence] | [label] | [action] |
```

---

### Conservative Rewrite Report

```md
## Conservative Rewrite Recommendations

| Original | Problem | Safer rewrite |
|---|---|---|
| [original claim] | [why too strong] | [rewrite] |
```

---

### Missing Evidence Report

```md
## Missing Evidence

| Claim | Missing evidence | Recommended next step |
|---|---|---|
| [claim] | [citation/baseline/ablation/result] | [next step] |
```

---

## Important Rules

- Never invent metrics, baselines, ablations, datasets, citations, or conclusions.
- Do not treat intended model behavior as demonstrated results unless evidence exists.
- Do not convert motivations or hypotheses into empirical findings.
- Do not broaden project scope implicitly.
- Do not treat a clean citation as claim support.
- Do not treat a single exploratory run as conclusive.
- Do not use results from a different split, dataset, metric, or configuration unless explicitly stated.
- Do not turn project goals into completed contributions.
- Do not hide uncertainty.
- Preserve the manuscript’s scientific tone while correcting evidence strength.

---

## Good Outputs

Good outputs include:

- sentence-by-sentence claim audits;
- supported versus unsupported claim lists;
- conservative rewrites for weak claims;
- identification of missing citations;
- identification of missing baselines or ablations;
- warnings about overgeneralization;
- warnings about wrong citation context;
- detection of claims that exceed project scope;
- required next steps before approval.

Bad outputs include:

- generic writing feedback without evidence checking;
- rewriting claims without explaining evidence;
- approving claims because they sound plausible;
- adding citations without verifying support;
- treating all weak claims as fully unsupported when conservative wording would fix them.

---

## Final Checklist

Before completing a claim audit:

1. [ ] Target section or claims are identified.
2. [ ] Claims are separated into auditable units.
3. [ ] Claim types are classified.
4. [ ] Evidence sources are listed.
5. [ ] Each claim has a support label.
6. [ ] Strong claims are checked carefully.
7. [ ] Citation-context issues are flagged.
8. [ ] Missing citations are identified.
9. [ ] Sentences needing citations are marked as `needs citation`.
10. [ ] Missing baselines, ablations, or metrics are identified when relevant.
11. [ ] Unsupported claims have TODOs or safer rewrites.
12. [ ] Contradicted claims are clearly marked.
13. [ ] Claims exceeding scope are narrowed or removed.
14. [ ] Citation metadata issues are handed to `citation-management`.
15. [ ] Missing literature support is handed to `research-lookup` or `literature-review`.
16. [ ] The final recommendation is clear: approve, revise, add evidence, or remove.

---

## Final Reminder

The claim-auditor should protect the paper from saying more than the evidence allows.

A good audit does not make the paper weaker. It makes the paper harder to reject.
