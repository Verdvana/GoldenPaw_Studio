# HAIR_A_01_FRONT_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.54
identity_md_revision: draft_0.47
hairstyle_document: canon/hairstyles/A/HAIRSTYLE.md
asset_id: HAIR_A_01_FRONT
candidate_id: HAIR_A_01_FRONT_v001
gate: "Gate 4 — Hairstyle Canon"
model_tool: "built-in image_gen"
status: GENERATED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
reference_count: 2
previous_ai_hairstyle_a_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/candidates/HAIR_A_01_FRONT_v001/HAIR_A_01_FRONT_v001.png"
checksum_sha256: "3e36844b25777245d81233a54e2a15493c7b880bded2dbaa15f06c73ccccb912"
qa_status: FAIL_FRAMING_REVIEW_REQUIRED
```

## Authorization and lineage

The user explicitly requested the next asset after all six Body components were approved. Gate 4 is open and the ordered first Hairstyle-A item is `HAIR_A_01_FRONT`. This is a fresh parallel generation from an approved scoped Face Master plus one deterministic derivative of the immutable Hairstyle-A L0 source. No Body image, Hairstyle-B image, prior Hairstyle-A candidate, previous shot, mirror or episode asset is an input.

## Reference plan

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`: defines the approved front-neutral owner identity, facial geometry, natural skin-tone appearance, neutral closed-mouth expression, and visual eye-level head/crown projection. Although visible hair is present, this input cannot independently define the final Hairstyle-A Canon geometry, hair length, side/back structure, outfit, body, lighting or background.
2. Image 2 / `OWNER_HAIRSTYLE_A_FACE_MASKED_001`: deterministic derivative of `L0_OWNER_017` (`DSC00847.jpg`); defines only Hairstyle A's near-center part, long straight loose direction, low-to-moderate crown volume, long face-framing front panels, dark-brown color relationship, below-chest length, subtle natural irregularity and tapered ends. Its gray face mask, head/face identity, skin, visible jacket, body, outdoor color cast, highlights and background are excluded.

## Candidate authority

- Hairstyle A front presentation only: front hairline/near-center part, crown volume, straight texture, face-framing panels, visible length, density, tapered ends and restrained neutral-studio highlights;
- no authority for face identity, skin tone, expression, body, outfit design, side/back hair structure, high/low-camera behavior, Hairstyle B, lighting, background or Canon status.

## Prompt assembly

```text
Use case: identity-preserve. Asset: HAIR_A_01_FRONT_v001, one adult technical hairstyle reference for CHR_HUMAN_001_OWNER, Identity draft_0.47 and spec draft_1.54. Create one new front-view L1 Hairstyle-A candidate in parallel; use no prior Hair candidate.

Image 1 (`OWNER_FACE_FRONT_NEUTRAL_CANON_L1`, path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`) defines only the approved front-neutral face identity, natural skin tone, closed-mouth neutral expression and standard eye-level head projection. Preserve the same person exactly. Image 2 (`OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`, path `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`) defines only Hairstyle A: a near-center part, long straight loose dark-brown hair, low-to-moderate crown volume, long face-framing front panels, subtle natural strand irregularity, length extending below the chest and naturally tapered uneven ends. Ignore its gray face mask, person, skin, jacket, body, outdoor colors, highlights and background.

Show the adult character squarely front-facing at true visual eye level, head neutral, eyes forward, mouth naturally closed, shoulders level. The hairstyle is the only review authority. Reproduce Hairstyle A specifically rather than a generic long-hair category: narrow near-center part visible only over the short frontal scalp region, natural hairline, controlled non-puffy crown, straight smooth lengths with fine individual strands, two long front panels falling naturally along both sides of the face and over the shoulders/chest, believable density, restrained dark-brown tonal variation, and tapered slightly irregular ends. Keep both sides natural rather than perfectly mirrored. No bangs, curtain bangs, waves, curls, bob shape, layers that shorten the front, tucked-behind-ear styling, ponytail, braid, bun, extensions, excessive volume, wet look, plastic shine, red/purple cast or Hairstyle-B elements.

Use an exact 3:4 portrait crop from complete head top through enough upper torso to show every visible hair end with 5–8% breathing room; no hair edge or tip cropped. 85–105mm-equivalent camera at eye height, horizontal optical axis, neutral gray-white seamless studio, soft even 5200–5600K light and realistic skin/hair texture. The only visible clothing is the upper portion of the same plain opaque pink Calibration Outfit one-piece; do not copy the source jacket. No props, scenery, text, logo, watermark, collage or multiple views. Do not beautify or alter the face, skin, age, body or outfit. Produce one REVIEW_REQUIRED image only.
```

## Attempt result

- generated_at: `2026-09-12`
- result: one 1086x1448 exact-3:4 PNG generated and saved at the declared project output path
- built_in_output: `/home/verdvana/.codex/generated_images/01a09467-3db0-70a2-bf86-1fb58ecbbfb6/exec-a2fe7616-fb03-4fc3-8ef7-33d73cd6ea47.png`
- project_candidate_checksum_sha256: `3e36844b25777245d81233a54e2a15493c7b880bded2dbaa15f06c73ccccb912`
- technical_precheck: standard front direction, neutral expression, eye-level intent, near-center part, controlled crown volume, long straight front panels, natural asymmetry, restrained dark-brown highlights and Calibration-Outfit upper portion pass; framing fails because the longest hair tips meet and are clipped by the bottom image boundary, so full length and tapered ends cannot be inspected; identity and exact hair match remain user-review items
- promotion_status: not promoted; explicit user decision required, and technical correction is recommended before Canon approval
