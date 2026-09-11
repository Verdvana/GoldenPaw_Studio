# FACE_01_FRONT_NEUTRAL_v008 — QA

- reviewer: AI technical precheck
- review_date: 2026-09-10
- overall: FAIL
- approval_status: REJECTED
- eligible_as_identity_reference: no
- eligible_for_next_gate: no

| Domain | Result | Evidence / remaining decision |
|---|---|---|
| Reference isolation | PASS BY RECORD | only B-derived face/skin pixels and face-masked DSC00847 hair pixels supplied; no AI candidate supplied |
| Framing/aspect | PASS WITH VARIATION | one 1086×1448 exact 3:4 image; tighter head-and-shoulders crop used after safety block |
| Whole-head projection | USER REVIEW REQUIRED | user-confirmed corrective camera method repeated from text; final acceptance remains with user |
| Target facial direction | FAIL | user reports no meaningful improvement over the prior two versions |
| Face width | FAIL | user reports the face is slightly too wide |
| Skin tone | USER REVIEW REQUIRED | B crop remains exclusive authority and whitening was prohibited |
| HAIRSTYLE_A | USER REVIEW REQUIRED | face-masked DSC00847 is the sole hair pixel reference; user-confirmed description repeated |
| Mask leakage | PASS | no gray oval or mask boundary visible |
| Safety retry | PASS | second attempt produced a neutral, non-sexual ID-style portrait |
| Canon promotion | REJECTED | superseded by v009; never use v008 as a pixel reference |

## User review checklist

Please verify:

1. whether facial appearance now returns to the v005-approved target;
2. whether skin tone remains correct;
3. whether the already accepted Hairstyle A remains correct;
4. whether the already accepted visual eye-level angle remains correct;
5. whether the tighter framing is acceptable for `FACE_01_FRONT_NEUTRAL`.
