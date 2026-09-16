# Generation Record

- asset_id: `OWNER_HOME_SLEEP_WINTER_01_WORN_FRONT`
- outfit_id: `OWNER_HOME_SLEEP_WINTER_01`
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- candidate_version: `v003`
- candidate_type: `worn_front_clean_rebuild`
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
  - `/home/verdvana/Project/GoldenPaw_Studio/outfits/OWNER_HOME_SLEEP_WINTER_01/approved/design_reference/OWNER_HOME_SLEEP_WINTER_01_DESIGN_REFERENCE.png`
- reference_count: `4`
- previous_candidate_pixels_used: `false`
- excluded_candidate_pixels:
  - `v001_worn_front/OWNER_HOME_SLEEP_WINTER_01_WORN_FRONT_v001.png`
  - `v002_worn_front/OWNER_HOME_SLEEP_WINTER_01_WORN_FRONT_v002.png`
- output_path: `OWNER_HOME_SLEEP_WINTER_01_WORN_FRONT_v003.png`

## Reference responsibilities

- Face L1: exact recognizable front owner identity and facial geometry only.
- Body L1: approved body proportions, pear-shaped waist/hip relationship, limb lengths and front standing articulation only.
- Hairstyle-A L1: standard front Hairstyle A only.
- Approved outfit design: separate strawberry-pink plush jacket, matching pants and Strawberry Bear slippers only.

## Prompt assembly

Clean rebuild of one professional, non-sensual front full-body apparel reference. Use the attached approved L1 face, body and Hairstyle-A images as hard identity and proportion constraints. Preserve the same recognizable facial structure, eye/nose/mouth relationship, face width, long straight dark-brown Hairstyle A, 168 cm / 60 kg target proportions, natural pear-shaped waist-to-hip relationship, leg length, foot scale, and relaxed front standing articulation. Do not use, edit, or visually inherit either rejected candidate. Apply the attached approved winter outfit design only: deep strawberry-pink hooded plush zip jacket with friendly Strawberry Bear hood, cream muzzle and small green leaf accents; matching separate straight-leg plush lounge pants; matching Strawberry Bear plush slippers. Jacket and pants must remain clearly separate, not a jumpsuit. Neutral gray-white seamless studio, soft even light, complete head/hands/feet, modest breathing room. No identity drift, no faceless mannequin, no body reshaping, no glamour retouching, no text, logo, watermark, collage or unrelated garments.

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- identity_check: `USER_REVIEW_REQUIRED`
- proportion_check: `USER_REVIEW_REQUIRED`
- user_review: `PENDING`
