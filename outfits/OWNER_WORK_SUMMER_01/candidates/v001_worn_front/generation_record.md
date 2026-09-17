# Generation Record

- asset_id: `OWNER_WORK_SUMMER_01_WORN_FRONT`
- outfit_id: `OWNER_WORK_SUMMER_01`
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- candidate_version: `v001`
- candidate_type: `worn_full_body_clean_face_rebuild_body_face_excluded`
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
- output_path: `OWNER_WORK_SUMMER_01_WORN_FRONT_v001.png`
- output_sha256: `d7d44bd17e8648c535e592867c9b9e631a40078a2516b79567f0c1e4dbd50307`

## Reference responsibilities and exclusions

1. Face Master is the sole authority for face identity, geometry, expression and clean facial-skin presentation.
2. Deterministic face-excluded Body crop defines only neck-below full-body proportions, limbs, feet and relaxed front standing articulation.
3. Hairstyle-A Master defines only standard front hair.
4. Approved summer officewear design reference defines only the black top, champagne-ivory polka-dot skirt, gray 15D matte pantyhose and black slingback kitten-heel shoes.

## Prompt assembly

Use case: `identity-preserve`
Asset type: L2 summer officewear worn full-body candidate
Primary request: Create a clean, professional, non-sensual front full-body apparel catalog image of the approved adult owner wearing the approved summer office outfit.
Composition/framing: vertical 3:4 portrait, eye-level, full head to full feet, centered, modest breathing room, no crop, no collage
Lighting/mood: soft even neutral studio lighting; clean uniform facial skin without bright/dark facial blotches
Constraints: Image 1 is the only face authority; Image 2 is used only below the neck; Image 3 defines only Hairstyle A; Image 4 defines only clothing. Preserve the exact face, hair, body proportions, limb lengths, foot scale and relaxed front standing articulation. Rebuild independently and do not inherit any prior candidate.
Outfit: fitted black short-sleeve low-neck professional top; champagne-ivory satin fitted mid-thigh pencil skirt with dense small black polka dots and rear center slit; gray 15D matte continuous closed-toe pantyhose; black ordinary-matte softly round-pointed slingback kitten-heel shoes with curved-cut vamp and single rear strap.
Avoid: full Body image face, face blending, facial relighting from Body, prior AI candidate pixels, iterative-generation artifacts, blotches, patches, smudges, identity drift, body reshaping, transparent hosiery, toe-cap line, latex, plastic, rubber, text, logo, watermark or collage

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- face_contamination_check: `PASS_WITH_USER_REVIEW` — no obvious dark/bright blotch, muddy relighting, patch, smudge, or inherited Body-face artifact at full-frame inspection.
- user_review: `PENDING`
