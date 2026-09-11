# FACE_01_FRONT_NEUTRAL_v007 — QA

- reviewer: AI technical precheck
- review_date: 2026-09-10
- overall: PARTIAL_PASS_REJECTED
- approval_status: REJECTED
- eligible_as_identity_reference: no
- eligible_for_next_gate: no

| Domain | Result | Evidence / remaining decision |
|---|---|---|
| Reference isolation | PASS BY RECORD | B crop is the only visible face input; DSC00847 face was masked; no generated candidate supplied |
| Source preservation | PASS | original B L1 and DSC00847 files remain unchanged; both derivatives have provenance and checksums |
| Framing/aspect | PASS | one 1086×1448 exact 3:4 portrait |
| Whole-head projection | USER-CONFIRMED PASS | user confirmed the angle is correct |
| Target face identity | FAIL | user confirmed the face remains incorrect and specified v005 facial appearance as target |
| Skin tone | USER REVIEW REQUIRED | B crop is exclusive skin authority and whitening was prohibited; final match requires user review |
| HAIRSTYLE_A | USER-CONFIRMED PASS | user confirmed the hairstyle is correct |
| Mask leakage | PASS | no visible gray oval or mask edge in output |
| Calibration Outfit | PASS | plain pink upper portion visible |
| Canon promotion | REJECTED | superseded by v008; never use v007 as a pixel reference |

## User review checklist

Please verify:

1. face details now match the B appearance anchor;
2. skin depth and warmth now match the B appearance anchor;
3. the previously accepted Hairstyle A remains correct;
4. the previously accepted visual eye-level angle remains correct.
