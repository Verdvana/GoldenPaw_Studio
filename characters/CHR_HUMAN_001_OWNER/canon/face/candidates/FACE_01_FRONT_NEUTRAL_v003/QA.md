# FACE_01_FRONT_NEUTRAL_v003 — QA

- reviewer: AI technical precheck
- review_date: 2026-09-09
- overall: FAIL
- approval_status: REJECTED
- eligible_as_identity_reference: no
- eligible_for_next_gate: no

| Domain | Result | Evidence / remaining decision |
|---|---|---|
| Reference isolation | PASS | only the approved B-image L1 face/skin anchor was supplied as pixels; A was text-derived from its registered L0 reference |
| Framing/aspect | PASS | one 1086×1448 exact 3:4 head-and-upper-chest portrait |
| Camera/expression | PASS | eye-level, frontal, neutral closed mouth, direct gaze |
| Target face/skin preservation | USER-CONFIRMED PASS | user confirmed the target appearance and skin tone are correct |
| HAIRSTYLE_A | PASS | long, straight, loose, near-center part; no bun/updo/hybrid style |
| Calibration Outfit | PASS | plain pink upper portion visible; no source jacket or sweater |
| Lighting/background | PASS | neutral soft gray-white studio, no obvious inherited outdoor/warm light patches |
| Skin/anatomy | PASS | coherent photographic face with natural texture and no obvious structural artifact |
| Camera/head pose | FAIL | user identified residual slightly high camera and slightly upturned subject inherited from the B source |
| Canon promotion | REJECTED | superseded by v004; never use v003 as a pixel reference |

## Pending user decision

The face/skin isolation method is confirmed and recorded in `IDENTITY.md draft_0.3`. v004 must reproduce that target from the original B L1 anchor while enforcing true eye-level optics and neutral head posture.
