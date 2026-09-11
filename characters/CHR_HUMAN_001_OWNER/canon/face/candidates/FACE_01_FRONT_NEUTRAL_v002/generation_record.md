# FACE_01_FRONT_NEUTRAL_v002 — Generation Record

```yaml
candidate_id: FACE_01_FRONT_NEUTRAL_v002
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
asset_level: L1_CANDIDATE
gate: GATE_2_FACE
status: REJECTED_TECHNICAL_PREFLIGHT
approval_status: REJECTED
generation_tool: built_in_imagegen
spec_revision: draft_1.2
identity_md_revision: draft_0.2
reference_set_ids:
  - OWNER_FACE_APPEARANCE_L1
  - OWNER_HAIRSTYLE_A_L0
reference_count: 2
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
output_path: characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v002/FACE_01_FRONT_NEUTRAL_v002.png
qa_status: FAIL_REFERENCE_ROLE_LEAKAGE
```

## Reference responsibility

| Image | Asset ID | Responsibility | Must not define |
|---|---|---|---|
| `CHR_WOMAN_001_HB04_HAIR_B.jpg` | OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001 | strict target front-face appearance and skin tone | Hairstyle B, pink top, high camera angle, body, lighting, background |
| `source/identity/raw/DSC00847.jpg` | L0_OWNER_017 | HAIRSTYLE_A only | face identity/shape, skin, body, pink jacket, outdoor light/background |

## Prompt

Use case: identity-preserve  
Asset type: L1 Face Identity Canon candidate, FACE_01_FRONT_NEUTRAL v002  
Primary request: Create one new eye-level neutral studio portrait. Preserve the woman's target face and skin-tone appearance strictly from Image 1. Change the hairstyle to HAIRSTYLE_A using Image 2 only for hair. Do not blend Image 2's face into Image 1.  
Input images: Image 1 is the sole authority for recognizable front-face appearance, facial relationships and skin tone. Image 2 is the sole authority for HAIRSTYLE_A: long straight loose dark hair, near-center parting, natural low-to-moderate volume, long face-framing panels and tapered ends.  
Expression: neutral, relaxed, mouth closed, eyes looking straight at camera.  
Clothing: upper portion of the same plain pink high-cut one-piece Calibration Outfit swimsuit; no jacket, sweater, dress, jewelry or accessories.  
Scene/backdrop: seamless neutral light gray to gray-white studio.  
Composition: exact 3:4 portrait, eye-level, perfectly frontal, head and upper chest, top of hair fully visible, shoulders level.  
Camera: neutral 85–105mm-equivalent portrait perspective; remove Image 1's high-angle viewpoint and Image 2's outdoor perspective without changing the target face.  
Lighting: soft even neutral studio illumination, 5200–5600K appearance; preserve Image 1's target skin tone under neutral light, but do not copy its shadows or highlights.  
Constraints: same face as Image 1, HAIRSTYLE_A from Image 2, no intermediate third hairstyle, no face averaging, no beautification, no age change, no face slimming, no eye enlargement, no nose narrowing, no pointed chin, natural skin texture.  
Avoid: Hairstyle B, bun/updo, pulled-back calibration hair, Image 2's face or body, pink zip jacket, tank top, dramatic light, color cast, lens flare, text, watermark, collage, multiple views.  
Output contract: one image only, REVIEW_REQUIRED, not automatically Canon.

## Result

- generated_at: 2026-09-09
- output_path: `FACE_01_FRONT_NEUTRAL_v002.png`
- dimensions: 1086×1448 (3:4)
- checksum_sha256: `fc0534ddf622fcd1e0b2053c540a59c996c678ff72e28df6db4445f404dc75dd`
- QA_record: `QA.md`
- user_decision: NOT_REQUESTED — agent rejected before presentation because Image 2 face leaked into identity
