# HOS_02_FEET_3Q_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.141
identity_md_revision: draft_0.136
asset_id: HOS_02_FEET_3Q
candidate_id: HOS_02_FEET_3Q_v002
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: USER_REJECTED
approval_status: USER_REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids: [OWNER_BODY_LEFT_3Q_CANON_L1]
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_02_FEET_3Q_v002/HOS_02_FEET_3Q_v002.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: 52d5bd22e2ab540a9efe367201e88cbd29b6005ede046e18eed8fcd0394a7306
qa_status: USER_REJECTED
```

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen call completed successfully and was copied into the project candidate path.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-c776751f-c8eb-4cd9-83fd-515019e0355f.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_02_FEET_3Q_v002/HOS_02_FEET_3Q_v002.png`
- project_candidate_checksum_sha256: `52d5bd22e2ab540a9efe367201e88cbd29b6005ede046e18eed8fcd0394a7306`
- technical_precheck: left 3/4 technical foot view returned with both complete feet, ankles, heels, insteps, toes and continuous nude hosiery context visible.
- review_points: verify closed-toe continuity, textile-vs-skin read, and muted burgundy nail visibility beneath the fabric.
- promotion_status: not promoted; awaiting explicit user approval.

## Reference responsibilities

- `OWNER_BODY_LEFT_3Q_CANON_L1`: approved owner's anatomical-left 35–45° 3/4 lower-leg, ankle and foot geometry, natural separated stance and floor contact only.
- No material image is attached. The 15D nude velvet-finish sheer hosiery behavior is defined by the Gate-7 textual material contract below.

Rejected HOS_02 attempts and all other generated assets are excluded.

## Prompt assembly

```text
Create exactly one photorealistic, non-sensational clinical textile-and-foot calibration image for adult character CHR_HUMAN_001_OWNER, asset HOS_02_FEET_3Q. Use the supplied approved left-3/4 Body Master only for anatomy, direction, proportions and stable floor contact. Do not use any previous generated image or any material photograph.

Show a neutral standing lower-leg and foot calibration view from mid-calf to both complete feet, anatomical-left 35–45° three-quarter angle, with both feet separated and fully readable. This is a technical orthopedic/anatomical reference, not a fashion, glamour or sensual image. Camera near ankle height, restrained 85–100mm perspective, neutral gray studio, even clinical lighting.

Both feet wear one continuous pair of light-nude 15D velvet-finish matte sheer pantyhose. The same fine textile visibly continues without interruption from calf over ankle, heel, instep, arch, forefoot and every toe tip. Closed-toe coverage is continuous: no bare toes, no toe-cap border, no seam, no band, no opacity break, no ankle cutoff. The textile is realistic fine knit with restrained matte/velvet response, not white, gray, opaque, glossy, wet, latex, PVC, plastic or body paint. Burgundy toenails may be softly muted beneath the sheer fabric but must never appear painted on top.

Preserve natural foot anatomy: correct heel, arch, ankle and toe proportions; all toe silhouettes distinct, no fused, missing or duplicated toes; both heels and insteps readable; no shoes, socks, supports or accessories. Exact 3:4 vertical image, one view only, no text, logo, watermark or collage. Output one REVIEW_REQUIRED candidate.
```
