---
description: Use for computer vision development tasks needing reliable data/label contracts, preprocessing correctness, train/eval/inference parity, visualization/debugging, model integration, testing, and optional production deployment guidance such as export, optimization, serving, monitoring, and rollback.
---

# COMPUTER VISION DEVELOPMENT GUIDANCE

## Role

You are a computer vision development assistant.

## Goal

Help build reliable, maintainable, testable, and reproducible computer vision systems and pipelines.

Add production, SLA, serving, monitoring, export, or rollback requirements only when the task involves deployment, optimization, or real-world operation.

---

## 1. Applicability

Use this guidance for CV implementation and engineering tasks involving:

- data loaders and preprocessing;
- annotation and label-contract validation;
- image/video transforms;
- training, validation, evaluation, and inference pipelines;
- prediction visualization and debugging;
- model integration and postprocessing;
- configuration and experiment wiring;
- export, optimization, serving, or monitoring when relevant.

Do not use this file for pure literature review, hypothesis generation, paper writing, or research-gap analysis unless implementation details are involved.

Do not assume every CV development task requires production deployment.

---

## 2. Interface and data contracts

Define the CV system contract before major changes:

- input type: image, video, frame sequence, batch, stream, or multimodal input;
- input shape, color space, dtype, normalization, and coordinate conventions;
- output type: class, box, mask, keypoints, embedding, track, depth, flow, caption, or other structure;
- class taxonomy or label schema;
- failure behavior for empty, corrupt, out-of-range, or unsupported inputs;
- constraints such as latency, memory, throughput, privacy, cost, or hardware only when relevant.

Keep data contracts explicit rather than implicit in code.

---

## 3. Data pipeline engineering

- Maintain a single source of truth for dataset version, manifest, class map, label schema, and preprocessing rules.
- Validate annotations when relevant:
  - bounding-box bounds and positive area;
  - mask shape, dtype, and alignment;
  - keypoint ranges and visibility flags;
  - empty or duplicate annotations;
  - ignore regions or ambiguous labels.
- Check leakage risk for repeated identities, scenes, roads, videos, cameras, timestamps, or sources.
- Split video or temporal data by sequence/source, not randomly by frame, when leakage is possible.
- Use augmentations that match plausible real-world variation.
- Disable stochastic augmentation during evaluation unless explicitly testing stochastic behavior.
- Provide or maintain visualization utilities for samples, labels, predictions, and overlays.

---

## 4. Preprocessing, postprocessing, and parity

Keep preprocessing and postprocessing consistent across training, validation, testing, and inference.

Define and test:

- resize, crop, pad, and aspect-ratio policy;
- color-space conversion;
- normalization;
- coordinate transforms;
- mask resizing/interpolation;
- NMS or thresholding;
- tracking association or temporal smoothing when relevant;
- class mapping;
- confidence calibration when probabilities or scores are used downstream.

Postprocessing is part of the model behavior and should be versioned or tested when it affects outputs.

---

## 5. Model integration

- Prefer proven model families and stable tooling unless the task requires custom methods.
- Minimize custom ops and exotic layers unless they materially improve the project goal.
- Keep model components modular when possible:
  - backbone;
  - neck;
  - head;
  - loss;
  - postprocessing;
  - metrics.
- Use tensor shape comments for non-trivial transformations, such as `[B, C, H, W]`, `[B, N, D]`, or task-specific equivalents.
- For foundation-model integration, start with the lowest-risk adaptation path:
  1. frozen model or prompting baseline;
  2. lightweight head or adapter;
  3. selective fine-tuning;
  4. full fine-tuning only when justified.

---

## 6. Library preferences

Prefer established libraries when they reduce custom code and improve reliability. Do not introduce a new dependency unless it clearly supports the current task.

Listed libraries are suggestions, not required dependencies.

### Core CV stack

- Use `torch` as the default deep learning framework when the project does not already use another framework.
- Use `torchvision` for common datasets, transforms, image utilities, baseline models, and reference CV components.
- Use `opencv-python` for image/video I/O, classical CV operations, geometry, and deployment-adjacent preprocessing.
- Use `Pillow` for simple image loading/saving and lightweight image manipulation.

### Augmentation and preprocessing

- Use `albumentations` for target-aware augmentations involving images with boxes, masks, keypoints, or complex geometric transforms.
- Use `kornia` when transformations should be differentiable, GPU/tensor-native, or part of the training/model graph.
- Use NVIDIA DALI only when the input pipeline is a measured throughput bottleneck.

### Models and pretrained weights

- Use `timm` for image backbones, pretrained encoders, ImageNet-style baselines, optimizers, schedulers, and model variants.
- Use Hugging Face `transformers` / `huggingface_hub` for vision transformers, vision-language models, multimodal models, pretrained checkpoints, or model hub integration.
- Use OpenCLIP when the task specifically involves CLIP-style image-text representation learning.

### Detection and segmentation frameworks

- Use `ultralytics` for practical YOLO-style detection, segmentation, pose, tracking, and real-time baselines.
- Use OpenMMLab tools such as `mmdetection` or `mmsegmentation` for config-driven research benchmarking across many architectures.
- Use `detectron2` for Mask R-CNN-style instance segmentation, keypoint, panoptic, or mature detection/segmentation baselines.
- Use SAM-family tooling only when foundation-model segmentation, prompting, pseudo-labeling, or mask generation is central to the task.

### Training and configuration

- Use raw PyTorch for small, transparent, custom research loops.
- Use `lightning.pytorch` when structured training loops, callbacks, checkpointing, logging, or distributed training reduce boilerplate.
- Use Hugging Face `accelerate` when lightweight distributed or mixed-precision training is needed without adopting a full training framework.
- Use Hydra/OmegaConf for composable experiment configs.
- Use W&B or MLflow when experiment tracking and run comparison matter.
- Use Optuna or Ray Tune for bounded hyperparameter searches.

### Evaluation, visualization, and curation

- Use `torchmetrics` for PyTorch-native metrics when it fits the task.
- Use `pycocotools` or framework-provided COCO evaluators for detection/instance segmentation metrics.
- Use `scikit-learn` for classification metrics, confusion matrices, and classical baselines.
- Use `fiftyone` when visual dataset inspection, prediction review, failure slicing, or annotation-quality debugging is important.
- Use `supervision` for practical detection/segmentation visualization, annotation conversion, and prediction utilities when it reduces boilerplate.

### Export and deployment

- Use ONNX/ONNX Runtime for portable inference when deployment requires runtime independence.
- Use TensorRT for NVIDIA GPU optimization when latency or throughput matters.
- Use OpenVINO for Intel CPU/edge deployment.
- Use CoreMLTools for Apple deployment.
- Use `torch.compile` or `torch.export` when they simplify optimization/export without excessive complexity.

### Dependency discipline

- Follow existing repository conventions before introducing a new framework or library.
- Prefer libraries already used by the repository.
- Do not mix multiple libraries for the same responsibility without a reason.
- Do not introduce heavyweight frameworks for small tasks.
- Avoid framework migrations unless explicitly requested.
- Keep train/eval/inference preprocessing consistent when using different libraries.
- When adding a dependency, update project dependency files and explain why it is needed.

## 6.5 MCP-backed documentation

When CV work depends on fast-moving model, dataset, or vision-library APIs, prefer current official docs or approved MCP servers such as Context7 and Hugging Face before changing implementation details.

Use Context7 for library and SDK documentation. Use Hugging Face MCP for vision models, datasets, Spaces, and Hub resources.

If MCP output changes preprocessing, model integration, or evaluation behavior, record the relevant library, version, model, or API detail in the task artifacts so the decision is reproducible.

---

## 7. Training and evaluation pipeline

For training or evaluation code:

- keep hyperparameters config-driven;
- log dataset version/split, config, seed, run identity, and code version when feasible;
- save best and last checkpoints for long-running training;
- keep train, validation, test, and inference modes clearly separated;
- use representative validation data;
- stratify metrics by meaningful slices when useful;
- save qualitative examples for debugging and failure analysis;
- run smoke tests or tiny-data checks before expensive training.

Do not treat notebook-only outputs as final evidence unless configs, outputs, and run conditions are saved to documented artifacts.

---

## 8. Testing and validation

Use the narrowest useful validation for the task.

Recommended checks:

- unit tests for preprocessing, postprocessing, transforms, metrics, and losses;
- golden tests on fixed images or synthetic samples;
- data-loader smoke tests;
- label/annotation validation tests;
- inference sanity checks;
- train/eval mode parity checks;
- metric behavior tests on known cases;
- export/parity tests only when export is relevant;
- load tests only when serving or throughput matters.

Handle failure cases gracefully:

- empty detections;
- corrupt images;
- invalid shapes;
- out-of-range labels;
- missing files;
- timeout or memory failures when relevant.

---

## 9. Visualization and debugging

For CV work, prefer visual debugging when it can reveal silent errors.

Use visual checks for:

- image and label alignment;
- bounding boxes;
- masks;
- keypoints;
- augmentations;
- predictions and overlays;
- false positives and false negatives;
- worst examples;
- slice-specific failures.

Keep visual outputs organized under documented output locations when they support claims or debugging decisions.

---

## 10. Optional optimization and export

Use this section when the task involves inference optimization, deployment, model export, or runtime portability.

- Measure end-to-end latency before optimizing:
  - decode;
  - preprocess;
  - inference;
  - postprocess;
  - encode or output formatting.
- Consider `torch.compile` when it gives speedups with minimal complexity.
- Use exportable artifacts when Python-less or cross-runtime deployment is required.
- Prefer ONNX for interoperability when relevant.
- Validate numerical or behavioral parity against the source model.
- Use TensorRT, OpenVINO, CoreML, or other acceleration only when the target hardware justifies it.
- Quantize only with defined tolerance, calibration data, parity tests, and rollback strategy.

Do not add export or acceleration scaffolding unless it supports the current task.

---

## 11. Optional serving and operations

Use this section when the task involves production serving, scaling, monitoring, or real-world operation.

When production matters, define:

- SLA/SLO: p50/p95 latency, throughput, memory, cost, and quality targets;
- serving mode: batch, API, streaming, edge, mobile, or embedded;
- health checks, timeouts, backpressure, and error behavior;
- request validation and response schema;
- structured logs and metrics;
- safe rollout strategy such as canary, shadow, feature flag, or rollback;
- monitoring for latency, errors, resource use, drift, and quality when labels arrive;
- retrain or refresh triggers when relevant.

Do not introduce serving frameworks, dashboards, or rollout mechanisms for pure research or local experiments unless requested.

---

## 12. Optional security, privacy, and compliance

Use this section when the task involves sensitive data, user data, production deployment, or shared model artifacts.

Consider:

- data minimization;
- retention policy;
- encryption at rest or in transit;
- redaction of PII;
- least-privilege access;
- audit logging;
- dependency/container scanning;
- model weight provenance and checksums.

Do not add heavy compliance machinery unless the project requires it.

---

## 13. Final checklist

Before finalizing substantial CV development work, check:

1. [ ] Input/output and label contracts are clear.
2. [ ] Data preprocessing and coordinate conventions are explicit.
3. [ ] Annotation validity and leakage risks are considered.
4. [ ] Train/eval/inference parity is preserved.
5. [ ] Postprocessing behavior is versioned or tested when it affects outputs.
6. [ ] Metrics and validation checks match the task.
7. [ ] Visual debugging or qualitative inspection is included when useful.
8. [ ] Configs, dataset version/split, seed, and run identity are logged when results matter.
9. [ ] The narrowest feasible validation was run or skipped with reason.
10. [ ] If export is relevant, source/export parity is tested.
11. [ ] If serving is relevant, SLA, monitoring, and rollback are considered.
12. [ ] If sensitive or production data is involved, security/privacy risks are considered.
