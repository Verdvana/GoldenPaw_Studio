# HOS_03_FEET_SIDE_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_03_FEET_SIDE
candidate_id: HOS_03_FEET_SIDE_v002
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_03_FEET_SIDE_v002/HOS_03_FEET_SIDE_v002.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: 46861af0705c3ec59b6d447c06ba74babc234f8e6b38d0638941040b0221f16e
qa_status: PENDING_USER_REVIEW
```

## Authorization and lineage

On 2026-09-15 the user authorized generation of HOS_03. v002 is an independent reconstruction from the approved anatomical-left side Body Master only. HOS_01, HOS_02 and blocked v001 are excluded as pixel inputs.

## Generation result

- generated_at: `2026-09-15`
- result: first prompt pass was output-moderation blocked; a safer clinical textile-inspection retry generated the saved candidate.
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_03_FEET_SIDE_v002/HOS_03_FEET_SIDE_v002.png`
- actual_dimensions_px: `1086x1448`
- checksum_sha256: `46861af0705c3ec59b6d447c06ba74babc234f8e6b38d0638941040b0221f16e`
- promotion_status: not promoted; explicit user review required.

## Reference responsibilities

- `OWNER_BODY_LEFT_SIDE_CANON_L1`: exact anatomical-left true side lower-leg, ankle, heel, arch and foot geometry, proportions and floor contact only.
- No material photograph is attached. Gate-7 15D nude matte/velvet continuous coverage is textual.

## Prompt assembly

```text
Create one neutral photorealistic medical textile quality-control reference image for adult character CHR_HUMAN_001_OWNER, asset HOS_03_FEET_SIDE. Use the supplied approved anatomical-left side Body Master only for true side lower-extremity geometry, heel profile, arch, ankle transition, toe alignment, proportions and floor contact. Do not use any prior generated image.

Composition: close technical crop from just below the knee through one complete foot, anatomical-left true side profile, enlarged enough to inspect heel, arch, instep, forefoot and toe tips. The foot is flat on one seamless floor plane. Exact 3:4 vertical frame, light-gray seamless clinical background, soft even white light, no props or styling.

A single continuous light-nude 15-denier matte sheer hosiery textile covers the visible lower extremity. Render it as a fine translucent woven veil with soft hazy diffusion and uniform surface response. The textile follows the side profile continuously from calf over ankle, heel, arch, instep, forefoot and toe tips. Show natural gentle longitudinal stretch along the arch and instep and localized soft diffusion over the toe forms. Keep the surface calm and uninterrupted.

The entire profile reads as one continuous textile plane: no toe-cap treatment, reinforced zone, seam, band, ankle cutoff, abrupt hue or opacity change, or crosswise construction feature. Preserve natural heel curve, arch line, ankle transition and toe count beneath the same hazy fabric. Burgundy nail color, if visible, stays muted beneath the textile.

No exposed skin, bare-toe appearance, opaque socks, glossy coating, plastic, rubber, latex, PVC, body paint, duplicated/fused/missing anatomy, shoes, supports, accessories, labels, logos, watermark, collage or extra views. Return one technical REVIEW_REQUIRED candidate only.
```
