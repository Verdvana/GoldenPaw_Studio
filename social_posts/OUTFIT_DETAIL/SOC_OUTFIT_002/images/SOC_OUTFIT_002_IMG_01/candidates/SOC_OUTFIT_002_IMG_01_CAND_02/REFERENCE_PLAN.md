# Candidate 02 Reference Plan

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_01`
- candidate_id: `SOC_OUTFIT_002_IMG_01_CAND_02`
- status: READY_FOR_GENERATION
- reference_count: 4
- budget_limit: 8

| Reference | Use / responsibility | Must not define |
|---|---|---|
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1`, `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | generation input: neck-below body and leg proportions | face, hair, identity, clothes, hosiery material, lighting, background |
| `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012`, `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png`, SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910` | generation input: skirt/blazer fit, white matte hosiery and continuous foot coverage | depicted face, hair, identity, body proportions, skin |
| `SOC_OUTFIT_002_IMG_01_CAND_01`, `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_01/candidates/SOC_OUTFIT_002_IMG_01_CAND_01/SOC_OUTFIT_002_IMG_01_CAND_01.png`, SHA-256 `133d82eabcbc11c37e314bb63c51ad20e851f683b5a10278b11e8e5a079d6c7e` | continuity only: camera angle, orange mat, grass, food placement and broad crop | body proportions/shape, leg pose, hosiery response, face, identity, clothing detail, lighting, rendering artifacts |
| Face Canon | none | face not visible; no face comparison input |

- face visible: no
- face inputs: none required
- body rule: deterministic face-excluded derivative only
- user change: bent legs folded back to the side; this overrides the straight-legged pose in Candidate 01

No other AI image defines this candidate's pose or body geometry.
