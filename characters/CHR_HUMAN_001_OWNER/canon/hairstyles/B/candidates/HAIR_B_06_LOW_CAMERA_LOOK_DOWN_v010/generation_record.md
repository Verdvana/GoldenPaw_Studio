# HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v010 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.197
identity_md_revision: draft_0.175
asset_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v010
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: USER_REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
view: {camera: low_angle_below_subject, head: natural_standing_neutral, gaze: down_to_camera, projection: unified_low_camera_with_reduced_crown}
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
previous_generated_hair_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v010/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v010.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: 50e83a190f320ef65a8920cfa4d36991f43929ee8bc2650a30d68cd79b53e710
qa_status: USER_REJECTED
```

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen call completed successfully and was copied into the project candidate path.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-0aabb6b1-27be-4d0c-a611-b4437844ec86.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v010/HAIR_B_06_LOW_CAMERA_LOOK_DOWN_v010.png`
- project_candidate_checksum_sha256: `50e83a190f320ef65a8920cfa4d36991f43929ee8bc2650a30d68cd79b53e710`
- technical_precheck: fresh prompt reset; low camera, downward gaze, reduced crown exposure and unified face/hair perspective requested.
- review_points: user must verify natural upright head posture and direct eye targeting of the low camera.
- promotion_status: not promoted; awaiting explicit user approval.

## Fresh prompt assembly

```text
Generate one photorealistic 3:4 portrait of CHR_HUMAN_001_OWNER wearing Hairstyle-B. Use only the supplied approved Face Canon, real B hair reference, and approved B appearance reference. Build this image independently from scratch; do not imitate or continue any prior generated candidate.

The woman is standing naturally and holding her head in the ordinary upright position. She is neither looking down with her head nor looking up with her head. Keep her head, neck, jaw, chin, forehead, hairline, crown and ears in a relaxed neutral standing alignment.

Use a clearly low camera placed below her eye line and below her chin, aimed upward at her. The camera position alone creates the low-angle view. The face and the hair must share one consistent low-camera projection: the upward view of the face must not be paired with a flat eye-level view of the crown. Reduce visible crown/top-of-head exposure; show only a narrow near-hairline top transition, with no broad top plane and no long scalp part. The hairline and crown must follow the same perspective as the low-angle face.

Her head stays still. Only her eyes look downward toward the camera below. Both pupils must be visibly lowered inside the eyes and aimed at the same camera position; she must not look straight ahead or past the camera. The visual statement is simple: naturally standing head, low camera, eyes looking down at the camera.

Keep the facial identity and proportions from the approved Face Canon. Keep Hairstyle-B's pulled-back front, compact dark-brown straight hair, controlled center part, restrained crown, side wisps, rearward gathering, and the small rear clip-held tuft. Do not create a new hairstyle or blend Hair-A and Hair-B.

Use the pink Calibration Outfit, neutral gray studio background, soft natural lighting, and a restrained portrait lens. No dramatic distortion, no fisheye, no extra views, no props, no text, no watermark, no collage. Output one candidate only with status REVIEW_REQUIRED.
```
