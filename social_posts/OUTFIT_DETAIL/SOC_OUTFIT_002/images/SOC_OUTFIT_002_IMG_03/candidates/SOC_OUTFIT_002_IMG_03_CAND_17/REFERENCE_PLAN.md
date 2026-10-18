# Reference Plan — SOC_OUTFIT_002_IMG_03_CAND_17

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_03`
- candidate_id: `SOC_OUTFIT_002_IMG_03_CAND_17`
- asset_level: L3
- status: `READY_FOR_GENERATION`; after generation `REVIEW_REQUIRED`
- user authorization: User's 2026-10-18 instruction changed IMG_03 to a playful reflection selfie in front of a forest-park café glass door, with phone covering the face.
- reference_count: 3; tool maximum 5
- face_visible: no; phone fully obscures face.

| Generation input | Responsibility | Must not define |
|---|---|---|
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` (SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`) | Neck-below body proportions and natural limb scale only | face, hair, identity, skin, outfit, hosiery material, pose, environment, lighting |
| `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png` (SHA-256 `216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63`) | Brown blazer, ivory knit, pleated skirt construction and colors only | face, hair, body, skin, hosiery, footwear, identity, pose, environment |
| `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png` (SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910`) | Soft-white matte hosiery textile/continuity only | depicted face/likeness, hair, body proportions, skin, identity, pose, footwear, environment |

## Routing and exclusions

- `generation_inputs`: the three references above.
- `qa_comparison_only`: `none`; the phone fully obscures the face, so no face pixels are generated or available for comparison. Never use an AI Face Canon as a generation input.
- Hair A only, text-specified if visible.
- No previous generated candidate is a generation input or authority.
- Café, reflective glass door, phone, warm interior glow, dusk exterior and playful pose are temporary L2 scene details specified in text only.
