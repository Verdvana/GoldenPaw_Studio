# FACE_03_RIGHT_3Q_NEUTRAL — Approved Reproduction Method

```yaml
method_id: OWNER_FACE_03_RIGHT_3Q_NEUTRAL_METHOD_V1
status: APPROVED_METHOD
approved_component: OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001
source_candidate: FACE_03_RIGHT_3Q_NEUTRAL_v002
generation_spec_revision: draft_1.17
generation_identity_revision: draft_0.16
documentation_spec_revision: draft_1.18
documentation_identity_revision: draft_0.17
recovery_reference_set: OWNER_FACE_RIGHT_3Q_NEUTRAL_RECOVERY_V1
downstream_reference_set: OWNER_FACE_RIGHT_3Q_NEUTRAL_CANON_L1
recreated_output_status: REVIEW_REQUIRED
```

This is the self-contained recovery recipe for the approved right-three-quarter L1 Face component. Ordinary L2/L3 shots use the approved Master within its metadata scope. Recreating this L1 component must start from the three ordered inputs below and creates a new `REVIEW_REQUIRED` candidate. Never use FACE_03 candidate/approved pixels, FACE_02 pixels, or a mirrored image-left face as an L1 recovery input.

## Approved output fingerprint

- approved asset: `OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001`
- path: `approved/FACE_03_RIGHT_3Q_NEUTRAL/OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001.jpg`
- dimensions: 1086×1448, exact 3:4
- current JPG SHA-256: `002b47b9b5e15d3a85d1467eb6b73890254c8d69d9d1422b24b5964841d412d8`
- approved source-candidate PNG SHA-256: `f88def7d4e88ad6fcd08a1aef36456bb0a04e1a42af76234716857535bbde20b`
- format note: user-transcoded JPEG is the active downstream Master; it does not replace the source-method lineage
- accepted prompt basis: complete v001 prompt plus one chin-only refinement
- seed/settings: ImageGen returned no seed or sampler settings; continuity therefore depends on fixed input order, strict role isolation, the prompt below and attribute-by-attribute QA

## Exact recovery input order and responsibilities

Input order is part of the method.

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
   - path: `approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
   - dimensions: 1086×1448
   - SHA-256: `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`
   - responsibility: highest authority for the exact recognizable woman, skull and facial-feature relationships, adult age, neutral-studio skin tone, fine facial geometry and neutral expression
   - must not define: right-view depth by itself, body, final outfit, Hairstyle B or episode setting

2. `L0_OWNER_012`
   - path: `../../source/identity/raw/14.jpg`
   - dimensions: 240×320
   - SHA-256: `f7a83644f202ebec95134c6d115397b9f52f12e79b5fb227a6b79182026bd788`
   - responsibility: anatomical-right/image-right direction, natural real-person right-side asymmetry and coarse orbital/nose/cheek/jaw depth only
   - must not define: fine geometry, lens-neutral proportions, identity priority, skin tone, phone perspective, hair, black clothing, mixed lighting or industrial background

3. `OWNER_HAIRSTYLE_A_FACE_MASKED_001`
   - path: `reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`
   - dimensions: 769×1080
   - SHA-256: `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`
   - responsibility: Hairstyle A near-center part, close roots, low crown volume, long straight loose silhouette, face-framing panels and tapered ends
   - must not define: face, skin, skull, body, clothing, light or background; the gray mask is deleted information

Do not add FACE_02 as a pixel input and do not mirror it. Do not add FACE_03 v001, v002 or the approved FACE_03 Master. Identity conflicts resolve in favor of Input 1; Input 2 remains deliberately weak and view-scoped.

## Direction, camera and approved chin contract

- anatomical right facial plane principally visible; face and nose point image-right;
- head rotation approximately 35–40° toward image-right, not near-front and not profile;
- eyes toward camera with a gentle relaxed gaze; neutral closed mouth;
- eye-height camera, horizontal optical axis, upright neutral head;
- coherent forehead, hairline, skull, crown, ears, jaw and chin projection;
- 85–105mm-equivalent portrait perspective; head top to upper chest; head 65–72% of frame height; exact 3:4;
- the bottom central chin curve is softly rounded and not pointed;
- preserve chin vertical length and forward projection, jaw width, jaw angle, lower-lip position and every other facial feature;
- never make the chin short, broad, heavy, recessed, swollen, doubled or childlike.

## Canonical prompt assembly

Keep this structure and wording stable. Only candidate ID and current governing revision labels may be updated.

```text
Use case: identity-preserve

Asset type: FACE_03_RIGHT_3Q_NEUTRAL, L1 Face Canon candidate <CANDIDATE_ID> for CHR_HUMAN_001_OWNER, governed by the current OWNER_L1_GENERATION_SPEC and OWNER_IDENTITY_ANCHOR revisions.

Input images: Image 1 is the approved front-neutral Face Canon and has highest authority for the exact recognizable woman, skull and facial-feature relationships, adult age, neutral-studio skin tone, fine facial geometry and neutral expression. Image 2 is a low-resolution real same-person image pointing image-right; it is authoritative only for the anatomical right facial plane, real face-points-image-right direction, natural right-side asymmetry and coarse orbital/nose/cheek/jaw depth. It must never override Image 1's fine geometry or lens-neutral proportions. Image 3 is a source-derived masked Hairstyle A reference and is authoritative only for hair. Resolve every identity conflict in favor of Image 1.

Create exactly one new photorealistic right-three-quarter neutral portrait. Turn the head approximately 35–40 degrees toward image-right so the anatomical right facial plane is principally visible. Keep the eyes looking toward the camera, mouth naturally closed and expression neutral with a gentle, relaxed gaze. Reconstruct the real opposite facial view; do not mirror an image-left face and do not copy or continue any previous AI candidate.

Preserve exactly the same recognizable woman as Image 1: skull proportions, eye spacing, brows, natural medium almond eye size and shape, nose, soft lips, naturally full cheeks, softly restrained cheekbones, rounded jaw transition, adult age, skin tone and natural asymmetry. Use Image 2 only to reveal genuine right-side direction/asymmetry and coarse depth. Do not inherit its low resolution, phone perspective, camera angle, facial simplification, skin color, mixed light, hair, black clothing or industrial background. Image 3 must not influence face, skin, skull, body, clothing, light or background. Make one and only one refinement: give the bottom central contour of the chin a more softly rounded, less pointed curve. Preserve the exact chin vertical length and forward projection, jaw width, jaw angle, lower-lip position and every other facial feature. Do not make the chin short, broad, heavy, recessed, swollen, doubled or childlike.

Hairstyle A only: near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels, subtle strand irregularity and tapered ends. No bun, updo, Hairstyle B or A/B hybrid.

Exact 3:4 portrait; head top to upper chest; head approximately 65–72% of frame height; 85–105mm-equivalent perspective; camera at eye height with a horizontal optical axis; upright neutral head; coherent forehead, hairline, skull, crown, ears, jaw and chin projection. Neutral gray-white seamless studio, soft even low-contrast 5200–5600K light, neutral white balance and natural photographic skin texture. If clothing is visible, show only the authentic upper portion of the pink high-cut one-piece Calibration Outfit, not a tank top or other garment.

Avoid mirroring, face pointing image-left, identity averaging, generic face, low-resolution feature loss, phone-camera distortion, face widening or slimming, enlarged eyes, narrowed nose, pointed chin, shortened or widened chin, changed jaw, high/sharp cheekbones, intense stare, smile, parted lips, age change, beauty filtering, whitening, heavy makeup, source styling leakage, wide-angle or top-down distortion, text, watermark, collage and multiple views.

One candidate image only. REVIEW_REQUIRED; do not label or imply Canon approval.
```

## Failure history

- v001: overall method and identity direction were accepted, but the chin remained slightly pointed. Its pixels are ineligible.
- v002: recreated from the same three original scoped inputs, with only the bottom-central chin-rounding constraint added; user approved it as the current component Canon.
- Recovery rule: reproduce v002's method, not its pixels. Any new output is independently reviewed and never overwrites this Master.

## Required QA order

1. exact identity and feature relationships against approved FACE_01;
2. anatomical right plane visible, face pointing image-right, and no mirrored-left artifacts;
3. moderate 35–40° view, near/far eye, nose, cheek/jaw depth and ear placement;
4. rounded chin terminal curve with unchanged length/projection/jaw/lower lip;
5. restrained cheekbones, gentle neutral gaze, adult age and closed mouth;
6. neutral skin, eye-level projection, lens neutrality, 3:4 framing and head scale;
7. Hairstyle A and the visible Calibration Outfit upper portion;
8. no text, watermark, collage, source leakage or anatomy artifacts.

An identity mismatch is a rejection even if the chin is attractive. Every recreation remains `REVIEW_REQUIRED` until separately approved.
