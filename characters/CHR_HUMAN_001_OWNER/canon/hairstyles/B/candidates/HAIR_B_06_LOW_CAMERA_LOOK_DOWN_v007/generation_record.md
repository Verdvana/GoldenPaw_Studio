# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v007 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.194
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v007
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: USER_REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: low_below_eye_line, head: fixed_neutral_upright, gaze: eyes_only_down_to_camera, projection: low_camera_without_head_pitch}
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
previous_generated_hair_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v007/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v007.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: ef82445267f3adba6adaecab9aa48012a4d72633744dd094261effce9b805d0c
qa_status: USER_REJECTED
```

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen call completed successfully and was copied into the project candidate path.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-326ffb55-8054-48e4-9d24-7a86eacd170c.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v007/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v007.png`
- project_candidate_checksum_sha256: `ef82445267f3adba6adaecab9aa48012a4d72633744dd094261effce9b805d0c`
- technical_precheck: head remains upright and fixed; camera is visibly lower and both eyes are directed downward toward it without a bowed-head pose.
- review_points: confirm the intended fixed-head/eye-only gaze relationship and low-camera height separation.
- promotion_status: not promoted; awaiting explicit user approval.

## Prompt assembly

```text
Create exactly one photorealistic 3:4 Hairstyle-B L1 candidate for CHR_HUMAN_001_OWNER from the three supplied references only. Independent v007 retry; do not use any generated Hair candidate.

Reference 1 approved Face Canon defines identity and stable facial geometry. Reference 2 real B source 8.jpg defines only B's pulled-back hairline and natural side wisps. Reference 3 approved B appearance anchor defines only B's center part, compact crown, rearward gathering and dark-brown straight texture.

Composition requirement: put the camera in a clearly lower position, below the subject's eyes and around the upper-chest/sternum level, looking slightly upward. The low camera position must be visible in the composition, but the subject's head must remain exactly where it would be in a normal upright portrait. The head is fixed and still: no looking down with the head, no nodding, no bowing, no chin tuck, no chin lift, no skull rotation, no forehead tilt, no hairline tilt. The line from the forehead through the nose, mouth, jaw and chin remains a normal neutral upright head alignment.

Only the eyes move: both eyeballs rotate downward to look at the camera below them. Make the pupils/irises visibly lowered within the eye openings while the face, nose, mouth and chin remain neutral. The intended read is unmistakably: "head stays still, camera is down low, woman looks down at it with her eyes only." Do not make an eye-level portrait. Do not make a bowed-head portrait. Do not use a low camera plus a downward-tilted face.

Use a natural 85–105mm lens and a moderate camera height separation; show only a subtle natural underside of the chin, never a dramatic under-chin perspective. Preserve Face Canon identity and proportions without beautification. Preserve Hair-B compact crown, pulled-back front, natural ear-side wisps, smooth rearward gathering, dark-brown straight texture, centered vertical claw clip, compact folded section and small 4–6 cm upward/backward tuft behind the head. No bun, topknot, ponytail, braid or fan.

Use a modest visible upper portion of the pink Calibration Outfit on a plain neutral gray-white studio background. Natural hair and skin texture, relevant ear-side hair edges in frame. No props, scenery, text, logo, watermark, collage or multiple views. Produce one REVIEW_REQUIRED image only.
```
