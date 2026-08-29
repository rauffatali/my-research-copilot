# Best Practices for Scientific Schematics

Use this reference with the `scientific-schematics` skill when creating technical scientific diagrams.

The goal is scientific clarity, not decorative polish.

---

## 1. Evidence Grounding

A diagram should be grounded in evidence or explicit instruction.

Acceptable sources:

- user-provided diagram description;
- manuscript method text;
- project documentation;
- code;
- configs;
- experiment plans;
- run/output artifacts;
- verified external sources.

If the diagram includes content not in the evidence, mark it as:

```text
TODO
conceptual
planned
hypothetical
```

or remove it.

---

## 2. No-Invention Rules

Do not invent:

- model layers;
- attention modules;
- fusion blocks;
- losses;
- datasets;
- metrics;
- results;
- baselines;
- experimental steps;
- deployment steps;
- causal arrows;
- biological pathway links;
- data sources;
- evaluation slices.

A schematic can mislead as strongly as a false sentence.

---

## 3. Diagram Types and Good Use

### Architecture Diagram

Best for:

- model blocks;
- data flow through network;
- input/output structure.

Needs evidence from:

- method text;
- code;
- configs.

Avoid:

- adding trendy modules not present in the model.

---

### Method Pipeline

Best for:

- end-to-end process;
- preprocessing;
- model inference;
- postprocessing;
- outputs.

Needs evidence from:

- method description;
- scripts;
- project docs.

Avoid:

- showing deployment or evaluation steps that are not part of the method.

---

### Data Workflow

Best for:

- collection;
- annotation;
- filtering;
- splitting;
- preprocessing;
- augmentation.

Needs evidence from:

- dataset docs;
- preprocessing scripts;
- split files.

Be careful with leakage-sensitive arrows.

---

### Training/Evaluation Protocol

Best for:

- train/validation/test separation;
- model selection;
- baseline comparison;
- metric reporting.

Needs evidence from:

- experiment plan;
- configs;
- runs;
- evaluation scripts.

Avoid:

- implying test-set tuning.

---

### System Diagram

Best for:

- software or hardware components;
- data interfaces;
- cloud/local components;
- sensor pipelines.

Needs evidence from:

- architecture docs;
- code;
- deployment notes.

Avoid:

- adding services or protocols not documented.

---

### Scientific Pathway

Best for:

- biological/chemical/physical processes;
- causal or temporal scientific processes.

Needs evidence from:

- verified source;
- domain documentation;
- user-provided pathway.

Avoid:

- hallucinated pathway links.

---

## 4. Visual Clarity Standards

Use:

- simple shapes;
- clear labels;
- consistent arrow direction;
- meaningful grouping;
- enough whitespace;
- high contrast;
- consistent font;
- consistent line weights;
- readable text at final size.

Avoid:

- clutter;
- excessive icons;
- shadows and decorative effects;
- tiny labels;
- ambiguous arrows;
- unlabeled colors;
- unnecessary 3D effects.

---

## 5. Typography

Use fonts that are readable and likely to work in publication contexts.

Recommended:

- Arial;
- Helvetica;
- Calibri;
- Liberation Sans;
- DejaVu Sans.

General guidance:

- labels should remain legible at final figure size;
- avoid decorative fonts;
- avoid all-caps labels except short acronyms;
- define abbreviations in caption or legend;
- keep label phrasing consistent with manuscript terms.

Do not include “Figure 1:” inside the image. The manuscript handles figure numbering.

---

## 6. Arrows and Flow

Arrows imply flow, dependency, or causality.

Use arrows only when the relationship is supported.

Arrow types should be consistent:

- solid arrows for primary flow;
- dashed arrows for optional or planned flow;
- dotted arrows for weak/indirect relation, if explained;
- no arrow when relationship is only grouping.

Avoid crossing arrows where possible.

Use one dominant flow direction:

- left-to-right;
- top-to-bottom;
- layered;
- swimlane.

---

## 7. Color and Accessibility

Use color to clarify, not decorate.

Prefer:

- colorblind-safe palettes;
- high contrast;
- labels or patterns in addition to color;
- limited number of colors;
- consistent color meaning.

Avoid:

- red/green-only distinctions;
- low-contrast pastel text;
- too many colors;
- color meaning not explained.

A diagram should remain understandable in grayscale when possible.

---

## 8. File Format Guidance

Use venue requirements as the final authority.

General guidance:

### Vector formats

Preferred for diagrams:

- PDF;
- SVG;
- EPS when required.

Best for:

- line diagrams;
- flowcharts;
- architecture figures;
- schematics.

### Raster formats

Use when vector is not available or accepted:

- PNG;
- TIFF.

For print, use high resolution, typically at least 300 DPI at final size.

Avoid JPEG for line diagrams because compression artifacts can reduce clarity.

Use `venue-templates` for exact requirements.

---

## 9. Caption Safety

Captions should describe what the diagram shows.

Good caption:

```text
Overview of the proposed visual detection pipeline, showing preprocessing, model inference, and bounding-box output stages.
```

Risky caption:

```text
The proposed pipeline robustly detects targets in real-world scenes.
```

Use `claim-auditor` for caption claims.

Do not include performance claims in captions unless supported by verified results.

---

## 10. Consistency With Manuscript

Before finalizing, check:

- component names match the method section;
- labels match terminology;
- figure is referenced in text;
- caption does not overclaim;
- diagram does not show unmentioned components;
- diagram does not omit critical components;
- figure order matches narrative flow.

Use `scientific-writing` to integrate figure references and captions.

---

## 11. Venue Constraints

Before submission, check:

- figure size;
- file format;
- resolution;
- font size;
- color mode;
- caption placement;
- panel labels;
- supplementary figure rules.

Use `venue-templates`.

Do not assume a generated image meets venue requirements.

---

## 12. AI Generation Review

If AI generation is used, review the output manually.

Check for:

- hallucinated components;
- incorrect text;
- misspelled labels;
- wrong arrows;
- extra datasets or metrics;
- misleading visual hierarchy;
- unreadable text;
- unwanted decorative elements.

Automated quality scores are helpful but not scientific validation.

---

## 13. Common Failure Modes

- diagram looks polished but is scientifically wrong;
- model includes blocks not in code;
- arrows imply unsupported causality;
- labels are too small;
- icons are ambiguous;
- figure includes fake metrics;
- caption overclaims;
- layout hides the main idea;
- diagram does not match manuscript text;
- venue format not checked.

---

## 14. Final Checklist

Before using a diagram in a manuscript:

- [ ] Purpose is clear.
- [ ] Evidence source is documented.
- [ ] Components are verified.
- [ ] Connections/arrows are verified.
- [ ] Missing details are marked TODO or removed.
- [ ] Labels are readable.
- [ ] Color is accessible.
- [ ] Caption is claim-safe.
- [ ] Figure is consistent with manuscript text.
- [ ] Output format is suitable.
- [ ] Venue requirements are checked.
- [ ] Figure claims are audited.

---

## Final Reminder

Scientific diagrams should simplify the truth, not decorate uncertainty.
