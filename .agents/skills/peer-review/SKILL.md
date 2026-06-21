---
name: peer-review
description: Use for reviewer-style critique of AI/ML/CV manuscripts, proposals, experiment packages, research narratives, and multi-disciplinary applied AI work. Supports single-reviewer critique and multi-reviewer panel review with AI/CV, domain, and hybrid reviewers. Best for assessing contribution clarity, novelty risk, methodological soundness, baseline fairness, evaluation adequacy, reproducibility, limitations, and likely reviewer objections. For internal methodology critique use scientific-critical-thinking. For evidence-to-claim auditing use claim-auditor.
---

# Peer Review

## Overview

Peer review is an external-facing evaluation of whether a research manuscript, proposal, experiment package, or research narrative is convincing to skeptical reviewers.

Use this skill to assess whether the work presents a clear contribution, uses fair baselines, reports adequate experiments, supports its claims, acknowledges limitations, and meets the expectations of the intended research audience.

This skill should simulate reviewer judgment, not merely provide editing suggestions.

For AI/ML/CV and applied AI work, peer review may be done in two ways:

1. **Single-reviewer mode** — one integrated reviewer-style critique.
2. **Multi-reviewer panel mode** — several reviewer personas with complementary expertise, followed by a meta-review.

Use multi-reviewer panel mode for substantial, interdisciplinary, domain-specific, or submission-sensitive work.

---

## Core Role

Peer review should answer:

```text
Would a skeptical reviewer find this work convincing?
What would they praise?
What would they criticize?
Which issues are fatal, major, or minor?
What evidence or revision would change the decision?
Is the likely recommendation accept, borderline, or reject?
```

This skill should evaluate the current artifact as reviewers would see it.

It should not silently fix the work. It should expose weaknesses clearly enough that the author or another skill can fix them.

---

## When to Use This Skill

Use this skill when:

- reviewing a manuscript draft;
- reviewing an abstract, introduction, method, experiment, result, discussion, or conclusion section;
- evaluating whether a research contribution is convincing;
- simulating likely reviewer objections;
- assessing whether experiments are sufficient for the claims;
- checking whether baselines and comparisons are fair;
- evaluating novelty framing and contribution positioning;
- reviewing a research proposal or planned paper structure;
- preparing for submission, rebuttal, or internal pre-review;
- deciding whether the current evidence package is strong enough for a paper claim;
- evaluating applied AI work that needs both technical and domain credibility;
- preparing an area-chair-style or meta-review summary.

Do not use this skill as the primary tool for:

- internal hypothesis or methodology critique; use `scientific-critical-thinking`;
- sentence-level claim support auditing; use `claim-auditor`;
- literature discovery; use `research-lookup`;
- literature synthesis; use `literature-review`;
- citation formatting, BibTeX hygiene, or hallucinated-reference cleanup; use `citation-management`;
- manuscript drafting or rewriting; use `scientific-writing`;
- visual artifact creation; use `scientific-schematics` or `generate-image`.

---

## Relationship to Other Skills

Use this skill after enough context exists for reviewer-style judgment.

Recommended workflow for a mature paper artifact:

```text
research-lookup
    → literature-review
    → citation-management
    → claim-auditor
    → scientific-critical-thinking
    → peer-review
```

Skill boundaries:

| Need | Use |
|---|---|
| Find closest prior work, baselines, datasets, benchmarks | `research-lookup` |
| Synthesize prior work and research gaps | `literature-review` |
| Verify references and BibTeX metadata | `citation-management` |
| Check sentence-level evidence support | `claim-auditor` |
| Pressure-test research decisions before they are locked | `scientific-critical-thinking` |
| Simulate external reviewer judgment | `peer-review` |
| Revise prose after review | `scientific-writing` |

This skill may recommend using other skills, but it should not pretend those checks have been completed unless evidence is available.

---

## Relationship to Research Gates

This skill is most relevant to the following gates in `docs/research_gates.md`:

- Research Direction Gate
- Experiment Decision Gate
- Evaluation and Result Interpretation Gate
- Claim Support Gate
- Red-Team Review Gate
- Paper Writing Gate
- Final Handoff Gate

Use this skill when a research artifact needs reviewer-style judgment after internal planning, validation, or claim auditing.

This skill should not replace gates. It should evaluate whether the artifact would survive skeptical external review.

---

## Tool Workflow Policy

Follow `docs/tool_workflow_policy.md`.

This skill's useful output must be written to the appropriate durable repository artifact rather than left only in chat.

When this skill changes workflow state, active artifacts, blockers, claim status, experiment status, manuscript state, or next step, update `docs/current_status.md`.

---

## Review Modes

Choose the smallest review mode that fits the task.

---

### 1. Single-Reviewer Review

Use for:

- small section reviews;
- early paper drafts;
- quick reviewer-style critique;
- local revisions;
- focused evaluation of one artifact.

Output:

- neutral summary;
- strengths;
- weaknesses;
- major comments;
- minor comments;
- questions for authors;
- recommendation if requested.

---

### 2. Multi-Reviewer Panel Review

Use for substantial manuscripts, applied AI papers, interdisciplinary work, or submission-readiness checks.

This mode simulates a review panel with complementary reviewer expertise.

Default panel:

1. **Method Reviewer**
   - AI/ML/CV technical expert.

2. **Domain Reviewer**
   - application-domain expert.

3. **Hybrid Reviewer**
   - expert who understands both the AI method and the application domain.

4. **Meta-Reviewer / Area Chair**
   - synthesizes reviewer disagreement, consensus, must-fix issues, and likely decision.

For example, for:

```text
Road damage detection using AI
```

use:

```text
Reviewer A — AI/CV Method Reviewer
Reviewer B — Road Damage / Infrastructure Domain Reviewer
Reviewer C — Hybrid Applied AI + Road Damage Reviewer
Meta-Reviewer — Area Chair synthesis
```

The panel should not produce three isolated reviews only. It must end with a meta-review.

Use `references/multi_reviewer_panel.md` for detailed reviewer-role definitions, disagreement handling, and domain-specific panel adaptation.

---

### 3. Rebuttal-Preparation Review

Use when preparing a response to reviewers.

Output:

- likely reviewer concerns;
- which concerns are valid;
- evidence needed for rebuttal;
- claims that should be weakened;
- experiments or analyses that can be added;
- response strategy.

---

### 4. Presentation or Slide Review

Use only when explicitly reviewing slides or a presentation.

Output:

- content and scientific clarity;
- visual/layout issues by slide;
- missing evidence or citations;
- timing and audience fit;
- recommended fixes.

---

## Multi-Reviewer Panel Design

When using multi-reviewer panel mode, define reviewers based on the work.

For most applied AI/CV papers, use the default three-reviewer panel.

### Reviewer A — Method Reviewer

Expertise:

```text
AI, ML, computer vision, model design, training, metrics, baselines, evaluation, reproducibility
```

Primary questions:

- Is the technical contribution clear?
- Is the method justified?
- Are baselines fair and strong enough?
- Are metrics appropriate?
- Are ablations sufficient?
- Are training and evaluation protocols reproducible?
- Are leakage risks considered?
- Are results interpreted correctly?
- Are claims proportional to evidence?

Typical concerns:

- weak baseline;
- missing ablation;
- unclear split;
- incompatible comparison;
- single-run result;
- metric mismatch;
- unreported implementation details;
- inflated novelty or SOTA claim.

---

### Reviewer B — Domain Reviewer

Expertise:

```text
application domain, task realism, data meaning, annotation validity, deployment context, domain-specific failure modes
```

For road damage detection, this reviewer checks:

- damage taxonomy;
- severity relevance;
- road-surface conditions;
- camera and acquisition realism;
- annotation consistency;
- deployment constraints;
- maintenance decision usefulness;
- weather, lighting, occlusion, and road-type variation;
- whether metrics reflect practical road-inspection value.

For other domains, adapt the reviewer to the application area.

Primary questions:

- Is the problem framed correctly for the domain?
- Are labels and task definitions meaningful?
- Is the dataset representative?
- Are domain-specific limitations acknowledged?
- Are failure modes practically important?
- Does the paper solve a domain-relevant problem or only optimize a generic metric?

Typical concerns:

- unrealistic dataset;
- incomplete label schema;
- missing severity or practical impact;
- poor deployment realism;
- annotation ambiguity;
- domain-specific failure modes ignored.

---

### Reviewer C — Hybrid Reviewer

Expertise:

```text
both AI/CV methodology and the application domain
```

Primary questions:

- Does the AI method actually solve the domain problem?
- Are technical metrics connected to domain needs?
- Is the contribution meaningful to both technical and domain audiences?
- Are experiments aligned with practical failure modes?
- Does the paper bridge the two fields or merely apply a model to a dataset?
- Is novelty technical, domain-specific, evaluation-specific, or application-specific?
- Are claims understandable and credible to interdisciplinary reviewers?

Typical concerns:

- technically valid but domain-irrelevant evaluation;
- domain motivation strong but AI contribution weak;
- method improvement not tied to practical impact;
- literature framing misses either AI or domain prior work;
- contribution falls between communities.

---

### Meta-Reviewer / Area Chair

The meta-reviewer synthesizes all reviewer perspectives.

Must include:

- consensus strengths;
- consensus weaknesses;
- reviewer disagreements;
- must-fix issues;
- optional improvements;
- likely decision;
- evidence that would change the decision;
- readiness status.

Readiness status:

- `ready for submission`;
- `minor revision needed`;
- `needs stronger evidence`;
- `needs experiment redesign`;
- `needs literature/context work`;
- `not ready`.

---

## Context-Aware Review Mode

For substantial AI/ML/CV manuscript or proposal reviews, do not review the artifact in isolation.

Before generating the final review, build a minimal review context:

1. **Internal compression**
   - Identify the paper’s core claims, method, evidence, datasets, metrics, and contribution.

2. **External context**
   - Use `research-lookup` when closest prior work, recent related work, relevant datasets, or standard baselines are missing.

3. **Domain narrative**
   - Use `literature-review` when a broader synthesis is needed to understand how the proposed work fits into the field.

4. **Baseline scouting**
   - Identify missing baselines, missing datasets, missing benchmarks, or unfair comparisons.

5. **Active verification**
   - Use `scientific-critical-thinking` to generate skeptical questions about novelty, technical soundness, evaluation validity, leakage risk, and claim strength.

6. **Claim support check**
   - Use `claim-auditor` when manuscript claims need to be checked against repository artifacts or verified citations.

7. **Reference integrity**
   - Use `citation-management` when references appear fake, mismatched, unverified, or suspicious.

8. **Reviewer synthesis**
   - Produce the final peer-review report only after the strongest available context has been compressed into actionable concerns.

Use the smallest necessary version of this process. Do not perform broad literature search for small local edits.

---

## Peer Review Workflow

Conduct review in six stages.

### Stage 1: Identify the Review Target

Identify what is being reviewed:

- full manuscript;
- abstract;
- introduction;
- related work;
- method section;
- experiment section;
- results section;
- discussion/conclusion;
- research proposal;
- experiment package;
- rebuttal draft;
- slide or presentation draft.

Also identify the intended venue or audience if known.

If venue is unknown, review against general AI/ML/CV research expectations.

For domain-specific applied AI work, identify the domain and whether multi-reviewer panel mode is needed.

---

### Stage 2: Summarize the Work

Provide a short neutral summary:

1. What problem is being addressed?
2. What is the claimed contribution?
3. What method, experiment, dataset, or analysis is used?
4. What evidence is presented?
5. What conclusion is the author asking the reader to accept?

The summary should be descriptive, not promotional.

---

### Stage 3: Evaluate Contribution and Novelty

Assess whether the contribution is clear, meaningful, and properly framed.

Check:

1. Is the research question clear?
2. Is the contribution stated precisely?
3. Is the work positioned against relevant prior work?
4. Is novelty technical, empirical, dataset-related, evaluation-related, or application-specific?
5. Is the claimed novelty stronger than the evidence supports?
6. Is the contribution meaningful beyond implementation?
7. Would a reviewer understand why this work matters?

Red flags:

- contribution is mostly “we tried model X”;
- novelty claim lacks closest-prior-work comparison;
- method is new to the project but not new to the field;
- contribution depends on weak baseline;
- paper overstates generality or impact;
- application value is clear but research contribution is unclear.

---

### Stage 4: Evaluate Methodology

Assess whether the method or study design supports the research question.

For AI/ML/CV work, check:

1. Are inputs, outputs, task definition, and assumptions clear?
2. Is the method motivated by a concrete limitation or failure mode?
3. Is the architecture, loss, augmentation, training, or evaluation change justified?
4. Are data and label contracts clear?
5. Are preprocessing and postprocessing described?
6. Are implementation details sufficient for reproduction?
7. Are there unnecessary or unexplained complexities?
8. Are likely confounders or leakage risks addressed?

Red flags:

- method complexity without mechanism;
- missing data split details;
- unclear label schema;
- unclear preprocessing or postprocessing;
- train/eval/inference mismatch;
- dataset leakage not considered;
- insufficient implementation detail for reproduction.

---

### Stage 5: Evaluate Experiments and Evidence

Assess whether the experiments are sufficient and fair.

Check:

1. Is there a meaningful baseline?
2. Is the baseline fairly implemented and tuned?
3. Are comparisons under the same evaluation protocol?
4. Are metrics aligned with the claims?
5. Are ablations sufficient to isolate the claimed mechanism?
6. Are failure cases or qualitative examples analyzed?
7. Are relevant slices reported when needed?
8. Are results single-run or multi-seed?
9. Are negative or mixed results acknowledged?
10. Are compute and dataset constraints transparent?

For CV tasks, consider:

- detection metrics such as mAP, AP50/AP75, recall, small-object metrics;
- segmentation metrics such as mIoU, Dice/F1, boundary quality;
- classification metrics such as accuracy, F1, confusion matrix, per-class precision/recall;
- domain-shift or robustness slices when claims require them;
- visual overlays, false positives, false negatives, and worst-case examples.

Red flags:

- headline metric only;
- no ablation for main method component;
- unfair or weak baseline;
- qualitative cherry-picking;
- no validation of target failure mode;
- test-set tuning risk;
- strong conclusion from one run;
- missing error bars or variance where variance matters.

---

### Stage 6: Evaluate Writing, Framing, and Limitations

Assess whether the paper communicates honestly and convincingly.

Check:

1. Is the abstract faithful to the evidence?
2. Does the introduction motivate the problem without exaggeration?
3. Are claims proportional to the results?
4. Are limitations visible and specific?
5. Are figures and tables understandable?
6. Are conclusions supported by evidence?
7. Are future-work claims separated from demonstrated findings?
8. Is the writing clear enough for the target audience?

Red flags:

- abstract overclaims;
- limitations are generic or hidden;
- conclusion introduces unsupported claims;
- important negative results are omitted;
- terminology is inflated;
- paper sounds polished but evidence is thin.

---

## Review Dimensions

Use the dimensions below when assigning review severity.

### 1. Significance

Ask:

- Is the problem important?
- Is the work useful to the target research community?
- Does it address a real gap, limitation, or failure mode?
- Is the contribution large enough for the intended venue?

### 2. Originality

Ask:

- What is new?
- Is the novelty clearly distinguished from prior work?
- Is the work more than an engineering combination?
- Is the novelty claim appropriately cautious?

### 3. Soundness

Ask:

- Are methods appropriate?
- Are experiments controlled?
- Are conclusions supported?
- Are confounders, leakage risks, and limitations addressed?

### 4. Evaluation Quality

Ask:

- Are metrics appropriate?
- Are baselines fair?
- Are ablations meaningful?
- Are failure modes analyzed?
- Is the evaluation protocol reproducible?

### 5. Reproducibility

Ask:

- Are data, code, configs, hyperparameters, seeds, and evaluation details sufficiently described?
- Are preprocessing and postprocessing clear?
- Are run artifacts or result sources traceable?

### 6. Clarity

Ask:

- Is the paper easy to follow?
- Are the research question, method, results, and conclusion clearly connected?
- Are figures and tables readable?
- Is the writing precise and proportional?

### 7. Limitations and Ethics

Ask:

- Are limitations specific and honest?
- Are dataset, bias, privacy, deployment, or misuse risks relevant?
- Does the paper avoid overstating real-world readiness?

### 8. Domain Validity

For applied AI/CV work, ask:

- Is the task definition domain-credible?
- Are labels meaningful to domain users?
- Is the dataset representative of the real problem?
- Are domain-specific failure modes considered?
- Do metrics reflect useful domain outcomes?
- Does the paper avoid claiming domain impact from technical metrics alone?

---

## Recommendation Levels

Use one of these recommendation levels when requested.

### Strong Accept

The work is significant, original, technically sound, well-evaluated, clearly written, and has only minor issues.

Use rarely.

### Accept

The work is solid and useful, with manageable weaknesses that do not undermine the main contribution.

### Weak Accept

The work has value but also notable limitations. The main claims are mostly supported, but improvements are needed.

### Borderline

The work has some strengths, but the contribution, evidence, or clarity may be insufficient for the venue.

### Weak Reject

The work has potential but has important weaknesses in novelty, methodology, evaluation, framing, or evidence.

### Reject

The work has major flaws that undermine the contribution or conclusions, such as unsupported claims, weak baselines, invalid evaluation, leakage risk, or unclear contribution.

### Strong Reject

The work has fundamental flaws or lacks a viable research contribution for the intended venue.

Use sparingly and justify clearly.

---

## Comment Severity

Use severity labels when useful.

### Critical

Issues that could invalidate the work or require major redesign.

Examples:

- invalid evaluation protocol;
- dataset leakage risk;
- unsupported main claim;
- missing essential baseline;
- contribution not identifiable;
- domain framing is invalid for the application.

### Major

Issues that substantially weaken the work but may be fixable.

Examples:

- incomplete ablation;
- weak novelty framing;
- unclear data split;
- missing failure analysis;
- overclaiming in abstract or conclusion;
- weak domain validity.

### Minor

Issues that improve clarity, presentation, or completeness.

Examples:

- unclear figure labels;
- missing implementation detail;
- wording too strong in one sentence;
- citation needed for a background statement.

---

## Structuring Single-Reviewer Reports

Use this structure for a full single-reviewer report.

### 1. Summary

Briefly summarize the paper or artifact in neutral language.

Include:

- problem;
- proposed approach;
- main evidence;
- claimed contribution.

### 2. Strengths

List the strongest aspects of the work.

### 3. Weaknesses

List the main weaknesses.

Distinguish between critical, major, and minor weaknesses.

### 4. Major Comments

For each major issue:

1. State the issue.
2. Explain why it matters.
3. Identify what evidence or revision is needed.
4. Say whether it affects the main claim.

### 5. Minor Comments

For each minor issue:

1. Identify the section, figure, table, or claim if possible.
2. State the issue.
3. Suggest a concise fix.

### 6. Questions for Authors

Ask specific questions that would help evaluate the work.

### 7. Recommendation

Provide a recommendation if requested.

Explain the recommendation in one short paragraph.

---

## Structuring Multi-Reviewer Panel Reports

Use this structure when multi-reviewer panel mode is requested or appropriate.

```md
# Multi-Reviewer Panel Review

## Review Target

- Artifact:
- Topic:
- Intended venue/audience:
- Review mode:
- Domain:

## Neutral Paper Summary

[Short summary of problem, method, evidence, and contribution.]

---

## Reviewer A: AI/CV Method Reviewer

### Summary

### Strengths

### Major Concerns

### Minor Concerns

### Required Fixes

### Questions for Authors

### Recommendation

[Strong Accept / Accept / Weak Accept / Borderline / Weak Reject / Reject / Strong Reject]

---

## Reviewer B: Domain Reviewer

### Summary

### Strengths

### Major Concerns

### Minor Concerns

### Required Fixes

### Questions for Authors

### Recommendation

[Strong Accept / Accept / Weak Accept / Borderline / Weak Reject / Reject / Strong Reject]

---

## Reviewer C: Hybrid Reviewer

### Summary

### Strengths

### Major Concerns

### Minor Concerns

### Required Fixes

### Questions for Authors

### Recommendation

[Strong Accept / Accept / Weak Accept / Borderline / Weak Reject / Reject / Strong Reject]

---

## Meta-Reviewer / Area Chair Summary

### Consensus Strengths

### Consensus Weaknesses

### Reviewer Disagreements

### Must-Fix Issues

### Optional Improvements

### Evidence That Would Change the Decision

### Likely Decision

[Decision]

### Research Readiness

[ready for submission / minor revision needed / needs stronger evidence / needs experiment redesign / needs literature-context work / not ready]

### Final Recommendation

[Concrete next action.]
```

The meta-review should be more than a summary. It should decide what matters most.

---

## Road Damage Detection Example Panel

When reviewing road damage detection using AI, use this reviewer panel unless a different panel is requested.

### Reviewer A — AI/CV Method Reviewer

Focus:

- detector/segmenter choice;
- baselines;
- mAP, AP50/AP75, recall, per-class metrics;
- small-object performance;
- train/validation/test protocol;
- augmentation;
- ablations;
- leakage;
- reproducibility;
- comparison fairness.

### Reviewer B — Road Damage / Infrastructure Reviewer

Focus:

- damage taxonomy;
- road-surface realism;
- severity labels;
- annotation reliability;
- acquisition conditions;
- maintenance relevance;
- practical false positives/false negatives;
- domain-specific failure modes;
- deployment constraints.

### Reviewer C — Hybrid Reviewer

Focus:

- whether the AI evaluation maps to road-inspection needs;
- whether the contribution is meaningful to both CV and infrastructure audiences;
- whether domain limitations weaken technical claims;
- whether better domain-aware metrics or slices are needed;
- whether the paper bridges technical and practical impact.

---

## Presentation and Slide Review

Use this section only when explicitly reviewing slides or a presentation.

Do not make presentation review the default peer-review mode.

When reviewing slides, inspect the visual artifact directly when possible.

Check:

- one main idea per slide;
- readable text;
- clear figures;
- no element overlap or truncation;
- consistent design;
- sufficient citations;
- clear research question;
- methods summarized at the right level;
- results visible and interpretable;
- conclusions supported by shown evidence;
- timing appropriate for the talk length.

Report slide issues by slide number when available.

Use this output structure:

1. Overall presentation assessment.
2. Content and scientific clarity.
3. Visual/layout issues by slide.
4. Missing evidence or citations.
5. Timing and audience fit.
6. Recommended fixes.

---

## Visual Artifacts

Do not generate schematics by default.

If the review identifies a need for a figure, architecture diagram, workflow schematic, taxonomy, domain workflow, or evaluation-protocol visual, recommend it as a revision.

Use `scientific-schematics` separately only when explicitly requested or clearly useful.

---

## Tone and Approach

Maintain a constructive, professional, and rigorous tone.

Do:

- be specific;
- be balanced;
- identify both strengths and weaknesses;
- explain why each issue matters;
- suggest actionable fixes;
- distinguish fatal flaws from fixable issues;
- avoid demanding unnecessary experiments outside the paper scope;
- separate AI/CV concerns from domain concerns when using panel mode;
- synthesize disagreements clearly in the meta-review.

Do not:

- attack the authors;
- use sarcasm or dismissive language;
- request experiments only because they would be interesting;
- impose personal preferences as requirements;
- invent missing citations, results, or claims;
- make unsupported accusations;
- overstate the certainty of the review;
- let the domain reviewer ignore technical validity;
- let the method reviewer ignore domain validity.

---

## Resources

This skill includes reference materials to support peer review:

- `references/multi_reviewer_panel.md` — reviewer-panel guidance for applied AI/ML/CV work. Defines the AI/CV method reviewer, domain reviewer, hybrid reviewer, meta-reviewer, disagreement handling, readiness labels, and domain-specific panel adaptation such as road damage detection.
- `references/ai_cv_review_criteria.md` — AI/ML/CV-specific peer-review criteria covering contribution clarity, novelty, task formulation, dataset and split validity, leakage risk, baseline fairness, method justification, ablation quality, evaluation protocol, failure analysis, reproducibility, claim-evidence alignment, limitations, and recommendation heuristics.
- `references/common_issues.md` — frequent methodological, statistical, reporting, reproducibility, and interpretation problems encountered during scientific peer review.
- `references/reporting_standards.md` — general reporting standards across disciplines. Use only when relevant to the manuscript type or venue.

For AI/ML/CV review, prioritize:

- contribution clarity;
- fair baselines;
- controlled ablations;
- leakage-safe data splits;
- reproducible training and evaluation;
- appropriate metrics;
- failure analysis;
- claim-evidence alignment.

For applied/domain-specific AI review, also prioritize:

- task validity;
- domain realism;
- label and annotation validity;
- dataset representativeness;
- practical failure modes;
- domain-relevant metrics;
- deployment or usage assumptions.

General biomedical reporting standards such as CONSORT, STROBE, and PRISMA should be used only when the manuscript type makes them relevant.

---

## Final Checklist

Before finalizing the review, verify:

1. [ ] The review target is clear.
2. [ ] The review mode is clear: single reviewer or multi-reviewer panel.
3. [ ] The work is summarized neutrally.
4. [ ] Strengths are identified.
5. [ ] Critical and major weaknesses are separated.
6. [ ] Contribution and novelty are evaluated.
7. [ ] Baselines and comparisons are evaluated.
8. [ ] Evaluation protocol and metrics are evaluated.
9. [ ] Reproducibility and artifact traceability are considered.
10. [ ] Claims are checked for proportionality.
11. [ ] Limitations are assessed.
12. [ ] Domain validity is assessed when applicable.
13. [ ] Multi-reviewer panel reports include method, domain, hybrid, and meta-review perspectives when requested.
14. [ ] Feedback is specific and actionable.
15. [ ] Recommendation, if given, is consistent with the stated issues.
16. [ ] The meta-review or final recommendation identifies the most important next action.

---

## Final Reminder

Peer review should simulate the pressure of external scrutiny.

For interdisciplinary AI work, the strongest review is not one generic critique. It is a structured panel that tests technical soundness, domain validity, and the bridge between them.
