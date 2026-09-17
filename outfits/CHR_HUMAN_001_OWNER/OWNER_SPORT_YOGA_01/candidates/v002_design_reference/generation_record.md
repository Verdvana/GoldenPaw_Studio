# Outfit Generation Record

- asset_id: `OWNER_SPORT_YOGA_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_SPORT_YOGA_01`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- head_policy: `not_applicable`
- candidate_version: `v002`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/candidates/v002_design_reference/OWNER_SPORT_YOGA_01_DESIGN_REFERENCE_v002.png`
- output_sha256: `d81553a69475fe7a7c7aec0d7d372e47f9a7a2e0175d80357316635f2b6c3523`
- original_candidate_path: `candidates/v002_design_reference/OWNER_SPORT_YOGA_01_DESIGN_REFERENCE_v002.png`
- promoted_asset_path: `approved/design_reference/OWNER_SPORT_YOGA_01_DESIGN_REFERENCE.png`
- promoted_asset_sha256: `d81553a69475fe7a7c7aec0d7d372e47f9a7a2e0175d80357316635f2b6c3523`
- reference_budget: `text-only; v001 pixels not used`

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

Use case: `product-mockup`. Create a clean opaque-background clothing-only design
reference plate for a reusable L2 yoga outfit. No person, mannequin, head, face,
body, hands, feet, or shoes. Show front and rear views of a light-pink strappy
open-back yoga tank top; front and rear views of full-length smooth opaque matte yoga
pants in a clearly warm pink-apricot color; and a separate flesh-tone nude 15D sheer
hosiery swatch with restrained pearlescent textile sheen. No footwear.

Use an opaque, solid light neutral gray studio background, not transparency and not
black. Use vertical 3:4 standardized product-board composition, consistent scale,
clean spacing, ample margin, and no labels or text. Keep the rear tank-top view
clearly open-backed with simple restrained straps. Keep pants clearly opaque, matte,
full length to just above the ankle, and distinct from hosiery. Keep hosiery only as
a small separate material swatch; it is flesh-tone, 15D, sheer and pearlescent,
never wet, oily, plastic or rubber.

Define only clothing silhouette, open-back strap construction, colors, hosiery
finish, and outfit coordination. Avoid any person or identity information, shoes,
transparent background, black background, glossy/oily hosiery, opaque hosiery,
latex, PVC, plastic, rubber, text, logo, watermark, or collage clutter.

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `UNREVIEWED`
- visual_status: `PASS_WITH_USER_REVIEW`
- garment_reference_isolation_check: `PASS`
- face_contamination_check: `NOT_APPLICABLE`
- decision: `APPROVED_AND_PROMOTED`
- approved_by: `user`
- approved_at: `2026-09-17`
