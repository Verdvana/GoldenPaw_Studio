# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.189
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v002
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: USER_REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: clearly_below_eye_line, subject_head: entire_head_lowered, gaze: camera, projection: low_camera_subject_looking_down}
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
previous_generated_hair_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v002/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v002.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: a1dd9b771816721ae849d1331eec787c6847c6768dc58748160e92e0b9acda33
qa_status: USER_REJECTED
```

## Reference roles

- `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`: approved identity and stable facial geometry only; no Hair-A, lighting or background authority.
- `OWNER_HAIRSTYLE_B_L0` / `8.jpg`: real B hairline, pulled-back front, side wisps, gathering direction and restrained volume only; face, expression, hands, sweater, warm light and garden excluded.
- `OWNER_HAIRSTYLE_B_APPEARANCE_L1`: approved B center part, compact crown, smooth gathering, dark-brown color, restrained highlights and fine strands only; face, high-camera geometry, clothing, lighting and background excluded.

## Candidate authority and exclusions

This candidate defines only Hair-B behavior in the corrected low-camera/subject-looking-down relationship: reduced visible crown, short frontal part, ear-side and under-jaw wisps, rearward gathering, and the low-angle projection of the centered claw clip/fold/short tuft. It must not redefine face, body, clothing, expression, skin, hosiery, lighting, background or any other B view. `v001` and all generated Hair pixels are excluded.

## Prompt assembly

```text
Use case: identity-preserve. Create exactly one photorealistic 3:4 Hairstyle-B L1 candidate for CHR_HUMAN_001_OWNER from the three supplied references only. Do not use HAIR_B_06 v001 or any generated Hair image.

The approved front Face reference defines only identity and stable facial geometry. The real B reference defines only real hairline, pulled-back front, natural side wisps, gathering direction and restrained volume. The approved B appearance anchor defines only center-part projection, compact crown, smooth rearward gathering, dark-brown tone, restrained highlights and fine strands. Ignore all other properties of these references.

The camera must be clearly below the subject's eye line and aimed upward. The adult subject must lower the entire head toward the chest and look downward directly into the camera. Make the lower-camera relationship unmistakable: show a readable underside of the chin and lower jaw, while the forehead and top of the skull recede away from the camera. This must not look like a high camera, top-down view, or eye-level portrait with only the eyes rotated.

Preserve the approved face without beautification or geometry changes. Hair-B must have a compact controlled crown with the visible frontal part ending very short near the hairline; no large exposed crown surface and no long scalp line. Show natural ear-side and under-jaw wisps displaced by the lowered head, smooth rearward gathering, and dark-brown predominantly straight texture. The centered vertical medium claw clip at the occiput and compact clip-held fold remain behind the lowered head and may be only partially visible; do not turn them into a bun, topknot or ponytail. The small 4–6 cm tuft remains restrained and points gently upward/backward where visible.

Use only a modest visible upper portion of the pink Calibration Outfit on a plain neutral gray-white studio background. Restrained 85–105mm-equivalent perspective, soft even neutral lighting, natural skin and hair texture, complete relevant hair edges and ear/under-jaw relationships in frame. No props, scenery, text, logo, watermark, collage or multiple views. Produce one REVIEW_REQUIRED image only.
```

## Generation result

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen call completed successfully.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-1ef3d7f0-a340-454f-a33e-809ba5042ff9.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v002/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v002.png`
- project_candidate_checksum_sha256: `a1dd9b771816721ae849d1331eec787c6847c6768dc58748160e92e0b9acda33`
- technical_precheck: rejected. Head/camera relationship remains mixed: too much top/crown is visible, creating the impression that only the facial features look down while the crown stays near eye-level.
- review_points: v002 must not be used as a pixel input or downstream reference. A future independent retry must rotate the entire head downward, nearly hide the crown surface, and establish the low camera through the underside of the chin, nose base and under-jaw hair.
- promotion_status: rejected; no promotion.

## User rejection

- statement: “头顶和暴露还是多，有种只有五官俯视而头顶平视的感觉，重新来”
- decision: `USER_REJECTED`
- rejected_candidate_pixels_used: `NO`
