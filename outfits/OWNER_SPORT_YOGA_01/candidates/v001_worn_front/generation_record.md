# Generation Record

- asset_id: `OWNER_SPORT_YOGA_01_WORN_FRONT`
- outfit_id: `OWNER_SPORT_YOGA_01`
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- candidate_version: `v001`
- candidate_type: `worn_front`
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
- output_path: `OWNER_SPORT_YOGA_01_WORN_FRONT_v001.png`

## Reference responsibilities

- Face L1: exact front owner identity and facial geometry only.
- Body L1: approved body proportions, pear-shaped waist/hip relationship, limb lengths and front standing articulation only; does not define the yoga outfit or glossy hosiery.
- Hairstyle-A L1: standard front Hairstyle A only.
- Approved yoga design: dusty rose-pink simple Y-back top, warm apricot-peach full-length yoga pants, nude 15D glossy hosiery styling and white training shoes only.

## Prompt assembly

Clean professional sportswear catalog worn reference, one front full-body view. Use the attached approved L1 face, body and Hairstyle-A images as hard constraints: preserve the same recognizable owner face, long straight dark-brown Hairstyle A, natural pear-shaped body proportions, waist/hip relationship, limb lengths, foot scale and relaxed upright front stance. Do not use or inherit any prior generated candidate. Apply the attached approved yoga design: soft dusty rose-pink simple strappy sports top with restrained Y-back construction, warm apricot-peach fitted full-length yoga pants ending just above the ankles, and white performance training shoes with small pale-pink/peach accents. Add light natural nude 15D glossy pantyhose as one continuous closed-toe textile garment from waist through feet, visibly sheer with fine knitted fiber texture and soft oily highlights, flexible fabric behavior, never plastic, rubber, latex, vinyl or mannequin-like; no toe-cap line. Neutral gray-white seamless studio, soft even light, complete head/hands/feet with modest breathing room. No face drift, body reshaping, text, logo, watermark, collage or unrelated garments.

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- identity_check: `USER_REVIEW_REQUIRED`
- proportion_check: `USER_REVIEW_REQUIRED`
- hosiery_material_check: `USER_REVIEW_REQUIRED`
- user_review: `PENDING`
