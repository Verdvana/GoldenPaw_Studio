# BODY_02_LEFT_3Q_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.233
identity_md_revision: draft_0.185
asset_id: BODY_02_LEFT_3Q
candidate_id: BODY_02_LEFT_3Q_v003
gate: "Gate 3 — Body Canon"
generation_tool: built_in_image_gen
use_case: identity-preserve
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
reference_set_ids:
  - OWNER_FACE_LEFT_3Q_NEUTRAL_RECOVERY_V1
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_BODY_REAR_CURRENT_LOWER_BODY_FACE_HAIR_EXCLUDED_DERIVATIVE
generation_inputs:
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", responsibility: "source-derived recognizable identity, facial relationships, adult age appearance, neutral skin and expression baseline", must_not_define: "hair, body, clothing, lighting or background"}
  - {asset_id: L0_OWNER_013, path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/15.jpg", responsibility: "real same-person anatomical-left three-quarter depth and face-points-image-left geometry", must_not_define: "identity priority, smile, gaze, makeup, retouching, skin tone, hair, clothing, lighting or background"}
  - {asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png", responsibility: "HAIRSTYLE_A only", must_not_define: "face, skin, skull, body, clothing, light or background"}
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", responsibility: "current Body01 neck-below front geometry: 168 cm / 60 kg scale, torso, waist/hip, leg and foot geometry", must_not_define: "face, identity, hair, clothing design, hosiery material, lighting or background"}
  - {asset_id: OWNER_BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_CROP.png", responsibility: "current Body06 rear lower-body cross-view alignment", must_not_define: "face, skin identity, hair, clothing design, hosiery material, lighting or background"}
qa_comparison_only:
  - {asset_id: BODY_02_LEFT_3Q_v002, path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_02_LEFT_3Q_v002/BODY_02_LEFT_3Q_v002.png", purpose: "user-feedback comparison only; never a generation input"}
  - {asset_id: OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity comparison only"}
reference_count: 5
previous_ai_body_candidate_count: 0
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4 preferred"
seed: null
settings: {tool: built_in_image_gen, output: single candidate}
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_02_LEFT_3Q/OWNER_BODY_02_LEFT_3Q_CANON_002.png
qa_status: PASS_USER_APPROVED
```

## Generation output

- generated_at: 2026-09-18
- source_tool_output: `/home/verdvana/.codex/generated_images/01a0b49f-870e-7ea0-ae0e-60b4626f5cef/exec-70d84a1f-7cc5-42f5-a197-c73bf711dc02.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_02_LEFT_3Q_v003/BODY_02_LEFT_3Q_v003.png` before promotion
- copy_operation: `COPY`; the source tool output remains untouched.
- dimensions: `1086x1448`, exact 3:4
- sha256: `8f887e81ffe517099fb9af25cf010f8dc33deeace9f8f55253b4641ac8876db1`
- status: superseded by the approval record below.

## User approval and promotion

- approval_evidence: `登记`
- approved_at: 2026-09-19
- approver: user
- approved_component: `OWNER_BODY_02_LEFT_3Q_CANON_002`
- promotion_operation: `MOVE`, unchanged source raster; no duplicate candidate raster retained.
- approved_path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_02_LEFT_3Q/OWNER_BODY_02_LEFT_3Q_CANON_002.png`
- approved_sha256: `8f887e81ffe517099fb9af25cf010f8dc33deeace9f8f55253b4641ac8876db1`

## User-directed correction

`BODY_02_LEFT_3Q_v002` is not used as a generation input. The user directs exactly two changes for v003:

1. Restore a neutral cervical alignment: head centered over the neck and upper torso, without a forward head posture or anterior neck lean.
2. Bring each lower-leg axis forward and closer to its corresponding thigh axis: knee center, shin midline and ankle center should be nearly collinear in the three-quarter projection, with no visible backward set, bowing or outward calf drift.

All other approved/current geometry and appearance constraints remain unchanged.

## Prompt assembly

```text
Use case: identity-preserve. Create one non-sexual, neutral full-length clinical character-proportion calibration photograph of the same adult woman in anatomical-left three-quarter view, about 35–40 degrees toward image-left. Inputs 1–3 solely reconstruct source-derived left-three-quarter face identity and Hairstyle A; Inputs 4–5 solely constrain current registered front/rear body geometry. Do not use generated imagery to define the face.

Keep the same adult 168 cm / approximately 60 kg scale, torso length, waist-to-hip relationship, hip breadth, natural thigh/calf volume, heel/foot scale, neutral expression, Calibration Outfit, lighting and framing. Head, shoulders, ribcage, pelvis, knees and feet turn together in a stable neutral stance; no contrapposto, crossed limbs, fashion pose or torso twist.

Correction 1: neutral cervical alignment. The head is centered directly over the neck and upper torso, chin level, no forward head posture, no anterior neck lean, no neck extension or compression.

Correction 2: lower legs. From the three-quarter view, bring both lower legs slightly forward so each knee center, shin midline and ankle center is nearly collinear and directly under the corresponding thigh axis. Calves must continue the thigh direction with natural volume: no visible backward lower-leg set, outward bowing, lateral calf drift or O-shaped leg line. Both feet remain fully flat and naturally grounded.

Wear a plain pink athletic one-piece calibration garment, continuous pale 15D closed-foot matte/velvet pantyhose and no footwear. Exact 3:4, complete head/hair/hands/feet, level 70–85mm-equivalent camera, neutral gray-white seamless studio and soft even clinical 5200–5600K light. No props, text, watermark, collage, glamour posing or sexualized presentation. One REVIEW_REQUIRED candidate only.
```
