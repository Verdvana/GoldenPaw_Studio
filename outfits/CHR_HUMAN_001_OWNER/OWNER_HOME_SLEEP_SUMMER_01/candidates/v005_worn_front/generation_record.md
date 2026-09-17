# Outfit Generation Record

- asset_id: `OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT`
- outfit_id: `OWNER_HOME_SLEEP_SUMMER_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v005`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_HOME_SLEEP_SUMMER_01/candidates/v005_worn_front/OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT_v005.png`

## Validation target

- fit_or_design_question: Verify front fit, hem length, satin drape, 15D glossy hosiery, toe-area textile tension, footwear relationship, and head/neck/shoulder relationship with a complete owner head present.
- acceptance_checks: [face follows L0 Face method without iterative contamination, Hairstyle A only, dress fit readable, glossy hosiery visible, hosiery tension visible over toes, open-toe slides correctly layered]

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png
    responsibility: source-derived face identity, facial relationships, natural skin tone and texture
    must_not_define: [hair, crown, body, clothing, hosiery, footwear, lighting, background]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    responsibility: Hairstyle A only
    must_not_define: [face, identity, skin, body, clothing, hosiery, footwear, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: neck-below body proportions, limb lengths, feet scale, neutral stance
    must_not_define: [face, identity, hair, clothing, hosiery design, footwear design, lighting, background]
  - asset_id: OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE
    path: approved/design_reference/OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE.png
    responsibility: floral satin dress, pale-pink feather slides, outfit-level glossy hosiery contract
    must_not_define: [owner face, identity, skin, body, hair, pose, lighting, background]
```

## QA comparison only

```yaml
qa_comparison_only:
  - asset_id: OWNER_FACE_FRONT_NEUTRAL_CANON_L1
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope: [identity drift, facial-feature relationships, skin contamination, projection, framing]
```

The AI Face Canon above is not a generation input.

## Reference isolation

- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- ai_face_canon_used_as_generation_input: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

Use case: `product-mockup`. Create a modest professional apparel-catalog fitting
reference of the same adult owner, with a complete head, face, Hairstyle A, neck,
shoulders, torso, legs and feet visible in a neutral front standing pose. This is
strictly an L2 clothing-fit validation image, not a video keyframe and not a new
identity Canon. Generate the visible face from the source-derived Face method and
its L0 inputs; do not use any AI Face Canon pixels.

Dress her in the approved warm-ivory floral satin short camisole sleep dress with
soft cowl neckline, fine double shoulder straps, natural satin drape and gently
flared hem. Add pale-pink feather-trimmed open-toe flat slides. Add continuous nude
15D sheer pantyhose from waist through ankles, insteps, heels and toes, with a clear
but restrained glossy oil-sheen textile response and visible fine fabric tension over
the toe contours beneath the open-toe slides. The toe area must be textile-covered,
not bare skin and not exposed toenails.

Use a seamless light neutral gray studio, soft even catalog lighting, centered
vertical 3:4 full-body framing, normal catalog scale, and no dramatic styling. Keep
the face natural and clean: no blotches, patches, smudges, muddy relighting,
beautification, altered age, facial redesign, or iterative-generation artifacts.
Preserve Hairstyle A: long straight loose dark-brown hair, near-center part, low
crown and tapered ends. Use the Body derivative only for neck-below proportions and
stance. Use the outfit design reference only for clothing and footwear.

Avoid face drift, hairstyle B, body reshaping, bare legs, bare toes, exposed
toenails, opaque or matte hosiery, toe-cap seams, closed-toe shoes, latex, PVC,
plastic, rubber, liquid surfaces, extra garments, text, logo, watermark, collage,
or any prior candidate pixels.

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `UNREVIEWED`
- fit_validation_status: `UNREVIEWED`
- face_contamination_check: `UNREVIEWED`
- face_generation_method_followed: `true`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `PENDING_REVIEW`
- generation_attempt_result: `BLOCKED_BY_IMAGEGEN_SAFETY_SYSTEM`
- generation_attempt_note: `The head-present Owner worn-front generation followed L0 + Face method and excluded L1 Face from inputs, but output moderation rejected the request; no v005 raster was produced.`
