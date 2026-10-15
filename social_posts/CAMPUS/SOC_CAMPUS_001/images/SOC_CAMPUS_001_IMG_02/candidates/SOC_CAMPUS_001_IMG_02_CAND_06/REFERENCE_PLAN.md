# Reference Plan — SOC_CAMPUS_001_IMG_02_CAND_06

Status: `DRAFT — REVIEW_REQUIRED`

User authorization (2026-10-15): asked that the hosiery texture read clearly and the odd shoes be replaced with black single-strap heels. One revised candidate only.

## Generation inputs (5 / ImageGen tool limit)

| # | Asset ID / version | Source | Responsibility | Must not define |
|---|---|---|---|---|
| 1 | `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png`; SHA-256 `1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91` | Source-derived face identity and geometry only | Hair, body, clothing, lighting, stage, makeup or background |
| 2 | `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png`; SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd` | Natural skin tone/texture only | Face geometry, expression, makeup, hair, clothes, lighting or background |
| 3 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`; SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | Neck-below proportions and limb anatomy only | Face, skin, hair, clothes, hosiery material, lighting or environment |
| 4 | `L0_OWNER_006` / Hairstyle B L0 | `characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg`; SHA-256 `734458326895b48099efa0dc58c43646d8b104823c1c36c1def8f27d08d88c17` | Hairstyle B hairline, pulled-back front and gathered hair only | Face/identity, expression, skin, sweater, body, light or background |
| 5 | `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001` / approved L1 | `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/CHR_WOMAN_001_HB04_HAIR_B.jpg`; SHA-256 `e83de80864c158a299bc3e2042b198fe76bd9452b01a7d595a1cd0d973fd613f` | Hairstyle B design/color and claw-clip detail only | Face generation, skin identity, body, clothing, light or background |

Nearest hosiery material reviewed: `L0_HOS_15_NSS_002`, `materials/hosiery/source_library/raw/15d_nude_soft_sheen/IMG_2589.jpg`, SHA-256 `1c3ea08ea6f95fb8c4f3c189dc2a0027f0214bdf031320315a60232ddf741864`. The ImageGen tool accepts at most five references, so it is represented by an explicit text material specification only. No AI/generated candidate or prior IMG_02 output is used.

## QA comparison only

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`: approved face Canon, comparison after generation only.
- Approved Body Canon: proportion QA only, not attached to generation.
