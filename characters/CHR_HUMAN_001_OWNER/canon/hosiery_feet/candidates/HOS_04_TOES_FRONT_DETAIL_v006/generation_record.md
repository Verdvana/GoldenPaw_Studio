# HOS_04_TOES_FRONT_DETAIL_v006 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_04_TOES_FRONT_DETAIL
candidate_id: HOS_04_TOES_FRONT_DETAIL_v006
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_04_TOES_FRONT_DETAIL_v006/HOS_04_TOES_FRONT_DETAIL_v006.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: edd77f0ff374599c9e1e96ff06462d58573e6da32d56bfbf51a810eb5baf21c9
qa_status: PENDING_USER_REVIEW
```

## Authorization and lineage

On 2026-09-15 the user requested a small increase in HOS_04 textile thickness because v005 appeared too thin. v006 is an independent reconstruction from the approved front Body Master only. v005 and all earlier HOS_04 candidates are excluded as pixel inputs.

## Generation result

- generated_at: `2026-09-15`
- result: generated successfully with the approved front Body Master as the sole image reference.
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_04_TOES_FRONT_DETAIL_v006/HOS_04_TOES_FRONT_DETAIL_v006.png`
- actual_dimensions_px: `1086x1448`
- checksum_sha256: `edd77f0ff374599c9e1e96ff06462d58573e6da32d56bfbf51a810eb5baf21c9`
- promotion_status: not promoted; explicit user review required.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: front foot and toe anatomy, proportions and neutral contact only.
- No material photograph or previous generated hosiery image is attached.

## Prompt assembly

```text
Create one neutral photorealistic medical textile quality-control reference image, exact 3:4 vertical. Use the supplied approved front Body Master only for front foot and toe anatomy, proportions and neutral contact. Do not use any previous generated image.

Show a straight-on close technical view of both complete forefeet and all toe forms, with a small amount of ankle and instep context. Feet parallel, naturally separated, fully readable, flat on a light-gray seamless clinical surface. Camera at toe height, restrained perspective, soft even white light, no props or styling.

A single continuous light-nude 15-denier matte sheer woven textile covers the toes, forefeet, insteps and ankle context. Compared with an extremely thin veil, make the textile only slightly more substantial and visibly present: a modest increase in yarn density and opacity, still clearly translucent, soft, hazy and fine-knit. It must remain a 15D sheer hosiery appearance, not 30D, not opaque and not a sock.

The fabric follows each rounded toe form with smooth low-contrast tension, gently stretches over the nail and toe pad, bridges the shallow spaces between adjacent toes, and softly diffuses the underlying contours. Toe shapes remain natural but unified by the same continuous textile. Burgundy nail color is subdued and blurred beneath the slightly denser fabric, never crisp or exposed.

The textile continues without interruption from ankle over instep, forefoot and every toe tip. No toe-cap construction, reinforced panel, seam, band, transverse boundary, abrupt hue or opacity change, hard interdigital groove, glossy coating, plastic surface or opaque sock. Preserve natural toe count, spacing and proportions.

No exposed surface, bare-toe appearance, rubber, latex, PVC, body paint, duplicated/fused/missing anatomy, shoes, accessories, labels, logos, watermark, collage or extra views. Return one technical REVIEW_REQUIRED candidate only.
```
