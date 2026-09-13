# EXP_12_SHY_v002 — QA

- asset_id: `EXP_12_SHY`
- candidate_id: `EXP_12_SHY_v002`
- asset_level: L1 candidate
- reviewer: AI technical precheck; user approval required
- review_date: 2026-09-13
- overall: PASS_USER_APPROVED
- approval_status: APPROVED

| Check | Status | Evidence / correction |
|---|---|---|
| Fresh source-parallel reconstruction | PASS | Only approved Face, approved Hair-A and scoped real `13.jpg` were supplied; v001 and all Expression images were excluded |
| Same approved identity | PASS_AI_PRECHECK | Permanent feature relationships, adult age and base skin tone visually align with FACE_01 |
| Head lowered appropriately | PASS | Modest natural downward pitch and gently lowered chin are visible without deep bow, side tilt or shoulder collapse |
| Gaze follows lowered head | PASS_AI_PRECHECK | Both eyes coherently avert downward toward one side without ocular distortion |
| Slightly more smile | PASS | Fully closed bilateral corner lift is clearer than v001 but remains restrained, with no teeth or laugh |
| Subtle natural blush | PASS | Light symmetric soft-rose warmth is localized to upper cheeks with feathered edges; no cosmetic circles or global skin-tone shift |
| Adult natural shyness | PASS | No childish coyness, seduction, wink, pout, lip bite, panic or theatrical acting |
| L0 responsibilities isolated | PASS | No hand, wedding makeup, veil, wedding clothing, L0 hairstyle, strong head turn or background inherited from `13.jpg` |
| Permanent geometry preserved | PASS_AI_PRECHECK | No visible redesign of eyes, brows, nose, lips, jaw or chin beyond head projection and transient expression |
| Approved visible Hair A preserved | PASS_SCOPED | Near-center part, controlled crown and long straight dark-brown panels remain consistent |
| Correct framing/outfit/background | PASS | 1086x1448 exact 3:4, neutral studio and pink Calibration Outfit upper portion |
| No prohibited artifacts | PASS | No hands, props, second person, text, logo, watermark, collage or multiple views |

## Promotion decision

The user explicitly approved v002 on 2026-09-13. Its raster was moved unchanged to the approved Canon component path. This approval is expression-action scoped and does not lock the complete Expression set or `owner_v1.0`; v001 remains rejected.
