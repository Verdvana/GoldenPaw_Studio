# HOS_01_LOWER_LEGS_FEET_FRONT_v006 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_01_LOWER_LEGS_FEET_FRONT
candidate_id: HOS_01_LOWER_LEGS_FEET_FRONT_v006
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: PROMOTED_TO_L1_COMPONENT
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids: [OWNER_BODY_FRONT_CANON_L1]
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_01_LOWER_LEGS_FEET_FRONT/OWNER_HOS_01_LOWER_LEGS_FEET_FRONT_CANON_002.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: ea8f2e413fd7bdacfd4328853ccbbe190fa10f0a36f003b3b724f56a364298d3
qa_status: PASS_BY_EXPLICIT_USER_REVIEW
```

## Authorization and lineage

On 2026-09-15 the user rejected v005 because its crosswise toe-root line was more pronounced. Inspection confirmed that the approved Body Master does not contain this line. The likely failure mode is model insertion of a conventional pantyhose toe-cap boundary, amplified by a distant full-lower-leg crop and repeated negative wording. v006 changes the composition and wording strategy. It is an independent reconstruction from the approved front Body Master only; no HOS_01 Canon raster or previous candidate pixels are used.

## Generation result

- generated_at: `2026-09-15`
- result: first v006 wording pass was output-moderation blocked; a safer clinical textile quality-control retry generated the saved candidate.
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_01_LOWER_LEGS_FEET_FRONT_v006/HOS_01_LOWER_LEGS_FEET_FRONT_v006.png`
- actual_dimensions_px: `1086x1448`
- checksum_sha256: `ea8f2e413fd7bdacfd4328853ccbbe190fa10f0a36f003b3b724f56a364298d3`
- promotion_status: promoted to `OWNER_HOS_01_LOWER_LEGS_FEET_FRONT_CANON_002` after explicit user approval.
- approval_record: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_01_LOWER_LEGS_FEET_FRONT/approvals/APPROVAL_OWNER_HOS_01_LOWER_LEGS_FEET_FRONT_002.md`

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: front lower-leg and foot anatomy/proportions, neutral parallel contact and burgundy toenail direction only.
- No material photograph is attached. The textile behavior is specified in prose.

## Prompt assembly

```text
Create one neutral photorealistic clinical textile-fit reference for adult character CHR_HUMAN_001_OWNER, asset HOS_01_LOWER_LEGS_FEET_FRONT. Use the supplied approved front Body Master only for front lower-leg and foot anatomy, proportions, neutral parallel stance and floor contact. Do not use any previous generated image.

Composition: a close technical crop from just below the knees through both complete feet, with the feet large enough in frame for textile inspection; straight-on front view, both feet flat, separate and fully readable, exact 3:4 vertical frame. Light-gray seamless studio, soft even neutral light, no props.

The visible legs and feet are covered by one continuous light-nude 15D velvet-matte sheer pantyhose. Render it as a fine, translucent, softly hazy woven veil with a uniform surface response. Across the feet, the textile follows the length of each toe individually and remains smoothly continuous from instep into the forefoot and across the toe forms. The spaces between adjacent toes show gentle fabric convergence and soft diffusion, while the overall surface stays calm and uninterrupted. Burgundy toenails are only muted color beneath the textile.

The forefoot must read as one uninterrupted textile plane: no crosswise construction feature, no toe-cap treatment, no reinforced zone, no seam, no band, no abrupt tonal or opacity change, and no straight mark across the foot. Toe separation is only soft, localized anatomical contouring under the same hazy fabric, never a transverse line. Keep natural toe count, spacing, heel and ankle anatomy.

No bare toes, exposed nails, opaque socks, glossy coating, plastic, latex, PVC, rubber, body paint, duplicated/fused/missing toes, broken heels, shoes, supports, accessories, erotic or fashion styling, text, logo, watermark, collage or extra views. Output one REVIEW_REQUIRED candidate only.
```
