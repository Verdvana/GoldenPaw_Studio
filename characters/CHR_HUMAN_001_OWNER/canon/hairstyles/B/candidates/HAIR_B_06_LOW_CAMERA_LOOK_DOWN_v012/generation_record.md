# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v012 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.199
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v012
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: USER_REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: below_eye_line, head: upright_neutral, gaze: downward_to_camera, crown: reduced}
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
previous_generated_hair_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v012/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v012.png"
actual_dimensions_px: null
checksum_sha256: null
qa_status: USER_REJECTED
```

## Fresh prompt assembly

```text
Create one photorealistic 3:4 owner portrait with Hairstyle-B from the supplied approved Face Canon, real B hair source, and approved B appearance anchor. Build a new image from scratch. Do not use any previous generated candidate.

Camera placement: the camera is physically lower than the woman's eye line, below the chin, and points upward at her. This is a low-angle shot. The camera cannot be above her eyes and the image cannot show a large top-down view of her head.

Head posture: she is standing normally with her head held naturally upright and still. The head does not dip, bow, nod, lift, turn or tilt. Her chin is not pushed toward the camera. Her face remains in its normal standing alignment.

Gaze: she looks directly at the low camera by moving only her eyes downward. Both pupils must be visibly in the lower part of the eyes and both gaze directions must point to the camera lens below. She must not look at the viewer's eye level, into the distance, or below the lens.

Perspective: because the camera is low, the lower face may show a subtle underside view. The top of the head must be minimally visible, with no broad crown plane and no long exposed scalp part. Face, hairline and crown must share the same low-camera perspective; do not mix a low-angle face with a high-angle or eye-level crown.

Keep the owner's identity from Face Canon. Keep Hairstyle-B: pulled-back front, compact dark-brown straight hair, restrained part, side wisps and rearward gathering. Pink calibration outfit, neutral gray studio background, natural lighting, restrained lens. No fisheye, props, text, watermark, collage or multiple views. Output one REVIEW_REQUIRED candidate.
```
