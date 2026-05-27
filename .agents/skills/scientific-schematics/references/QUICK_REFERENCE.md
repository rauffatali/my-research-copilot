# Scientific Schematics Quick Reference

Use this quick reference when creating evidence-aware technical diagrams.

For non-technical images, use `generate-image`.

For final venue size/format requirements, use `venue-templates`.

For figure captions and manuscript prose, use `scientific-writing`.

For figure-related claims, use `claim-auditor`.

---

## 1. Decide Whether This Skill Applies

Use `scientific-schematics` if the figure includes:

- technical components;
- architecture blocks;
- process steps;
- arrows or causal/temporal flow;
- scientific labels;
- method stages;
- experiment protocol;
- data workflow;
- system components;
- pathway relationships.

Use `generate-image` if the image is:

- decorative;
- photographic;
- conceptual art;
- non-technical illustration;
- general-purpose visual asset.

---

## 2. Evidence Checklist

Before making a diagram, identify the evidence source.

```text
[ ] explicit user description
[ ] manuscript text
[ ] docs/
[ ] src/
[ ] configs/
[ ] scripts/
[ ] runs/
[ ] outputs/
[ ] verified external source
```

If none exists, create a specification with TODOs.

---

## 3. Diagram Specification Template

```md
## Diagram Specification

### Purpose

[What the diagram should communicate.]

### Evidence Source

- [source]

### Diagram Type

[architecture / pipeline / workflow / protocol / flowchart / pathway / system diagram]

### Required Components

- [component]

### Required Connections

- [A → B]

### Labels

- [label]

### Layout

[left-to-right / top-to-bottom / layered / swimlane / panel layout]

### Must Not Include

- [unsupported item]

### TODOs

- TODO: [missing information]

### Output Target

[path, format, document type]
```

---

## 4. Safe Prompt Template

Use this when calling a diagram-generation script or AI image model.

```text
Create a clean scientific [diagram type] for [purpose].

Use only the following components:
1. [component]
2. [component]
3. [component]

Use only the following connections:
- [A] → [B]
- [B] → [C]

Required labels:
- [label]

Layout:
- [left-to-right / top-to-bottom / panel layout]

Style:
- white or light background
- high contrast
- readable labels
- simple shapes
- no decorative effects
- colorblind-safe colors if color is used

Do not include:
- performance numbers
- unsupported datasets
- extra model blocks
- deployment components
- causal arrows not listed above
- claims such as “best,” “robust,” or “state-of-the-art”
```

---

## 5. Safe Examples

### Method Pipeline

```text
Create a left-to-right road damage detection pipeline with five blocks:
input road image → preprocessing → detector backbone → detection head → bounding-box output.
Use only these blocks. Do not include performance metrics, dataset names, or deployment steps.
```

### Training/Evaluation Protocol

```text
Create a top-to-bottom experiment protocol diagram:
dataset → train/validation/test split → model training on train split → model selection on validation split → final evaluation on test split → metric report.
Do not show test-set tuning.
```

### Architecture Diagram

```text
Create a block diagram of the verified model architecture:
input image → encoder → feature fusion → prediction head → output mask.
Use simple rectangular blocks and arrows. Do not add attention modules or losses unless listed.
```

---

## 6. Unsafe Prompts

Avoid:

```text
Make an impressive AI figure for our method.
```

```text
Create a state-of-the-art architecture diagram.
```

```text
Show that our method improves road damage detection.
```

These invite unsupported content.

---

## 7. Manual Review Checklist

After generation or drawing:

- [ ] All components are supported by evidence.
- [ ] No extra components were added.
- [ ] Arrows match actual flow.
- [ ] Labels are correct.
- [ ] No unverified metrics or results appear.
- [ ] No unsupported dataset or baseline appears.
- [ ] Layout is readable.
- [ ] Text is legible.
- [ ] Colors are accessible.
- [ ] Caption claims are routed to `claim-auditor`.
- [ ] Format requirements are routed to `venue-templates`.

---

## 8. Common Handoffs

| Need | Skill |
|---|---|
| Caption/prose | `scientific-writing` |
| Figure claim support | `claim-auditor` |
| Venue sizing/format | `venue-templates` |
| Result tables | `results-scaffold` |
| Non-technical image | `generate-image` |
| Scientific/method critique | `scientific-critical-thinking` |
| Reviewer-style figure critique | `peer-review` |

---

## 9. Output Paths

Common paths:

```text
paper/figures/
figures/
outputs/figures/
```

Also save specification/review notes when possible:

```text
figure_name_spec.md
figure_name_review.json
```

---

## Final Reminder

If the diagram would require guessing, stop at a specification with TODOs.
