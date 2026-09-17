# Outfit Generation Record

- asset_id:
- outfit_id:
- asset_level: L2
- asset_purpose: `design_reference|worn_fit_validation|material_detail|drape_detail|construction_detail`
- view_type: `design_reference|worn_front|worn_3q|worn_back|material_detail|drape_detail|construction_detail`
- head_policy: `not_applicable|head_present_owner_face_method`
- candidate_version:
- status: `DRAFT|REVIEW_REQUIRED|REJECTED|APPROVED`
- generation_tool:
- generated_at:
- output_path:
- output_sha256:

## Validation target

- fit_or_design_question:
- acceptance_checks:
  -

## Generation inputs

Only actual image inputs used for generation belong here. Resolve paths through the
reference registry or the outfit's garment-reference manifest before generation.

```yaml
generation_inputs:
  - asset_id:
    path:
    responsibility:
    must_not_define:
      -
```

For a visible owner face, the sole face authority is the applicable source-derived
Face method and its L0 inputs. An AI Face Canon, AI Body Canon, previous outfit,
previous shot, or generated candidate must not appear in this section.

## QA comparison only

These are post-generation comparison references and must never be passed to the
generator or treated as identity lineage.

```yaml
qa_comparison_only:
  - asset_id:
    path:
    comparison_scope:
      - identity drift
      - face contamination
      - framing/projection
```

## Reference isolation

- garment_references_used:
  -
- previous_candidate_pixels_used: `true|false`
- previous_shot_pixels_used: `true|false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## QA

- technical_status: `UNREVIEWED|PASS|FAIL`
- fit_validation_status: `UNREVIEWED|PASS|FAIL|REVIEW_REQUIRED`
- face_contamination_check: `PASS|FAIL|REVIEW_REQUIRED|NOT_APPLICABLE`
- face_generation_method_followed: `true|false|not_applicable`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision:
- reviewer:
- reviewed_at:
