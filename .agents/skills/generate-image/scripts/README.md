# Generate Image Scripts

This folder supports the `generate-image` skill.

## Purpose

Use `generate_image.py` for general-purpose non-technical image generation and image editing.

Use `scientific-schematics` instead for:

- technical diagrams;
- architecture figures;
- method pipelines;
- workflows;
- scientific schematics;
- circuits;
- pathways;
- evidence-sensitive figures.

## Basic usage

```bash
python scripts/generate_image.py "abstract blue presentation background, no text" -o assets/background.png
```

Fast direct Gemini smoke test:

```bash
python scripts/generate_image.py "simple blue gradient background, no text" --provider google -m google-gemini-fast --timeout 600 -o assets/google_test.png
```

Edit an image:

```bash
python scripts/generate_image.py "make the sky warmer" --input photo.jpg -o edited_photo.png
```

## API key

The script supports three providers:

- `openrouter` (default): uses `OPENROUTER_API_KEY`
- `google`: uses `GEMINI_API_KEY`
- `openai`: uses `OPENAI_API_KEY`

Linux/macOS:

```bash
export OPENROUTER_API_KEY="your_key_here"
export GEMINI_API_KEY="your_key_here"
export OPENAI_API_KEY="your_key_here"
```

Windows CMD:

```bat
set OPENROUTER_API_KEY=your_key_here
```

Windows PowerShell:

```powershell
$env:OPENROUTER_API_KEY = "your_key_here"
```

You can also place the key in a local `.env` file:

```text
OPENROUTER_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
```

Do not commit API keys.

## Safety

Generated images are visual assets, not scientific evidence.

Do not use this script to fabricate:

- experimental results;
- model outputs;
- datasets;
- technical diagrams;
- scientific mechanisms;
- evidence-sensitive manuscript figures.

Use `claim-auditor` for figure/caption claims and `venue-templates` for final submission formatting.
