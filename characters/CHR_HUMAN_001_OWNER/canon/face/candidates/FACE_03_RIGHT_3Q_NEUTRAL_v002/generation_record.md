# FACE_03_RIGHT_3Q_NEUTRAL_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.17
identity_md_revision: draft_0.16
asset_id: FACE_03_RIGHT_3Q_NEUTRAL
candidate_id: FACE_03_RIGHT_3Q_NEUTRAL_v002
gate: "Gate 2 — Face Identity Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_L0_FACE_RIGHT_3Q_LIMITED
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
reference_count: 3
prompt_basis: "FACE_03 v001 prompt plus one chin-only refinement"
seed_settings: "built-in image_gen; seed and detailed settings not returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_03_RIGHT_3Q_NEUTRAL_v002/FACE_03_RIGHT_3Q_NEUTRAL_v002.png"
pixel_storage_status: "MOVED_TO_CANON_THEN_TRANSCODED; CANDIDATE_RASTER_REMOVED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_03_RIGHT_3Q_NEUTRAL/OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001.jpg"
qa_status: PASS_USER_APPROVED
```

## Reference plan

Identical to v001 and in the same order: approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` for exact identity; low-resolution real `L0_OWNER_012` only for anatomical-right/image-right direction, natural asymmetry and coarse depth; `OWNER_HAIRSTYLE_A_FACE_MASKED_001` only for Hairstyle A. v001 is not supplied.

## Single permitted change

Make the bottom central curve of the chin more softly rounded and less pointed. Preserve chin vertical length, forward projection, jaw width, jaw angle, lower-lip position and all other facial geometry. Do not shorten, widen, recess, swell or infantilize the chin.

## Final assembled prompt

Use case: identity-preserve

Asset type: `FACE_03_RIGHT_3Q_NEUTRAL`, L1 Face Canon candidate v002 for `CHR_HUMAN_001_OWNER`, governed by `OWNER_L1_GENERATION_SPEC` draft_1.17 and `OWNER_IDENTITY_ANCHOR` draft_0.16.

Input images: Image 1 is the approved front-neutral Face Canon and has highest authority for the exact recognizable woman, skull and facial-feature relationships, adult age, neutral-studio skin tone, fine facial geometry and neutral expression. Image 2 is a low-resolution real same-person image pointing image-right; it is authoritative only for the anatomical right facial plane, real face-points-image-right direction, natural right-side asymmetry and coarse orbital/nose/cheek/jaw depth. It must never override Image 1's fine geometry or lens-neutral proportions. Image 3 is a source-derived masked Hairstyle A reference and is authoritative only for hair. Resolve every identity conflict in favor of Image 1.

Create exactly one new photorealistic right-three-quarter neutral portrait. Turn the head approximately 35–40 degrees toward image-right so the anatomical right facial plane is principally visible. Keep the eyes looking toward the camera, mouth naturally closed and expression neutral with a gentle, relaxed gaze. Reconstruct the real opposite facial view; do not mirror an image-left face and do not copy or continue any previous AI candidate.

Preserve exactly the same recognizable woman as Image 1: skull proportions, eye spacing, brows, natural medium almond eye size and shape, nose, soft lips, naturally full cheeks, softly restrained cheekbones, rounded jaw transition, adult age, skin tone and natural asymmetry. Use Image 2 only to reveal genuine right-side direction/asymmetry and coarse depth. Do not inherit its low resolution, phone perspective, camera angle, facial simplification, skin color, mixed light, hair, black clothing or industrial background. Image 3 must not influence face, skin, skull, body, clothing, light or background. Make one and only one refinement: give the bottom central contour of the chin a more softly rounded, less pointed curve. Preserve the exact chin vertical length and forward projection, jaw width, jaw angle, lower-lip position and every other facial feature. Do not make the chin short, broad, heavy, recessed, swollen, doubled or childlike.

Hairstyle A only: near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels, subtle strand irregularity and tapered ends. No bun, updo, Hairstyle B or A/B hybrid.

Exact 3:4 portrait; head top to upper chest; head approximately 65–72% of frame height; 85–105mm-equivalent perspective; camera at eye height with a horizontal optical axis; upright neutral head; coherent forehead, hairline, skull, crown, ears, jaw and chin projection. Neutral gray-white seamless studio, soft even low-contrast 5200–5600K light, neutral white balance and natural photographic skin texture. If clothing is visible, show only the authentic upper portion of the pink high-cut one-piece Calibration Outfit, not a tank top or other garment.

Avoid mirroring, face pointing image-left, identity averaging, generic face, low-resolution feature loss, phone-camera distortion, face widening or slimming, enlarged eyes, narrowed nose, pointed chin, shortened or widened chin, changed jaw, high/sharp cheekbones, intense stare, smile, parted lips, age change, beauty filtering, whitening, heavy makeup, source styling leakage, wide-angle or top-down distortion, text, watermark, collage and multiple views.

One candidate image only. `REVIEW_REQUIRED`; do not label or imply Canon approval.

## Generation settings/result

- generated_at: `2026-09-10T15:59:47+08:00`
- seed/settings: built-in `image_gen`; seed and detailed settings were not returned
- source output: `/home/verdvana/.codex/generated_images/01a089e9-1904-7443-9200-afbaa6608bae/exec-c830b8ca-39d1-474c-abe3-4306dd68f12f.png`
- original output path: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_03_RIGHT_3Q_NEUTRAL_v002/FACE_03_RIGHT_3Q_NEUTRAL_v002.png` (record only; raster removed after promotion)
- output_dimensions: `1086x1448`
- output_checksum: `f88def7d4e88ad6fcd08a1aef36456bb0a04e1a42af76234716857535bbde20b`
- QA_record: `QA.md`

## Approval outcome

- user decision: approved as Canon on `2026-09-10`
- promoted asset: `OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001`
- current approved path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_03_RIGHT_3Q_NEUTRAL/OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001.jpg`
- current approved JPG checksum: `002b47b9b5e15d3a85d1467eb6b73890254c8d69d9d1422b24b5964841d412d8`
- approval record: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_03_RIGHT_3Q_NEUTRAL/approvals/APPROVAL_OWNER_FACE_03_RIGHT_3Q_NEUTRAL_001.md`
- reproduction method: `characters/CHR_HUMAN_001_OWNER/canon/face/FACE_03_RIGHT_3Q_NEUTRAL_METHOD.md`
- full release: `owner_v1.0` remains unlocked
