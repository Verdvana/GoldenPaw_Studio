# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v011 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.198
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v011
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: USER_REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: low_camera, head: natural_upright, gaze: directly_at_low_camera, projection: approved_A_composition_geometry_with_B_hair}
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1, OWNER_HAIR_A_LOW_CAMERA_LOOK_DOWN_CANON_L1]
reference_count: 4
previous_generated_hair_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v011/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v011.png"
actual_dimensions_px: null
checksum_sha256: null
qa_status: USER_REJECTED
```

## Prompt assembly

```text
Create one photorealistic 3:4 Hairstyle-B candidate for the owner. Use the approved Hair-A low-camera image as the exact composition and gaze-direction guide: retain its clearly low camera placement, upright natural head relationship, and direct eye contact with the low camera. Use the approved Face Canon for the owner's identity. Replace the Hair-A hairstyle completely with Hairstyle-B defined by real 8.jpg and the approved B appearance anchor.

The subject stands naturally with the head upright and still. Do not lower, raise, nod, bow, tuck, lift, rotate or tilt the head. The camera is below the face and looks upward. The woman's eyes must directly look into that low camera, with both pupils visibly aligned toward the camera lens; do not let the eyes look below, above, beside or through the camera.

Keep the same unified low-camera perspective across face, hairline and crown as the approved A low-camera composition. Reduce visible crown/top-of-head exposure; no broad top plane and no long flat scalp part. Do not create a mismatch where the face is low-angle but the crown is eye-level.

Identity comes only from the approved Face Canon. Hair comes only from B references: pulled-back front, compact dark-brown straight hair, restrained center part, side wisps, rearward gathering and small rear clip-held tuft. Do not retain any Hair-A pixels or Hair-A hairstyle. Do not use any prior generated candidate.

Pink Calibration Outfit, neutral gray studio background, natural texture, restrained lens, no distortion, props, text, watermark, collage or multiple views. Output one REVIEW_REQUIRED candidate only.
```
