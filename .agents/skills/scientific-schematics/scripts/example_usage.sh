#!/usr/bin/env bash
# Example usage for scientific-schematics on Linux/macOS.
#
# This launcher demonstrates evidence-aware technical diagram generation.
# Generated diagrams must be manually checked before manuscript use.

set -euo pipefail

echo "=========================================="
echo "Scientific Schematics - Linux/macOS Examples"
echo "=========================================="
echo ""

if [ -z "${OPENROUTER_API_KEY:-}" ]; then
    echo "ERROR: OPENROUTER_API_KEY is not set."
    echo "Set it with:"
    echo "  export OPENROUTER_API_KEY='your_key_here'"
    exit 1
fi

mkdir -p figures

echo "Example 1: Method pipeline"
python scripts/generate_schematic.py \
  "Create a clean left-to-right method pipeline with exactly five blocks: input image -> preprocessing -> detector backbone -> detection head -> bounding-box output. Use only these blocks and adjacent arrows." \
  -o figures/method_pipeline_example.png \
  --doc-type conference \
  --iterations 1 \
  --provider openrouter \
  --timeout 300

echo ""
echo "Example 2: Training/evaluation protocol"
python scripts/generate_schematic.py \
  "Create a top-to-bottom experiment protocol diagram: dataset -> train/validation/test split -> train model on train split -> select checkpoint on validation split -> evaluate once on test split -> metric report. Do not show test-set tuning." \
  -o figures/eval_protocol_example.png \
  --doc-type report \
  --iterations 1 \
  --provider openrouter \
  --timeout 300

if [ -n "${GEMINI_API_KEY:-}" ]; then
  echo ""
  echo "Example 3: Direct Gemini smoke test"
  python scripts/generate_schematic.py \
    "Create a simple three-block left-to-right workflow: input image -> preprocessing -> prediction. Use only these labels." \
    -o figures/gemini_direct_smoke_test.png \
    --doc-type presentation \
    --iterations 1 \
    --provider google \
    --timeout 600
else
  echo ""
  echo "Skipping direct Gemini example because GEMINI_API_KEY is not set."
fi

if [ -n "${OPENAI_API_KEY:-}" ]; then
  echo ""
  echo "Example 4: Direct OpenAI smoke test"
  python scripts/generate_schematic.py \
    "Create a simple three-block left-to-right workflow: input image -> preprocessing -> prediction. Use only these labels." \
    -o figures/openai_direct_smoke_test.png \
    --doc-type presentation \
    --iterations 1 \
    --provider openai \
    --timeout 600
else
  echo ""
  echo "Skipping direct OpenAI example because OPENAI_API_KEY is not set."
fi

echo ""
echo "Done. Manually verify all generated diagrams before manuscript use."
