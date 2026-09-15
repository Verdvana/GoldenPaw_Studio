# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v005 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.192
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v005
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: USER_REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: clearly_below_eye_line, head: neutral_upright, gaze: eyes_down_to_camera, projection: low_camera_without_head_tilt}
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
previous_generated_hair_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v005/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v005.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: 29b5acb32b29b52e1fea406d6fee5a32f77e0f51a99764d2628922f0571f6713
qa_status: USER_REJECTED
```

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen call completed successfully and was copied into the project candidate path.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-5f1d2076-1804-4d97-8075-94410efc0ca6.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v005/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v005.png`
- project_candidate_checksum_sha256: `29b5acb32b29b52e1fea406d6fee5a32f77e0f51a99764d2628922f0571f6713`
- technical_precheck: head and hairline remain neutral/upright while both eyes direct downward toward the low camera; low-camera angle is mild and does not create the rejected bowed-head geometry.
- review_points: confirm that the eye-only downward gaze and restrained low-camera perspective match the intended slot, and confirm B rear clip/tuft visibility if needed.
- promotion_status: not promoted; awaiting explicit user approval.

## Reference roles

- `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`: identity and stable facial geometry only; head remains neutral.
- `OWNER_HAIRSTYLE_B_L0` / `8.jpg`: real B hairline, pulled-back front, side wisps and gathering direction only.
- `OWNER_HAIRSTYLE_B_APPEARANCE_L1`: B center part, compact crown, rearward gathering, dark-brown straight texture, restrained highlights and fine strands only.

Rejected v001–v004 are continuity evidence only and are not pixel inputs.

## Prompt assembly

```text
Use case: identity-preserve. Create exactly one photorealistic 3:4 Hairstyle-B L1 candidate for CHR_HUMAN_001_OWNER from the three supplied approved/scoped references only. This is an independent v005 retry. Do not use v001, v002, v003, v004 or any generated Hair image.

The approved front Face Canon defines identity and stable facial geometry with a natural neutral head position. The real B reference defines only B's real hairline, pulled-back front, natural side wisps and gathering direction. The approved B appearance anchor defines only B's center part, compact crown, rearward gathering, dark-brown straight texture, restrained highlights and fine strands. Ignore all other properties of the references.

Make the camera clearly below the subject's eye line and aimed upward, but keep the entire head and neck in a natural neutral upright position: do not nod, bow, tuck the chin, raise the chin, rotate the skull, or pitch the hairline/crown. The face should remain anatomically near-neutral to the camera. The only directed action is the eyes: both eyes look downward toward the low camera while the brow, nose, mouth, jaw, forehead, hairline and crown remain in the same neutral head orientation. The viewer must read "head still, eyes looking down," not a bowed head and not an eye-level portrait with the head tilted.

Use restrained 85–105mm perspective and a modest low-camera rise so the underside of the chin is only naturally visible, without making the face a dramatic under-chin portrait. Preserve the approved face identity and proportions without beautification or geometry changes. Keep Hair-B's compact controlled crown, pulled-back front, natural ear-side wisps, smooth rearward gathering, dark-brown predominantly straight texture and restrained volume. The centered vertical claw clip, compact folded section and small 4–6 cm upward/backward tuft remain behind the head; no bun, topknot, ponytail, braid or fan.

Use a modest visible upper portion of the pink Calibration Outfit on a plain neutral gray-white studio background. Natural hair and skin texture, complete relevant ear-side hair edges in frame. No props, scenery, text, logo, watermark, collage or multiple views. Produce one REVIEW_REQUIRED image only.
```
