# Owner Character Workspace

ID: `CHR_HUMAN_001_OWNER`. Current locked Canon release: none. Approved L1 components may exist with individual approval records; the full `owner_v1.0` remains unlocked until its version manifest is explicitly locked.

Current human-readable Face lookup: `canon/face/FACE_CANON_INDEX.md`.

L0 identity originals belong in `source/identity/raw/`. The working L1 program is split into face, expressions, body, poses, hairstyles A/B, hosiery/feet details, appearance, and immutable version manifests.

Owner calibration outfit: pink high-cut one-piece swimsuit, 15D velvet-finish sheer pantyhose, no shoes. It exists to calibrate body geometry and material continuity, not as default story wardrobe.

Approved L1 components currently include `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`, `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001`, `OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001`, `OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001`, `OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001`, `OWNER_BODY_01_FRONT_CANON_001`, and scoped `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001`. Each approval remains attribute-scoped and the complete `owner_v1.0` release is still unlocked.

For downstream front body geometry use `OWNER_BODY_FRONT_CANON_L1`. For L1 recovery use `OWNER_BODY_FRONT_RECOVERY_V1` together with `canon/body/BODY_01_FRONT_METHOD.md`; never use generated BODY_01 candidates or the approved Body Master as a new L1 pixel input.

For downstream left-three-quarter identity use `OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1`. For L1 recovery use `OWNER_FACE_LEFT_3Q_NEUTRAL_RECOVERY_V1` together with `canon/face/FACE_02_LEFT_3Q_NEUTRAL_METHOD.md`; never use a generated FACE_02 candidate as a recovery input.

For downstream right-three-quarter identity use `OWNER_FACE_RIGHT_3Q_NEUTRAL_CANON_L1`. For L1 recovery use `OWNER_FACE_RIGHT_3Q_NEUTRAL_RECOVERY_V1` together with `canon/face/FACE_03_RIGHT_3Q_NEUTRAL_METHOD.md`; never mirror FACE_02 or use generated FACE_03 pixels as a recovery input.

For downstream left-profile identity use `OWNER_FACE_LEFT_PROFILE_NEUTRAL_CANON_L1`. For L1 recovery use `OWNER_FACE_LEFT_PROFILE_NEUTRAL_RECOVERY_V1` with `canon/face/FACE_04_LEFT_PROFILE_NEUTRAL_METHOD.md`; never use the approved FACE_04 pixels, FACE_03, FACE_05, another generated angle or a mirror as a recovery input. The method retains the limited-evidence disclosure.

For downstream right-profile identity use `OWNER_FACE_RIGHT_PROFILE_NEUTRAL_CANON_L1`. For L1 recovery use `OWNER_FACE_RIGHT_PROFILE_NEUTRAL_RECOVERY_V1` with `canon/face/FACE_05_RIGHT_PROFILE_NEUTRAL_METHOD.md`; never use generated FACE_05 pixels, another generated angle or a mirror as a recovery input.
