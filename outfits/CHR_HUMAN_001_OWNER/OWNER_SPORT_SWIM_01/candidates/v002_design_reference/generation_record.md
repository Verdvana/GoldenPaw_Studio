# Outfit Generation Record

- asset_id: `OWNER_SPORT_SWIM_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_SPORT_SWIM_01`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- head_policy: `not_applicable`
- candidate_version: `v002`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_SWIM_01/candidates/v002_design_reference/OWNER_SPORT_SWIM_01_DESIGN_REFERENCE_v002.png`
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

Use case: `product-mockup`. Create a clean clothing-only design reference plate with
no person, mannequin, head, face, body, hands, or feet. Show front and rear views of
the same white high-cut one-piece swimsuit with evenly distributed small strawberry
motifs, plus a plain white swim cap, plain white swim goggles, and a separate
skin-tone 15D matte pantyhose swatch. No footwear.

The construction must be read differently in the two views: in the FRONT view, show
a comparatively wider front lower gusset/panel. In the REAR view, show a very large
open-back cutout and a much narrower rear lower panel, only a narrow center rear
gusset/bridge, clearly narrower than the front panel and narrower than the previous
candidate. Do not mirror the front panel onto the back. Keep the garment coherent,
non-sensational, and technically plausible as swimwear. The cap and goggles must be
plain white with no strawberry motifs.

Use an opaque solid light neutral gray background, soft even catalog lighting,
vertical 3:4 standardized product-board composition, consistent scale, clean spacing,
ample margin, no labels or text. Define only swimsuit construction, cap, goggles,
hosiery material, and outfit coordination. Do not define any person or identity.

Avoid: person, model, mannequin, face, body, skin, hair, hands, feet, lifestyle pool
scene, dramatic lighting, large strawberries, patterned cap, patterned goggles,
opaque tights, glossy hosiery, latex, PVC, plastic, rubber, logo, readable text,
watermark, or collage clutter.

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- garment_reference_isolation_check: `PASS`
- face_contamination_check: `NOT_APPLICABLE`
- decision: `PENDING_USER_APPROVAL`
- observed_note: `Front panel is visibly wider; rear view shows a large open-back cutout and a substantially narrower rear center panel. Cap and goggles are plain white. Confirm the exact rear width and coverage before approval.`
