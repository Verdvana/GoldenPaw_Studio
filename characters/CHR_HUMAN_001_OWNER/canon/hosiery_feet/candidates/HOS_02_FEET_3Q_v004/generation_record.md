# HOS_02_FEET_3Q_v004 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_02_FEET_3Q
candidate_id: HOS_02_FEET_3Q_v004
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: PROMOTED_TO_L1_COMPONENT
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids: [OWNER_BODY_LEFT_3Q_CANON_L1]
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_02_FEET_3Q/OWNER_HOS_02_FEET_3Q_CANON_001.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: 0d0d5b55c0a33bed682465328e278b99e27de38aee472203c862aa4389ae6427
qa_status: PASS_BY_EXPLICIT_USER_REVIEW
```

## Authorization and lineage

On 2026-09-15 the user explicitly requested generation of HOS_02 and specified two correction targets: visible hosiery tension between the toes and a soft, hazy sheer-textile appearance. This is an independent reconstruction from the approved left 3/4 Body Master only. v001 and v003 had no raster output; v002 was user-rejected. No rejected or failed candidate pixels are used.

## Generation result

- generated_at: `2026-09-15`
- result: user-supplied raster was found in the project approved directory and verified as a 1086x1448 RGB PNG.
- original_candidate_path: no candidate raster path; the user placed the raster directly in `canon/hosiery_feet/approved/`.
- current_approved_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_02_FEET_3Q/OWNER_HOS_02_FEET_3Q_CANON_001.png`
- approval: explicit user approval received on `2026-09-15`.

## Promotion record

- decision: `APPROVED`
- approval_record: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_02_FEET_3Q/approvals/APPROVAL_OWNER_HOS_02_FEET_3Q_001.md`
- metadata: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_02_FEET_3Q/OWNER_HOS_02_FEET_3Q_CANON_001.png.metadata.yaml`

## Reference responsibilities

- `OWNER_BODY_LEFT_3Q_CANON_L1`: approved anatomical-left 3/4 lower-leg, ankle and foot geometry, proportions, direction, separated stance and floor contact only.
- No material photograph is attached. The 15D nude matte/velvet sheer hosiery behavior is defined textually to keep the material continuous, soft and non-plastic.

## Prompt assembly

```text
Use case: photorealistic-natural
Asset type: Gate-7 L1 hosiery and foot calibration candidate
Primary request: Create exactly one neutral, non-sensational technical lower-limb textile calibration image for adult character CHR_HUMAN_001_OWNER, asset HOS_02_FEET_3Q.
Input image: approved OWNER_BODY_LEFT_3Q_CANON_L1 only; use it only for anatomical-left 35–45 degree three-quarter lower-leg and foot geometry, natural proportions, separated stance and stable floor contact.
Scene/backdrop: clean neutral light-gray seamless studio, no props.
Subject: only lower legs from mid-calf through both complete feet, both feet fully separated and readable.
Style/medium: photorealistic clinical apparel-fit documentation, restrained 85–100mm perspective, camera near ankle height, even neutral white lighting.
Materials/textures: one continuous light-nude 15D velvet-finish sheer pantyhose garment; fine translucent textile with soft hazy diffusion and restrained matte response. Show subtle fabric tension following each toe separately: delicate smooth stretch and gentle translucent shading in the spaces between adjacent toes, with no hard lines or dark grooves. The hazy veil must soften the toe silhouettes and burgundy toenails beneath the fabric without making the feet look bare.
Constraints: continuous coverage from mid-calf over ankle, heel, arch, instep, forefoot and every toe tip; closed-toe hosiery; natural toe count and anatomy; one image, exact 3:4 vertical frame; REVIEW_REQUIRED candidate only.
Avoid: toe-cap edge, seam, band, ankle cutoff, opacity break, material change, bare toes, opaque socks, white/gray hosiery, glossy wet plastic, latex, PVC, rubber, body paint, exaggerated toe grooves, duplicated/fused/missing toes, shoes, supports, accessories, erotic/fashion styling, text, logo, watermark, collage, extra views, and any prior generated image.
```
