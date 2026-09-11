# FACE_04_LEFT_PROFILE_NEUTRAL — Approved Reproduction Method

```yaml
method_id: OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_METHOD_V1
status: APPROVED_METHOD
approved_component: OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001
source_candidate: FACE_04_LEFT_PROFILE_NEUTRAL_v001
generation_spec_revision: draft_1.22
generation_identity_revision: draft_0.21
documentation_spec_revision: draft_1.27
documentation_identity_revision: draft_0.26
recovery_reference_set: OWNER_FACE_LEFT_PROFILE_NEUTRAL_RECOVERY_V1
downstream_reference_set: OWNER_FACE_LEFT_PROFILE_NEUTRAL_CANON_L1
recreated_output_status: REVIEW_REQUIRED
```

This is the self-contained recovery recipe for the approved left-profile L1 Face component. Ordinary L2/L3 shots may use the approved Master within its metadata scope. Recreating the L1 component starts from the three ordered inputs below and always produces a new `REVIEW_REQUIRED` candidate.

Critical evidence limitation: no matching-direction true-profile L0 exists. The user approved the constrained generated result as the current Canon component, but this does not turn it into real-source evidence. Never use the approved JPG, source candidate PNG, FACE_03, FACE_05, another generated angle, a previous shot, or any mirror as an L1 recovery input.

## Approved output fingerprint

- approved asset: `OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001`
- path: `approved/FACE_04_LEFT_PROFILE_NEUTRAL/OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001.jpg`
- dimensions: 1086×1448, exact 3:4
- current JPG SHA-256: `b6c1d513a4ce8f32d70860de2dde2816ef5f1400c82e09f4550b96e9545798c4`
- approved source-candidate PNG SHA-256: `8e98187213ae2ef2a9a135611b34c5d828ff99ce9c8c3efcd7e61ecb12699c83`
- format note: user-transcoded JPEG is the single physical downstream Master; the filename was corrected from an accidental FACE_05 label without re-encoding, while the former candidate PNG path/checksum remain as textual provenance
- accepted prompt basis: conservative left-profile reconstruction from front identity, limited same-direction real depth, and isolated Hairstyle A
- seed/settings: built-in ImageGen returned no seed or sampler settings; continuity depends on fixed input order, role isolation, prompt structure and QA

## Exact recovery input order and fingerprints

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
   - path: `approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
   - dimensions: 1086×1448
   - SHA-256: `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`
   - responsibility: highest authority for exact identity, skull and fine feature relationships, adult age, neutral-studio skin, rounded lower face and expression
   - must not define: missing left-profile depth by simple rotation, body, final outfit, Hairstyle B or episode setting

2. `L0_OWNER_012`
   - path: `../../source/identity/raw/14.jpg`
   - dimensions: 240×320
   - SHA-256: `f7a83644f202ebec95134c6d115397b9f52f12e79b5fb227a6b79182026bd788`
   - responsibility: real same-person face/nose pointing image-right, visible-side natural asymmetry, and coarse orbit/nose/cheek/jaw depth only
   - must not define: fine pure-profile silhouette, lens-neutral proportions, camera-seeking gaze, phone distortion, hair, clothing, makeup, skin color, light or background

3. `OWNER_HAIRSTYLE_A_FACE_MASKED_001`
   - path: `reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`
   - dimensions: 769×1080
   - SHA-256: `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`
   - responsibility: Hairstyle A near-center part, close roots, low crown volume, long straight loose silhouette, face-framing panels and tapered ends
   - must not define: face, skin, skull, body, clothing, light or background; the gray oval is deleted information

Input order is fixed. Do not add FACE_04 candidate/approved pixels, FACE_03, FACE_05, another generated Face angle or a mirror.

## Approved direction and appearance contract

- anatomical left facial plane visible; face and nose point image-right;
- true 85–90° profile, one eye principally visible and no far iris beyond the bridge;
- visible eye looks naturally ahead toward image-right, not toward camera;
- user-approved conservative forehead–nose–lips–rounded-chin silhouette;
- softly full cheek, restrained low-soft cheekbone, rounded jaw transition and non-pointed chin;
- moderate natural nose, never tall, narrow, sharp, upturned, doll-like or strongly projecting;
- eye-height camera, horizontal optical axis, upright neutral head, 85–105mm-equivalent perspective;
- exact 3:4, head top to upper chest, head approximately 65–72% of frame height;
- neutral gray-white studio, soft 5200–5600K light, HAIRSTYLE_A, and visible upper portion of the pink Calibration Outfit.

## Canonical prompt assembly

Preserve the complete prompt stored in `candidates/FACE_04_LEFT_PROFILE_NEUTRAL_v001/generation_record.md` under “Final assembled prompt”. When recreating, change only the candidate ID and governing revision labels. Keep the input descriptions in the same order and retain every direction, identity, evidence-limit, hairstyle, camera, outfit and negative constraint. Do not add a generated comparison image.

## Success history and QA

- v001: generated from the exact three scoped sources with no mirror or generated angle; technical QA passed and the user explicitly approved it without requested changes.
- QA order: reference isolation; limited-evidence disclosure; anatomical left/image-right direction; true-profile geometry; identity; nose/lip/chin/jaw/ear relationships; gentle gaze; camera/framing; Hairstyle A/outfit; artifacts.
- Any recreated image is a new `REVIEW_REQUIRED` candidate and never overwrites the approved Master.
