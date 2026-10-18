# Candidate 02 Reference Plan

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_02`
- candidate_id: `SOC_OUTFIT_002_IMG_02_CAND_02`
- status: READY_FOR_GENERATION
- reference_count: 5
- budget_limit: 8

| Reference | Use / responsibility | Must not define |
|---|---|---|
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1`, face-excluded derivative path, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | generation input: neck-below body proportions | face, identity, hair, clothes, hosiery material, scene |
| `OWNER_HAIR_A_01_FRONT_CANON_001`, `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`, SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219` | generation input: Hair A only | face, skin, body, clothes, scene |
| `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE`, design reference path, SHA-256 `216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63` | generation input: blazer, knit top and pleated skirt only | person, body, face, hair, skin, identity, hosiery material, footwear detail |
| `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012`, worn-front path, SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910` | generation input: white pantyhose and cream plush mule design/fit only | depicted face, hair, body proportions, skin, identity |
| `SOC_OUTFIT_002_IMG_02_CAND_01`, prior candidate path, SHA-256 `7c8313592e1e5ebad2e24c8bc5d67794baf11f2f9afa808503671e06577e878c` | continuity only: park mirror placement, circular framing and camera-to-mirror perspective | face, identity, expression, body proportions, hair design, outfit, hosiery, footwear, reflection scale, wide-angle strength, lighting/rendering artifacts |

## Face-safe declaration

- face visible: no; phone fully occludes the face
- face generation inputs: none; do not invent visible facial features
- body: deterministic face-excluded derivative only
- hairstyle: Hair A only
- previous candidate: continuity of mirror placement/composition only; user's new reflection scale and wide-angle instructions override it
- QA Face Canon: not required as a generation input; verify the face remains fully obscured
