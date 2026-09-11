# FACE_01_FRONT_NEUTRAL_v007 — Generation Record

```yaml
candidate_id: FACE_01_FRONT_NEUTRAL_v007
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
asset_level: L1_CANDIDATE
gate: GATE_2_FACE
status: SUPERSEDED_REVISION_REQUIRED
approval_status: REJECTED
generation_tool: built_in_imagegen
spec_revision: draft_1.6
identity_md_revision: draft_0.6
pixel_reference_set_ids:
  - OWNER_FACE_APPEARANCE_L1_CROPPED_DERIVATIVE
  - OWNER_HAIRSTYLE_A_L0_FACE_MASKED_DERIVATIVE
pixel_reference_count: 2
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
output_path: characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v007/FACE_01_FRONT_NEUTRAL_v007.png
qa_status: PARTIAL_PASS_HAIR_CAMERA_FAIL_FACE
```

## Reference responsibility

| Input | Responsibility | Explicit exclusion |
|---|---|---|
| Image 1 — `B_FACE_SKIN_CROP.png` | exact face identity and B-anchor skin tone | hair, crown, camera/head pose, body, outfit, lighting/background |
| Image 2 — `DSC00847_HAIR_ONLY_MASKED.png` | v006-confirmed Hairstyle A design only | masked area, face, skin, body, outfit, pose, camera, outdoor light/background |

No generated Face candidate is supplied. v006 success is carried only as user-confirmed text constraints.

## Prompt strategy

- give Image 1 absolute priority for every facial landmark and all visible skin color;
- treat the gray oval in Image 2 as deleted information, not a design feature;
- reuse the user-confirmed v006 Hairstyle A description and subtle inverse camera compensation;
- prohibit averaging Image 1 with any visible identity cues outside Image 1.

## Prompt assembly

Generate one photorealistic `FACE_01_FRONT_NEUTRAL_v007`. Image 1 has absolute authority for exact facial landmarks, proportions, apparent age, natural asymmetry, texture, luminance and warm-neutral skin hue; prohibit redesign, averaging and whitening. Image 2 is the face-masked DSC00847 derivative and defines only visible Hairstyle A pixels; its gray oval means deleted information and must not influence any shape or color. Reuse the user-confirmed v006 hair specification: flat roots, low crown, near-center natural part, narrow silhouette, restrained density, fine separated strands, slim face-framing locks and tapered wispy uneven ends. Reuse the user-confirmed subtle anti-high-camera setup: camera 2–3 cm below pupil midpoint, 1–2° upward pitch, 100–105mm lens, while the final image reads neutral eye-level. Pink calibration swimsuit upper portion, neutral studio, exact B skin depth, exact 3:4; no previous generated candidate, mask trace, beautification, text or collage.

## Result

- generated_at: 2026-09-10
- output_path: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v007/FACE_01_FRONT_NEUTRAL_v007.png`
- checksum_sha256: `3d60201cde8b5c40b93cb3342db532c5532dea0257a80b7866996723f391a758`
- dimensions: `1086x1448` (exact 3:4)
- QA_record: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v007/QA.md`
- user_decision: rejected as a whole; Hairstyle A and angle accepted, but facial appearance is incorrect; user identifies v005 facial appearance as the target; never use v007 as a pixel reference
