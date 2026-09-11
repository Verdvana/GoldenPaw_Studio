# FACE_03_RIGHT_3Q_NEUTRAL_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.16
identity_md_revision: draft_0.15
asset_id: FACE_03_RIGHT_3Q_NEUTRAL
candidate_id: FACE_03_RIGHT_3Q_NEUTRAL_v001
gate: "Gate 2 — Face Identity Canon"
model_tool: "built-in image_gen"
status: GENERATED_REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_L0_FACE_RIGHT_3Q_LIMITED
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
reference_count: 3
seed_settings: "built-in image_gen; seed and detailed settings not returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_03_RIGHT_3Q_NEUTRAL_v001/FACE_03_RIGHT_3Q_NEUTRAL_v001.png"
qa_status: USER_REVISION_REQUESTED_CHIN_ONLY
```

## 1. Task and candidate intent

Create one fresh right-three-quarter neutral L1 Face candidate. The nose points image-right and the anatomical right facial plane is principally visible. The approved front Face Master controls fine identity. The only real image-right source is low resolution and therefore controls direction, real right-side asymmetry and coarse depth only.

## 2. Reference plan

| Priority | Reference ID | Path | Responsibility | Must not define |
|---:|---|---|---|---|
| 1 | `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` | `canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.png` | exact identity, skull/facial-feature relationships, adult age, skin tone, neutral expression and fine geometry | right-three-quarter direction by itself, body, final outfit, Hairstyle B, episode setting |
| 2 | `L0_OWNER_012` | `source/identity/raw/14.jpg` | real same-person anatomical right facial plane, face-points-image-right direction, natural right-side asymmetry and coarse orbital/nose/cheek/jaw depth | fine geometry, lens-neutral proportions, camera height, eye size, skin tone, texture, makeup, hair, black clothing, industrial background or mixed light |
| 3 | `OWNER_HAIRSTYLE_A_FACE_MASKED_001` | `canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png` | Hairstyle A part, low roots/volume, long straight silhouette, face-framing panels and tapered ends | face, skin, skull, body, white jacket, outdoor color/light or background |

Reference budget: three images. `L0_OWNER_012` is 240×320 and is explicitly subordinate to the approved Face Master for all fine identity decisions. No FACE_02 image, prior AI candidate or mirrored source is used.

## 3. Identity and view locks

- Preserve the exact recognizable woman from approved `FACE_01` and `IDENTITY.md` draft_0.15.
- Preserve natural medium almond eyes, exact spacing, brows, nose, soft lips, naturally full cheeks, softly restrained cheekbones, rounded jaw transition, soft rounded chin, adult age and gentle neutral gaze.
- Turn the head approximately 35–40° toward image-right; anatomical right facial plane principally visible; eyes look toward camera.
- Reconstruct a real opposite view, not a horizontally mirrored left view. Preserve natural facial asymmetry where supported by the approved front Master and L0 right-side evidence.

## 4. Camera, hair and appearance

- 85–105mm-equivalent portrait perspective, eye-height horizontal camera, neutral upright head.
- Exact 3:4, head top to upper chest, head approximately 65–72% of frame height.
- Neutral gray-white seamless studio, soft even 5200–5600K light and natural skin texture.
- Hairstyle A only; no bun, updo, Hairstyle B or hybrid.
- Visible clothing is only the authentic upper portion of the pink high-cut one-piece Calibration Outfit; it remains non-authoritative.

## 5. Negative constraints

No mirroring, left-facing result, identity averaging, generic face, low-resolution facial simplification, phone-camera distortion, face widening, slimming, enlarged eyes, narrowed nose, pointed chin, high/sharp cheekbones, intense stare, smile, parted lips, age change, beauty filter, whitening, formal makeup, source hair/clothes/background leakage, wide angle, top-down view, text, watermark or collage.

## Final assembled prompt

Use case: identity-preserve

Asset type: `FACE_03_RIGHT_3Q_NEUTRAL`, L1 Face Canon candidate v001 for `CHR_HUMAN_001_OWNER`, governed by `OWNER_L1_GENERATION_SPEC` draft_1.16 and `OWNER_IDENTITY_ANCHOR` draft_0.15.

Input images: Image 1 is the approved front-neutral Face Canon and has highest authority for the exact recognizable woman, skull and facial-feature relationships, adult age, neutral-studio skin tone, fine facial geometry and neutral expression. Image 2 is a low-resolution real same-person image pointing image-right; it is authoritative only for the anatomical right facial plane, real face-points-image-right direction, natural right-side asymmetry and coarse orbital/nose/cheek/jaw depth. It must never override Image 1's fine geometry or lens-neutral proportions. Image 3 is a source-derived masked Hairstyle A reference and is authoritative only for hair. Resolve every identity conflict in favor of Image 1.

Create exactly one new photorealistic right-three-quarter neutral portrait. Turn the head approximately 35–40 degrees toward image-right so the anatomical right facial plane is principally visible. Keep the eyes looking toward the camera, mouth naturally closed and expression neutral with a gentle, relaxed gaze. Reconstruct the real opposite facial view; do not mirror an image-left face and do not copy or continue any previous AI candidate.

Preserve exactly the same recognizable woman as Image 1: skull proportions, eye spacing, brows, natural medium almond eye size and shape, nose, soft lips, naturally full cheeks, softly restrained cheekbones, rounded jaw transition, soft rounded chin, adult age, skin tone and natural asymmetry. Use Image 2 only to reveal genuine right-side direction/asymmetry and coarse depth. Do not inherit its low resolution, phone perspective, camera angle, facial simplification, skin color, mixed light, hair, black clothing or industrial background. Image 3 must not influence face, skin, skull, body, clothing, light or background.

Hairstyle A only: near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels, subtle strand irregularity and tapered ends. No bun, updo, Hairstyle B or A/B hybrid.

Exact 3:4 portrait; head top to upper chest; head approximately 65–72% of frame height; 85–105mm-equivalent perspective; camera at eye height with a horizontal optical axis; upright neutral head; coherent forehead, hairline, skull, crown, ears, jaw and chin projection. Neutral gray-white seamless studio, soft even low-contrast 5200–5600K light, neutral white balance and natural photographic skin texture. If clothing is visible, show only the authentic upper portion of the pink high-cut one-piece Calibration Outfit, not a tank top or other garment.

Avoid mirroring, face pointing image-left, identity averaging, generic face, low-resolution feature loss, phone-camera distortion, face widening or slimming, enlarged eyes, narrowed nose, pointed chin, high/sharp cheekbones, intense stare, smile, parted lips, age change, beauty filtering, whitening, heavy makeup, source styling leakage, wide-angle or top-down distortion, text, watermark, collage and multiple views.

One candidate image only. `REVIEW_REQUIRED`; do not label or imply Canon approval.

## Generation settings/result

- generated_at: `2026-09-10T15:08:11+08:00`
- seed/settings: built-in `image_gen`; seed and detailed settings were not returned
- source output: `/home/verdvana/.codex/generated_images/01a089e9-1904-7443-9200-afbaa6608bae/exec-8a100670-6bb3-4ca8-97a2-31852ab45458.png`
- output_path: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_03_RIGHT_3Q_NEUTRAL_v001/FACE_03_RIGHT_3Q_NEUTRAL_v001.png`
- output_dimensions: `1086x1448`
- output_checksum: `e9e53bd5f8d8965533979ec108640d8362d6fc73f74855f5f1c86bf541f4bbdc`
- QA_record: `QA.md`

## User review outcome

- overall method/direction: retained
- requested refinement: chin remains slightly too pointed
- required v002 change: round only the bottom central chin contour while preserving chin length/projection, jaw width and all other facial features
- disposition: retain v001 as `REVIEW_REQUIRED`; generate v002 from the same three scoped inputs, not from v001
