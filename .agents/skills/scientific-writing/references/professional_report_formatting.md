# Professional Report Formatting

This reference supports the `scientific-writing` skill for general scientific reports.

For venue-specific templates, page limits, LaTeX class files, and submission formatting, use `venue-templates`.

For prior author style, use `prior-style-adapter`.

---

## 1. Purpose

Professional formatting should make scientific content easier to read and audit.

Formatting should not hide weak evidence or make unsupported claims look stronger.

---

## 2. General Report Structure

A scientific report may include:

1. Title
2. Abstract or executive summary
3. Introduction
4. Background / Related Work
5. Methods
6. Experiments / Evaluation
7. Results
8. Discussion
9. Limitations
10. Conclusion
11. References
12. Appendix

Use only sections that fit the artifact.

For venue-specific structure, use `venue-templates`.

---

## 3. Section Headings

Headings should be:

- descriptive;
- concise;
- parallel when useful;
- aligned with the paper argument.

Avoid vague headings:

```text
More Details
Additional Information
Some Results
```

Prefer:

```text
Dataset and Split Construction
Baseline Comparison
Failure Case Analysis
```

---

## 4. Paragraph Formatting

Use readable paragraphs.

Avoid:

- giant paragraphs;
- one-sentence paragraphs everywhere;
- repetitive paragraph rhythm;
- overly perfect AI-like structure.

Good scientific reports use natural variation while staying clear.

---

## 5. Lists

Use lists for:

- contributions;
- experimental settings;
- limitations;
- reviewer responses;
- requirements;
- ablation factors.

Do not overuse lists in manuscript prose when a paragraph would read more naturally.

---

## 6. Tables

Use tables for structured information.

Good tables have:

- clear title/caption;
- meaningful columns;
- units;
- metric names;
- protocol notes;
- no invented values;
- consistent formatting.

Use `results-scaffold` for result-table placeholders.

---

## 7. Figures

Figures should be referenced in the text and support a claim or explanation.

Use:

- `scientific-schematics` for technical diagrams;
- `generate-image` for general images;
- `venue-templates` for placement/format constraints.

Do not describe missing figures as complete.

---

## 8. LaTeX Formatting

For LaTeX writing:

- preserve labels and references;
- do not invent citation keys;
- escape special characters when needed;
- keep TODOs visible;
- avoid changing template commands unless requested.

Use `venue-templates` for LaTeX class/template compliance.

---

## 9. Tone and Visual Cleanliness

Professional scientific formatting should be:

- readable;
- consistent;
- not cluttered;
- aligned with evidence;
- not overly decorative.

Avoid using formatting to compensate for unclear argumentation.

---

## 10. Formatting Checklist

Before finalizing a report:

- [ ] section structure matches the artifact purpose;
- [ ] headings are descriptive;
- [ ] paragraphs are readable and natural;
- [ ] tables/figures are referenced and supported;
- [ ] TODOs are visible;
- [ ] no unsupported claims are hidden by polish;
- [ ] venue-specific formatting is handed to `venue-templates`;
- [ ] prior style adaptation is handed to `prior-style-adapter`.

---

## Final Reminder

Professional formatting improves readability.

It does not replace evidence, citations, or claim support.
