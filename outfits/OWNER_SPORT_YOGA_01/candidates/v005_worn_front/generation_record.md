# Generation Record

- asset_id: `OWNER_SPORT_YOGA_01_WORN_FRONT`
- outfit_id: `OWNER_SPORT_YOGA_01`
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- candidate_version: `v005`
- candidate_type: `clean_l1_only_rebuild_material_correction`
- status: `REVIEW_REQUIRED`
- approval_status: `PENDING_USER_REVIEW`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-16`
- reference_set_ids:
  - `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`
  - `OWNER_BODY_FRONT_CANON_L1`
  - `OWNER_HAIR_A_FRONT_CANON_L1`
- actual_imagegen_input_paths:
  - `/home/verdvana/Project/GoldenPaw_Studio/characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
  - `/home/verdvana/Project/GoldenPaw_Studio/characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg`
  - `/home/verdvana/Project/GoldenPaw_Studio/characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
- reference_count: `3`
- previous_candidate_pixels_used: `false`
- ai_generated_outfit_references_used: `false`
- excluded_candidate_pixels:
  - `v001_worn_front/OWNER_SPORT_YOGA_01_WORN_FRONT_v001.png`
  - `v002_worn_front/OWNER_SPORT_YOGA_01_WORN_FRONT_v002.png`
  - `v003_worn_front/OWNER_SPORT_YOGA_01_WORN_FRONT_v003.png`
  - `v004_worn_front/OWNER_SPORT_YOGA_01_WORN_FRONT_v004.png`
- output_path: `OWNER_SPORT_YOGA_01_WORN_FRONT_v005.png`

## Clean-lineage contract

Only approved L1 face, body and Hairstyle-A images are image inputs. No AI-generated outfit, worn-view, design-board or prior candidate image is used. Reconstruct the L2 outfit from text only.

## Prompt assembly

Clean independent rebuild from the three attached approved L1 owner references only. Preserve the exact recognizable owner face and facial proportions, long straight dark-brown Hairstyle A, natural pear-shaped body proportions, waist-to-hip relationship, limb lengths, foot scale and front standing articulation. Do not inherit any AI-generated face or outfit image. Create one professional non-sensual front full-body sportswear reference. Outfit by text specification: dusty rose-pink simple sports top; warm apricot-peach full-length yoga pants from waist continuously to a crisp cuff just above the ankles; white performance training shoes with small pale pink accents. The pants must be unmistakably substantial opaque matte athletic fabric, clearly separate from skin, with visible woven/knit textile grain, waistband and restrained seams, no shine, no translucency, no skin-like gradients, and enough thickness to soften knee and shin bone contours. Separately show pale nude 15D hosiery only below the pant cuffs over ankles and feet; it is lighter and slightly whitish than the skin, sheer knitted textile with restrained oily highlights, never darker or orange. Clean boundary, no calf fade, no material blending. Neutral gray-white seamless studio, soft even light, complete head/hands/feet, modest breathing room. No body reshaping, faceless mannequin, identity drift, text, logo, watermark, collage or unrelated garments.

## QA

- technical_status: `PASS`
- visual_status: `REJECTED_IDENTITY_DRIFT`
- identity_check: `FAIL`
- proportion_check: `PENDING`
- pants_material_check: `USER_REVIEW_REQUIRED`
- hosiery_color_check: `PASS_WITH_USER_REVIEW`
- lineage_check: `PASS`
- user_review: `REJECTED_PENDING_REBUILD`
- rejection_reason: `Face shows severe identity drift despite L1 inputs; this candidate must not be used downstream.`
