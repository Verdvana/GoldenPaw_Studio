# Generation Record

- asset_id: `OWNER_HOME_SLEEP_WINTER_01_WORN_FRONT`
- outfit_id: `OWNER_HOME_SLEEP_WINTER_01`
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- candidate_version: `v001`
- candidate_type: `worn_front`
- status: `REJECTED`
- approval_status: `REJECTED_BY_USER`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-16`
- reference_set_ids:
  - `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`
  - `OWNER_BODY_FRONT_CANON_L1`
  - `OWNER_HAIR_A_FRONT_CANON_L1`
- reference_count: `3`
- previous_candidate_pixels_used: `false`
- actual_imagegen_input_paths: `NOT_USED_IN_THIS_FAILED_CALL`
- next_call_requirement: `The three paths in reference_inputs.yaml must be passed as actual referenced_image_paths; naming them only in the prompt is invalid.`
- outfit_design_reference: `outfits/OWNER_HOME_SLEEP_WINTER_01/approved/design_reference/OWNER_HOME_SLEEP_WINTER_01_DESIGN_REFERENCE.png` (design responsibility only)
- output_path: `OWNER_HOME_SLEEP_WINTER_01_WORN_FRONT_v001.png`

## Reference responsibilities and exclusions

1. Approved face front Canon: owner's front identity only; excludes body, hair, outfit, pose, lighting and background.
2. Approved Body front Canon: approved body proportions and front standing articulation only; excludes outfit design, props, footwear and setting.
3. Approved Hair-A front Canon: standard front Hairstyle A only; excludes face geometry, body, clothing, footwear and setting.
4. Approved winter sleepwear design reference: deep strawberry-pink hooded plush zip jacket, matching lounge pants and Strawberry Bear slippers only; excludes owner identity, body and hair.

## Prompt assembly

Create one professional, non-sensual apparel catalog worn reference of the approved adult owner in a neutral front standing pose. Preserve the approved front identity and Hairstyle A. Show the approved practical two-piece winter homewear: deep strawberry-pink hooded plush zip jacket with friendly Strawberry Bear hood/face treatment, cream muzzle and small green strawberry-leaf accents; matching deep strawberry-pink straight-leg plush lounge pants; matching Strawberry Bear plush slippers. Keep the jacket and pants clearly separate for easy bathroom access; no jumpsuit. Use soft realistic plush texture, tidy construction, comfortable relaxed fit, complete head/hands/feet with modest breathing room, neutral gray-white seamless studio and soft even catalog lighting. No sensual styling, body emphasis, exposed underwear, text, logo, watermark, collage, or unrelated garments.

## QA

- technical_status: `PASS`
- visual_status: `REJECTED`
- user_review: `REJECTED_BY_USER`
- rejection_reason: `Generated face did not match the approved owner identity; declared L1 references were not supplied as actual image inputs.`
