# Social Post Reference Plan

- post_id: SOC_YOGA_001
- image_asset_id: SOC_YOGA_001_IMG_01
- candidate_id: SOC_YOGA_001_IMG_01_CAND_01
- status: GENERATION_AUTHORIZED
- reference_count: 3
- budget_limit: 8
- selected_reference_set_ids: [OWNER_HAIR_A_FRONT_CANON_L1]

| Priority | Reference ID/path | Level/status | Use | Responsibility | Must not define |
|---:|---|---|---|---|---|
| 1 | `OWNER_HAIR_A_01_FRONT_CANON_001` | L1 approved, scoped | generation_input | Hair-A only | Face, skin, body, outfit, light, scene |
| 2 | `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7` | deterministic L0-derived | generation_input | Neck-below adult proportion and standing anatomy | Face, skin, hair, outfit, scene |
| 3 | `OWNER_SPORT_YOGA_01_WORN_FRONT` | L2 approved | generation_input | Yoga outfit and light-skin-tone 15D matte hosiery, no footwear | Face, body identity, hair, temporary hoodie/shoes, environment |

## Face-safe declaration

- face visible: no; phone completely covers the face and no reflective face is allowed.
- applicable source-derived Face method: not applicable.
- L0 or deterministic L0-derived face inputs: none.
- approved AI Face Canon QA comparison only: none.
- face-excluded body derivative and checksum: `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7`; `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`.
