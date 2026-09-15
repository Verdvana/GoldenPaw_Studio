# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.190
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v003
gate: "Gate 4 — Hairstyle Canon"
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: clearly_below_eye_line, subject_head: entire_head_rotated_down, gaze: camera, projection: low_camera_subject_looking_down}
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
previous_generated_hair_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v003/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v003.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: 9a7017083dd88c4eb4158f75f16d5c1e2d0852d8f9f4d79b8e37c9ee44adcdeb
qa_status: REVIEW_REQUIRED
```

## Prompt assembly

```text
Use case: identity-preserve. Create exactly one photorealistic 3:4 Hairstyle-B L1 candidate for CHR_HUMAN_001_OWNER from the three supplied references only. This is an independent retry for HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v003. Do not use v001, v002, or any generated Hair image.

The approved front Face reference defines only identity and stable facial geometry. The real B reference defines only real B hairline, pulled-back front, natural side wisps, gathered direction and restrained volume. The approved B design anchor defines only B center part, compact crown, rearward gathering, dark-brown straight texture, restrained highlights and fine strands. Ignore all other properties of every reference.

Make the camera unmistakably low: place the camera well below the subject's eye line, aimed upward. Rotate the entire head as one rigid anatomical unit downward toward the chest; the eyes, brow, nose, mouth, chin, forehead, hairline, skull and crown must share the same downward head rotation. The subject looks down directly into the low camera. This is not a high camera, not top-down, and not an eye-level portrait with only the eyes or face tilted.

The resulting projection must show the underside of the chin and lower jaw clearly, with the nose base visible from below. The forehead and top of the skull must recede away from the camera; the crown surface must be almost entirely hidden, with no broad top plane and no long visible scalp part. Keep the visible frontal part extremely short near the hairline. Do not let the hairline/crown remain upright while the face tilts.

Preserve the approved face without beautification or geometry changes. Show B's compact controlled crown, pulled-back front, natural ear-side and under-jaw wisps displaced by the lowered head, smooth rearward gathering and dark-brown predominantly straight texture. The centered vertical claw clip, compact clip-held fold and small 4–6 cm upward/backward tuft remain behind the head and may be almost fully occluded; do not turn them into a bun, topknot or ponytail.

Use a modest visible upper portion of the pink Calibration Outfit on a plain neutral gray-white studio background. Restrained 85–105mm perspective, soft even neutral lighting, natural hair and skin texture, complete relevant ear-side and under-jaw hair edges in frame. No props, scenery, text, logo, watermark, collage or multiple views. Produce one REVIEW_REQUIRED image only.
```

## Generation result

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen call completed successfully.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-9e4c5d54-d19d-4b1f-8dd8-7ca2afeb6470.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v003/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v003.png`
- project_candidate_checksum_sha256: `9a7017083dd88c4eb4158f75f16d5c1e2d0852d8f9f4d79b8e37c9ee44adcdeb`
- technical_precheck: entire head is pitched downward as one unit; crown/top surface is nearly hidden; underside of chin, lower jaw and nose base are strongly readable; ear-side and under-jaw wisps remain coherent; neutral studio and pink Calibration Outfit context comply.
- review_points: confirm the low-camera pitch is now correct and whether the mostly occluded claw clip remains acceptable for this projection-specific Hair-B slot.
- promotion_status: not promoted; awaiting explicit user approval.
