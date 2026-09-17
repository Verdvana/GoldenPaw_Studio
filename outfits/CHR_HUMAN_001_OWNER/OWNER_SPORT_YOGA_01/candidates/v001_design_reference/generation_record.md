# Outfit Generation Record

- asset_id: `OWNER_SPORT_YOGA_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_SPORT_YOGA_01`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- head_policy: `not_applicable`
- candidate_version: `v001`
- status: `REJECTED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/candidates/v001_design_reference/OWNER_SPORT_YOGA_01_DESIGN_REFERENCE_v001.png`
- reference_budget: `text-only; no supplied garment reference images`

## Generation inputs

```yaml
generation_inputs: []
qa_comparison_only: []
```

## Reference isolation

- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

Use case: `product-mockup`. Create a clean clothing-only design reference plate for
a reusable L2 yoga outfit, with no person, mannequin, head, face, body, hands, or
feet. Show a light-pink strappy open-back yoga tank top with a clear restrained
open-back construction; full-length smooth opaque matte yoga pants in pink with a
warm apricot undertone; a separate flesh-tone nude 15D sheer hosiery material swatch
with a restrained pearlescent sheen; and no footwear. The hosiery is a continuous
closed-toe pantyhose textile contract, shown only as a material swatch.

Scene/backdrop: seamless light neutral gray studio product board, soft even neutral
catalog lighting.

Composition/framing: vertical 3:4 standardized clothing design plate; show front and
rear tank-top views aligned at consistent scale, the pants as front and rear views,
the hosiery swatch separately, and no shoes. Ample margin, clean spacing, no labels
or text.

Materials/textures: light-pink performance fabric top; smooth opaque matte pink
yoga pants with a warm apricot cast and minimal construction; fine flesh-tone 15D
sheer hosiery with soft pearl-like textile highlights, never wet or plastic.

Constraints: define only garment silhouette, open-back strap construction, color,
hosiery finish, and outfit coordination. No person or identity information.

Avoid: person, model, mannequin, face, body, skin, hair, hands, feet, shoes,
dramatic lighting, glossy/oily hosiery, opaque tights, latex, PVC, plastic, rubber,
text, logo, watermark, unrelated garments, or collage clutter.

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `UNREVIEWED`
- visual_status: `UNREVIEWED`
- garment_reference_isolation_check: `PASS`
- face_contamination_check: `NOT_APPLICABLE`
- decision: `REJECTED — transparent/black background and pants color not sufficiently warm apricot-pink`
