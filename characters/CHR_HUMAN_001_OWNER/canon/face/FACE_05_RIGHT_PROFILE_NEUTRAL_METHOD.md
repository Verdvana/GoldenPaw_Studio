# FACE_05_RIGHT_PROFILE_NEUTRAL — Approved Reproduction Method

```yaml
method_id: OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_METHOD_V1
status: APPROVED_METHOD
approved_component: OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001
source_candidate: FACE_05_RIGHT_PROFILE_NEUTRAL_v002
generation_spec_revision: draft_1.19
generation_identity_revision: draft_0.18
documentation_spec_revision: draft_1.20
documentation_identity_revision: draft_0.19
recovery_reference_set: OWNER_FACE_RIGHT_PROFILE_NEUTRAL_RECOVERY_V1
downstream_reference_set: OWNER_FACE_RIGHT_PROFILE_NEUTRAL_CANON_L1
recreated_output_status: REVIEW_REQUIRED
```

This is the self-contained recovery recipe for the approved right-profile L1 Face component. Ordinary L2/L3 shots use the approved Master within its metadata scope. Recreating this L1 component starts from the three ordered inputs below and produces a new `REVIEW_REQUIRED` candidate. Never use FACE_05 candidate/approved pixels, another generated Face angle, a mirrored face, or a previous shot as an L1 recovery input.

## Approved output fingerprint

- approved asset: `OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001`
- path: `approved/FACE_05_RIGHT_PROFILE_NEUTRAL/OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001.jpg`
- dimensions: 1086×1448, exact 3:4
- current JPG SHA-256: `de670f987d341e686f5239d6b5c7a920cd431050c2907c26de759a5cf37f6b97`
- approved source-candidate PNG SHA-256: `7a92f8ffbf0d9a8b5baf28b8962e1ab76035800ca220c9cc4f82e9e5c904c9ea`
- format note: user-transcoded JPEG is the active downstream Master; it does not replace the source-method lineage
- accepted prompt basis: full v001 construction prompt plus one restrained nasal-tip size refinement
- seed/settings: built-in ImageGen returned no seed or sampler settings; continuity depends on input order, role isolation, prompt structure and QA

## Exact recovery input order and fingerprints

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
   - path: `approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
   - dimensions: 1086×1448
   - SHA-256: `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`
   - responsibility: highest authority for exact identity, skull and feature relationships, adult age, neutral-studio skin and expression
   - must not define: full profile depth alone, body, final outfit, Hairstyle B or episode setting

2. `L0_OWNER_009`
   - path: `../../source/identity/raw/11.jpg`
   - dimensions: 1522×1773
   - SHA-256: `948a092a360192af3f8718b27e35562ca5e14a21022e1161f8449be75b830a46`
   - responsibility: genuine anatomical-right profile pointing image-left; forehead/nose/philtrum/lip/chin silhouette, orbital depth, ear placement and jaw/neck transition
   - must not define: identity priority, glancing eye pose, updo, makeup, retouching, skin color/texture, directional light, black clothing or pink backdrop

3. `OWNER_HAIRSTYLE_A_FACE_MASKED_001`
   - path: `reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`
   - dimensions: 769×1080
   - SHA-256: `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`
   - responsibility: Hairstyle A near-center part, close roots, low crown volume, long straight loose silhouette, face-framing panels and tapered ends
   - must not define: face, skin, skull, body, clothing, light or background; the gray oval is deleted information

Input order is fixed. Do not add v001, v002, the approved FACE_05 image, FACE_02, FACE_03 or a mirror.

## Direction, camera and approved nose contract

- anatomical right facial plane visible; face and nose point image-left;
- true 85–90° profile, one eye principally visible and no far iris beside the bridge;
- visible eye looks naturally ahead toward image-left, not toward camera;
- clean forehead–nose–lips–chin silhouette, neutral closed mouth and gentle expression;
- eye-height camera, horizontal optical axis, upright neutral head, 85–105mm-equivalent perspective;
- exact 3:4, head top to upper chest, head approximately 65–72% of frame height;
- nasal tip bulk and forward projection are slightly reduced relative to the raw v001 construction result;
- preserve nose root, bridge length/curve, dorsum angle, alar/nostril structure, nasolabial angle, philtrum, lips, rounded chin, jaw and all other features;
- never make the nose pinched, sharp, upturned, bridge-shortened or generically beautified.

## Canonical prompt assembly

Preserve this structure. Only candidate ID and current governing revision labels may change.

```text
Use case: identity-preserve

Asset type: FACE_05_RIGHT_PROFILE_NEUTRAL, L1 Face Canon candidate <CANDIDATE_ID> for CHR_HUMAN_001_OWNER, governed by the current OWNER_L1_GENERATION_SPEC and OWNER_IDENTITY_ANCHOR revisions.

Input images: Image 1 is the approved front-neutral Face Canon and has highest authority for the exact recognizable woman, skull and facial-feature relationships, adult age, neutral-studio skin tone, fine facial geometry and neutral expression. Image 2 is the strongest real same-person profile photograph; it is authoritative only for her genuine right-profile geometry with the face and nose pointing image-left: forehead-to-nose bridge, orbital depth, philtrum, lips, rounded chin, jaw-to-ear relationship, visible ear placement and jaw/neck transition. Image 3 is a source-derived masked Hairstyle A reference and is authoritative only for hair. Resolve every identity conflict in favor of Image 1.

Create exactly one new photorealistic neutral full right-profile portrait. Rotate the head about 85–90 degrees so the anatomical right facial plane is visible and the face/nose points image-left. Show a clean true profile rather than a three-quarter view: one eye is principally visible, no far iris appears beside the nasal bridge, and the forehead–nose–lips–chin silhouette reads clearly. The visible eye looks naturally straight ahead toward image-left, not toward the camera. Mouth naturally closed; expression neutral, gentle and relaxed. Reconstruct from the three scoped inputs in parallel; do not mirror another Canon and do not copy or continue any AI candidate.

Preserve the same recognizable woman as Image 1: skull proportions, natural medium almond eye, brow, softly shaped lips, naturally full cheek volume, restrained cheekbone, rounded jaw transition, softly rounded non-pointed chin, adult age, skin tone and natural asymmetry. Use Image 2 only for view-dependent real profile geometry. Do not inherit Image 2's sideways/glancing eye pose, widened eye, styled updo, formal makeup, retouching, warm/pink color cast, directional studio light, black clothing or pink background. Image 3 must not influence face, skin, skull, body, clothing, light or background. Make one and only one restrained refinement relative to the base method: make the profile nose slightly smaller by reducing only the nasal tip bulk and forward projection a little. Preserve the exact nose root position, bridge length and curve, dorsum angle, alar and nostril structure, nasolabial angle, philtrum and all other features. Do not make the nose narrow, sharp, upturned, bridge-shortened or generically beautified. Keep the lips, rounded chin, chin projection, jaw, ear, eye, cheek and every non-nasal feature unchanged in design.

Hairstyle A only: near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels and tapered ends. Arrange the visible-side hair naturally behind the ear enough to keep the real ear, jawline and profile silhouette readable, while the remaining hair hangs loose behind the shoulder. No bun, updo, ponytail, Hairstyle B or A/B hybrid.

Exact 3:4 portrait, head top to upper chest, head approximately 65–72% of frame height, 85–105mm-equivalent portrait perspective, camera at eye height with horizontal optical axis, upright neutral head, coherent forehead/hairline/skull/crown/ear/jaw/chin projection. Do not tilt the head or make a dramatic shoulder pose. Neutral gray-white seamless studio, soft even low-contrast 5200–5600K illumination, neutral white balance and natural photographic skin texture. If clothing is visible, show only the authentic upper portion of the same pink high-cut one-piece Calibration Outfit, not a tank top or another garment.

Avoid three-quarter view, near-profile, face pointing image-right, mirroring, visible far iris, camera-seeking gaze, identity averaging, generic face, enlarged eye, overly small nose, narrowed nose, pointed or upturned nose, shortened bridge, pointed chin, changed jaw, high sharp cheekbone, face slimming, intense stare, smile, parted lips, age change, beauty filtering, whitening, heavy makeup, source styling leakage, updo, dramatic side light, wide-angle or top-down distortion, text, watermark, collage and multiple views.

One candidate image only. REVIEW_REQUIRED; do not label or imply Canon approval.
```

## Failure history and QA

- v001: user accepted everything except that the nose should be smaller; its pixels are ineligible.
- v002: rebuilt from the same three sources, changing only nasal-tip bulk and forward projection; user approved it.
- QA order: identity; anatomical right/image-left direction; pure-profile geometry; approved nose size while preserving root/bridge/alar relationships; lips/chin/jaw/ear; gentle gaze; camera/framing; Hairstyle A/outfit; artifacts.

Any recreated image is a new `REVIEW_REQUIRED` candidate and never overwrites the approved Master.
