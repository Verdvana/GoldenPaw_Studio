# Outfit Generation Record

- asset_id: `OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT`
- outfit_id: `OWNER_HOME_SLEEP_SUMMER_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- candidate_version: `v002`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_HOME_SLEEP_SUMMER_01/candidates/v002_worn_front/OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT_v002.png`

## Validation target

- fit_or_design_question: Recheck front fit, hem length, relaxed satin drape, and unmistakable continuous 15D glossy hosiery coverage from waist through the toes under the open-toe slides.
- face_visibility: `none`
- acceptance_checks:
  - no visible face or identity
  - dress straps, cowl neckline, fit, and hem are readable
  - hosiery is visibly a continuous sheer textile over ankles, insteps, and toes
  - open-toe slippers sit over the hosiery-covered feet without bare-foot appearance

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE
    path: approved/design_reference/OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE.png
    responsibility: approved garment, footwear, and glossy hosiery design contract
    must_not_define: [face, identity, skin, body, hair, pose, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_FACE_EXCLUDED_DERIVATIVE
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v1/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: neck-below proportions, limb lengths, feet scale, neutral stance
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

Use case: `product-mockup`.

Create one modest professional apparel-catalog fitting reference: a fully clothed
adult apparel model in a neutral front standing position, cropped above the mouth so
no facial identity is visible. Show the complete outfit from the lower neck through
the feet at normal catalog scale. Use the approved warm-ivory floral satin short
camisole sleep dress with softly draped cowl neckline, fine double straps, and gently
flared hem. Add pale-pink feather-trimmed open-toe flat slides. Most importantly,
show one continuous nude 15D sheer hosiery textile from waist through ankles,
instep, heel, and every toe beneath the open-toe slides: the toes must remain visibly
covered by the same fine glossy hosiery, not bare skin. The hosiery has restrained
oil-sheen highlights and plausible textile transparency.

Use a seamless light neutral gray studio background, soft even catalog lighting,
centered vertical 3:4 framing, and no close-up of any body part. Use the approved
design reference only for garment, footwear, and hosiery design; use the face-excluded
body derivative only for neck-below proportions and neutral stance. No face-generation
input is permitted or needed.

Avoid face, head, hair, identity, glamour styling, body reshaping, bare legs, bare
toes, exposed toenails, opaque tights, matte hosiery, toe-cap seam, closed-toe shoes,
latex, PVC, plastic, rubber, liquid surfaces, unrelated garments, text, logo,
watermark, or prior candidate pixels.

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
- generation_attempt_note: `Two neutral apparel-catalog prompts were rejected at output moderation; no v002 raster was produced.`
