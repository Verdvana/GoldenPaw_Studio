# Reference Plan — SOC_OUTFIT_002_IMG_03_CAND_18

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_03`
- candidate_id: `SOC_OUTFIT_002_IMG_03_CAND_18`
- asset_level: L3
- status: `READY_FOR_GENERATION`; after generation `REVIEW_REQUIRED`
- user authorization: User's 2026-10-18 instruction: playful selfie against forest-park café glass door, phone covers face. This revision uses fully closed plush slippers after CAND_17 exposed toe shapes.
- reference_count: 2; tool maximum 5
- face_visible: no; phone fully obscures face.

| Generation input | Responsibility | Must not define |
|---|---|---|
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` (SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`) | Neck-below body proportions and natural limb scale only | face, hair, identity, skin, outfit, hosiery material, footwear, pose, environment, lighting |
| `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png` (SHA-256 `216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63`) | Dark-brown blazer, ivory knit, pleated skirt construction and color only | face, hair, body, skin, hosiery, footwear, identity, pose, environment |

## Routing and exclusions

- `generation_inputs`: the two references above; hosiery and fully closed slippers are specified in text. The outfit design reference is scoped to blazer, knit and skirt only; exclude any hosiery/footwear appearance from it.
- `qa_comparison_only`: none; phone fully blocks the face, so no face pixels are generated or available for comparison. No AI Face Canon is a generation input.
- Hair A only, text-specified if visible.
- CAND_17 and all other generated candidates are excluded as inputs.
- Temporary scene: generic forest-park café glass entrance at dusk, with a physically plausible single reflection and soft warm light inside; no recurring location canon.
