# Outfit Generation Record

- asset_id: `OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_HOME_SLEEP_SUMMER_01`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- candidate_version: `v001`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_HOME_SLEEP_SUMMER_01/candidates/v001_design_reference/OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE_v001.png`
- output_sha256: `19450c6fd2372b012f06d973b73b1f2ffee03ea41ce9b03ed9ecd2118962b4b5`
- original_candidate_path: `candidates/v001_design_reference/OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE_v001.png`
- promoted_asset_path: `approved/design_reference/OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE.png`
- promoted_asset_sha256: `19450c6fd2372b012f06d973b73b1f2ffee03ea41ce9b03ed9ecd2118962b4b5`

## Reference budget

- input_reference_count: `3`
- references_used: `REF_001`, `REF_002`, `REF_003`
- reference_set_scope: garment and footwear design only

## Generation inputs

```yaml
generation_inputs:
  - asset_id: REF_001
    path: reference_inputs/garment_references/clothes_front.jpg
    responsibility: front garment silhouette, cowl neckline, straps, floral satin and hem drape
    must_not_define: [model identity, face, body, skin, hair, pose, lighting, background]
  - asset_id: REF_002
    path: reference_inputs/garment_references/clothes_back.jpg
    responsibility: crossed open-back straps, rear neckline, rear drape and hem fall
    must_not_define: [model identity, face, body, skin, hair, pose, lighting, background]
  - asset_id: REF_003
    path: reference_inputs/garment_references/shoes.jpg
    responsibility: pale-pink feather-trimmed open-toe flat slide design
    must_not_define: [model identity, face, body, skin, hair, feet anatomy, pose, lighting, background]
```

## QA comparison only

```yaml
qa_comparison_only: []
```

## Prompt assembly

Use case: `product-mockup`

Asset type: clean clothing design reference plate for a reusable L2 outfit package.

Primary request: Create one neutral, consistent apparel-design presentation of a
single warm-ivory floral satin camisole-strap short sleep dress, showing the garment
front and back as two matching full-length garment views side by side, plus the
matching pale-pink feather-trimmed open-toe flat slide slippers as a separate small
footwear view. Include a small unobtrusive visual swatch of 15D nude sheer hosiery
with a controlled glossy/oil-sheen textile finish to document the complete outfit
contract, without showing a person.

Scene/backdrop: seamless light neutral gray studio background, no room or lifestyle
setting.

Subject: garments and footwear only; no mannequin, model, body, face, hands or feet.

Style/medium: clean realistic apparel catalog/product reference, consistent neutral
presentation, physically plausible satin and feather texture.

Composition/framing: vertical 3:4 design plate, front and back dress views aligned
to the same scale and baseline, footwear separated below or beside the dress views,
ample margin, no collage clutter, no labels or text.

Materials/textures: warm-ivory satin with small delicate pink/peach floral print,
soft cowl neckline, fine double shoulder straps, crossed open-back straps, short
gently flared hem, natural satin drape; pale-pink fluffy feather trim on flat
open-toe slides; sheer nude 15D hosiery swatch with subtle controlled oily gloss.

Constraints: use the three supplied images only for their declared garment and
footwear responsibilities. Preserve the garment's front/back construction and the
shoe's feather-trimmed open-toe design. No person or identity information.

Avoid: model, face, body, skin, hair, hands, feet, mannequin, jewelry, makeup,
room background, dramatic colored lighting, unrelated garments, opaque tights,
matte hosiery, latex, PVC, plastic, rubber, liquid skin, text, logo, watermark,
garbled labels, or extra footwear.

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
