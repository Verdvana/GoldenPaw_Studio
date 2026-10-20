# Candidate 11 Reference Plan

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_02`
- candidate_id: `SOC_OUTFIT_002_IMG_02_CAND_11`
- status: READY_FOR_GENERATION
- reference_count: 4
- budget_limit: 8
- user_direction: "透视效果大幅强化加大力度（强烈的凸面镜鱼眼广角球面畸变）；人物姿态活泼俏皮（重心微移、微曲膝、单手高举仰拍手机遮脸、另一手比耶）；凸面镜明显高于人物（大幅高度差，人物明显后仰、手臂高举向上仰角拍摄）；画面构图自然随意，打破死板对称与横平竖直"

| Reference | Responsibility | Must not define |
|---|---|---|
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | neck-below body proportions, leg and arm anatomy | face, identity, hair, clothes, hosiery, scene |
| `OWNER_HAIR_A_01_FRONT_CANON_001` — `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`, SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219` | Hair A only | face, body, clothes, skin, scene |
| `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png`, SHA-256 `216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63` | garment design (chocolate-brown blazer, ivory knit, pleated skirt) | person, face, body, hair, skin, hosiery, footwear |
| `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png`, SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910` | hosiery coverage, closed textile toes, plush mule fit | face, hair, body proportions, skin, identity |

## Face-safe declaration

- face visible: no; smartphone raised high in front of face angled upward toward the overhead mirror completely blocks face.
- generation_inputs: face-excluded body derivative, Hair A Canon, clothing design reference, worn-front hosiery/footwear reference.
- continuity_only_input: none; fresh generation addressing user feedback on perspective, pose, and layout.
- qa_comparison_only: none (face fully occluded).
