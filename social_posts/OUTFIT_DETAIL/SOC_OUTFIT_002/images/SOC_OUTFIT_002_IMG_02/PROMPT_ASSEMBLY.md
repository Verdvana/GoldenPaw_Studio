# Social Post Prompt Assembly / Generation Record

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_02`
- candidate_id: `SOC_OUTFIT_002_IMG_02_CAND_01`
- model/tool: OpenAI ImageGen
- status: CANDIDATE_GENERATED_REVIEW_REQUIRED
- reference_plan: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_02/REFERENCE_PLAN.md`
- generation_inputs: L0-derived face geometry crop (face identity/features only); L0-derived natural skin crop (skin context only); face-excluded body derivative (neck-below geometry only); Hair A Canon (hair only); Autumn 02 worn-front Canon (clothing/hosiery only, face/hair excluded)
- qa_comparison_only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` (post-generation only; not attached to ImageGen)
- face_generation_rule: source-derived L0 inputs plus `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`; never use AI Face/Body Canon as face-generation input

## 1. Everyday moment and composition

A full-body mirror selfie on an autumn visit to a generic public forest park. The subject stands a few steps in front of a large circular convex wide-angle vehicle-safety mirror mounted on a pole beside a park path junction. She holds her phone and photographs her reflection; the whole reflected figure from head through hosiery-covered feet fits inside the curved mirror. The circular rim, a little of the pole, grass, path and autumn trees are visible around the reflection. Phone/camera is aimed at the mirror; no fake interface or second photographer. Keep composition casual, not staged.

## 2. Identity locks

Generate owner's face only from the two L0-derived face inputs using source-derived Face method constraints. Preserve natural facial-feature relationships, face width and warm-neutral skin. No beautification, face slimming, enlarged eyes, age shift, whitening, heavy contour, smoothing, skin patches or muddy relighting. Hair A only: long straight dark-brown hair, near-center part, low natural crown and tapered loose lengths. Maintain a plausible eye-level face projection within the mirror; no broad overhead crown or incompatible face/crown angles.

## 3. Body and appearance locks

Use only face-excluded neck-below body derivative for body proportions. Preserve natural scale and limb alignment. A relaxed standing pose with balanced weight, slight turn and one phone-holding arm; no stretched or bowed legs. Body image must not define face, skin, hair, garment, hosiery or scene.

## 4. Outfit and material contract

Autumn 02: tailored dark chocolate-brown blazer over fitted ivory fine-ribbed high-neck knit; high-waisted dark-brown pleated mini skirt; medium-thick soft-white matte pantyhose continuous from waist to closed toes. No shoes per user direction. If feet show, keep hosiery fully over heel, instep and toes; no bare toes, gaps, seams or plastic sheen. The worn-front reference defines clothes and hosiery only, not the depicted person's face, hair, body proportions or skin.

## 5. Cat, props and scale

No cat or fixed props. Temporary scene item is the circular convex safety mirror and its simple pole/mount; no other fixed prop Canon.

## 6. Environment and temporary dressing

Generic public forest-park path junction in autumn, grass edges and trees with warm foliage. Convex mirror produces a coherent wide-angle reflection: surroundings curve toward the perimeter and full-body subject is smaller toward the center, but remains legible. Include only vague public-park context; no specific park signage, residence cues or recognizable branding.

## 7. Carousel continuity-only instructions

Generate independently from approved masters. Share only the same outing, Autumn 02 clothing and no-shoes/continuous-hosiery styling with IMG_01. Do not use IMG_01 pixels as input or let it define identity, body, hair, outfit, hosiery, mirror or environment.

## 8. Realism and negative constraints

Photorealistic handheld mirror selfie, plausible convex optics and circular rim, correct physical reflection, natural contact and shadows. No normal flat mirror look, no impossible straightening, no doubled body/phone, no extra fingers or limbs, no garbled signage, no text/logo/UI/watermark, no synthetic studio bokeh, no face contamination or private-home cues. Keep the reflection clear enough to read a full-body selfie while preserving real convex distortion.

## 9. Output contract

- platform: social feed carousel draft
- aspect ratio/resolution: vertical 4:5; native dimensions recorded after generation
- expected filename: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_02/candidates/SOC_OUTFIT_002_IMG_02_CAND_01/SOC_OUTFIT_002_IMG_02_CAND_01.png`

## Generation settings/result

- generated_at: 2026-10-17
- seed/settings: not exposed by ImageGen; native 1122×1402 PNG, approximately 4:5
- output_path: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_02/candidates/SOC_OUTFIT_002_IMG_02_CAND_01/SOC_OUTFIT_002_IMG_02_CAND_01.png`
- output_checksum: `7c8313592e1e5ebad2e24c8bc5d67794baf11f2f9afa808503671e06577e878c`
- QA_record: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_02/qa/QA.md` (pending)
