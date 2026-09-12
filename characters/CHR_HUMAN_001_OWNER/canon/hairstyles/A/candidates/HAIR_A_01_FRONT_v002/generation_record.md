# HAIR_A_01_FRONT_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.56
identity_md_revision: draft_0.48
hairstyle_document: canon/hairstyles/A/HAIRSTYLE.md
asset_id: HAIR_A_01_FRONT
candidate_id: HAIR_A_01_FRONT_v002
gate: "Gate 4 — Hairstyle Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
reference_count: 2
previous_ai_hairstyle_a_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/candidates/HAIR_A_01_FRONT_v002/HAIR_A_01_FRONT_v002.png"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png"
current_promoted_checksum_sha256: "18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219"
checksum_sha256: "18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user reviewed v001 and stated that the nose looked slightly too large while the other visible directions were acceptable. v002 is a fresh parallel generation from the same approved Face Master and deterministic Hairstyle-A L0 derivative. v001 pixels are not supplied. Its accepted hairstyle attributes are retained only as written review intent, while the approved Face Master remains the sole facial authority. The v001 framing failure is also corrected by showing every hair tip with clear space below.

## Reference plan

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`: defines the approved front-neutral identity, including the exact established nose bridge width, nose-tip volume, alar width and overall nose projection, plus skin tone, neutral closed-mouth expression and visual eye-level head projection. It cannot define final Hairstyle-A length/ends, body, outfit, lighting or background.
2. Image 2 / `OWNER_HAIRSTYLE_A_FACE_MASKED_001`: deterministic derivative of `L0_OWNER_017`; defines only the near-center part, long straight loose direction, low-to-moderate crown volume, long face-framing panels, dark-brown color relationship, below-chest length, subtle natural irregularity and tapered ends. Its mask, identity, skin, jacket, body, outdoor colors and background are excluded.

## Candidate authority

- Hairstyle A front presentation only: front hairline/near-center part, crown volume, straight texture, face-framing panels, complete visible length, density, tapered ends and restrained highlights;
- the nose correction restores approved Face geometry and does not grant this Hair candidate any face authority;
- no authority for face identity, body, outfit design, side/back hair structure, Hairstyle B, lighting, background or Canon status.

## Prompt assembly

```text
Use case: identity-preserve. Asset: HAIR_A_01_FRONT_v002, one adult technical hairstyle reference for CHR_HUMAN_001_OWNER, Identity draft_0.48 and spec draft_1.56. Generate independently from the two source references; do not use v001 pixels.

Image 1 (`OWNER_FACE_FRONT_NEUTRAL_CANON_L1`, path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`) is the sole face authority. Match the exact approved person and especially restore Image 1's existing natural nose proportions: same bridge width, restrained nose-tip volume, alar width and frontal projection. Do not enlarge, broaden, sharpen or redesign the nose. Image 2 (`OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`, path `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`) defines only Hairstyle A: near-center part, long straight loose dark-brown hair, low-to-moderate crown volume, long face-framing front panels, fine natural irregularity and tapered below-chest ends. Ignore its mask, person, jacket, body, color cast and background.

Squarely front-facing at true visual eye level, neutral head, eyes forward, mouth naturally closed, level shoulders. Preserve the accepted hairstyle direction in written form: a short narrow near-center part, natural hairline, controlled non-puffy crown, straight smooth lengths with fine strands, two long front panels falling naturally over both shoulders and chest, believable density, restrained dark-brown tonal variation, slight natural asymmetry and tapered irregular ends. No bangs, waves, curls, short layers, ear tucks, ponytail, braid, bun, extensions, excessive volume, wet look, plastic shine, red/purple cast or Hairstyle-B elements.

Exact 3:4 portrait with a deliberately wider head-through-upper-waist crop. Make the head smaller in frame than v001. Show the complete top, both outer hair edges and every longest left/right hair tip, plus an unmistakable 5–8% clear band of pink outfit/background below all tips; absolutely no hair touches or exits the bottom boundary. 85–105mm-equivalent camera at eye height, horizontal optical axis, neutral gray-white studio, soft even 5200–5600K light, realistic skin and hair. Only the upper portion of the plain opaque pink Calibration Outfit is visible. No props, text, logo, watermark, collage or multiple views. Hairstyle is the only review authority; do not alter face, skin, age, body or outfit. Produce one REVIEW_REQUIRED image only.
```

## Attempt result

- generated_at: `2026-09-12`
- result: one 1086x1448 exact-3:4 PNG generated and saved at the declared project output path
- built_in_output: `/home/verdvana/.codex/generated_images/01a09467-3db0-70a2-bf86-1fb58ecbbfb6/exec-97ba0918-3cbf-465b-a171-db2da1f198b9.png`
- project_candidate_checksum_sha256: `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`
- technical_precheck: nose bridge/tip/alar presentation is visibly more restrained than v001 and broadly returns toward the approved Face Master without granting new face authority; standard front direction, neutral eye-level pose, near-center part, controlled crown volume, long straight panels, natural asymmetry and dark-brown highlights pass; every visible hair tip is complete with clear pink-outfit/background space below, correcting the v001 framing failure; exact identity and hairstyle match remain user-review items
- promotion_status: promoted unchanged after explicit user approval

## User approval

On 2026-09-12 the user stated: “可以的，登记吧”. The candidate was promoted unchanged to `OWNER_HAIR_A_01_FRONT_CANON_001`. Approval covers only the scoped standard front Hairstyle-A attributes and complete front-view length/end presentation. Visible face and nose remain governed by the approved Face component; this approval does not lock the complete `owner_v1.0`.
