# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v004 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.191
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v004
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: USER_REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: clearly_below_eye_line, subject_head: entire_head_rotated_down, gaze: camera, projection: low_camera_subject_looking_down}
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1, OWNER_HAIR_A_LOW_CAMERA_LOOK_DOWN_CANON_L1]
reference_count: 4
previous_generated_hair_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v004/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v004.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: 23023bd26ca2db203688240f1568c676f89a67f1a6067ff1e1bc6233176e73e4
qa_status: USER_REJECTED
```

## Reference roles

- `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`: face identity and stable facial geometry only.
- `OWNER_HAIRSTYLE_B_L0` / `8.jpg`: real B hairline, pulled-back front, side wisps and gathering direction only.
- `OWNER_HAIRSTYLE_B_APPEARANCE_L1`: B center part, compact crown, rearward gathering, dark-brown texture and restrained highlights only.
- `OWNER_HAIR_A_LOW_CAMERA_LOOK_DOWN_CANON_L1`: low-camera head pitch, chin-toward-chest relationship, underside-of-chin and nose-base perspective only. Must not define A or B hairstyle pixels, face identity, facial geometry, body, clothing or lighting.

## Candidate authority and exclusions

This candidate defines only Hair-B response under the corrected low-camera/entire-head-looking-down relationship. A low-camera Canon is a geometry-only supporting reference here; it is not a Hair-B or face source. Do not use v001–v003 or any other generated Hair image as pixel input.

## Prompt assembly

```text
Use case: identity-preserve. Create exactly one photorealistic 3:4 Hairstyle-B L1 candidate for CHR_HUMAN_001_OWNER. This is an independent v004 retry; do not use any prior generated Hair image.

Reference 1, approved front Face Canon, defines only identity and stable facial geometry. Reference 2, real B source 8.jpg, defines only real B hairline, pulled-back front, natural side wisps and gathering direction. Reference 3, approved B appearance anchor, defines only B center part, compact crown, smooth rearward gathering, dark-brown straight texture, restrained highlights and fine strands. Reference 4, approved Hair-A low-camera Canon, is a geometry-only supporting reference for the camera-under-chin relationship, chin tucked toward the chest, visible lower jaw/nose base and whole-head downward pitch. Do not copy its Hair-A hairstyle, facial identity or facial geometry.

Make the camera unmistakably low and place it below the mouth/eye line, aimed upward from under the chin. Rotate the entire head and skull downward as one rigid anatomical unit: forehead, hairline, crown, eyes, nose, mouth and chin share the same downward pitch. The chin is nearer the camera and tucked toward the chest; the forehead and crown recede away. Show a clear underside of the chin, lower jaw and nose base. The crown/top plane must be almost entirely hidden, with no broad top surface and no mixed projection where only the facial features look down while the hair remains level.

Preserve the approved Face Canon identity and facial proportions without beautification. For Hair-B, keep the visible frontal part extremely short, the crown compact, the pulled-back front and natural ear-side/under-jaw wisps coherent with the lowered head. Maintain smooth rearward gathering, dark-brown straight texture and restrained volume. The centered vertical claw clip, compact folded section and 4–6 cm upward/backward tuft remain behind the head and may be mostly occluded; no bun, topknot, ponytail, braid or fan. Do not copy Hair-A.

Use a modest visible upper portion of the pink Calibration Outfit on a plain neutral gray-white studio background. Restrained 85–105mm perspective, soft even neutral lighting, natural texture, relevant ear-side and under-jaw hair edges in frame. No props, scenery, text, logo, watermark, collage or multiple views. Produce one REVIEW_REQUIRED image only.
```

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen call completed successfully and was copied into the project candidate path.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-df5cc3b1-fc87-4246-8ca3-f348733e252a.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v004/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v004.png`
- project_candidate_checksum_sha256: `23023bd26ca2db203688240f1568c676f89a67f1a6067ff1e1bc6233176e73e4`
- technical_precheck: low-camera facial perspective is improved using the approved Hair-A low-camera asset only as geometry support; the entire head remains pitched downward, with readable lower jaw/nose base and restrained crown exposure.
- review_points: confirm whether the A-referenced facial projection is now the desired low-camera expression for Hair-B, and whether the mostly occluded rear clip/tuft is acceptable in this projection-specific slot.
- rejection: user states the candidate shows the head tilted downward while the face remains near eye-level; this does not match the requested neutral head with downward eye gaze.
- promotion_status: not promoted; rejected and forbidden as downstream pixel input.
