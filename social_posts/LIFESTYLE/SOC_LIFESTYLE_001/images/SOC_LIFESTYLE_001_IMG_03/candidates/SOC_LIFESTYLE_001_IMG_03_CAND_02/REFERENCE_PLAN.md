# Social Post Reference Plan — SOC_LIFESTYLE_001_IMG_03_CAND_02

- post_id: SOC_LIFESTYLE_001
- image_asset_id: SOC_LIFESTYLE_001_IMG_03
- candidate_id: SOC_LIFESTYLE_001_IMG_03_CAND_02
- status: DRAFT
- reference_count: 2
- budget_limit: 8
- budget_exception: none
- selected_reference_set_ids: [OWNER_BODY_FRONT_CURRENT_FACE_EXCLUDED_DERIVATIVE, OWNER_HOS_15D_NUDE_MATTE_MATERIAL_CROP_001]

| Priority | Reference ID/path | Level/status/version | `generation_input` or `qa_comparison_only` | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|---|
| 1 | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` | approved-scoped deterministic derivative | generation_input | neck-below body, leg and foot proportions only | face, hair, outfit, hosiery material, pose, background | legs/feet are the sole subject |
| 2 | `materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png` | L0-derived material crop | generation_input | continuous light-skin 15D matte/velvet sheer hosiery | identity, skin pigmentation, body/foot anatomy, clothing, pose, background | hosiery is central |

## Face-safe declaration

- face visible: no
- applicable source-derived Face method: not applicable; face is outside the frame
- L0 or deterministic L0-derived face inputs: none
- approved AI Face Canon QA comparison only: none; face is not visible
- face-excluded body derivative and checksum: `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7`; its face-exclusion provenance/metadata remains authoritative

## Conflict resolution

Earlier post images contribute text-only continuity: same outfit, bouquet and flower-shop sidewalk. Their pixels are excluded. `SOC_LIFESTYLE_001_IMG_03_CAND_01` was rejected for composition and is not a reference.

## Excluded references

All previous AI images and candidates excluded. No face or hair source is needed because those attributes are outside this crop.
