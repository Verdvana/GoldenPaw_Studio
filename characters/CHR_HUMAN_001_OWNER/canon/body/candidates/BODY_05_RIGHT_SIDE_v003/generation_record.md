# BODY_05_RIGHT_SIDE_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.233
identity_md_revision: draft_0.185
asset_id: BODY_05_RIGHT_SIDE
candidate_id: BODY_05_RIGHT_SIDE_v003
gate: "Gate 3 — Body Canon"
generation_tool: built_in_image_gen
use_case: identity-preserve
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
reference_set_ids: [OWNER_FACE_RIGHT_PROFILE_NEUTRAL_RECOVERY_V1, OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE, OWNER_BODY_REAR_CURRENT_LOWER_BODY_FACE_HAIR_EXCLUDED_DERIVATIVE]
generation_inputs:
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", sha256: d98019128bfa974a102813da52b4a2905ec4aa7c95eb5222a163e419f287e74d, responsibility: "source-derived identity and neutral skin baseline", must_not_define: "hair, body, clothing, lighting or background"}
  - {asset_id: L0_OWNER_009, path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/11.jpg", sha256: 948a092a360192af3f8718b27e35562ca5e14a21022e1161f8449be75b830a46, responsibility: "genuine anatomical-right profile pointing image-left and view-dependent profile geometry only", must_not_define: "identity priority, skin, hair, clothing, lighting or background"}
  - {asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png", sha256: 6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd, responsibility: "HAIRSTYLE_A only: long, straight, loose, near-center-parted hair", must_not_define: "face, body, clothing, lighting or background"}
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b, responsibility: "current front body geometry, straight leg axes, scale and stance", must_not_define: "face, identity, hair, clothing design, hosiery material, lighting or background"}
  - {asset_id: OWNER_BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_CROP.png", sha256: c3ce9451c3c328181a715f9efb4475f8ac69bf17259c51c2c9f513822944b10e, responsibility: "current rear lower-body cross-view geometry", must_not_define: "face, identity, hair, clothing design, hosiery material, lighting or background"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_05_RIGHT_PROFILE_NEUTRAL/OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and true-profile comparison only"}
  - {asset_id: OWNER_BODY_05_RIGHT_SIDE_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_05_RIGHT_SIDE/OWNER_BODY_05_RIGHT_SIDE_CANON_001.png", purpose: "post-generation continuity comparison only"}
reference_count: 5
previous_ai_body_candidate_count: 0
aspect_ratio: "3:4"
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_05_RIGHT_SIDE_v003/BODY_05_RIGHT_SIDE_v003.png
qa_status: PASS_USER_APPROVED
```

Create exactly one non-sexual clinical full-length technical reference at an exact 90-degree anatomical-right profile: face and whole body point image-left, one eye principally visible, no torso twist. Inputs 1–2 reconstruct only source-derived profile identity; Input 3 is the sole hairstyle authority; Inputs 4–5 constrain only current Body01/06 geometry. Preserve the 168 cm / approximately 60 kg scale, torso length, waist-to-hip relationship, natural thigh/calf volume, straight lower-leg direction, heel and foot scale. Keep head, torso, pelvis, knees and feet in one true side direction; knees, shins and ankles remain aligned with their thigh axes. Both feet are naturally grounded. Wear the fixed plain pink high-cut athletic one-piece, continuous pale 15D matte/velvet closed-foot pantyhose and no footwear. Hair is mandatory HAIRSTYLE_A: long, straight, loose dark-brown hair with a near-center part, low-to-medium crown volume, long face-side strands, and tapered ends falling below the chest. The hair must be fully down and unbound. Absolutely no updo, bun, chignon, ponytail, braid, hair clip, barrette, pin, tie, or any gathered/secured hair. Exact 3:4, complete figure, level 70–85mm camera, neutral gray-white studio, soft even light. No props, text, watermark, glamour posing or sexualized presentation. Output one REVIEW_REQUIRED candidate only.

## Generation result and technical precheck

- generated_at: 2026-09-19
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_05_RIGHT_SIDE_v003/BODY_05_RIGHT_SIDE_v003.png`
- dimensions: `1086x1448`, exact 3:4
- sha256: `93a2dd69e4789878067943cca8b5f08ec849a39c140ed170f7e24d3e3e13d74b`
- result: `USER_REVIEW_REQUIRED__TECHNICAL_PRECHECK_PASS`
- precheck: exact right-side orientation; full figure and grounded feet are visible; fixed calibration outfit is present. Visible hair is long, straight, loose and near-center-parted, with no bun, gathered structure, clip or other hair accessory.

## Promotion decision

The user explicitly instructed: “用上一版本登记吧，v003”. The candidate raster was moved unchanged to `OWNER_BODY_05_RIGHT_SIDE_CANON_002`; it is the current active right-side Body05 Master. Canon 001 was returned unchanged to its original v001 candidate directory. Full `owner_v1.0` remains unlocked.
