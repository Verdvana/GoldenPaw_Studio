# HOS_03_FEET_SIDE_v006 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_03_FEET_SIDE
candidate_id: HOS_03_FEET_SIDE_v006
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: PROMOTED_TO_L1_COMPONENT
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids: [OWNER_BODY_LEFT_SIDE_CANON_L1]
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_03_FEET_SIDE/OWNER_HOS_03_FEET_SIDE_CANON_001.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: e9e224eda17aaf4dc144d7198c9cdc60fc7a2b6f0f6afb30bebb4453dbd0d1be
qa_status: PASS_BY_EXPLICIT_USER_REVIEW
```

## Authorization and lineage

On 2026-09-15 the user accepted v005's hallux and toe-bridge direction but requested removal of inappropriate hosiery folds at the front ankle and below the ankle. v006 is an independent reconstruction from the approved side Body Master only; v001–v005 are excluded as pixel inputs.

## Generation result

- generated_at: `2026-09-15`
- result: generated successfully with the approved side Body Master as the sole image reference.
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_03_FEET_SIDE_v006/HOS_03_FEET_SIDE_v006.png`
- actual_dimensions_px: `1086x1448`
- checksum_sha256: `e9e224eda17aaf4dc144d7198c9cdc60fc7a2b6f0f6afb30bebb4453dbd0d1be`
- promotion_status: promoted to `OWNER_HOS_03_FEET_SIDE_CANON_001` after explicit user approval.
- approval_record: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_03_FEET_SIDE/approvals/APPROVAL_OWNER_HOS_03_FEET_SIDE_001.md`

## Reference responsibilities

- `OWNER_BODY_LEFT_SIDE_CANON_L1`: true side lower-leg, heel, arch, ankle and foot geometry, broad natural hallux profile, proportions and flat floor contact only.
- No material photograph or previous generated hosiery image is attached.

## Prompt assembly

```text
Create one neutral photorealistic medical textile quality-control reference image, exact 3:4 vertical. Use the supplied approved anatomical-left side Body Master only for one true side-profile lower-extremity form, heel, arch, ankle, broad hallux profile, proportions and flat floor contact. Do not use any previous generated image.

Show a close technical crop from just below the knee through one complete foot, true anatomical-left side profile, enlarged for material inspection. The foot is standing flat and weight-bearing on one seamless floor plane. Light-gray seamless clinical background, soft even white light, no props or styling.

A single continuous light-nude 15-denier matte sheer woven textile covers the form from calf through ankle, heel, arch, instep, forefoot and toe tips. It is a fine translucent veil with soft hazy diffusion, uniform weave and stable high-elasticity fit.

The hosiery is taut and smoothly fitted to the standing anatomy. From calf through the front ankle, ankle hollow, heel transition, arch and instep, the fabric lies flat and follows the contour continuously. The front ankle and the area immediately below the ankle must be clean, smooth and evenly tensioned, with no loose material.

Keep the broad natural rounded hallux profile from the approved anatomy, with smaller toes softly nested behind it. Preserve v005's unified toe-region textile: the forefoot is one calm continuous covered silhouette, toe spaces are shallow and hazy, and the fabric bridges the toes with subtle longitudinal tension.

Hard material constraints: no wrinkles, folds, bunching, slack, sagging, gathered fabric, compression rings, transverse creases, diagonal creases, ankle bands, abrupt weave changes, opacity breaks, seams, toe-cap construction or dark grooves anywhere, especially at the front ankle and below the ankle. The textile must look elastic, smooth and closely fitted, never loose or low-stretch. Any nail color remains muted beneath the fabric.

No exposed surface, bare-toe appearance, opaque sock, glossy coating, plastic, rubber, latex, PVC, body paint, duplicated/missing anatomy, shoes, supports, accessories, labels, logos, watermark, collage or extra views. Return one technical REVIEW_REQUIRED candidate only.
```
