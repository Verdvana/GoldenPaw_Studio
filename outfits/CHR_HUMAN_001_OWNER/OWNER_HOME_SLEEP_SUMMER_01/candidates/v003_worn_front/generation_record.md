# Outfit Generation Record

- asset_id: `OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT`
- outfit_id: `OWNER_HOME_SLEEP_SUMMER_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- candidate_version: `v003`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_HOME_SLEEP_SUMMER_01/candidates/v003_worn_front/OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT_v003.png`

## Validation target

- fit_or_design_question: Verify front fit, hem length, relaxed satin drape, glossy 15D hosiery, and visible textile tension across the toes beneath the open-toe slides.
- face_visibility: `none`
- acceptance_checks: [no visible face, dress fit and hem readable, hosiery sheen visible, hosiery visibly continuous over toes, open-toe slides correctly layered]

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE
    path: approved/design_reference/OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE.png
    responsibility: approved dress, footwear, and outfit-level glossy hosiery design
    must_not_define: [face, identity, skin, body, hair, pose, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: neck-below body proportions, limb lengths, foot scale, neutral stance
    must_not_define: [face, identity, hair, clothing, hosiery design, footwear design, lighting, background]
```

## QA comparison only

```yaml
qa_comparison_only: []
```

## Reference isolation

- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

Use case: `product-mockup`. Create one modest professional apparel catalog fitting
reference for an L2 outfit package. Show a fully clothed adult apparel model in a
neutral front standing position, cropped above the mouth so no facial identity is
visible. The purpose is strictly garment construction and fit validation.

Show the complete warm-ivory floral satin short camisole sleep dress: soft cowl
neckline, fine double shoulder straps, natural satin drape, and gently flared hem.
Add pale-pink feather-trimmed open-toe flat slides. The nude 15D sheer hosiery must
be unmistakably a continuous glossy textile from waist through ankles, insteps,
heels, and toes. Show fine woven hosiery tension across each toe and around the
open-toe shoe edge; no bare toe skin or exposed toenails. Keep the feet at normal
full-outfit catalog scale, not a close-up.

Use a seamless light neutral gray background, soft even catalog lighting, centered
vertical 3:4 framing from lower neck through feet. Use Image 1 only for outfit
design. Use Image 2 only for neck-below proportions and stance. No face-generation
input is permitted or needed. No identity, glamour styling, body reshaping, bare
legs, bare toes, opaque tights, matte hosiery, toe-cap seam, closed-toe shoes,
latex, PVC, plastic, rubber, liquid surfaces, text, logo, watermark, or prior
candidate pixels.

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `UNREVIEWED`
- fit_validation_status: `UNREVIEWED`
- face_contamination_check: `NOT_APPLICABLE`
- face_generation_method_followed: `not_applicable`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `PENDING_REVIEW`
- generation_attempt_result: `BLOCKED_BY_IMAGEGEN_SAFETY_SYSTEM`
- generation_attempt_note: `The revised neutral apparel-catalog prompt using the new Body 01 face-excluded derivative was rejected at output moderation; no v003 raster was produced.`
