# Generation Record

- asset_id: `OWNER_SPORT_YOGA_01_WORN_FRONT`
- outfit_id: `OWNER_SPORT_YOGA_01`
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- candidate_version: `v007`
- candidate_type: `clean_face_body_rebuild_user_text_amendment`
- status: `REVIEW_REQUIRED`
- approval_status: `PENDING_USER_REVIEW`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-16`
- user_text_amendment: `No pants texture or stitching; no shoes; barefoot; hosiery slightly oily but paler/whiter than skin; remove facial iterative-contamination blotches.`
- reference_set_ids:
  - `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`
  - `OWNER_BODY_FRONT_CANON_L1`
- reference_count: `2`
- actual_imagegen_input_paths:
  - `/home/verdvana/Project/GoldenPaw_Studio/characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
  - `/home/verdvana/Project/GoldenPaw_Studio/characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg`
- previous_candidate_pixels_used: `false`
- ai_generated_references_used: `false`
- excluded_candidate_pixels:
  - `v001_worn_front` through `v006_worn_front`, including `v006` rejected by user
- output_path: `OWNER_SPORT_YOGA_01_WORN_FRONT_v007.png`

## Reference responsibilities and exclusions

1. Approved Face-front Canon: sole face identity, adult age, natural skin color, neutral expression and clean facial-skin presentation; excludes body, hair, clothing, hosiery, pose, lighting and setting.
2. Approved Body-front Canon: 168 cm / 60 kg front body proportions, long Hairstyle A, limb proportions and relaxed front standing articulation only; excludes face refinement, outfit, hosiery variant, footwear, environment and lighting design.

## Must not define

No prior candidate pixels, failed image artifacts, generated outfit image, or prior-shot pixels may be used. This L2 candidate must not redefine L1 face, body, hairstyle or identity Canon.

## Prompt assembly

Use case: identity-preserve. Asset type: L2 front worn yoga-outfit reference. Image 1 is the sole authority for the exact recognizable adult owner's front face, natural facial skin, neutral closed-mouth expression, and clean even complexion. Image 2 defines her approved front body proportions, long straight Hairstyle A, limb lengths, foot scale and relaxed front standing articulation. Preserve the same person exactly: no generic replacement face, no face blending, no beauty retouching, no altered age, no facial discoloration, blotches, patches, marks, smudges, duplicated facial features, or artifacts from prior generations.

Dress her in a soft dusty rose-pink simple athletic top and warm apricot-peach full-length yoga pants ending with a crisp cuff just above the ankles. The pants must be smooth, opaque and matte performance fabric with a plain clean surface: no visible textile grain, no seams, no stitch lines, no panels, no texture, no sheen, no transparency, no skin-like gradients, no bare-leg appearance, no latex, plastic, rubber or satin. The pants must remain a single even matte peach color and subtly soften knee/shin contours.

No shoes. Show both full feet bare except for continuous pale-white nude 15D pantyhose from waist through toes. The pantyhose must be noticeably lighter and whiter than her natural skin while still a plausible light nude textile, very sheer, fine knitted, and with a restrained soft oily gloss only on the hosiery. Keep the hosiery visibly present over ankles, heels, insteps and every toe; soft burgundy toenail color may show faintly beneath the textile. No bare toes, toe-cap line, horizontal toe-root line, plastic/rubber/latex/liquid surface, detached feet or missing/extra/fused toes.

Neutral gray-white seamless studio, soft even light, eye-level 70–85 mm perspective, vertical 3:4 full-body image with head, hair, hands and feet complete and modest breathing room. One adult person only. No yoga pose, shoes, socks, props, text, logo, watermark, collage, extra garments, braid or altered hairstyle.

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- actual_image_inputs_verified: `true`
- user_review: `PENDING`
