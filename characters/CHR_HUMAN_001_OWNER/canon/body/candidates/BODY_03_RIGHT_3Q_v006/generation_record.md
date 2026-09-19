# BODY_03_RIGHT_3Q_v006 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.233
identity_md_revision: draft_0.185
asset_id: BODY_03_RIGHT_3Q
candidate_id: BODY_03_RIGHT_3Q_v006
gate: "Gate 3 — Body Canon"
generation_tool: built_in_image_gen
use_case: identity-preserve
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
reference_set_ids:
  - OWNER_FACE_RIGHT_3Q_NEUTRAL_RECOVERY_V1
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_BODY_REAR_CURRENT_LOWER_BODY_FACE_HAIR_EXCLUDED_DERIVATIVE
generation_inputs:
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", responsibility: "source-derived recognizable identity, fine facial relationships, adult age and neutral skin baseline", must_not_define: "hair, body, clothing, lighting or background"}
  - {asset_id: L0_OWNER_012, path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/14.jpg", responsibility: "anatomical-right/image-right direction, natural right-side asymmetry and coarse depth only", must_not_define: "fine geometry, identity priority, skin tone, phone perspective, hair, clothing, lighting or background"}
  - {asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png", responsibility: "HAIRSTYLE_A only", must_not_define: "face, skin, skull, body, clothing, light or background"}
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", responsibility: "current front body geometry: 168 cm / 60 kg scale, torso, waist/hip, leg width, near-straight axes, foot scale and stance", must_not_define: "face, identity, hair, clothing design, hosiery material, lighting or background"}
  - {asset_id: OWNER_BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_CROP.png", responsibility: "current rear lower-body cross-view alignment: hip, thigh/calf, lower-leg, heel and foot geometry", must_not_define: "face, skin identity, hair, clothing design, hosiery material, lighting or background"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_03_RIGHT_3Q_NEUTRAL/OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and image-right projection comparison only"}
  - {asset_id: OWNER_BODY_03_RIGHT_3Q_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_03_RIGHT_3Q_v005/BODY_03_RIGHT_3Q_v005.png", purpose: "post-generation continuity comparison only; never a generation input"}
reference_count: 5
previous_ai_body_candidate_count: 0
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4 preferred"
seed: null
settings: {tool: built_in_image_gen, output: single candidate}
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_03_RIGHT_3Q/OWNER_BODY_03_RIGHT_3Q_CANON_002.png
qa_status: PASS_USER_APPROVED
```

## Generation output

- generated_at: 2026-09-19
- source_tool_output: `/home/verdvana/.codex/generated_images/01a0b49f-870e-7ea0-ae0e-60b4626f5cef/exec-361f5808-4e86-471e-9b6d-9476a1726dcd.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_03_RIGHT_3Q_v006/BODY_03_RIGHT_3Q_v006.png` before promotion
- copy_operation: `COPY`; the source tool output remains untouched.
- dimensions: `1086x1448`, exact 3:4
- sha256: `2a18d38fb4441d50427753263700699a6ce2f571ae5a497720c8c4158fd658a7`
- status: superseded by the approval record below.

## User approval and promotion

- approval_evidence: `登记`
- approved_at: 2026-09-19
- approver: user
- approved_component: `OWNER_BODY_03_RIGHT_3Q_CANON_002`
- promotion_operation: `MOVE`, unchanged source raster; no duplicate candidate raster retained.
- approved_path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_03_RIGHT_3Q/OWNER_BODY_03_RIGHT_3Q_CANON_002.png`
- approved_sha256: `2a18d38fb4441d50427753263700699a6ce2f571ae5a497720c8c4158fd658a7`

## User-directed objective

Regenerate Body03 as a fresh independent candidate. Preserve Body01 and Body06's current straight lower-leg direction and the same cross-view body proportions: 168 cm / approximately 60 kg scale, torso length, waist-to-hip relationship, hip breadth, natural thigh/calf volume, heel/foot scale and neutral standing geometry.

## Prompt assembly

```text
Use case: identity-preserve. Create one non-sexual, neutral full-length clinical character-proportion calibration photograph of the same adult woman in anatomical-right three-quarter view, about 35–40 degrees toward image-right. Inputs 1–3 solely reconstruct source-derived right-three-quarter face identity and Hairstyle A; Inputs 4–5 solely constrain current registered Body01 and Body06 geometry. Do not use generated imagery to define the face.

The anatomical right face and body planes are principally visible and the nose points image-right. Keep eyes naturally toward the camera, mouth closed, expression neutral, eye-level head and a softly rounded chin. Head, shoulders, ribcage, pelvis, knees and feet turn together as one stable neutral unit: no torso twist, contrapposto, fashion pose or crossed limbs.

Match the face-excluded Body01/Body06 geometry: same 168 cm / approximately 60 kg adult scale, torso length, waist placement, waist-to-hip transition, hip breadth, natural thigh/calf volume and heel/foot scale. Keep each lower leg nearly collinear with its corresponding thigh axis: knee center, shin midline and ankle center directly aligned in the three-quarter projection, no backward set, bowing, outward calf drift or O-shaped leg line. Both feet fully flat and naturally grounded.

Wear a plain pink athletic one-piece calibration garment, continuous pale 15D closed-foot matte/velvet pantyhose and no footwear. Exact 3:4, complete head/hair/hands/feet, level 70–85mm-equivalent camera, neutral gray-white seamless studio and soft even clinical 5200–5600K light. No props, text, watermark, collage, glamour posing or sexualized presentation. One REVIEW_REQUIRED candidate only.
```
