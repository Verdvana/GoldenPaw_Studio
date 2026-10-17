# Social Post Prompt Assembly — SOC_LIFESTYLE_001_IMG_01_CAND_01

- post_id: SOC_LIFESTYLE_001
- image_asset_id: SOC_LIFESTYLE_001_IMG_01
- candidate_id: SOC_LIFESTYLE_001_IMG_01_CAND_01
- model/tool: OpenAI ImageGen
- status: GENERATED_REVIEW_REQUIRED
- reference_plan: `REFERENCE_PLAN.md`
- generation_inputs: source-derived face/skin crop; face-masked L0 Hairstyle-A derivative; face-excluded body derivative; scoped L0 hosiery material crop
- qa_comparison_only: approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` (after generation only)
- face_generation_rule: source-derived L0 inputs plus `FACE_01_FRONT_NEUTRAL_METHOD.md` constraints; AI Face/Body Canon is QA-only

## 1. Everyday moment and composition

A believable casual front-camera selfie made by the adult owner herself just outside a small unbranded flower shop on a plane-tree Shanghai sidewalk on a softly overcast warm autumn afternoon. One arm is naturally extended holding a modern plain smartphone; the phone and hand are visibly reflected in a nearby shop window, making the handheld capture unmistakable. The other arm cradles a modest bouquet wrapped in plain kraft paper. Slightly imperfect selfie framing, mild natural perspective, head through mid-thigh crop, enough lower frame to clearly show the skirt and sheer pantyhose. Background softly legible, not staged.

## 2. Identity locks

Use only the source-derived face geometry/skin reference for face and skin; preserve the real adult woman's natural feature relationships, age and warm-neutral skin. Use the masked L0 reference only for HAIRSTYLE_A: long, straight, loose dark-brown hair, near-center part, slim face-framing strands and tapered ends. Natural relaxed expression. Do not copy the mask or its gray area.

## 3. Body and appearance locks

Body derivative defines only neck-below proportions, limbs and natural adult physique. No slimming, leg lengthening, body reshaping, extra fingers or distorted phone grip.

## 4. Outfit and material contract

Cream fine-knit light top, light-khaki straight mini skirt, pale nude/light-skin 15D matte velvet-finish sheer pantyhose, brown loafers (visible only if crop naturally allows), light thin trench draped over one forearm. The pantyhose are a continuous fine textile, subtly visible over the thighs, never bare legs, plastic, latex, oily or wet. Keep clothing natural for a 22–26°C cloudy Shanghai day.

## 5. Cat, props and scale

No cat. Plain smartphone with realistic hand grip, no visible logo, screen UI or text. One natural bouquet in unmarked kraft paper.

## 6. Environment and temporary dressing

Generic small neighborhood flower shop entrance, plane-tree sidewalk, softly overcast daylight, faintly damp pavement, ordinary urban street. No home or office. No readable signs, brand names or fabricated lettering.

## 7. Carousel continuity-only instructions

None; this is image 01. Outfit, time, bouquet and location are design facts for this post only.

## 8. Realism and negative constraints

Photographic realism, physically consistent overcast reflections and contact shadows, natural skin texture, textile rendering and believable selfie geometry. No extra or fused fingers, duplicated phone, mirrored text, face drift, muddy or bright/dark face patches, makeup-heavy beauty filter, plastic skin, bare-leg break, hosiery discontinuity, latex/PVC/rubber, watermark, fake UI or garbled text.

## 9. Output contract

- platform: social feed
- aspect ratio/resolution: vertical 4:5, native portrait generation closest available
- required safe areas: face, phone, bouquet, skirt and visible hosiery remain within central 90%
- expected filename/path: `SOC_LIFESTYLE_001_IMG_01_CAND_01.png` in this candidate directory

## Final assembled prompt

Generate exactly one photorealistic vertical 4:5 candid smartphone front-camera selfie, captured by the adult owner herself just outside a small generic flower shop on a Shanghai plane-tree sidewalk on a softly overcast warm autumn afternoon. Her own arm is naturally extended holding a plain modern phone; show the phone and hand in a nearby shop-window reflection so it is clearly a hand-held selfie, with authentic mild selfie perspective and slightly imperfect casual framing. Her other arm carries a modest seasonal bouquet in plain kraft paper. Crop from head to mid-thigh so the outfit and sheer hosiery are unmistakably visible. Preserve the adult woman's face and warm-neutral skin strictly from the source-derived face/skin input, following the face method constraints; do not use AI face/body imagery to generate her face. Apply only the supplied face-masked L0 reference for HAIRSTYLE_A: long straight loose dark-brown hair, near-center part and tapered ends. Apply the face-excluded body derivative only for neck-below body proportions. Dress her in a cream fine-knit light top, light-khaki straight mini skirt and pale nude/light-skin 15D matte velvet-finish sheer pantyhose, with a light thin trench draped over one forearm. Pantyhose are real fine textile with subtle visible presence and continuous coverage, not bare skin, plastic, latex or wet gloss. Soft natural overcast light, plane trees and a faintly damp ordinary sidewalk; no home or office. Keep hands, phone, face, bouquet and outfit anatomically coherent. No readable text, signs, brands, UI, watermark or garbled lettering. No beauty filter, face identity drift, dark/bright/muddy face patches, plastic skin, extra fingers, distorted phone, hosiery discontinuity or synthetic fashion-campaign posing.

## Generation settings/result

- generated_at: 2026-10-16
- seed/settings: tool did not expose seed or sampler settings
- output_path: `SOC_LIFESTYLE_001_IMG_01_CAND_01.png`
- output_checksum: `5d8d5254006fba1698733512659a044fa9e10d3a149b56dab8405ee023a5253c`
- QA_record: `QA.md`; initial visual review complete, awaiting user review/approval
