# Outfit Generation Record

- asset_id: `OWNER_SPORT_SWIM_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_SPORT_SWIM_01`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- head_policy: `not_applicable`
- candidate_version: `v001`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_SWIM_01/candidates/v001_design_reference/OWNER_SPORT_SWIM_01_DESIGN_REFERENCE_v001.png`
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
a coordinated swimming outfit, with no person, mannequin, head, face, body, hands,
or feet. Show front and rear views of a white high-cut open-back one-piece swimsuit
covered evenly with small strawberry motifs; a white swim cap; white swim goggles;
and a separate nude 15D matte hosiery swatch representing the existing outfit
contract, with no footwear.

The swimsuit rear lower coverage must be intentionally narrow, approximately one
third the width of the corresponding front lower coverage, expressed as a precise
technical garment construction. Keep the garment coherent and non-sensational,
with clean professional swimwear catalog presentation. Make the back visibly open,
the leg openings high-cut, and the strawberry pattern small, repeated and evenly
distributed over the white base.

Use an opaque solid light neutral gray background, soft even catalog lighting,
vertical 3:4 standardized product-board composition, consistent scale, clean
spacing, ample margin, no labels or text. Define only swimwear, cap, goggles,
hosiery material and outfit coordination. Do not define any person or identity.

Avoid: person, model, mannequin, face, body, skin, hair, hands, feet, lifestyle
pool scene, dramatic lighting, large strawberries, green swimsuit, opaque tights,
glossy hosiery, latex, PVC, plastic, rubber, logo, readable text, watermark, or
collage clutter.

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
- observed_note: `The cap rendered with small strawberry motifs as part of the coordinated board; confirm whether the final cap should be plain white or patterned white.`
