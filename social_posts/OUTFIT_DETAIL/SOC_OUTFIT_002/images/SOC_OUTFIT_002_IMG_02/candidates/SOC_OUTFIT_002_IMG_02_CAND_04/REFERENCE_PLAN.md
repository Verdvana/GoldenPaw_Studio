# Candidate 04 Reference Plan

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_02`
- candidate_id: `SOC_OUTFIT_002_IMG_02_CAND_04`
- status: READY_FOR_GENERATION
- reference_count: 5
- budget_limit: 8

| Reference | Responsibility | Must not define |
|---|---|---|
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | neck-below proportions | face, identity, hair, clothes, hosiery material, scene |
| `OWNER_HAIR_A_01_FRONT_CANON_001` — `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`, SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219` | Hairstyle A only | face, skin, body, clothes, scene |
| `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png`, SHA-256 `216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63` | garment design only | person, face, body, hair, skin, hosiery, footwear |
| `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png`, SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910` | white hosiery and plush mule design/fit only | depicted face, hair, body proportions, skin, identity |
| `SOC_OUTFIT_002_IMG_02_CAND_03` — `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_02/candidates/SOC_OUTFIT_002_IMG_02_CAND_03/SOC_OUTFIT_002_IMG_02_CAND_03.png`, SHA-256 `9e72ca87aeee48b06a2b09152f42834361d72a98e6bb8ef51bb555c21558cbcb` | continuity only: forest park and round mirror framing, small scale, playful pose and phone concealment | face, identity, body geometry, optical distortion, lighting or artifacts |

## Face-safe declaration

- face visible: no; phone fully obscures face
- generation_inputs: face-excluded body derivative, Hair A design, clothing design, hosiery/footwear design
- continuity_only_input: CAND_03 only for scene and playful pose concept; its insufficient person distortion is explicitly rejected
- qa_comparison_only: none; face fully obscured
