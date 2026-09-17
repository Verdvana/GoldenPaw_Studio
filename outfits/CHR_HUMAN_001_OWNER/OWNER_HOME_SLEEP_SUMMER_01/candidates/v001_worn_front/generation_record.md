# Outfit Generation Record

- asset_id: `OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT`
- outfit_id: `OWNER_HOME_SLEEP_SUMMER_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- candidate_version: `v001`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_HOME_SLEEP_SUMMER_01/candidates/v001_worn_front/OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT_v001.png`
- output_sha256: `6c4c4e0cd3d3d8d1c17051d3180278bb7f04bf53f16bc9b8b2410e706f08d8d7`

## Validation target

- fit_or_design_question: Verify front fit, hem length, relaxed drape, continuous 15D glossy hosiery, and relationship between hosiery-covered toes and open-toe feather slides.
- face_visibility: `none`
- acceptance_checks:
  - shoulder straps and cowl neckline sit naturally
  - dress length and short flared hem are readable
  - satin dress remains distinct from skin and hosiery
  - hosiery is continuous from waist through toes with controlled glossy textile highlights
  - open-toe slippers leave the toe area open

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE
    path: approved/design_reference/OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE.png
    responsibility: approved outfit garment, footwear, and glossy hosiery design contract
    must_not_define: [face, identity, skin, body, hair, pose, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_FACE_EXCLUDED_DERIVATIVE
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v1/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: neck-below body proportions, limb lengths, feet scale, and neutral front stance only
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

Use case: `product-mockup`

Asset type: neutral L2 worn-front apparel fit-validation plate, not a video keyframe
and not an identity reference.

Primary request: Create one neutral front-view technical apparel fit-validation image
from the neck down to the feet, showing one adult woman's body without a visible
face or identifiable head. Dress her in the approved warm-ivory floral satin short
camisole sleep dress with softly draped cowl neckline, fine double shoulder straps,
crossed-back construction implied only where visible from the front, and short gently
flared hem. Add continuous nude 15D sheer pantyhose with a controlled glossy/oil-sheen
textile finish from waist through every toe, and pale-pink feather-trimmed open-toe
flat slide slippers.

Scene/backdrop: seamless light neutral gray studio background, soft even technical
catalog light.

Subject: neck-down apparel fit validation only; natural neutral standing stance;
no visible face, head, hair, jewelry, or identity cues.

Composition/framing: vertical 3:4 full-body crop from lower neck/shoulders through
feet, front view, centered, enough margin to see the entire hem and both shoes.

Materials/textures: warm-ivory satin with small pink/peach floral print and natural
soft drape; sheer 15D nude hosiery with fine textile presence and restrained oily
highlights only on the hosiery; pale-pink soft feather trim on open-toe slides.

Constraints: use the approved design reference only for declared outfit properties.
Use the face-excluded body derivative only for neck-below proportions, limb lengths,
feet scale, and stance. No face-generation input is permitted or needed.

Avoid: face, head, hair, model identity, beauty retouching, body reshaping, opaque
tights, matte hosiery, bare legs, naked toes, closed-toe shoes, toe-cap seams,
latex, PVC, plastic, rubber, liquid surface, wrong dress color, unrelated garments,
text, logo, watermark, or prior candidate pixels.

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `PASS`
- fit_validation_status: `FAIL`
- face_contamination_check: `NOT_APPLICABLE`
- face_generation_method_followed: `not_applicable`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `REJECTED — toe region does not clearly demonstrate continuous hosiery coverage`
