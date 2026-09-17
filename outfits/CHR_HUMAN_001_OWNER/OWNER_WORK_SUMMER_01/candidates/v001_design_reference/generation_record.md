# Outfit Generation Record

- asset_id: `OWNER_WORK_SUMMER_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_WORK_SUMMER_01`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- head_policy: `not_applicable`
- candidate_version: `v001`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/candidates/v001_design_reference/OWNER_WORK_SUMMER_01_DESIGN_REFERENCE_v001.png`
- output_sha256: `95300662f092faba2f8c84bb3c23ab661306026a95d392fee1366f9cb12ba9bb`
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

Use case: `product-mockup`.

Asset type: clean clothing-only design reference plate for a reusable L2 summer
office outfit. Create a single coordinated outfit presentation with no person,
mannequin, head, face, body, hands, or feet: a black ultra-low-neckline fitted
short-sleeve top; a fitted white skirt with a restrained champagne undertone,
dense small black polka dots, and a hem ending at mid-thigh; gray 15D matte sheer
closed-toe pantyhose as a separate textile swatch; and refined black approximately
5 cm pointed-toe pumps with a square metal buckle detail. The shoe must have no
brand logo or readable text.

Scene/backdrop: seamless light neutral gray studio product board, soft even neutral
catalog lighting.

Composition/framing: vertical 3:4 consistent apparel design plate; show the top,
skirt front and rear construction as aligned garment views if useful, the hosiery
as a small material swatch, and the two shoes as a separate footwear view. Keep
consistent scale, ample margin, clean spacing, no collage clutter, no labels.

Materials/textures: black fitted short-sleeve top with smooth matte apparel fabric;
white skirt with a subtle champagne warmth and small dense crisp black polka dots;
gray 15D sheer matte hosiery with fine textile appearance and no shine; black shoe
with refined smooth finish, pointed toe, square buckle, and stable approximately
5 cm heel.

Constraints: define only garment silhouette, color, pattern, hosiery finish,
footwear construction, and outfit coordination. No person or identity information.

Avoid: model, mannequin, face, body, skin, hair, jewelry, pose, lighting drama,
background scene, brand logo, readable text, watermark, unrelated garments, glossy
hosiery, opaque tights, latex, PVC, plastic, rubber, or exaggerated anatomy.

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `UNREVIEWED`
- visual_status: `PASS_WITH_USER_REVIEW`
- garment_reference_isolation_check: `PASS`
- face_contamination_check: `NOT_APPLICABLE`
- decision: `PENDING_USER_REVIEW`
