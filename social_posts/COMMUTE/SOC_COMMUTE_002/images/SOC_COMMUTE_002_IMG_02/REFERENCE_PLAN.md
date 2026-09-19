# Social Post Reference Plan

- post_id: SOC_COMMUTE_002
- image_asset_id: SOC_COMMUTE_002_IMG_02
- candidate_id: SOC_COMMUTE_002_IMG_02_CAND_01
- status: GENERATION_AUTHORIZED
- reference_count: 5
- budget_limit: 8
- budget_exception: none
- selected_reference_set_ids: [OWNER_L0_FACE_HIGH_RES_3Q, OWNER_HAIR_A_LEFT_3Q_CANON_L1]

| Priority | Reference ID/path | Level/status/version | Use | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|---|
| 1 | `L0_OWNER_013` — `characters/CHR_HUMAN_001_OWNER/source/identity/raw/15.jpg` | L0 immutable | generation_input | High-resolution 3/4 face structure | Hair, makeup, outfit, body, light, scene | Natural 3/4 walking glance |
| 2 | `L0_OWNER_014` — `characters/CHR_HUMAN_001_OWNER/source/identity/raw/16.jpg` | L0 immutable | generation_input | Supporting 3/4 facial relationships | Hair, makeup, outfit, body, light, scene | Face reconstruction support |
| 3 | `OWNER_HAIR_A_02_3Q_CANON_001` | L1 approved, scoped | generation_input | Hair-A 3/4 loose long hair only | Face, skin, body, outfit, light, scene | Matches walking angle |
| 4 | `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7` | deterministic L0-derived | generation_input | Adult full-body proportion and stride anatomy | Face, skin, hair, outfit, scene | Full-body walking read |
| 5 | `OWNER_WORK_SUMMER_01_WORN_FULL_BODY` | approved outfit | generation_input | Workwear, smoke-gray 15D matte hosiery and taupe pumps | Face, skin, body identity, hair, environment | Shared workday wardrobe |
| 6 | `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` | L1 approved | qa_comparison_only | Identity-drift and contamination comparison | Any generation authority | Required face QA only |

## Face-safe declaration

- face visible: yes
- applicable source-derived Face method: L0 3/4 reconstruction from `OWNER_L0_FACE_HIGH_RES_3Q`; prompt locks natural L0 facial relationships without importing makeup or studio retouching.
- L0 or deterministic L0-derived face inputs: `L0_OWNER_013`, `L0_OWNER_014`.
- approved AI Face Canon QA comparison only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`.
- face-excluded body derivative and checksum: `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7`; `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`.

## Conflict resolution

Scoped asset responsibility wins. No previous generated image may define this independent still.

## Excluded references

- `SOC_COMMUTE_001` images: L3-only, prohibited as visual inputs.
- AI Face and Body Canon images: prohibited as generation input under the face-safe rule.
