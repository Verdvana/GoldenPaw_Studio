# FACE_01_FRONT_NEUTRAL_v006 — Generation Record

```yaml
candidate_id: FACE_01_FRONT_NEUTRAL_v006
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
asset_level: L1_CANDIDATE
gate: GATE_2_FACE
status: SUPERSEDED_REVISION_REQUIRED
approval_status: REJECTED
generation_tool: built_in_imagegen
spec_revision: draft_1.5
identity_md_revision: draft_0.5
pixel_reference_set_ids:
  - OWNER_FACE_APPEARANCE_L1_CROPPED_DERIVATIVE
  - OWNER_HAIRSTYLE_A_L0
pixel_reference_count: 2
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
output_path: characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v006/FACE_01_FRONT_NEUTRAL_v006.png
qa_status: PARTIAL_PASS_HAIR_CAMERA_FAIL_FACE_SKIN_MATCH
```

## Reference responsibility

| Input | Responsibility | Explicit exclusion |
|---|---|---|
| Image 1 — `B_FACE_SKIN_CROP.png` | exact user-accepted face and B-anchor skin tone only | crown, full hair design, source camera/head pose, body, outfit, lighting/background |
| Image 2 — `L0_OWNER_017` / `DSC00847.jpg` | exact Hairstyle A structure only | face, skin, body, clothing, outdoor camera/light/background |

No generated Face candidate is supplied. Image 1 is a crop-only derivative with provenance and no independent authority.

## Prompt strategy

- remove the B source's crown pixels so they cannot directly seed another top-down crown;
- reproduce DSC00847's specific hair construction rather than a generic long straight hairstyle;
- use a subtle 1–2° upward optical compensation to counter the repeatedly inherited high-camera bias while requiring the final image to read neutral, not low-angle;
- explicitly match the B crop's skin luminance and warm-neutral chroma, prohibiting studio-light whitening.

## Prompt assembly

Generate one photorealistic `FACE_01_FRONT_NEUTRAL_v006`. Image 1 defines only the exact recognizable face, facial relationships, age, texture and B-anchor skin tone; match its luminance and warm-neutral chroma without whitening. Image 2 defines only Hairstyle A: very flat close-to-scalp roots, low crown, near-center naturally imperfect part, narrow upper silhouette, straight loose dark-brown lengths, fine separated strands, modest asymmetry, slim face-framing locks and tapered wispy uneven ends. Apply a corrective camera position 2–3 cm below pupil midpoint with only 1–2° upward pitch so the final portrait reads neutral eye-level. Show the crown from the front with almost no horizontal top surface, no overhead oval plane and no long receding scalp part. The face, forehead, hairline, cranium, crown, ears and jaw must share one projection. Pink calibration swimsuit upper portion, neutral gray-white studio, soft even 5200–5600K light, 100–105mm-equivalent perspective, exact 3:4, no generated candidate reference, no beautification, text or collage.

## Result

- generated_at: 2026-09-10
- output_path: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v006/FACE_01_FRONT_NEUTRAL_v006.png`
- checksum_sha256: `f5ad905ec349ffda3078d53d9d99d14599535b63e80a2e106d451c44c493a0b8`
- dimensions: `1086x1448` (exact 3:4)
- QA_record: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v006/QA.md`
- user_decision: rejected as a whole; Hairstyle A and visual eye-level angle accepted, identity direction still correct, but facial details and skin tone are slightly mismatched; never use v006 as a pixel reference
