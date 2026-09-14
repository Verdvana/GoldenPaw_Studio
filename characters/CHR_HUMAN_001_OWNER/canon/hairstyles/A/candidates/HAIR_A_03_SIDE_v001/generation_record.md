# HAIR_A_03_SIDE_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.153
identity_md_revision: draft_0.141
hairstyle_document: canon/hairstyles/A/HAIRSTYLE.md
asset_id: HAIR_A_03_SIDE
candidate_id: HAIR_A_03_SIDE_v001
gate: "Gate 4 — Hairstyle Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_LEFT_PROFILE_NEUTRAL_CANON_L1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
reference_count: 2
previous_ai_hairstyle_a_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_03_SIDE/OWNER_HAIR_A_03_SIDE_CANON_001.png"
checksum_sha256: "3f1e9b07b7342f5ab1636d723c06fcbb299833d8ddaa521575711bb056ee2930"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user requested the next asset after approving `HAIR_A_02`. This authorizes exactly one `HAIR_A_03_SIDE_v001` candidate. The general plan does not assign a side, so this record fixes the candidate as anatomical-left true profile with the nose pointing image-right, matching the established `FACE_04_LEFT_PROFILE_NEUTRAL` naming. It is built in parallel from one approved profile Face Master and one deterministic L0 hair-only derivative. No `HAIR_A_01`, `HAIR_A_02`, other generated Hair raster, Expression, Pose or Shot is supplied.

## Reference responsibilities

1. `OWNER_FACE_LEFT_PROFILE_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_04_LEFT_PROFILE_NEUTRAL/OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001.jpg`
   - SHA-256: `b6c1d513a4ce8f32d70860de2dde2816ef5f1400c82e09f4550b96e9545798c4`
   - responsibility: approved owner identity in anatomical-left true profile, nose pointing image-right; eye-level head projection, forehead–nose–lip–chin silhouette, ear position, jaw–neck relation, natural skin tone and neutral closed-mouth expression.
   - evidence limitation: the fine profile silhouette is a user-approved constrained reconstruction without a matching-direction true-profile L0 verification image.
   - must_not_define: Hairstyle-A design, length, ends, final hairline/ear-side arrangement, body, outfit design, lighting or background; visible hair is context only and has no independent Hair authority.
2. `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`
   - SHA-256: `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`
   - responsibility: Hairstyle A only—near-center part, long straight loose dark-brown direction, low-to-moderate crown volume, long face-framing panels, believable density, below-chest length, restrained highlights, subtle strand irregularity and tapered ends.
   - must_not_define: gray mask, face/identity, skin, body, pink jacket, outdoor color cast, lighting or background.

Reference budget: 2 images. No previously generated Hairstyle-A raster is attached.

## Candidate authority

- only the anatomical-left standard-side Hairstyle-A silhouette: side-projected part/hairline, ear-side relationship, crown and rear-head contour, front/rear hair-mass depth, straight loose fall, full length, density, tonal response and tapered ends;
- no authority for face identity/geometry, skin, expression, body, outfit design, other Hair-A views, Hairstyle B, lighting, background or Canon status.

## Prompt assembly

```text
Use case: identity-preserve. Asset: HAIR_A_03_SIDE_v001, one adult technical hairstyle reference for CHR_HUMAN_001_OWNER, Identity draft_0.141 and spec draft_1.153. Generate independently from the two declared references; do not use approved HAIR_A_01/02 pixels or any generated Hair candidate.

Image 1 (`OWNER_FACE_LEFT_PROFILE_NEUTRAL_CANON_L1`) is the sole identity and viewpoint authority: preserve the exact approved person in anatomical-left true profile, nose pointing image-right, approximately 85–90 degrees from front, true eye-level neutral head, natural skin tone, one principal eye visible, relaxed forward gaze and naturally closed mouth. Preserve the approved forehead–nose–lip–chin silhouette, ear position and jaw–neck relation. Its visible hair is context only and must not independently define the final hairstyle. Image 2 (`OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`) defines only Hairstyle A: a short narrow near-center part, natural hairline, low-to-moderate non-puffy crown, long straight loose dark-brown hair, long face-framing front panels, smooth lengths with fine natural irregularity, believable density, restrained highlights, below-chest length and naturally tapered irregular ends. Ignore its gray mask, person, jacket, body, outdoor cast and background.

Project the fixed Hairstyle-A design naturally into this left-profile view. Keep the forehead hairline readable; show a believable ear-side transition with part of the near ear visible through or beside fine strands, and show the rear cranial contour plus the depth of hair falling behind the shoulder. A narrow front panel may follow the cheek/jaw, but it must not cover the principal eye or obscure the approved forehead–nose–lip–chin silhouette. Hair falls freely over and behind the shoulders with realistic depth and slight strand irregularity. No ear-tuck redesign, bangs, waves, curls, short layers, ponytail, braid, bun, extensions, excessive volume, wet look, plastic shine, red/purple cast or any Hairstyle-B element.

Exact 3:4 portrait, true eye-level 85–105mm perspective, head-through-upper-waist crop. Show the complete crown, front and rear outer hair edges, and every longest hair tip with an unmistakable 5–8% clear band below all tips; no hair touches or exits the bottom or side boundaries. Neutral gray-white seamless studio, soft even 5200–5600K light, realistic skin and hair. Only the upper portion of the same plain opaque pink Calibration Outfit is visible. No props, text, logo, watermark, collage or multiple views. Hairstyle is the only review authority; do not alter face, skin, age, body or outfit. Produce one REVIEW_REQUIRED image only.
```

## QA status

### Attempt 1

- result: generated successfully from the two declared scoped references; no previously generated Hair raster was supplied.
- output: 1086x1448 RGB PNG, exact 3:4.
- built-in output: `/home/verdvana/.codex/generated_images/01a09edc-9182-7031-a3e5-d4b1ec7d7e75/exec-a8d2b124-2248-4ede-b84f-b9cb3e60f52b.png`
- project output: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/candidates/HAIR_A_03_SIDE_v001/HAIR_A_03_SIDE_v001.png`
- SHA-256: `3f1e9b07b7342f5ab1636d723c06fcbb299833d8ddaa521575711bb056ee2930`

## Visual QA result

- PASS: exact 3:4 single-view composition; anatomical-left true profile with nose pointing image-right and neutral eye-level head projection.
- PASS: short side-projected near-center part, natural readable hairline, low-to-moderate crown, near-ear visibility, believable rear-head contour and clear front/rear hair-mass depth.
- PASS: the principal eye and approved forehead–nose–lip–chin silhouette remain unobscured by the narrow face-side strands.
- PASS: long straight loose dark-brown fall, restrained highlights, natural strand irregularity, below-chest length and tapered irregular ends; crown, front/rear outer edges and every longest tip remain inside the frame with clear lower space.
- PASS: only the pink Calibration Outfit upper portion appears; no source jacket, outdoor background, text, logo, watermark or Hairstyle-B element is present.
- exact identity and final hairstyle match remain user-review decisions. Candidate stays `REVIEW_REQUIRED` and gains no Canon/downstream authority before explicit approval.

## User approval and promotion

- user statement: “批准”
- decision date: 2026-09-14
- decision: `APPROVED`
- promoted asset ID: `OWNER_HAIR_A_03_SIDE_CANON_001`
- physical operation: `MOVE`
- original candidate path/checksum: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/candidates/HAIR_A_03_SIDE_v001/HAIR_A_03_SIDE_v001.png` / `3f1e9b07b7342f5ab1636d723c06fcbb299833d8ddaa521575711bb056ee2930`
- current approved path/checksum: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_03_SIDE/OWNER_HAIR_A_03_SIDE_CANON_001.png` / unchanged
- candidate raster retained: `NO`
- approval record: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_03_SIDE/approvals/APPROVAL_OWNER_HAIR_A_03_SIDE_001.md`
- full Canon lock: `NO`
