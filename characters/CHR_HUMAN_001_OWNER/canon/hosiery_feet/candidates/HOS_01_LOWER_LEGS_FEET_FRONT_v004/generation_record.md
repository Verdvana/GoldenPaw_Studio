# HOS_01_LOWER_LEGS_FEET_FRONT_v004 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_01_LOWER_LEGS_FEET_FRONT
candidate_id: HOS_01_LOWER_LEGS_FEET_FRONT_v004
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_01_LOWER_LEGS_FEET_FRONT_v004/HOS_01_LOWER_LEGS_FEET_FRONT_v004.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: 79d8bcb6a3b0d665d156743620842e81b2f1842980a12bd03c10b2e87e533451
qa_status: PENDING_USER_REVIEW
```

## Authorization and lineage

On 2026-09-15 the user requested a new HOS_01 version because the approved front asset does not show enough visible hosiery tension between adjacent toes. This is an independent reconstruction from the approved front Body Master only. The approved HOS_01 raster and all earlier HOS_01 candidates are excluded as pixel inputs; their successful geometry is retained only as written scope.

## Generation result

- generated_at: `2026-09-15`
- result: generated successfully with the approved front Body Master as the sole image reference.
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_01_LOWER_LEGS_FEET_FRONT_v004/HOS_01_LOWER_LEGS_FEET_FRONT_v004.png`
- actual_dimensions_px: `1086x1448`
- checksum_sha256: `79d8bcb6a3b0d665d156743620842e81b2f1842980a12bd03c10b2e87e533451`
- promotion_status: not promoted; explicit user review required.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: approved front lower-leg and foot anatomy/proportions, parallel neutral standing contact, natural skin-tone baseline and burgundy toenail direction only.
- No material photograph is attached. The 15D nude matte/velvet continuous-textile behavior is defined textually to avoid confusing material identity with anatomy.

## Prompt assembly

```text
Use case: photorealistic-natural
Asset type: Gate-7 L1 hosiery and foot calibration candidate
Primary request: Create exactly one neutral, non-sensational technical lower-limb textile calibration image for adult character CHR_HUMAN_001_OWNER, asset HOS_01_LOWER_LEGS_FEET_FRONT.
Input image: approved OWNER_BODY_FRONT_CANON_L1 only; use it solely for front lower-leg and foot anatomy/proportions, parallel neutral stance, floor contact and burgundy toenail direction. Do not use any previous HOS_01 raster or generated image.
Scene/backdrop: light-gray seamless clinical studio, no props.
Subject: only both lower legs from just above the knees through both complete feet, straight-on front view, both feet flat, separate and fully readable.
Style/medium: photorealistic orthopedic apparel-fit documentation, camera near mid-shin/ankle height, restrained 85–100mm perspective, soft even neutral white lighting.
Materials/textures: one continuous light-nude 15D velvet-finish matte sheer pantyhose garment, fine translucent woven textile with a soft hazy veil. Make the textile tension between adjacent toes visibly clearer than a flat skin-like wash: the fabric should smoothly stretch across each toe and gently bridge the interdigital spaces, with subtle continuous tonal compression and fine weave convergence, but no dark grooves or drawn lines. Keep the entire foot softly diffused through the hosiery; burgundy toenails remain muted and blurred beneath it.
Constraints: uninterrupted coverage from above knees through calves, ankles, heels, insteps, forefeet and every toe tip; one closed-toe textile layer; identical hue, weave, opacity and translucency across instep, forefoot and toes; exact 3:4 vertical frame; one REVIEW_REQUIRED candidate.
Avoid: toe-cap edge, seam, band, horizontal toe-root boundary, hard interdigital lines, exposed bare toes, crisp nail edges, opaque socks, glossy wet coating, plastic, latex, PVC, rubber, body paint, duplicated/fused/missing toes, broken heels, shoes, supports, accessories, erotic/fashion styling, text, logo, watermark, collage, extra views, and any prior generated image.
```
