# Outfit Generation Record

- asset_id: `OWNER_WORK_WINTER_01_WORN_FRONT`
- outfit_id: `OWNER_WORK_WINTER_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v005`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/candidates/v005_worn_front/OWNER_WORK_WINTER_01_WORN_FRONT_v005.png`
- output_sha256: `b0e61b1f53d5e733782ffd51bef80682336eb6cac0803096dd2bce55158b2743`
- reference_budget: `5 inputs; source-derived face set + BODY_01 face-excluded body reference + active approved outfit design + hosiery material reference`

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png
    responsibility: [owner face identity, facial-feature relationships, warm-neutral skin texture and tone]
    must_not_define: [hair, body, clothing, lighting, background]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    responsibility: [Hairstyle-A front presentation]
    must_not_define: [face, body, clothing, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: [strict BODY_01 proportions, waist-to-hip relationship, thigh and calf volume, shoulder width and overall scale]
    must_not_define: [face, facial features, hair, clothing design, hosiery material, lighting, background]
  - asset_id: OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED_v003
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/approved/design_reference/OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED.png
    responsibility: [approved outfit clothing design]
    must_not_define: [owner identity, face, body, skin, hair, pose, lighting, hosiery material, background]
  - asset_id: HOSIERY_30D_NUDE_SOFT_SHEEN_MATERIAL_001
    path: materials/hosiery/source_library/raw/30d_nude_soft_sheen/IMG_2682.jpg
    responsibility: [broad central hosiery highlight band, smooth lateral falloff, darker edges]
    must_not_define: [owner identity, face, body, hair, outfit design, boots, pose, background]
```

## QA comparison only

```yaml
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope: [identity drift, face contamination, facial projection]
```

## Reference isolation

- garment_references_used: [OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED_v003]
- material_references_used: [HOSIERY_30D_NUDE_SOFT_SHEEN_MATERIAL_001]
- body_reference_used: [OWNER_BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2]
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`

## Prompt assembly

```text
Create one photorealistic vertical 3:4 front-facing full-outfit fit-validation image of the adult owner standing neutrally in a light-gray studio. Generate the face only from source-derived Face method inputs and use Hairstyle-A. Strictly match BODY_01 proportions from the face-excluded body reference: natural realistic adult proportions, approximately 7 to 7.5 head-heights overall, head not undersized, normal neck length, compact natural torso, accurate shoulder width, visible waist-to-hip relationship, fuller upper thighs and proportionate calves. Do not elongate the body or legs, do not make a fashion-model 8-head silhouette, do not slim or reshape the hips and thighs.

Preserve the approved winter office outfit exactly: slightly deeper gray wool short coat still lighter than the dark-gray wool short skirt, oversized lapel, minimal closure with no two large buttons, brown scarf, dark-gray short skirt, deep black-brown felt straight-shaft boots, uncinched ankles, just below knee, approximately 5 cm wedge heel.

Keep the hosiery material exactly as the approved v004 direction based on IMG_2682.jpg: light nude 30D-style, subtly transparent, with one broad diffuse vertical highlight band centered on the front of each leg; strongest in the center, smoothly fading toward both sides and visibly darker at the lateral edges. No glitter, no scattered sparkle, no thin linear streak, no oily or wet gloss.

Eye-level centered front view, full body head to floor, neutral catalog lighting, realistic textile texture. Do not change identity, face features, hair, outfit, hosiery material, boots or pose except correcting head-to-body scale and BODY_01 proportions.
```

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- fit_validation_status: `REVIEW_REQUIRED`
- body_proportion_check: `PASS_WITH_USER_REVIEW`
- head_to_body_ratio_check: `PASS_WITH_USER_REVIEW`
- face_contamination_check: `REVIEW_REQUIRED`
- hosiery_material_check: `PASS_WITH_USER_REVIEW`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `PENDING_USER_REVIEW`
