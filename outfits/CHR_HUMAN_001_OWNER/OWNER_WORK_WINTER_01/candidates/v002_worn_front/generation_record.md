# Outfit Generation Record

- asset_id: `OWNER_WORK_WINTER_01_WORN_FRONT`
- outfit_id: `OWNER_WORK_WINTER_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v002`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/candidates/v002_worn_front/OWNER_WORK_WINTER_01_WORN_FRONT_v002.png`
- output_sha256: `f243fc74f44a3936c4a4b24d3909fc0f1dedb2f83fe00b5cac4cb41708da383e`
- reference_budget: `4 inputs; source-derived face set + face-excluded body derivative + active approved outfit design`

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
    responsibility: [active approved outfit silhouette, minimal coat closure, colors, pearl hosiery appearance, straight boot shaft and black-brown color]
    must_not_define: [owner identity, face, body, skin, hair, pose, lighting, background]
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
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

```text
Use case: identity-preserve
Asset type: L2 worn_front fit-validation image for the approved winter office outfit.
Input images: source-derived face/skin authority only; face-masked Hairstyle-A authority only; face-excluded body authority only; active approved outfit design authority only.
Primary request: Create one photorealistic vertical 3:4 front-facing full outfit fit-validation image of the same adult owner standing neutrally in a simple studio. Show head to floor, shoulders, coat, scarf, skirt, legs and boots. Generate the face only from source-derived Face method inputs, with natural warm-neutral skin, neutral closed-mouth expression, direct gaze and Hairstyle-A long straight dark-brown hair.
Subject: active approved winter office outfit: slightly deeper gray wool short coat, still clearly lighter than the dark-gray wool short skirt, oversized lapel, minimal clean closure with no two large buttons; brown scarf; dark-gray short skirt; light-skin 60D hosiery that is visibly thicker than the previous worn image, slightly transparent, with clearly visible fine pearlescent woven sparkle distributed across the fabric. The hosiery must remain softly matte and textile-like, with no long straight or linear oily highlights. Deep black-brown felt straight-shaft boots with parallel sides and no ankle cinching, ending just below the knee, approximately 5 cm wedge heel.
Scene/backdrop: seamless neutral light-gray studio, no props.
Style/medium: photorealistic apparel fit photography, natural skin and textile texture.
Composition/framing: eye-level front view, centered full-body head-to-floor, enough room to inspect coat/scarf, skirt hem, hosiery surface and boot shaft/heel.
Lighting/mood: soft diffuse neutral catalog lighting; pearl sparkle appears as many small soft woven glints, never specular streaks.
Constraints: preserve owner body proportions from the face-excluded body derivative. The outfit design defines clothing only. Do not use the approved Face Canon as generation input; it is QA-only after generation.
Avoid: face drift, generic beautification, body reshaping, Hair-B, mannequin, extra person, glossy/oily hosiery, linear streak highlights, wet shine, latex/PVC/plastic/rubber/liquid surface, opaque tights, bare toes, broken hosiery continuity, buttons, prominent hardware, coat darker than skirt, ankle-tapered boots, gathered shaft, boots too low, boots over knee, stiletto or block heel, heel over 5 cm, logos, text, watermark.
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
