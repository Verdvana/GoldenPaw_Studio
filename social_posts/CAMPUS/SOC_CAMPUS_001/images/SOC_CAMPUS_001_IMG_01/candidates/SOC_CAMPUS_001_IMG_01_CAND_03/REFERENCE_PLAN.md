# Reference Plan — SOC_CAMPUS_001_IMG_01_CAND_03

- post_id: `SOC_CAMPUS_001`
- candidate_id: `SOC_CAMPUS_001_IMG_01_CAND_03`
- asset_level: `L3`
- status: `READY_FOR_ONE_USER_REQUESTED_REDO`
- reference_budget: `5 / 8 images`
- generation is independent; prior generated candidates are excluded.
- resolved reference sets: `OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_L0_FACE_014_GEOMETRY_CROP_V1`, `OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `HOS_30D_BLACK_MATTE_OVERALL`
- L0 selection note: user rejected two 013-only face attempts for likeness. Crop 014 is included narrowly as secondary geometry/asymmetry support; crop 012 is skin context only. This is a documented face-coverage exception to the usual two-L0-image preference.

| Reference | Responsibility | Must not define |
|---|---|---|
| `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png`, SHA-256 `1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91` | Primary L0 face geometry and identity | Hair, makeup, retouching, body, clothing, lighting or background |
| `OWNER_FACE_L0_OWNER_014_GEOMETRY_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_014_FACE_GEOMETRY_CROP_001.png`, SHA-256 `4b8c56d695ab768e1820b5b8ea826282f811f2ecbce3d0a3b061bff4c793fd29` | Supporting natural facial geometry/asymmetry only | Its smile, makeup, hair, lighting, camera or background |
| `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png`, SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12a6b79182026bd788` | Natural skin tone/texture only | Face geometry, identity, hair, body or lighting |
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | Neck-below proportions, torso/hip/leg contour, scale | Face, hair, outfit design, hosiery appearance, light or setting |
| `L0_HOS_30_BM_003` — `materials/hosiery/source_library/raw/30d_black_matte/IMG_2557.JPG`, SHA-256 `302c10d81dc753490029aa392b45664c21d09eb6f7aa2e81f09a355f91a150bd` | Black hue and matte textile response only | 20D opacity, person, pose, garment design, text or background |

## Face-safe declaration

- Face visible: yes. Source-derived Face method plus L0 derivatives only define face generation.
- AI Face Canon `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001` is comparison-only after generation.
- Approved Body Canon `OWNER_BODY_01_FRONT_CANON_007` is comparison-only after generation; the generation input is its face-excluded derivative above.
- Excluded from generation: CAND_01, CAND_02 and all other AI-generated images; all AI face/body canons; Hairstyle A/B images.
- Hair is the user's scoped L2 design: long, dark-brown, loose, straight bangs.
