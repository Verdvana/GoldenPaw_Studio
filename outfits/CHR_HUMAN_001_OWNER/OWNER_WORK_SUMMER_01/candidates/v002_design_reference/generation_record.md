# Outfit Generation Record

- asset_id: `OWNER_WORK_SUMMER_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_WORK_SUMMER_01`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- head_policy: `not_applicable`
- candidate_version: `v002`
- status: `REJECTED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/candidates/v002_design_reference/OWNER_WORK_SUMMER_01_DESIGN_REFERENCE_v002.png`
- output_sha256: `ade5f3b0f4ca7c065540354f9fa8b2beab97b62d46395c2d3fdbe82f832c7394`
- reference_budget: `text-only; no previous candidate pixels used`

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

Use case: `product-mockup`. Create a clean clothing-only design reference plate
for a reusable L2 summer office outfit, with no person, mannequin, head, face,
body, hands, or feet. Show a black ultra-low-neckline fitted short-sleeve top; a
fitted skirt with a predominantly white but clearly warm champagne-tinted base and
dense small crisp black polka dots, ending at mid-thigh; a gray 15D matte sheer
hosiery material swatch; and black approximately 5 cm one-band open-toe heeled
sandals. Each sandal has one simple broad horizontal front strap across the forefoot
and exactly one thin rear heel strap, with no closed toe box and no additional ankle
straps. No brand text or logo.

Scene/backdrop: seamless light neutral gray studio product board, soft even neutral
catalog lighting.

Composition/framing: vertical 3:4 standardized clothing design plate; show front
and rear garment views aligned at consistent scale, the hosiery swatch separately,
and the pair of sandals separately. Ample margin, clean spacing, no labels or text.

Materials/textures: smooth black matte top; white fabric with a clearly visible
warm champagne undertone and dense small black polka dots; gray 15D sheer matte
hosiery with fine textile appearance and no shine; black refined heeled sandals with
clean smooth finish and a simple metallic square buckle only if naturally supported
by the single front strap, no logo.

Constraints: define only garment silhouette, color, pattern, hosiery finish,
footwear construction, and outfit coordination. Do not use the previous candidate
as an image input.

Avoid: person, model, mannequin, face, body, skin, hair, jewelry, pose, dramatic
lighting, room background, closed-toe pump, pointed pump, multiple heel straps,
ankle-wrap straps, opaque tights, glossy hosiery, latex, PVC, plastic, rubber,
brand logo, readable text, watermark, collage clutter, or unrelated garments.

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `UNREVIEWED`
- visual_status: `PASS_WITH_USER_REVIEW`
- garment_reference_isolation_check: `PASS`
- face_contamination_check: `NOT_APPLICABLE`
- decision: `REJECTED_BY_USER — awaiting supplied garment reference images`
