# Social Post Prompt Assembly / Generation Record

- post_id: `SOC_CAMPUS_001`
- image_asset_id: `SOC_CAMPUS_001_IMG_01`
- candidate_id: `SOC_CAMPUS_001_IMG_01_CAND_01`
- model/tool: `OpenAI ImageGen`
- status: `READY_FOR_ONE_CANDIDATE`
- reference_plan: `social_posts/CAMPUS/SOC_CAMPUS_001/images/SOC_CAMPUS_001_IMG_01/REFERENCE_PLAN.md`
- generation_inputs: [`OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001`, `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001`, `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1`, `L0_HOS_30_BM_003`]
- qa_comparison_only: [`OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001`]
- face_generation_rule: use the designated L0-derived face inputs plus the applicable source-derived Face-method prompt constraints; no AI face/body/candidate pixels as generation input

## 1. Everyday moment and composition

One off-guard friend snapshot at a generic university building exit on an ordinary 2018 school day. Camera is held casually around chest height from a few steps away, slightly tilted and a little late to the moment. The adult woman is already walking and talking to an off-camera classmate, one arm holding two books against her side while the other is halfway through settling a backpack strap. She looks toward the companion, not at the camera. Full-body 4:5 vertical frame so the outfit, continuous pantyhose and shoes are naturally visible; the subject is not centered perfectly, and the gesture is unfinished. Keep the face readable in a soft three-quarter view with nose toward image-left, without turning the candid into a posed portrait.

## 2. Identity locks

Generate the adult owner's face from the two declared L0-derived face inputs and the source-derived Face-method constraints only. Preserve the exact source identity, facial feature relationships and natural apparent age; do not de-age, beautify, slim, reshape, enlarge eyes, refine nose or change jaw/chin. The AI Face Canon is QA comparison only after generation. Skin stays natural and warm-neutral without brightening, patchy relighting or makeup contamination.

## 3. Body and appearance locks

Use the face-excluded body derivative only for neck-below scale, body proportions and limb geometry. Preserve natural adult body scale and credible walking anatomy; do not lengthen legs or change waist/hip proportions. Head, face and bangs stay consistent as one natural projection. Hands and fingers hold books and adjust the strap plausibly.

## 4. Outfit and material contract

One complete 2018-inspired casual campus look: a relaxed cream/light-gray knit cardigan over a plain light T-shirt, dark charcoal/navy plaid A-line skirt at a practical everyday length, charcoal-black matte 20D semisheer pantyhose, simple white low-top canvas sneakers and an unbranded navy backpack. The long pantyhose is one continuous textile garment from waist/hips through thighs, knees, calves, ankles, heels, insteps and toes, with closed-toe construction. Let natural skin tone show softly through the 20D fabric; no bare toes, no material breaks, no shiny latex/PVC/plastic/rubber/liquid/body-paint effect. Use the black 30D source only for black hue and matte textile response; it must not make the target opaque or 30D. Clothing is everyday and non-sexualized; no school uniform, logos or deliberate body emphasis.

## 5. Cat, props and scale

No cat or fixed props. Two ordinary textbooks and the plain backpack are temporary props. No legible book text, personal information, brand marks or readable signage.

## 6. Environment and temporary dressing

Generic campus building exit with a few indistinct students far in the background; no recognizable university architecture, school sign, crest or logo. Late-morning natural light with plausible open-shade/doorway contrast. Keep background activity subtle and secondary.

## 7. Carousel continuity-only instructions

This is the first image in the proposed carousel. Only this one candidate is authorized now. Do not generate other images or a contact sheet. Wardrobe, long blunt bangs and 2018 campus context are episode design facts; no previous generated image is supplied as input.

## 8. Realism and negative constraints

2017–2018 phone snapshot character: ordinary wide main-camera perspective around 26–28 mm equivalent, moderate computational auto-HDR, mildly softened fine detail and modest local sharpening, slightly imperfect exposure across doorway/shade, no simulated film grain or fake blur. Keep face and eyes naturally readable; only a little movement softness in the trailing foot, loose hair ends or backpack strap if physically plausible. Avoid portrait-mode cutout bokeh, studio lighting, editorial fashion posing, centered symmetrical composition, staged hand-on-hip pose, eye contact with camera, fashion-catalog smile, pristine perfect alignment, plastic skin, blotches, incoherent shadows, watermark, fake UI, date stamp, text, logos or garbled writing. Do not replicate text/branding from any reference.

## 9. Output contract

- platform: social feed
- aspect ratio/resolution: vertical 4:5, target 2160x2700 px if supported; keep native aspect ratio, never stretch
- required safe areas: keep full head/hair silhouette, books, skirt hem, both legs and shoes within frame with modest edge margins
- expected filename/path: `social_posts/CAMPUS/SOC_CAMPUS_001/images/SOC_CAMPUS_001_IMG_01/candidates/SOC_CAMPUS_001_IMG_01_CAND_01/SOC_CAMPUS_001_IMG_01_CAND_01.png`

## Final assembled prompt

Create exactly one natural, photorealistic 4:5 vertical smartphone snapshot from a generic university building exit on an ordinary 2018 school day. This is a friend’s unplanned candid, not a posed photo: the adult owner is already mid-step and talking to a classmate just off camera, holding two ordinary books against her side while her other hand is halfway through settling a plain backpack strap. She looks toward the companion, never at the camera; catch an unfinished, everyday gesture. Photograph casually from a few steps away at about chest height with an ordinary 26–28 mm-equivalent phone main-camera view. Let her sit slightly off-center in the frame with a small natural camera tilt and imperfect timing. Show her full outfit and both shoes naturally without asking her to display them. Generic campus doorway, soft late-morning daylight and a few distant indistinct students; no identifiable campus, school signs, crest or logos.

Use the supplied deterministic L0-derived face-geometry crop only for the owner’s facial identity and feature geometry, and the supplied L0-derived skin-context crop only for natural skin tone/texture. Follow the project’s source-derived Face-method constraints. Preserve her exact adult identity, facial relationships, skin and apparent age; do not de-age or beautify. Use the face-excluded body derivative only for neck-below body proportions and anatomy. Never use any AI Face Canon, Body Canon or generated image to generate the face.

Her user-authorized L2-only hairstyle for this post is long natural dark-brown hair with straight, clean blunt bangs ending just above the eyebrows and long loose lengths falling past the chest; keep a few separate strands and slight movement from walking, not a salon finish. This is not Hairstyle A or B and must not be blended with either. Outfit: relaxed cream/light-gray knit cardigan over a plain light T-shirt, dark charcoal/navy plaid A-line skirt at a practical everyday length, charcoal-black matte 20D semisheer pantyhose, simple white low-top canvas sneakers and an unbranded navy backpack. Pantyhose are a single continuous textile garment from waist/hips to every toe, closed-toe and matte; natural skin tone is softly visible through the 20D fabric. The black 30D material reference defines only black hue and matte textile surface response, never its denier or opacity. No bare or naked toes, no ankle/instep/heel/toe discontinuity, no latex/PVC/plastic/rubber/liquid/body-paint finish, no deliberate leg posing or sexualized styling.

Render like a 2017–2018 consumer-phone photo with moderate automatic HDR, slightly imperfect doorway exposure, mildly softened fine detail and modest local sharpening. Keep the face readable; at most allow subtle physically plausible movement softness in the trailing shoe, loose ends of hair or backpack strap. No portrait-mode cutout blur, strong film grain, sepia, date stamp, fake app UI, watermark, readable text or branding. Do not copy any reference person, pose, garment or background beyond its declared responsibility. One image only; no sheet, variants or additional carousel frames.

## Generation settings/result

- generated_at: `2026-10-15` (Asia/Shanghai)
- seed/settings: seed unavailable; built-in ImageGen native output
- output_path: `social_posts/CAMPUS/SOC_CAMPUS_001/images/SOC_CAMPUS_001_IMG_01/candidates/SOC_CAMPUS_001_IMG_01_CAND_01/SOC_CAMPUS_001_IMG_01_CAND_01.png`
- output_checksum: `dc3f1f961cd19ba6f228d5bd8d6cfd39bb33ecabead538b661001a6081e46880`
- QA_record: `social_posts/CAMPUS/SOC_CAMPUS_001/images/SOC_CAMPUS_001_IMG_01/qa/QA.md` (visual QA recorded; user review pending)
