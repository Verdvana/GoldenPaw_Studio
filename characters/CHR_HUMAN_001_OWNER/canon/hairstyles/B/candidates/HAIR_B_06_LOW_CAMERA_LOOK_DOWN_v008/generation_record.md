# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v008 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.195
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v008
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: USER_REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: low_below_eye_line, head: naturally_upright_fixed, gaze: visibly_eyes_down_targeting_camera, projection: low_camera_without_head_pitch}
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
previous_generated_hair_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v008/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v008.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: 2633ee7cfcf52e7e624baafe9aa71439ee0a3922a006611099e51d01a2d9dfac
qa_status: USER_REJECTED
```

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen call completed successfully and was copied into the project candidate path.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-768ad789-9b48-47e4-a726-7ec2fb5ade87.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v008/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v008.png`
- project_candidate_checksum_sha256: `2633ee7cfcf52e7e624baafe9aa71439ee0a3922a006611099e51d01a2d9dfac`
- technical_precheck: low camera is separated below the eye line; head is held neutral/upright; both eyes visibly direct downward toward the camera.
- review_points: user to verify that the head is truly fixed and that the eye-only downward gaze is unmistakable.
- promotion_status: not promoted; awaiting explicit user approval.

## Prompt assembly

```text
Create exactly one photorealistic 3:4 Hairstyle-B L1 candidate for CHR_HUMAN_001_OWNER from the three supplied references only. Independent v008 retry; do not use any generated Hair image.

Reference 1 approved Face Canon defines identity and stable facial geometry. Reference 2 real B source 8.jpg defines only B pulled-back hairline and natural side wisps. Reference 3 approved B appearance anchor defines only B center part, compact crown, rearward gathering and dark-brown straight texture.

The head posture is locked: keep the head naturally upright and completely still, exactly like a person standing normally. The vertical centerline of the forehead, nose, lips and chin must remain straight and neutral; jaw and chin must not angle toward or away from the camera. No nodding, bowing, chin tuck, chin lift, skull rotation, forehead tilt, or hairline tilt. Do not create low-camera feeling by changing the head pose.

Place the camera physically low, well below the eyes and below the chin line, looking gently upward. The camera must not be at eye level. Make the low placement visible through a mild upward view of the lower face, while keeping the head's natural upright outline.

Only the eyes move. Both eyes must visibly rotate downward and clearly target the camera below them: pupils/irises sit in the lower half of the visible eye openings, with the gaze direction converging downward toward the same low point directly in front of the subject. Do not let the eyes look straight at the viewer or toward the horizon. The final read must be unambiguous: naturally upright head, low camera, eyes looking down at that camera.

Use a natural 85–105mm lens, moderate perspective, no fisheye or dramatic distortion. Preserve Face Canon identity and proportions without beautification. Preserve Hair-B compact crown, pulled-back front, natural ear-side wisps, smooth rearward gathering, dark-brown straight texture, centered vertical claw clip, compact folded section and small 4–6 cm upward/backward tuft behind the head. No bun, topknot, ponytail, braid or fan.

Use a modest visible upper portion of the pink Calibration Outfit on a plain neutral gray-white studio background. Natural hair and skin texture, relevant ear-side hair edges in frame. No props, scenery, text, logo, watermark, collage or multiple views. Produce one REVIEW_REQUIRED image only.
```
