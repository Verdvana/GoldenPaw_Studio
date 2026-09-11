# FACE_01_FRONT_NEUTRAL_v001 — QA

- reviewer: AI technical precheck
- review_date: 2026-09-09
- overall: FAIL
- approval_status: REJECTED
- eligible_as_identity_reference: no
- eligible_for_next_gate: no

| Domain | Result | Evidence / remaining decision |
|---|---|---|
| Reference compliance | PASS | Exactly `L0_OWNER_012` + `L0_OWNER_010`; no prior AI face used |
| Framing/aspect | PASS | 1086×1448, exact 3:4; single head-and-upper-chest view |
| Camera/orientation | PASS | frontal, eye-level appearance, no visible head turn or dramatic perspective |
| Expression | PASS | neutral, relaxed, mouth closed, no visible teeth |
| Lighting/background | PASS | neutral gray-white studio, even soft light, no inherited colored light or strong light patch |
| Calibration hair | PASS | hair pulled back from face; treated as non-Canon calibration hair |
| Calibration outfit | PASS | plain pink shoulder straps/upper portion visible; no alternate garment or accessory |
| Skin rendering | PASS | photographic texture retained; no obvious plastic/PVC surface or extreme beauty filter |
| Face anatomy | PASS | coherent eyes, nose, lips, ears, jaw and facial symmetry; no visible structural artifact |
| Identity match | FAIL | User rejected the target appearance and directed future Face assets to follow the approved B-image face/skin anchor |
| Hairstyle policy | FAIL | Non-B L1 assets must use HAIRSTYLE_A; this candidate used temporary calibration hair |
| Canon promotion | REJECTED | Permanently ineligible as Canon or downstream reference |

## User review checklist

Please evaluate only identity geometry, not the temporary calibration hair or neutral lighting:

- overall recognizability;
- face width/length and cheek fullness;
- eye size, shape and spacing;
- brow geometry;
- nose bridge/tip/width;
- lip shape and relative fullness;
- jaw taper and chin roundness;
- apparent age.

Decision must be one of: reject with corrections; retain as a candidate and request another variant; or explicitly approve as `FACE_01_FRONT_NEUTRAL` for `owner_v1.0`.
