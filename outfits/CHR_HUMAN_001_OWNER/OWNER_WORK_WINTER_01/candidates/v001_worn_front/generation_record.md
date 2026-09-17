# Outfit Generation Record

- asset_id: `OWNER_WORK_WINTER_01_WORN_FRONT`
- outfit_id: `OWNER_WORK_WINTER_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v001`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/candidates/v001_worn_front/OWNER_WORK_WINTER_01_WORN_FRONT_v001.png`
- output_sha256: `054c5911ff43bb12668f15b585ee6aedb302ab2adc0fcffcbcdee428f2daeb17`
- reference_budget: `4 inputs; face-safe source-derived face set + face-excluded body derivative + approved outfit design`

## Validation target

- fit_or_design_question: `Validate the approved winter office outfit worn frontally on the owner, including coat lapel/shoulder fit, scarf placement, skirt length, hosiery appearance, boot shaft height, and wedge heel.`
- acceptance_checks:
  - `head-present front view with owner face generated only from source-derived Face method inputs`
  - `no AI Face Canon, AI Body Canon, previous outfit, or previous shot used as generation input`
  - `light-gray oversized lapel coat, dark-gray short skirt, brown scarf preserved`
  - `light-skin 60D subtly transparent pearl hosiery; delicate woven sparkle, not oil gloss`
  - `brown felt boots end just below the knee; approximately 5 cm wedge heel`
  - `no upper-body occlusion that prevents coat/scarf fit review`

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
  - asset_id: OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/approved/design_reference/OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED.png
    responsibility: [approved outfit garment silhouette, colors, layering, pearl hosiery appearance, boot construction]
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

- garment_references_used: [OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED]
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

```text
Use case: identity-preserve
Asset type: L2 worn_front fit-validation image for an approved winter office outfit.
Input images: Image 1 source-derived face/skin authority only; Image 2 face-masked Hairstyle-A authority only; Image 3 face-excluded body authority only; Image 4 approved outfit design authority only.
Primary request: Create one photorealistic vertical 3:4 front-facing full outfit fit-validation image of the same adult owner standing neutrally in a simple studio. Show the head, face, shoulders, coat, skirt, full legs and boots so the entire approved outfit can be evaluated. Generate the owner's face only from the source-derived Face method inputs, with natural warm-neutral skin, neutral closed-mouth expression, direct gaze, and Hairstyle-A long straight dark-brown hair.
Subject: adult owner in the approved winter office outfit: light-gray short wool coat with oversized notched lapel, dark-gray wool short skirt, brown scarf, light-skin 60D subtly transparent pearl-effect hosiery with delicate woven sparkle and no oil shine, brown felt straight-shaft boots ending just below the knee with an approximately 5 cm wedge heel.
Scene/backdrop: seamless neutral light-gray studio, no props.
Style/medium: photorealistic apparel fit photography, natural skin and textile texture.
Composition/framing: eye-level front view, centered full-body head-to-floor, enough room to see coat shoulders and scarf placement, skirt hem, continuous hosiery and both boot shafts/heels.
Lighting/mood: soft neutral catalog lighting; pearlescent hosiery sparkle is fine and restrained, never a broad glossy reflection.
Constraints: outfit image defines clothing only; face-safe source-derived Face method is sole face-generation authority. Preserve owner body proportions from the face-excluded body derivative. Do not use the approved Face Canon as generation input; it is QA-only after generation.
Avoid: face drift, face contamination, generic beautification, body reshaping, Hair-B, mannequin, extra person, glossy/oily hosiery, latex/PVC/plastic/rubber/liquid surface, opaque tights, bare toes, broken hosiery continuity, boots too low, boots over knee, stiletto or block heel, heel over 5 cm, logos, text, watermark.
```

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `UNREVIEWED`
- visual_status: `PASS_WITH_USER_REVIEW`
- fit_validation_status: `REVIEW_REQUIRED`
- face_contamination_check: `REVIEW_REQUIRED`
- face_generation_method_followed: `true`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `PENDING_USER_REVIEW`
