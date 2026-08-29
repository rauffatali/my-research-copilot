# Scientific Report Formatting Guide

This guide supports the `scientific-writing` skill.

Use it for generic internal scientific reports, draft research summaries, lab notes, technical reports, and shareable intermediate artifacts.

For venue-specific manuscript, conference, journal, poster, grant, or camera-ready formatting, use `venue-templates`.

For prior author style adaptation, use `prior-style-adapter`.

For result-table scaffolding, use `results-scaffold`.

---

## 1. Purpose

This guide helps agents format generic scientific reports without pretending they are final venue submissions.

It should support:

- readable internal reports;
- evidence-first structure;
- visible TODOs;
- citation-aware writing;
- clear tables and figures;
- conservative claims;
- reproducible research summaries.

It should not replace venue-specific templates or submission instructions.

---

## 2. Use This Guide For

Use this guide when preparing:

- internal research summaries;
- project progress reports;
- experiment summaries;
- literature synthesis reports;
- claim audit reports;
- peer-review response notes;
- methodology notes;
- draft technical reports;
- supervisor/advisor-readable summaries.

Do not use it as the final authority for:

- CVPR / ICCV / ECCV / NeurIPS / ICML / ICLR formatting;
- IEEE / ACM / Springer / Elsevier / Nature / Science templates;
- journal submission rules;
- camera-ready formatting;
- poster templates;
- grant proposal formatting.

Use `venue-templates` for those cases.

---

## 3. Evidence-First Report Structure

A generic scientific report may use this structure:

```text
Title
Author / Agent
Date
Project
Status

Abstract or Executive Summary
1. Purpose
2. Background / Context
3. Method or Approach
4. Evidence / Experiments / Sources
5. Results or Findings
6. Interpretation
7. Limitations
8. Recommended Next Steps
9. References
10. Appendix
```

Include only sections that are relevant.

Do not add empty formal sections just for polish.

---

## 4. Required Metadata

At the top of a report, include:

```text
Title:
Project:
Author / Agent:
Date:
Status:
Evidence sources:
```

Recommended status labels:

- `draft`;
- `preliminary`;
- `evidence incomplete`;
- `ready for claim audit`;
- `ready for peer review`;
- `final internal report`.

If the report includes claims that have not been audited, say so.

---

## 5. TODO Markers

Use visible TODO markers for missing support.

Examples:

```text
TODO: needs citation
TODO: needs literature-review support
TODO: needs result
TODO: needs ablation
TODO: needs baseline
TODO: needs claim audit
TODO: needs citation-management verification
TODO: needs venue-template check
TODO: needs figure artifact
```

Do not hide missing evidence behind polished prose.

---

## 6. Citation Handling

For generic reports:

- use existing verified citation keys when available;
- mark missing citations with TODOs;
- do not invent citation keys;
- do not invent references;
- use `citation-management` for reference verification.

Example:

```latex
Prior work has commonly formulated the target visual task as an object detection problem~\cite{TODO_NEEDS_VERIFIED_CITATION}.
```

Better when no verified key exists:

```text
TODO: needs citation for the target visual task's object-detection framing.
```

---

## 7. Tables

Tables should be used for structured information, such as:

- experiment summaries;
- baseline comparisons;
- ablation plans;
- source lists;
- claim audit matrices;
- limitation summaries;
- review comments.

Table rules:

- include clear column names;
- do not invent values;
- mark missing values as TODO;
- include units and metrics;
- state whether values are final or preliminary.

Example:

```text
| Method | Dataset split | Metric | Result | Status |
|---|---|---:|---:|---|
| Baseline | test | mAP | TODO | pending verified run |
```

Use `results-scaffold` for result-table placeholders.

---

## 8. Figures

Figures should support explanation or evidence.

Use:

- `scientific-schematics` for technical diagrams, method workflows, architecture figures, and scientific schematics;
- `generate-image` for non-technical general visual assets;
- `results-scaffold` for tables and result-layout scaffolds.

Do not describe a figure as completed unless it exists.

Use placeholders:

```text
TODO: add method pipeline schematic.
TODO: add qualitative failure-case figure.
```

---

## 9. Claim Strength

Keep report claims proportional to evidence.

Avoid:

- “proves”;
- “solves”;
- “state-of-the-art”;
- “robust”;
- “generalizes”;
- “significantly improves”;
- “real-world ready”;

unless evidence supports that exact wording.

Prefer:

- “suggests”;
- “provides evidence that”;
- “under the evaluated protocol”;
- “in the current setting”;
- “requires further validation”;
- “preliminary results indicate”.

Use `claim-auditor` before finalizing claim-heavy reports.

---

## 10. Human Scientific Style

Reports should sound like careful human research writing, not generic AI prose.

Avoid overly perfect, generic, or inflated prose.

Weak:

```text
Artificial intelligence has revolutionized numerous domains and provides unprecedented opportunities.
```

Better:

```text
Computer vision methods are increasingly used for visual inspection tasks, including automated inspection in scientific and industrial settings.
```

Use `prior-style-adapter` if the report should match the author’s previous writing style.

---

## 11. LaTeX Report Notes

When using the provided LaTeX template:

- keep TODOs visible;
- do not invent citations;
- do not insert final numbers before verification;
- preserve labels and references;
- use placeholders for missing figures/tables;
- do not convert this generic template into a venue-specific submission template.

Use `venue-templates` for venue compliance.

---

## 12. Final Report Checklist

Before finishing a report:

- [ ] purpose is clear;
- [ ] status is marked;
- [ ] evidence sources are listed;
- [ ] unsupported claims are marked;
- [ ] missing citations are marked;
- [ ] result values are verified or marked TODO;
- [ ] tables/figures are real or marked TODO;
- [ ] limitations are visible;
- [ ] next steps are concrete;
- [ ] claim-heavy text is routed to `claim-auditor`;
- [ ] citation/reference issues are routed to `citation-management`;
- [ ] venue formatting needs are routed to `venue-templates`.

---

## Final Reminder

Formatting should make the evidence easier to inspect.

It should never make incomplete evidence look final.
