# Candidate 03 Reference Plan

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_02`
- candidate_id: `SOC_OUTFIT_002_IMG_02_CAND_03`
- status: READY_FOR_GENERATION
- reference_count: 5
- budget_limit: 8

| Reference | Responsibility | Must not define |
|---|---|---|
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | neck-below proportions | face, identity, hair, clothes, hosiery material, scene |
| `OWNER_HAIR_A_01_FRONT_CANON_001` — `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`, SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219` | Hairstyle A only | face, skin, body, clothes, scene |
| `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png`, SHA-256 `216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63` | garment design only | person, face, body, hair, skin, hosiery, footwear |
| `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png`, SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910` | white hosiery and plush mule design/fit only | depicted face, hair, body proportions, skin, identity |
| `SOC_OUTFIT_002_IMG_02_CAND_02` — `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_02/candidates/SOC_OUTFIT_002_IMG_02_CAND_02/SOC_OUTFIT_002_IMG_02_CAND_02.png`, SHA-256 `1d7b065d4afa811e129c2f883ca57e86d71797c858f813441033f4c7dcb57eb5` | continuity only: park/mirror location, circular mirror framing, outfit blocking and phone concealment | face, identity, body geometry, reflection scale, pose, optical distortion, lighting or artifacts |

## Face-safe declaration

- face visible: no; phone must fully occlude face
- generation_inputs: face-excluded body derivative; Hair A design; clothing-only garment refs; CAND_02 continuity only
- qa_comparison_only: none because face is fully hidden
- new user changes override prior mirror subject appearance: smaller figure and playful pose; optical distortion must visibly affect the reflected person, not just scenery
