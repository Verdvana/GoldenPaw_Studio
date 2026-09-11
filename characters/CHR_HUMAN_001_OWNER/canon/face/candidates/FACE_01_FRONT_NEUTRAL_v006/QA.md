# FACE_01_FRONT_NEUTRAL_v006 — QA

- reviewer: AI technical precheck
- review_date: 2026-09-10
- overall: PARTIAL_PASS_REJECTED
- approval_status: REJECTED
- eligible_as_identity_reference: no
- eligible_for_next_gate: no

| Domain | Result | Evidence / remaining decision |
|---|---|---|
| Reference isolation | PASS BY RECORD | crop-only B derivative supplied for face/skin; DSC00847 supplied for hair; no generated Face candidate supplied |
| L1 source preservation | PASS | original B L1 file was not edited or overwritten; crop provenance and checksum are recorded |
| Framing/aspect | PASS | one 1086×1448 exact 3:4 portrait |
| Whole-head projection | USER-CONFIRMED PASS | user confirmed the visual eye-level angle is correct |
| Target face identity | PARTIAL PASS | user confirmed the identity direction remains correct but noted a small facial mismatch |
| Skin tone | FAIL | user noted a small mismatch from the B anchor |
| HAIRSTYLE_A | USER-CONFIRMED PASS | user confirmed the hairstyle is correct |
| Calibration Outfit | PASS | plain pink upper portion visible |
| Lighting/background | PASS | neutral gray-white studio with soft even illumination |
| Canon promotion | REJECTED | superseded by v007; never use v006 as a pixel reference |

## User review checklist

Please decide independently whether:

1. the face remains the accepted identity;
2. skin depth and warmth now match the B image;
3. the crown no longer reads as top-down;
4. Hairstyle A now reproduces DSC00847 closely enough, including flat roots, restrained density and wispy tapered ends.
