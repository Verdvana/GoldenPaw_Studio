# Candidate 03 Reference Plan

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_01`
- candidate_id: `SOC_OUTFIT_002_IMG_01_CAND_03`
- status: READY_FOR_GENERATION
- reference_count: 3
- budget_limit: 8

| Reference | Responsibility | Must not define |
|---|---|---|
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | neck-below body and natural limb proportions | face, hair, identity, clothing, hosiery material, lighting, background |
| `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png`, SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910` | skirt/blazer fit, white matte hosiery material/coverage | depicted face, hair, identity, body proportions, skin |
| `SOC_OUTFIT_002_IMG_01_CAND_02` — `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_01/candidates/SOC_OUTFIT_002_IMG_01_CAND_02/SOC_OUTFIT_002_IMG_01_CAND_02.png`, SHA-256 `52c27ecac87e7fc4e2f02651e4ba82470354c9665defe6c718639679cead8694` | continuity only: accepted bent-side-sit pose, crop, picnic placement, clothing texture impression | anatomy/proportions, leg lengths, precise leg geometry, hosiery material, identity, face, lighting or artifacts |

- face visible: no
- generation_inputs: body derivative for neck-below proportion only; approved worn-front for clothing/material only
- continuity_only_input: CAND_02 only for accepted pose idea/crop/scene; explicitly correct its impossible left-leg geometry
- qa_comparison_only: none
- accepted user attributes: bent legs folded to the side; Autumn 02 clothing texture
- targeted correction: left knee and foot positions must form plausible foreshortened anatomy, with left leg visibly bent and tucked beside/behind the right leg; no excessively long left thigh/shin, no knee pushed to far-left edge, feet do not line up unnaturally
