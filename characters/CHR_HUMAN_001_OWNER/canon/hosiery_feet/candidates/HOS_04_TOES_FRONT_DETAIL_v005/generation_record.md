# HOS_04_TOES_FRONT_DETAIL_v005 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_04_TOES_FRONT_DETAIL
candidate_id: HOS_04_TOES_FRONT_DETAIL_v005
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids: [OWNER_BODY_FRONT_CANON_L1]
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_04_TOES_FRONT_DETAIL_v005/HOS_04_TOES_FRONT_DETAIL_v005.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: e8c41adc9a5bee1c14a84f50dee03e046a71231b18bd72b84c53d22ca3ecbe87
qa_status: PENDING_USER_REVIEW
```

## Authorization and lineage

On 2026-09-15 the user requested the next Gate-7 item, HOS_04. v005 is an independent reconstruction from the approved front Body Master only. v001 was rejected, v002 remains review-only, and v003/v004 returned no raster output; none are used as pixel inputs.

## Generation result

- generated_at: `2026-09-15`
- result: generated successfully with the approved front Body Master as the sole image reference.
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_04_TOES_FRONT_DETAIL_v005/HOS_04_TOES_FRONT_DETAIL_v005.png`
- actual_dimensions_px: `1086x1448`
- checksum_sha256: `e8c41adc9a5bee1c14a84f50dee03e046a71231b18bd72b84c53d22ca3ecbe87`
- promotion_status: not promoted; explicit user review required.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: front foot and toe geometry, proportions and neutral contact only.
- No material photograph or previous generated hosiery image is attached.

## Prompt assembly

```text
Create one neutral photorealistic medical textile quality-control reference image, exact 3:4 vertical. Use the supplied approved front Body Master only for front foot and toe anatomy, proportions and neutral contact. Do not use any previous generated image.

Show a straight-on close technical view of both complete forefeet and all toe forms, with a small amount of ankle and instep context. Feet parallel, naturally separated, fully readable, flat on a light-gray seamless clinical surface. Camera at toe height, restrained perspective, soft even white light, no props or styling.

A single continuous light-nude 15-denier matte sheer woven textile covers the toes, forefeet, insteps and ankle context. It reads as a fine translucent veil with soft hazy diffusion and uniform weave, hue, opacity and surface response. Make the textile moderately visible rather than bare-skin-like.

The fabric follows each rounded toe form with smooth, low-contrast tension: it gently stretches over the nail and toe pad, bridges the shallow spaces between adjacent toes, and softly diffuses the underlying contours. Toe shapes remain natural but are unified by the same continuous textile; there are no deep open gaps or exposed-looking separations. Tension should appear as subtle curved tonal compression and a restrained matte highlight integrated into the weave, never as drawn lines.

The textile continues without interruption from ankle over instep, forefoot and every toe tip. No toe-cap construction, reinforced panel, seam, band, transverse boundary, abrupt hue or opacity change, hard interdigital groove, glossy coating or opaque sock. Burgundy nail color is muted and only beneath the fabric. Preserve natural toe count, spacing and proportions.

No exposed surface, bare-toe appearance, plastic, rubber, latex, PVC, body paint, duplicated/fused/missing anatomy, shoes, accessories, labels, logos, watermark, collage or extra views. Return one technical REVIEW_REQUIRED candidate only.
```
