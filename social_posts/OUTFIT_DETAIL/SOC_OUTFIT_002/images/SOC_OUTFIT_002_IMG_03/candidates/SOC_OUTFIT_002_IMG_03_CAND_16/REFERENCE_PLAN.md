# Reference Plan — SOC_OUTFIT_002_IMG_03_CAND_16

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_03`
- candidate_id: `SOC_OUTFIT_002_IMG_03_CAND_16`
- asset_level: L3
- status: `READY_FOR_GENERATION`; after generation `REVIEW_REQUIRED`
- user authorization: Continued IMG_03 gate, preserving user-approved dark scene and outfit direction while correcting CAND_15's cropped slipper. Full-body framing with visible margin below both shoes is required.
- reference_count: 5; tool maximum 5
- face_visible: small edge fragment only; source-derived L0 face generation only.

| Generation input | Responsibility | Must not define |
|---|---|---|
| `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` (SHA-256 `1c6ad34c3f51c2d9fae4d69630d54fa50f6629cd9def55e0caca2a8234193e91`) | Face identity/feature geometry for the small visible fragment | hair, makeup, source lighting/background, body, clothing, skin retouch/color, camera design |
| `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png` (SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd`) | Natural warm-neutral skin context only | fine geometry, hair, makeup, body, clothing, lighting/background |
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` (SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`) | Neck-below proportions, limb and full-body scale only | face, hair, identity, skin, outfit, hosiery, footwear, scene, lighting |
| `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png` (SHA-256 `216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63`) | Brown blazer, ivory knit, pleated skirt construction/colors only | face, hair, body, skin, hosiery, footwear, identity, pose, environment |
| `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png` (SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910`) | White matte hosiery textile/continuity only | depicted face/likeness, hair, body proportions, skin, identity, pose, scene, footwear design |

## Face-safe and shot routing

- `generation_inputs`: five scoped references above. Generate the small visible face fragment only from L0-derived geometry/skin crops using `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` (`characters/CHR_HUMAN_001_OWNER/canon/face/FACE_01_FRONT_NEUTRAL_METHOD.md`).
- `qa_comparison_only`: approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` at `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; never attach to ImageGen.
- Hair A only; swept behind the visible cheek/ear.
- No previous generated candidate is an input or authority.
- Temporary scene: generic dim forest park after dusk. Closed-toe cream plush slippers and extra bottom frame margin are text-only shot requirements.
