# FACE_01_FRONT_NEUTRAL_v004 — QA

- reviewer: AI technical precheck
- review_date: 2026-09-10
- overall: FAIL
- approval_status: REJECTED
- eligible_as_identity_reference: no
- eligible_for_next_gate: no

| Domain | Result | Evidence / remaining decision |
|---|---|---|
| Reference isolation | PASS | only the original approved B-image L1 face/skin anchor was supplied as pixels; neither v002 nor v003 was supplied |
| Framing/aspect | PASS | one 1086×1448 exact 3:4 head-and-upper-torso portrait |
| Eye gaze | USER-CONFIRMED PASS | user confirmed the eyes now read as looking level |
| Whole-head eye-level projection | FAIL | user identified that the crown still appears top-down and does not share the face's level projection |
| Target face/skin preservation | USER-CONFIRMED PASS | user confirmed both facial appearance and skin tone |
| HAIRSTYLE_A | FAIL | user confirmed the hairstyle does not match DSC00847 closely enough |
| Calibration Outfit | PASS | plain pink upper portion visible |
| Lighting/background | PASS | neutral gray-white studio with soft, even illumination and no obvious inherited light patches |
| Skin/anatomy | PASS | coherent photographic face and natural skin texture; no obvious structural artifact |
| Canon promotion | REJECTED | superseded by v005; never use v004 as a pixel reference |

## User review checklist

Please decide separately whether:

1. camera height and head posture now read as true eye-level;
2. facial identity matches the accepted face direction from v003;
3. skin tone matches the accepted skin direction from v003;
4. Hairstyle A remains correct.

The user-confirmed face/skin result and failure causes are recorded textually in `IDENTITY.md draft_0.4`. The v004 image itself is excluded from all downstream reference sets.
