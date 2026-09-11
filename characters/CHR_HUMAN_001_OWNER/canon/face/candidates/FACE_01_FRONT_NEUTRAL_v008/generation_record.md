# FACE_01_FRONT_NEUTRAL_v008 — Generation Record

```yaml
candidate_id: FACE_01_FRONT_NEUTRAL_v008
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
asset_level: L1_CANDIDATE
gate: GATE_2_FACE
status: SUPERSEDED_REVISION_REQUIRED
approval_status: REJECTED
generation_tool: built_in_imagegen
spec_revision: draft_1.7
identity_md_revision: draft_0.7
pixel_reference_set_ids:
  - OWNER_FACE_APPEARANCE_L1_CROP_2X_DERIVATIVE
  - OWNER_HAIRSTYLE_A_L0_FACE_MASKED_DERIVATIVE
pixel_reference_count: 2
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
output_path: characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v008/FACE_01_FRONT_NEUTRAL_v008.png
qa_status: FAIL_FACE_WIDTH_AND_IDENTITY_MATCH
```

## Reference responsibility

| Input | Responsibility | Explicit exclusion |
|---|---|---|
| Image 1 — `B_FACE_SKIN_CROP_2X.png` | exclusive face identity and B-anchor skin tone | hair, crown, camera, body, outfit, lighting/background |
| Image 2 — `DSC00847_HAIR_ONLY_MASKED.png` | user-confirmed Hairstyle A design only | masked area, face, skin, body, outfit, pose, camera, outdoor light/background |

No AI candidate is supplied. v005 defines only the user-confirmed textual face target; v007 defines only the user-confirmed textual hairstyle/camera method.

## Targeted facial correction

Relative to the rejected v007 direction, restore the v005-approved facial appearance through text only: fuller softer cheeks and mid/lower face, a slightly wider rounded jaw taper, restrained natural eye opening without enlargement or lifted outer corners, natural nose width and soft tip, unsharpened lips, and a soft rounded chin. Avoid face slimming, eye enlargement, pointed jaw/chin, or generic beautification.

## Result

- attempt_1: output blocked by image safety system (`sexual` false-positive); no image produced or saved
- retry_adjustment: tighter non-sexual ID-photo head-and-shoulders framing; calibration garment visible only at shoulder edges; identity, hairstyle, skin and camera constraints unchanged
- generated_at: 2026-09-10
- output_path: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v008/FACE_01_FRONT_NEUTRAL_v008.png`
- checksum_sha256: `51d05cbae7ed3c440c9c50a28f3c5d374e70d72446e302dd0d5cba8c335eb412`
- dimensions: `1086x1448` (exact 3:4)
- QA_record: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v008/QA.md`
- user_decision: rejected; facial appearance remains too similar to the prior two rejected versions and the face is slightly too wide; never use v008 as a pixel reference
