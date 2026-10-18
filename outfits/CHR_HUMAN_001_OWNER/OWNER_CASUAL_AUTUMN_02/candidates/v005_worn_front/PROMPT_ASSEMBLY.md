# Prompt Assembly — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v005

- model/tool: built-in ImageGen
- status: `READY_FOR_SINGLE_GENERATION`
- reference_plan: `REFERENCE_PLAN.md`
- generation_inputs: `5` (listed in `generation_record.md`)
- qa_comparison_only: `3` (not supplied to generator)
- face_generation_rule: source-derived L0 inputs plus `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`; AI Face Canon is QA-only

## Final assembled prompt

Create one independent photorealistic L2 outfit fit-validation image, exact 3:4
portrait, full body from head to both feet, on a neutral light-gray seamless studio
background with soft even neutral light. The owner stands naturally and directly
front-facing, head upright, neutral closed-mouth expression and gaze at camera; both
feet fully visible and supported. Use the L0-derived face geometry crop and L0 skin
context crop only to generate the face under the source-derived
`OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` constraints: preserve the same adult woman's
recognizable natural feature relationships, face shape, warm-neutral skin tone and
texture; no beautification, reshaping, whitening, cooling, smoothing, identity drift,
blotches, patches, smudges or muddy relighting. Never use an AI Face Canon, AI Body
Canon, previous candidate or generated image as a face input. Use the face-masked
DSC00847 derivative only for Hairstyle A: long, straight, loose dark-brown hair,
near-center naturally imperfect part, very low restrained crown, fine face-framing
strands and tapered ends. No Hairstyle B, curls, bun, ponytail or hybrid. Use the
deterministic face-excluded body derivative only for neck-below body proportions,
front stance and foot scale; do not reshape or slim the body.

Dress the owner exactly in the approved v005 outfit: tailored dark chocolate brown
blazer with classic notched lapels and long sleeves; fitted ivory fine-ribbed
high-neck knit top; high-waisted dark chocolate brown mini skirt with crisp, even
pleats; pale sheer matte hosiery; cream ivory plush fuzzy open-toe mule slippers with
a low flat sole. Keep blazer, knit and pleated skirt textures realistic and garment
silhouettes faithful to the approved design. Hosiery is continuous matte textile
from waist/hips through thighs, knees, calves, ankles, heels, insteps and closed toes.
Through the open slipper toe area, show the same hosiery-covered toes with subtle
natural show-through; never bare toes or skin gaps. It must not look like latex, PVC,
plastic, rubber, liquid coating, wet gloss or body paint. Do not add accessories,
logos, readable text, watermark, props, collage, extra person or extra anatomy.

Use the outfit reference only for garments; the body derivative only below the neck;
the hair derivative only for Hairstyle A; the L0-derived face inputs only for face
generation. Do not copy face/body/pose/lighting/background from the outfit image.
Generate one candidate only. Status after generation is `REVIEW_REQUIRED`; not Canon.

## Generation settings/result

- generated_at: `2026-10-17`
- seed/settings: `not exposed by ImageGen`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v005_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v005.png`
- output_checksum: `pending`
- QA_record: `generation_record.md`
