# Social Post Reference Plan — SOC_LIFESTYLE_001_IMG_01_CAND_01

- post_id: SOC_LIFESTYLE_001
- image_asset_id: SOC_LIFESTYLE_001_IMG_01
- candidate_id: SOC_LIFESTYLE_001_IMG_01_CAND_01
- status: DRAFT
- reference_count: 4
- budget_limit: 8
- budget_exception: none
- selected_reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1, OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE, OWNER_BODY_FRONT_CURRENT_FACE_EXCLUDED_DERIVATIVE, OWNER_HOS_15D_NUDE_MATTE_MATERIAL_CROP_001]

| Priority | Reference ID/path | Level/status/version | `generation_input` or `qa_comparison_only` | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|---|
| 1 | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png` | deterministic L0-derived crop | generation_input | source-derived face geometry and natural skin context | hair, camera, outfit, environment, lighting design | face-safe rule |
| 2 | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png` | deterministic masked L0 derivative | generation_input | HAIRSTYLE_A only | face, skin, body, clothes, background | visible hair |
| 3 | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` | approved-scoped deterministic derivative | generation_input | neck-below body/limb proportions only | face, hair, clothes, hosiery, environment | body visible |
| 4 | `materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png` | L0-derived material crop | generation_input | light-skin 15D matte/velvet sheer textile | identity, skin pigmentation, body anatomy, outfit, pose, background | hosiery visible |
| 5 | `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg` | approved L1 Canon | qa_comparison_only | post-generation identity/feature and face contamination comparison | all generation attributes | required QA only; never generation input |

## Face-safe declaration

- face visible: yes
- applicable source-derived Face method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`, applied as a downstream source-derived face generation method
- L0 or deterministic L0-derived face inputs: `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001`
- approved AI Face Canon QA comparison only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
- face-excluded body derivative and checksum: `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7`; see source metadata/provenance record

## Conflict resolution

The scoped responsibilities above take precedence. Prior AI images are not generation inputs. This single-frame selfie is generated directly from source/master responsibilities.

## Excluded references

All prior social images and generated candidates excluded to prevent identity lineage and reduce redundancy. Full face/body Canon rasters excluded from generation.
