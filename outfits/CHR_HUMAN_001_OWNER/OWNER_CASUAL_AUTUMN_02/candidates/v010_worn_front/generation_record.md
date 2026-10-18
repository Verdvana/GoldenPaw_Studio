# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v010

- character_id: `CHR_HUMAN_001_OWNER`
- asset_id: `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v010`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `worn_front`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v010`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-10-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v010_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v010.png`
- output_sha256: `345592b5cb475a21808e0524dcf126f52ded9f04ac11dc28a08c4d59286c2792`
- reference_set_ids: [`OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE`, `HOS_USER_SELECTED_SHEER_PALE_AND_PLUSH_MULES`]
- reference_budget: `5 generation inputs; 3 QA-only comparisons`
- aspect_ratio: `3:4 portrait`
- seed_settings: `ImageGen does not expose seed or sampler settings`

## User corrections

- Face: use source-derived L0 geometry under `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`; approved Face Canon is comparison-only. Do not beautify, reshape, enlarge eyes, slim face, or modify natural feature relationships.
- Hair: exact Hairstyle A from the L0 DSC00847 hair-only derivative; low close roots, controlled narrow crown, near-center part with the root-flow apex slightly image-left of center, long straight loose dark-brown lengths, slim face-framing panels, slight asymmetry, fine separated strands and tapered ends. Avoid symmetric curtain hair, waves, tucked-back ears, tied sections and excessive crown volume.
- Body: retain the accepted registered body proportions and leg volume from the face-excluded derivative. Feet together and parallel; legs straight, knees and calves close enough to touch naturally; no O-shaped bowing or gap caused by stance.
- Hosiery: medium-thick matte white continuous textile pantyhose, distinctly white and opaque over legs; visibly smooth textile tension over calves, ankles, insteps and covered toes. Only the toe tips may show slight skin tone through the fabric. No bare toe, open seam, plastic shine, latex, rubber, or body-paint effect.
- Slippers: cream plush open-toe mule upper guided by Photo 2, with a clearly visible but restrained approximately 3 cm sole. Photo 2 and the approved design-reference raster do not define thickness.

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png
    sha256: 1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91
    responsibility: L0-derived facial geometry and recognizable identity only, rendered in a neutral front projection under the FACE_01 method
    must_not_define: [hair, makeup, skin retouch, body, clothing, lighting, background]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    sha256: 6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd
    responsibility: L0 Hairstyle A hair pixels and construction only
    must_not_define: [face, identity, body, clothing, lighting, background, gray mask]
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b
    responsibility: neck-below stature, body proportions and natural limb volume only
    must_not_define: [face, hair, clothing, hosiery material, footwear, pose, leg alignment, lighting, background]
  - asset_id: OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v005
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png
    sha256: 216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63
    responsibility: blazer, knit top, pleated skirt design and cream plush slipper upper only
    must_not_define: face, body, proportions, skin, hair, pose, hosiery, sole thickness, lighting, background
  - asset_id: L0_HOS_USER_001
    path: materials/hosiery/source_library/raw/user_selected_sheer_pale/PHOTO_2.jpg
    sha256: e86602ca169ba9677ac314353481022fcf8ba636068970898b4e067acecb6083
    responsibility: plush mule upper/open-toe interaction and supporting hosiery textile reference; latest explicit user text defines white matte heavier opacity and toe-tip translucency
    must_not_define: person, face, skin pigmentation, anatomy, pose, proportions, background, watermark, sole thickness, or final hosiery color/opacity contrary to latest text
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    sha256: 4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4
    comparison_scope: [identity drift, natural feature relationships, face contamination, projection, framing]
  - asset_id: OWNER_HAIR_A_01_FRONT_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png
    sha256: 18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219
    comparison_scope: [approved front Hairstyle A attributes only]
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    sha256: 90e021fcf5c72416b2b3c6405cfe2abe2d43c28e49da6dbabc250f73da306978
    comparison_scope: [registered body proportions and leg volume only]
```

## Reference isolation

- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` prompt constraints + L0-derived face geometry crop
- hairstyle: `HAIRSTYLE_A`, L0 scoped hair derivative only
- body_reference_is_face_excluded_derivative: `true`
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- hosiery_reference_is_user_L0_material_only: `true`
- qa_comparison_only is never supplied to ImageGen
- prompt assembly: `PROMPT_ASSEMBLY.md`

## QA

- technical_status: `PASS` (1086x1448, exact 3:4, full head and both feet visible)
- fit_validation_status: `UNREVIEWED`
- face_contamination_check: `REVIEW_REQUIRED`
- face_generation_method_followed: `true`
- hairstyle_A_check: `REVIEW_REQUIRED` (long, straight, loose front hair appears close to A; compare user-facing result)
- leg_alignment_check: `FAIL` (medial calves and inner feet remain separated)
- hosiery_continuity_and_material_check: `REVIEW_REQUIRED` (matte white and covered toe tips rendered; detailed tension/toe show-through pending review)
- slipper_sole_thickness_check: `REVIEW_REQUIRED` (sole visible; exact 3 cm appearance needs review)
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `REVIEW_REQUIRED`
- reviewer: `Codex visual review; final user review pending`
- reviewed_at: `2026-10-17`
