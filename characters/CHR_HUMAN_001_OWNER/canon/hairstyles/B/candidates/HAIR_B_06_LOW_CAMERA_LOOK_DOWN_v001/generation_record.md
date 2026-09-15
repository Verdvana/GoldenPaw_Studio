# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.188
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v001
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: USER_REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: low, subject_head: lowered, gaze: camera, projection: low_camera_subject_looking_down}
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
previous_generated_hair_inputs: []
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v001/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v001.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: a3fc7c49e3ad3df221d48b37f5b18b680819d3238fe8275c0aea16da2fc76afb
qa_status: USER_REJECTED
```

## Reference roles

- `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`: identity and stable facial geometry only. Its standard eye-level front Hair-A arrangement, clothing, lighting and background are excluded.
- `OWNER_HAIRSTYLE_B_L0` / `8.jpg`: real B hairline, pulled-back front, natural face-side wisps, gathered direction and front volume only. Its face, expression, hands, sweater, warm light and garden are excluded.
- `OWNER_HAIRSTYLE_B_APPEARANCE_L1`: approved B center-part, compact crown, smooth gathering, dark-brown color, restrained highlights and fine strands only. Its high-camera face/context and clothing/background are excluded.

## Candidate authority and exclusions

This candidate may define only Hairstyle-B response under a low camera with the subject looking down: lower-camera crown/forehead framing, ear-side and under-jaw wisps, rearward gathering direction, and the visible projection of the centered vertical claw clip, compact folded hair and short 4–6 cm upward/backward tuft. The face remains context from the approved Face Canon and is not redefined by this Hair candidate.

It must not define a new face, body, outfit, expression, skin, hosiery, lighting, background, any A/B blend, or any other B view. Do not use B01–B04 or any generated Hair raster as input.

## Prompt assembly

```text
Use case: identity-preserve. Asset type: one adult technical Hairstyle-B Canon candidate for CHR_HUMAN_001_OWNER. Create exactly one new photorealistic 3:4 portrait reference in parallel from the three supplied references; do not use any prior generated Hair image.

Reference image 1, OWNER_FACE_FRONT_NEUTRAL_CANON_L1, defines only the approved person's identity and stable facial geometry. Ignore its standard eye-level Hair-A arrangement, clothing, lighting and background.
Reference image 2, OWNER_HAIRSTYLE_B_L0, defines only real B hairline behavior, pulled-back front, natural side wisps, gathered-updo direction and restrained volume. Ignore its face, expression, hands, sweater, warm light and garden setting.
Reference image 3, OWNER_HAIRSTYLE_B_APPEARANCE_L1, defines only approved B center-part projection, compact crown, smooth rearward gathering, dark-brown color, restrained highlights and fine strands. Ignore its face, high-camera perspective, clothing, lighting and background.

Show one coherent low-camera view: the camera is clearly below the subject's eye line and looks upward, while the adult subject lowers the entire head and looks directly toward the camera. This is a real low-angle projection, not an eye-level camera with only the eyes rotated downward. Use a restrained 85–105mm-equivalent perspective so the face remains natural and the lower-camera relationship is readable without exaggeration. Keep the face, ears, chin and upper chest in one uncluttered portrait composition with a modest visible upper portion of the pink Calibration Outfit on a plain neutral gray-white studio background.

Hair-B under this low camera: preserve the compact controlled crown and near-center part, with only a short frontal part visible before it disappears into the crown; do not expose a large crown surface or a long scalp line. Show the pulled-back front, natural ear-side and under-jaw wisps, and smooth dark-brown rearward gathering. The centered vertical medium matte dark-brown claw clip remains at the occiput and may be partially hidden by the lowered head angle, but its rear-center placement must remain structurally coherent. The compact folded hair stays clip-held, not a bun, topknot or ponytail. A small restrained 4–6 cm tuft projects gently upward/backward above the clip where visible; do not enlarge it into a fan or long tail.

Preserve the approved face without beautification, identity drift, altered nose/jaw/eyes, changed age or expression. Use natural straight dark-brown hair, controlled low-to-moderate volume, realistic density, restrained highlights and fine strands. Exact 3:4 portrait, complete relevant hair edges and ear-side/under-jaw relationships in frame, soft even neutral studio lighting, natural texture. No props, scenery, text, logo, watermark, collage or multiple views. Produce one REVIEW_REQUIRED image only.
```

## Generation result

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen call completed successfully.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-bde82079-24c2-4f6e-b4da-6b0f1a73751d.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v001/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v001.png`
- project_candidate_checksum_sha256: `a3fc7c49e3ad3df221d48b37f5b18b680819d3238fe8275c0aea16da2fc76afb`
- technical_precheck: rejected. The output exposes too much top/crown surface and reads as a high-camera view rather than a clearly low-camera view observing a lowered head.
- review_points: v001 must not be used as a pixel input or downstream reference. A future independent retry must place the camera clearly below the eye line, lower the entire head, minimize visible crown, and make the underside of the chin and under-jaw/ear-side hair projection readable.
- promotion_status: rejected; no promotion.

## User rejection

- statement: “nono,这不是低机位，这是高机位，低机位应该是人物在俯视”
- decision: `USER_REJECTED`
- rejected_candidate_pixels_used: `NO`
