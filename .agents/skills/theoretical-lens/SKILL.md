---
name: theoretical-lens
description: Use to identify when a research failure mode, architecture choice, or empirical trick has a load-bearing mathematical structure (geometric, topological, probabilistic/information-theoretic, optimization/variational, spectral, or statistical) worth making explicit as part of the contribution, instead of only adapting trendy architectures. Every mathematical claim must carry an explicit rigor label and a real source where applicable; never invents theorems or dresses up empirical tricks in unearned formalism. Use sparingly, only when the framing is load-bearing. For empirical/methodological critique use scientific-critical-thinking. For citation verification use citation-management. For manuscript claim auditing use claim-auditor.
---

# Theoretical Lens

## Overview

Most idea generation in this workflow is trend-following: find recent papers, adapt architectures, borrow tricks. That produces real, useful contributions, but it also produces the "why not the newer thing" reviewer trap, because trend-following novelty ages fast and invites endless comparator objections.

This skill is a different lens: given a failure mode, architecture choice, or empirical trick already under discussion, ask whether it has an underlying mathematical structure that can be made explicit and exploited as a more principled, defensible contribution — rather than only "we combined component A and component B because both are recent."

This is a creativity and framing aid, not a proof generator. It never invents new theorems, and it never dresses up an empirical trick in unearned formalism.

## Core Principle: Taste, Not Force-Fitting

Mathematical taste includes knowing when *not* to reach for mathematics. Before proposing a mathematical framing, check:

1. Is there a natural mathematical object underlying this failure mode? Examples: thin-structure fragmentation -> connectivity/topology; class imbalance -> extremal/robust statistics; boundary localization -> distance geometry; annotation noise or under-confidence -> probabilistic calibration; feature entanglement -> information bottleneck / mutual information; training instability -> spectral/Lipschitz conditioning; generalization gap -> statistical learning theory.
2. Would this framing change the experiment design, loss, or evaluation choice — or is it only relabeling an existing trick with fancier words?
3. Would a mathematically literate reviewer find it load-bearing, or would it read as decoration?

If the honest answer to (2) or (3) is "decorative," say so explicitly and drop the framing. A plain engineering explanation is often the correct, higher-integrity choice. Do not use this skill on every task; use it when it earns its place.

## When to Use This Skill

Use when:

- brainstorming a research direction and the contribution type under consideration is architectural novelty, adaptation-and-combination for a domain, or a theoretical contribution (see the Contribution Type field in `docs/agent/research_direction.md`);
- a failure mode has been identified and the current explanation is purely empirical ("this worked in practice") with no principled account of why;
- selecting or designing a loss function, regularizer, sampling strategy, or evaluation metric, and a more principled formulation might exist;
- a reviewer-anticipation exercise (`scientific-critical-thinking`, the novelty risk matrix) surfaces "the mechanism isn't well motivated" as a weakness;
- writing the Expected Mechanism field of `docs/agent/research_direction.md`, or a comparator's rationale in `docs/agent/novelty_risk_matrix.md`.

Do not use when:

- the task is simple engineering/implementation with no open design or mechanism question;
- a strong mathematical framing has already been found and cited — repeating it with new notation adds nothing;
- time pressure or task scope calls for a narrow fix, not a reframing exercise.

## Relationship to Other Skills

- `research-lookup` / `literature-review`: use these to find the actual paper that establishes a mathematical property. Never assert a connection to a named theorem, bound, or property from memory alone without checking it against a real source.
- `scientific-critical-thinking`: use after a mathematical framing is proposed, to pressure-test whether it is genuinely load-bearing or decorative, and whether it changes a falsifiable prediction.
- `claim-auditor`: use once manuscript prose asserts a mathematical property, to verify the sentence matches its rigor label and source.
- `citation-management`: use to verify the metadata of any paper cited as the source of a mathematical property.

## Rigor Vocabulary (Mandatory)

Every mathematical claim produced by this skill must carry exactly one label from the canonical vocabulary defined in `.agents/workflow/policies/evidence_and_claim_policy.md`:

- `proven` — a specific theorem or result, in a specific cited paper or standard reference, that directly applies here.
- `established_result` — a widely known mathematical fact (e.g., a standard inequality or a named distance/divergence property) that does not need a novel citation but should still be named precisely.
- `heuristic_analogy` — structurally inspired by a real mathematical object, but not proven to transfer to this exact setting.
- `empirically_motivated` — the technique works in practice; the mathematical framing is a plausible explanation, not a guarantee.
- `unverified_conjecture` — a new derivation or claim proposed here, not yet independently checked.

Do not invent a sixth label. Do not upgrade a label without new evidence (a citation found, or a derivation independently checked).

## Candidate Mathematical Lenses

Use the smallest relevant lens. These are starting points, not an exhaustive taxonomy, and every specific technique named below must still be checked against a real source before being cited in project artifacts.

### Geometric / Topological
Distance-transform and boundary-based reformulations of segmentation losses; connectivity- and skeleton-preserving losses grounded in topological invariants; shape priors as geometric constraints.

### Probabilistic / Information-Theoretic
Calibration and uncertainty quantification; entropy regularization; information-bottleneck framings of feature compression; label smoothing as an entropy-regularized target; interpolation-based augmentation as vicinal risk minimization.

### Optimization / Variational
Recasting a discrete evaluation metric (IoU, Dice) as a differentiable surrogate and examining its convexity/gradient behavior; regularization as a Lagrangian relaxation of a constrained problem; understanding why a loss landscape is easy or hard to optimize.

### Spectral / Algebraic
Spectral normalization and Lipschitz-bounded layers for stability or robustness claims; graph-Laplacian based smoothness priors when structure is graph-like.

### Statistical / Estimation-Theoretic
Bias-variance framing of a design choice; robust-statistics treatment of heavy-tailed or imbalanced classes; generalization-gap arguments from statistical learning theory, stated with their actual assumptions, not asserted loosely.

## Anti-Hallucination Rules

These are not optional.

- Do not name a theorem, bound, or named property without a specific citation or a fully shown derivation.
- Do not introduce notation, operators, or theorem-like framing ("Proposition 1", "Lemma") that is not load-bearing to the argument being made.
- Do not claim a property (convexity, boundedness, a Lipschitz constant, an unbiasedness result) without either citing the source or deriving it explicitly, step by step, in the artifact.
- Do not blur `heuristic_analogy` into `proven` language. Say "inspired by" or "analogous to," not "guarantees" or "proves," unless the label is `proven`.
- Do not claim a technique is "principled" or "theoretically motivated" in manuscript-facing text unless the rigor label and citation are attached.
- When uncertain whether a mathematical connection actually holds, say so plainly. A hedged, honest "this is a heuristic analogy, unverified in this specific setting" is a correct output. A confident-sounding but unverified mathematical claim is a failure of this skill, not a success.
- If a genuinely new derivation is proposed, show every step; do not skip steps and assert the conclusion. Mark it `unverified_conjecture` regardless of how convincing it looks, until independently checked.

## Durable Output

This skill's notes are not durable until written to a repository artifact, per `.agents/workflow/policies/tool_workflow_policy.md`. Depending on context, record a Theoretical Lens Note in:

- `docs/agent/research_direction.md`'s Expected Mechanism field, when it shapes the frozen direction;
- `docs/agent/novelty_risk_matrix.md`'s comparator ledger Rationale column, when it explains why a comparator is included, probed, or excluded;
- `docs/agent/hypotheses.md`, when it directly supports a specific hypothesis;
- `docs/agent/brainstorming_brief.md`, for exploratory notes that have not yet shaped a decision.

Do not leave a theoretical framing only in chat output.

## Output Format

```md
## Theoretical Lens Note

### Failure Mode / Phenomenon
[What is being explained or targeted.]

### Candidate Mathematical Structure
[The specific mathematical object, framing, or family being proposed.]

### Rigor Label
[proven / established_result / heuristic_analogy / empirically_motivated / unverified_conjecture]

### Source or Derivation
[Citation, or the full derivation if `unverified_conjecture`.]

### What This Framing Changes
[What experiment, loss, metric, or design decision this framing actually affects. If nothing, say so and recommend dropping the framing.]

### What Would Falsify or Weaken It
[Concrete evidence that would undercut the framing.]

### Decision
[adopt_as_contribution_framing / use_as_supporting_explanation_only / drop]
```

## Important Rules

- Do not force a mathematical framing onto every idea; most good engineering contributions do not need one.
- Do not present an analogy as a guarantee.
- Do not invent citations to support a mathematical claim; if no real source is found, label it `unverified_conjecture` or `heuristic_analogy` and say so.
- Do not let this skill replace `scientific-critical-thinking`'s decision-recommendation discipline — a theoretical lens note still needs a decision, not just an interesting observation.
- Do not use this skill to make a paper sound more rigorous than the evidence supports; that is exactly the failure mode it exists to prevent.

## Final Checklist

Before finishing a theoretical-lens task:

1. [ ] The failure mode or phenomenon being explained is stated concretely.
2. [ ] A specific mathematical structure is named, not a vague appeal to "theory."
3. [ ] A rigor label is attached from the canonical vocabulary.
4. [ ] A real citation is attached, or the derivation is shown in full, or the claim is explicitly marked unverified.
5. [ ] What the framing changes about the design or experiment is stated; if nothing, the framing is dropped.
6. [ ] A decision is given: adopt, use as supporting explanation only, or drop.

## Final Reminder

A mathematician's taste includes restraint. The goal is not to make the work sound more theoretical — it is to find the cases where a principled framing genuinely changes what you would do next, and to say plainly when it doesn't.
