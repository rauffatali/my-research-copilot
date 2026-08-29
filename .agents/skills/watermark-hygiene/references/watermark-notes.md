# Text watermark notes

## Deterministic marks

Invisible Unicode, bidirectional controls, tag characters, exotic spaces, and selected confusables can carry machine-readable signals or cause broken copy, search, and diffs.

`clean_text.py` removes or normalizes known carriers and reports exact counts. By default it preserves contextual characters used by emoji, joining scripts, Mongolian selectors, Khmer inherent vowels, Hangul fillers, and Arabic/Syriac orthography. The lightweight workflow also disables space normalization by default so multilingual typography remains intact. Aggressive flags can damage intentional text and should remain opt-in.

## Out of scope

Token-sampling or statistical watermarks live in word choice and token sequences
rather than deterministic Unicode artifacts. This skill neither detects nor
rewrites them. It also does not score detectors, optimize against detector
outputs, simulate authorship, or remove general provenance.

Never describe a Unicode cleanup as certified, undetectable, or proof of human
authorship. Detector behavior and provenance decisions remain outside this
skill's evidence boundary.
