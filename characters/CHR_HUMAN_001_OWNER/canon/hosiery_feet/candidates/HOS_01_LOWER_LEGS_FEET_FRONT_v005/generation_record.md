# HOS_01_LOWER_LEGS_FEET_FRONT_v005 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_01_LOWER_LEGS_FEET_FRONT
candidate_id: HOS_01_LOWER_LEGS_FEET_FRONT_v005
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_01_LOWER_LEGS_FEET_FRONT_v005/HOS_01_LOWER_LEGS_FEET_FRONT_v005.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: 5e15bf6075003b95736a3776961500e704ddfa2bedb86e5b29cb4ca48a05055e
qa_status: PENDING_USER_REVIEW
```

## Authorization and lineage

On 2026-09-15 the user rejected the v004 visual result because a strange horizontal line remained at the toe roots. v005 is an independent reconstruction from the approved front Body Master only. The approved HOS_01 raster, v004 and all earlier candidates are excluded as pixel inputs.

## Generation result

- generated_at: `2026-09-15`
- result: generated successfully with the approved front Body Master as the sole image reference.
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_01_LOWER_LEGS_FEET_FRONT_v005/HOS_01_LOWER_LEGS_FEET_FRONT_v005.png`
- actual_dimensions_px: `1086x1448`
- checksum_sha256: `5e15bf6075003b95736a3776961500e704ddfa2bedb86e5b29cb4ca48a05055e`
- promotion_status: not promoted; explicit user review required.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: approved front lower-leg and foot anatomy/proportions, parallel neutral standing contact, natural skin-tone baseline and burgundy toenail direction only.
- No material photograph is attached. The 15D nude matte/velvet continuous-textile behavior is defined textually.

## Prompt assembly

```text
Create exactly one neutral, non-sensational technical lower-limb textile calibration image for adult character CHR_HUMAN_001_OWNER, asset HOS_01_LOWER_LEGS_FEET_FRONT. Use the supplied approved front Body Master only for front lower-leg and foot anatomy/proportions, parallel neutral stance, floor contact and burgundy toenail direction. Do not use any previous HOS_01 raster or generated image.

Show only both lower legs from just above the knees through both complete feet, straight-on front view, both feet flat, separated and fully readable. Light-gray seamless clinical studio, no props, restrained 85–100mm perspective, soft even neutral white lighting, exact 3:4 vertical frame.

One continuous light-nude 15D velvet-matte sheer pantyhose garment covers the legs and feet. Keep a soft hazy translucent veil and fine woven textile response. The fabric gently conforms around the separate toes and has subtle smooth tension in the interdigital spaces, but every transition from instep to forefoot to toe tips must be visually continuous.

HARD NEGATIVE REQUIREMENT: absolutely no horizontal line at the toe roots or metatarsophalangeal area. Do not create a seam, toe-cap edge, reinforced toe, ridge, crease, band, color strip, opacity strip, weave direction change, highlight break, shadow stripe, or any straight/transverse mark crossing the forefoot. Do not replace the horizontal line with any other graphic boundary. The only visible toe separation must be soft natural anatomical contouring seen through the same uninterrupted hazy textile. Burgundy toenails remain low-saturation, blurred and beneath the fabric.

Keep normal toe count and anatomy. No bare toes, exposed nails, opaque socks, glossy coating, plastic, latex, PVC, rubber, body paint, duplicated/fused/missing toes, broken heels, shoes, supports, accessories, erotic or fashion styling, text, logo, watermark, collage, extra views, or prior generated image. Output one REVIEW_REQUIRED candidate only.
```
