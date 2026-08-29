---
name: results-scaffold
description: Create draft LaTeX result tables, comparison layouts, ablation placeholders, robustness/slice tables, qualitative-result layouts, experiment-status tables, and result-section scaffolding without inventing metrics. Use when planned experiments, partial run structure, or manuscript result needs exist but final results are not yet established. For interpretation and prose use scientific-writing. For claim verification use claim-auditor.
---

# Results Scaffold

## Overview

Results Scaffold prepares the manuscript structure for reporting experiments before final metrics are complete or stable.

Use this skill to create paper-ready result table skeletons, result-section outlines, captions, and placeholder prose while preserving scientific discipline.

This skill prepares structure, not interpretation.

It should help the project move from:

```text
planned experiments / partial runs / outputs structure
→ result tables and section scaffolds
→ scientific-writing
→ claim-auditor
```

It must never invent numeric results, rankings, improvements, statistical significance, or conclusions.

---

## Core Responsibility

This skill answers:

```text
What result table or result block will the paper need?
What rows and columns are justified by the current experiment plan?
Which values are still missing?
How should missing values be marked?
What result prose can be safely written before final numbers exist?
What handoff is needed before claims are finalized?
```

The output should make it easy to fill in verified values later.

---

## Relationship to Other Skills

Use the smallest relevant skill combination.

| Need | Use |
|---|---|
| Prepare result table skeletons and placeholders | `results-scaffold` |
| Write final result prose after values are verified | `scientific-writing` |
| Check whether result claims are supported | `claim-auditor` |
| Critique whether experiments are decisive | `scientific-critical-thinking` |
| Simulate reviewer objections to results | `peer-review` |
| Verify citations/references in result context | `citation-management` |
| Apply venue-specific table/format rules | `venue-templates` |

Recommended flow:

```text
runs/ + outputs/ + docs/current_status.md
    → results-scaffold
    → scientific-writing
    → claim-auditor
```

If the table reveals missing experiments or weak comparisons:

```text
results-scaffold
    → scientific-critical-thinking
```

If final formatting depends on a venue:

```text
results-scaffold
    → venue-templates
```

---

## When to Use This Skill

Use this skill when:

- planned experiments exist but final metrics are missing;
- partial run folders exist but results are not stable;
- paper needs result-table placeholders;
- main comparison table needs structure;
- ablation table needs structure;
- robustness or slice evaluation table needs structure;
- per-class metric table needs structure;
- qualitative result figure/table layout is needed;
- result-section prose needs safe placeholders;
- captions are needed before values are final;
- the paper needs clear TODOs for missing metrics;
- experiment status needs to be summarized.

---

## Do Not Use This Skill For

Do not use this skill to:

- invent final numbers;
- infer missing metrics;
- rank methods without evidence;
- claim improvement;
- claim statistical significance;
- interpret results as final;
- write final conclusions;
- add baselines outside locked scope without marking as proposed;
- fabricate run artifacts;
- hide missing experiments;
- replace claim auditing.

If final values are available, still verify them from `runs/`, `outputs/`, or result artifacts before writing claims.

---

## Evidence and Context Sources

Use these as sources of truth:

- `runs/` for experiment structure, run IDs, logs, and planned result organization;
- `outputs/` for generated summaries, tables, plots, predictions, or artifacts;
- `docs/PROJECT_PLAN.md` for locked scope and planned comparisons;
- `docs/research_gates.md` for result and claim gates;
- `docs/research_context.md` for framing and evaluation goals;
- `docs/current_status.md` for what is done, pending, or blocked;
- `paper/` for manuscript structure and section context;
- experiment configs and scripts when needed to identify models, datasets, splits, or metrics.

If the repository context is insufficient, use TODOs rather than guessing.

---

## Placeholder Standards

Use clear placeholders that cannot be mistaken for real results.

Preferred placeholders:

```text
TODO
TBD
--
TODO_RESULT
TODO_METRIC
TODO_BASELINE
TODO_ABLATION
TODO_RUN_ID
TODO_SPLIT
```

Use `--` only when the value is not applicable.

Use `TODO` or `TBD` when the value is expected but missing.

Do not use realistic-looking fake numbers such as:

```text
0.00
99.9
XX.X
[VALUE]
```

unless the style is explicitly requested and clearly marked.

Recommended LaTeX placeholder:

```latex
\texttt{TODO}
```

or:

```latex
TODO
```

depending on the manuscript style.

## Evidence-State Boundary

Result tables, figures, metric cells, and prose shells created before actual evidence exists are `placeholder_only` until durable evidence replaces them. Existing `TODO`, `TODO_RESULT`, and `TODO_METRIC` conventions remain structural placeholders; they must not be interpreted as `result_pending` unless a real result dependency exists. If a run or raw output exists but the result is not consolidated through the applicable Phase 3 process, use `result_pending`. Neither state permits invented numerical data or final result claims.

---

## Result Block Types

Choose the smallest scaffold that fits the need.

---

### 1. Main Comparison Table

Use for primary method-vs-baseline results.

Typical columns:

- Method;
- Backbone / model family;
- Dataset;
- Split;
- Metric 1;
- Metric 2;
- Runtime / Params, if relevant;
- Notes.

Example:

```latex
\begin{table}[t]
\centering
\caption{Main comparison under the planned evaluation protocol. Values marked TODO must be filled only from verified run artifacts.}
\label{tab:main-results}
\begin{tabular}{l l c c c}
\toprule
Method & Setting & mAP & AP50 & Recall \\
\midrule
Baseline model & TODO_SPLIT & TODO & TODO & TODO \\
Proposed model & TODO_SPLIT & TODO & TODO & TODO \\
\bottomrule
\end{tabular}
\end{table}
```

Safe surrounding prose:

```text
Table~\ref{tab:main-results} is intended to report the primary comparison between the evaluated baseline and proposed model under the same dataset split and metric protocol. Final values should be inserted only after the corresponding run artifacts are verified.
```

Unsafe prose:

```text
Table~\ref{tab:main-results} shows that our method outperforms all baselines.
```

---

### 2. Ablation Table

Use when the paper needs to isolate components.

Typical columns:

- Variant;
- Component removed/changed;
- Dataset/split;
- Metric;
- Difference from full model;
- Notes.

Example:

```latex
\begin{table}[t]
\centering
\caption{Ablation scaffold for isolating the contribution of planned model components. TODO values require verified controlled runs.}
\label{tab:ablation}
\begin{tabular}{l c c c}
\toprule
Variant & Component tested & mAP & Notes \\
\midrule
Full model & -- & TODO & TODO \\
w/o component A & Component A & TODO & TODO \\
w/o component B & Component B & TODO & TODO \\
\bottomrule
\end{tabular}
\end{table}
```

Safe prose:

```text
Table~\ref{tab:ablation} is reserved for controlled ablations. Each row should correspond to a run that changes only the specified component relative to the full model.
```

---

### 3. Robustness / Slice Table

Use when results need to be broken down by condition, domain, class, size, weather, source, or difficulty.

Typical columns:

- Slice / condition;
- Number of samples;
- Baseline metric;
- Proposed metric;
- Difference;
- Notes.

Example:

```latex
\begin{table}[t]
\centering
\caption{Robustness and slice-analysis scaffold. Values should be filled from verified per-slice evaluation outputs.}
\label{tab:slice-results}
\begin{tabular}{l c c c}
\toprule
Slice & Samples & Baseline mAP & Proposed mAP \\
\midrule
Small targets & TODO & TODO & TODO \\
Low-light scenes & TODO & TODO & TODO \\
Occluded targets & TODO & TODO & TODO \\
\bottomrule
\end{tabular}
\end{table}
```

Safe prose:

```text
Table~\ref{tab:slice-results} is intended to summarize performance across predefined evaluation slices. These results should be used to support robustness claims only after the slice definitions and metrics are verified.
```

---

### 4. Per-Class Metric Table

Use for detection, segmentation, classification, or multi-label tasks.

Typical columns:

- Class;
- Support / count;
- AP / IoU / F1 / Recall;
- Baseline;
- Proposed;
- Notes.

Example:

```latex
\begin{table}[t]
\centering
\caption{Per-class metric scaffold. Counts and metrics must be filled from verified evaluation artifacts.}
\label{tab:per-class}
\begin{tabular}{l c c c}
\toprule
Class & Support & Baseline AP & Proposed AP \\
\midrule
Class A & TODO & TODO & TODO \\
Class B & TODO & TODO & TODO \\
Class C & TODO & TODO & TODO \\
\bottomrule
\end{tabular}
\end{table}
```

Use this when aggregate metrics may hide class-specific failure modes.

---

### 5. Qualitative Result Layout

Use for figures showing examples, successes, failures, or qualitative comparisons.

This skill should scaffold the layout and caption only. It should not generate images.

Use `scientific-schematics` or existing outputs for visual artifacts.

Example caption scaffold:

```latex
\begin{figure}[t]
\centering
% TODO: insert qualitative examples from verified output artifacts.
\caption{Qualitative result scaffold. The final figure should include representative successes and failure cases, with examples selected from verified prediction outputs.}
\label{fig:qualitative-results}
\end{figure}
```

Safe prose:

```text
Figure~\ref{fig:qualitative-results} is planned to show representative qualitative predictions, including both successful detections and failure cases. The examples should be selected from verified output artifacts rather than manually cherry-picked.
```

---

### 6. Experiment Status Table

Use to summarize what is complete, running, blocked, or planned.

Example:

```latex
\begin{table}[t]
\centering
\caption{Experiment status scaffold. This table is for project tracking and should not be presented as final results.}
\label{tab:experiment-status}
\begin{tabular}{l l l l}
\toprule
Experiment & Status & Expected artifact & Notes \\
\midrule
Baseline training & TODO & runs/TODO & TODO \\
Proposed model training & TODO & runs/TODO & TODO \\
Ablation: component A & TODO & runs/TODO & TODO \\
\bottomrule
\end{tabular}
\end{table}
```

This is useful for internal drafts but may not belong in the final paper.

---

### 7. Result-Section Scaffold

Use when drafting a result section before values are final.

Safe scaffold:

```latex
\section{Results}

This section will report the planned comparisons under the evaluation protocol described in Section~\ref{sec:experiments}. Table~\ref{tab:main-results} will summarize the main comparison between the evaluated baselines and the proposed method. Table~\ref{tab:ablation} will report controlled ablations for the main method components. Final quantitative claims should be added only after the corresponding run artifacts are verified.

\todo{Insert main comparison results after verified metrics are available.}
\todo{Insert ablation interpretation after controlled runs are complete.}
\todo{Run claim-auditor before finalizing result claims.}
```

---

## Caption-Safe Wording

Captions should describe intended content without claiming outcomes.

Safe caption phrases:

- “Scaffold for...”
- “Planned comparison of...”
- “Values marked TODO require verified run artifacts.”
- “This table is intended to report...”
- “The final table should include...”
- “Qualitative examples should be selected from verified outputs.”

Avoid:

- “Our method achieves...”
- “The proposed method outperforms...”
- “The results demonstrate...”
- “This confirms...”
- “Significant improvement...”

unless final values and claim audit support the wording.

---

## Result Prose Rules

Before final metrics are available, result prose may describe:

- what will be reported;
- what comparison is planned;
- what metrics will be used;
- what table/figure will contain;
- what evidence is still needed.

Before final metrics are available, result prose must not describe:

- which method wins;
- numeric improvements;
- ranking;
- statistical significance;
- final conclusions;
- robustness/generalization;
- mechanism claims.

Safe:

```text
The main comparison will evaluate each model under the same test split and metric protocol.
```

Unsafe:

```text
The proposed model provides the best performance across all metrics.
```

---

## AI/CV Table Guidance

For AI/ML/CV papers, common result tables include:

### Detection

Metrics may include:

- mAP;
- AP50;
- AP75;
- per-class AP;
- recall;
- precision;
- small/medium/large object AP;
- FPS or latency.

### Segmentation

Metrics may include:

- mIoU;
- Dice/F1;
- per-class IoU;
- boundary F1;
- pixel accuracy.

### Classification

Metrics may include:

- accuracy;
- F1;
- precision;
- recall;
- AUROC;
- confusion matrix;
- calibration metrics.

### Robustness / Domain Shift

Metrics may be grouped by:

- domain/source;
- weather;
- lighting;
- camera type;
- object size;
- occlusion;
- severity or priority;
- geographic/source split.

### Efficiency

Metrics may include:

- parameters;
- FLOPs;
- latency;
- FPS;
- memory;
- hardware.

Only include columns that are relevant to the claim and likely to be filled.

---

## Applied Object-Detection Example

For an applied object-detection task, possible scaffold tables include:

1. Main detector comparison;
2. Per-class AP;
3. Small/large target performance;
4. Acquisition-condition slice;
5. Source-domain slice;
6. Severity-aware evaluation, if labels exist;
7. Qualitative false positives/false negatives;
8. Inference speed for deployment relevance.

Example main table:

```latex
\begin{table}[t]
\centering
\caption{Applied object-detection result scaffold. TODO values must be replaced only after verified evaluation outputs are available.}
\label{tab:main-results}
\begin{tabular}{l c c c c}
\toprule
Method & Split & mAP & AP50 & Recall \\
\midrule
Baseline detector & TODO & TODO & TODO & TODO \\
Proposed detector & TODO & TODO & TODO & TODO \\
\bottomrule
\end{tabular}
\end{table}
```

Do not claim practical usefulness unless the evaluation connects to domain-relevant outcomes.

---

## What To Do

When asked to scaffold results:

1. Identify the intended result block.
2. Check available repository context.
3. Identify models, baselines, datasets, splits, and metrics from evidence.
4. Choose the smallest suitable table type.
5. Use clear placeholders for missing values.
6. Add caption-safe wording.
7. Add result-section placeholder prose only if useful.
8. Mark all assumptions and TODOs.
9. Recommend next steps for filling and auditing.
10. Do not interpret placeholders as results.

---

## Output Formats

Choose the smallest useful output.

---

### Table Scaffold Output

Use this structure:

```md
## Result Table Scaffold

### Intended Use

[main comparison / ablation / robustness / per-class / qualitative / status]

### Assumptions

- [assumption]

### LaTeX Table

[table]

### TODOs

- [missing metric]
- [missing run]
- [missing baseline]

### Next Step

[fill from runs/outputs, then claim-auditor]
```

---

### Result Section Scaffold Output

```md
## Result Section Scaffold

### Section Purpose

[what this section will report]

### Planned Tables/Figures

| Artifact | Purpose | Missing evidence |
|---|---|---|
| Table X | [purpose] | [missing] |

### Draft Placeholder Text

[text]

### TODOs

- [TODO]

### Handoff

- [scientific-writing / claim-auditor / scientific-critical-thinking]
```

---

### Experiment Status Output

```md
## Experiment Status Scaffold

| Experiment | Status | Expected artifact | Needed for claim |
|---|---|---|---|
| [experiment] | [planned/running/done/blocked] | [path] | [claim/table] |
```

---

## Important Rules

- Never invent numeric results.
- Never imply placeholder values are real results.
- Never write conclusions that depend on missing metrics.
- Never rank methods without verified evidence.
- Never claim statistical significance without statistical evidence.
- Never hide missing baselines or ablations.
- Keep tables aligned with locked project scope.
- Prefer explicit TODO markers over guessed content.
- Keep formatting compatible with the paper’s LaTeX style.
- Mark assumptions clearly.
- Route final claims to `claim-auditor`.

---

## Good Outputs

Good outputs include:

- main comparison table drafts;
- ablation table drafts;
- robustness/slice table drafts;
- per-class metric table drafts;
- qualitative result figure placeholders;
- experiment status tables;
- result-section placeholder paragraphs;
- captions that describe intended content without claiming outcomes;
- TODO lists for missing metrics, runs, baselines, and ablations.

Bad outputs include:

- fake numbers;
- fake improvements;
- fake rankings;
- final conclusions without verified results;
- captions that claim outcomes;
- tables with unnecessary columns;
- placeholders that look like real metrics;
- result prose that hides missing evidence.

---

## Final Checklist

Before completing a results-scaffold task:

1. [ ] Intended result block is identified.
2. [ ] Evidence/context sources are checked.
3. [ ] Rows are justified by known or planned comparisons.
4. [ ] Columns are realistic and minimal.
5. [ ] Metrics match the expected claim.
6. [ ] Placeholders are visibly placeholders.
7. [ ] Captions do not claim outcomes.
8. [ ] Surrounding prose does not interpret missing results.
9. [ ] Assumptions are listed.
10. [ ] Missing runs, baselines, ablations, or metrics are marked.
11. [ ] Handoff to `scientific-writing` is clear.
12. [ ] Handoff to `claim-auditor` is clear before final claims.
13. [ ] Handoff to `scientific-critical-thinking` is recommended if experiments appear indecisive.
14. [ ] Venue formatting needs are left to `venue-templates`.

---

## Final Reminder

A result scaffold is a promise of structure, not a result.

Its job is to make missing evidence visible and make final evidence easy to insert safely.
