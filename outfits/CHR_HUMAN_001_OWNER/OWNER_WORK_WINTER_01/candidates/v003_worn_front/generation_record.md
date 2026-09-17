# Outfit Generation Record

- asset_id: `OWNER_WORK_WINTER_01_WORN_FRONT`
- outfit_id: `OWNER_WORK_WINTER_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v003`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/candidates/v003_worn_front/OWNER_WORK_WINTER_01_WORN_FRONT_v003.png`
- output_sha256: `d3def27b48d5fa3437d26dc5f5daee108a2187dda8058aba95de64226add17cc`
- reference_budget: `5 inputs; source-derived face set + face-excluded body derivative + active approved outfit design + hosiery material reference`

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png
    responsibility: [owner face identity, facial-feature relationships, warm-neutral skin texture and tone]
    must_not_define: [hair, body, clothing, lighting, background]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    responsibility: [Hairstyle-A front presentation, long straight dark-brown hair, near-center part]
    must_not_define: [face, body, clothing, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: [face-excluded owner body proportions, front standing articulation, limb and foot geometry]
    must_not_define: [face, facial features, hair, clothing design, hosiery material, lighting, background]
  - asset_id: OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED_v003
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/approved/design_reference/OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED.png
    responsibility: [active approved outfit silhouette, colors, minimal coat closure, scarf, skirt, straight boot shaft and black-brown color]
    must_not_define: [owner identity, face, body, skin, hair, pose, lighting, hosiery material, background]
  - asset_id: HOSIERY_30D_NUDE_SOFT_SHEEN_MATERIAL_001
    path: materials/hosiery/source_library/raw/30d_nude_soft_sheen/IMG_2682.jpg
    responsibility: [soft nude hosiery finish, fine even translucency, gentle diffuse sheen]
    must_not_define: [owner identity, face, body, hair, outfit design, boot design, pose, background]
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
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

```text
Create one photorealistic vertical 3:4 front-facing full-outfit fit-validation image of the same adult owner standing neutrally in a simple light-gray studio. Generate the face only from the source-derived Face method inputs, with Hairstyle-A long straight dark-brown hair. Preserve the active approved winter office outfit exactly: slightly deeper gray wool short coat that remains lighter than the dark-gray wool short skirt, oversized lapel, minimal clean closure with no two large buttons, brown scarf, dark-gray short skirt, and deep black-brown felt straight-shaft boots with parallel sides, no ankle cinching, ending just below the knee, approximately 5 cm wedge heel.

Change only the hosiery material from the prior validation: use light nude 30D-style hosiery based on IMG_2682.jpg, with fine even translucency and a gentle diffuse soft sheen across the textile. It should be subtly transparent and skin-like, with smooth uniform woven finish and restrained soft light—not glitter, not scattered star-like sparkles, not glossy oil, not wet shine, and no long straight or linear specular highlights. Preserve continuous hosiery coverage from thighs through feet under the closed-toe boots.

Soft diffuse neutral catalog lighting, realistic wool and felt texture, no props, no logos, no text, no watermark. Do not change the face, body proportions, hair, coat, scarf, skirt, boot color, boot height, boot shaft shape, or heel.
```

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- fit_validation_status: `REVIEW_REQUIRED`
- face_contamination_check: `REVIEW_REQUIRED`
- face_generation_method_followed: `true`
- hosiery_material_check: `PASS_WITH_USER_REVIEW`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `PENDING_USER_REVIEW`
