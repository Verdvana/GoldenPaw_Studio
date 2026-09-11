# FACE_01_FRONT_NEUTRAL_v002 — QA

- reviewer: AI technical precheck
- review_date: 2026-09-09
- overall: FAIL
- approval_status: REJECTED
- eligible_as_identity_reference: no
- eligible_for_next_gate: no

| Domain | Result | Evidence |
|---|---|---|
| Format/composition | PASS | single 1086×1448 3:4 frontal studio portrait |
| HAIRSTYLE_A | PASS | long straight loose hair rather than B updo |
| Calibration Outfit | PASS | pink upper portion visible |
| Face reference isolation | FAIL | output visibly absorbed face/age/body cues from `DSC00847.jpg` instead of strictly preserving the B-image face target |
| Iteration eligibility | REJECTED | must never be used as a reference or written into `IDENTITY.md` |

## Corrective action

For v003, remove the A photo from ImageGen inputs. Use the approved B L1 image as the sole pixel reference and supply the already-analyzed HAIRSTYLE_A characteristics as text derived from `DSC00847.jpg`.
