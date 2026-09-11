# Owner L0 Reference Guide

This guide prevents repeated analysis of all 16 originals. These L0 photos are used mainly while building or repairing Canon. Once `owner_v1.0` is locked, ordinary shots should use the scoped L1 Face/Body/Expression Canon instead of returning to all L0 photos.

Direction labels describe where the face points **inside the image**, avoiding left/right anatomical ambiguity.

## Approved Face routing

| Need | Use | Rule |
|---|---|---|
| downstream front body geometry | `OWNER_BODY_FRONT_CANON_L1` | use the approved L1 Body Master directly within its metadata scope |
| recreate front Body L1 Master | `OWNER_BODY_FRONT_RECOVERY_V1` | follow `canon/body/BODY_01_FRONT_METHOD.md`; never add a generated BODY_01 candidate or approved Body Master |
| downstream front-neutral identity | `OWNER_FACE_FRONT_NEUTRAL_CANON_L1` | use the approved L1 Master directly within its metadata scope |
| recreate front-neutral L1 Master | `OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1` | follow `canon/face/FACE_01_FRONT_NEUTRAL_METHOD.md`; never add a generated Face candidate |
| downstream left-3/4 neutral identity, face points image-left | `OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1` | use the approved L1 Master directly within its metadata scope |
| recreate left-3/4 neutral L1 Master | `OWNER_FACE_LEFT_3Q_NEUTRAL_RECOVERY_V1` | preserve its three-image order and follow `canon/face/FACE_02_LEFT_3Q_NEUTRAL_METHOD.md`; never add v001–v004 or the approved FACE_02 pixels |
| downstream right-3/4 neutral identity, face points image-right | `OWNER_FACE_RIGHT_3Q_NEUTRAL_CANON_L1` | use the approved L1 Master directly within its metadata scope |
| recreate right-3/4 neutral L1 Master | `OWNER_FACE_RIGHT_3Q_NEUTRAL_RECOVERY_V1` | preserve its three-image order and follow `canon/face/FACE_03_RIGHT_3Q_NEUTRAL_METHOD.md`; never mirror FACE_02 or add any FACE_03 generated pixels |
| downstream left-profile neutral identity, face points image-right | `OWNER_FACE_LEFT_PROFILE_NEUTRAL_CANON_L1` | use the approved L1 Master directly within its metadata scope and retain its limited-evidence note |
| recreate left-profile neutral L1 Master | `OWNER_FACE_LEFT_PROFILE_NEUTRAL_RECOVERY_V1` | preserve its three-image order and follow `canon/face/FACE_04_LEFT_PROFILE_NEUTRAL_METHOD.md`; never add FACE_04/FACE_03/FACE_05 generated pixels or a mirror |
| downstream right-profile neutral identity, face points image-left | `OWNER_FACE_RIGHT_PROFILE_NEUTRAL_CANON_L1` | use the approved L1 Master directly within its metadata scope |
| recreate right-profile neutral L1 Master | `OWNER_FACE_RIGHT_PROFILE_NEUTRAL_RECOVERY_V1` | preserve its three-image order and follow `canon/face/FACE_05_RIGHT_PROFILE_NEUTRAL_METHOD.md`; never add FACE_05 generated pixels, another generated angle or a mirror |

## Recommended sets

| Need | Use first | Optional second | Do not add by default |
|---|---|---|---|
| neutral frontal identity analysis | `L0_OWNER_012` (`14.jpg`) | `L0_OWNER_010` (`12.jpg`) or `L0_OWNER_007` (`9.jpg`) | retouched wedding smiles |
| high-resolution face structure support | `L0_OWNER_013` (`15.jpg`) | `L0_OWNER_009` (`11.jpg`) | full-body photos |
| profile, face pointing image-left | `L0_OWNER_009` (`11.jpg`) | none | frontal selfies |
| 3/4, face pointing image-left, L0 construction support | `L0_OWNER_013` (`15.jpg`) | `L0_OWNER_014` (`16.jpg`) only for a documented coverage failure | generated FACE_02 images; unrelated body images |
| 3/4, face pointing image-right, limited L0 support | `L0_OWNER_012` (`14.jpg`) | none | mirroring image-left sources; using this low-resolution phone image for fine or lens-neutral geometry |
| near-front smile/teeth | `L0_OWNER_008` (`10.jpg`) | `L0_OWNER_001` (`2.jpg`) or `L0_OWNER_004` (`5.png`) | neutral selfie unless identity conflict appears |
| surprise/open-mouth expression | `L0_OWNER_006` (`8.jpg`) | none | body references |
| natural laugh | `L0_OWNER_016` (`DSC01015.JPG`) | none | wedding portraits |
| frontal standing/body context | `L0_OWNER_002` (`3.jpg`) | `L0_OWNER_003` (`4.jpg`) | portraits |
| walking articulation | `L0_OWNER_003` (`4.jpg`) | none | other body states |
| side/rear silhouette context | `L0_OWNER_015` (`17.jpg`) | none | use as primary due to low resolution |
| HAIRSTYLE_A construction | `L0_OWNER_017` (`DSC00847.jpg`) | none | face/body/outfit/background from this image |
| HAIRSTYLE_B construction | `L0_OWNER_006` (`8.jpg`) | approved `HAIR_B_CANDIDATE_001` for final design detail | surprised expression, sweater, warm lighting and background |

## Selection rules

- Use at most **two owner L0 images** for a single Canon candidate unless a documented conflict requires a third.
- Pair one natural/neutral image with one high-resolution angled image when constructing identity. Do not average every photo.
- `2.jpg`, `5.png`, `10.jpg`, `15.jpg`, and `16.jpg` contain makeup and/or studio retouching; use them for geometry and expression, not canonical skin texture.
- `12.jpg` and `14.jpg` are natural neutral evidence but too small and too close-camera to define lens-neutral proportions alone.
- Body appearance differs across dates, wardrobe, pose, and likely life stage. All body images are **context only** until the user approves the adjusted Calibration Body Canon.
- `3.jpg`, `4.jpg`, and `17.jpg` must never make their dresses, shoes, or legwear part of Body Canon.
- Do not use `13.jpg` as an identity anchor: the downward pose and hand contact hide geometry.
- `DSC00847.jpg` and `8.jpg` have explicit hair responsibilities. Select them through the hairstyle reference sets; do not treat either whole image as universal authority.

## Current coverage gaps

No strong profile pointing image-right and no neutral calibration-style front/side/back body set. The approved image-left-pointing right-profile component now covers its ordinary downstream view. Real image-right 3/4 evidence remains limited and low-resolution, but its approved component also covers ordinary use. Remaining gaps are addressed through gated Canon creation, not by mirroring or overloading weak L0 images.
