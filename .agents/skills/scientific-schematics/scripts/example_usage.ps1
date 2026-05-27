# Example usage for scientific-schematics on Windows PowerShell.
# Generated diagrams must be manually checked before manuscript use.

Write-Host "=========================================="
Write-Host "Scientific Schematics - PowerShell Examples"
Write-Host "=========================================="
Write-Host ""

if (-not $env:OPENROUTER_API_KEY) {
    Write-Host "ERROR: OPENROUTER_API_KEY is not set."
    Write-Host "Set it for this session with:"
    Write-Host '  $env:OPENROUTER_API_KEY = "your_key_here"'
    Write-Host "Or persist it with:"
    Write-Host '  [Environment]::SetEnvironmentVariable("OPENROUTER_API_KEY", "your_key_here", "User")'
    exit 1
}

New-Item -ItemType Directory -Force -Path "figures" | Out-Null

Write-Host "Example 1: Method pipeline"
python scripts/generate_schematic.py `
  "Create a clean left-to-right method pipeline with exactly five blocks: input road image -> preprocessing -> detector backbone -> detection head -> bounding-box output. Use only these blocks and adjacent arrows." `
  -o figures/method_pipeline_example.png `
  --doc-type conference `
  --iterations 1 `
  --provider openrouter `
  --timeout 300

Write-Host ""
Write-Host "Example 2: Training/evaluation protocol"
python scripts/generate_schematic.py `
  "Create a top-to-bottom experiment protocol diagram: dataset -> train/validation/test split -> train model on train split -> select checkpoint on validation split -> evaluate once on test split -> metric report. Do not show test-set tuning." `
  -o figures/eval_protocol_example.png `
  --doc-type report `
  --iterations 1 `
  --provider openrouter `
  --timeout 300

if ($env:GEMINI_API_KEY) {
    Write-Host ""
    Write-Host "Example 3: Direct Gemini smoke test"
    python scripts/generate_schematic.py `
      "Create a simple three-block left-to-right workflow: input image -> preprocessing -> prediction. Use only these labels." `
      -o figures/gemini_direct_smoke_test.png `
      --doc-type presentation `
      --iterations 1 `
      --provider google `
      --timeout 600
} else {
    Write-Host ""
    Write-Host "Skipping direct Gemini example because GEMINI_API_KEY is not set."
}

if ($env:OPENAI_API_KEY) {
    Write-Host ""
    Write-Host "Example 4: Direct OpenAI smoke test"
    python scripts/generate_schematic.py `
      "Create a simple three-block left-to-right workflow: input image -> preprocessing -> prediction. Use only these labels." `
      -o figures/openai_direct_smoke_test.png `
      --doc-type presentation `
      --iterations 1 `
      --provider openai `
      --timeout 600
} else {
    Write-Host ""
    Write-Host "Skipping direct OpenAI example because OPENAI_API_KEY is not set."
}

Write-Host ""
Write-Host "Done. Manually verify all generated diagrams before manuscript use."
