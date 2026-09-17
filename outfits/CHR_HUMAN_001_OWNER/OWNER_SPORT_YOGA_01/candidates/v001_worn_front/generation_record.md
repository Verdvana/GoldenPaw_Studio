# Outfit Generation Record

- asset_id: `OWNER_SPORT_YOGA_01_WORN_FRONT`
- outfit_id: `OWNER_SPORT_YOGA_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v001`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/candidates/v001_worn_front/OWNER_SPORT_YOGA_01_WORN_FRONT_v001.png`
- reference_budget: `4 generation inputs; no unapproved outfit raster used`

## Validation target

- fit_or_design_question: Verify front fit of the light-pink open-back yoga tank, warm apricot-pink yoga pants, no-footwear contract, and flesh-tone pearlescent 15D hosiery while retaining the complete owner head and face.
- acceptance_checks: [L0 Face method followed, Hairstyle A only, top fit readable, pants color and opacity readable, pearlescent hosiery visible, continuous toe coverage, no shoes]

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png
    responsibility: source-derived face identity, facial relationships, natural skin tone and texture
    must_not_define: [hair, crown, body, clothing, hosiery, lighting, background]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    responsibility: Hairstyle A only
    must_not_define: [face, identity, skin, body, clothing, hosiery, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: neck-below body proportions, limb lengths, foot scale, neutral stance
    must_not_define: [face, identity, hair, clothing, hosiery design, footwear, lighting, background]
  - asset_id: OWNER_SPORT_YOGA_01_TEXT_CONTRACT
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/OUTFIT.md
    responsibility: light-pink open-back tank, warm apricot-pink matte pants, pearlescent 15D hosiery, no footwear
    must_not_define: [owner face, identity, body, skin, hair, pose, lighting, background]
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
- unapproved_outfit_raster_used_as_generation_input: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

Use case: `product-mockup`. Create a modest professional sportswear catalog fitting
reference of the same adult owner with complete head, face, Hairstyle A, neck,
shoulders, torso, legs and feet visible in a neutral front standing pose. The image
is an L2 clothing-fit validation asset, not a video keyframe or identity Canon.
Generate the face only from the source-derived Face method and L0 inputs; do not use
any AI Face Canon pixels.

Dress her in a light-pink strappy yoga tank top with a clearly open back and
restrained athletic strap construction. Add full-length smooth opaque matte yoga
pants in pink with a warm apricot undertone, ending just above the ankles. Add
continuous flesh-tone nude 15D sheer pantyhose from waist through ankles, feet and
toes, with subtle pearlescent textile highlights and visible but natural fabric
tension over the toes. No shoes or other footwear.

Use a seamless light neutral gray studio, soft even catalog lighting, centered
vertical 3:4 full-body framing, normal catalog scale. Preserve natural face
relationships, warm-neutral skin and Hairstyle A: long straight loose dark-brown
hair, near-center part, low crown and tapered ends. Keep pants opaque and matte;
keep hosiery separate, sheer and pearlescent, never plastic or wet-looking. No face
blotches, patches, smudges, muddy relighting, beautification, body reshaping or
iterative-generation artifacts.

Avoid hairstyle B, face drift, previous candidates, unapproved outfit images, shoes,
bare legs, bare toes, exposed toenails, opaque hosiery, glossy/oily hosiery, latex,
PVC, plastic, rubber, liquid surfaces, extra garments, text, logo, watermark,
collage, or background scene.

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
- generation_attempt_note: `The head-present Owner worn-front generation followed L0 + Face method and excluded L1 Face from inputs, but output moderation rejected the request; no worn-front raster was produced.`
