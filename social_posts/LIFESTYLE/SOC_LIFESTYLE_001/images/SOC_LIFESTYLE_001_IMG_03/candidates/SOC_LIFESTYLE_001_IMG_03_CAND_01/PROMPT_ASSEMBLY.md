# Social Post Prompt Assembly — SOC_LIFESTYLE_001_IMG_03_CAND_01

- post_id: SOC_LIFESTYLE_001
- image_asset_id: SOC_LIFESTYLE_001_IMG_03
- candidate_id: SOC_LIFESTYLE_001_IMG_03_CAND_01
- model/tool: OpenAI ImageGen
- status: GENERATED_REVIEW_REQUIRED
- reference_plan: `REFERENCE_PLAN.md`
- generation_inputs: source-derived face/skin crop; masked L0 Hairstyle-A derivative; face-excluded body derivative; scoped hosiery material crop
- qa_comparison_only: approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` after generation only
- face_generation_rule: source-derived L0 inputs plus applicable Face method prompt constraints; AI Face/Body Canon is QA-only

## 1. Everyday moment and composition

The owner is taking one final full-body phone selfie in the flower-shop window reflection as she starts to walk away. One foot is naturally stepping forward, the bouquet rests in her opposite arm, and her phone is visibly held at chest height. Capture full body including shoes and continuous tights, with casual slightly off-center framing.

## 2. Identity locks

Generate face from source-derived face/skin input only, applying `FACE_01_FRONT_NEUTRAL_METHOD.md`. Use the masked L0 hair image only for HAIRSTYLE_A. No previous AI image may define face or hair.

## 3. Body and appearance locks

Use the face-excluded body derivative for neck-below proportions only. Keep natural adult build, plausible step biomechanics and realistic limb lengths.

## 4. Outfit and material contract

Same cream lightweight fine-knit top, light-khaki straight mini skirt, pale nude/light-skin 15D matte velvet-finish sheer pantyhose, brown loafers, and thin light trench carried over one forearm. Pantyhose must be visibly textile-sheer and continuous across both legs and covered feet; no bare legs/toes, latex, PVC, plastic or oily gloss.

## 5. Cat, props and scale

No cat. Plain smartphone in one hand, bouquet in the opposite arm, natural scale and grip.

## 6. Environment and temporary dressing

Same generic flower-shop frontage and plane-tree sidewalk, cloudy afternoon, no home or office. Window reflection is the only framing device; no readable signage or logos.

## 7. Carousel continuity-only instructions

Text-only continuity: outfit, time/weather, bouquet and shop street. Previous images are not image inputs and define no identity, body, hair, hosiery, props or residence.

## 8. Realism and negative constraints

Photographic, plausible handheld reflection and walking weight transfer. Correct number and placement of fingers, phone, legs and shoes. Natural floor contact and consistent soft overcast reflections. No face patches/drift, over-smoothing, hosiery breaks, bare toes, extra limbs, floating feet, garbled text, logos, UI or watermark.

## 9. Output contract

- platform: social feed
- aspect ratio/resolution: vertical 4:5, native portrait generation closest available
- required safe areas: face, phone, bouquet, stepping foot and tights/shoes all remain within central 90%
- expected filename/path: `SOC_LIFESTYLE_001_IMG_03_CAND_01.png` in this candidate directory

## Final assembled prompt

Generate exactly one photorealistic vertical 4:5 candid full-body handheld smartphone reflection selfie of the adult owner taking one last picture as she begins walking away from a small generic flower shop onto a Shanghai plane-tree sidewalk on a softly cloudy autumn afternoon. Earlier carousel images provide text-only continuity for the outfit, bouquet, cloudy afternoon and public flower-shop street; they are not visual references. Show the owner holding a plain phone at chest height in the broad shop-window reflection, face visible beside the phone, and one foot naturally stepping forward. Full body from head through both brown loafers must fit. Preserve the owner's face and warm-neutral skin only from the source-derived face/skin input under the applicable source-derived Face method. Use the masked L0 reference solely for HAIRSTYLE_A, long straight loose dark-brown hair, near-center part, tapered ends. Use the face-excluded body derivative only for neck-below proportions and natural limb geometry. Same outfit: cream lightweight fine-knit top, light-khaki straight mini skirt, pale nude/light-skin 15D matte velvet-finish sheer pantyhose, brown loafers, light trench draped over one forearm; same modest bouquet in kraft paper. Make the pantyhose visibly fine sheer textile, matte, continuous over both legs, ankles and covered toes, not bare skin, latex, PVC, plastic or wet gloss. Natural walking balance, plausible phone grip and reflection, correct shoe contact, soft overcast daylight, ordinary public sidewalk. No home/office, readable text, logos, UI, watermark, garbled letters, face identity drift, face patches, extra fingers/limbs, distorted legs or hosiery discontinuities.

## Generation settings/result

- generated_at: 2026-10-16
- seed/settings: tool did not expose seed or sampler settings
- output_path: `SOC_LIFESTYLE_001_IMG_03_CAND_01.png`
- output_checksum: `43b5b6c7487158d889eb23ff51f83c5aeb51f2eeaf83a7ce2dc0f2b6ae294353`
- QA_record: `QA.md`; initial visual review complete, awaiting user decision
