#!/usr/bin/env python3
"""
Optional PDF generation utility for literature-review artifacts.

Converts a Markdown literature review into a PDF using Pandoc and a LaTeX
engine. This script is optional; literature-review outputs do not need to be
PDFs unless the user requests a shareable or archival artifact.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


DEFAULT_ENGINE_CANDIDATES = ["xelatex", "lualatex", "pdflatex"]


def find_available_engine(preferred: str | None = None) -> str | None:
    """Return the first available PDF engine."""
    candidates = [preferred] if preferred else []
    candidates.extend([e for e in DEFAULT_ENGINE_CANDIDATES if e != preferred])

    for engine in candidates:
        if engine and shutil.which(engine):
            return engine
    return None


def generate_pdf(
    markdown_file: str,
    output_pdf: str | None = None,
    citation_style: str = "apa",
    template: str | None = None,
    toc: bool = True,
    number_sections: bool = True,
    pdf_engine: str | None = None,
) -> bool:
    """Generate a PDF from a markdown file using pandoc."""

    md_path = Path(markdown_file)
    if not md_path.exists():
        print(f"Error: Markdown file not found: {markdown_file}")
        return False

    if output_pdf is None:
        output_pdf = str(md_path.with_suffix(".pdf"))

    if not shutil.which("pandoc"):
        print("Error: pandoc is not installed.")
        print("Install with: brew install pandoc (macOS) or apt-get install pandoc (Linux)")
        return False

    engine = find_available_engine(pdf_engine)
    if engine is None:
        print("Error: No supported LaTeX PDF engine found.")
        print("Install one of: xelatex, lualatex, or pdflatex")
        print("Note: latexmk is useful, but this script currently passes a LaTeX engine to pandoc.")
        return False

    cmd = [
        "pandoc",
        str(md_path),
        "-o",
        str(output_pdf),
        f"--pdf-engine={engine}",
        "-V",
        "geometry:margin=1in",
        "-V",
        "fontsize=11pt",
        "-V",
        "colorlinks=true",
        "-V",
        "linkcolor=blue",
        "-V",
        "urlcolor=blue",
        "-V",
        "citecolor=blue",
    ]

    if toc:
        cmd.extend(["--toc", "--toc-depth=3"])

    if number_sections:
        cmd.append("--number-sections")

    bib_file = md_path.with_suffix(".bib")
    if bib_file.exists():
        csl_value = citation_style if citation_style.endswith(".csl") else f"{citation_style}.csl"
        cmd.extend(["--citeproc", "--bibliography", str(bib_file), "--csl", csl_value])

    if template:
        template_path = Path(template)
        if template_path.exists():
            cmd.extend(["--template", str(template_path)])
        else:
            print(f"Warning: template not found, ignoring: {template}")

    try:
        print(f"Generating PDF: {output_pdf}")
        print(f"Using PDF engine: {engine}")
        print(f"Command: {' '.join(cmd)}")
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✓ PDF generated successfully: {output_pdf}")
        return True
    except subprocess.CalledProcessError as e:
        print("Error generating PDF:")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False


def check_dependencies() -> bool:
    """Check if required dependencies are installed."""
    checks = {
        "pandoc": shutil.which("pandoc"),
        "latexmk": shutil.which("latexmk"),
        "xelatex": shutil.which("xelatex"),
        "lualatex": shutil.which("lualatex"),
        "pdflatex": shutil.which("pdflatex"),
    }

    print("Dependency check:")
    for name, path in checks.items():
        if path:
            print(f"✓ {name} is installed ({path})")
        else:
            print(f"✗ {name} is NOT installed")

    has_engine = any(checks[name] for name in ("xelatex", "lualatex", "pdflatex"))

    if not checks["pandoc"]:
        print("\nMissing required dependency: pandoc")
        return False

    if not has_engine:
        print("\nMissing required LaTeX engine.")
        print("Install one of: xelatex, lualatex, or pdflatex")
        print("latexmk alone is not enough for this script unless you explicitly redesign the pandoc pipeline.")
        return False

    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a PDF from markdown using pandoc.")
    parser.add_argument("markdown_file", nargs="?", help="Path to markdown file")
    parser.add_argument("output_pdf", nargs="?", help="Output PDF path")
    parser.add_argument("--citation-style", default="apa", help="Citation style (default: apa)")
    parser.add_argument("--template", help="Path to custom LaTeX template")
    parser.add_argument("--pdf-engine", choices=["xelatex", "lualatex", "pdflatex"], help="Preferred PDF engine")
    parser.add_argument("--no-toc", action="store_true", help="Disable table of contents")
    parser.add_argument("--no-numbers", action="store_true", help="Disable section numbering")
    parser.add_argument("--check-deps", action="store_true", help="Check if dependencies are installed")
    return parser.parse_args()


def main():
    args = parse_args()

    if args.check_deps:
        sys.exit(0 if check_dependencies() else 1)

    if not args.markdown_file:
        print("Usage: python generate_pdf.py <markdown_file> [output_pdf] [options]")
        sys.exit(1)

    success = generate_pdf(
        markdown_file=args.markdown_file,
        output_pdf=args.output_pdf,
        citation_style=args.citation_style,
        template=args.template,
        toc=not args.no_toc,
        number_sections=not args.no_numbers,
        pdf_engine=args.pdf_engine,
    )
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()