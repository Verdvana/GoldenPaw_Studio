# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v009

- character_id: `CHR_HUMAN_001_OWNER`
- asset_id: `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v009`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `worn_front`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v009`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-10-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v009_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v009.png`
- output_sha256: `70a107e434c050f0ccd5b543dd1b519a4f39a97bd199d02500239ad0b515a201`
- reference_set_ids: [`OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE`, `HOS_USER_SELECTED_SHEER_PALE_AND_PLUSH_MULES`]
- reference_budget: `5 generation inputs; 2 QA-only comparisons`
- aspect_ratio: `3:4 portrait`
- seed_settings: `ImageGen does not expose seed or sampler settings`

## User corrections addressed

- Face must match registered owner appearance: use high-resolution L0-derived face-geometry crop; after generation compare to approved Face Canon for QA only.
- Hairstyle A must match its registered source: use the masked L0 DSC00847 derivative and specify long, straight, loose hair with no tie-back.
- Leg stance must not look O-shaped: retain the face-excluded body reference for proportions but pose feet parallel and together, knees and calves naturally close/touching; do not alter body proportions.
- Use uploaded Photo 2 directly for hosiery material and fuzzy slipper upper appearance only.
- Slipper sole thickness: user-directed approximately 5 cm; Photo 2 and approved v005 raster do not define sole thickness.

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png
    sha256: 1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91
    responsibility: L0-derived face geometry and recognizable identity only, projected to a neutral front view under FACE_01 method constraints
    must_not_define: [hair, makeup, skin color/retouch, body, clothing, lighting, background]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    sha256: 6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd
    responsibility: L0 Hairstyle A hair pixels and construction only
    must_not_define: [face, identity, body, clothing, lighting, background, gray mask]
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b
    responsibility: neck-below body proportions and leg volume only
    must_not_define: [face, hair, clothing, hosiery material, footwear, leg stance, lighting, background]
  - asset_id: OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v005
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png
    sha256: 216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63
    responsibility: blazer/knit/skirt design and slipper upper/color only
    must_not_define: face, body, proportions, skin, hair, pose, hosiery anatomy, sole thickness, lighting, background
  - asset_id: L0_HOS_USER_001
    path: materials/hosiery/source_library/raw/user_selected_sheer_pale/PHOTO_2.jpg
    sha256: e86602ca169ba9677ac314353481022fcf8ba636068970898b4e067acecb6083
    responsibility: user-selected pale sheer hosiery appearance, subtle transparency and textile presence; plush open-toe mule upper and toe-opening interaction
    must_not_define: person, face, skin pigmentation, leg/foot anatomy, pose, body proportions, background, watermark, or 5 cm sole thickness
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope: [identity drift, facial relationships, face contamination, projection, framing]
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    comparison_scope: [registered body proportions, leg volume and alignment only]
```

## Reference isolation

- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` prompt constraints + L0-derived geometry crop
- hairstyle: `HAIRSTYLE_A`
- body_reference_is_face_excluded_derivative: `true`
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- hosiery_reference_is_user_L0_material_only: `true`
- qa_comparison_only is never supplied to ImageGen
- prompt assembly: `PROMPT_ASSEMBLY.md`

## QA

- technical_status: `PASS` (1086x1448, exact 3:4, full head and both feet visible)
- fit_validation_status: `UNREVIEWED`
- face_contamination_check: `REVIEW_REQUIRED` (no obvious blotches; face brightness/eye styling may still drift from the approved comparison Canon)
- face_generation_method_followed: `true`
- hairstyle_A_check: `PASS` (long loose dark-brown hair, near-center part, no tie-back)
- leg_alignment_check: `PASS` (feet together, legs close, no O-shaped bowing)
- hosiery_continuity_and_material_check: `REVIEW_REQUIRED` (pale sheer appearance follows uploaded Photo 2; user to confirm textile/toe coverage)
- slipper_sole_thickness_check: `PASS` (visible platform approximately 5 cm)
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `REVIEW_REQUIRED`
- reviewer: `Codex visual review; final user review pending`
- reviewed_at: `2026-10-17`
