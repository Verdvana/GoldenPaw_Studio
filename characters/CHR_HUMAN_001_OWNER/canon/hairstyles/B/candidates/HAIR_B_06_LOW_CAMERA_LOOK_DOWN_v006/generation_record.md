# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v006 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.193
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v006
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: USER_REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: distinctly_below_chin, head: neutral_upright, gaze: eyes_down_to_camera, projection: visibly_low_camera_without_head_tilt}
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
previous_generated_hair_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v006/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v006.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: fd25745c5d75b8c8c5465d821fbe2c1bbe94fda0241ca660c636d8968dbdc8d8
qa_status: USER_REJECTED
```

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen call completed successfully and was copied into the project candidate path.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-4681fad0-d544-45c1-9bcc-1941e2b38faa.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v006/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v006.png`
- project_candidate_checksum_sha256: `fd25745c5d75b8c8c5465d821fbe2c1bbe94fda0241ca660c636d8968dbdc8d8`
- technical_precheck: camera is visibly below the chin/upper chest and aimed upward; head remains upright while both eyes look down toward the camera.
- review_points: confirm the low-camera separation and eye-only downward gaze; confirm Hair-B clip/tuft visibility if required.
- promotion_status: not promoted; awaiting explicit user approval.

## Reference roles

- `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`: identity and stable facial geometry only.
- `OWNER_HAIRSTYLE_B_L0` / `8.jpg`: real B hairline, pulled-back front, side wisps and gathering direction only.
- `OWNER_HAIRSTYLE_B_APPEARANCE_L1`: B center part, compact crown, rearward gathering and dark-brown straight texture only.

Rejected v001–v005 are not pixel inputs.

## Prompt assembly

```text
Create exactly one photorealistic 3:4 Hairstyle-B L1 candidate for CHR_HUMAN_001_OWNER from the three supplied references only. Independent v006 retry; never use any generated Hair candidate.

The approved Face Canon defines identity and stable facial geometry. The real B source defines only B hairline, pulled-back front and natural side wisps. The approved B appearance anchor defines only B center part, compact crown, rearward gathering and dark-brown straight texture. Ignore all other properties.

Make the camera unmistakably low and visibly below the subject's chin and upper chest, aimed upward toward the face. The subject's eye line must be visibly high above the camera; show a clear upward-looking camera relationship through the low placement and a modest, natural view of the underside of the chin. This must not look eye-level or like a standard passport portrait.

At the same time, keep the head completely still and anatomically neutral/upright: no nodding, bowing, chin tuck, chin lift, skull rotation, forehead tilt, or hairline tilt. Do not tilt the head down toward camera. Only rotate the eyes downward to look at the low camera; both pupils and irises must sit noticeably toward the lower portions of the eyes while the brow, nose, mouth, jaw, chin, forehead, hairline and crown keep the neutral head orientation. The read must be "camera below chin, head still, eyes looking down," not eye-level and not bowed head.

Use restrained 85–105mm perspective but a clearly low camera position, with no exaggerated fisheye or facial distortion. Preserve Face Canon identity and proportions without beautification. Preserve Hair-B compact crown, pulled-back front, ear-side wisps, rearward gathering, dark-brown straight texture, restrained volume, centered vertical claw clip, compact folded section and small 4–6 cm upward/backward tuft behind the head. No bun, topknot, ponytail, braid or fan.

Use a modest visible upper portion of the pink Calibration Outfit on a plain neutral gray-white studio background. Natural hair and skin texture, relevant ear-side hair edges in frame. No props, scenery, text, logo, watermark, collage or multiple views. Produce one REVIEW_REQUIRED image only.
```
