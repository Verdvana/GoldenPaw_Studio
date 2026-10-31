# Outfit Generation Record
- asset_id: OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v002
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- asset_purpose: design_reference
- view_type: design_reference
- head_policy: not_applicable
- candidate_version: v002
- status: APPROVED
- generation_tool: built-in image_gen.imagegen
- generated_at: 2026-10-30
- authorization: 2026-10-30 user requested normal shorts instead of low-rise, with hosiery waistband still far above shorts
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v002.png
- original_candidate_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v002_design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v002.png
- output_sha256: f23cac0b56d8d24a75778d2c49522e17bf3b45bff8a1e4f6aa1293cbba4f9a7d

## Validation target
- fit_or_design_question: regular mid-rise normal-length shorts with a taller denim front rise; distinct much higher hosiery waist near blouse
- acceptance_checks: shorts genuinely changed; white sheer panel remains substantial; blouse/shoes/material continuity retained; product-only image

## Generation inputs
```yaml
generation_inputs:
  - asset_id: OWNER_DATE_SUMMER_01_DESIGN_REFERENCE
    version: v001 approved historical low-rise design
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE.png
    sha256: d50e6073e79f744e40b94d1b954d41439ac01eb62e4a5db9fe70afa851fbb3de
    responsibility: edit target; blouse, hosiery material/construction, sandals, palette and layout only
    must_not_define: [revised shorts waist/rise/length, person, face, body proportions, skin, hair, identity]
qa_comparison_only: []
reference_budget: {maximum_images: 1, actual_images: 1}
```

## Reference isolation
- garment_references_used: approved clothing-only design above; resolved from outfit manifest
- previous_candidate_pixels_used: false (approved garment design edit only)
- previous_shot_pixels_used: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false
- lighting_or_background_taken_from_garment_reference: product layout/lighting retained for this edit only; no owner authority
- no source identity images or failed worn attempts attached; no raster copies in inputs

## Prompt assembly / settings
- Exact prompt: PROMPT.txt alongside this record
- Edit one clothing-only image; opaque background
- Seed/model/quality/resolution: tool defaults / not exposed
- User-directed design revision; no worn generation in this call

## QA
- technical_status: PASS
- fit_validation_status: REVIEW_REQUIRED (design review; no worn validation)
- face_contamination_check: NOT_APPLICABLE
- face_generation_method_followed: not_applicable
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- decision: regular-rise shorts visibly revised; design candidate ready for user review, no automatic promotion
- reviewer: Codex visual inspection
- reviewed_at: 2026-10-30


## User approval

- approved_by: user
- approval_date: 2026-10-30
- approval_evidence: “好 继续生成” after revised regular-rise design
- scope: L2 design only; authorize one worn-front validation candidate
- promotion_operation: MOVED unchanged; no duplicate raster
- current_approved_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v002.png
- approved_sha256: f23cac0b56d8d24a75778d2c49522e17bf3b45bff8a1e4f6aa1293cbba4f9a7d
