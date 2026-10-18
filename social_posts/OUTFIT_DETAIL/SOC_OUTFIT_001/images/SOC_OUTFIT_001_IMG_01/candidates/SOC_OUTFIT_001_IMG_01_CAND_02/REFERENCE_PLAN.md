# Candidate 02 Reference Plan

- post_id: `SOC_OUTFIT_001`
- image_asset_id: `SOC_OUTFIT_001_IMG_01`
- candidate_id: `SOC_OUTFIT_001_IMG_01_CAND_02`
- status: READY_FOR_GENERATION
- reference_count: 6
- budget_limit: 8
- selected_reference_set_ids: [OWNER_L0_FACE_013_GEOMETRY_CROP_V1, OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE, OWNER_HAIR_A_FRONT_CANON_L1, OWNER_CASUAL_AUTUMN_02_WORN_FRONT_APPROVED_V012]

| Ref | Path / ID | Role | Must not define |
|---|---|---|---|
| L0 face geometry crop | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` / `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` | generation input: facial geometry and identity only | source hair, makeup, skin retouch/color, camera, lighting, body, clothes, background |
| L0 skin context crop | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png` / `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` | generation input: natural warm-neutral skin context only | fine geometry, hair, makeup, body, outfit, lighting design, background |
| Face-excluded body derivative | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` / `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` | generation input: neck-below proportions | face, hair, skin identity, clothing, hosiery material, lighting, background |
| Hair A Canon | `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png` / `OWNER_HAIR_A_01_FRONT_CANON_001` | generation input: Hair A only | face, skin, body, outfit, lighting, background |
| Candidate 01 | `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_001/images/SOC_OUTFIT_001_IMG_01/superseded/SOC_OUTFIT_001_IMG_01_SUPERSEDED_v1.png` / `SOC_OUTFIT_001_IMG_01_CAND_01` | continuity/composition only: crop, selfie camera position, window placement and reflection placement | face, expression, facial geometry, skin, body, hair, outfit details/material, identity, lighting/rendering artifacts |
| Face Canon | `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg` / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` | QA comparison only, post-generation | all generation properties |

The prior candidate's image is attached only to retain its broad framing, selfie angle, and glass/window composition. It is not identity, face, body, hair, outfit, material, or rendering authority. The Face Canon is not attached to generation.
