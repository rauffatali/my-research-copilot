#!/usr/bin/env python3
"""Generate or edit general-purpose non-technical images.

This script supports the generate-image skill.

Use it for general images, illustrations, photos, artwork, backgrounds, and
non-technical visual assets.

Do not use it for technical diagrams, scientific schematics, method pipelines,
architecture diagrams, workflow diagrams, result figures, plots, or evidence-
sensitive scientific figures. Use scientific-schematics or results-scaffold
instead.

Examples:
    python scripts/generate_image.py "abstract blue presentation background, no text" -o assets/background.png

    python scripts/generate_image.py "make the sky warmer" --input photo.jpg -o edited_photo.png

    python scripts/generate_image.py "conceptual non-technical abstract texture illustration, no arrows, no labels" --mode general
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
from pathlib import Path
from typing import Any


DEFAULT_PROVIDER = "openrouter"
DEFAULT_MODEL = "google/gemini-3.1-flash-image-preview"

MODELS = {
    "gemini": "google/gemini-3.1-flash-image-preview",
    "flux-pro": "black-forest-labs/flux.2-pro",
    "flux-flex": "black-forest-labs/flux.2-flex",
    "google-gemini": "gemini-3.1-flash-image-preview",
    "google-gemini-fast": "gemini-2.5-flash-image",
    "openai-gpt-image": "gpt-image-1",
    "openai-gpt-image-2": "gpt-image-2",
}

PROVIDER_ENV_KEYS = {
    "openrouter": ("OPENROUTER_API_KEY",),
    "google": ("GEMINI_API_KEY",),
    "openai": ("OPENAI_API_KEY",),
}


TECHNICAL_WARNING_TERMS = [
    "flowchart",
    "pipeline",
    "architecture",
    "schematic",
    "diagram",
    "workflow",
    "circuit",
    "pathway",
    "protocol",
    "model blocks",
    "neural network",
    "evaluation metric",
    "result table",
    "graph",
    "plot",
]


def find_env_api_key(provider: str) -> str | None:
    """Find provider API key from environment or nearby .env files."""
    names = PROVIDER_ENV_KEYS[provider]
    for name in names:
        env_value = os.environ.get(name)
        if env_value:
            return env_value.strip()

    current = Path.cwd()
    for parent in [current] + list(current.parents):
        env_file = parent / ".env"
        if not env_file.exists():
            continue
        for line in env_file.read_text(encoding="utf-8", errors="replace").splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            for name in names:
                if stripped.startswith(f"{name}="):
                    value = stripped.split("=", 1)[1].strip().strip('"').strip("'")
                    if value:
                        return value
    return None


def warn_if_technical(prompt: str, force: bool = False) -> None:
    """Warn if prompt appears to request technical schematic content."""
    lower = prompt.lower()
    hits = [term for term in TECHNICAL_WARNING_TERMS if term in lower]
    if not hits:
        return

    warning = (
        "Warning: this prompt contains terms that may indicate a technical or evidence-sensitive figure: "
        + ", ".join(hits)
        + ".\nUse scientific-schematics for technical diagrams, workflows, model architectures, pathways, or evidence-sensitive figures."
    )
    print(warning, file=sys.stderr)

    if not force:
        print("Continue anyway with --force-general if this is truly a general/non-technical image.", file=sys.stderr)
        sys.exit(2)


def load_image_as_data_url(image_path: Path) -> str:
    """Load image as base64 data URL."""
    if not image_path.exists():
        raise FileNotFoundError(f"Input image not found: {image_path}")

    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    mime = mime_types.get(image_path.suffix.lower())
    if not mime:
        raise ValueError(f"Unsupported input image extension: {image_path.suffix}")

    data = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{data}"


def save_base64_image(base64_data: str, output_path: Path) -> None:
    """Save base64 image to output path."""
    if "," in base64_data:
        base64_data = base64_data.split(",", 1)[1]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(base64.b64decode(base64_data))


def output_mime_type(output_path: Path) -> str:
    """Return output MIME type from extension."""
    return {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(output_path.suffix.lower(), "image/png")


def extract_image_from_response(response_json: dict[str, Any]) -> str | None:
    """Extract base64 image from common OpenRouter response shapes."""
    choices = response_json.get("choices", [])
    if not choices:
        return None

    message = choices[0].get("message", {})
    images = message.get("images")
    if images:
        first = images[0]
        if isinstance(first, dict):
            image_url = first.get("image_url", {})
            if isinstance(image_url, dict):
                return image_url.get("url")
            return first.get("url")

    content = message.get("content")
    if isinstance(content, list):
        for item in content:
            if isinstance(item, dict) and item.get("type") in {"image_url", "output_image"}:
                image_url = item.get("image_url", {})
                if isinstance(image_url, dict) and image_url.get("url"):
                    return image_url["url"]
                if item.get("url"):
                    return item["url"]

    if isinstance(content, str) and content.startswith("data:image"):
        return content

    return None


def resolve_model(model: str) -> str:
    """Resolve model alias to model id."""
    return MODELS.get(model, model)


def provider_default_model(provider: str) -> str:
    """Return a reasonable default model for a provider."""
    if provider == "google":
        return "gemini-3.1-flash-image-preview"
    if provider == "openai":
        return "gpt-image-1"
    return DEFAULT_MODEL


def build_messages(prompt: str, input_image: Path | None) -> list[dict[str, Any]]:
    """Build OpenRouter chat messages."""
    if input_image:
        return [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": load_image_as_data_url(input_image)},
                    },
                ],
            }
        ]

    return [{"role": "user", "content": prompt}]


def generate_image(
    *,
    provider: str,
    prompt: str,
    output: Path,
    model: str,
    input_image: Path | None,
    api_key: str,
    timeout: int,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Generate or edit image through the selected provider."""
    if provider == "openrouter":
        return generate_image_openrouter(
            prompt=prompt,
            output=output,
            model=model,
            input_image=input_image,
            api_key=api_key,
            timeout=timeout,
            dry_run=dry_run,
        )
    if provider == "google":
        return generate_image_google(
            prompt=prompt,
            output=output,
            model=model,
            input_image=input_image,
            api_key=api_key,
            timeout=timeout,
            dry_run=dry_run,
        )
    if provider == "openai":
        return generate_image_openai(
            prompt=prompt,
            output=output,
            model=model,
            input_image=input_image,
            api_key=api_key,
            timeout=timeout,
            dry_run=dry_run,
        )
    raise ValueError(f"Unsupported provider: {provider}")


def generate_image_openrouter(
    *,
    prompt: str,
    output: Path,
    model: str,
    input_image: Path | None,
    api_key: str,
    timeout: int,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Generate or edit image through OpenRouter."""
    payload = {
        "model": resolve_model(model),
        "messages": build_messages(prompt, input_image),
        "modalities": ["image", "text"],
    }

    if dry_run:
        return {"dry_run": True, "payload_preview": {**payload, "messages": "[omitted]"}}

    try:
        import requests
    except ImportError as exc:
        raise RuntimeError("Missing dependency: requests. Install with `pip install requests`.") from exc

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=timeout,
    )

    try:
        response_json = response.json()
    except Exception as exc:
        raise RuntimeError(f"OpenRouter returned non-JSON response: HTTP {response.status_code}") from exc

    if response.status_code != 200:
        raise RuntimeError(f"OpenRouter error HTTP {response.status_code}: {json.dumps(response_json)[:1000]}")

    image_data = extract_image_from_response(response_json)
    if not image_data:
        raise RuntimeError("No image data found in response. Check model support or response format.")

    save_base64_image(image_data, output)
    return response_json


def extract_google_image(response_json: dict[str, Any]) -> str | None:
    """Extract base64 image from Gemini generateContent response."""
    for candidate in response_json.get("candidates", []):
        content = candidate.get("content", {})
        for part in content.get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if isinstance(inline, dict) and inline.get("data"):
                return inline["data"]
    return None


def generate_image_google(
    *,
    prompt: str,
    output: Path,
    model: str,
    input_image: Path | None,
    api_key: str,
    timeout: int,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Generate or edit image directly through Gemini API."""
    parts: list[dict[str, Any]] = [{"text": prompt}]
    if input_image:
        data_url = load_image_as_data_url(input_image)
        header, data = data_url.split(",", 1)
        mime = header.split(":", 1)[1].split(";", 1)[0]
        parts.append({"inline_data": {"mime_type": mime, "data": data}})

    resolved_model = resolve_model(model)
    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": {"responseModalities": ["IMAGE", "TEXT"]},
    }

    if dry_run:
        return {"dry_run": True, "provider": "google", "model": resolved_model, "payload_preview": "[omitted]"}

    try:
        import requests
    except ImportError as exc:
        raise RuntimeError("Missing dependency: requests. Install with `pip install requests`.") from exc

    response = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{resolved_model}:generateContent",
        headers={
            "x-goog-api-key": api_key,
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=timeout,
    )

    try:
        response_json = response.json()
    except Exception as exc:
        raise RuntimeError(f"Google Gemini returned non-JSON response: HTTP {response.status_code}") from exc

    if response.status_code != 200:
        raise RuntimeError(f"Google Gemini error HTTP {response.status_code}: {json.dumps(response_json)[:1000]}")

    image_data = extract_google_image(response_json)
    if not image_data:
        raise RuntimeError("No image data found in Google Gemini response. Check model support or response format.")

    save_base64_image(image_data, output)
    return response_json


def extract_openai_image(response_json: dict[str, Any]) -> str | None:
    """Extract base64 image from OpenAI Image API response."""
    data = response_json.get("data", [])
    if not data:
        return None
    first = data[0]
    if isinstance(first, dict):
        return first.get("b64_json")
    return None


def generate_image_openai(
    *,
    prompt: str,
    output: Path,
    model: str,
    input_image: Path | None,
    api_key: str,
    timeout: int,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Generate or edit image directly through OpenAI Image API."""
    resolved_model = resolve_model(model)
    headers = {"Authorization": f"Bearer {api_key}"}
    output_format = output_mime_type(output).split("/", 1)[1]

    if dry_run:
        return {
            "dry_run": True,
            "provider": "openai",
            "model": resolved_model,
            "mode": "edit" if input_image else "generation",
            "output_format": output_format,
        }

    try:
        import requests
    except ImportError as exc:
        raise RuntimeError("Missing dependency: requests. Install with `pip install requests`.") from exc

    if input_image:
        with input_image.open("rb") as image_file:
            response = requests.post(
                "https://api.openai.com/v1/images/edits",
                headers=headers,
                data={
                    "model": resolved_model,
                    "prompt": prompt,
                    "n": "1",
                    "size": "1024x1024",
                    "output_format": output_format,
                },
                files={"image": (input_image.name, image_file, output_mime_type(input_image))},
                timeout=timeout,
            )
    else:
        response = requests.post(
            "https://api.openai.com/v1/images/generations",
            headers={**headers, "Content-Type": "application/json"},
            json={
                "model": resolved_model,
                "prompt": prompt,
                "n": 1,
                "size": "1024x1024",
                "output_format": output_format,
            },
            timeout=timeout,
        )

    try:
        response_json = response.json()
    except Exception as exc:
        raise RuntimeError(f"OpenAI returned non-JSON response: HTTP {response.status_code}") from exc

    if response.status_code != 200:
        raise RuntimeError(f"OpenAI error HTTP {response.status_code}: {json.dumps(response_json)[:1000]}")

    image_data = extract_openai_image(response_json)
    if not image_data:
        raise RuntimeError("No image data found in OpenAI response. Check model support or response format.")

    save_base64_image(image_data, output)
    return response_json


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Generate or edit general-purpose non-technical images.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/generate_image.py "abstract blue presentation background, no text" -o assets/background.png

  python scripts/generate_image.py "make the sky warmer" --input photo.jpg -o edited_photo.png

  python scripts/generate_image.py "conceptual abstract texture illustration, no arrows, no labels" --mode general

Windows PowerShell:
  $env:OPENROUTER_API_KEY = "your_key_here"
  $env:GEMINI_API_KEY = "your_key_here"
  $env:OPENAI_API_KEY = "your_key_here"

Windows CMD:
  set OPENROUTER_API_KEY=your_key_here

Linux/macOS:
  export OPENROUTER_API_KEY="your_key_here"
        """,
    )
    parser.add_argument("prompt", help="Prompt for image generation or edit instruction.")
    parser.add_argument("-i", "--input", type=Path, help="Input image path for editing.")
    parser.add_argument("-o", "--output", type=Path, default=Path("generated_image.png"), help="Output image path.")
    parser.add_argument("--provider", choices=["openrouter", "google", "openai"], default=DEFAULT_PROVIDER, help="Image provider. Default: openrouter.")
    parser.add_argument("-m", "--model", default=DEFAULT_MODEL, help="Provider model id or alias: gemini, google-gemini, google-gemini-fast, flux-pro, flux-flex, openai-gpt-image, openai-gpt-image-2.")
    parser.add_argument("--api-key", help="Provider API key. Prefer environment variable or .env file.")
    parser.add_argument("--timeout", type=int, default=300, help="HTTP read timeout in seconds. Default: 300.")
    parser.add_argument("--mode", choices=["general", "edit"], default="general", help="Intent label for clarity.")
    parser.add_argument("--force-general", action="store_true", help="Proceed even if prompt looks technical.")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print request plan without calling API.")
    return parser.parse_args()


def main() -> int:
    """CLI entry point."""
    args = parse_args()

    warn_if_technical(args.prompt, force=args.force_general)

    model = args.model
    if model == DEFAULT_MODEL:
        model = provider_default_model(args.provider)

    api_key = args.api_key or find_env_api_key(args.provider)
    if not api_key and not args.dry_run:
        names = " or ".join(PROVIDER_ENV_KEYS[args.provider])
        print(f"Error: {names} not found.", file=sys.stderr)
        print("Set it as an environment variable or place it in a local .env file.", file=sys.stderr)
        return 1

    try:
        result = generate_image(
            provider=args.provider,
            prompt=args.prompt,
            output=args.output,
            model=model,
            input_image=args.input,
            api_key=api_key or "DRY_RUN",
            timeout=args.timeout,
            dry_run=args.dry_run,
        )
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.dry_run:
        print(json.dumps(result, indent=2))
    else:
        print(f"[generate-image] Wrote image: {args.output}")
        print("[generate-image] Reminder: this image is a visual asset, not scientific evidence.")
        print("[generate-image] Use scientific-schematics for technical diagrams and venue-templates for final figure formatting.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
