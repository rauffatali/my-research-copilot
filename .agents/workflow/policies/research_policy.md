# Research defaults

Before changing research direction, implementation, training, evaluation, or manuscript claims, define:

- project type,
- task,
- inputs,
- outputs,
- constraints,
- contribution target,
- validation strategy.

## Empirical ML / CV work

For model, loss, augmentation, training, or evaluation changes, state:

1. why it fits the current project scope,
2. what baseline it is compared against,
3. what metric or failure mode it targets,
4. how it will be ablated,
5. what risk it introduces.

Use `.agents/guidance/cv-researcher.md`, `.agents/guidance/cv-dev.md`, or `.agents/guidance/ai-ml-research-dev.md` for detailed expectations depending on the task.

Preserve reproducibility where possible:
- config,
- seed,
- dataset version,
- split definition,
- run identity,
- code version,
- metric definition.

Use leakage-safe splits and maintain data/label contracts.

Prefer slice-aware evaluation and qualitative failure analysis over headline metrics alone.

## Theoretical work

For theoretical claims or proposals, state:

1. definitions,
2. assumptions,
3. claim or proposition,
4. reasoning or derivation path,
5. relation to prior work,
6. limitations or cases not covered.

Do not present informal intuition as a proven result.

Use `theoretical-lens` when exploring whether a failure mode or design choice has a load-bearing mathematical framing, and label every mathematical claim using the rigor vocabulary in `.agents/workflow/policies/evidence_and_claim_policy.md`.

## Architectural novelty

For architecture or method-design proposals, state:

1. motivation,
2. prior method being improved or contrasted,
3. expected mechanism of improvement,
4. complexity or tradeoff introduced,
5. validation strategy,
6. minimal comparison needed.

Do not introduce architectural complexity without a clear contribution hypothesis.

Consider `theoretical-lens` when the expected mechanism of improvement may have a principled mathematical explanation beyond "this worked in similar settings," but do not force a mathematical framing onto a change that is only an empirical trick.

## Dataset, benchmark, or evaluation work

For dataset, benchmark, or evaluation changes, state:

1. data source or benchmark scope,
2. annotation or measurement contract,
3. possible bias or leakage risk,
4. evaluation protocol,
5. baseline or reference point,
6. limitations.