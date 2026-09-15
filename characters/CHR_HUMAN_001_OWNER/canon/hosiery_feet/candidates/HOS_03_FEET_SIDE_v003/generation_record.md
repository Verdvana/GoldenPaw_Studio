# HOS_03_FEET_SIDE_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_03_FEET_SIDE
candidate_id: HOS_03_FEET_SIDE_v003
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_03_FEET_SIDE_v003/HOS_03_FEET_SIDE_v003.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: 2a4c97ff158808cf5c36c15e6f64944ec838184076cb8951e8161a3a5f73eade
qa_status: PENDING_USER_REVIEW
```

## Authorization and lineage

On 2026-09-15 the user requested a correction because v002 lacked visible fabric tension between the toes and rendered the toe gaps too clearly. v003 is an independent reconstruction from the approved anatomical-left side Body Master only. v001 and v002 are excluded as pixel inputs.

## Generation result

- generated_at: `2026-09-15`
- result: generated successfully with the approved side Body Master as the sole image reference.
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_03_FEET_SIDE_v003/HOS_03_FEET_SIDE_v003.png`
- actual_dimensions_px: `1086x1448`
- checksum_sha256: `2a4c97ff158808cf5c36c15e6f64944ec838184076cb8951e8161a3a5f73eade`
- promotion_status: not promoted; explicit user review required.

## Reference responsibilities

- `OWNER_BODY_LEFT_SIDE_CANON_L1`: exact anatomical-left true side lower-leg, ankle, heel, arch and foot geometry, proportions and floor contact only.
- No material photograph is attached. Gate-7 15D nude matte/velvet continuous coverage is textual.

## Prompt assembly

```text
Create one neutral photorealistic medical textile quality-control reference image for adult character CHR_HUMAN_001_OWNER, asset HOS_03_FEET_SIDE. Use the supplied approved anatomical-left side Body Master only for true side lower-extremity geometry, heel profile, arch, ankle transition, toe alignment, proportions and floor contact. Do not use any prior generated image.

Composition: close technical crop from just below the knee through one complete foot, anatomical-left true side profile, enlarged for textile inspection. The foot is flat on one seamless floor plane. Exact 3:4 vertical frame, light-gray seamless clinical background, soft even white light, no props or styling.

A single continuous light-nude 15-denier matte sheer textile covers the visible lower extremity as a soft hazy translucent veil. The fabric follows the side profile continuously from calf over ankle, heel, arch, instep, forefoot and toe tips.

Primary correction: the textile must visibly bridge and soften the spaces between adjacent toe forms. Show smooth fabric tension running lengthwise along each toe and gentle continuous bridging across the interdigital spaces, with low-contrast rounded transitions. The toes remain anatomically present but their gaps are shallow, softly diffused and clearly covered by the same textile; they must not read as deep open separations or exposed skin. The fabric surface stays uniform, calm and uninterrupted from instep through the forefoot and toes.

Preserve the natural side heel curve, arch, ankle transition and toe count beneath the textile. No crosswise construction feature, toe-cap treatment, reinforced zone, seam, band, cutoff, abrupt hue or opacity change, dark groove, deep cleft or graphic line. Burgundy nail color, if visible, is muted beneath the textile.

No exposed surface, bare-toe appearance, opaque sock, glossy coating, plastic, rubber, latex, PVC, body paint, duplicated/fused/missing anatomy, shoes, supports, accessories, labels, logos, watermark, collage or extra views. Return one technical REVIEW_REQUIRED candidate only.
```
