# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v014 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v014
gate: "Gate 4 — Hairstyle Canon"
status: APPROVED
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: low_camera_looking_up, head: neutral, gaze: down_to_camera, hair: B_replacement}
reference_set_ids: [OWNER_HAIR_A_LOW_CAMERA_LOOK_DOWN_CANON_L1, OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 4
previous_generated_hair_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/approved/HAIR_B_06_LOW_CAMERA_LOOK_DOWN/OWNER_HAIR_B_06_LOW_CAMERA_LOOK_DOWN_CANON_001.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: b042bfc3879eaa1a9f70c1f22e397045661860aef196993cf834d08f728f50de
qa_status: PASS_USER_APPROVED
```

## Reference responsibilities

- `OWNER_HAIR_A_LOW_CAMERA_LOOK_DOWN_CANON_L1`: low-camera perspective, neutral head relationship, downward gaze, hidden crown and under-jaw/ear-side framing only; must not define Hair-A or any Hair-B pixels.
- `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`: approved owner identity and stable facial geometry only; must not define camera projection, hairstyle, outfit, lighting or background.
- `OWNER_HAIRSTYLE_B_L0` (`8.jpg`): real B hairline, pulled-back front, side wisps, gathered direction and restrained volume only; must not define face, expression, clothing, lighting or background.
- `OWNER_HAIRSTYLE_B_APPEARANCE_L1`: approved B center part, compact crown, smooth rearward gathering, dark-brown straight texture, restrained highlights and fine strands only; must not define face, high-camera geometry, clothing, lighting or background.

## Prompt assembly

```text
Use case: identity-preserve
Asset type: owner L1 Hairstyle-B low-camera technical Canon candidate
Primary request: Create one photorealistic 3:4 vertical Hairstyle-B candidate for HAIR_B_06_LOW_CAMERA_LOOK_DOWN. Preserve the approved owner's identity and preserve the low-camera composition. The camera is clearly below the subject, looking upward; the subject keeps the head naturally neutral and looks down toward the low camera with the eyes, without a high-camera or eye-level reconstruction. Show the same head size and chest crop as the approved Hair-A low-camera reference.
Input images: Image 1 defines only low-camera composition, neutral head relationship, downward gaze, hidden crown and under-jaw/ear-side framing. Image 2 defines only approved owner identity. Image 3 defines only real Hairstyle-B hairline and gathered-updo behavior. Image 4 defines only approved Hairstyle-B design: restrained center part, compact dark-brown straight hair, smooth rearward gathering, fine side wisps and a small restrained rear clip-held tuft.
Scene/backdrop: neutral light-gray seamless studio background.
Subject: same adult owner, calm neutral expression, pink calibration one-piece visible at the shoulders/chest if clothing appears.
Style/medium: photographic realism, natural skin and hair texture.
Composition/framing: head top through upper chest, complete hair silhouette; low camera looking upward, only the eyes look downward, no broad visible crown/top plane.
Lighting/mood: soft neutral studio light, neutral white balance, low contrast.
Constraints: change only the hairstyle relative to the low-camera composition; preserve face, facial proportions, head posture, camera height, gaze direction, framing, outfit, lighting and background. Hair-B must be visibly pulled back, compact, straight, dark brown, with restrained part, side wisps, rearward gathering and small rear tuft/clip structure.
Avoid: Hair-A, loose long hair, high camera, eye-level camera, visible broad top-of-head plane, head tilt, chin tuck, face drift, body drift, clothing change, dramatic lighting, text, watermark, extra views, previous AI candidates.
```

User approved this candidate with “合格的，登记吧”. The raster was moved (not copied) to the approved Canon path. Approval is scoped to the Hairstyle-B low-camera/look-down view; full `owner_v1.0` remains unlocked.
