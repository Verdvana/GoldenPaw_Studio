# Generation Record

- asset_id: `OWNER_HOME_SLEEP_WINTER_01_WORN_FRONT`
- outfit_id: `OWNER_HOME_SLEEP_WINTER_01`
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- candidate_version: `v004`
- candidate_type: `worn_upper_body_clean_face_rebuild_body_face_excluded`
- status: `REVIEW_REQUIRED`
- approval_status: `PENDING_USER_REVIEW`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- reference_set_ids:
  - `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`
  - `OWNER_BODY_FRONT_LOWER_TORSO_CROP_v1`
  - `OWNER_HAIR_A_FRONT_CANON_L1`
- reference_count: `4`
- actual_image_inputs_verified: `true`
- previous_candidate_pixels_used: `false`
- output_path: `OWNER_HOME_SLEEP_WINTER_01_WORN_FRONT_v004.png`
- output_sha256: `e88b094f936e15ddc49e2b05501fabb3ac22373e5f8d9e4dcf91dfa2dde285c9`

## Reference responsibilities and exclusions

1. Face Master is the sole authority for face identity, geometry, expression and clean facial-skin presentation.
2. Deterministic Body crop is a neck-below proportion reference only; its face and head are physically excluded.
3. Hairstyle-A Master defines only the standard front hair shape and hair texture.
4. Approved winter design reference defines only the separate strawberry-pink plush jacket, matching pants and Strawberry Bear slippers.

## Prompt assembly

Use case: `identity-preserve`
Asset type: L2 winter homewear worn upper-body comparison candidate
Primary request: Create a clean, professional, non-sensual front upper-body apparel catalog image of the approved adult owner wearing the approved two-piece winter homewear. Preserve the exact owner face from Image 1 and do not borrow facial pixels, facial lighting, facial spots, or facial shading from the Body crop.
Scene/backdrop: neutral gray-white seamless studio
Subject: adult owner, head through upper hips, relaxed front posture, complete head and shoulders, enough jacket detail for comparison
Style/medium: photorealistic natural studio catalog photography
Composition/framing: vertical 3:4 portrait, eye-level, head through upper hips, centered, no collage
Lighting/mood: soft even neutral light, clean and uniform facial skin, no hard facial shadow patches or bright/dark blotches
Materials/textures: deep strawberry-pink soft plush hooded zip jacket with rounded bear ears, cream muzzle and small green leaf accents; matching visible plush waistband/upper pants; soft fleece texture without face-like noise
Constraints: use Image 1 as the only face authority; use Image 2 only below the neck; preserve Hairstyle A from Image 3; use Image 4 only for clothing design; rebuild independently from text and references
Avoid: prior v001/v002/v003 pixels, full Body image face, face blending, facial relighting from Body, iterative-generation artifacts, blotches, patches, smudges, beauty retouching, identity drift, body reshaping, exposed underwear, text, logo, watermark, collage

## QA

- technical_status: `PENDING_OUTPUT`
- visual_status: `PENDING_OUTPUT`
- user_review: `PENDING`
