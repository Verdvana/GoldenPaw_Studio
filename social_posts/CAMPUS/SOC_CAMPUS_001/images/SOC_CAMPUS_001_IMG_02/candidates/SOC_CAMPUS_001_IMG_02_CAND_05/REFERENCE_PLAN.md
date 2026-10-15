# Reference Plan — SOC_CAMPUS_001_IMG_02_CAND_05

Status: `DRAFT — REVIEW_REQUIRED`

User authorization (2026-10-15): “第二张换成发型B,晚礼服，缎光舍宾肉色连裤袜，一字带高跟凉鞋，在学校晚会当主持人的单反抓拍”. One candidate only.

## Generation inputs (5 / ImageGen tool limit)

| # | Asset ID / version | Source | Responsibility | Must not define |
|---|---|---|---|---|
| 1 | `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png`; SHA-256 `1c6ad34c3f51c2d9fae4d69630d54af50f6629cd9def55e0caca2a8234193e91` | Source-derived face identity and facial geometry, moderate three-quarter view, face only | Hair, body, clothes, lighting, event, expression beyond natural speech |
| 2 | `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png`; SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd` | Natural skin tone/texture context only | Geometry, identity override, makeup, hair, clothing, body, lighting |
| 3 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`; SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | Neck-below body proportions and limb anatomy only | Face, skin tone, hair, clothing, pose-performance, hosiery material, lighting |
| 4 | `L0_OWNER_006` / Hairstyle B L0 | `characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg`; SHA-256 `734458326895b48099efa0dc58c43646d8b104823c1c36c1def8f27d08d88c17` | Hairstyle B real hairline, front pulled-back sections, face-framing strands, gathered style only | Face/identity, expression, skin, sweater, body, light, background |
| 5 | `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001` / approved L1 | `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/CHR_WOMAN_001_HB04_HAIR_B.jpg`; SHA-256 `e83de80864c158a299bc3e2042b198fe76bd9452b01a7d595a1cd0d973fd613f` | Hairstyle B design/color and approved claw-clip/updo details only | Face generation, face/skin identity, body, clothes, light, background |

The closest registered hosiery material source was checked: `L0_HOS_15_NSS_002` (`materials/hosiery/source_library/raw/15d_nude_soft_sheen/IMG_2589.jpg`, SHA-256 `1c3ea08ea6f95fb8c4f3c189dc2a0027f0214bdf031320315a60232ddf741864`). It is not attached because ImageGen accepts at most five image references; use the textual target description “nude 15D sheer with restrained soft satin sheen” only. Optional face crop 014 is also omitted; crop 013 covers the required identity geometry.

## QA comparison only; never generation inputs

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` (approved L1 face identity comparison; use only after generation for identity/feature relationships and contamination QA).
- Approved body Canon may be consulted after generation for proportion QA only; do not attach it to ImageGen. Source-derived face-excluded Body derivative above is the sole body generation reference.

Rejected IMG_02 CAND_01–04 and approved IMG_01 are excluded from all generation inputs and QA lineage. No previous shot or generated image defines this candidate.
