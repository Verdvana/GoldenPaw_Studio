# Social Post Reference Plan

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_01`
- candidate_id: `SOC_OUTFIT_002_IMG_01_CAND_01`
- status: READY_FOR_GENERATION
- reference_count: 2
- budget_limit: 8
- selected_reference_set_ids: [OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE, OWNER_CASUAL_AUTUMN_02_WORN_FRONT_APPROVED_V012]

| Priority | Reference ID/path | Level/status/version | Use | Responsibility | Must not define |
|---:|---|---|---|---|---|
| 1 | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` / `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` / SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | approved deterministic face-excluded derivative | generation_input | neck-below proportion/leg geometry only | face, hair, identity, clothing, hosiery material, lighting, background |
| 2 | `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png` / `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` / SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910` | approved L2 worn-front ref | generation_input | Autumn 02 garment appearance/fit and medium-thick matte white continuous hosiery only | depicted face/likeness/expression/identity, hair, body proportions, skin, identity lineage |

## Face-safe declaration

- face visible: no; crop is from skirt/waist to hosiery-covered feet
- source-derived Face method: not needed; no face rendered
- face-excluded body derivative and checksum: `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1`, `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`
- approved Face Canon: not attached; not needed

## Shot-specific wardrobe choice

No shoes per user direction; the soft-white matte pantyhose continues over the visible feet and toes. This is an L3 styling choice, not a change to the L2 outfit Canon.

## Exclusions

No previous post image, face/hair input, private-location reference, or unapproved image is used. Picnic blanket and food are text-only temporary assets.
