# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012

- character_id: `CHR_HUMAN_001_OWNER`
- asset_id: `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `worn_front`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v012`
- status: `APPROVED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-10-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png` (current authoritative path)
- output_sha256: `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910`
- original_candidate_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v012_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png` (moved on approval)
- approved_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png`
- approved_sha256: `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910`
- reference_set_ids: [`OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_L0_FACE_FRONT_NEUTRAL`, `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `HOS_USER_SELECTED_SHEER_PALE_AND_PLUSH_MULES`]
- reference_budget: `5 generation inputs; 3 QA-only comparisons`
- aspect_ratio: `3:4 portrait`
- seed_settings: `ImageGen does not expose seed or sampler settings`

## User corrections

- Face: combine source-derived L0 geometry with natural frontal `L0_OWNER_012` (`14.jpg`) under `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`; the geometry crop defines fine structure and 14.jpg defines natural front identity/expression context only. Face Canon is comparison-only. Use a relaxed neutral expression with mouth closed and no smile. Do not beautify, reshape, enlarge eyes, slim face, or modify natural feature relationships.
- Hair: exact Hairstyle A from the L0 DSC00847 hair-only derivative; low close roots, controlled narrow crown, near-center part with the root-flow apex slightly image-left of center, long straight loose dark-brown lengths, slim face-framing panels, slight asymmetry, fine separated strands and tapered ends. Avoid symmetric curtain hair, waves, tucked-back ears, tied sections and excessive crown volume.
- Body: retain the accepted registered body proportions and leg volume from the face-excluded derivative. Feet together and parallel; inner thighs and knees meet, medial calves remain in contact from below the knees to lower calves, inner ankles and slipper edges touch; no O-shaped bowing or leg gap.
- Hosiery: medium-thick matte white continuous textile pantyhose, distinctly white and opaque over legs; visibly smooth textile tension over calves, ankles, insteps and covered toes. Only the toe tips may show slight skin tone through the fabric. No bare toe, open seam, plastic shine, latex, rubber, or body-paint effect.
- Slippers: cream plush open-toe mule upper guided by Photo 2, with a clearly visible but restrained approximately 3 cm sole. Photo 2 and the approved design-reference raster do not define thickness.
- Leg stance: candidate v010 missed the required contact. In this independent generation, medial thighs, knees, calves, inner ankles and inner edges of the slippers must meet or touch naturally; avoid the visible vertical gap between calves seen in v010. The v010 pixels are not an input.
- Garment design is specified in text because the five-reference limit is allocated to source face, hairstyle, body, and hosiery/footwear material.

## Approved future-reference scope

- allowed: outfit appearance/fit/drape, white matte pantyhose textile and coverage, toe-opening interaction, and plush mule design/sole only
- strictly forbidden: using this image, any crop from it, or features inferred from it to define the depicted person's face/likeness or hairstyle/hair attributes
- additional exclusions: body proportions, skin, identity lineage, and video keyframe identity
- approval evidence: user said `可以 批准，但是被参考时严禁参考此图的人物长相和发型`
- approval_record: `APPROVAL_RECORD.md`; official approval: `../../approved/worn_front/APPROVAL_v012.md`

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png
    sha256: 1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91
    responsibility: L0-derived facial geometry and recognizable identity only, rendered in a neutral front projection under the FACE_01 method
    must_not_define: [hair, makeup, skin retouch, body, clothing, lighting, background]
  - asset_id: L0_OWNER_012
    path: characters/CHR_HUMAN_001_OWNER/source/identity/raw/14.jpg
    sha256: f7a83644f202ebec95134c6d115397b9f52f12e79b5fb227a6b79182026bd788
    responsibility: natural frontal L0 face identity, neutral expression and skin context only; fine proportions remain subordinate to high-resolution geometry crop and FACE_01 method
    must_not_define: [hair, makeup styling, body, clothing, pose, close-camera distortion, lighting, background]
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

- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` prompt constraints + L0-derived geometry crop + natural frontal L0_OWNER_012 context
- hairstyle: `HAIRSTYLE_A`, L0 scoped hair derivative only
- body_reference_is_face_excluded_derivative: `true`
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- hosiery_reference_is_user_L0_material_only: `true`
- qa_comparison_only is never supplied to ImageGen
- prompt assembly: `PROMPT_ASSEMBLY.md`

## QA

- technical_status: `PASS` (1086x1448, exact 3:4, full head and both feet visible)
- fit_validation_status: `APPROVED_BY_USER`
- face_contamination_check: `PASS` (no obvious blotches or contamination in visual review; user explicitly prohibits future face-reference use)
- face_generation_method_followed: `true`
- hairstyle_A_check: `APPROVED_BY_USER`; excluded from all future reference responsibility
- leg_alignment_check: `APPROVED_BY_USER` (medial calves, inner ankles and slipper inner edges meet closely)
- hosiery_continuity_and_material_check: `APPROVED_BY_USER`
- slipper_sole_thickness_check: `APPROVED_BY_USER` (approximately 3 cm)
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `APPROVED`
- reviewer: `user`
- reviewed_at: `2026-10-17`

## Promotion and approval

- approval_status: `APPROVED`
- approved_by: `user`
- approval_date: `2026-10-17`
- approval_evidence: `可以 批准，但是被参考时严禁参考此图的人物长相和发型`
- current_approved_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png`
- current_approved_sha256: `ee5f5e473a6d5d0cf02545e03c1c0125752297cdb3f1e13b43ded02e36793910`
- promotion_operation: `MOVED`; candidate raster moved to its approved version path, no duplicate raster retained
