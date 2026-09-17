# Generation Record

- asset_id: `OWNER_HOME_SLEEP_WINTER_01_WORN_FRONT`
- outfit_id: `OWNER_HOME_SLEEP_WINTER_01`
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- candidate_version: `v005`
- candidate_type: `worn_full_body_clean_face_rebuild_body_face_excluded`
- status: `APPROVED`
- approval_status: `APPROVED_BY_USER`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- reference_set_ids:
  - `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`
  - `OWNER_BODY_FRONT_FULL_BODY_FACE_EXCLUDED_CROP_v1`
  - `OWNER_HAIR_A_FRONT_CANON_L1`
- reference_count: `4`
- actual_image_inputs_verified: `true`
- previous_candidate_pixels_used: `false`
- original_candidate_path: `candidates/v005_worn_front/OWNER_HOME_SLEEP_WINTER_01_WORN_FRONT_v005.png`
- current_approved_path: `approved/worn_front/OWNER_HOME_SLEEP_WINTER_01_WORN_FRONT.png`
- output_sha256: `0ed215d53992eb2bf093969b8d9c331423b0e8b959590555bef5636c1e9d5242`

## Reference responsibilities and exclusions

1. Face Master is the sole authority for face identity, geometry, expression and clean facial-skin presentation.
2. Deterministic face-excluded Body crop defines only neck-below full-body proportions, limbs, feet and front standing articulation.
3. Hairstyle-A Master defines only standard front hair.
4. Approved winter design reference defines only the separate strawberry-pink plush jacket, matching pants and Strawberry Bear slippers.

## Prompt assembly

Use case: `identity-preserve`
Asset type: L2 winter homewear worn full-body comparison candidate
Primary request: Create a clean, professional, non-sensual front full-body apparel catalog image of the approved adult owner wearing the approved two-piece winter homewear.
Composition/framing: vertical 3:4 portrait, eye-level, full head to full feet, centered, modest breathing room, no crop, no collage
Lighting/mood: soft even neutral studio lighting; clean uniform facial skin without bright/dark facial blotches
Constraints: Image 1 is the only face authority; Image 2 is used only below the neck; Image 3 defines only Hairstyle A; Image 4 defines only clothing. Preserve the exact face, hair, body proportions, limb lengths, foot scale and relaxed front standing articulation. Rebuild independently and do not inherit any prior candidate.
Avoid: full Body image face, prior v001/v002/v003/v004 pixels, face blending, facial relighting from Body, iterative-generation artifacts, blotches, patches, smudges, identity drift, body reshaping, exposed underwear, text, logo, watermark, collage

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- face_contamination_check: `PASS_WITH_USER_REVIEW` — no obvious dark/bright blotch, muddy relighting, patch, smudge, or inherited Body-face artifact at full-frame inspection; user approved the candidate for L2 Canon registration.
- body_face_isolation_check: `PASS` — Body input was the deterministic face-excluded full-body derivative.
- user_review: `APPROVED`
- approval_evidence: `2026-09-17 user approved v005 as Canon`
