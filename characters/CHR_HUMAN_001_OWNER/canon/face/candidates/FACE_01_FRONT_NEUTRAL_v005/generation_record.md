# FACE_01_FRONT_NEUTRAL_v005 — Generation Record

```yaml
candidate_id: FACE_01_FRONT_NEUTRAL_v005
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
asset_level: L1_CANDIDATE
gate: GATE_2_FACE
status: SUPERSEDED_REVISION_REQUIRED
approval_status: REJECTED
generation_tool: built_in_imagegen
spec_revision: draft_1.4
identity_md_revision: draft_0.4
pixel_reference_set_ids:
  - OWNER_FACE_APPEARANCE_L1
  - OWNER_HAIRSTYLE_A_L0
pixel_reference_count: 2
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
output_path: characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v005/FACE_01_FRONT_NEUTRAL_v005.png
qa_status: FAIL_CROWN_HAIR_SKIN
```

## Reference responsibility

| Input | Responsibility | Explicit exclusion |
|---|---|---|
| Image 1 — original approved B L1 image | target face, facial relationships, apparent age and skin tone only | Hairstyle B, head/camera pose, crown projection, outfit, lighting, background |
| Image 2 — `L0_OWNER_017` / `DSC00847.jpg` | Hairstyle A only: part, crown volume, hairline transition, straight loose silhouette, face-framing panels, length, strand grouping and tapered ends | face identity, facial geometry, skin, body, clothing, pose, camera, outdoor lighting/background |

No generated Face candidate, including v003 or v004, may be supplied as a reference.

## Prompt

Use case: identity-preserve. Generate one new `FACE_01_FRONT_NEUTRAL_v005`. Image 1 is authoritative only for the woman's exact target face and natural skin tone. Image 2 is authoritative only for Hairstyle A and must not influence the face, skin, body, clothing, pose, lighting or background. Reproduce Hairstyle A from Image 2 closely: the same near-center part, very low smooth crown volume, close-to-scalp roots, straight long loose dark hair, slim face-framing side sections, natural strand grouping, chest-length silhouette and tapered uneven ends; do not invent a fuller salon blowout or retain any Hairstyle B structure. Rebuild the entire head under one true eye-level projection: camera optical center at pupil midpoint, horizontal axis, upright neutral head, Frankfort plane level. The face, forehead, hairline, skull, crown contour, ears and jaw must all share that level projection. Show only the small amount of upper hair surface naturally visible from eye height; no overhead oval crown plane, no long receding scalp part, no top-down skull, no face/crown perspective mismatch. Preserve the user-confirmed face/skin direction without using v004. Plain pink calibration swimsuit upper portion, neutral gray-white studio, soft even 5200–5600K light, 85–105mm-equivalent perspective, exact 3:4. One photorealistic `REVIEW_REQUIRED` candidate; no text, collage, beautification, face redesign or reference lighting leakage.

## Result

- generated_at: 2026-09-10
- output_path: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v005/FACE_01_FRONT_NEUTRAL_v005.png`
- checksum_sha256: `9ce4fd57e7d67cf98b0f4cb8ebea1636cbd4bfd9637e1851f7f9f07ece945673`
- dimensions: `1086x1448` (exact 3:4)
- QA_record: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v005/QA.md`
- user_decision: rejected; facial identity remains correct, but crown still reads top-down, Hairstyle A does not fully match DSC00847, and skin tone is slightly lighter than the B anchor; never use v005 as a pixel reference
