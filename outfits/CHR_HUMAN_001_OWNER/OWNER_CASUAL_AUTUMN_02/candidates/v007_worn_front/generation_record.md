# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v007

- asset_id: `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v007`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `worn_front`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v007`
- status: `REJECTED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-10-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v007_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v007.png`
- output_sha256: `6bfa8b2e43a61008d3cf10929f532d7285e93ef961147fe9b7e4973d4670cc8b`
- reference_set_ids: [`OWNER_L0_FACE_FRONT_NEUTRAL`, `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE`, `HOS_15D_WHITE_SOFT_SHEEN_FRONT`]
- reference_budget: `5 generation inputs; 2 QA-only comparisons`
- aspect_ratio: `3:4 portrait`
- seed_settings: `ImageGen does not expose seed or sampler settings`

## Validation target

Independent full-body front fit validation for approved v005 outfit with visible continuous pale sheer hosiery and covered toes. v005/v006 worn candidates are failed outputs and are not generation inputs or continuity references.

## Generation inputs

Use one neutral front L0 face source plus the scoped hair, body, outfit and hosiery references:

```yaml
- asset_id: L0_OWNER_012
  path: characters/CHR_HUMAN_001_OWNER/source/identity/raw/14.jpg
  sha256: f7a83644f202ebec95134c6d115397b9f52f12e79b5fb227a6b79182026bd788
  responsibility: natural frontal L0 face identity and skin context only, under the applicable Face method constraints
  must_not_define: [source hair, clothing, body, pose, camera, lighting, background]
- asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
  path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
  responsibility: Hairstyle A only
  must_not_define: [face, identity, skin, body, clothing, lighting, background, mask]
- asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
  path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
  responsibility: neck-below body geometry and stance only
  must_not_define: [face, hair, clothing, hosiery material, lighting, background]
- asset_id: OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v005
  path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png
  responsibility: approved clothing design only
  must_not_define: [face, body, proportions, skin, hair, identity, pose, lighting, background]
- asset_id: L0_HOS_15_WSS_002
  path: materials/hosiery/source_library/raw/15d_white_soft_sheen/IMG_2604.jpg
  responsibility: pale white 15D hosiery color, translucency, textile boundary and continuous leg-to-foot coverage only
  must_not_define: [person, face, body proportions, skin pigmentation, pose, clothing, shoes, background, lighting]
```

The hosiery source is a material-only input. Generation inputs remain separate from QA comparison references. No AI Face/Body Canon, prior candidate, or previous shot is used as a generation input.

## QA comparison only

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — identity, facial-feature relationships, face contamination, projection and framing only.
- `OWNER_BODY_01_FRONT_CANON_007` — front body proportions and stance only.

## Reference isolation

- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` with registered frontal L0 source `L0_OWNER_012`
- hairstyle: `HAIRSTYLE_A`
- body_reference_is_face_excluded_derivative: `true`
- hosiery_material_source_is_material_only: `true`
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- prompt assembly: `PROMPT_ASSEMBLY.md`

## QA

- technical_status: `PASS` (1086x1448, exact 3:4, full head and feet visible)
- fit_validation_status: `FAIL` (hosiery reads as absent/too faint)
- face_contamination_check: `REVIEW_REQUIRED` (comparison-only identity check pending)
- face_generation_method_followed: `true`
- hosiery_continuity_and_material_check: `FAIL` (legs appear bare; toes appear uncovered)
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- outfit_fidelity_check: `PASS`
- hairstyle_check: `PASS` (Hairstyle A)
- decision: `REJECTED — visible hosiery/covered-toe requirement not met`
- reviewer: `Codex visual QA`
- reviewed_at: `2026-10-17`
