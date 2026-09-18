# BODY_06_BACK_v005 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.230
identity_md_revision: draft_0.182
asset_id: BODY_06_BACK
candidate_id: BODY_06_BACK_v005
gate: Gate 3 — Body Canon
model_tool: built-in image_gen
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_BODY_FRONT_CURRENT_FACE_EXCLUDED_DERIVATIVE
  - OWNER_L0_BODY_REAR_SIDE_CONTEXT
  - OWNER_HAIR_A_BACK_CANON_L1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 5
previous_ai_body_candidate_count: 0
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_06_BACK_v005/BODY_06_BACK_v005.png
checksum_sha256: 840c0de636c8d3d7c80cab9e268f6e5a76d0d271e56a85ae544be9a5f4b918f0
dimensions: 1086x1448
qa_status: PASS_USER_APPROVED
```

## Inputs and responsibilities

1. `OWNER_BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v3` — deterministic current-005 neck-below geometry only: waist/hip relationship, fuller thigh/calf volume, straight leg axes, outer leg contours, foot scale and neutral stance; excludes face, hair, clothing, hosiery material, lighting and background.
2. `L0_OWNER_002` / `source/identity/raw/3.jpg` — stature and natural body context only.
3. `L0_OWNER_015` / `source/identity/raw/17.jpg` — rear/side depth and silhouette plausibility only; it must not override the current front-derived leg contours.
4. `OWNER_HAIR_A_04_BACK_CANON_001` — Hairstyle-A rear fall only.
5. `OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001` — pale slightly-whiter 15D hosiery and gradual heel-transparency behavior only.

`OWNER_BODY_01_FRONT_CANON_005`, `OWNER_BODY_06_BACK_CANON_002` and `BODY_06_BACK_v004` are `qa_comparison_only`; no previous back candidate pixels are generation inputs.

## Prompt assembly

Create exactly one neutral, non-erotic, exact 180-degree full-length back-view technical apparel-fit chart of the same adult woman, fully clothed in a plain pink athletic one-piece garment, continuous pale hosiery and no shoes. Use the face-excluded current-front derivative as the primary authority for all neck-below proportions and leg contour alignment; use the rear/side L0 only to add plausible back depth. Use the Hair-A image only for rear hair and the hosiery crop only for material.

The back body must match current front Canon 005 in measurable silhouette logic: same 168 cm / approximately 60 kg scale, same slightly narrow waist, same smooth waist-to-hip transition, same fuller thigh and calf volume, same straight lower-leg axes, same leg width and same outer-leg contour envelope. In particular, the back-view outer edges of the thighs and calves must align with the front-approved width and continue at corresponding heights; do not narrow, bow, taper inward, or independently redesign the legs in back view. Keep a tiny natural inner-leg separation, symmetric knees and ankles, uncrossed legs, and both feet fully flat on the floor.

The rear one-piece opening remains a clearly raised/high-cut athletic opening aligned with the front opening height, symmetric and coherent at the waist-to-hip-to-upper-thigh transition. Hosiery remains the accepted pale, slightly-whiter 15D matte/velvet sheer textile, continuous over the full legs and feet. At both rear heels retain a smooth gradual transition to slightly greater translucency while keeping complete coverage; no white ring, hard band, seam, material break or plastic appearance.

Neutral gray-white seamless studio, soft even light, level 70–85mm camera, exact 3:4 portrait, complete head and feet visible, head/body exactly away from camera, no twist, props, text, watermark or collage. One `REVIEW_REQUIRED` candidate only; not Canon.

## QA plan

Primary checks: compare back leg widths and outer contour envelope against the current-front face-excluded derivative at corresponding heights; verify straight axes, preserved fuller volume, waist/hip continuity, high-cut opening alignment, full-foot contact and hosiery/heel-gradient continuity. Compare approved back Canon only as a secondary historical view QA; do not promote automatically.

## Generation output

- Generated source: `/home/verdvana/.codex/generated_images/01a0aeda-94e0-7940-aa23-e89d1ec0cff1/exec-4d32186b-4a3f-4bcd-bc4d-a324c3a0c3e5.png`
- Repository candidate: `BODY_06_BACK_v005.png`
- Visual precheck: rear leg width and outer contour are more closely constrained to the current front-derived geometry; the v018/v019 body volume and accepted hosiery appearance remain present for user review.

## Approval and promotion

- User approval: “可以 登记吧”
- Approved asset: `OWNER_BODY_06_BACK_CANON_003`
- Promoted path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_06_BACK_v005/BODY_06_BACK_v005.png`
- Original candidate path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_06_BACK_v005/BODY_06_BACK_v005.png`
- Promotion operation: moved unchanged; no duplicate candidate raster retained
