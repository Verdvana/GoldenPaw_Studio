# Reference Plan — SOC_OUTFIT_002_IMG_03_CAND_10

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_03`
- candidate_id: `SOC_OUTFIT_002_IMG_03_CAND_10`
- asset_level: L3
- status: `READY_FOR_GENERATION`; final status `REVIEW_REQUIRED`
- user authorization: Existing IMG_03 generation gate (2026-10-17), continued by user's 2026-10-18 request for a new third-image candidate with revised prone leg/foot pose.
- reference_count: 5; tool maximum 5
- face_visible: only a small cropped edge glimpse; face must be generated from L0-derived source crops.

| Generation input | Responsibility | Must not define |
|---|---|---|
| `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` (SHA-256 `1c6ad34c3f51c2d9fae4d69630d54fa50f6629cd9def55e0caca2a8234193e91`) | Source-derived identity and facial feature geometry for tiny visible face portion | hair, makeup, source light/background, body, clothing, camera design, skin retouch/color |
| `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png` (SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd`) | Natural warm-neutral skin color/texture only | fine geometry, hair, makeup, body, clothing, lighting design, background |
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` (SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`) | Neck-below body proportions only | face, hair, identity, skin, clothing, hosiery material, pose, scene, lighting |
| `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png` (SHA-256 `216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63`) | Approved dark chocolate-brown blazer and pleated skirt; ivory high-neck knit; clothing construction/color only | face, hair, body/proportions, skin, hosiery material, identity, pose, environment |
| `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png` (SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910`) | Soft-white matte pantyhose textile and continuous heel/instep/toe coverage only | face/likeness, hair, body proportions, skin, identity, shoes, pose, environment |

## Color and scene reference routing

- User requested the outfit and picnic-mat colors to match image 02. Image 02 candidate `SOC_OUTFIT_002_IMG_02_CAND_08` was inspected for color notes only and is **not** a generation input; its pose, person, reflection, park composition, and other L3 content are excluded. The approved outfit design reference independently supplies the same brown/ivory clothing palette.
- Picnic mat: warm saturated orange, specified in text from the post's approved temporary-dressing brief; no generated image defines the mat.
- Environment and pose are text-only temporary shot design. No previous IMG_03 candidate is a generation input.
- `generation_inputs` are exactly the five approved/scoped references in the table. `qa_comparison_only`: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` at `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; never attach to ImageGen.
- Hairstyle A is specified in text only for the tiny visible hair sliver.
