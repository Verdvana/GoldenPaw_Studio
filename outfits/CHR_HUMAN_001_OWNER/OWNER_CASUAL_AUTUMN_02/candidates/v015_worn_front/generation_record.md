# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v015

- character_id: `CHR_HUMAN_001_OWNER`
- asset_id: `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v015`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `worn_front`
- candidate_version: `v015`
- status: `APPROVED`
- generation_tool: `built-in ImageGen`
- generation_method: `OWNER_BODY_01_FRONT_METHOD_V2 source/reference recipe adapted for approved L2 outfit`
- user_authorization: `2026-10-27 user explicitly directed to follow the generation method used for approved front-appearance assets after rejecting the prior L0 face-recovery attempts`
- reference_set_ids: [`OWNER_FACE_APPEARANCE_L1_CONTEXT_NO_CROWN_DERIVATIVE`, `OWNER_L0_BODY_FRONT_CONTEXT`, `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`]
- responsibility: approved front-face appearance and skin target; L0 body context; L0 Hairstyle A; approved Autumn 02 garment presentation
- reference_budget: `5 generation inputs; no prior worn candidate or full-body AI Canon is an input`
- aspect_ratio: `3:4 portrait`
- requested_resolution: `native exact 3:4; preferred 1536x2048`
- seed_settings: `ImageGen does not expose seed or sampler settings`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v015.png` (current authoritative path)
- original_candidate_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v015_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v015.png` (moved on approval)
- generated_at: `2026-10-27`
- output_sha256: `aec0eccdc38bcbe2b2dea8fae3e5988c98b461b76764cdffa2b46b560fb4cc09`
- qa_status: `PASS_USER_APPROVED`

## Generation inputs

1. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png`; exact approved front-face appearance and natural skin tone only; exclude Hairstyle B, camera angle, crown, makeup, body, outfit, lighting, background and rendering artifacts. This follows the specific face-reference role in approved `BODY_01_FRONT_v025` generation recipe, as directed by the user for this attempt.
2. `L0_OWNER_002` — `characters/CHR_HUMAN_001_OWNER/source/identity/raw/3.jpg`; real stature, torso, waist/hip placement, limb length and stance context only; exclude face, hair, clothes, shoes and background.
3. `L0_OWNER_003` — `characters/CHR_HUMAN_001_OWNER/source/identity/raw/4.jpg`; real torso, waist, hip, thigh, calf and limb-volume cross-check only; exclude face, hair, styling, clothes and environment.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`; Hairstyle A only; mask defines nothing; exclude face, identity, body, skin, clothing, lighting and background.
5. `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png`; garment appearance/construction/colors only; no person, face, hair, body, skin or identity cues.

## QA comparison only (never generation inputs)

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`: post-generation face feature/identity/contamination check only.
- `OWNER_BODY_01_FRONT_CANON_007`: post-generation full-body frontal appearance and proportions comparison only.
- `OWNER_HAIR_A_01_FRONT_CANON_001`: post-generation Hairstyle A check only.

## User approval and promotion

- approval_status: `APPROVED`
- approved_by: `user`
- approval_date: `2026-10-27`
- approval_evidence: `批准V15,这个长相是对的，丝袜，脚趾处袜面，衣着也合格`
- approved_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v015.png`
- approved_sha256: `aec0eccdc38bcbe2b2dea8fae3e5988c98b461b76764cdffa2b46b560fb4cc09`
- promotion_operation: `MOVED`; candidate raster moved unchanged; no duplicate raster retained
