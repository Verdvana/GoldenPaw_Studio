# HOS_04_TOES_FRONT_DETAIL_v007 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_04_TOES_FRONT_DETAIL
candidate_id: HOS_04_TOES_FRONT_DETAIL_v007
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_04_TOES_FRONT_DETAIL_v007/HOS_04_TOES_FRONT_DETAIL_v007.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: 7ab611451b85e8de66d8043ffa929aea937b790486768237e6f059b6b0278358
qa_status: PENDING_USER_REVIEW
```

## Authorization and lineage

On 2026-09-15 the user requested two small corrections to v006: slightly more textile thickness and stronger curved fabric tension between adjacent toes. v007 is an independent reconstruction from the approved front Body Master only. v001–v006 are excluded as pixel inputs.

## Generation result

- generated_at: `2026-09-15`
- result: generated successfully with the approved front Body Master as the sole image reference.
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_04_TOES_FRONT_DETAIL_v007/HOS_04_TOES_FRONT_DETAIL_v007.png`
- actual_dimensions_px: `1086x1448`
- checksum_sha256: `7ab611451b85e8de66d8043ffa929aea937b790486768237e6f059b6b0278358`
- promotion_status: not promoted; explicit user review required.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: front foot and toe anatomy, proportions and neutral contact only.
- No material photograph or previous generated hosiery image is attached.

## Prompt assembly

```text
Create one neutral photorealistic medical textile quality-control reference image, exact 3:4 vertical. Use the supplied approved front Body Master only for front foot and toe anatomy, proportions and neutral contact. Do not use any previous generated image.

Show a straight-on close technical view of both complete forefeet and all toe forms, with a small amount of ankle and instep context. Feet parallel, naturally separated, fully readable, flat on a light-gray seamless clinical surface. Camera at toe height, restrained perspective, soft even white light, no props or styling.

A single continuous light-nude 15-denier matte sheer woven textile covers the toes, forefeet, insteps and ankle context. Make it a little more substantial than v006: modestly denser fine knit and slightly greater opacity, while remaining clearly translucent, soft, hazy and delicate. It must remain sheer 15D hosiery, not 30D, not opaque and not a sock.

Strengthen the curved textile tension between adjacent toes. Each toe is softly wrapped by the same fabric, and the knit forms visible but gentle curved arcs that bridge from one toe contour toward the next through the shallow interdigital spaces. These arcs should read as smooth fabric tension integrated into the weave, with a restrained matte highlight and soft diffusion—not as seams, drawn lines, dark grooves or toe-cap borders. The toes remain natural and unified by one continuous textile plane. Burgundy nail color is subdued and blurred beneath the slightly denser fabric.

The textile continues without interruption from ankle over instep, forefoot and every toe tip. No toe-cap construction, reinforced panel, seam, band, transverse boundary, abrupt hue or opacity change, hard interdigital groove, glossy coating, plastic surface or opaque sock. Preserve natural toe count, spacing and proportions.

No exposed surface, bare-toe appearance, rubber, latex, PVC, body paint, duplicated/fused/missing anatomy, shoes, accessories, labels, logos, watermark, collage or extra views. Return one technical REVIEW_REQUIRED candidate only.
```
