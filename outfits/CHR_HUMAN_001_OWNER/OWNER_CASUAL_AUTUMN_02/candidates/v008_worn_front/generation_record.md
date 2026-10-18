# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v008

- asset_id: `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v008`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `worn_front`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v008`
- status: `REJECTED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-10-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v008_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v008.png`
- output_sha256: `4a5c38f46a0cb191c9425640ba83a4398bbccd2bbbb3a12a86d7254b5bbfa889`
- reference_set_ids: [`OWNER_L0_FACE_FRONT_NEUTRAL`, `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE`, `HOS_15D_WHITE_SOFT_SHEEN_FRONT`]
- reference_budget: `5 generation inputs; 2 QA-only comparisons`
- aspect_ratio: `3:4 portrait`
- seed_settings: `ImageGen does not expose seed or sampler settings`

## Validation target

One independent full-body front fit-validation candidate matching approved v005, with readable pale sheer hosiery and covered toes. Denier is a design parameter left open by `OUTFIT.md`; this candidate uses medium-sheer 30D hosiery to make textile continuity legible while retaining translucency. Earlier candidates v005–v007 are rejected and are not inputs.

## Generation inputs

```yaml
generation_inputs:
  - asset_id: L0_OWNER_012
    path: characters/CHR_HUMAN_001_OWNER/source/identity/raw/14.jpg
    responsibility: L0 frontal face identity and natural skin context only, under Face method constraints
    must_not_define: [source hair, clothing, body, pose, camera, lighting, background]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    responsibility: Hairstyle A only
    must_not_define: [face, identity, skin, body, clothing, lighting, background, gray mask]
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: face-excluded neck-below body proportions and front stance only
    must_not_define: [face, identity, hair, clothing, hosiery, lighting, background]
  - asset_id: OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v005
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png
    responsibility: approved outfit garments/colors/layers/slippers only
    must_not_define: [face, body, proportions, skin, hair, identity, pose, lighting, background]
  - asset_id: L0_HOS_15_WSS_002
    path: materials/hosiery/source_library/raw/15d_white_soft_sheen/IMG_2604.jpg
    responsibility: pale white hosiery color and continuous leg-to-foot textile response only
    must_not_define: [person, face, body proportions, skin pigmentation, pose, clothing, shoes, background, lighting]
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope: [identity drift, face contamination, facial relationships, projection]
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    comparison_scope: [body proportions and stance]
```

## Reference isolation

- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`; source-derived L0 only
- hairstyle: `HAIRSTYLE_A`
- body_reference_is_face_excluded_derivative: `true`
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- hosiery_source_is_material_only: `true`
- QA comparisons are not generator inputs
- prompt assembly: `PROMPT_ASSEMBLY.md`

## QA

- technical_status: `PASS` (1086x1448, exact 3:4, full head and both feet visible)
- fit_validation_status: `UNREVIEWED`
- face_contamination_check: `REVIEW_REQUIRED` (no obvious blotches; possible tone/identity drift remains for reviewer)
- face_generation_method_followed: `true`
- hosiery_continuity_and_material_check: `FAIL` (legs appear bare; toe fabric not visible)
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- outfit_fidelity_check: `PASS`
- decision: `REJECTED — hosiery continuity and visible toe coverage not met`
- reviewer: `Codex visual QA`
- reviewed_at: `2026-10-17`
