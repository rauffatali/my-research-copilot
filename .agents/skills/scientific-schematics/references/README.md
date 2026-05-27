# Scientific Schematics References

These references support the `scientific-schematics` skill.

Use this skill for evidence-aware scientific and technical diagrams, including:

- neural network architecture diagrams;
- method pipelines;
- data-processing workflows;
- training/evaluation protocols;
- system diagrams;
- flowcharts;
- scientific pathways;
- technical graphical abstracts.

Use `generate-image` for non-technical, decorative, photographic, or general-purpose images.

---

## Core Rule

A scientific schematic is a visual claim.

Do not invent:

- model components;
- pipeline stages;
- datasets;
- metrics;
- results;
- baselines;
- causal arrows;
- deployment steps;
- pathway relationships.

If information is missing, create a diagram specification with TODOs rather than guessing.

---

## Reference Files

### `QUICK_REFERENCE.md`

Use for fast diagram planning and prompt construction.

Includes:

- diagram selection;
- evidence checklist;
- safe prompt template;
- manual review checklist;
- handoffs.

### `best_practices.md`

Use for publication-quality technical diagram standards.

Includes:

- evidence grounding;
- figure types;
- accessibility;
- typography;
- file formats;
- caption safety;
- venue handoffs.

---

## Recommended Workflow

```text
evidence/context
    → diagram specification
    → generation or manual drawing
    → manual scientific verification
    → scientific-writing for caption/prose
    → claim-auditor for caption/figure claims
    → venue-templates for final size/format
```

---

## Evidence Sources

Use:

- explicit user description;
- `paper/`;
- `docs/`;
- `src/`;
- `configs/`;
- `scripts/`;
- `runs/`;
- `outputs/`.

If a diagram is based only on a rough idea, label it as conceptual or planned.

---

## AI Generation Note

AI generation scripts may be used as implementation helpers.

Generated diagrams are not automatically scientifically correct.

Always review:

- components;
- arrows;
- labels;
- omitted details;
- unsupported additions;
- consistency with manuscript and project evidence.

Do not expose API keys or hardcode secrets.

---

## Final Reminder

A clear schematic should reduce ambiguity.

It should not add unsupported scientific content.
