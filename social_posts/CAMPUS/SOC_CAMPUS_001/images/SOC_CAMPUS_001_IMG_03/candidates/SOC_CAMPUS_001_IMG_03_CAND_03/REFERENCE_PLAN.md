# Reference Plan — SOC_CAMPUS_001_IMG_03_CAND_03

- post_id: `SOC_CAMPUS_001`
- image_asset_id: `SOC_CAMPUS_001_IMG_03`
- candidate_id: `SOC_CAMPUS_001_IMG_03_CAND_03`
- asset_level: `L3`
- status: `READY_FOR_ONE_USER_AUTHORIZED_CANDIDATE`
- reference budget: `5 / 8 images`
- resolved reference sets: `OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_L0_FACE_014_GEOMETRY_CROP_V1`, `OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `HOS_30D_BLACK_MATTE_OVERALL`

| Asset | Responsibility | Must not define |
|---|---|---|
| L0 face geometry crop 013 — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png`, SHA `1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91` | Primary face identity and feature geometry | Hair, clothing, body, lighting, scene
| L0 face geometry crop 014 — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_014_FACE_GEOMETRY_CROP_001.png`, SHA `4b8c56d695ab768e1820b5b8ea826282f811f2ecbce3d0a3b061bff4c793fd29` | Supporting L0 left-three-quarter depth/asymmetry only | Expression, hair, makeup, styling, lighting, camera/background
| L0 skin crop 012 — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png`, SHA `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12a6b79182026bd788` | Natural skin tone/texture only | Face geometry, hair, outfit, body, lighting
| Face-excluded Body derivative — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`, SHA `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | Neck-below body scale/proportions and limb anatomy | Face, hair, skin identity, outfit design, hosiery, setting/light
| `L0_HOS_30_BM_003` — `materials/hosiery/source_library/raw/30d_black_matte/IMG_2557.JPG`, SHA `302c10d81dc753490029aa392b45664c21d09eb6f7aa2e81f09a355f91a150bd` | Charcoal-black hue and matte textile response only | Target denier, identity, body, pose, clothing, footwear, scene/light

- `generation_inputs`: five above-listed original L0/derivative images only.
- `qa_comparison_only`: approved `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001` and `OWNER_BODY_01_FRONT_CANON_007`; comparison only after generation.
- `must_not_use`: IMG_01/IMG_02 approved L3 images, all generated candidates, AI face/body Canons as generation inputs. Outfit and hairstyle are text-only L2 design continuity.
- Visible face: yes, near-three-quarter toward the food stall; use source-derived `FACE_02_LEFT_3Q_NEUTRAL_METHOD.md` constraints.
