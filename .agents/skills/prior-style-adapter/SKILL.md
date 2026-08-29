---
name: prior-style-adapter
description: Adapt manuscript prose to the project's prior-paper writing style using paper/style/prior_paper_style.md. If that file is missing, derive it from one or more PDFs in paper/style/ before adapting prose. Use when revising paper/ text for tone, phrasing, paragraph flow, sentence rhythm, and stylistic expression of evidence-calibrated hedging already authorized by the scientific brief, without copying prior wording, importing claims, inventing evidence, or changing technical meaning. Use claim-auditor after adaptation when claims are changed or clarified.
---

# Prior Style Adapter

## Overview

Prior Style Adapter revises manuscript prose so it aligns with the project's established academic writing style.

This skill supports two modes:

1. `style-bootstrap`
2. `style-adaptation`

Use this skill when the user wants text in `paper/` to sound more like the author's prior papers or established project style.

This skill adapts style, not scientific content.

It should preserve technical meaning, evidence strength, citation intent, LaTeX structure, and claim scope.

For manuscript work, follow `.agents/guidance/manuscript-writing.md` for writing-slice staging, transformation checks, and integration boundaries. This skill is a style adapter, not a scientific or integration authority.

When the active role is `independent_reviewer`, its strict read-only boundary overrides style-bootstrap or adaptation writes. Return observations or suggested wording in the response and do not write style guides, drafts, review artifacts, or any other repository file.

---

## Style Source

Use the following file as the primary style reference when it exists:

```text
paper/style/prior_paper_style.md
```

If `paper/style/prior_paper_style.md` does not exist, check `paper/style/` for one or more prior-paper PDFs:

```text
paper/style/*.pdf
```

If suitable PDFs exist, enter `style-bootstrap` mode:

- extract reusable style traits from the PDFs;
- write or refresh `paper/style/prior_paper_style.md`;
- then continue in `style-adaptation` mode.

If needed for local context, also read:

```text
paper/AGENTS.md
paper/
```

and the specific manuscript file or section being revised.

Do not infer author style from memory. Use the provided style file or project artifact.

If neither `paper/style/prior_paper_style.md` nor suitable prior-paper PDFs exist, say so and perform only a conservative academic revision without claiming prior-style alignment.

Template or placeholder PDFs in `paper/style/` are not suitable style sources by themselves. Treat them only as file-format examples unless they actually contain recoverable prior-paper prose that you want to bootstrap from.

---

## Modes

### 1. Style-Bootstrap Mode

Use this mode when:

- `paper/style/prior_paper_style.md` is missing; and
- one or more prior-paper PDFs exist in `paper/style/`.

Goal:

- derive a reusable style guide from prior papers;
- save it as `paper/style/prior_paper_style.md`;
- make later style adaptation repeatable across sessions.

In this mode:

1. read the available prior-paper PDFs;
2. extract only reusable style traits such as:
   - tone;
   - sentence rhythm;
   - paragraph flow;
   - transition habits;
   - how the author expresses cautious or qualified claims;
   - contribution phrasing;
   - results narration style;
   - limitation style;
   - technical density;
3. write or refresh `paper/style/prior_paper_style.md`;
4. do not copy text, citations, claims, or section structure from the prior papers;
5. continue with `style-adaptation` mode when prose revision is requested.

### 2. Style-Adaptation Mode

Use this mode when:

- `paper/style/prior_paper_style.md` exists.

Goal:

- revise manuscript prose so it matches the established prior-paper style while preserving meaning and evidence discipline.

---

## Core Responsibility

This skill answers:

```text
How can this manuscript text be revised to better match the author/project style while preserving meaning and evidence discipline?
```

It should adapt:

- tone;
- phrasing habits;
- sentence rhythm;
- paragraph flow;
- transition style;
- contribution phrasing;
- results narration style;
- limitation phrasing;
- stylistic expression of evidence-calibrated hedging already specified by the scientific brief;
- level of technical density;
- author-like academic voice.

It should not create new scientific content.

After a material style adaptation, preserve the pre-adaptation and post-adaptation text for differential comparison and route the result to `claim-auditor`. Citation or reference changes go to `citation-management` when relevant.

---

## Relationship to Other Skills

Use the smallest relevant skill combination.

| Need | Use |
|---|---|
| Draft or revise scientific content | `scientific-writing` |
| Adapt prose to established author/project style | `prior-style-adapter` |
| Check whether final claims are supported | `claim-auditor` |
| Verify references, citations, DOI/arXiv metadata, or BibTeX | `citation-management` |
| Use venue-specific wording, structure, or formatting | `venue-templates` |
| Critique scientific logic before rewriting | `scientific-critical-thinking` |
| Simulate reviewer-facing critique | `peer-review` |

Recommended workflow:

```text
scientific-writing
    -> prior-style-adapter
    -> claim-auditor
```

For pure style adaptation:

```text
prior-style-adapter
    -> claim-auditor if claims were changed, clarified, narrowed, or reorganized
```

Style adaptation must not hide unsupported claims.

---

## When to Use This Skill

Use this skill for:

- abstracts;
- introductions;
- related work transitions;
- contribution statements;
- method overview paragraphs;
- results discussion paragraphs;
- limitation sections;
- conclusions;
- reviewer-facing rewrites;
- rebuttal paragraphs;
- manuscript passages that sound generic or AI-like;
- text that needs to match the author's prior academic tone;
- bootstrapping `paper/style/prior_paper_style.md` from prior-paper PDFs when the style file is missing.

This skill is especially useful after `scientific-writing` produces a technically correct draft that still needs to sound like the author.

---

## Do Not Use This Skill For

Do not use this skill to:

- invent citations;
- invent results;
- invent baselines;
- invent novelty;
- rewrite the scientific argument without evidence;
- copy sentences from prior papers;
- import prior-paper technical claims;
- change method meaning;
- remove necessary caveats;
- strengthen claims beyond evidence;
- make unsupported claims sound more polished;
- alter LaTeX commands, labels, refs, or citation keys unless explicitly requested.

If content is scientifically weak, mark the issue instead of hiding it with style.

---

## What To Do

1. Check whether `paper/style/prior_paper_style.md` exists.
2. If it does not exist, check `paper/style/` for prior-paper PDFs.
3. If PDFs exist, generate `paper/style/prior_paper_style.md` in `style-bootstrap` mode before adapting prose.
4. If no style file and no suitable PDFs exist, report that prior-style alignment is unavailable and fall back to conservative academic revision only.
5. Read the target manuscript text.
6. Read `paper/style/prior_paper_style.md` when available.
7. Identify relevant style features:
   - tone;
   - sentence rhythm;
   - paragraph flow;
   - transition habits;
   - contribution phrasing;
   - results narration style;
   - limitation style;
   - how cautious or qualified claims are expressed;
   - technical density.
8. Identify claims that must not be strengthened.
9. Revise the text to better match the style.
10. Preserve technical meaning and evidence strength.
11. Preserve LaTeX commands, citation keys, labels, and references.
12. Report any places where style adaptation could not be done safely.
13. Recommend `claim-auditor` if claims were changed or if support is uncertain.

---

## Anti-Copying Boundary

Style adaptation is not imitation by copying.

Allowed:

- matching level of formality;
- matching conservative tone;
- matching paragraph pacing;
- matching transition style;
- matching concise contribution phrasing;
- matching how limitations are framed.

Not allowed:

- copying sentences;
- copying distinctive phrases;
- copying examples;
- copying claims;
- copying citation patterns;
- importing structure that changes meaning;
- reusing prior-paper wording with minor edits.

If a prior style has a distinctive phrase, capture the function of that phrase, not the words.

Example:

Prior style function:

```text
The author tends to state the limitation directly and then narrow the claim.
```

Safe adaptation:

```text
The current evaluation is limited to the available test split, so the results should be interpreted as evidence for this setting rather than broader deployment conditions.
```

Unsafe adaptation:

```text
Copying the same limitation sentence from a prior paper.
```

---

## Avoid AI-Like Over-Smoothing

Do not make the prose sound like generic AI-generated academic text.

Avoid:

- overly perfect symmetry;
- repetitive sentence rhythm;
- generic transitions;
- inflated importance;
- vague confidence;
- excessive polish;
- broad filler phrases.

Avoid phrases like:

- "plays a crucial role";
- "significant advancements";
- "comprehensive framework";
- "robust solution";
- "seamlessly integrates";
- "unprecedented opportunities";
- "state-of-the-art performance" unless verified.

Prefer:

- concrete nouns;
- specific verbs;
- natural sentence variation;
- direct limitation statements;
- claim scope tied to evidence;
- author-like pacing.

The text should sound human, careful, and technically grounded.

---

## Claim-Strength Boundary

Preserve or improve claim discipline.

Do not change:

```text
suggests
```

to:

```text
demonstrates
```

unless evidence supports the stronger word.

Prefer safer wording when evidence is limited:

| Risky wording | Safer wording |
|---|---|
| proves | provides evidence that |
| solves | addresses |
| demonstrates | suggests / indicates, if evidence is limited |
| robust | robust under the evaluated conditions |
| generalizes | was evaluated on / showed performance on |
| significantly improves | improves, unless significance was tested |
| outperforms all baselines | outperforms the evaluated baselines |
| state-of-the-art | competitive / strong / improved over evaluated baselines |
| first | avoid unless literature evidence is strong |

If the original text appears to overclaim or requires a change in scientific strength, flag it to `research_lead` and `claim-auditor`. Do not independently choose stronger, weaker, broader, or narrower scientific wording.

If the original text is under-specific, style adaptation may clarify it without strengthening the claim.

---

## LaTeX Preservation Rules

Preserve:

- citation commands;
- citation keys;
- labels;
- refs;
- equations;
- figure/table references;
- section commands;
- comments that mark TODOs;
- macros;
- glossary/acronym commands.

Examples of things to preserve:

```latex
\cite{...}
\ref{...}
\label{...}
\todo{...}
\acrshort{...}
```

Do not rename citation keys or labels.

If a citation appears suspicious, recommend `citation-management`.

If a cited sentence may not be supported, recommend `claim-auditor`.

---

## Section-Specific Style Guidance

### Abstract

Adapt for:

- concise problem framing;
- careful contribution statement;
- no unsupported novelty;
- no invented final results;
- conservative conclusion.

### Introduction

Adapt for:

- natural motivation flow;
- citation-aware background;
- clear gap statement;
- restrained contribution phrasing.

Do not create new gap claims.

### Related Work

Adapt for:

- synthesis rather than listing;
- smooth transitions between method families;
- conservative positioning.

Do not invent citations or prior-work claims.

### Method

Adapt for:

- precise technical description;
- clear sequence;
- reproducibility-oriented wording.

Do not add performance claims.

### Results / Discussion

Adapt for:

- careful comparison language;
- evidence-bound interpretation;
- explicit evaluated setting;
- limitation-aware wording.

Do not add improvements, rankings, or significance.

### Conclusion

Adapt for:

- concise supported summary;
- no new claims;
- careful future-work framing.

---

## Output Style

When rewriting, prefer:

- formal and precise academic tone;
- moderate sentence length;
- natural variation in rhythm;
- application-motivated framing where relevant;
- explicit but conservative wording;
- coherent paragraph progression;
- restrained conclusions tied to evidence;
- author-like style without copying.

---

## Output Formats

Choose the smallest useful output.

---

### Style Bootstrap Report

Use when generating or refreshing the style guide.

```md
## Style Bootstrap Report

### Source PDFs

- [pdf path]

### Extracted Style Traits

- [trait]

### Output

- `paper/style/prior_paper_style.md`

### Notes

- [limitations or ambiguity]
```

---

### Direct Rewrite

Use when the user only needs the revised text.

```md
## Revised Text

[revised text]
```

---

### Rewrite With Notes

Use when style-sensitive changes or scientific caution matters.

```md
## Revised Text

[revised text]

## Style Adaptation Notes

- [tone/rhythm/flow adjustment]
- [stylistic expression of evidence-calibrated hedging]

## Preserved Elements

- citations preserved
- labels/refs preserved
- technical meaning preserved

## Remaining Risks

- [needs claim-auditor / citation-management / evidence check]
```

---

### Before/After Table

Use when the user wants traceability.

```md
| Original | Revised | Reason |
|---|---|---|
| [text] | [revision] | [style/evidence reason] |
```

---

## Important Rules

- Do not copy prior-paper sentences.
- Do not claim prior-style alignment if no style file or suitable prior-paper PDFs exist.
- Do not import citations, claims, results, or structure from prior work.
- Do not turn motivations or hypotheses into results.
- Do not strengthen claims beyond the available evidence.
- Do not remove caveats that are scientifically necessary.
- Do not hide unsupported claims with polished prose.
- Preserve LaTeX commands, citation keys, labels, and references unless explicitly asked.
- Use `claim-auditor` when claim support may have changed.
- Use `citation-management` when citation integrity is uncertain.

---

## Good Outputs

Good outputs:

- preserve meaning;
- sound closer to the author's prior style;
- reduce generic AI-like prose;
- improve paragraph flow;
- keep claims conservative;
- preserve LaTeX structure;
- report any remaining evidence risks.

Bad outputs:

- copy previous-paper wording;
- make the prose sound generic and over-polished;
- add unsupported claims;
- remove limitations;
- strengthen results;
- invent citations;
- alter technical meaning;
- silently change citation keys or labels.

---

## Final Checklist

Before completing a style adaptation:

1. [ ] Target manuscript text was read.
2. [ ] `paper/style/prior_paper_style.md` was used if available.
3. [ ] If the style file was missing, prior-paper PDFs were checked.
4. [ ] If PDFs existed, the style file was generated or refreshed before adaptation.
5. [ ] Technical meaning is preserved.
6. [ ] Claims are not strengthened beyond evidence.
7. [ ] Necessary caveats remain.
8. [ ] Prior-paper wording was not copied.
9. [ ] No citations, results, baselines, or novelty claims were invented.
10. [ ] LaTeX commands, labels, refs, and citation keys are preserved.
11. [ ] The prose sounds human and author-like, not generic AI.
12. [ ] Any uncertain claim support is routed to `claim-auditor`.
13. [ ] Any citation/reference issue is routed to `citation-management`.

---

## Final Reminder

Prior style adaptation should make the manuscript sound more like the author, not more like a polished generic AI system.

The best style adaptation preserves scientific meaning while making the prose feel natural, restrained, and consistent with the project's established voice.
