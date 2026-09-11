# FACE_01_FRONT_NEUTRAL_v010 — QA

- reviewer: AI technical precheck
- review_date: 2026-09-10
- overall: PARTIAL_PASS_REJECTED
- approval_status: REJECTED
- eligible_as_identity_reference: no
- eligible_for_next_gate: no

| Domain | Result | Evidence / remaining decision |
|---|---|---|
| Reference isolation | PASS BY RECORD | original B L1 image plus face-masked DSC00847 derivative; no AI Face candidate supplied |
| Requested constraint merge | PASS BY RECORD | v005 face/skin block and v006 hair/crown/camera block were copied from their generation records and combined |
| Framing/aspect | PASS | 1086×1448 exact 3:4, standard head-to-upper-chest framing |
| Face and features | USER-CONFIRMED PASS | user described the facial features as perfect |
| Skin tone | USER-CONFIRMED PASS | user described the skin tone as perfect |
| Whole-head projection | FAIL | user reports that the visible top-head area remains too large and does not read as eye-level |
| HAIRSTYLE_A | USER REVIEW REQUIRED | v006-confirmed hair constraint block applied to the masked DSC00847 input |
| Mask leakage | PASS | no gray mask artifact visible |
| Canon promotion | REJECTED | superseded by v011; never use v010 as a pixel reference |

## User review checklist

Please compare v010 against the desired combination: v005 facial appearance and skin, plus v006 Hairstyle A and crown/camera angle. v009 remains available as an unapproved backup candidate.
