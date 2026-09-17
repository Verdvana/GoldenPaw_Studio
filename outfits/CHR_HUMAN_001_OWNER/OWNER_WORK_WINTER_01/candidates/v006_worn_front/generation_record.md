# Outfit Generation Record

- asset_id: `OWNER_WORK_WINTER_01_WORN_FRONT`
- outfit_id: `OWNER_WORK_WINTER_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- candidate_version: `v006`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/candidates/v006_worn_front/OWNER_WORK_WINTER_01_WORN_FRONT_v006.png`
- output_sha256: `f658e58575c9f47873a22d96259c9c9c1ba4088268bccc5730d0f50ad0958b33`
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
    responsibility: [broad central hosiery highlight band and darker lateral edges]
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
Create one photorealistic vertical 3:4 front-facing full-outfit fit-validation image of the adult owner standing neutrally in a light-gray studio. Generate the face only from source-derived Face method inputs and use Hairstyle-A. Correct the head-to-body ratio: make the head and face visibly larger relative to the full figure, with a natural approximately 6.8 to 7.2 head-height proportion, not a small head or fashion-model 8-head silhouette. Keep the face identity and facial features unchanged. Use BODY_01 as strict authority for neck-below-body proportions: preserve its shoulder width, compact torso, waist-to-hip relationship, fuller upper thighs, proportionate calves, leg length and overall scale. Do not elongate the body or legs, and do not slim the hips or thighs.

Preserve the approved winter office outfit exactly: slightly deeper gray wool short coat still lighter than the dark-gray wool short skirt, oversized lapel, minimal clean closure with no two large buttons, brown scarf, dark-gray short skirt, deep black-brown felt straight-shaft boots with parallel sides, uncinched ankles, just below knee, approximately 5 cm wedge heel.

The hosiery material is mandatory and must be visibly present: use the exact visual behavior of IMG_2682.jpg—light nude 30D-style, subtly transparent, with one broad, clearly readable vertical central highlight band on the front of each leg. The band is brightest in its wide center, smoothly fades in brightness toward both sides, and becomes visibly darker at the lateral edges. This is a broad tonal gradient across the hosiery, not a thin stripe. Maintain this band from upper thigh through the visible calf above the boots. Soft textile finish, no glitter, no scattered sparkles, no uniform flat matte, no oily gloss, no wet shine, no multiple linear streaks.

Eye-level centered front view, full body head to floor, neutral catalog lighting. Keep all clothing, boots, pose and background unchanged; only correct the head scale and restore the hosiery central highlight-band gradient.
```

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- fit_validation_status: `REVIEW_REQUIRED`
- head_to_body_ratio_check: `PASS_WITH_USER_REVIEW`
- body_proportion_check: `PASS_WITH_USER_REVIEW`
- hosiery_material_check: `PASS_WITH_USER_REVIEW`
- face_contamination_check: `REVIEW_REQUIRED`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `PENDING_USER_REVIEW`
