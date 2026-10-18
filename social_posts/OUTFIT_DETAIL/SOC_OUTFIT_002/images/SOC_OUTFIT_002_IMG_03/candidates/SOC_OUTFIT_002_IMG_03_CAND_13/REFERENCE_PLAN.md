# Reference Plan — SOC_OUTFIT_002_IMG_03_CAND_13

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_03`
- candidate_id: `SOC_OUTFIT_002_IMG_03_CAND_13`
- asset_level: L3
- status: `READY_FOR_GENERATION`; after generation `REVIEW_REQUIRED`
- user authorization: continued IMG_03 generation gate, with latest user correction on 2026-10-18: much smaller face sliver, genuinely dark full-frame after-dusk exposure, and hosiery continuously covering all toes and toe gaps beneath plush mules.
- reference_count: 5; tool maximum 5
- face_visible: tiny edge sliver only; source-derived L0 face generation only.

| Generation input | Responsibility | Must not define |
|---|---|---|
| `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` (SHA-256 `1c6ad34c3f51c2d9fae4d69630d54fa50f6629cd9def55e0caca2a8234193e91`) | Face identity/feature geometry for the tiny edge sliver | hair, makeup, source light/background, body, clothing, skin retouch/color, camera design |
| `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png` (SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd`) | Natural warm-neutral skin context only | fine geometry, hair, makeup, body, clothing, lighting design, background |
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` (SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`) | Neck-below proportions, limb and full-body scale only | face, hair, identity, skin, outfit, hosiery material, footwear, scene, lighting |
| `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png` (SHA-256 `216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63`) | Brown blazer, ivory knit, pleated skirt construction/colors only | face, hair, body, skin, hosiery material, shoes, identity, pose, environment |
| `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png` (SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910`) | White matte hosiery textile and cream plush open-toe mule design; hosiery must remain continuous over all toes under the opening | depicted face/likeness, hair, body proportions, skin, identity, pose, environment |

## Face-safe and shot routing

- `generation_inputs`: the five scoped references above. Generate the tiny visible face only from the two L0-derived face/skin crops using `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` (`characters/CHR_HUMAN_001_OWNER/canon/face/FACE_01_FRONT_NEUTRAL_METHOD.md`).
- `qa_comparison_only`: approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` at `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; never attach to ImageGen.
- Hair A only, text-specified because the face/hair area is minimal.
- No generated candidate, including CAND_12, is a generation input or authority for face, body, outfit, hosiery, footwear, lighting, or environment.
- Scene and lighting are text-only temporary design: generic forest park after dusk, whole frame dark, path and foliage dim, readable through restrained low-light ambient exposure, no bright path or artificially bright subject. Camera, stride and motion blur are text-only shot design.
