# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v005

- character_id: `CHR_HUMAN_001_OWNER`
- asset_id: `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v005`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `worn_front`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v005`
- status: `REJECTED`
- approval_status: `REJECTED_BY_QA`
- gate: `L2 outfit front fit-validation after approved design v005`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-10-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v005_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v005.png`
- output_sha256: `ee9b14608801a3a0f871195a77f126d5296e98760ebe2d0eceb82748311f04d5`
- reference_set_ids: [`OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1`, `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE`]
- reference_budget: `5 generation inputs; 3 QA comparison only`
- aspect_ratio: `3:4 portrait`
- seed_settings: `ImageGen does not expose seed or sampler settings`

## Validation target

Does the newly approved dark-brown blazer, ivory ribbed turtleneck, pleated mini skirt, pale sheer hosiery and cream plush open-toe slippers fit naturally on the registered owner appearance and body proportions, with Hairstyle A?

Acceptance checks:

- Face generated only from the listed L0-derived face and skin references under `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`; no AI face/body Canon or generated candidate is a generation input.
- Hairstyle A only, following the face-masked DSC00847 derivative; no Hairstyle B or hybrid.
- Body derivative is face-excluded and defines neck-below proportions/stance only.
- Outfit matches approved design v005; no item from superseded v004 outfit design.
- Hosiery is pale, sheer, matte textile and continuous through legs, heels, insteps and enclosed toes visible through open-toe slippers; no bare toes, gaps, latex/plastic/rubber appearance.
- Full head and both slippers visible; directly front-facing neutral stance with both feet supported; exact 3:4; no text, logo, watermark, props or extra anatomy.
- Post-generation face-contamination review against approved Face Canon is comparison-only.

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png
    sha256: 1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91
    responsibility: L0-derived recognizable face geometry and identity only
    must_not_define: [source hair, makeup, skin retouch, body, camera, lighting, clothing, background]
  - asset_id: OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png
    sha256: 89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd
    responsibility: natural L0 skin tone and texture context only
    must_not_define: [fine face geometry, hair, makeup, body, clothing, camera, lighting, background]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    sha256: 6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd
    responsibility: L0 Hairstyle A pixels and construction only
    must_not_define: [face, identity, skin, body, clothing, lighting, background, gray mask]
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b
    responsibility: face-excluded neck-below front body proportions, stance and foot scale only
    must_not_define: [face, identity, hair, clothing, hosiery material, lighting, background]
  - asset_id: OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v005
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png
    sha256: 216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63
    responsibility: approved v005 outfit garments, palette, layering and slipper design only
    must_not_define: [face, body, proportions, skin, hair, identity, pose, hosiery anatomy, lighting, background]
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope: [identity drift, feature relationships, skin contamination, projection, framing]
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    comparison_scope: [front body proportion and stance]
  - asset_id: L0_HOS_15_WSS_002
    path: materials/hosiery/source_library/raw/15d_white_soft_sheen/IMG_2604.jpg
    comparison_scope: [pale hosiery color, sheerness, continuous textile response]
```

## Reference isolation

- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` with source-derived L0 crops above
- hairstyle: `HAIRSTYLE_A`
- generation_inputs and qa_comparison_only are separate; no AI Face/Body Canon or previous candidate is an input
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- body_reference_is_face_excluded_derivative: `true`
- outfit_reference_used_for_identity_or_body: `false`
- generation prompt and responsibilities are detailed in `PROMPT_ASSEMBLY.md`

## QA

- technical_status: `PASS` (1086x1448, exact 3:4, full head and both feet visible)
- fit_validation_status: `FAIL` (hosiery not visibly defined as continuous textile)
- face_contamination_check: `REVIEW_REQUIRED` (comparison-only identity check pending)
- face_generation_method_followed: `true`
- hosiery_continuity_and_material_check: `FAIL` (legs read as bare; toes appear uncovered in open slippers)
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- outfit_fidelity_check: `PASS` (blazer, knit, pleated skirt, slippers match v005 design)
- hairstyle_check: `PASS` (Hairstyle A appearance)
- decision: `REJECTED — hosiery continuity/toe coverage failure`
- reviewer: `Codex visual QA`
- reviewed_at: `2026-10-17`
