# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v009 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.196
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v009
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: USER_REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: low_below_eye_line, head: natural_standing_neutral, gaze: eyes_locked_down_to_camera, projection: low_camera_head_fixed}
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1, OWNER_HAIR_A_LOW_CAMERA_LOOK_DOWN_CANON_L1]
reference_count: 4
previous_generated_hair_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v009/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v009.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: 865cf6818992d88bbe9c68ddbb3ede1b1b932d270a7a919b8f5448157aa70b48
qa_status: USER_REJECTED
```

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen call completed successfully and was copied into the project candidate path.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-001dcca3-5a93-43ed-bb7b-403e769f9246.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v009/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v009.png`
- project_candidate_checksum_sha256: `865cf6818992d88bbe9c68ddbb3ede1b1b932d270a7a919b8f5448157aa70b48`
- technical_precheck: low camera relationship is present; head is intended to remain upright; both eyes are directed downward toward the low camera.
- review_points: user must verify eye targeting and that the head is not lowered.
- promotion_status: not promoted; awaiting explicit user approval.

## Reference roles

- `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`: identity and stable facial geometry only.
- `OWNER_HAIRSTYLE_B_L0` / `8.jpg`: real B hairline, pulled-back front and side wisps only.
- `OWNER_HAIRSTYLE_B_APPEARANCE_L1`: B center part, compact crown and rearward gathering only.
- `OWNER_HAIR_A_LOW_CAMERA_LOOK_DOWN_CANON_L1`: scoped visual aid for the relationship of a low camera and downward eye gaze only; must not define Hair-A pixels, Hair-B pixels, identity or head tilt.

Rejected v001–v008 are not pixel inputs.

## Prompt assembly

```text
Create exactly one photorealistic 3:4 Hairstyle-B L1 candidate for CHR_HUMAN_001_OWNER from the four supplied references only. Independent v009 retry; do not use any generated Hair image.

Face Canon defines identity and stable facial geometry. Real B source and approved B anchor define Hair-B only. The approved Hair-A low-camera image is a scoped geometry aid only: use it only to understand a low camera with downward eye gaze, never its hair pixels, face identity, head tilt or hairstyle.

The woman is standing naturally with her head completely fixed in a normal upright neutral position. Her head must not be lowered at all. No nodding, bowing, chin tuck, chin lift, skull rotation, forehead tilt, jaw tilt, or hairline tilt. Keep the face axis and head silhouette like a natural upright standing portrait.

Place the camera clearly below the eye line, around the lower chest level, aimed gently upward. The low camera must be visually evident, but do not create it by lowering or tilting the head. The camera is the only low element.

The eyes, and only the eyes, look down directly at that low camera. Make the pupils/irises visibly displaced downward within both eye openings and make both gaze directions converge on the same low camera point. The eyes must not look at the viewer's eye level or straight at the horizon. The unmistakable read is: head remains naturally upright and still; camera is low; eyes look down to the camera. Do not produce a bowed head or a camera-facing neutral gaze.

Use a natural 85–105mm lens and restrained low-angle perspective. Preserve Face Canon identity and proportions without beautification. Preserve Hair-B compact crown, pulled-back front, natural ear-side wisps, smooth rearward gathering, dark-brown straight texture, centered vertical claw clip, compact folded section and small 4–6 cm upward/backward tuft behind the head. No bun, topknot, ponytail, braid or fan.

Use a modest visible upper portion of the pink Calibration Outfit on a plain neutral gray-white studio background. Natural hair and skin texture, relevant ear-side hair edges in frame. No props, scenery, text, logo, watermark, collage or multiple views. Produce one REVIEW_REQUIRED image only.
```
