# Owner Face Canon Index

```yaml
index_id: OWNER_FACE_CANON_INDEX
character_id: CHR_HUMAN_001_OWNER
index_revision: 4
updated_at: "2026-09-11"
full_release_lock_status: UNLOCKED
approved_face_components: 5
```

This is the human-readable lookup index for current approved Face Masters. Machine routing remains in `registries/reference_sets.yaml`.

## Current approved Masters

| Asset ID | View contract | Current JPG Master | SHA-256 | Downstream set | L1 recovery method |
|---|---|---|---|---|---|
| `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` | front neutral, eye-level | `approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg` | `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4` | `OWNER_FACE_FRONT_NEUTRAL_CANON_L1` | `FACE_01_FRONT_NEUTRAL_METHOD.md` |
| `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001` | anatomical left 3/4, face points image-left | `approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg` | `3f50c08e2993aa8dd406abd093d24f8a581b6e1475aa4dd57bda3884fed3b745` | `OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1` | `FACE_02_LEFT_3Q_NEUTRAL_METHOD.md` |
| `OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001` | anatomical right 3/4, face points image-right | `approved/FACE_03_RIGHT_3Q_NEUTRAL/OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001.jpg` | `002b47b9b5e15d3a85d1467eb6b73890254c8d69d9d1422b24b5964841d412d8` | `OWNER_FACE_RIGHT_3Q_NEUTRAL_CANON_L1` | `FACE_03_RIGHT_3Q_NEUTRAL_METHOD.md` |
| `OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001` | anatomical left profile, face points image-right; constrained reconstruction approved by user | `approved/FACE_04_LEFT_PROFILE_NEUTRAL/OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001.jpg` | `b6c1d513a4ce8f32d70860de2dde2816ef5f1400c82e09f4550b96e9545798c4` | `OWNER_FACE_LEFT_PROFILE_NEUTRAL_CANON_L1` | `FACE_04_LEFT_PROFILE_NEUTRAL_METHOD.md` |
| `OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001` | anatomical right profile, face points image-left | `approved/FACE_05_RIGHT_PROFILE_NEUTRAL/OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001.jpg` | `de670f987d341e686f5239d6b5c7a920cd431050c2907c26de759a5cf37f6b97` | `OWNER_FACE_RIGHT_PROFILE_NEUTRAL_CANON_L1` | `FACE_05_RIGHT_PROFILE_NEUTRAL_METHOD.md` |

All five Face Masters are user-transcoded transfer-efficient JPG files at 1086×1448, exact 3:4. FACE_04's uploaded conversion was initially named `OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001.jpg` inside the FACE_04 folder; it has been corrected to the FACE_04 asset filename without re-encoding.

## Format and provenance rule

- The user transcoded the four approved PNG Masters to JPG to reduce transfer volume.
- The JPG checksum is now the authoritative current-file fingerprint for lookup and downstream attachment.
- The source candidate PNG path and original checksum remain textual generation/approval provenance; its raster is removed after promotion so the current JPG is the single physical Master. JPEG conversion is not recorded as a new generation or identity decision.
- L1 recreation must use each method's recovery set. Do not use either the JPG Master or the historical candidate PNG as an AI-to-AI recovery chain.
- These are approved components with `UNLOCKED_COMPONENT`; the complete `owner_v1.0` release is not locked.

## FACE_04 evidence note

FACE_04 was explicitly approved by the user from the constrained v001 candidate. Its method permanently records that no matching-direction true-profile L0 exists: `14.jpg` supplies only same-direction natural asymmetry and coarse depth. Reproduction must use the recovery set and must never mirror/use FACE_05, FACE_03, another generated angle, the approved FACE_04 JPG, or the source candidate PNG.
