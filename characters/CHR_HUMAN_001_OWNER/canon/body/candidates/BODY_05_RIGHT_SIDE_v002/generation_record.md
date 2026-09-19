# BODY_05_RIGHT_SIDE_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.233
identity_md_revision: draft_0.185
asset_id: BODY_05_RIGHT_SIDE
candidate_id: BODY_05_RIGHT_SIDE_v002
gate: "Gate 3 — Body Canon"
generation_tool: built_in_image_gen
use_case: identity-preserve
status: PLANNED
approval_status: REVIEW_REQUIRED
reference_set_ids: [OWNER_FACE_RIGHT_PROFILE_NEUTRAL_RECOVERY_V1, OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE, OWNER_BODY_REAR_CURRENT_LOWER_BODY_FACE_HAIR_EXCLUDED_DERIVATIVE]
generation_inputs:
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", responsibility: "source-derived identity and neutral skin baseline", must_not_define: "hair, body, clothing, lighting or background"}
  - {asset_id: L0_OWNER_009, path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/11.jpg", responsibility: "genuine anatomical-right profile pointing image-left and view-dependent profile geometry only", must_not_define: "identity priority, skin, hair, clothing, lighting or background"}
  - {asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png", responsibility: "HAIRSTYLE_A only", must_not_define: "face, body, clothing, lighting or background"}
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", responsibility: "current front body geometry, straight leg axes, scale and stance", must_not_define: "face, identity, hair, clothing design, hosiery material, lighting or background"}
  - {asset_id: OWNER_BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_CROP.png", responsibility: "current rear lower-body cross-view geometry", must_not_define: "face, identity, hair, clothing design, hosiery material, lighting or background"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_05_RIGHT_PROFILE_NEUTRAL/OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and true-profile comparison only"}
  - {asset_id: OWNER_BODY_05_RIGHT_SIDE_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_05_RIGHT_SIDE/OWNER_BODY_05_RIGHT_SIDE_CANON_001.png", purpose: "post-generation continuity comparison only"}
reference_count: 5
previous_ai_body_candidate_count: 0
aspect_ratio: "3:4"
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_05_RIGHT_SIDE_v002/BODY_05_RIGHT_SIDE_v002.png
qa_status: TECHNICAL_PRECHECK_FAILED__HAIRSTYLE_A_DRIFT
```

Create one non-sexual clinical full-length technical reference at an exact 90-degree anatomical-right profile: face and whole body point image-left, one eye principally visible, no torso twist. Inputs 1–3 reconstruct only source-derived profile identity and Hairstyle A; Inputs 4–5 constrain only current Body01/06 geometry. Preserve the 168 cm / approximately 60 kg scale, torso length, waist-to-hip relationship, natural thigh/calf volume, straight lower-leg direction, heel and foot scale. Keep head, torso, pelvis, knees and feet in one true side direction; knees, shins and ankles remain aligned with their thigh axes. Both feet are naturally grounded. Wear the fixed plain pink high-cut athletic one-piece, continuous pale 15D matte/velvet closed-foot pantyhose and no footwear. Exact 3:4, complete figure, level 70–85mm camera, neutral gray-white studio, soft even light. No props, text, watermark, glamour posing or sexualized presentation. Output one REVIEW_REQUIRED candidate only.

## Generation result and technical precheck

- generated_at: 2026-09-19
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_05_RIGHT_SIDE_v002/BODY_05_RIGHT_SIDE_v002.png`
- dimensions: `1086x1448`, exact 3:4
- sha256: `08e92359b94e7b11c5270e045dc22ccf39e0f7efd6ab4b6926b5f387922358f0`
- result: `USER_REVIEW_REQUIRED__TECHNICAL_FAIL`
- failure: the output shows an updo/bun and a hair clip, which violates the required long, straight, loose `HAIRSTYLE_A`. It is ineligible for approval, downstream use, or any future generation input.
