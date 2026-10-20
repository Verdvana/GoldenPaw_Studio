# Social Post Prompt Assembly / Generation Record

- post_id: `SOC_OUTFIT_003`
- image_asset_id: `SOC_OUTFIT_003_IMG_01`
- candidate_id: `SOC_OUTFIT_003_IMG_01_CAND_01`
- model/tool: built-in `image_gen` image edit
- status: GENERATED; REVIEW_REQUIRED
- reference_plan: `REFERENCE_PLAN.md`
- generation_inputs: `L0_OWNER_SOC_OUTFIT_003_SOURCE_IMG_9103`, `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001`, `OWNER_BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1`, `OWNER_HAIR_A_01_FRONT_CANON_001`, `OWNER_HAIR_A_04_BACK_CANON_001`
- qa_comparison_only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
- face_generation_rule: source-derived L0 face geometry and skin inputs plus `FACE_01_FRONT_NEUTRAL_METHOD.md` constraints; approved AI Face/Body Canons are not generation inputs
- user_gate: authorized one candidate for IMG_01 on 2026-10-20

## 1. Everyday moment and composition

Retouch the user's original vertical phone photo from a real shoe-store try-on moment. Keep the same bent-forward pose, camera position, full-length framing, mirror reflection, shoe displays, floor, store lighting, shadows, exposure and color balance. Preserve the original 9:16 composition and do not crop away the hosiery or shoes.

## 2. Identity locks

The mirror reflection is the only visible face. Keep its original small scale, downward gaze, head angle and expression. Use the L0-derived face-geometry crop for identity and feature relationships; the original real photo supplies only the existing natural skin appearance under its actual lighting. Follow `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`; preserve natural feature relationships, age and warm-neutral skin. No face slimming, eye enlargement, nose refinement, age change, whitening, smoothing or generic beautification. The AI Face Canon is for post-generation QA comparison only.

## 3. Body and appearance locks

Use the approved face/hair-excluded rear lower-body derivative only for hip, thigh, calf, ankle and heel proportions. Keep the source pose, bent posture, limb angles, hands, feet and floor contact. Make only a canon-consistent body-shape adjustment that is visible under the same garments; do not change clothing design or pose. Use HAIRSTYLE_A only: near-center part in the mirror, long straight loose dark-brown hair, low controlled crown and natural tapered ends. In the bent pose, let the same long hair fall naturally with gravity. Do not blend A/B or invent another hairstyle.

## 4. Outfit and material contract

Preserve the exact brown patterned sweater, checked skirt, shoes and existing pale beige/tan pantyhose from the source photo. Keep the pantyhose conspicuous and visibly continuous from under the skirt over both legs through ankles and into the visible shoe openings, with the source's existing color, opacity and matte textile appearance. Do not expose bare-leg patches, recolor or replace the hosiery, turn it glossy/plastic, or alter the shoe shape/color/placement. The garments may follow the canon-matched body naturally while retaining their original designs, colors, pattern, length and styling.

## 5. Cat, props and scale

No cat. Preserve the existing shoes, display footwear, handbags, boxes/packing material and their scale and placement.

## 6. Environment and temporary dressing

Keep the same mall shoe store, wall and mirrors, original Chinese wall signage, shelf arrangement, display shoes, overhead fixtures, floor reflections and ambient light. Do not replace, redesign, brighten, darken or relight the environment. Do not add brands, readable new text, UI or watermarks.

## 7. Carousel continuity-only instructions

This is IMG_01 and is independently edited from its own real source photo and approved master assets. It defines no identity, body, hair, shoe, hosiery-material or environment authority for another image.

## 8. Realism and negative constraints

Photographic retouch only. Preserve all non-subject scene details and original optical perspective. No crop, zoom, re-stage, background repaint, mirror deformation, light/color change, garment replacement, hosiery discontinuity, plastic skin, changed face identity, changed pose, malformed hands/feet/shoes, invented store branding, fake UI, watermark or garbled text.

## 9. Output contract

- platform: portrait social-feed draft
- aspect ratio/resolution: preserve source 9:16 framing, 2268×4032 source target or nearest native portrait output without cutting off the hosiery/shoes
- required safe areas: keep entire visible hosiery coverage and both shoes in frame; keep reflected face and hair inside the mirror
- expected filename/path: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_003/images/SOC_OUTFIT_003_IMG_01/candidates/SOC_OUTFIT_003_IMG_01_CAND_01/SOC_OUTFIT_003_IMG_01_CAND_01.png`

## Final assembled prompt

Use case: identity-preserve photo edit. Asset type: one L3 image for the first frame of `SOC_OUTFIT_003`, a shoe-shopping social carousel. Image 1 is the edit target: the user's original 9:16 shoe-store mirror photo and the source of its actual lighting, outfit, hosiery, environment, expression and natural skin appearance. Image 2 is the source-derived L0 face-geometry reference and defines facial identity/feature relationships only. Image 3 is an approved deterministic face/hair-excluded rear lower-body derivative and defines hips, thighs, calves, ankles and heels only. Images 4 and 5 are approved Hairstyle A Canon views and define front-in-mirror and rear hair construction only. Edit only the owner's face appearance as visible in the mirror, Hairstyle A and visible lower-body proportions. Preserve the original downward gaze, expression, head angle, bent pose, arm/hand positions and full-body camera framing. Preserve the original brown patterned sweater, checked skirt, pale beige/tan pantyhose and shoes exactly in design, color, pattern, length and placement. Keep the pantyhose clearly visible and continuous from under the skirt over both legs and into the shoe openings; retain its source matte textile appearance and opacity, with no bare-skin breaks or plastic shine. Keep the exact shopping-mall store, mirrors, wall/signage, shelves, display shoes, handbags, floor, reflections, overhead fixtures, ambient lighting, exposure, shadows and color balance. No crop, zoom, re-stage, new text, logos, UI or watermark. Use the L0-derived face geometry and `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`; never use an AI Face/Body Canon or generated candidate as a generation input. Photorealistic localized retouch; all non-person scene details remain as in the source.

## Generation settings/result

- generated_at: 2026-10-20
- seed/settings: one built-in image edit call; seed not exposed by tool
- output_path: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_003/images/SOC_OUTFIT_003_IMG_01/candidates/SOC_OUTFIT_003_IMG_01_CAND_01/SOC_OUTFIT_003_IMG_01_CAND_01.png`
- output_checksum: `97e74af5ab97bc6b23eaf1a31d6ed7c9ef442a10fff7ba17cd40b64d9b223d0b`
- output_dimensions: `941x1672`
- QA_record: `qa/QA.md` (to be completed after visual inspection)
