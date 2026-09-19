# BODY_02_LEFT_3Q_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.233
identity_md_revision: draft_0.185
asset_id: BODY_02_LEFT_3Q
candidate_id: BODY_02_LEFT_3Q_v002
gate: "Gate 3 — Body Canon"
generation_tool: built_in_image_gen
use_case: identity-preserve
status: PLANNED
approval_status: REVIEW_REQUIRED
reference_set_ids:
  - OWNER_FACE_LEFT_3Q_NEUTRAL_RECOVERY_V1
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_BODY_REAR_CURRENT_LOWER_BODY_FACE_HAIR_EXCLUDED_DERIVATIVE
generation_inputs:
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", sha256: d98019128bfa974a102813da52b4a2905ec4aa7c95eb5222a163e419f287e74d, responsibility: "source-derived recognizable identity, facial relationships, adult age appearance, neutral skin and expression baseline", must_not_define: "hair, body, clothing, lighting or background"}
  - {asset_id: L0_OWNER_013, path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/15.jpg", sha256: 1851e8decaa3430f127c3e720f7fba8bb119370008ef7795313fd6e76b396af0, responsibility: "real same-person anatomical-left three-quarter depth, nose projection, cheek-to-jaw depth, visible-ear placement and face-points-image-left geometry", must_not_define: "identity priority, smile, gaze, makeup, retouching, skin tone, hair, clothing, lighting or background"}
  - {asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png", sha256: 6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd, responsibility: "HAIRSTYLE_A only — near-center part, long straight loose dark-brown silhouette, face-framing panels and tapered ends", must_not_define: "face, skin, skull, body, clothing, light or background"}
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b, responsibility: "current Body01 neck-below front geometry: 168 cm / 60 kg scale, shoulder/torso length, waist/hip ratio, leg width, straight axes, foot scale and neutral stance", must_not_define: "face, identity, hair, clothing design, hosiery material, lighting or background"}
  - {asset_id: OWNER_BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_CROP.png", sha256: c3ce9451c3c328181a715f9efb4475f8ac69bf17259c51c2c9f513822944b10e, responsibility: "current Body06 rear lower-body cross-view alignment: hip, thigh/calf, lower-leg, heel and foot geometry only", must_not_define: "face, skin identity, hair, clothing design, hosiery material, lighting or background"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg", purpose: "post-generation face identity, left-three-quarter projection and face-contamination comparison only"}
  - {asset_id: OWNER_BODY_02_LEFT_3Q_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_02_LEFT_3Q_v001/BODY_02_LEFT_3Q_v001.png", purpose: "post-generation continuity comparison only; never a generation input"}
reference_count: 5
previous_ai_body_candidate_count: 0
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4 preferred"
seed: null
settings: {tool: built_in_image_gen, output: single candidate}
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_02_LEFT_3Q_v002/BODY_02_LEFT_3Q_v002.png
qa_status: TECHNICAL_PRECHECK_COMPLETE__USER_REVIEW_REQUIRED
```

## Attempt 1 — no output

- attempted_at: 2026-09-18
- result: `NO_OUTPUT_MODERATION_BLOCKED`
- moderation_stage: output
- reported_category: sexual
- request_id: `83e2377e-c0b6-4107-9ef7-67993ba319c6`
- raster_created: false
- consequence: no candidate image, checksum, or visual feedback exists; no attribute is written back to any Canon or reference set.
- retry_scope: one neutral clinical-calibration retry using the same five declared inputs, with a shorter non-editorial prompt and no new visual references.

## Attempt 2 — candidate output

- generated_at: 2026-09-18
- result: `OUTPUT_CREATED`
- source_tool_output: `/home/verdvana/.codex/generated_images/01a0b49f-870e-7ea0-ae0e-60b4626f5cef/exec-a64d209a-aaaf-442f-90c5-7b8665057908.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_02_LEFT_3Q_v002/BODY_02_LEFT_3Q_v002.png`
- copy_operation: `COPY`; the source tool output remains untouched.
- dimensions: `1086x1448`, exact 3:4
- sha256: `f951caddcd3a5a7547b2a3c59f0fe4a6d3192d6a9a4f1461f4c3c29202b012c9`
- status: `REVIEW_REQUIRED`; no promotion or Canon routing change has occurred.

## Prompt assembly

```text
Use case: identity-preserve
Asset type: BODY_02_LEFT_3Q_v002, L1 technical body-calibration candidate for CHR_HUMAN_001_OWNER.

Create exactly one photorealistic, non-sexual, neutral full-length technical reference of the same adult woman in anatomical-left three-quarter view, approximately 35–40 degrees toward image-left. Image 1 defines only source-derived recognizable facial identity, adult age, neutral skin and expression baseline. Image 2 defines only the real same-person left-three-quarter facial depth and face-points-image-left geometry. Image 3 defines only Hairstyle A. Image 4 defines only the current registered Body01 neck-below front geometry. Image 5 defines only the current registered Body06 rear lower-body geometry. Do not let any input define a property outside its declared role.

The anatomical left face and body planes are principally visible and the nose points image-left. Keep eyes naturally toward the camera, mouth closed, expression neutral, eye-level head, and a 70–85mm-equivalent level camera. Preserve Image 1 identity; Image 2 may solve only view-dependent depth. Keep the face natural: slightly lower softer cheekbone, softly rounded chin terminal curve without changing chin length or jaw width, and gentle alert gaze without changing eye size, shape, spacing or pupil placement. Do not use AI face or body imagery to define the face.

Turn head, shoulders, ribcage, pelvis, knees and feet together as one stable neutral body unit: no torso twist, contrapposto, fashion pose or crossed limbs. Match Images 4 and 5 as cross-view geometry constraints: the same 168 cm / approximately 60 kg adult scale, torso length, waist placement, waist-to-hip transition, hip breadth, natural thigh/calf volume, near-straight knee-shin-ankle axes, heel and foot scale. Do not slim, widen, shorten, lengthen, shrink the head or redesign any body mass.

Use the fixed Calibration Outfit: plain pink high-cut one-piece athletic swimsuit, continuous slightly-whitish light-nude 15D matte/velvet sheer pantyhose from waist through hips, legs, ankles, heels, insteps and every toe, no shoes. Burgundy toenail polish may be softly visible only beneath the continuous textile. Both feet are fully flat and naturally grounded; hands, fingers, heels and toes are fully visible. No bare toes, toe seam, reinforced toe, ankle cutoff, white ring, hard material boundary, latex, PVC, plastic, wet coating or body paint.

HAIRSTYLE_A only: near-center part, close-to-scalp roots, controlled low crown volume, long straight loose dark-brown hair, face-framing panels and tapered ends. Exact 3:4 portrait: complete head, hair, hands, heels and toes with 5–8% breathing room. Neutral gray-white seamless studio, soft even 5200–5600K illumination, no props, furniture, scenery, text, watermark, collage or multiple views. Produce one REVIEW_REQUIRED candidate only; do not label or imply Canon approval.
```
