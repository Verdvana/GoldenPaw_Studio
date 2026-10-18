# Social Post Reference Plan

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_02`
- candidate_id: `SOC_OUTFIT_002_IMG_02_CAND_01`
- status: READY_FOR_GENERATION
- reference_count: 6 (five generation inputs plus Face Canon QA-only)
- budget_limit: 8
- selected_reference_set_ids: [OWNER_L0_FACE_013_GEOMETRY_CROP_V1, OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1, OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE, OWNER_HAIR_A_FRONT_CANON_L1, OWNER_CASUAL_AUTUMN_02_WORN_FRONT_APPROVED_V012]

| Priority | Reference ID/path | Level/status/version | Use | Responsibility | Must not define |
|---:|---|---|---|---|---|
| 1 | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` / `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` / SHA-256 `1c6ad34c3f51c2d9fae4d69630a54fa50f6629cd9def55e0caca2a8234193e91` | deterministic L0-derived | generation_input | face geometry/identity only | source hair, makeup, retouched skin/color, camera, light, body, clothing, background |
| 2 | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png` / `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` / SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd` | deterministic L0-derived | generation_input | natural warm-neutral skin context only | fine geometry, hair, makeup, camera, body, clothes, lighting design, background |
| 3 | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` / `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` / SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | approved deterministic derivative | generation_input | neck-below proportions only | face, hair, identity, outfit, hosiery material, lighting, background |
| 4 | `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png` / `OWNER_HAIR_A_01_FRONT_CANON_001` / SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219` | approved L1 | generation_input | Hair A front design only | face, skin, body, outfit, lighting, background |
| 5 | `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png` / `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` / SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910` | approved L2 | generation_input | clothing/fit/drape and medium-thick matte-white hosiery only | depicted face, hair, body proportions, skin, identity lineage |
| 6 | `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg` / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` / SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4` | approved L1 | qa_comparison_only | post-generation identity, facial relationships, skin contamination and projection check | all generation properties; never attach to generation tool |

## Face-safe declaration

- face visible: yes
- source-derived Face method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` (`characters/CHR_HUMAN_001_OWNER/canon/face/FACE_01_FRONT_NEUTRAL_METHOD.md`); apply face/skin source rules and Hair A camera/projection constraints adapted to an outdoor mirror selfie
- L0/L0-derived face inputs: OWNER_013 geometry crop and OWNER_012 skin-context crop above
- approved AI Face Canon: QA comparison only, not attached to generation
- face-excluded body derivative and checksum: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1; `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`

## Environment

The circular convex vehicle-safety mirror, pole and public path junction are text-only temporary scene details. It is not a recurring environment or prop Canon.
