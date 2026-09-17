# Outfit Generation Record

- asset_id: `OWNER_SPORT_BADMINTON_01_WORN_FRONT`
- outfit_id: `OWNER_SPORT_BADMINTON_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v001`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_BADMINTON_01/candidates/v001_worn_front/OWNER_SPORT_BADMINTON_01_WORN_FRONT_v001.png`
- output_sha256: `c8aca786eca78cb385846e5f9a76365c77ebe50adbdb06cc8cb2267fabf19920`
- original_candidate_path: `candidates/v001_worn_front/OWNER_SPORT_BADMINTON_01_WORN_FRONT_v001.png`
- promoted_asset_path: `approved/worn_front/OWNER_SPORT_BADMINTON_01_WORN_FRONT.png`
- promoted_asset_sha256: `c8aca786eca78cb385846e5f9a76365c77ebe50adbdb06cc8cb2267fabf19920`
- generation_inputs: [OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, OWNER_HAIRSTYLE_A_FACE_MASKED_001, OWNER_BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v2, OWNER_SPORT_BADMINTON_01_DESIGN_REFERENCE]
- qa_comparison_only: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1]
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- ai_face_canon_used_as_generation_input: `false`
- unapproved_outfit_raster_used_as_generation_input: `false`
- face_generation_method_followed: `true`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`

## Generation inputs

Use the source-derived Face method and L0 inputs for the visible owner's face; use
the face-excluded Body derivative for neck-below proportions and neutral stance; use
the approved design reference only for outfit properties. Do not use the AI Face
Canon as a generation input.

## Validation target

- fit_or_design_question: Verify the complete head-present owner presentation, visor/head relationship, sleeveless tank fit, tennis-skirt length and built-in shorts, lightweight white 15D matte thigh-high hosiery, and performance-shoe relationship.
- acceptance_checks: [clean Face method result, Hairstyle A only, crownless visor, tank and skirt fit readable, hosiery visibly sheer rather than thick, top edge above knee, shoes remain performance footwear]

## Prompt assembly

Use case: `product-mockup`. Create a modest professional badminton apparel catalog
fitting reference of the same adult owner with complete head, face, Hairstyle A,
neck, shoulders, torso, legs and feet visible in a neutral front standing pose. This
is an L2 clothing-fit validation asset, not a video keyframe or identity Canon.
Generate the face only from the source-derived Face method and L0 inputs; do not use
any AI Face Canon pixels.

Dress her in the approved coordinated badminton outfit: a crownless white sports
visor with a narrow pale mint-green headband; a pale mint-green sleeveless athletic
tank; a pure-white tennis skirt with built-in shorts; lightweight white 15D sheer
matte thigh-high hosiery with the top edge above the knee and subtle underlying skin
visibility; and white performance badminton shoes with small pale-mint and soft
lavender accents. Keep hosiery fine, translucent, matte and textile-like, never
thick, opaque or cotton-like. Keep the visor clearly open-crown and the outfit
modest, practical and sport-functional.

Use seamless light neutral gray studio lighting, soft even catalog illumination,
centered vertical 3:4 full-body framing, normal catalog scale. Preserve natural
face relationships, warm-neutral skin and Hairstyle A: long straight loose dark-
brown hair, near-center part, low crown and tapered ends. No face blotches, patches,
smudges, muddy relighting, beauty retouching, body reshaping or iterative artifacts.

Avoid hairstyle B, face drift, previous candidates, bare legs, opaque white tights,
thick stockings, cotton texture, ribbed socks, full pantyhose, glossy hosiery,
closed-crown hat, long sleeves, high heels, latex, PVC, plastic, rubber, text,
logo, watermark, collage or lifestyle court background.

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `PASS`
- fit_validation_status: `PASS_WITH_USER_REVIEW`
- face_contamination_check: `REVIEW_REQUIRED`
- face_generation_method_followed: `true`
- decision: `APPROVED_AND_PROMOTED`
- approved_by: `user`
- approved_at: `2026-09-17`
