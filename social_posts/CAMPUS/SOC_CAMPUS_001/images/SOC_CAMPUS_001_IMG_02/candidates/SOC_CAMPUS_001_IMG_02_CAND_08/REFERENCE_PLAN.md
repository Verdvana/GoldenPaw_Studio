# Reference Plan — SOC_CAMPUS_001_IMG_02_CAND_08

Status: `DRAFT — REVIEW_REQUIRED`

User authorization (2026-10-15): “场景换成女生宿舍一楼的大镜子，衣服是浅粉色短裤，白色衬衫，肉色丝袜，芭蕾鞋，一手拿着iphoneX遮脸自拍，齐刘海”. This supersedes prior IMG_02 gala direction and authorizes one fresh review candidate.

## Generation inputs (2)

| # | Asset ID / version | Source | Responsibility | Must not define |
|---|---|---|---|---|
| 1 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`; SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | Neck-below body proportions and plausible anatomy only | Face, skin, hair, clothing, hosiery, footwear, lighting or background |
| 2 | `L0_HOS_15_NSS_002` | `materials/hosiery/source_library/raw/15d_nude_soft_sheen/IMG_2589.jpg`; SHA-256 `1c3ea08ea6f95fb8c4f3c189dc2a0027f0214bdf031320315a60232ddf741864` | Nude 15D sheer textile color, transparency and restrained soft sheen only | Person, identity, body shape, face/skin, pose, clothing, shoes, lighting or room |

## Prompt-authorized temporary styling

- Hairstyle: user-specified long dark-brown straight hair with full straight bangs, as a post-specific L2 variation. Existing generation spec § hairstyle explicitly permits per-image L2/L3 temporary variations when the user specifies them. This styling is exclusive to this shot, does not blend Hairstyle A/B, does not gain Canon authority and is not a reusable hairstyle reference.
- Face: fully hidden behind the iPhone X in the mirror; do not render eyes, nose, mouth or partial face. Hair/head silhouette may show. Since no face is visible, no face image is a generation input.
- Outfit/setting/phone: defined in text only from this user instruction and the post's temporary design brief.

## QA comparison only

- No Face Canon is used for generation. Approved Face Canon may be viewed after generation only to check that no unintended face fragments or AI-face-derived content leaked around the phone; there should be no visible facial features to compare.
- Approved Body Canon: QA comparison only if needed; never attach as a generation reference.

Previous IMG_02 candidates, all generated images, and IMG_01 are excluded from generation inputs and continuity references.
