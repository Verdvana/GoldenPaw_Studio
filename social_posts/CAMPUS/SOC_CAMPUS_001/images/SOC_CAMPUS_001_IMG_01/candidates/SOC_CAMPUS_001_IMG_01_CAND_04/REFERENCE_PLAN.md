# Reference Plan — SOC_CAMPUS_001_IMG_01_CAND_04

- status: `READY_FOR_ONE_USER_REQUESTED_LEG_REFINEMENT`
- reference budget: `5 / 8 images`
- CAND_03 is the edit target for continuity only: framing, camera, pose, clothing placement and other unchanged scene pixels. It must not define face/body identity, body geometry, hair identity, skin, or hosiery material.
- Only the visible calf/shin contour is being edited. Face and body generation authorities remain source-derived L0 face references and the face-excluded approved-body derivative.

| Image | Responsibility | Must not define |
|---|---|---|
| `CAND_03` — `SOC_CAMPUS_001_IMG_01_CAND_03.png` | Edit target for shot framing, camera, pose placement, existing outfit placement and scene continuity; preserve all unedited regions | Face identity/generation, body geometry, skin, hair identity, hosiery material |
| `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png`, SHA-256 `1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91` | L0 face identity/geometry authority if face rendering is affected | Hair, clothing, body, makeup, lighting, scene |
| `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png`, SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12a6b79182026bd788` | Natural skin tone/texture only if affected | Fine geometry, identity, hair, body, outfit, lighting |
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | Neck-below body proportions and natural lower-leg scale/contour | Face, hair, outfit design, hosiery, lighting, background |
| `L0_HOS_30_BM_003` — `materials/hosiery/source_library/raw/30d_black_matte/IMG_2557.JPG`, SHA-256 `302c10d81dc753490029aa392b45664c21d09eb6f7aa2e81f09a355f91a150bd` | Hosiery black hue and matte textile response only | Denier/opacity, body/pose, shoes, text, lighting or background |

## QA only

- Approved Face02 and Body01 Canons: comparison-only after generation.
- Other AI-generated candidates: excluded as identity/body/material references.
