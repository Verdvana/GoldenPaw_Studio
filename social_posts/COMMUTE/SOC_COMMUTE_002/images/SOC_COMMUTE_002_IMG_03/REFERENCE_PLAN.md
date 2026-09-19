# Social Post Reference Plan

- post_id: SOC_COMMUTE_002
- image_asset_id: SOC_COMMUTE_002_IMG_03
- candidate_id: SOC_COMMUTE_002_IMG_03_CAND_01
- status: GENERATION_AUTHORIZED
- reference_count: 3
- budget_limit: 8
- budget_exception: none
- selected_reference_set_ids: [OWNER_HAIR_A_BACK_CANON_L1]

| Priority | Reference ID/path | Level/status/version | Use | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|---|
| 1 | `OWNER_HAIR_A_04_BACK_CANON_001` | L1 approved, scoped | generation_input | Hair-A rear silhouette, length and tapered ends only | Face, skin, body, outfit, light, scene | Back-facing commuter view |
| 2 | `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7` | deterministic L0-derived | generation_input | Neck-below adult body proportion and walking anatomy | Face, skin, hair, outfit, scene | Perspective-consistent full figure |
| 3 | `OWNER_WORK_SUMMER_01_WORN_FULL_BODY` | approved outfit | generation_input | Workwear, smoke-gray 15D matte hosiery and taupe pumps | Face, skin, body identity, hair, environment | Shared workday wardrobe |

## Face-safe declaration

- face visible: no; do not show a face, reflection, selfie screen or readable portrait.
- applicable source-derived Face method: not applicable.
- L0 or deterministic L0-derived face inputs: none.
- approved AI Face Canon QA comparison only: not applicable.
- face-excluded body derivative and checksum: `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7`; `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`.

## Conflict resolution

Only declared L2 temporary dressing may define the generic station entrance. No prior social post image is used.

## Excluded references

- all L0 face materials and AI Face Canon: no face is visible.
- `SOC_COMMUTE_001` images: L3-only, prohibited as visual inputs.
