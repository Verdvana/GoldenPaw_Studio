# Outfit Generation Record

- asset_id: `OWNER_WORK_WINTER_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_WORK_WINTER_01`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- head_policy: `not_applicable`
- candidate_version: `v001`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/candidates/v001_design_reference/OWNER_WORK_WINTER_01_DESIGN_REFERENCE_v001.png`
- output_sha256: `19f62fa433d65bdbee983e95e18414c0cba6435915551dffc23aa0149266221e`
- reference_budget: `text-only; no supplied garment reference images`

## Generation inputs

```yaml
generation_inputs: []
```

## QA comparison only

```yaml
qa_comparison_only: []
```

## Reference isolation

- garment_references_used: none
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

```text
Use case: product-mockup
Asset type: clean clothing-only L2 winter officewear design reference plate.
Primary request: Create exactly one photorealistic vertical 3:4 apparel design board with no person, no mannequin, no head, no face, no torso, no hands, and no worn upper-body image. Present one coordinated winter office outfit as clean product views: a light-gray wool short coat with an oversized notched lapel and tailored short length; a dark-gray wool short skirt with a neat structured hem; a brown soft winter scarf shown as a separate folded accessory; a light-skin 60D pantyhose textile swatch; and brown felt straight-shaft boots, ending below the knee, with an approximately 5 cm wedge heel and closed toes.
Scene/backdrop: seamless pale neutral-gray studio product board with soft even catalog lighting.
Subject: garments and accessories only, arranged with ample spacing and consistent scale; no body or upper-body silhouette.
Style/medium: photorealistic premium apparel catalog photography, accurate fabric texture.
Composition/framing: vertical 3:4; coat and skirt as front garment views, scarf separate, hosiery as a small material swatch, pair of boots in a separate three-quarter footwear view; clean alignment and margins, no labels.
Lighting/mood: soft neutral winter daylight-balanced studio light, low contrast.
Color palette: light gray, dark gray, medium warm brown, light skin-tone hosiery, brown felt footwear.
Materials/textures: visible wool nap and tailored seams; soft woven scarf; realistic 60D fine textile with softly matte surface and medium transparency; felt boot shaft with natural fibers; structured wedge sole approximately 5 cm.
Constraints: clothing-only design authority for garment silhouette, color, layering, hosiery material appearance, and footwear construction; no owner identity or body information.
Avoid: person, model, mannequin, upper-body image, head, face, skin body, hair, jewelry, hands, feet inside hosiery, glossy hosiery, latex, PVC, plastic, rubber, wet/liquid/body-paint appearance, bare toes, toe-cap line, ankle discontinuity, knee-high or over-the-knee boots, stiletto or block heel, heel over 5 cm, brand logo, readable text, watermark, collage clutter.
```

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `UNREVIEWED`
- visual_status: `PASS_WITH_USER_REVIEW`
- garment_reference_isolation_check: `PASS`
- face_contamination_check: `NOT_APPLICABLE`
- hosiery_material_check: `REVIEW_REQUIRED`
- footwear_height_and_heel_check: `REVIEW_REQUIRED`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `PENDING_USER_REVIEW`
