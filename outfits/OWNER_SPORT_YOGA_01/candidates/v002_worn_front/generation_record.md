# Generation Record

- asset_id: `OWNER_SPORT_YOGA_01_WORN_FRONT`
- outfit_id: `OWNER_SPORT_YOGA_01`
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- candidate_version: `v002`
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
- output_path: `OWNER_SPORT_YOGA_01_WORN_FRONT_v002.png`

## Correction contract

The warm apricot-peach yoga pants are a separate opaque matte performance textile, continuous from waist to just above the ankles; they must not become skin-colored, transparent, glossy, or bare at the calves. The nude 15D hosiery is a separate continuous garment under/with the pants, and only the hosiery has the glossy/oily sheen, sheer knitted texture and soft highlights. No material blending or calf transition.

## Prompt assembly

Clean rebuild, not an edit of any prior generated image. Use the attached approved L1 face, body and Hairstyle-A images as hard identity and proportion constraints, preserving the same recognizable owner, long straight dark-brown Hairstyle A, natural pear-shaped proportions, limb lengths and front stance. Use the attached approved yoga design only for clothing. Show a soft dusty rose-pink simple sports top, warm apricot-peach full-length yoga pants that remain opaque matte and continuous from waist to just above the ankles, and white performance training shoes with pale pink/peach accents. Add separate nude 15D glossy pantyhose: continuous sheer textile coverage from waist through feet, with the oil-like sheen and highlights visible only on the hosiery, never on the yoga pants. Do not let the pants fade into bare legs or change color at the calves. Neutral gray-white seamless studio, front full-body, complete head/hands/feet, soft even light. No prior candidate pixels, no plastic/rubber/latex/vinyl hosiery, no body reshaping, no text, logo, watermark or collage.

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- identity_check: `USER_REVIEW_REQUIRED`
- proportion_check: `USER_REVIEW_REQUIRED`
- material_separation_check: `USER_REVIEW_REQUIRED`
- user_review: `PENDING`
