# Outfit Generation Record

- asset_id: `OWNER_WORK_WINTER_01_WORN_FRONT`
- outfit_id: `OWNER_WORK_WINTER_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- candidate_version: `v007`
- status: `APPROVED_BY_USER`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/approved/worn_front/OWNER_WORK_WINTER_01_WORN_FRONT_APPROVED.png`
- original_candidate_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/candidates/v007_worn_front/OWNER_WORK_WINTER_01_WORN_FRONT_v007.png`
- output_sha256: `cb7baf4a373b4c91618bd5286eae898ca17506f9ce337f534c85cd4e46809a1e`
- reference_budget: `5 inputs; source-derived face set + BODY_01 face-excluded body reference + active approved outfit design + hosiery material reference`

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png
    responsibility: [owner face identity and facial-feature relationships]
    must_not_define: [hair, body, clothing, lighting, background]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    responsibility: [Hairstyle-A presentation]
    must_not_define: [face, body, clothing, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: [strict BODY_01 body proportions and overall scale]
    must_not_define: [face, facial features, hair, clothing, hosiery material, lighting, background]
  - asset_id: OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED_v003
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/approved/design_reference/OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED.png
    responsibility: [approved outfit design]
    must_not_define: [owner identity, face, body, skin, hair, hosiery material, background]
  - asset_id: HOSIERY_30D_NUDE_SOFT_SHEEN_MATERIAL_001
    path: materials/hosiery/source_library/raw/30d_nude_soft_sheen/IMG_2682.jpg
    responsibility: [central soft highlight band, darker lateral edges, hosiery finish]
    must_not_define: [owner identity, face, body, hair, outfit, boots, pose, background]
```

## QA comparison only

```yaml
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope: [identity drift, face contamination, facial projection]
```

## Reference isolation

- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- body_reference_used: [OWNER_BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2]
- material_reference_used: [HOSIERY_30D_NUDE_SOFT_SHEEN_MATERIAL_001]
- downstream_identity_lineage_allowed: `false`

## Prompt assembly

```text
Create one photorealistic vertical 3:4 front-facing full-outfit fit-validation image of the adult owner standing neutrally in a light-gray studio. Generate the face only from source-derived Face method inputs and use Hairstyle-A. Make the head and face slightly larger than v006, with a natural approximately 6.5 to 6.9 head-height proportion; never undersized or fashion-model elongated. Keep the face identity and features unchanged. Use BODY_01 as strict authority for all neck-below-body proportions: preserve its shoulder width, compact torso, waist-to-hip relationship, fuller upper thighs, proportionate calves, leg length and overall scale. Do not elongate, slim or reshape the body.

Preserve the approved winter office outfit exactly: slightly deeper gray wool short coat still lighter than the dark-gray wool short skirt, oversized lapel, minimal clean closure with no two large buttons, brown scarf, dark-gray short skirt, deep black-brown felt straight-shaft boots with parallel sides, uncinched ankles, just below knee, approximately 5 cm wedge heel.

The hosiery must be visibly thicker than v006, with increased textile opacity and a stronger soft skin-blurring effect: smooth the visibility of pores, veins and small skin details while retaining realistic leg form and subtle transparency. Keep the hosiery light nude and textile-like, not opaque tights. Preserve the exact material light structure from IMG_2682.jpg: one broad, diffuse vertical highlight band centered on the front of each leg, brightest across the middle, smoothly fading laterally, with noticeably darker outer side edges and a darker narrow edge contour. The band is a wide tonal gradient, never a thin line. Maintain the current successful banded highlight while increasing coverage and skin softening. No glitter, scattered sparkle, oily gloss, wet shine, or multiple linear streaks.

Eye-level centered front view, full body head to floor, neutral catalog lighting. Keep all clothing, boots, pose and background unchanged; only adjust head scale and hosiery thickness, skin-softening coverage, and darker lateral edge falloff.
```

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- fit_validation_status: `REVIEW_REQUIRED`
- head_to_body_ratio_check: `PASS_WITH_USER_REVIEW`
- body_proportion_check: `REVIEW_REQUIRED`
- hosiery_thickness_and_skin_softening_check: `PASS_WITH_USER_REVIEW`
- hosiery_band_and_edge_falloff_check: `PASS_WITH_USER_REVIEW`
- face_contamination_check: `REVIEW_REQUIRED`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `APPROVED_BY_USER`

## Approval record

- approved_by_user: `yes`
- approval_statement: `批准`
- approval_date: `2026-09-17`
- approved_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/approved/worn_front/OWNER_WORK_WINTER_01_WORN_FRONT_APPROVED.png`
- candidate_raster_moved_to_approved_path: `yes`
- promotion_scope: `approved worn fit-validation view only; not Character Canon, not video keyframe, not identity lineage`
