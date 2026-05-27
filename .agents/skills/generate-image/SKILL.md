---
name: generate-image
description: Generate or edit general-purpose non-technical images, including photos, illustrations, artwork, concept art, presentation visuals, backgrounds, and visual assets. Use scientific-schematics instead for technical diagrams, scientific schematics, workflows, method pipelines, architectures, flowcharts, circuits, pathways, or evidence-sensitive figures. Do not use this skill to fabricate scientific evidence, results, datasets, model structures, or technical claims.
---

# Generate Image

## Overview

Generate Image creates or edits general-purpose visual assets.

Use this skill for images where the main goal is visual expression, illustration, presentation support, or non-technical imagery.

Examples:

- photos or photorealistic images;
- artistic illustrations;
- concept art;
- non-technical presentation visuals;
- backgrounds;
- visual assets for reports or slides;
- simple illustrative images;
- image editing or modification;
- style transfer;
- general-purpose image generation.

Do not use this skill for technical or evidence-sensitive scientific diagrams.

For technical diagrams, use `scientific-schematics`.

---

## Core Boundary

Use `generate-image` for general visuals.

Use `scientific-schematics` when the image contains:

- arrows representing technical flow;
- architecture blocks;
- method pipeline stages;
- experimental protocol;
- data-processing workflow;
- system diagram;
- circuit diagram;
- biological/scientific pathway;
- technical labels;
- scientific schematic structure;
- figure content that must match manuscript evidence exactly.

If a visual could be interpreted as a scientific claim, route to `scientific-schematics` or `claim-auditor`.

---

## Relationship to Other Skills

| Need | Use |
|---|---|
| General image generation or editing | `generate-image` |
| Technical/scientific diagrams | `scientific-schematics` |
| Figure size, format, or venue rules | `venue-templates` |
| Caption or manuscript prose | `scientific-writing` |
| Caption/figure claim support | `claim-auditor` |
| Result tables or result placeholders | `results-scaffold` |
| Reviewer critique of figures | `peer-review` |

Recommended workflow for general visuals:

```text
generate-image
    → scientific-writing for caption/prose if needed
    → venue-templates for final size/format if used in a submission
```

For technical figures:

```text
scientific-schematics
    → paper/agent/figure_support.md
    → claim-auditor
    → venue-templates
```

`generate-image` may be used as a raster rendering backend for a technical figure only after `scientific-schematics` has produced a locked diagram specification. It should not decide the scientific content of the figure.

---

## When to Use This Skill

Use this skill when the user asks for:

- general image generation;
- image editing;
- visual assets;
- photo-style images;
- illustrations;
- artwork;
- concept visuals;
- decorative or background images;
- presentation title visuals;
- non-technical report images;
- style transformations;
- removing/changing visual elements in a general image;
- creating a mood, scene, or non-technical concept image.

---

## Do Not Use This Skill For

Do not use this skill for:

- neural network architecture diagrams;
- method pipeline diagrams;
- workflow diagrams;
- experiment protocol diagrams;
- technical flowcharts;
- circuit diagrams;
- biological pathways;
- scientific schematics;
- result tables;
- plots or charts;
- evidence-sensitive figures;
- medical/scientific claims;
- fabricated datasets or experiments;
- model components not provided by evidence;
- results or metrics;
- anything that must be technically exact.

Use `scientific-schematics`, `results-scaffold`, or another appropriate skill instead.

---

## Research Safety Rules

Generated images must not fabricate research evidence.

Do not generate images that imply:

- an experiment was performed;
- a dataset exists;
- a result was obtained;
- a model has a specific architecture;
- a method has specific pipeline stages;
- a biological or physical mechanism is verified;
- a medical/scientific claim is true;
- a deployment system exists;
- a figure is evidence from the project.

If the image is conceptual, label it conceptually in any caption or surrounding text.

Example safe caption:

```text
Conceptual illustration generated for presentation background; not an experimental result.
```

Unsafe caption:

```text
Example output from our model.
```

unless it is actually from verified project outputs.

---

## Image Editing Rules

When editing an existing image:

- preserve the user’s requested subject and intent;
- do not add scientific meaning unless requested and supported;
- do not alter data visualizations or scientific figures in a way that changes evidence;
- do not edit plots, graphs, or result figures to change apparent results;
- route technical diagram edits to `scientific-schematics`;
- route venue-specific sizing/format issues to `venue-templates`.

---

## Prompting Guidance

Good prompts are specific about visual style and content.

Include:

- subject;
- setting;
- style;
- composition;
- aspect ratio or output size if needed;
- mood;
- color/lighting if relevant;
- what to exclude.

Good prompt:

```text
Create a clean, non-technical presentation background showing an abstract road surface texture with subtle blue lighting, no text, no icons, no charts.
```

Bad prompt for this skill:

```text
Create a road damage detection pipeline with arrows from dataset to detector to evaluation metrics.
```

That belongs to `scientific-schematics`.

---

## Output Locations

Common output locations:

```text
assets/images/
figures/
paper/figures/
slides/images/
outputs/images/
```

Use the project’s existing convention when available.

For manuscript or venue use, route final format checks to `venue-templates`.

---

## Local Script Usage

This skill may include:

```text
scripts/generate_image.py
```

The script may require:

```text
OPENROUTER_API_KEY
```

Use environment variables or a local `.env` file.

Direct provider placeholders may exist in `.env.example`:

```text
GEMINI_API_KEY
OPENAI_API_KEY
```

Do not assume these direct providers are active unless the local generation script explicitly supports them. The current repo-owned script defaults to OpenRouter, but the CLI now exposes `--provider openrouter|google|openai` for the supported backends.

Do not expose API keys.

Do not hardcode secrets.

Generated images should be reviewed before use.

---

## Output Formats

### General Image Request

```md
## Image Generation Plan

Purpose:
Output path:
Prompt:
Exclusions:
Need venue check: yes/no
Need caption: yes/no
```

### Image Handoff

```md
## Image Handoff

Image file:
Purpose:
Conceptual or evidence-based:
Required checks:
- [ ] caption does not imply scientific evidence
- [ ] venue format checked if used in submission
```

---

## Important Rules

- Do not create technical diagrams with this skill.
- Do not fabricate scientific evidence.
- Do not fabricate results, datasets, or model structures.
- Do not make conceptual visuals look like project outputs.
- Do not alter scientific plots or result figures to change evidence.
- Do not expose API keys.
- Do not treat generated images as manuscript evidence.
- Use `scientific-schematics` for technical figures.
- Use `venue-templates` for final figure format.
- Use `claim-auditor` for figure/caption claims.

---

## Final Checklist

Before completing a generate-image task:

1. [ ] The image is general/non-technical.
2. [ ] It does not require scientific schematic accuracy.
3. [ ] It does not fabricate research evidence.
4. [ ] It does not imply verified results unless evidence exists.
5. [ ] Technical diagrams are routed to `scientific-schematics`.
6. [ ] Venue formatting needs are routed to `venue-templates`.
7. [ ] Captions/prose are routed to `scientific-writing` if needed.
8. [ ] Claim-sensitive captions are routed to `claim-auditor`.

---

## Final Reminder

Generate Image creates visual assets.

It does not create scientific evidence.
