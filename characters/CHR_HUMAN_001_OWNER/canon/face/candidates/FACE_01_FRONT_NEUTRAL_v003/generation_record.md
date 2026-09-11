# FACE_01_FRONT_NEUTRAL_v003 — Generation Record

```yaml
candidate_id: FACE_01_FRONT_NEUTRAL_v003
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
asset_level: L1_CANDIDATE
gate: GATE_2_FACE
status: SUPERSEDED_REVISION_REQUIRED
approval_status: REJECTED
generation_tool: built_in_imagegen
spec_revision: draft_1.2
identity_md_revision: draft_0.2
pixel_reference_set_ids:
  - OWNER_FACE_APPEARANCE_L1
text_derived_design_sources:
  - OWNER_HAIRSTYLE_A_L0
pixel_reference_count: 1
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
output_path: characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v003/FACE_01_FRONT_NEUTRAL_v003.png
qa_status: FAIL_CAMERA_HEAD_POSE
```

## Reference responsibility

| Input | Asset ID | Responsibility | Must not define |
|---|---|---|---|
| Pixel Image 1: `CHR_WOMAN_001_HB04_HAIR_B.jpg` | OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001 | strict target face, facial relationships, apparent age and skin tone | Hairstyle B, top, high camera angle, lighting, background |
| Text-derived A specification originally analyzed from `DSC00847.jpg` | L0_OWNER_017 | long straight loose A hairstyle only | no pixels supplied; cannot leak its face/body/skin |

## Prompt

Use case: identity-preserve. Edit the visual identity from the sole supplied image into a neutral eye-level Face Canon portrait. Preserve the exact recognizable face, facial proportions, feature relationships, apparent adult age and skin-tone appearance from Image 1. Change only the hairstyle, camera viewpoint, neutral studio setup, expression precision and Calibration Outfit presentation. HAIRSTYLE_A is specified in text from the separately analyzed real reference: long straight loose dark-brown hair, near-center part, natural low-to-moderate crown volume, long face-framing panels, length extending below the chest, subtle natural straight-hair irregularity and tapered ends. No bun, no updo, no pulled-back hair and no hybrid style. Neutral closed-mouth expression, eyes straight to camera. Plain pink high-cut one-piece Calibration Outfit upper portion only. Exact 3:4, eye-level, perfectly frontal, head and upper chest, neutral 85–105mm perspective, seamless gray-white background, soft even 5200–5600K studio illumination, natural skin texture. Preserve Image 1's face even while correcting its high-angle camera; do not redesign or average identity. Avoid face slimming, age change, enlarged eyes, narrowed nose, pointed chin, beauty filter, heavy makeup, Image 1 Hairstyle B, tank-top reinterpretation, dramatic light, color cast, text, watermark, collage or multiple views. One REVIEW_REQUIRED candidate only.

## Result

- generated_at: 2026-09-09
- output_path: `FACE_01_FRONT_NEUTRAL_v003.png`
- dimensions: 1086×1448 (3:4)
- checksum_sha256: `b5ac623403acb6e64096e4eef8ab69520d1baca476a4f80f58f8a27bf8b1cda2`
- QA_record: `QA.md`
- user_decision: REVISE — face/skin correct; camera remains slightly high and subject slightly looks upward
