# HOS_03_FEET_SIDE_v004 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_03_FEET_SIDE
candidate_id: HOS_03_FEET_SIDE_v004
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids: [OWNER_BODY_LEFT_SIDE_CANON_L1]
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_03_FEET_SIDE_v004/HOS_03_FEET_SIDE_v004.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: 2af4c2b83f17a0d211ca5ab3c597196eaa647ff0efad274ff0a1393dd840dc81
qa_status: PENDING_USER_REVIEW
```

## Authorization and lineage

On 2026-09-15 the user rejected v003 because the toe gaps remained too distinct and the added textile tension was not visually different. Comparison with the approved side Body Master showed that the model was over-preserving individual toe outlines. v004 changes the visual hierarchy: the covered forefoot silhouette is primary, and toe anatomy is only a soft secondary contour. This is an independent reconstruction from the approved side Body Master; v001–v003 are excluded as pixel inputs.

## Generation result

- generated_at: `2026-09-15`
- result: generated successfully with the approved side Body Master as the sole image reference.
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_03_FEET_SIDE_v004/HOS_03_FEET_SIDE_v004.png`
- actual_dimensions_px: `1086x1448`
- checksum_sha256: `2af4c2b83f17a0d211ca5ab3c597196eaa647ff0efad274ff0a1393dd840dc81`
- promotion_status: not promoted; explicit user review required.

## Reference responsibilities

- `OWNER_BODY_LEFT_SIDE_CANON_L1`: exact anatomical-left true side lower-leg, ankle, heel, arch and broad foot profile, proportions and floor contact only.
- No material photograph is attached. Gate-7 15D nude matte/velvet continuous coverage is textual.

## Prompt assembly

```text
Create one neutral photorealistic medical textile quality-control reference image, exact 3:4 vertical. Use the supplied approved anatomical-left side Body Master only for one true side-profile lower-extremity form, broad heel and arch geometry, ankle transition, proportions and flat floor contact. Do not use any previous generated image.

Show a close technical crop from just below the knee through one complete foot, true anatomical-left side profile, enlarged for material inspection. Light-gray seamless clinical background, soft even white light, no props or styling.

A single continuous light-nude 15-denier matte sheer woven textile covers the form from calf through ankle, heel, arch, instep, forefoot and toe tips. It is a soft translucent veil with hazy diffusion and uniform weave, hue, opacity and surface response.

Critical visual hierarchy: the covered forefoot must read as one smooth, nearly continuous textile silhouette. The textile bridges across the toe region and softly compresses the toe forms together. Individual toe tips are not separately outlined; toe anatomy is visible only as very shallow, low-contrast rounded vertical undulations beneath the same fabric. There are no dark interdigital gaps, open clefts, bare-looking separations or sharp toe boundaries. Create subtle lengthwise fabric tension along the top of the toes and instep while keeping the toe region softly unified.

Preserve only the broad side anatomy that matters for this view: natural heel curve, arch curve, ankle transition, overall forefoot direction and flat contact. Do not prioritize crisp individual toe separation. No crosswise construction feature, toe-cap treatment, reinforced zone, seam, band, cutoff, abrupt hue or opacity change, dark groove or graphic line. Any nail color remains an indistinct muted tone beneath the textile.

No exposed surface, bare-toe appearance, opaque sock, glossy coating, plastic, rubber, latex, PVC, body paint, duplicated/missing anatomy, shoes, supports, accessories, labels, logos, watermark, collage or extra views. Return one technical REVIEW_REQUIRED candidate only.
```
