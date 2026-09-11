# FACE_01_FRONT_NEUTRAL_v005 — QA

- reviewer: AI technical precheck
- review_date: 2026-09-10
- overall: FAIL
- approval_status: REJECTED
- eligible_as_identity_reference: no
- eligible_for_next_gate: no

| Domain | Result | Evidence / remaining decision |
|---|---|---|
| Reference isolation | PASS BY PROMPT/RECORD | B L1 image supplied for face/skin only; DSC00847 supplied for hair only; no generated Face candidate supplied |
| Framing/aspect | PASS | one 1086×1448 exact 3:4 head-and-upper-torso portrait |
| Eye gaze | PASS | eyes look horizontally toward the lens |
| Whole-head eye-level projection | FAIL | user reported essentially no improvement: the crown still reads as viewed from above |
| Target face identity | USER-CONFIRMED PASS | user confirmed facial identity remains correct |
| Skin tone | FAIL | user reported a slight lightening relative to the B appearance anchor |
| HAIRSTYLE_A | FAIL | user reported that the result still does not fully follow DSC00847 |
| Calibration Outfit | PASS | plain pink upper portion visible |
| Lighting/background | PASS | neutral gray-white studio with soft even illumination |
| Skin/anatomy | PASS | coherent photographic face with no obvious structural artifact |
| Canon promotion | REJECTED | superseded by v006; never use v005 as a pixel reference |

## User review checklist

Please decide separately whether:

1. facial identity and skin tone remain correct despite adding the DSC00847 hair reference;
2. Hairstyle A now matches DSC00847 closely enough;
3. the forehead, hairline, crown and face now share a single true eye-level projection;
4. no residual top-down crown surface or overlong receding scalp part remains.
