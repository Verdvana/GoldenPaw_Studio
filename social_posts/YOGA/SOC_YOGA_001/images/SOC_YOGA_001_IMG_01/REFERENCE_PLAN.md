# Social Post Reference Plan

- post_id: SOC_YOGA_001
- image_asset_id: SOC_YOGA_001_IMG_01
- candidate_id: SOC_YOGA_001_IMG_01_CAND_13
- status: APPROVED_L3
- reference_count: 5
- budget_limit: 8
- selected_reference_set_ids: [OWNER_L0_FACE_HIGH_CAMERA, OWNER_HAIR_A_FRONT_CANON_L1, OWNER_BODY_FRONT_CURRENT_FACE_EXCLUDED_DERIVATIVE]

| Priority | Reference ID/path | Level/status | Use | Responsibility | Must not define |
|---:|---|---|---|---|---|
| 1 | `L0_OWNER_012` | L0 immutable | generation_input | Small, incidental visible facial identity from a high camera angle | Body, hair, outfit, scene, pose |
| 2 | `L0_OWNER_010` | L0 immutable | generation_input | Small, incidental visible facial identity from a high camera angle | Body, hair, outfit, scene, pose |
| 3 | `OWNER_HAIR_A_01_FRONT_CANON_001` | L1 approved, scoped | generation_input | Hair-A only | Face, skin, body, outfit, light, scene |
| 4 | `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7` | deterministic L0-derived | generation_input | Neck-below adult proportion and standing anatomy | Face, skin, hair, outfit, scene |
| 5 | `OWNER_SPORT_YOGA_01_WORN_FRONT` | L2 approved | generation_input | Coral yoga leggings and light-skin-tone 15D matte hosiery only | Face, body identity, hair, approved top design, temporary lilac top/hoodie/shoes, environment |

## Face-safe declaration

- face visible: yes; only a small, incidental partial face is permitted at the upper image edge.
- applicable source-derived Face method: `OWNER_L0_FACE_HIGH_CAMERA`; high-angle L0 sources only.
- L0 or deterministic L0-derived face inputs: `L0_OWNER_012`, `L0_OWNER_010`.
- approved AI Face Canon QA comparison only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`; never a generation input.
- face-excluded body derivative and checksum: `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7`; `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`.
