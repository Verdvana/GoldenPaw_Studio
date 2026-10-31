# Outfit Generation Record
- asset_id: OWNER_DATE_SUMMER_01_WORN_FRONT_v001
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- asset_purpose: worn_fit_validation
- view_type: worn_front
- head_policy: head_present_owner_face_method
- candidate_version: v001
- status: REVIEW_REQUIRED
- generation_tool: built-in image_gen.imagegen
- generated_at: attempted 2026-10-30; no image returned
- authorization: user “可以 继续”, 2026-10-30; approved design and requested next fitting candidate
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v001_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v001.png
- output_sha256: null (no raster returned)

## Validation target
- fit_or_design_question: verify underbust hem, high hosiery waist covering navel and approaching top, shorts below navel, material continuity and open-toe stiletto fit
- acceptance_checks: identity and clean skin; Hair A; current Body01 proportions; neckline/sleeves/hem; clearly separate high/low waistlines; sheer white abdominal panel; closed-toe textile under sandals; balanced heel support

## Generation inputs
```yaml
generation_inputs:
  - asset_id: OWNER_DATE_SUMMER_01_DESIGN_REFERENCE
    version: v001 approved
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE.png
    responsibility: approved garment design, layering, colors, textile and sandals only
    must_not_define: owner face, body proportions, skin, hair, identity, pose, lighting, background
  - asset_id: OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001
    version: v1 deterministic derivative
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png
    responsibility: L0 face geometry, recognizable adult identity only
    must_not_define: skin color, hair, body, outfit, makeup, camera, lighting, background
  - asset_id: OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001
    version: v1 deterministic derivative
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png
    responsibility: L0 warm-neutral natural skin baseline only
    must_not_define: face geometry, identity geometry, hair, body, outfit, camera, background
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    version: v7 / Canon 007 derivative
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: face-excluded current Body01 neck-below geometry only
    must_not_define: face, identity, skin, hair, clothing, hosiery appearance, lighting, background
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    version: v1 deterministic derivative
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    responsibility: L0 Hairstyle A only
    must_not_define: face, skin, body, outfit, pose, lighting, background
reference_budget: {maximum_images: 5, actual_images: 5}
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope: [identity drift, face contamination, framing/projection]
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    comparison_scope: [body proportion QA only]
```

## Reference resolution and method
- Named sets: OWNER_L0_FACE_013_GEOMETRY_CROP_V1, OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1, OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE, OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE.
- Nearest identity REFERENCE_GUIDE and FACE_01_FRONT_NEUTRAL_METHOD.md read; current source-only global rule overrides historical B_FACE_SKIN_CONTEXT_NO_CROWN and AI face input routing.
- Face method prompt constraints retained; two deterministic real L0 crops replace generated B face context per global source-only rule.
- Body crop provenance: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/PROVENANCE.md; crop x=0,y=308,w=1086,h=1140; no generative transformation.
- Face/skin crop provenance: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/PROVENANCE.md.
- Hair provenance: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/REFERENCE_INPUTS.md.
- Input SHA-256 checksums: INPUT_CHECKSUMS.txt.
- Approved outfit file is clothing-only; not a generated human identity input.
- No extra material photo: approved L2 design and written material contract define white sheer hosiery; do not import nude calibration material.

## Reference isolation
- garment_references_used: approved design only
- previous_candidate_pixels_used: false (approved clothing-only design is scoped input)
- previous_shot_pixels_used: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false
- lighting_or_background_taken_from_garment_reference: false

## Settings / prompt assembly
- PROMPT.txt is exact submitted prompt
- 1 fresh candidate, opaque background, native portrait 3:4 requested
- model, seed, sampler, exact resolution and quality: not exposed / tool defaults
- No raster input copies in this directory.

## QA
- technical_status: FAIL (service moderation block, no output)
- fit_validation_status: REVIEW_REQUIRED (not performed; no output)
- face_contamination_check: REVIEW_REQUIRED
- face_generation_method_followed: true
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- decision: BLOCKED_NO_OUTPUT; not a visual QA rejection, no candidate raster exists; no retry or downstream use
- reviewer: Codex, execution result only
- reviewed_at: 2026-10-30


## Execution failure

- HTTP 400 moderation_blocked at output stage, category sexual.
- request_id: 51bb7620-26a6-44cd-aa01-ba542bd98115
- No output returned, saved, reviewed, approved or used downstream.
- Intended output_path above is reserved only, not an existing file.
