# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v013 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.200
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v013
gate: "Gate 4 — Hairstyle Canon"
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: approved_A_low_camera_composition, head: approved_A_fixed_neutral_relation, gaze: approved_A_direct_low_camera_gaze, hair: B_replacement}
reference_set_ids: [OWNER_HAIR_A_LOW_CAMERA_LOOK_DOWN_CANON_L1, OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 4
previous_generated_hair_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v013/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v013.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: f341f46cb0272ca0451cded4380cb6588f124b4cdfe822103d846bfee02236e3
qa_status: REVIEW_REQUIRED
```

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen edit completed successfully and was copied into the project candidate path.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-09f6d105-473d-4ae2-b92e-2e6e932f6e28.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v013/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v013.png`
- project_candidate_checksum_sha256: `f341f46cb0272ca0451cded4380cb6588f124b4cdfe822103d846bfee02236e3`
- technical_precheck: candidate registered at user's direction; low-camera composition and gaze remain subject to review.
- promotion_status: registered as candidate only; not promoted to Canon.

## Prompt assembly

```text
Edit the supplied approved Hair-A low-camera Canon composition to create one photorealistic 3:4 Hairstyle-B candidate. Preserve the source composition exactly: preserve the camera height, low-angle perspective, head position, upright head posture, and the subject's direct eye contact with the low camera. Do not regenerate or reinterpret the head, face, camera or gaze.

Change only the hairstyle. Remove the Hair-A hairstyle and replace it with Hairstyle-B using the supplied real B hair reference and approved B appearance anchor: pulled-back front, compact dark-brown straight hair, restrained part, side wisps, rearward gathering and small rear clip-held tuft. Hair-B must follow the same low-camera perspective as the preserved source composition, with reduced crown exposure and no broad top plane.

Use the approved Face Canon only to preserve identity if needed. Do not alter facial identity, facial proportions, expression, head angle, eye direction, camera height, framing, outfit or background. Do not use any previous generated candidate. No new pose, no head tilt, no high-camera reconstruction, no eye-level gaze, no extra views, no text or watermark. Output one REVIEW_REQUIRED candidate only.
```
