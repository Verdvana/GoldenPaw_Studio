# FACE_05_RIGHT_PROFILE_NEUTRAL_v001 — QA

- reviewer: AI technical precheck
- review_date: 2026-09-10
- overall: TECHNICAL_PASS_USER_REVIEW_REQUIRED
- approval_status: REVIEW_REQUIRED
- eligible_as_identity_reference: no
- eligible_for_next_face_component: no, pending explicit user approval

| Domain | Result | Evidence / remaining decision |
|---|---|---|
| Reference isolation | PASS BY RECORD | Approved FACE_01, real `11.jpg`, and masked Hairstyle A only; no prior profile candidate, FACE_02, FACE_03 or mirrored input |
| Framing/aspect | PASS | 1086×1448 exact 3:4; one head-to-upper-chest portrait without collage or text |
| Direction | PASS | Face and nose point image-left; recorded as anatomical right profile under the project convention |
| Full-profile geometry | PASS | Approximately 85–90°; one eye principally visible, no second iris, and a clean forehead–nose–lips–chin silhouette |
| Camera/head projection | PASS | Visually eye-level and upright without obvious phone, top-down or wide-angle distortion |
| Identity | USER PARTIAL PASS | User accepted all visible identity/presentation attributes except that the nose should be slightly smaller |
| Real profile correspondence | USER PARTIAL PASS | Profile structure, lips, chin, orbital depth, ear and jaw-neck transition accepted; nasal size requires one restrained revision |
| Chin and cheekbone | PASS | Chin reads softly rounded rather than pointed; cheekbone is restrained and integrated into the cheek |
| Gaze/expression | PASS | Visible eye looks naturally forward toward image-left; mouth is closed and expression relaxed-neutral |
| Skin/makeup | PASS | Neutral skin treatment and restrained makeup; no pink-background or formal-retouching leakage |
| HAIRSTYLE_A | PASS | Long straight loose dark-brown hair with controlled crown; visible-side hair is behind the ear; no updo/B blend |
| Calibration Outfit | PASS WITH NON-AUTHORITATIVE NOTE | Pink upper portion is present; garment geometry remains outside this Face asset's authority |
| Anatomy/artifacts | PASS | Ear, eye, nose, lips and neck are coherent; no text or watermark |
| Canon promotion | BLOCKED PENDING USER | Candidate remains `REVIEW_REQUIRED`; explicit approval is required |

## User review checklist

1. Does the side view still read as the same woman as the three approved Face components?
2. Are the nose bridge/tip, lips, rounded chin, jaw/neck transition and ear placement accurate?
3. Is the pure profile direction, gentle forward gaze, Hairstyle A and framing acceptable?

QA does not promote this asset. Explicit user approval is still required.

## User feedback incorporated for next candidate

The user stated: “鼻子小一点，别的ok”. v002 may change only nasal tip bulk and forward projection slightly. v001 pixels remain ineligible as a generation input.
