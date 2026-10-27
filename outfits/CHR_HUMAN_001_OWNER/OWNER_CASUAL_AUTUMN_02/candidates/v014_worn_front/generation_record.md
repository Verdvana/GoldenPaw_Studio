# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v014

- character_id: `CHR_HUMAN_001_OWNER`
- asset_id: `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v014`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `worn_front`
- candidate_version: `v014`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- spec_revision: `draft_1.234`
- identity_md_revision: `draft_0.11`
- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`
- reference_set_ids: [`OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`]
- responsibility: full-body front appearance; L0-generated owner face and Hairstyle A; face-excluded registered body; preserve previously approved outfit fit, color, materials and construction
- reference_budget: `5 generation inputs; approved face/hair/body Canons are QA-only`
- aspect_ratio: `3:4 portrait`
- requested_resolution: `1536x2048 or nearest native 3:4`
- seed_settings: `ImageGen does not expose seed or sampler settings`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v014_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v014.png`
- generated_at: `2026-10-27`
- output_sha256: `7fcaacbf2afd4b623a336e725939d5fe46a295153b16aaf55211f9ec74c52896`
- qa_status: `PASS_INITIAL_VISUAL_QA; USER_REVIEW_REQUIRED`

## Generation inputs and scoped responsibilities

1. `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — L0 geometry crop; face shape and facial feature relationships only.
2. `L0_OWNER_012` — source `14.jpg`; frontal identity/expression and natural skin context only.
3. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — masked L0 `DSC00847` derivative; Hairstyle A pixels/construction only.
4. `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — deterministic neck-below body derivative; proportions and natural limb volume only.
5. `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` — approved worn-front image; outfit appearance, garment fit/drape, hosiery and slipper design only. It must not define face, likeness, skin, body proportions, hair, or identity lineage. Face/body/hair regions are strictly excluded from interpretation.

## QA comparison only (never generation inputs)

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`: face identity, relationships, projection and contamination comparison only.
- `OWNER_HAIR_A_01_FRONT_CANON_001`: approved Hairstyle A comparison only.
- `OWNER_BODY_01_FRONT_CANON_007`: approved full-body front comparison for likeness and body proportions only.

## Prompt assembly

See `PROMPT_ASSEMBLY.md`. This is a new independent L2 candidate. v013 is not an image input and is retained as rejected provenance only.
