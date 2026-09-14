# HAIR_A_02_3Q_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.150
identity_md_revision: draft_0.138
hairstyle_document: canon/hairstyles/A/HAIRSTYLE.md
asset_id: HAIR_A_02_3Q
candidate_id: HAIR_A_02_3Q_v001
gate: "Gate 4 — Hairstyle Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
reference_count: 2
previous_ai_hairstyle_a_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_02_3Q/OWNER_HAIR_A_02_3Q_CANON_001.png"
checksum_sha256: "160fd3c30c2756d438877ee6508a3e424ec96aaecde84917610a92196e759919"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user requested returning to the remaining list in order, beginning with Hairstyle A. This authorizes exactly one `HAIR_A_02_3Q_v001` candidate. It is generated in parallel from the approved left-three-quarter Face Master and the deterministic face-masked L0 Hairstyle-A derivative. `HAIR_A_01` approved pixels and all Hair candidates, Expressions, Poses and Shots are excluded.

## Reference responsibilities

1. `OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg`
   - SHA-256: `3f50c08e2993aa8dd406abd093d24f8a581b6e1475aa4dd57bda3884fed3b745`
   - responsibility: approved owner anatomical-left 3/4 identity, face direction toward image-left, eye-level head projection, natural skin tone and neutral closed-mouth expression.
   - must_not_define: Hairstyle-A design/length/ends, body, outfit design, lighting or background; its visible hair is context only and has no independent Hair authority.
2. `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`
   - SHA-256: `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`
   - responsibility: Hairstyle A only—near-center part, long straight loose dark-brown direction, low-to-moderate crown volume, long face-framing panels, believable density, chest-below length, subtle strand irregularity and tapered ends.
   - must_not_define: gray mask, face/identity, skin, body, pink jacket, outdoor color cast, lighting or background.

Reference budget: 2 images. No prior generated Hair raster is attached.

## Candidate authority

- only the anatomical-left 3/4 Hairstyle-A silhouette, part projection, crown volume, face-side relationship, straight loose fall, complete length, density, tonal response and tapered ends;
- no authority for face identity/geometry, skin, expression, body, outfit design, other Hair-A views, Hairstyle B, lighting, background or Canon status.

## Prompt assembly

```text
Use case: identity-preserve. Asset: HAIR_A_02_3Q_v001, one adult technical hairstyle reference for CHR_HUMAN_001_OWNER, Identity draft_0.138 and spec draft_1.150. Generate independently from the two declared references; do not use approved HAIR_A_01 pixels or any generated Hair candidate.

Image 1 (`OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1`) is the sole identity and viewpoint authority: preserve the exact approved person, anatomical-left facial plane principally visible, face pointing image-left, approximately 35–45-degree left 3/4 turn, true eye-level neutral head, natural skin tone, relaxed eyes and naturally closed mouth. Its visible hair is context only and must not independently define the final hairstyle. Image 2 (`OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`) defines only Hairstyle A: a short narrow near-center part, natural hairline, low-to-moderate non-puffy crown, long straight loose dark-brown hair, long face-framing panels, smooth lengths with fine natural irregularity, believable density, restrained highlights, below-chest length and naturally tapered irregular ends. Ignore its gray mask, person, jacket, body, outdoor cast and background.

Show how the fixed Hairstyle-A design projects at this left 3/4 angle: the near-side and far-side front panels follow the turned face naturally without hiding the eyes, nose, mouth or jaw; the far contour remains visible; hair falls freely over and behind the shoulders with realistic depth, slight natural asymmetry and no ear-tuck redesign. Do not introduce bangs, waves, curls, short layers, ponytail, braid, bun, extensions, excessive volume, wet look, plastic shine, red/purple cast or any Hairstyle-B element.

Exact 3:4 portrait, true eye-level 85–105mm perspective, head-through-upper-waist crop. Show the complete crown, both outer hair edges, every longest left/right hair tip and an unmistakable 5–8% clear band below all tips; no hair touches or exits the bottom or side boundaries. Neutral gray-white seamless studio, soft even 5200–5600K light, realistic skin and hair. Only the upper portion of the same plain opaque pink Calibration Outfit is visible. No props, text, logo, watermark, collage or multiple views. Hairstyle is the only review authority; do not alter face, skin, age, body or outfit. Produce one REVIEW_REQUIRED image only.
```

## QA status

### Attempt 1

- result: generated successfully from the two declared scoped references; no previous generated Hair raster was supplied.
- output: 1086x1448 RGB PNG, exact 3:4.
- built-in output: `/home/verdvana/.codex/generated_images/01a09edc-9182-7031-a3e5-d4b1ec7d7e75/exec-4d63bc9b-cfe1-42cd-888d-a89d97e67616.png`
- project output: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/candidates/HAIR_A_02_3Q_v001/HAIR_A_02_3Q_v001.png`
- SHA-256: `160fd3c30c2756d438877ee6508a3e424ec96aaecde84917610a92196e759919`

## Visual QA result

- PASS: exact 3:4 single-view composition, anatomical-left approximately 35–45-degree 3/4 direction and neutral eye-level head projection.
- PASS: near-center short part, controlled low-to-moderate crown, readable near/far contours, long straight loose face-side panels, restrained dark-brown tonal variation and naturally tapered irregular ends.
- PASS: complete crown, outer side edges and all longest hair tips remain inside the frame; no hair edge is clipped.
- NOTE: clear space below the longest near-side tips is narrower than the prompted ideal 5–8%, but the full tips remain visibly complete and technically reviewable.
- PASS: only the pink Calibration Outfit upper portion appears; no source jacket, outdoor background, text, logo or Hairstyle-B element is present.
- identity and exact hairstyle match remain user-review decisions. Candidate stays `REVIEW_REQUIRED` and gains no Canon/downstream authority before explicit approval.

## User approval and promotion

- user statement: “不错，合格”
- decision date: 2026-09-14
- decision: `APPROVED`
- promoted asset ID: `OWNER_HAIR_A_02_3Q_CANON_001`
- physical operation: `MOVE`
- original candidate path/checksum: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/candidates/HAIR_A_02_3Q_v001/HAIR_A_02_3Q_v001.png` / `160fd3c30c2756d438877ee6508a3e424ec96aaecde84917610a92196e759919`
- current approved path/checksum: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_02_3Q/OWNER_HAIR_A_02_3Q_CANON_001.png` / unchanged
- candidate raster retained: `NO`
- approval record: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_02_3Q/approvals/APPROVAL_OWNER_HAIR_A_02_3Q_001.md`
- full Canon lock: `NO`
