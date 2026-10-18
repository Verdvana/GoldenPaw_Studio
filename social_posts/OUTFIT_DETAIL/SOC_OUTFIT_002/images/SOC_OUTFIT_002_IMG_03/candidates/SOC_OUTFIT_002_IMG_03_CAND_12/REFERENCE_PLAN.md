# Reference Plan — SOC_OUTFIT_002_IMG_03_CAND_12

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_03`
- candidate_id: `SOC_OUTFIT_002_IMG_03_CAND_12`
- asset_level: L3
- status: `READY_FOR_GENERATION`; after generation `REVIEW_REQUIRED`
- user authorization: IMG_03 gate, updated by user's 2026-10-18 instruction changing the scene to a dusk forest-park walking selfie and specifying plush slippers.
- reference_count: 5; tool maximum 5
- face_visible: a small portion of face; source-derived L0 face generation only.

| Generation input | Responsibility | Must not define |
|---|---|---|
| `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` (SHA-256 `1c6ad34c3f51c2d9fae4d69630d54fa50f6629cd9def55e0caca2a8234193e91`) | Face identity and feature geometry for small visible face portion | hair, makeup, source light/background, body, clothing, skin retouch/color, camera design |
| `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png` (SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd`) | Natural warm-neutral skin color/texture only | fine geometry, hair, makeup, body, clothes, lighting design, background |
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` (SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`) | Neck-below body proportions, limbs and scale only | face, hair, identity, skin, outfit, hosiery material, shoes, scene, lighting |
| `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png` (SHA-256 `216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63`) | Brown blazer, ivory knit, pleated skirt construction and colors only | face, hair, body, skin, hosiery material, shoes, identity, pose, environment |
| `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png` (SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910`) | White matte hosiery continuity and cream plush open-toe mule design only | depicted face/likeness, hair, body proportions, skin, identity, pose, environment |

## Face-safe and shot routing

- `generation_inputs`: the five scoped references above. Face is generated only from the two L0-derived face/skin crops under `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` (`characters/CHR_HUMAN_001_OWNER/canon/face/FACE_01_FRONT_NEUTRAL_METHOD.md`).
- `qa_comparison_only`: approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` at `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; never attach to ImageGen.
- Hair A only, specified in text because face/hair remain small.
- All prior IMG_03 outputs are excluded from generation input and from defining identity, body, clothing, hosiery, shoes, or environment.
- Temporary scene: generic public forest park at dusk, no recognizable signage or recurring-location claims. Camera, stride, and motion blur are text-only shot design.
