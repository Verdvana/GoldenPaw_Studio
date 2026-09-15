# HOS_04_TOES_FRONT_DETAIL_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.201
identity_md_revision: draft_0.136
asset_id: HOS_04_TOES_FRONT_DETAIL
candidate_id: HOS_04_TOES_FRONT_DETAIL_v001
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: USER_REJECTED
approval_status: USER_REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids: [OWNER_BODY_FRONT_CANON_L1]
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_04_TOES_FRONT_DETAIL_v001/HOS_04_TOES_FRONT_DETAIL_v001.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: e5c96de505c9eacd0c0fb94793726608643b293ecc9c0373559150fb5b099f3b
qa_status: USER_REJECTED
```

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen call completed successfully and was copied into the project candidate path.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-94bf0ee3-5de0-4ce6-9f85-3c9a473a6bb2.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_04_TOES_FRONT_DETAIL_v001/HOS_04_TOES_FRONT_DETAIL_v001.png`
- project_candidate_checksum_sha256: `e5c96de505c9eacd0c0fb94793726608643b293ecc9c0373559150fb5b099f3b`
- technical_precheck: straight-on technical close-up returned with both forefeet, all toe silhouettes and toe tips readable, and fine textile coverage visible over the nails.
- review_points: verify no toe-cap boundary or material break, and confirm the visible muted burgundy nails read beneath the fabric.
- promotion_status: not promoted; awaiting explicit user approval.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: approved front lower-leg and foot geometry, toe proportions and neutral contact only.
- No material photograph is attached; Gate-7 15D nude matte/velvet continuous closed-toe behavior is textual.

HOS_01–03 and all other generated hosiery assets are excluded.

## Prompt assembly

```text
Create exactly one photorealistic, neutral clinical textile inspection image for adult character CHR_HUMAN_001_OWNER, asset HOS_04_TOES_FRONT_DETAIL. Use the supplied approved Body Master only for front-facing toe, forefoot and ankle geometry. Do not use any previous generated hosiery image or material photograph.

Show a straight-on technical close-up of both complete forefeet and toes, with a small amount of ankle and lower-leg context. Both feet are parallel, separated, fully in frame and resting neutrally on a light gray studio surface. Every toe silhouette and toe tip must be readable. Camera at toe height, restrained natural perspective, even neutral clinical lighting. This is a textile quality-control reference, not fashion or glamour.

Both feet are covered by one continuous pair of light-nude 15D sheer pantyhose with a soft velvet-matte finish. The same fine textile layer visibly lies over every toenail and every toe tip. Show continuous closed-toe coverage with no bare skin, no toe-cap border, no reinforced toe patch, no seam, no transverse line, no band, no opacity break and no abrupt color change. The textile is fine, translucent knit with restrained matte/velvet response; never glossy, wet, plastic, latex, PVC, rubber, opaque or body paint. Burgundy toenails may be faintly and softly visible beneath the fabric only.

Preserve natural toe anatomy and the supplied Body Master's proportions. No shoes, socks, supports, accessories, duplicated toes, fused toes or missing toes. Exact 3:4 vertical frame, one view only, no text, logo, watermark or collage. Output one REVIEW_REQUIRED candidate only.
```
