# FACE_01_FRONT_NEUTRAL_v001 — Generation Record

```yaml
candidate_id: FACE_01_FRONT_NEUTRAL_v001
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
asset_level: L1_CANDIDATE
gate: GATE_2_FACE
status: REJECTED
approval_status: REJECTED
generation_tool: built_in_imagegen
spec_revision: draft_1.1
identity_md_revision: draft_0.1
reference_set_ids:
  - OWNER_L0_FACE_FRONT_NEUTRAL
reference_count: 2
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
output_path: characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_01_FRONT_NEUTRAL_v001/FACE_01_FRONT_NEUTRAL_v001.png
qa_status: TECHNICAL_PASS_USER_IDENTITY_REVIEW_PENDING
```

## Reference responsibility

| Image | Asset ID | Responsibility | Must not define |
|---|---|---|---|
| `source/identity/raw/14.jpg` | L0_OWNER_012 | primary natural neutral frontal identity and feature placement | phone perspective, mixed lighting, hair, outfit, body, fine skin texture |
| `source/identity/raw/12.jpg` | L0_OWNER_010 | secondary neutral frontal relationship check | low camera angle, phone perspective, lighting, hair, outfit, body, fine detail |

## Prompt

Use case: photorealistic-natural  
Asset type: L1 Face Identity Canon candidate, FACE_01_FRONT_NEUTRAL  
Primary request: Generate exactly one neutral, front-facing studio identity portrait of the same adult woman shown in the two identity references. Faithfully reconcile her stable real facial identity across both references; do not beautify or redesign her face.  
Input images: Image 1 (`14.jpg`) is the primary natural frontal identity reference; Image 2 (`12.jpg`) is secondary support for frontal feature relationships. Neither image defines lighting, skin texture, hairstyle, clothing, body, background, or camera perspective.  
Subject: preserve a softly oval-to-rounded oval face, natural cheek fullness, gently tapering rounded jaw and chin, natural medium almond-shaped eyes with realistic spacing and subtle asymmetry, softly shaped brows, natural moderate nose with a softly rounded tip, and natural lips with a gently fuller lower lip. Same recognizable person, adult age unchanged.  
Expression: neutral, relaxed, mouth naturally closed, eyes looking straight at camera.  
Hair: non-story calibration hair only, dark hair simply pulled back away from the face to reveal forehead, temples, ears, jawline and facial outline; this is not HAIRSTYLE_A or HAIRSTYLE_B and is not authoritative for hair.  
Clothing: if visible in the head-and-upper-chest crop, show only the upper portion and straps of the same plain pink high-cut one-piece Calibration Outfit swimsuit; no other garment, jewelry, veil, sweater, jacket, dress, or accessories.  
Scene/backdrop: seamless neutral light gray to gray-white studio background.  
Style/medium: high-fidelity photorealistic neutral studio photography with natural pores and subtle real skin texture, no beauty-filter reinterpretation.  
Composition/framing: 3:4 portrait, eye-level camera, perfectly frontal head orientation, head and upper chest, top of head fully visible, head occupies roughly 65–72% of image height, shoulders level and symmetrical.  
Camera: neutral 85–105mm-equivalent portrait perspective, no wide-angle distortion, no high-angle or low-angle view.  
Lighting/mood: soft large-source studio light, low contrast, even facial illumination, neutral 5200–5600K white balance, no dramatic shadow, colored light, rim glow, lens flare, or inherited light patches.  
Authoritative for: front neutral face identity geometry only.  
Must not define: final hairstyle, body proportions, skin-color Canon, makeup Canon, outfit design, background style, or expression variants.  
Avoid: face slimming, pointed chin, enlarged eyes, narrowed nose, age change, doll-like face, plastic skin, excessive smoothing, heavy makeup, asymmetric camera angle, head tilt, smile, open mouth, visible teeth, stylized rendering, text, logo, watermark, collage, multiple views, extra people.  
Output contract: one image only; candidate status REVIEW_REQUIRED; do not label or imply approval.

## Result

- generated_at: 2026-09-09
- output_path: `FACE_01_FRONT_NEUTRAL_v001.png`
- dimensions: 1086×1448 (3:4)
- checksum_sha256: `d18ca9e54d41460e0c6a3c3573e680496dd6c31ffb202a06a1e3578e0785907a`
- QA_record: `QA.md`
- user_decision: REJECTED — wrong target appearance and wrong non-B hairstyle policy
