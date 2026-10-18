# Social Post Prompt Assembly / Generation Record

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_01`
- candidate_id: `SOC_OUTFIT_002_IMG_01_CAND_01`
- model/tool: OpenAI ImageGen
- status: CANDIDATE_GENERATED_REVIEW_REQUIRED
- reference_plan: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_01/REFERENCE_PLAN.md`
- generation_inputs: `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` (neck-below geometry only); `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` (clothing fit/drape and matte-white hosiery only)
- qa_comparison_only: none (face not visible)
- face_generation_rule: no face appears; body image is deterministic face-excluded

## 1. Everyday moment and composition

A seated forest-park picnic selfie, photographed by the owner with the phone held above her lap and angled down toward the blanket below her. Crop from waist/skirt to both hosiery-covered feet, with no head or face. Her legs rest comfortably together and turned to one side, extending diagonally over an orange picnic blanket. Show surrounding grass clearly and a small spread of picnic food on the mat. A hand/forearm may enter near the edge to make the handheld selfie perspective legible; phone itself stays outside frame. Natural 4:5 portrait composition.

## 2. Identity locks

No face, head, hair or identity features in frame. Do not synthesize a partial face, reflection or portrait.

## 3. Body and appearance locks

The face-excluded body derivative defines only neck-below proportions and leg shape. Preserve natural leg alignment and volume; do not lengthen, thin, bow or stylize the legs. Relaxed seated contact with blanket and grass.

## 4. Outfit and material contract

Autumn 02: dark chocolate-brown tailored blazer only if a natural sleeve edge enters frame; high-waisted dark chocolate-brown crisp pleated mini skirt visible over upper thighs. Soft-white medium-thick matte pantyhose continuously covers waist/hips, thighs, knees, calves, ankles, heels, insteps and closed toes wherever visible. No shoes per user instruction. Barefoot means no footwear, not bare skin. Do not show naked toes, stocking boundary, seams, plastic/latex sheen, or discontinuity.

## 5. Cat, props and scale

No cat or fixed props. Temporary items: one orange picnic blanket on grass; modest unbranded picnic food such as a pastry and fruit, plus optional closed thermos. Keep item count small and natural; believable contact, scale and shadows. No readable packaging or logos.

## 6. Environment and temporary dressing

Generic public forest-park clearing in autumn, textured grass around the blanket, scattered fallen leaves at the edge, softly visible tree trunks in the background. No identifiable park, signage, or residence.

## 7. Carousel continuity-only instructions

This image and IMG_02 are independently generated. Only the same outing, Autumn 02 garments and no-shoes/continuous-white-hosiery choice are shared. Do not use another image as input.

## 8. Realism and negative constraints

Candid phone selfie, credible top-down camera perspective, naturally rumpled blanket, real grass contact and clothing folds. Keep picnic objects secondary to the requested outfit/setting. No sexualized pose, no studio look, no synthetic symmetry, no distorted legs/feet, no extra/missing toes, no floating props, no broken hosiery, no plastic fabric, no text/logo/UI/watermark, no face or private-home cues.

## 9. Output contract

- platform: social feed carousel draft
- aspect ratio/resolution: vertical 4:5, native image dimensions recorded after generation
- expected filename: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_01/candidates/SOC_OUTFIT_002_IMG_01_CAND_01/SOC_OUTFIT_002_IMG_01_CAND_01.png`

## Generation settings/result

- generated_at: 2026-10-17
- seed/settings: not exposed by ImageGen; native 1122×1402 PNG, approximately 4:5
- output_path: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_01/candidates/SOC_OUTFIT_002_IMG_01_CAND_01/SOC_OUTFIT_002_IMG_01_CAND_01.png`
- output_checksum: `133d82eabcbc11c37e314bb63c51ad20e851f683b5a10278b11e8e5a079d6c7e`
- QA_record: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_01/qa/QA.md` (pending)
