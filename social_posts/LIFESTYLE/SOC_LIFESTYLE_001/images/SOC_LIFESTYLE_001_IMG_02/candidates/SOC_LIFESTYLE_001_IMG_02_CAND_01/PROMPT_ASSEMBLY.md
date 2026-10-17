# Social Post Prompt Assembly — SOC_LIFESTYLE_001_IMG_02_CAND_01

- post_id: SOC_LIFESTYLE_001
- image_asset_id: SOC_LIFESTYLE_001_IMG_02
- candidate_id: SOC_LIFESTYLE_001_IMG_02_CAND_01
- model/tool: OpenAI ImageGen
- status: GENERATED_REVIEW_REQUIRED
- reference_plan: `REFERENCE_PLAN.md`
- generation_inputs: source-derived face/skin crop; masked L0 Hairstyle-A derivative; face-excluded body derivative; scoped hosiery material crop
- qa_comparison_only: approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` after generation only
- face_generation_rule: source-derived L0 inputs plus applicable Face method prompt constraints; AI Face/Body Canon is QA-only

## 1. Everyday moment and composition

Full-length casual selfie by the owner herself, standing just outside the same generic flower shop. She holds her own phone at chest height and uses the broad shop window as a natural reflection, capturing her full outfit from head to loafers. Phone and gripping hand clearly visible in reflection; face remains visible beside the phone. Slightly imperfect handheld alignment, ordinary sidewalk and plane trees, soft cloudy afternoon.

## 2. Identity locks

Generate face only from the source-derived face/skin input following `FACE_01_FRONT_NEUTRAL_METHOD.md`. Preserve natural adult identity and warm-neutral skin, no beautification. The masked L0 hair image defines only HAIRSTYLE_A, long straight loose dark brown hair with a near-center part and tapered ends. Do not use any previous AI image to define face or hair.

## 3. Body and appearance locks

The face-excluded body derivative defines only neck-below proportions and limb geometry; preserve realistic natural build and limb length, with no elongation or slimming.

## 4. Outfit and material contract

Maintain the approved look: cream fine-knit top, light-khaki straight mini skirt, pale nude/light-skin 15D matte velvet-finish sheer pantyhose, brown loafers, light thin trench carried over one forearm. Make the pantyhose leg-to-foot coverage continuous and textile-realistic. The entire tights and shoes should be visible; hosiery must not look like bare skin, latex, plastic or wet gloss.

## 5. Cat, props and scale

No cat. One plain modern smartphone held naturally in one hand. Same modest bouquet in kraft paper in the other arm. No brands or readable screen UI.

## 6. Environment and temporary dressing

Same cloudy autumn afternoon, same public flower-shop frontage and plane-tree sidewalk as the approved first post image. Use a clean broad window reflection without readable signage. Public street only; no home or office.

## 7. Carousel continuity-only instructions

Continuity is text-only: same owner outfit, bouquet, flower-shop street and afternoon. The first image's pixels are not an input and cannot define identity, body, hairstyle, hosiery, props or location architecture.

## 8. Realism and negative constraints

Photographic candid mirror/reflection selfie, plausible reflection geometry, natural hands and phone grip, correctly grounded feet, consistent cloudy daylight. No face contamination, identity drift, face/body patches, extra fingers, duplicated limbs, broken shoes, distorted body proportions, hosiery discontinuity or bare-toe breaks, latex/PVC/plastic/rubber, garbled text, fake UI, logos or watermark.

## 9. Output contract

- platform: social feed
- aspect ratio/resolution: vertical 4:5, native portrait generation closest available
- required safe areas: keep face, phone, bouquet, complete legs, shoes and full outfit inside central 90%
- expected filename/path: `SOC_LIFESTYLE_001_IMG_02_CAND_01.png` in this candidate directory

## Final assembled prompt

Generate exactly one photorealistic vertical 4:5 full-length casual smartphone reflection selfie, taken by the adult owner herself just outside a generic small flower shop on a Shanghai plane-tree sidewalk on the same softly cloudy afternoon as the companion image. The first image contributes text-only continuity (same outfit, bouquet, flower-shop street, time/weather) and is not a visual reference. The owner holds a plain modern smartphone at chest height; show the phone and hand clearly in the broad shop-window reflection while keeping her face visible beside it. Full body from head through both loafers must fit, including the skirt and uninterrupted pale sheer pantyhose. Preserve her face and warm-neutral skin only from the supplied source-derived face/skin input, following the applicable front-face method; no generated face/body image defines identity. Use the masked L0 reference only for HAIRSTYLE_A, long straight loose dark-brown hair with a near-center part and tapered ends. Use the face-excluded body derivative only for neck-below proportions. Keep the approved first-image wardrobe: cream fine-knit top, light-khaki straight mini skirt, pale nude/light-skin 15D matte velvet-finish sheer pantyhose, brown loafers, light thin trench draped on one forearm; carry the same modest kraft-paper bouquet. Pantyhose are continuous realistic textile from waist to toes, subtly sheer and matte, never bare legs or bare toes, plastic, latex or wet gloss. Soft cloudy daylight, ordinary public sidewalk and plane trees, no home or office. Natural hands, phone, reflection and floor contact. No readable signage, brands, UI, watermark, garbled letters, face patches/drift, extra fingers, duplicated body parts, distorted legs or broken hosiery.

## Generation settings/result

- generated_at: 2026-10-16
- seed/settings: tool did not expose seed or sampler settings
- output_path: `SOC_LIFESTYLE_001_IMG_02_CAND_01.png`
- output_checksum: `88fbb8865641db323b204ad3395bee5dccfb150575f2b7190e6b00c02953f4c0`
- QA_record: `QA.md`; initial visual review completed, hosiery readability needs user review
