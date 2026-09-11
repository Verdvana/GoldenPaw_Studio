# FACE_02_LEFT_3Q_NEUTRAL_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.12
identity_md_revision: draft_0.12
asset_id: FACE_02_LEFT_3Q_NEUTRAL
candidate_id: FACE_02_LEFT_3Q_NEUTRAL_v002
gate: "Gate 2 — Face Identity Canon"
model_tool: "built-in image_gen"
status: GENERATED_REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_count: 3
seed_settings: "built-in image_gen; seed and detailed settings not returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_02_LEFT_3Q_NEUTRAL_v002/FACE_02_LEFT_3Q_NEUTRAL_v002.png"
qa_status: USER_REVISION_REQUESTED_CHIN_ONLY
```

## 1. Task and refinement intent

Create one fresh `FACE_02_LEFT_3Q_NEUTRAL` candidate from the same approved/scoped Master references as v001. Preserve the successful overall direction while applying only three user-requested refinements: slightly lower-looking and softer cheekbone prominence, a subtly rounder chin termination, and a softer relaxed gaze.

`FACE_02_LEFT_3Q_NEUTRAL_v001` is not an input and must not define pixels. Its accepted and rejected properties are carried only as written user feedback.

## 2. Reference plan

| Priority | Reference ID | Path | Responsibility | Must not define |
|---:|---|---|---|---|
| 1 | `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` | `canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.png` | exact approved identity, facial-feature relationships, age, skin tone, neutral expression, naturally rounded chin family | new 3/4 geometry alone, body, final outfit, Hairstyle B, episode lighting/background |
| 2 | `L0_OWNER_013` | `source/identity/raw/15.jpg` | real image-left left-three-quarter orbital, nose, cheek/jaw depth and ear placement | high-looking cheekbone exaggeration, smile, gaze, makeup, retouching, skin tone, light, ornament, hairstyle, clothing, background |
| 3 | `OWNER_HAIRSTYLE_A_FACE_MASKED_001` | `canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png` | Hairstyle A part, roots, volume, long straight silhouette, face-framing panels and ends | face, expression, skin, skull, body, clothing, outdoor light/color, background |

Reference budget: three images. No previous candidate is supplied.

## 3. Locked properties

- Same recognizable woman, adult age, skin tone, facial-feature scale and natural asymmetry as the approved Face Canon.
- Same left three-quarter intent: head 35–40 degrees toward image-left, anatomical left facial plane principally visible, eyes toward camera.
- Same Hairstyle A, eye-level camera, neutral studio, head-to-upper-chest framing and pink Calibration Outfit upper portion.
- Mouth remains naturally closed and neutral; no smile is used to soften the expression.

## 4. Targeted changes only

- Cheekbone: lower the perceived apex only slightly and soften the zygomatic contour into the natural cheek volume. Do not flatten the face, enlarge the cheeks or change the jaw width.
- Chin: reduce pointedness only slightly, producing a softer rounded terminal curve consistent with the approved front Canon. Do not shorten the chin or create a broad/heavy jaw.
- Gaze: relax upper/lower eyelid tension and reduce stare intensity while preserving exact eye size, almond shape, spacing, canthal direction and pupil placement. No squint, smile, eyebrow redesign or sleepy expression.

## 5. Output contract

One new 3:4 photorealistic candidate only. No collage, text or watermark. Status remains `REVIEW_REQUIRED`; no automatic promotion.

## Final assembled prompt

Use case: identity-preserve

Asset type: `FACE_02_LEFT_3Q_NEUTRAL`, L1 Face Canon candidate v002 for `CHR_HUMAN_001_OWNER`, governed by `OWNER_L1_GENERATION_SPEC` draft_1.12 and `OWNER_IDENTITY_ANCHOR` draft_0.12.

Input images: Image 1 is the approved front-neutral Face Canon and is authoritative for the exact recognizable woman, facial-feature relationships, adult age, neutral-studio skin tone, natural eye design, soft rounded jaw/chin family and neutral expression. Image 2 is the real L0 left-three-quarter source and is authoritative only for orbital depth, nose projection, cheek-to-jaw depth, ear placement and face-points-image-left geometry. Image 3 is the masked Hairstyle A reference and is authoritative only for hair. Resolve identity conflicts in favor of Image 1. Do not use or imitate any previous FACE_02 generated candidate.

Create exactly one fresh photorealistic left-three-quarter neutral portrait. Turn the head approximately 35–40 degrees toward image-left so the anatomical left facial plane is principally visible. Eyes look toward the camera; mouth is naturally closed. Preserve the approved identity, angle intent, nose, near/far eye relationship, skin tone, age, Hairstyle A, eye-level camera, framing, neutral studio and Calibration Outfit presentation.

Make only three restrained refinements relative to the written review target: (1) the cheekbone should appear just slightly lower and its contour should flow more softly into the natural cheek, without flattening the face or making the cheeks fuller; (2) the chin should be just slightly less pointed, ending in a softer rounded curve, without shortening it or widening the jaw; (3) the gaze should feel gentler and more relaxed by subtly reducing eyelid tension and stare intensity, while keeping exactly the same eye size, almond shape, spacing, canthal direction and pupil placement. Do not create a smile, squint, sleepy expression, altered eyebrows or enlarged eyes.

Image 2 must not transmit its smile, strong cheekbone styling, gaze, formal makeup, retouching, skin tone, lighting, ornaments, hairstyle, clothing or background. Image 3 must not influence face, expression, skin, skull, body, clothing, light or background.

Hairstyle A only: near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels and tapered ends. No bun, updo, Hairstyle B or hybrid.

Exact 3:4 portrait, head top to upper chest, head about 65–72% of frame height, 85–105mm-equivalent perspective, eye-height camera, horizontal optical axis, upright neutral head, no top-down or upturned-head projection. Neutral gray-white seamless studio, soft even 5200–5600K light, natural skin texture. Visible clothing is only the authentic upper portion of the pink high-cut one-piece Calibration Outfit.

Avoid identity drift, generic face, high or sharp cheekbone exaggeration, flat face, swollen cheeks, pointed chin, broad heavy chin, changed jaw width, changed eye geometry, intense stare, smile, squint, sleepiness, beauty filter, whitening, heavy makeup, wide-angle distortion, dramatic styling, text, watermark, collage or multiple views.

One candidate only. `REVIEW_REQUIRED`; do not label or imply Canon approval.

## Generation settings/result

- generated_at: `2026-09-10T14:27:41+08:00`
- seed/settings: built-in `image_gen`; seed and detailed settings were not returned
- source output: `/home/verdvana/.codex/generated_images/01a089e9-1904-7443-9200-afbaa6608bae/exec-1e56708f-d395-4e69-8b46-5264899954f9.png`
- output_path: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_02_LEFT_3Q_NEUTRAL_v002/FACE_02_LEFT_3Q_NEUTRAL_v002.png`
- output_dimensions: `1086x1448`
- output_checksum: `a5b0500e0024883c29cc0014b1fe6bb31b82c0c0c57cc61ca4381a5daa14f171`
- QA_record: `QA.md`

## User review outcome

- approved in scope: identity direction, cheekbone refinement, softer gaze, angle, skin tone, Hairstyle A, camera and composition
- requested refinement: make only the terminal chin curve slightly rounder
- must remain unchanged: chin length, jaw width, jaw angle, lips and all other facial structures
- disposition: retain as `REVIEW_REQUIRED`; create v003 from the same scoped Master references, not from this candidate
