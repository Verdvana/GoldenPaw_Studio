# FACE_03_RIGHT_3Q_NEUTRAL_v001 — QA

- reviewer: AI technical precheck
- review_date: 2026-09-10
- overall: USER_REVISION_REQUESTED_CHIN_ONLY
- approval_status: REVIEW_REQUIRED
- eligible_as_identity_reference: no
- eligible_for_next_face_component: no, pending explicit user approval

| Domain | Result | Evidence / remaining decision |
|---|---|---|
| Reference isolation | PASS BY RECORD | Approved FACE_01 defines fine identity; low-resolution L0_OWNER_012 is limited to true right-side direction/asymmetry/coarse depth; masked L0 hair derivative defines Hairstyle A; no FACE_02 or candidate image supplied |
| Framing/aspect | PASS | 1086×1448 exact 3:4; one head-to-upper-chest portrait without collage or text |
| View direction | PASS | Nose points image-right and the anatomical right facial plane is principally visible |
| No-mirror rule | PASS BY METHOD | Image-right L0 evidence was used; the approved image-left FACE_02 was deliberately excluded |
| Three-quarter angle | PASS | Clear moderate right-three-quarter rotation, distinct from both front and profile |
| Camera/head projection | PASS | Visually eye-level, neutral upright head and no obvious phone-camera or top-down distortion |
| Facial identity | AI PRECHECK PASS / USER REQUIRED | Skull, eyes, brows, nose, lips, cheeks, rounded jaw/chin and adult age are broadly coherent with approved FACE_01; limited right-side L0 resolution makes user review decisive |
| Right-side structure/asymmetry | USER REQUIRED | Near/far eye, nose projection, right cheek-to-jaw depth and visible-ear placement look coherent, but must be judged against the real person because the only direct L0 view is 240×320 |
| Gaze/expression | PASS | Gentle, alert gaze and neutral closed mouth without inherited smile or teeth |
| Skin and makeup | PASS | Neutral skin treatment and restrained makeup; no visible mixed-light or industrial-background leakage |
| HAIRSTYLE_A | PASS | Near-center part, low controlled volume and long straight loose hair; no updo/B blend |
| Calibration Outfit | PASS WITH NON-AUTHORITATIVE NOTE | Pink upper portion is present; garment geometry remains non-authoritative |
| Anatomy/artifacts | PASS | Face and visible ear are coherent; no obvious duplicate features, text or watermark |
| User review | REVISION REQUESTED | Overall method is retained; chin remains slightly too pointed and must be rounder without collateral facial changes |
| Canon promotion | BLOCKED | Candidate remains `REVIEW_REQUIRED`; v002 must use the original scoped inputs rather than v001 pixels |

## User review checklist

1. Does this remain unmistakably the same woman as approved FACE_01 and FACE_02?
2. Is the right-side near/far eye relationship and nose projection correct?
3. Are the right cheek, jaw, chin and visible ear natural for her rather than a mirrored left side?
4. Are the gentle gaze, skin tone and Hairstyle A consistent with the approved assets?
5. Is the amount of right-three-quarter rotation appropriate?

QA does not promote this asset. Explicit user approval is still required.
