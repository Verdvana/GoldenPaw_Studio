# Generation Record

- asset_id: `OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT`
- outfit_id: `OWNER_HOME_SLEEP_SUMMER_01`
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- candidate_version: `v002`
- candidate_type: `worn_front_regeneration`
- status: `APPROVED`
- approval_status: `APPROVED_BY_USER`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-16`
- owner_spec_revision_consulted: `draft_1.222`
- reference_set_ids:
  - `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`
  - `OWNER_BODY_FRONT_CANON_L1`
  - `OWNER_HAIR_A_FRONT_CANON_L1`
  - `OWNER_HOS_01_LOWER_LEGS_FEET_FRONT_CANON_L1`
- reference_count: `5` including the approved L2 outfit design reference
- actual_imagegen_input_paths:
  - `/home/verdvana/Project/GoldenPaw_Studio/characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
  - `/home/verdvana/Project/GoldenPaw_Studio/characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg`
  - `/home/verdvana/Project/GoldenPaw_Studio/characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
  - `/home/verdvana/Project/GoldenPaw_Studio/characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_01_LOWER_LEGS_FEET_FRONT/OWNER_HOS_01_LOWER_LEGS_FEET_FRONT_CANON_002.png`
  - `/home/verdvana/Project/GoldenPaw_Studio/outfits/OWNER_HOME_SLEEP_SUMMER_01/approved/design_reference/OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE.png`
- previous_candidate_pixels_used: `false`
- outfit_design_reference: `outfits/OWNER_HOME_SLEEP_SUMMER_01/approved/design_reference/OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE.png`
- output_path: `approved/worn_front/OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT.png`
- original_candidate_path: `candidates/v002_worn_front/OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT_v002.png`
- promotion_method: `MOVE_NO_PIXEL_COPY`
- approval_date: `2026-09-16`
- approval_evidence: `User explicitly said “批准了”`

## Reference responsibilities and exclusions

1. Approved face-front Canon: the owner's visible front identity only; excludes body, hair, outfit, hosiery, footwear, pose, lighting and background.
2. Approved Body-front Canon: approved 168 cm / 60 kg body proportions, limb proportions, waist/hip ratio and neutral front stance; excludes outfit and footwear design.
3. Approved Hair-A front Canon: standard front Hairstyle A only; excludes face geometry, body, clothing, hosiery, footwear and setting.
4. Approved HOS-01 lower-legs/feet front Canon: continuous 15D nude matte closed-toe hosiery treatment, softened burgundy toenails beneath textile, and natural front foot presentation only; excludes complete identity, outfit and footwear.
5. Approved summer-sleepwear design reference: champagne silk camisole sleep-dress silhouette/material impression and pink medium-width bow-front open-toe flat slippers only; excludes identity, body, hair and hosiery material authority.

## Must not define

This L2 candidate must not redefine or supersede any L1 face, body, hair, skin, hosiery/feet or identity Canon. It must not use `v001` or any other unapproved/failed AI candidate as a pixel reference. It must not alter the approved L2 outfit design.

## Reference budget

Five images total: one face, one body, one hairstyle, one hosiery/feet, and one outfit-design reference. No previous-shot or previous-candidate image.

## Prompt assembly

Use case: identity-preserve. Asset type: L2 front worn outfit reference. Create one photorealistic, non-erotic, neutral studio fashion-reference photograph of the approved adult owner, visibly presenting her real approved front face rather than a mannequin, faceless stand-in, or generic model. Preserve the approved front identity, natural 168 cm / 60 kg body proportions, standard Hairstyle A, relaxed closed-mouth neutral expression, straight-on neutral standing articulation, and natural hands and feet.

Dress her in the approved summer home sleepwear exactly: a champagne-colored silk camisole-strap short sleep dress with a simple softly curved neckline, relaxed natural A-line drape, tasteful upper-thigh hem, refined realistic silk sheen, and no added lace or decoration; plus the approved pink satin medium-width bow-front open-toe flat slide slippers with a low completely flat sole. Under the dress, use nude 15D matte pantyhose as one continuous closed-toe textile garment from waist through thighs, knees, calves, ankles, heels, insteps and toes. The textile must remain visibly present over every toe, with soft natural transparency and subtle burgundy toenail color only beneath the hosiery; no bare toes, toe-cap line, horizontal toe-root seam, detached foot section, socks, or polish painted on top of the textile. The slippers are genuinely open at the toe, and the hosiery-covered toes remain naturally visible through the opening.

Neutral gray-white seamless studio, soft even 5200–5600K lighting, eye-level 70–85 mm portrait perspective, vertical 3:4 full-body framing with the complete head, hair, hands, slippers and feet visible and modest breathing room. One adult person only. No mannequin, faceless person, generic replacement face, identity drift, beautification, altered age, altered body proportions, crossed legs, fashion pose, bedroom, props, text, logo, watermark, collage, extra garments, robe, lingerie styling, nudity, transparency through the dress, high heels, platform, closed-toe footwear, plush footwear, plastic/latex/PVC/rubber/liquid hosiery, malformed hands, malformed feet, fused shoe/toes, extra or missing digits.

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- actual_image_inputs_verified: `true`
- user_review: `APPROVED`
