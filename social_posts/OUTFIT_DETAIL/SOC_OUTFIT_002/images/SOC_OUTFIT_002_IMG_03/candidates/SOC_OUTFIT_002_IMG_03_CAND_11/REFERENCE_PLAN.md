# Reference Plan — SOC_OUTFIT_002_IMG_03_CAND_11

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_03`
- candidate_id: `SOC_OUTFIT_002_IMG_03_CAND_11`
- asset_level: L3
- status: `READY_FOR_GENERATION`; after generation `REVIEW_REQUIRED`
- user authorization: IMG_03 gate authorized on 2026-10-17 and continued by the 2026-10-18 user request. This is a pose correction following review of CAND_10.
- reference_count: 5; tool maximum 5
- face_visible: tiny cropped edge portion only; face generated from L0-derived crops.

| Generation input | Responsibility | Must not define |
|---|---|---|
| `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` (SHA-256 `1c6ad34c3f51c2d9fae4d69630d54fa50f6629cd9def55e0caca2a8234193e91`) | Face geometry/identity for tiny visible edge | hair, makeup, source lighting/background, body, clothes, skin color/retouch |
| `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png` (SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd`) | Natural skin color/texture only | fine geometry, hair, makeup, body, clothes, lighting/background |
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` (SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`) | Neck-below body proportions only | face, hair, identity, skin, clothing, hosiery, pose, scene, lighting |
| `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png` (SHA-256 `216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63`) | Approved brown/ivory clothing design and colors only | face, hair, body, skin, identity, hosiery, pose, environment |
| `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png` (SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910`) | Soft-white matte hosiery material and continuous foot coverage only | depicted face, hair, body proportions, skin, identity, pose, shoes, scene |

## Routing

- The inspected IMG_02 CAND_08 was used only to note the brown/ivory palette and is not a generation input. It must not define identity, pose, composition, or environment.
- Orange picnic mat is specified in text from the post's temporary dressing. No generated image is its authority.
- `generation_inputs`: the five table entries. `qa_comparison_only`: approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` at `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; never attach to ImageGen.
- Hair A is text-only for any tiny hair sliver. No previous generated candidate is an input.
