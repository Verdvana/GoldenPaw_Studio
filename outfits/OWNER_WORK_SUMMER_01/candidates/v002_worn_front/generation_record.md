# Generation Record

- asset_id: `OWNER_WORK_SUMMER_01_WORN_FRONT`
- outfit_id: `OWNER_WORK_SUMMER_01`
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- candidate_version: `v002`
- candidate_type: `worn_full_body_axis_corrected_clean_face_rebuild`
- status: `REVIEW_REQUIRED`
- approval_status: `PENDING_USER_REVIEW`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- reference_set_ids:
  - `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`
  - `OWNER_BODY_FRONT_FULL_BODY_FACE_EXCLUDED_CROP_v1`
  - `OWNER_HAIR_A_FRONT_CANON_L1`
- reference_count: `4`
- actual_image_inputs_verified: `true`
- previous_candidate_pixels_used: `false`
- excluded_candidate_pixels:
  - `v001_worn_front/OWNER_WORK_SUMMER_01_WORN_FRONT_v001.png`
- output_path: `OWNER_WORK_SUMMER_01_WORN_FRONT_v002.png`
- output_sha256: `96a279a91acf4c1a26aefa9da2b3695493f6204d8b515de010d6ba86e2308c92`

## Reference responsibilities and exclusions

1. Face Master is the sole authority for face identity, geometry, expression and clean facial-skin presentation.
2. Face-excluded Body crop defines only neck-below full-body proportions, limb lengths, feet and relaxed front standing articulation.
3. Hairstyle-A Master defines only standard front hair.
4. Approved summer officewear design defines only the clothing and footwear design.

## Prompt assembly

Use case: `identity-preserve`
Asset type: L2 summer officewear worn full-body corrected candidate
Primary request: Rebuild the same clean, professional, non-sensual front full-body summer officewear catalog image with corrected neutral standing leg alignment.
Composition/framing: vertical 3:4, eye-level, full head to full feet, centered, modest breathing room, no crop, no collage
Pose correction: neutral front standing; pelvis level; both thighs, knees, calves, ankles and heel centers aligned on each leg's natural vertical anatomical axis; lower legs straight and parallel with no bow-legged or knock-kneed deviation, no knee collapse, no crossed legs, no twisting, no weight shift; both feet flat and symmetrically placed.
Lighting/mood: soft even neutral studio lighting; clean uniform facial skin without bright/dark facial blotches
Constraints: Image 1 only defines face; Image 2 only defines below-neck body context; Image 3 only defines Hairstyle A; Image 4 only defines clothing. Do not use v001 pixels.
Outfit: fitted black short-sleeve low-neck top; champagne-ivory satin fitted mid-thigh pencil skirt with dense small black polka dots; gray 15D matte continuous closed-toe pantyhose; black softly round-pointed matte slingback kitten-heel shoes with curved vamp and single rear strap.
Avoid: full Body face, prior candidate pixels, face blending, facial relighting from Body, facial artifacts, leg axis deviation, bent knees, crossed ankles, asymmetrical foot placement, body reshaping, text, logo, watermark or collage

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- face_contamination_check: `PASS_WITH_USER_REVIEW`
- leg_axis_check: `PASS_WITH_USER_REVIEW`
- user_review: `PENDING`
