# FACE_01_FRONT_NEUTRAL_v010 — Generation Record

```yaml
candidate_id: FACE_01_FRONT_NEUTRAL_v010
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
asset_level: L1_CANDIDATE
gate: GATE_2_FACE
status: SUPERSEDED_REVISION_REQUIRED
approval_status: REJECTED
generation_tool: built_in_imagegen
spec_revision: draft_1.9
identity_md_revision: draft_0.9
pixel_reference_set_ids:
  - OWNER_FACE_APPEARANCE_L1
  - OWNER_HAIRSTYLE_A_L0_FACE_MASKED_DERIVATIVE
pixel_reference_count: 2
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
output_path: characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v010/FACE_01_FRONT_NEUTRAL_v010.png
qa_status: PARTIAL_PASS_FACE_SKIN_FAIL_CROWN_ANGLE
```

## Constraint merge requested by user

### v005 face/skin constraint block

- original full B L1 image is authoritative only for the exact target face, facial relationships, apparent age and natural skin tone;
- no extra face-width correction, slimming, widening or beautification;
- preserve the user-confirmed face/skin direction while excluding B hair, pose, camera, clothing, light and background.

### v006 hair/crown/camera constraint block

- Hairstyle A: flat close-to-scalp roots, low crown, near-center naturally imperfect part, narrow silhouette, straight loose dark-brown lengths, fine separated strands, modest asymmetry, slim face-framing locks and tapered wispy uneven ends;
- camera 2–3 cm below pupil midpoint with only 1–2° upward pitch, final result visually neutral eye-level;
- crown from the front with almost no horizontal top surface; no overhead oval plane, long receding scalp part or face/crown projection mismatch.

No v005/v006 image is supplied. The output is a fresh parallel generation from the original approved B anchor and L0-derived masked hair reference.

## Result

- generated_at: 2026-09-10
- output_path: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v010/FACE_01_FRONT_NEUTRAL_v010.png`
- checksum_sha256: `c36ad2ea1cf77df409c7763b890815ffe7e890407280863b2849e7d282fd5ac8`
- dimensions: `1086x1448` (exact 3:4)
- QA_record: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v010/QA.md`
- user_decision: rejected as a whole; facial features and skin tone are perfect, but visible crown/top-head area remains too large and does not read as true eye-level; never use v010 as a pixel reference
