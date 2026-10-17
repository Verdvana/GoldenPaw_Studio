# Social Post Reference Plan — SOC_LIFESTYLE_001_IMG_03_CAND_03

- post_id: SOC_LIFESTYLE_001
- image_asset_id: SOC_LIFESTYLE_001_IMG_03
- candidate_id: SOC_LIFESTYLE_001_IMG_03_CAND_03
- status: DRAFT
- reference_count: 2
- budget_limit: 8
- budget_exception: none
- selected_reference_set_ids: [OWNER_BODY_FRONT_CURRENT_FACE_EXCLUDED_DERIVATIVE, OWNER_HOS_15D_NUDE_MATTE_MATERIAL_CROP_001]

| Priority | Reference ID/path | Level/status/version | `generation_input` or `qa_comparison_only` | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|---|
| 1 | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` | approved-scoped deterministic derivative | generation_input | neck-below anatomy, natural leg proportions and alignment | face, hair, outfit, hosiery material, pose, background | correct straight lower-leg axes |
| 2 | `materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png` | L0-derived material crop | generation_input | continuous light-skin 15D matte/velvet hosiery | identity, anatomy, clothing, pose, background | hosiery appearance |

## Face-safe declaration

- face visible: no
- applicable source-derived Face method: not applicable
- L0 or deterministic L0-derived face inputs: none
- approved AI Face Canon QA comparison only: none
- face-excluded body derivative and checksum: `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7`; see derivative metadata/provenance

## Conflict resolution

Text-only continuity from the post defines outfit, afternoon, bouquet and public setting. Candidate 01 was rejected for composition and candidate 02 for leg alignment; neither is an input or downstream reference.

## Excluded references

All previous AI images excluded. No face/hair source is needed for this face-out-of-frame shot.
