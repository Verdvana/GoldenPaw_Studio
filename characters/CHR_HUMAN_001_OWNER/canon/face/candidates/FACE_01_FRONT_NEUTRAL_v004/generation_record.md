# FACE_01_FRONT_NEUTRAL_v004 — Generation Record

```yaml
candidate_id: FACE_01_FRONT_NEUTRAL_v004
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
asset_level: L1_CANDIDATE
gate: GATE_2_FACE
status: SUPERSEDED_REVISION_REQUIRED
approval_status: REJECTED
generation_tool: built_in_imagegen
spec_revision: draft_1.3
identity_md_revision: draft_0.3
pixel_reference_set_ids:
  - OWNER_FACE_APPEARANCE_L1
text_derived_design_sources:
  - OWNER_HAIRSTYLE_A_L0
pixel_reference_count: 1
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
output_path: characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v004/FACE_01_FRONT_NEUTRAL_v004.png
qa_status: FAIL_HAIRSTYLE_AND_MIXED_HEAD_PERSPECTIVE
```

## Reference responsibility

| Input | Responsibility | Explicit exclusion |
|---|---|---|
| Original approved B L1 image | target face, facial relationships, apparent age and skin tone only | camera height, subject head tilt, Hairstyle B, outfit, lighting, background |
| Text-derived HAIRSTYLE_A specification | long straight loose A hairstyle | no second face image supplied |

Neither v002 nor v003 is supplied as a reference.

## Prompt

Use case: identity-preserve. Generate one new `FACE_01_FRONT_NEUTRAL_v004` from the original approved B L1 face/skin anchor. Preserve the user-confirmed target face and skin tone, while removing the source's slightly high camera and slightly upturned head. Enforce a true eye-level ID-photo geometry: camera optical center exactly level with the midpoint of both pupils; horizontal optical axis perpendicular to the frontal facial plane; neutral head posture; Frankfort horizontal plane level; chin neither raised nor lowered; gaze straight ahead; no visible upward-looking pose; do not show excessive top plane of the head. Use HAIRSTYLE_A from its fixed text specification: long straight loose dark-brown hair, near-center part, natural low-to-moderate crown volume, long face-framing panels and tapered ends. Plain pink one-piece Calibration Outfit upper portion, neutral gray-white studio, soft even 5200–5600K light, 85–105mm-equivalent perspective, exact 3:4. No face redesign, no v003 reference, no camera-angle inheritance, no bun/updo, no beauty filter, no text or collage. One REVIEW_REQUIRED candidate only.

## Result

- generated_at: 2026-09-10
- output_path: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v004/FACE_01_FRONT_NEUTRAL_v004.png`
- checksum_sha256: `1c98887cab8f77663d08172abd152c75205661751041d3d877c598931d7a3815`
- dimensions: `1086x1448` (exact 3:4)
- QA_record: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v004/QA.md`
- user_decision: rejected; face and skin accepted, but Hairstyle A is incorrect and the eye-level face does not match the still top-down-looking crown projection; never use v004 as a pixel reference
