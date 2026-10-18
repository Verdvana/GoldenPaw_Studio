# Social Post Reference Plan

- post_id: `SOC_OUTFIT_001`
- image_asset_id: `SOC_OUTFIT_001_IMG_01`
- candidate_id: `SOC_OUTFIT_001_IMG_01_CAND_03`
- status: READY_FOR_GENERATION
- reference_count: 6
- budget_limit: 8
- budget_exception: none
- selected_reference_set_ids: [OWNER_L0_FACE_013_GEOMETRY_CROP_V1, OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE, OWNER_HAIR_A_FRONT_CANON_L1, OWNER_CASUAL_AUTUMN_02_WORN_FRONT_APPROVED_V012]

| Priority | Reference ID/path | Level/status/version | `generation_input` or `qa_comparison_only` | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|---|
| 1 | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` (`OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001`, SHA-256 `1c6ad34c3f51c2d9fae4d69630a54fa50f6629cd9def55e0caca2a8234193e91`) | deterministic L0-derived; approved derivative | generation_input | real-source facial geometry and recognizable identity only | source hair, makeup, jewelry, retouched skin color, camera, lighting, body, clothes, background | Source-derived face authority per owner rule |
| 2 | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png` (`OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001`, SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd`) | deterministic L0-derived; approved derivative | generation_input | natural warm-neutral skin color/texture context only | fine face geometry, hairstyle, makeup, camera, body, clothing, lighting design, background | Natural skin evidence paired with geometry; low-resolution limits retained |
| 3 | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` (`OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1`, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`) | deterministic face-excluded L1 derivative; approved | generation_input | neck-below proportions only | face, hair, skin identity, clothing design, hosiery material, lighting, background | Prevent body drift while excluding face |
| 4 | `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png` (`OWNER_HAIR_A_01_FRONT_CANON_001`, SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`) | approved L1 Hair A front | generation_input | Hair A shape, part, color and fall only | face generation/identity, skin, body, outfit, camera, light, background | Owner face-visible non-Hair-B assets use Hair A |
| 5 | `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png` (`OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012`, SHA-256 `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910`) | approved L2 outfit ref | generation_input | outfit fit/drape, blazer, knit top, skirt, white hosiery and plush mule design | depicted face/likeness/expression/identity, hair, body proportions, skin, identity lineage, keyframe identity | Approved current worn view; facial and hair regions strictly prohibited as references |
| 6 | `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg` (`OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`, SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`) | approved L1 Face Canon | qa_comparison_only | post-generation identity drift, geometry, skin contamination, projection/framing QA | all generation responsibilities | Required comparison only; never input to face generation |

## Face-safe declaration

- face visible: yes
- applicable source-derived Face method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` at `characters/CHR_HUMAN_001_OWNER/canon/face/FACE_01_FRONT_NEUTRAL_METHOD.md`; apply source-derived face rules, Hair A block and camera/projection constraints, adapted to a casual handheld selfie without importing the method's studio background or calibration clothing
- L0 or deterministic L0-derived face inputs: OWNER_013 geometry crop + OWNER_012 natural skin context crop above
- approved AI Face Canon QA comparison only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` above
- face-excluded body derivative and checksum: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1; `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`

## Conflict resolution

Scoped asset responsibility wins. The approved outfit worn-front image's face and hairstyle are fully excluded. Owner's source-derived face method overrides general Canon routing for face generation. Body reference is deterministically face-excluded. Reference reflections are environment-only and do not define the subject.

## Excluded references

- Full owner L0 photos: unnecessary; named deterministic source crops cover required face properties.
- AI Face and Body Canon images: face/body Canon pixels are not generation inputs under the global face-safe rule.
- Any prior social images or candidates: none needed; no AI-to-AI lineage.
- Café/location images: none; the temporary public environment is described in text and has no established location Canon.
