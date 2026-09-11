# FACE_02_LEFT_3Q_NEUTRAL_v001 — QA

- reviewer: AI technical precheck
- review_date: 2026-09-10
- overall: USER_REVISION_REQUESTED
- approval_status: REVIEW_REQUIRED
- eligible_as_identity_reference: no
- eligible_for_next_face_component: no, pending explicit user approval

| Domain | Result | Evidence / remaining decision |
|---|---|---|
| Reference isolation | PASS BY RECORD | Approved `FACE_01` defines identity; `L0_OWNER_013` defines scoped three-quarter depth; masked `L0_OWNER_017` derivative defines Hairstyle A; no failed candidate supplied |
| Framing/aspect | PASS | 1086×1448 exact 3:4; single head-to-upper-chest portrait with no collage or text |
| View direction | PASS | Nose points image-left; anatomical left facial plane is principally visible; metadata records both conventions |
| Three-quarter angle | PASS | Clear moderate three-quarter rotation without reaching profile or remaining near-front |
| Camera/head projection | PASS | Visually eye-level, upright and free of obvious wide-angle, top-down or upturned-head distortion |
| Expression | PASS | Natural closed-mouth neutral expression; no inherited smile or visible teeth |
| Facial identity | AI PRECHECK PASS / USER REQUIRED | Overall skull, eyes, nose, mouth, cheeks, rounded jaw and age remain coherent with approved `FACE_01`; final recognizability and acceptable cross-angle likeness require user judgment |
| Skin and makeup | PASS | Neutral skin-tone treatment and restrained makeup; no obvious formal-photo color or directional-light leakage |
| HAIRSTYLE_A | PASS | Long straight loose dark-brown hair, near-center part, low controlled volume and face-framing lengths; no bun, updo or B-style blend |
| Calibration Outfit | PASS WITH NON-AUTHORITATIVE NOTE | Pink sleeveless upper portion is consistent with the established Face-crop presentation; garment geometry remains non-authoritative and must not be promoted from this image |
| Anatomy/artifacts | PASS | Two eyes and one visible ear are structurally coherent; no obvious facial duplication, hair fusion, text or watermark |
| User review | REVISION REQUESTED | Overall result is good; cheekbone appears slightly high, chin slightly pointed, and gaze insufficiently soft |
| Canon promotion | BLOCKED | Candidate remains `REVIEW_REQUIRED`; v002 must be rebuilt from approved/scoped Master references rather than using v001 as an image input |

## User review checklist

1. Does it unmistakably remain the same woman as the approved `FACE_01`?
2. Is the left-three-quarter rotation amount useful and natural?
3. Are the nose projection, near/far eye relationship, cheek depth, jaw and visible ear correct?
4. Are skin tone, neutral expression and apparent age consistent with the approved front view?
5. Is Hairstyle A acceptable at this angle, especially the part, crown volume and face-side hair relationship?

QA does not promote this asset. Explicit user approval is still required.
