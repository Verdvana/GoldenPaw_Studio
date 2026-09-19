# BODY_04_LEFT_SIDE_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.233
identity_md_revision: draft_0.186
asset_id: BODY_04_LEFT_SIDE
candidate_id: BODY_04_LEFT_SIDE_v003
gate: "Gate 3 — Body Canon"
generation_tool: built_in_image_gen
use_case: identity-preserve
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
reference_set_ids: [OWNER_FACE_LEFT_PROFILE_NEUTRAL_RECOVERY_V1, OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE, OWNER_BODY_REAR_CURRENT_LOWER_BODY_FACE_HAIR_EXCLUDED_DERIVATIVE]
generation_inputs:
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", sha256: d98019128bfa974a102813da52b4a2905ec4aa7c95eb5222a163e419f287e74d, responsibility: "source-derived identity and neutral skin baseline", must_not_define: "hair, body, clothing, lighting or background"}
  - {asset_id: L0_OWNER_012, path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/14.jpg", sha256: f7a83644f202ebec95134c6d115397b9f52f12e79b5fb227a6b79182026bd788, responsibility: "genuine image-right left-profile direction and limited view-dependent depth only", must_not_define: "fine identity priority, skin, hair, clothing, lighting or background"}
  - {asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png", sha256: 6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd, responsibility: "HAIRSTYLE_A only", must_not_define: "face, body, clothing, lighting or background"}
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b, responsibility: "current front body geometry, straight lower-leg axes, scale and stance", must_not_define: "face, identity, hair, clothing design, hosiery material, lighting or background"}
  - {asset_id: OWNER_BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_CROP.png", sha256: c3ce9451c3c328181a715f9efb4475f8ac69bf17259c51c2c9f513822944b10e, responsibility: "current rear lower-body cross-view geometry", must_not_define: "face, skin identity, hair, clothing design, hosiery material, lighting or background"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_04_LEFT_PROFILE_NEUTRAL/OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and true-profile comparison only"}
  - {asset_id: OWNER_BODY_04_LEFT_SIDE_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_04_LEFT_SIDE/OWNER_BODY_04_LEFT_SIDE_CANON_001.png", purpose: "post-generation continuity comparison only"}
reference_count: 5
previous_ai_body_candidate_count: 0
aspect_ratio: "3:4"
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_04_LEFT_SIDE_v003/BODY_04_LEFT_SIDE_v003.png
qa_status: PASS_USER_APPROVED
```

Create exactly one non-sexual clinical full-length technical reference at an exact 90-degree anatomical-left profile: face and whole body point image-right, one eye principally visible, no torso twist. Inputs 1–2 reconstruct only source-derived left-profile identity; Input 3 is the sole hairstyle authority; Inputs 4–5 constrain only currently registered Body01 and Body06 geometry. Preserve the 168 cm / approximately 60 kg scale, torso length, waist-to-hip relationship, natural thigh/calf volume, straight lower-leg direction, heel and foot scale. Keep head, torso, pelvis, knees and feet in one true side direction; knees, shins and ankles remain aligned with their thigh axes. Both feet are naturally grounded. Wear the fixed plain pink high-cut athletic one-piece, continuous pale 15D matte/velvet closed-foot pantyhose and no footwear. Hair is mandatory HAIRSTYLE_A: long, straight, loose dark-brown hair with a near-center part, low-to-medium crown volume, long face-side strands, and tapered ends falling below the chest. No updo, bun, clip, pin, tie, braid, ponytail or gathered hair. Exact 3:4, complete figure, level 70–85mm camera, neutral gray-white studio, soft even light. No props, text, watermark, glamour posing or sexualized presentation. Output one REVIEW_REQUIRED candidate only.

## Generation result and technical precheck

- generated_at: 2026-09-19
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_04_LEFT_SIDE_v003/BODY_04_LEFT_SIDE_v003.png`
- dimensions: `1086x1448`, exact 3:4
- sha256: `7c1c7f5eaf5699f4e39493ad4cfe120ee42497b2bc405137c901b87df843abd1`
- result: `USER_REVIEW_REQUIRED__TECHNICAL_PRECHECK_PASS`
- precheck: complete anatomical-left profile pointing image-right, visible grounded feet, calibration outfit, straight loose HAIRSTYLE_A with no gathered structure, and Body01/06-aligned body/leg geometry are present.

## Promotion decision

The user explicitly instructed: “登记”. The candidate raster was moved unchanged to `OWNER_BODY_04_LEFT_SIDE_CANON_002`, now the active Body04 Master. Canon 001 was returned unchanged to its original v002 candidate directory. Full `owner_v1.0` remains unlocked.
