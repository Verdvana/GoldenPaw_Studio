# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v013

- character_id: `CHR_HUMAN_001_OWNER`
- asset_id: `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v013`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `worn_front`
- candidate_version: `v013`
- status: `REJECTED_FOR_REVISION`
- generation_tool: `built-in ImageGen`
- spec_revision: `draft_1.234`
- identity_md_revision: `draft_0.11`
- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`
- reference_set_ids: [`OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`]
- responsibility: full-body front worn presentation; outfit design/fit, generated owner face from L0 source method, Hairstyle A, registered neck-below proportions, neutral studio framing
- must_not_define: [Canon promotion, any new identity facts, change to approved outfit construction, body reshaping, skin contamination]
- reference_budget: `5 generation inputs; approved face/hair/body Canons are QA-only`
- aspect_ratio: `3:4 portrait`
- requested_resolution: `1536x2048 or nearest native 3:4`
- seed_settings: `ImageGen does not expose seed or sampler settings`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v013_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v013.png`
- generated_at: `2026-10-27`
- output_sha256: `6279b2256d38e74e9c59e275ae146942385c36d95197b410436df486706d7365`
- qa_status: `REJECTED_FOR_REVISION`

## Generation inputs

1. `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png`; L0-derived face geometry and identity only; excludes hair, makeup, body, clothing, lighting, background.
2. `L0_OWNER_012` — `characters/CHR_HUMAN_001_OWNER/source/identity/raw/14.jpg`; natural frontal expression and skin context only; excludes close-camera distortion, hair styling, body, pose, clothing, lighting, background.
3. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`; Hairstyle A hair pixels/construction only; mask conveys no appearance and must not define face/identity/body/clothing/light/background.
4. `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`; neck-below body proportions and natural volume only; excludes face, hair, skin identity, clothing, hosiery, footwear, pose alignment, light/background.
5. `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png`; garment design, colors, construction only; excludes person, face, hair, body, skin and identity.

## QA comparison only (never generation inputs)

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`: face identity, relationships, projection and contamination comparison only.
- `OWNER_HAIR_A_01_FRONT_CANON_001`: approved Hairstyle A attributes comparison only.
- `OWNER_BODY_01_FRONT_CANON_007`: approved full-body front appearance/proportions comparison only. It cannot be supplied to generation.

## Prompt assembly

One independent L2 image generated in parallel from the scoped sources above. No previous candidate or worn-front image supplies identity, face, hair, or body. Outfit appearance is retained from the approved design reference and written design specification. Full assembled prompt will be saved in `PROMPT_ASSEMBLY.md`.
