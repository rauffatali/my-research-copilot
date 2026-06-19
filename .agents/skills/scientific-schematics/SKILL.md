---
name: scientific-schematics
description: Create evidence-aware scientific and technical diagrams such as neural network architectures, method pipelines, system diagrams, data-processing workflows, experiment protocols, flowcharts, and scientific schematics. Use when a figure must communicate verified technical structure. Do not use for decorative/general images; use generate-image for non-technical visuals. Do not invent model components, pipeline stages, datasets, metrics, results, or causal relations.
---

# Scientific Schematics

## Overview

Scientific Schematics creates technical visual artifacts for research manuscripts, reports, posters, slides, proposals, and documentation.

Use this skill for diagrams that explain scientific or technical structure, such as:

- neural network architectures;
- model pipelines;
- system diagrams;
- data-processing workflows;
- experiment protocols;
- evaluation pipelines;
- flowcharts;
- algorithms;
- biological or scientific pathways;
- circuit or instrumentation diagrams;
- technical graphical abstracts.

The goal is not to create attractive images by default. The goal is to create scientifically accurate diagrams that communicate verified structure clearly.

This skill may use AI generation scripts or other diagram-generation tools, but the scientific content must come from evidence or explicit user instruction.

---

## Core Principle: Evidence-Aware Diagrams

Do not invent diagram content.

A scientific schematic must be grounded in:

- explicit user instructions;
- manuscript text;
- project documentation;
- code or configuration;
- experiment plans;
- run/output artifacts;
- verified method descriptions;
- approved research context.

If the needed information is missing, create a diagram specification with TODOs instead of guessing.

Examples of forbidden invention:

- adding model blocks not present in the method;
- adding arrows that imply unsupported causal flow;
- adding datasets not used;
- adding metrics not measured;
- adding result values;
- adding baselines not in scope;
- adding deployment steps not described;
- adding biological pathway links not provided or verified;
- implying that planned work is completed.

---

## Relationship to Other Skills

Use the smallest relevant skill combination.

| Need | Use |
|---|---|
| Create technical/scientific diagrams | `scientific-schematics` |
| Generate decorative, conceptual, photographic, or non-technical images | `generate-image` |
| Draft manuscript prose around a figure | `scientific-writing` |
| Apply venue-specific figure size, format, or placement rules | `venue-templates` |
| Scaffold result tables or result-section structure | `results-scaffold` |
| Check whether figure-related claims are supported | `claim-auditor` |
| Critique whether the diagram reflects a sound method/evaluation | `scientific-critical-thinking` |
| Simulate reviewer critique of figures | `peer-review` |

Recommended manuscript visual workflow:

```text
paper/docs/src/configs/runs/outputs
    → scientific-schematics
    → paper/agent/figure_support.md
    → scientific-writing
    → claim-auditor
    → venue-templates
```

For non-technical visuals:

```text
generate-image
    → venue-templates
```

---

## Boundary With Generate Image

Use `scientific-schematics` for technical diagrams where correctness matters.

Use `generate-image` for:

- decorative images;
- concept art;
- general illustrations;
- photos or photo-realistic images;
- non-technical visual assets;
- artwork for presentations;
- visual mood boards;
- general-purpose image editing.

If the requested image contains technical structure, process flow, scientific labels, architecture components, or causal arrows, use `scientific-schematics`.

If the requested image is primarily aesthetic, use `generate-image`.

---

## When to Use This Skill

Use this skill when creating or revising:

- method pipeline figures;
- architecture diagrams;
- neural network block diagrams;
- data collection workflows;
- preprocessing diagrams;
- training/evaluation diagrams;
- experiment protocol figures;
- ablation diagrams;
- system architecture diagrams;
- flowcharts;
- algorithm diagrams;
- technical graphical abstracts;
- domain workflow schematics;
- scientific process diagrams;
- poster technical figures;
- grant proposal schematics.

Use it when the figure is expected to support a scientific explanation or manuscript claim.

---

## Do Not Use This Skill For

Do not use this skill to:

- create general artwork;
- generate decorative images;
- invent visual evidence;
- invent model components;
- invent results;
- invent metrics;
- invent datasets;
- invent arrows or causal relations;
- replace source verification;
- replace claim auditing;
- replace venue figure-format checks;
- make a figure look publication-ready while its content is scientifically unsupported.

A beautiful wrong diagram is worse than no diagram.

---

## Evidence and Context Sources

For repository-grounded schematics, inspect relevant context:

- `paper/` for figure callouts, captions, and manuscript method text;
- `docs/PROJECT_PLAN.md` for project scope;
- `docs/research_gates.md` for approved workflow constraints;
- `docs/research_context.md` for problem framing;
- `docs/current_status.md` for what is complete;
- `src/` for implementation structure;
- `scripts/` for pipelines;
- `configs/` for model/training/evaluation settings;
- `runs/` for experiment structure;
- `outputs/` for generated predictions, plots, or summaries.

If the user provides a precise diagram description, that can be used directly. Still mark unsupported assumptions.

---

## Diagram Planning Workflow

Before generating or drawing a schematic:

1. Identify the diagram purpose.
2. Identify the intended audience and document type.
3. Identify the evidence source.
4. List required components.
5. List required labels.
6. Define the flow direction.
7. Define what should not be shown.
8. Identify missing information.
9. Produce a diagram specification.
10. Generate or recommend generation only after the specification is clear.

Do not skip the specification step for complex research diagrams.

---

## Reference-Driven Figure Workflow

For publication-facing scientific visuals, use a reference-driven workflow inspired by academic illustration agents.

Required inputs:

- source context: method text, result notes, project plan, code, outputs, or explicit user instruction;
- communicative intent: caption, figure goal, section purpose, or audience need;
- evidence source: the artifact(s) that make the figure content supportable.

Preferred flow:

1. Figure brief: identify source context, communicative intent, figure type, audience, venue constraints, and what must not be shown.
2. Reference retrieval: find or list relevant reference examples and explain whether they are useful for structure, style, or both.
3. Diagram specification: define components, labels, arrows, layout, unsupported assumptions, TODOs, and output target.
4. Style plan: define palette, typography, containers, arrows, line weights, icon policy, density, and readability constraints.
5. Candidate generation: generate the figure using the safest appropriate method.
6. Critic review: evaluate candidates for faithfulness, conciseness, readability, aesthetics, caption alignment, and evidence support.
7. Iteration: revise only when the critique identifies a concrete content, layout, or style fix.
8. Finalization: save the selected figure and record the final decision in `paper/agent/figure_support.md`.

For methodology diagrams, architecture figures, workflows, and evidence-sensitive visuals, prefer structured outputs such as SVG, Mermaid, TikZ, Python drawing code, or diagram specifications that can be audited.

For statistical plots, prefer code-generated figures from real `runs/` or `outputs/` data. Do not use direct image generation for plots that encode measured values.

Raster image generation may be used only as a rendering backend after the diagram specification is locked and the generated image is critiqued against the source context and caption.

---

## Diagram Specification Format

Use this format before generation when the diagram is non-trivial.

```md
## Diagram Specification

### Purpose

[What the diagram should communicate.]

### Evidence Source

- [file/user instruction/artifact]

### Diagram Type

[architecture / pipeline / workflow / flowchart / protocol / pathway / system diagram]

### Required Components

- [component]

### Required Connections

- [A → B]
- [B → C]

### Labels

- [label]

### Layout

[left-to-right / top-to-bottom / layered / swimlane / panel layout]

### Must Not Include

- [unsupported component or claim]

### TODOs / Missing Information

- TODO: [missing detail]

### Output Target

[file path, document type, size/format if known]
```

---

## Diagram Types

Choose the smallest diagram type that communicates the point.

---

### 1. Neural Network Architecture

Use for model structure.

Include only verified components:

- inputs;
- backbone;
- encoder/decoder;
- attention blocks;
- fusion blocks;
- heads;
- losses, if relevant;
- outputs.

Avoid:

- invented layers;
- unexplained “feature enhancement” blocks;
- unsupported attention/fusion mechanisms;
- metric/result annotations unless verified.

---

### 2. Method Pipeline

Use for end-to-end process.

Typical stages:

```text
input data → preprocessing → model → postprocessing → output/evaluation
```

Include only actual or planned stages from evidence.

Mark planned or missing stages as TODO.

---

### 3. Data Processing Workflow

Use for dataset preparation.

Include:

- raw data;
- filtering;
- annotation;
- splitting;
- preprocessing;
- augmentation;
- train/validation/test separation.

Be careful with leakage-sensitive flows.

If leakage risk exists, recommend `scientific-critical-thinking`.

---

### 4. Training and Evaluation Protocol

Use for experiment explanation.

Include:

- train split;
- validation split;
- test split;
- training loop;
- model selection;
- metrics;
- baseline comparison.

Do not imply test-set tuning unless that is actually the protocol.

---

### 5. Ablation or Experiment Design Diagram

Use for explaining controlled comparisons.

Include:

- full model;
- variants;
- controlled factor;
- common dataset/split;
- metric target.

Do not show a component as beneficial until results are verified.

---

### 6. System Architecture

Use for software/hardware/system diagrams.

Include:

- components;
- interfaces;
- data flow;
- protocols if known;
- storage/compute elements.

Do not invent external services, protocols, or deployment steps.

---

### 7. Scientific Pathway or Process

Use for biological, physical, chemical, or domain process schematics.

Only include pathway relationships that are provided or verified.

If the pathway requires factual scientific lookup and the source is missing, request or route to appropriate research lookup.

---

### 8. Technical Graphical Abstract

Use when a venue or manuscript needs a compact technical overview.

Include:

- problem/input;
- core method;
- evaluation/output;
- key supported message.

Do not include final performance claims unless verified.

Use `venue-templates` to check whether a graphical abstract is required.

---

## Prompting Rules for AI Generation

When using an AI generation script, the prompt should be precise and evidence-bound.

Include:

- diagram type;
- layout direction;
- exact components;
- exact arrows;
- required labels;
- style constraints;
- what to exclude;
- output format/size if known.

Example:

```text
Create a clean left-to-right method pipeline diagram with five blocks:
(1) input road image, (2) preprocessing, (3) detector backbone, (4) detection head,
(5) bounding-box output. Show arrows only between adjacent blocks. Do not include
performance numbers, datasets, or deployment components. Use simple labels and a
white background.
```

Avoid vague prompts:

```text
Make a powerful AI road damage detection figure.
```

Vague prompts invite hallucinated visual content.

---

## Quality Review Standards

Review generated schematics for:

- scientific correctness;
- component completeness;
- unsupported additions;
- missing components;
- misleading arrows;
- label readability;
- layout clarity;
- accessibility;
- color contrast;
- font size;
- journal/venue constraints;
- consistency with manuscript text.

A generated diagram is not automatically correct.

Quality review is approximate. Manual scientific verification is required.

---

## Accessibility and Publication Standards

Prefer:

- clear labels;
- high contrast;
- readable font size;
- colorblind-safe palettes;
- simple layout;
- consistent shapes and arrows;
- minimal decorative elements;
- vector output when possible;
- high-resolution raster output when vector is not possible.

Avoid:

- tiny text;
- excessive colors;
- cluttered arrows;
- ambiguous icons;
- unlabelled components;
- decorative effects that reduce clarity;
- color-only meaning without labels or patterns.

Use `venue-templates` for final figure format, dimensions, and resolution requirements.

---

## Output Locations

For manuscript projects, typical output paths are:

```text
paper/figures/
figures/
outputs/figures/
```

Use the project’s existing convention when available.

Save:

- final figure;
- source prompt/specification;
- review notes;
- version history if generated iteratively.

Recommended companion file:

```text
figure_name_spec.md
```

or:

```text
figure_name_review.json
```

---

## Script Usage

This skill may include helper scripts such as:

```text
scripts/generate_schematic.py
scripts/generate_schematic_ai.py
scripts/example_usage.sh
```

Use them as implementation helpers only.

Important rules:

- API-based generation requires user/environment configuration.
- The current repo-owned AI schematic scripts use `OPENROUTER_API_KEY`.
- `GEMINI_API_KEY` and `OPENAI_API_KEY` may appear as direct-provider placeholders in `.env.example`, but do not assume direct-provider support unless the local script explicitly implements it.
- The schematic CLI now supports `--provider openrouter|google|openai`; OpenRouter keeps the full iterative critic loop, while direct providers generate the figure and require manual scientific review.
- Do not expose API keys.
- Do not hardcode secrets.
- Do not claim the generated image is publication-ready without review.
- Do not treat an automated quality score as scientific validation.
- Do not regenerate repeatedly without clear benefit.

If scripts rely on external APIs, output should clearly state:

```text
Generated diagram requires manual scientific verification before manuscript use.
```

---

## Captions and Manuscript Integration

After creating a diagram, a caption should be written or revised through `scientific-writing`.

Caption should describe:

- what the diagram shows;
- what each major component means;
- whether the diagram is conceptual, planned, or implemented;
- what evidence/source it is based on.

Do not write captions that claim results unless evidence exists.

Use `claim-auditor` for figure-caption claims.

Use `venue-templates` for caption format and figure placement.

---

## Output Formats

Choose the smallest useful output.

---

### Diagram Specification Only

Use when information is incomplete.

```md
## Diagram Specification

[spec]

## Missing Information

- TODO: [missing detail]

## Recommended Next Step

[provide missing details / inspect code / use scientific-schematics generation / claim-auditor]
```

---

### Generation Prompt Output

Use when creating a prompt for a generation script.

```md
## Evidence-Grounded Generation Prompt

[prompt]

## Exclusions

- [do not include]

## Manual Review Checklist

- [check]
```

---

### Figure Handoff Output

Use after figure creation.

```md
## Figure Handoff

### Figure File

[path]

### Source Evidence

- [source]

### What It Shows

[description]

### What It Does Not Show

[limitations]

### Required Checks

- [ ] scientific correctness
- [ ] claim-auditor for caption claims
- [ ] venue-templates for size/format
```

---

## Important Rules

- Do not invent model components.
- Do not invent pipeline stages.
- Do not invent datasets.
- Do not invent metrics.
- Do not invent results.
- Do not invent causal arrows.
- Do not create decorative images under this skill.
- Do not hide missing technical details.
- Do not treat generated diagrams as automatically correct.
- Do not expose API keys.
- Do not bypass venue figure requirements.
- Do not make figure captions stronger than evidence.
- Keep diagrams aligned with manuscript and project evidence.

---

## Good Outputs

Good outputs include:

- evidence-grounded diagram specifications;
- accurate architecture diagrams;
- method pipeline figures;
- training/evaluation protocol diagrams;
- data workflow figures;
- clean flowcharts;
- caption-safe figure descriptions;
- manual review checklists;
- clear TODOs for missing information.

Bad outputs include:

- beautiful but incorrect diagrams;
- invented technical blocks;
- unverified arrows;
- generated performance claims;
- decorative images presented as scientific figures;
- unreadable labels;
- cluttered visuals;
- figures inconsistent with manuscript text.

---

## Final Checklist

Before completing a scientific schematic task:

1. [ ] Diagram purpose is clear.
2. [ ] Evidence source or user instruction is identified.
3. [ ] Required components are listed.
4. [ ] Required connections/arrows are listed.
5. [ ] Unsupported components are excluded.
6. [ ] Missing information is marked as TODO.
7. [ ] Diagram type is appropriate.
8. [ ] Layout is specified.
9. [ ] Labels are readable and precise.
10. [ ] No results, metrics, datasets, or causal relations are invented.
11. [ ] Generated output is manually reviewable.
12. [ ] Caption claims are routed to `claim-auditor`.
13. [ ] Final format requirements are routed to `venue-templates`.
14. [ ] General non-technical images are routed to `generate-image`.

---

## Final Reminder

Scientific schematics are visual claims.

A schematic should make the research easier to understand without adding anything the evidence does not support.
