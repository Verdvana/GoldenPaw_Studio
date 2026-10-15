# Reference Plan — SOC_CAMPUS_001_IMG_02_CAND_10

Status: `DRAFT — REVIEW_REQUIRED`

User revision (2026-10-15): “发型是齐刘海+马尾，鞋换成肉粉色，姿势换成蹲在地上”. This revises IMG_02 CAND_09; one fresh review candidate. All earlier generated IMG_02 images are excluded.

## Generation inputs (2)

| # | Asset ID / version | Source | Responsibility | Must not define |
|---|---|---|---|---|
| 1 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`; SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | Neck-below body proportions and anatomy only | Face, skin, hair, outfit, tights, footwear, lighting, room or pose styling |
| 2 | `L0_HOS_15_NSS_002` | `materials/hosiery/source_library/raw/15d_nude_soft_sheen/IMG_2589.jpg`; SHA-256 `1c3ea08ea6f95fb8c4f3c189dc2a0027f0214bdf031320315a60232ddf741864` | Nude sheer hosiery textile, soft sheen and continuous fabric appearance only | Person, identity, face/skin, body anatomy, pose, clothing, shoes, lighting or room |

## Text-only scoped design

- Hairstyle: straight full bangs + ponytail, explicitly user-authorized as an IMG_02-specific L2 variation under `OWNER_L1_GENERATION_SPEC.md` `draft_1.234`; no A/B blend, Canon status, or reuse.
- Face: fully obscured by the rear of the iPhone X in the mirror; no face input or visible facial features.
- Setting, shirt, pink shorts, blush-pink ballet shoes, iPhone X, and crouching pose: derived only from the user's message and `PROMPT_ASSEMBLY.md`.

## QA comparison only

- Approved Face Canon: post-generation check only to confirm the phone fully occludes the face; never a generation input.
- Approved Body Canon: optional body proportion QA only; never a generation input.

No AI/generated image or earlier shot is used as a generation or continuity reference.
