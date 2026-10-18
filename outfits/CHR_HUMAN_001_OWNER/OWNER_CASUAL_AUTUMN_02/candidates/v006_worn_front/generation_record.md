# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v006

- asset_id: `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v006`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `worn_front`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v006`
- status: `REJECTED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-10-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v006_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v006.png`
- output_sha256: `3ce63b9df743fdb2c9b69c18340e439ed4af7de230e968136e69ae169448af28`
- reference_set_ids: [`OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1`, `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE`]
- reference_budget: `5 generation inputs; 3 QA-only comparisons`
- aspect_ratio: `3:4 portrait`
- seed_settings: `ImageGen does not expose seed or sampler settings`

## Validation target

Create a corrected independent full-body front fit validation of the approved v005 outfit, with clear continuous pale sheer hosiery and covered toes. v005 worn candidate was rejected for absent/unclear hosiery. Its pixels are not an input.

## Generation inputs

Exactly the five references and role exclusions documented in `../v005_worn_front/generation_record.md`; no image from v005 or any previous generated candidate is used. The face-generation inputs remain L0-derived only, the body reference remains face-excluded, and the approved v005 outfit image defines clothing only.

## QA comparison only

After generation only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` for identity/feature drift and face contamination; `OWNER_BODY_01_FRONT_CANON_007` for proportions/stance; `L0_HOS_15_WSS_002` for pale hosiery color and textile coverage. None is supplied to ImageGen.

## Reference isolation

- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` with the same source-derived L0 crops as v005
- hairstyle: `HAIRSTYLE_A`
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- body_reference_is_face_excluded_derivative: `true`
- approved AI Face/Body Canon generation inputs: `none`
- generation prompt: `PROMPT_ASSEMBLY.md`

## QA

- technical_status: `PASS` (1086x1448, exact 3:4, full head and both feet visible)
- fit_validation_status: `FAIL` (hosiery not visibly defined as continuous textile)
- face_contamination_check: `REVIEW_REQUIRED`
- face_generation_method_followed: `true`
- hosiery_continuity_and_material_check: `FAIL` (legs read as bare; toes appear uncovered)
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- outfit_fidelity_check: `PASS`
- decision: `REJECTED — hosiery continuity/toe coverage failure`
- reviewer: `Codex visual QA`
- reviewed_at: `2026-10-17`
