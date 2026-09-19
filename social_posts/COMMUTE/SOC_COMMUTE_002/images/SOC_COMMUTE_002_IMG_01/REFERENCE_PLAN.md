# Social Post Reference Plan

- post_id: SOC_COMMUTE_002
- image_asset_id: SOC_COMMUTE_002_IMG_01
- candidate_id: SOC_COMMUTE_002_IMG_01_CAND_01
- status: GENERATION_AUTHORIZED
- reference_count: 5
- budget_limit: 8
- budget_exception: none
- selected_reference_set_ids: [OWNER_L0_FACE_FRONT_NEUTRAL, OWNER_HAIR_A_LEFT_3Q_CANON_L1]

| Priority | Reference ID/path | Level/status/version | Use | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|---|
| 1 | `L0_OWNER_012` — `characters/CHR_HUMAN_001_OWNER/source/identity/raw/14.jpg` | L0 immutable | generation_input | Neutral face identity and natural facial relationships | Hair, outfit, body, light, scene | Face-visible 3/4 view |
| 2 | `L0_OWNER_010` — `characters/CHR_HUMAN_001_OWNER/source/identity/raw/12.jpg` | L0 immutable | generation_input | Additional natural face projection | Hair, outfit, body, light, scene | Avoids a single-source face reconstruction |
| 3 | `OWNER_HAIR_A_02_3Q_CANON_001` | L1 approved, scoped | generation_input | Hair-A 3/4 loose long hair only | Face, skin, body, outfit, light, scene | Matches the camera angle |
| 4 | `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7` | deterministic L0-derived | generation_input | Neck-below adult body scale and proportions | Face, skin, hair, outfit, scene | Keeps body source separated from face |
| 5 | `OWNER_WORK_SUMMER_01_WORN_FULL_BODY` | approved outfit | generation_input | Workwear, smoke-gray 15D matte hosiery and taupe pumps | Face, skin, body identity, hair, environment | Shared workday wardrobe |
| 6 | `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` | L1 approved | qa_comparison_only | Identity-drift and contamination comparison | Any generation authority | Required face QA only |

## Face-safe declaration

- face visible: yes
- applicable source-derived Face method: L0 neutral-face reconstruction from `OWNER_L0_FACE_FRONT_NEUTRAL`; prompt locks smaller refined lower face and natural L0 facial relationships.
- L0 or deterministic L0-derived face inputs: `L0_OWNER_012`, `L0_OWNER_010`.
- approved AI Face Canon QA comparison only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`.
- face-excluded body derivative and checksum: `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7`; `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`.

## Conflict resolution

Scoped asset responsibility wins. No prior social image is supplied or permitted as a generation input.

## Excluded references

- `SOC_COMMUTE_001` images: published L3 continuity-only assets, prohibited as identity/body/wardrobe/scene inputs.
- AI Face and Body Canon images: prohibited as generation input under the face-safe rule.
