---
name: watermark-hygiene
description: Use for optional, read-only inspection of invisible Unicode and text-transfer artifacts in authorized manuscript or research text, with deterministic cleanup available only as an explicit separate-output proposal. Preserve protected spans and report exact locations and context; do not rewrite prose, strip provenance, optimize detectors, or infer AI authorship.
---

# Watermark Hygiene

## Research Copilot integration and precedence

This skill retains the compatible text-only Unicode hygiene core from the upstream
`clean-user-facing-text` skill. The repository contracts and the active role take precedence over any
default behavior described below:

- Inspect and report first. Cleanup is optional, explicit, and written to a separate candidate output by
  default; this skill never silently mutates a manuscript or protected main target.
- Process only text the user owns or is authorized to process. A finding is not proof of a watermark, AI
  authorship, policy violation, or provenance status.
- Preserve Markdown and HTML structure, fenced and inline code, commands, paths, URLs, identifiers,
  API names, formulas, citation commands and keys, references, labels, exact values, technical terms,
  multilingual orthography, and required disclosures. Escalate ambiguous semantic or provenance issues
  instead of guessing.
- `independent_reviewer` is strictly read-only. A writable `candidate_writer` may apply an explicitly
  accepted deterministic cleanup only under `paper/draft/`, preserving the original and producing a
  focused diff. `human_researcher` authorization and a separate `integration_agent` invocation are
  required for any protected integration.
- This skill is outside the automatic prose-refinement chain. Academic naturalness, voice, claim scope,
  and scientific meaning belong to `academic-humanizer`, `prior-style-adapter`, `scientific-writing`,
  and `claim-auditor` as applicable.
- Statistical or token-sampling watermark rewriting, detector scoring or optimization, authorship
  simulation, provenance stripping, media processing, remote services, and automatic hooks are outside
  this skill and must not be invoked through it.

Apply a deterministic text-hygiene pass only to prose the user owns or is authorized to process. Never
claim that a cleanup proves human authorship, removes all provenance, or changes the result of an
external detector. Preserve required academic, legal, platform, and regulatory disclosures.

## Workflow

1. Identify the text that readers will see and confirm that the user owns it or is
   authorized to process it.
2. Protect non-prose spans before any proposed cleanup:
   - fenced and inline code, commands, paths, URLs, identifiers, and API names
   - formulas, citations, labels, cross-references, exact values, and verbatim text
   - HTML attributes, structured data, and required academic, legal, platform, or
     regulatory disclosures
3. Preserve every claim, fact, number, name, citation, and requirement. A Unicode
   finding is not evidence that prose is machine-generated, altered by a particular
   vendor, or safe to rewrite.
4. **Inspect before proposing cleanup.** Run the self-contained Unicode inspection
   script and record exact findings, code points, offsets, categories, and context.
   For a report-only audit that never writes output, use `--audit`:

   ```bash
   PYTHON "$SCRIPTS/inspect_text.py" --json INPUT
   PYTHON "$SCRIPTS/inspect_text.py" --audit INPUT  # detect-only Unicode report
   ```

5. Review every finding against the protected-span map. If a finding is ambiguous,
   load-bearing, or inside protected content, stop and leave it unchanged unless the
   user supplies a focused decision.
6. **Cleanup only after explicit approval.** Write a separate candidate output with
   the deterministic Unicode script; never silently mutate the source or a protected
   main target:

   ```bash
   PYTHON "$SCRIPTS/clean_text.py" INPUT -o OUTPUT --stats --no-normalize-spaces
   ```

   Use `--no-normalize-spaces` by default so NBSP, narrow no-break spaces, figure
   spaces, and CJK ideographic spaces retain their layout semantics. Normalize spaces
   only when the user requests it.
7. For Markdown or HTML, inspect hit positions first. If a hit falls inside code,
   attributes, or another non-prose span, do not run whole-file cleanup; clean only
   the explicitly authorized prose segment or leave that hit unchanged. These scripts
   are text-level tools, not Markdown or HTML parsers.
8. Compare the candidate with the original, preserve the original, and report the
   exact deterministic changes. A candidate cleanup is not an integration decision.
9. Return the audit or candidate proposal with unresolved findings clearly marked;
   do not silently return a rewritten manuscript.

## Deterministic Unicode pass

Resolve `SCRIPTS` to this skill's `scripts/` directory.
Use the available Python 3 launcher for the platform. Replace `PYTHON` below
with `python3` on most macOS/Linux systems, `py` on Windows, or another verified
Python 3 command.

This skill is self-contained and runs its vendored text scripts directly; it has no
service or network dependency. The deterministic pass handles transfer artifacts
such as zero-width and other invisible format characters, selected bidi controls,
noncharacters, and space homoglyphs. Inspection reports the character, Unicode
category/name, offset, and bounded context so a human can decide whether it is safe
to remove.

Inspect first when editing an existing file:

```bash
PYTHON "$SCRIPTS/inspect_text.py" --json INPUT
PYTHON "$SCRIPTS/clean_text.py" INPUT -o OUTPUT --stats --no-normalize-spaces
PYTHON "$SCRIPTS/inspect_text.py" --json OUTPUT
```

Use `-` for stdin. Prefer a new `*.cleaned.*` output. `--in-place` is available only
when the user explicitly requests source mutation; the script creates a `.bak`
backup, but a separate output remains the default for this skill.

Do not use `--aggressive-homoglyphs`, `--nfkc`, or `--strip-emoji-glue` unless the
user requests aggressive normalization and accepts possible changes to multilingual
text, emoji, directionality, or typography. Statistical or token-sampling watermarks
are not detected or rewritten by this skill.

The scripts support plain text, source text, Markdown, and HTML source as text. Do
not pass binary containers such as PDF, DOCX, images, or archives. The binary guard
refuses common container signatures rather than treating those files as text.

## Code and structure boundary

This skill does not rewrite prose, normalize general style, or alter technical
content. Never rename variables, alter string literals, reformat code, change
executable output, modify HTML attributes, or change citation/LaTeX syntax. Preserve
fenced and inline code byte-for-byte whenever practical. If a deterministic finding
is inside a protected span, report it and request a focused decision.

## Reporting

When the user asks for an audit, distinguish:

- **Verifiable:** Unicode characters found, removed, or replaced, with code points,
  locations, bounded context, and script counts; source and candidate paths/hashes
  when available.
- **Decision-dependent:** whether a finding is an accidental transfer artifact or
  intentional typography, and whether a proposed cleanup is acceptable.
- **Not established:** human authorship, AI authorship, official detector evasion,
  removal of a vendor's secret-key watermark, or removal of general provenance.

For technical background, read `references/watermark-notes.md`. For misuse or
disclosure questions, read `references/responsible-use.md`.

## Research Copilot handoff

The default flow is inspect -> exact report -> explicit decision -> preserve the
original -> focused candidate proposal -> claim/evidence validation. A candidate
writer may apply an accepted deterministic cleanup only to `paper/draft/`; it is not
scientific authority and must not silently change claims, evidence, citations,
technical meaning, or disclosures. `independent_reviewer` remains strictly
read-only. `research_lead` adjudicates ambiguous findings; `human_researcher`
authorizes protected integration; and a separate `integration_agent` performs that
integration when authorized. Use `claim-auditor` after any material transformation.

## Upstream provenance

Repository: https://github.com/guillaumemeyer/watermarks-remover
Source skill: `skills/clean-user-facing-text/`
Snapshot branch: `main`
Snapshot HEAD: `474be13921337e0ae6d7a8e6d161d03ad6e3f18a`
git describe --tags --always --dirty: `v0.6.0-15-g474be13`
Imported: 2026-08-29
License: MIT (see `LICENSE.upstream`)
