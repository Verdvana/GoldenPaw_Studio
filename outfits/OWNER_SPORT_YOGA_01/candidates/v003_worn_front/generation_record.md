# Generation Record

- asset_id: `OWNER_SPORT_YOGA_01_WORN_FRONT`
- outfit_id: `OWNER_SPORT_YOGA_01`
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- candidate_version: `v003`
- candidate_type: `worn_front_material_correction_clean_rebuild`
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
  - `/home/verdvana/Project/GoldenPaw_Studio/outfits/OWNER_SPORT_YOGA_01/approved/design_reference/OWNER_SPORT_YOGA_01_DESIGN_REFERENCE.png`
- reference_count: `4`
- previous_candidate_pixels_used: `false`
- excluded_candidate_pixels:
  - `v001_worn_front/OWNER_SPORT_YOGA_01_WORN_FRONT_v001.png`
  - `v002_worn_front/OWNER_SPORT_YOGA_01_WORN_FRONT_v002.png`
- output_path: `OWNER_SPORT_YOGA_01_WORN_FRONT_v003.png`

## Correction contract

The yoga pants are a substantial opaque matte performance textile, solid warm apricot-peach from waist continuously to just above the ankles. They must not look like skin, hosiery, bare legs, latex, rubber, plastic, satin or glossy leggings. The fabric thickness must soften the knee and shin bone contours; knees should read as covered by fabric, not as bare skin beneath a thin layer. The nude 15D hosiery is a separate pale, slightly milky-white translucent textile visible only below the pant cuffs on the ankles/feet; it may have restrained oily highlights, but it must be lighter than the surrounding skin and must not become darker or orange.

## Prompt assembly

Clean rebuild, not an edit of any prior generated image. Use the attached approved L1 face, body and Hairstyle-A images as hard constraints for the same recognizable owner, long straight dark-brown Hairstyle A, natural pear-shaped proportions, limb lengths, foot scale and front standing articulation. Do not use any previous candidate pixels. Apply the attached approved yoga design: soft dusty rose-pink simple sports top, warm apricot-peach full-length yoga pants ending just above the ankles, and white performance shoes with pale pink/peach accents. Critical material separation: the yoga pants must be a visibly substantial, opaque, solid warm apricot-peach matte performance fabric with no shine, no transparency, no skin-like gradients, no bare-leg appearance, no latex/plastic/rubber look, and enough thickness to soften knee and shin bone definition. They must remain the same matte peach fabric continuously from waist to ankle with a clean cuff boundary. Separately show pale nude 15D hosiery only from the pant cuffs over the ankles and feet: lighter than the skin, slightly whitish/milky, sheer knitted textile with restrained oily highlights, never darker, orange, plastic or rubber. No material blending and no calf fade. Neutral gray-white seamless studio, soft even light, complete head/hands/feet, modest breathing room. No body reshaping, text, logo, watermark or collage.

## QA

- technical_status: `PASS`
- visual_status: `REJECTED_MATERIAL_APPEARANCE`
- identity_check: `USER_REVIEW_REQUIRED`
- proportion_check: `USER_REVIEW_REQUIRED`
- pants_material_check: `FAIL`
- hosiery_color_check: `PARTIAL`
- user_review: `PENDING`
