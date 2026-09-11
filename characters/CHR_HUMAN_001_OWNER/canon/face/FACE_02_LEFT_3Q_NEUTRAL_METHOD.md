# FACE_02_LEFT_3Q_NEUTRAL — Approved Reproduction Method

```yaml
method_id: OWNER_FACE_02_LEFT_3Q_NEUTRAL_METHOD_V1
status: APPROVED_METHOD
approved_component: OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001
source_candidate: FACE_02_LEFT_3Q_NEUTRAL_v004
generation_spec_revision: draft_1.14
generation_identity_revision: draft_0.14
documentation_spec_revision: draft_1.15
documentation_identity_revision: draft_0.15
recovery_reference_set: OWNER_FACE_LEFT_3Q_NEUTRAL_RECOVERY_V1
downstream_reference_set: OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1
output_status: REVIEW_REQUIRED
```

This file is the self-contained recovery recipe for recreating the approved left-three-quarter L1 Face component. Ordinary L2/L3 shots that need this view use the approved Master directly. Recreating the L1 component always starts from the three scoped Master/source inputs below and produces a new `REVIEW_REQUIRED` candidate; it never starts from v001–v004 or from the approved generated pixels.

## Approved output fingerprint

- approved asset: `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001`
- path: `approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg`
- dimensions: 1086×1448, exact 3:4
- current JPG SHA-256: `3f50c08e2993aa8dd406abd093d24f8a581b6e1475aa4dd57bda3884fed3b745`
- approved source-candidate PNG SHA-256: `34f1a633d37434c8bb17ba28259ff76fa0ba495abb02816979d6b2b6e8a265c3`
- format note: user-transcoded JPEG is the active downstream Master; it does not replace the source-method lineage
- accepted prompt basis: complete v001 prompt structure plus exactly three concise refinements to cheekbone, chin and gaze
- seed/settings: the built-in ImageGen call did not return a seed or reproducible sampler settings; therefore stability depends on exact reference order, strict role isolation, prompt structure and QA rather than a seed claim

## Exact recovery input order and fingerprints

Input order is part of the method and must not be changed casually.

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
   - path: `approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
   - dimensions: 1086×1448
   - SHA-256: `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`
   - exclusive responsibility: exact approved recognizable identity, skull and facial-feature relationships, adult age appearance, neutral-studio skin tone and neutral-expression baseline
   - must not define: the new three-quarter geometry by itself, body, final outfit, Hairstyle B or episode setting

2. `L0_OWNER_013`
   - path: `../../source/identity/raw/15.jpg`
   - dimensions: 957×1048
   - SHA-256: `1851e8decaa3430f127c3e720f7fba8bb119370008ef7795313fd6e76b396af0`
   - exclusive responsibility: real same-person left-three-quarter orbital depth, nose projection, cheek-to-jaw depth, visible-ear placement and face-points-image-left geometry
   - must not define: identity priority, smile, gaze, formal makeup, retouching, skin tone, directional light, ornaments, updo, clothing or background

3. `OWNER_HAIRSTYLE_A_FACE_MASKED_001`
   - path: `reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`
   - dimensions: 769×1080
   - SHA-256: `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`
   - exclusive responsibility: Hairstyle A near-center part, close-to-scalp roots, controlled low volume, long straight loose silhouette, face-framing panels and tapered ends
   - must not define: face, skin, skull, body, white jacket, outdoor color/light or background; the gray oval is deleted information

Do not add `16.jpg` by default. It repeats the same direction with a stronger teeth smile and raises expression/makeup leakage risk. Do not add the B appearance anchor because the approved `FACE_01` now supplies the identity and skin authority. Do not attach v001, v002, v003, v004 or the approved FACE_02 image to recreate L1.

## Direction and camera contract

- asset name: `FACE_02_LEFT_3Q_NEUTRAL`;
- anatomical left facial plane is principally visible;
- nose points image-left;
- head rotation target is approximately 35–40° toward image-left, with a moderate three-quarter view rather than near-front or profile;
- eyes look toward the camera without an intense stare;
- camera at eye height, horizontal optical axis, upright neutral head;
- forehead, hairline, skull, crown, ears, jaw and chin share one coherent projection;
- 85–105mm-equivalent portrait perspective; no wide-angle facial expansion;
- head top to upper chest, head approximately 65–72% of frame height;
- exact 3:4 portrait, neutral gray-white seamless studio, soft even 5200–5600K illumination.

## Approved facial refinement block

These refinements are intentionally short. Do not expand them into a long redesign brief:

- cheekbone: appear slightly lower, with a softer contour integrated naturally into the cheek; never flatten or inflate the face;
- chin: soft rounded terminal curve; preserve chin length, projection and jaw width; never produce a pointed, broad, short, heavy or childlike chin;
- gaze: gentle and alert through relaxed eyelid tension; preserve eye size, almond shape, spacing, canthal direction and pupil placement; no squint, sleepiness, smile or eyebrow redesign.

All other facial geometry remains locked to the approved front Master. The three refinements are corrections to the left-three-quarter presentation, not permission to redesign identity.

## Hairstyle and visible outfit

- `HAIRSTYLE_A` only: near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels, subtle strand irregularity and tapered ends;
- forbid bun, updo, ponytail, Hairstyle B and A/B hybrid;
- if clothing is visible, it is only the authentic upper portion of the pink high-cut one-piece Calibration Outfit;
- visible pink straps/neckline are non-authoritative for garment geometry and must not be interpreted as a separate tank top.

## Canonical prompt assembly

Preserve this structure and keep the three refinement sentences inside the identity block. Update only the candidate ID and current governing revision labels when required.

```text
Use case: identity-preserve

Asset type: FACE_02_LEFT_3Q_NEUTRAL, L1 Face Canon candidate <CANDIDATE_ID> for CHR_HUMAN_001_OWNER, governed by the current OWNER_L1_GENERATION_SPEC and OWNER_IDENTITY_ANCHOR revisions.

Input images: Image 1 is the approved front-neutral Face Canon and is authoritative for the exact recognizable woman, facial-feature relationships, adult age appearance, neutral-studio skin tone and neutral expression. Image 2 is the real L0 left-three-quarter source and is authoritative only for the same person's orbital depth, nose projection, cheek-to-jaw depth, ear placement and face-points-image-left geometry. Image 3 is a source-derived masked Hairstyle A reference and is authoritative only for hair design. Resolve identity conflicts in favor of Image 1.

Primary request: Create exactly one new photorealistic left-three-quarter neutral portrait. Turn the head approximately 35–40 degrees toward image-left so the anatomical left facial plane is principally visible. Keep the eyes looking toward the camera, the mouth naturally closed and the expression neutral. Reconstruct the new angle from the three scoped master references in parallel; do not copy or continue any previous AI candidate.

Identity: Preserve exactly the same recognizable woman as Image 1, including skull proportions, eye spacing, brows, natural eye size, nose, soft lips, naturally full cheeks, rounded jaw transition, rounded chin, adult age and natural asymmetry. Image 2 may solve only real view-dependent depth. Do not inherit its smile, gaze, formal makeup, retouching, skin tone, lighting, ornaments, hairstyle, clothing or background. Image 3 must not influence face, skin, skull, body, clothing, light or background. Add only these restrained refinements while keeping all other facial features unchanged: make the cheekbone appear slightly lower with a softer contour; give the chin a softer, rounder terminal curve without changing chin length or jaw width; make the gaze gentler by relaxing eyelid tension without changing eye size, shape, spacing, canthal direction or pupil placement.

Hairstyle: HAIRSTYLE_A only — near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels, subtle strand irregularity and tapered ends. No bun, no updo, no Hairstyle B and no A/B hybrid.

Composition and camera: Exact 3:4 portrait; head top to upper chest; head approximately 65–72% of frame height; 85–105mm-equivalent portrait perspective; camera at eye height; horizontal optical axis; upright neutral head; visually level forehead, hairline, skull, crown, ears and jaw. No top-down or upturned-head projection and no excessive visible crown plane.

Scene and light: Neutral gray-white seamless studio; soft even low-contrast 5200–5600K light; neutral white balance; natural photographic skin texture. If clothing is visible, show only the authentic upper portion of the same pink high-cut one-piece Calibration Outfit, not a tank top or other pink garment.

Avoid: identity averaging, generic face, slimming, enlarged eyes, narrowed nose, pointed chin, high or sharply prominent cheekbone, intense stare, age change, beauty filter, whitening, heavy makeup, smile, parted lips, distorted ears, asymmetric eye errors, wide-angle distortion, dramatic styling, color cast, text, watermark, collage and multiple views.

Output: One candidate image only. REVIEW_REQUIRED; do not label or imply Canon approval.
```

## Failure history and what not to learn

- v001: identity direction was good; user requested only slightly lower/softer cheekbone, rounder chin and gentler gaze. Do not use its pixels.
- v002: most requested refinements were good, but the prompt had begun accumulating additional explanatory constraints. Do not use its pixels or treat it as the recovery baseline.
- v003: user rejected the facial features. It is `REJECTED` and ineligible for all reference use.
- v004: approved output. Its success came from returning to the v001 prompt structure and adding only the three concise refinements. Use the method, not its pixels, for L1 recreation.

## Required QA order

1. exact recognizable identity and all facial-feature relationships against approved `FACE_01`;
2. anatomical left plane visible and face pointing image-left;
3. moderate three-quarter rotation, near/far eye relationship, nose projection, cheek/jaw depth and visible-ear placement;
4. cheekbone height/softness, chin terminal roundness and gentle gaze without collateral changes;
5. adult age, neutral closed mouth, skin tone and absence of formal-photo makeup/light leakage;
6. eye-level projection, lens neutrality, 3:4 framing and head scale;
7. Hairstyle A construction and absence of B/updo contamination;
8. Calibration Outfit upper portion and absence of text, watermark, collage or anatomy artifacts.

Any identity mismatch is a rejection even if the three targeted refinements look attractive. Every recreated output remains `REVIEW_REQUIRED` until separately approved; it never overwrites this approved Master.
