# ML Leakage Patterns

This reference lists common leakage and confounding patterns in ML and computer vision workflows.

Use it when auditing datasets, splits, preprocessing, evaluation protocols, or result claims.

Leakage means the model, training process, evaluation process, or research workflow has access to information that would not be available in the intended real setting.

---

## 1. Duplicate and near-duplicate leakage

### Pattern

The same or highly similar sample appears in both training and evaluation splits.

### CV examples

- Same image resized or compressed differently.
- Adjacent video frames split across train and test.
- Burst-mode photos split randomly.
- Same road scene captured from slightly different angles.
- Cropped patches from the same original image distributed across splits.

### Detection ideas

- Hash exact files.
- Use perceptual hashes.
- Compare image embeddings.
- Group by original image ID, video ID, road segment, capture session, or source folder.
- Manually inspect nearest neighbors across splits.

### Risk

The model may memorize scene appearance instead of learning the target concept.

---

## 2. Source leakage

### Pattern

The source of the data is correlated with the label or target.

### Examples

- All severe damage images come from one city or camera.
- Positive examples come from one dataset and negative examples from another.
- Certain labels are mostly from one annotation campaign.
- Test data shares the same capture device distribution as training, while deployment will not.

### Detection ideas

- Compare label distribution by source.
- Compare split distribution by source.
- Train a simple classifier to predict split or source from metadata.
- Check whether source-specific backgrounds correlate with labels.

### Risk

The model learns source artifacts instead of semantic content.

---

## 3. Group leakage

### Pattern

Samples from the same real-world entity are split across train and test.

### Common groups

- patient;
- user;
- road segment;
- camera;
- vehicle;
- location;
- video;
- building;
- sensor;
- timestamp sequence;
- document;
- product;
- scene.

### CV road-damage examples

- Same road segment appears in both train and test.
- Same dashcam route is randomly split by frame.
- Same city block appears under slightly different lighting.
- Same camera vehicle captures both train and test data.

### Mitigation

Split by group, not by individual sample.

---

## 4. Temporal leakage

### Pattern

Future information influences training or validation.

### Examples

- Random split across time when deployment is future-facing.
- Preprocessing statistics computed using all data, including test.
- Labels corrected using later information unavailable at prediction time.
- Road repair state indirectly reveals future condition.
- Model selection uses test data collected after training period.

### Mitigation

Use time-aware splits when deployment is temporal.

---

## 5. Preprocessing leakage

### Pattern

Preprocessing uses information from validation or test data.

### Examples

- Normalization statistics computed on the full dataset.
- Feature selection performed before splitting.
- Imputation fitted on all data.
- Vocabulary/tokenizer fitted on all documents including test.
- Image normalization calibrated using test images.

### Mitigation

Fit preprocessing only on training data unless the operation is genuinely label- and split-independent.

---

## 6. Augmentation leakage

### Pattern

Augmented versions of the same sample appear across splits.

### Examples

- Original image in train, augmented copy in test.
- Crops from one image assigned to different splits.
- Synthetic samples generated from test images.
- Pseudo-labels generated using models trained with test-adjacent data.

### Mitigation

Split before augmentation.

Keep all derivatives of a source sample in the same split.

---

## 7. Label leakage

### Pattern

The input contains information that directly or indirectly reveals the label.

### Examples

- Folder names encode labels and are included as features.
- File names contain class names.
- Metadata includes annotation status.
- Image overlays, masks, or watermarks reveal labels.
- Different label classes use different image resolutions or formats.
- Annotation artifacts are visible in images.

### Detection ideas

- Inspect filenames and paths.
- Train metadata-only baselines.
- Check image dimensions, compression, and source distributions by label.
- View random samples for visual artifacts.

---

## 8. Test-set tuning leakage

### Pattern

The final evaluation set influences model selection, thresholds, prompts, or reporting.

### Examples

- Threshold chosen based on test performance.
- Test failures inspected repeatedly during development.
- Prompt or postprocessing adjusted after looking at test outputs.
- Best checkpoint selected using test metric.
- Qualitative examples from test set guide model changes.

### Mitigation

Use validation data for tuning.

Keep final test data untouched until final evaluation.

Record when and how evaluation data was inspected.

---

## 9. Cross-validation leakage

### Pattern

Cross-validation folds are not independent.

### Examples

- Related samples appear in different folds.
- Preprocessing is fitted before fold splitting.
- Hyperparameters are selected using outer-fold test results.
- Augmented copies cross folds.
- Patient/location/video groups cross folds.

### Mitigation

Use grouped or nested cross-validation when needed.

Fit preprocessing inside each training fold.

---

## 10. Annotation leakage

### Pattern

Annotation process differs across splits or labels in ways that leak information.

### Examples

- One annotator labels mostly positive samples.
- Label style changes across time.
- Bounding-box tightness differs by dataset source.
- Certain classes have systematically different annotation quality.
- Test annotations were cleaned more carefully than train annotations.

### CV risks

- Model learns annotation style.
- Evaluation rewards dataset-specific conventions.
- Apparent improvement reflects label consistency, not model quality.

### Detection ideas

- Compare annotator, campaign, and source metadata across splits.
- Inspect annotation density and box size distribution.
- Check class imbalance and ignored labels by split.
- Review random labels per split.

---

## 11. Metric leakage

### Pattern

Evaluation metric or postprocessing is tuned to exploit test characteristics.

### Examples

- NMS threshold tuned on test.
- Confidence threshold chosen to maximize test F1.
- Class merging decided after test failures.
- Evaluation ignores difficult cases after inspection.
- Metric implementation changes after seeing results.

### Mitigation

Freeze evaluation protocol before final evaluation.

Document thresholds and postprocessing.

---

## 12. Foundation model and pretraining leakage

### Pattern

Pretrained models may have seen evaluation data or highly similar data.

### Examples

- Public benchmark images included in web-scale pretraining.
- Vision-language model has seen captions or examples from the benchmark.
- Synthetic data generated by a model trained on overlapping sources.

### Mitigation

Acknowledge pretraining uncertainty.

Use held-out private or newly collected data when possible.

Compare against equivalent pretrained baselines.

---

## 13. Leakage audit checklist

Before claiming a split or evaluation is leakage-safe, check:

1. Are exact duplicates removed or grouped?
2. Are near-duplicates checked?
3. Are groups such as road, video, camera, location, source, or time kept within one split?
4. Are preprocessing statistics fit only on training data?
5. Are augmentations applied after splitting?
6. Are filenames, folders, metadata, or image artifacts label-revealing?
7. Was test data used for tuning, threshold selection, prompt iteration, or qualitative selection?
8. Are annotation styles consistent across splits?
9. Are baseline and proposed method evaluated under the same protocol?
10. Is there an artifact documenting the leakage audit?

Do not claim “no leakage” without either evidence or clearly stated assumptions.