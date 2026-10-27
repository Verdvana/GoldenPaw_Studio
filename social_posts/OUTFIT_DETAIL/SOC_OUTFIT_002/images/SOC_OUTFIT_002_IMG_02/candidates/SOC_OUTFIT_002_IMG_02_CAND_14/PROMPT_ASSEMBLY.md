# Social Post Prompt Assembly / Generation Record

- candidate_id: SOC_OUTFIT_002_IMG_02_CAND_14
- status: REVIEW_REQUIRED
- model/tool: OpenAI ImageGen built-in
- generation_inputs: five scoped sources in GENERATION_RECORD.json
- qa_comparison_only: approved Face Canon; never attached
- seed/settings: not exposed
- output_path: SOC_OUTFIT_002_IMG_02_CAND_14.png
- QA: REVIEW_REQUIRED; see QA.md

## Final assembled prompt

Use case: photorealistic-natural. Create ONE vertical 4:5 candid autumn picnic social-post photograph, a direct handheld FRONT-CAMERA SELFIE taken by the adult woman herself while lying prone on the picnic blanket. This is the photo from her outstretched phone, not a photograph of her taking a selfie. No mirror.

STRICT SCOPED INPUT ROLES, in attached order:
1: real-source face geometry crop. Sole authority for facial identity and feature relationships, not makeup, retouch or hairstyle.
2: real-source skin context crop. Natural warm-neutral skin tone/texture only, not hair, clothing or fine geometry.
3: approved face-excluded body derivative. Neck-below body/limb proportions only. Ignore calibration swimsuit, hosiery, hair and background.
4: approved face-excluded Autumn 02 clothing derivative. Clothing construction, fit/drape and matte-white hosiery only. Ignore hair, depicted body proportions, skin, studio, and slippers.
5: approved FIRST PICNIC SHOT, CONTINUITY ONLY. Match this exact rust-orange woven textured picnic blanket, grass with golden fallen leaves, croissant and cookie on crumpled brown paper, green grapes and red apple, their relative grouping, and warm afternoon light direction. It must NOT define woman identity, face, skin, body, hair, clothing construction or hosiery material. This is a fresh parallel-source generation with a new prone pose.

ACTION AND CAMERA, essential: She lies on her stomach, abdomen/hips and both THIGHS resting naturally on the orange picnic blanket. BOTH knees are bent roughly 90 degrees so both LOWER LEGS rise approximately vertically from the knees. Ankles are loose, with feet naturally drooping gently, not stiff pointed ballet toes. Thighs stay down. One bent forearm/elbow supports the raised upper torso. Her OTHER arm extends out and slightly above the side of her head holding the phone just outside the frame. Use a physically reachable wide-angle selfie camera position, pointing diagonally backward down the length of her clothed torso toward her skirt, thighs and the raised lower legs/feet. The reaching sleeve/arm enters from the near frame edge with plausible selfie foreshortening. Show her clothed body and both raised lower legs in a readable composition, not a third-person photographer's view. A partial face appears cropped by the near SIDE edge: one eye, cheek and part of the mouth, with the rest outside the image, as an informal close selfie. Keep this secondary to the body and picnic scene. Do not display her whole face, a phone hiding her face, a mirror or a second photographer. Keep whole-body context and picnic setting balanced with the raised legs; do not make a foot close-up.

WARDROBE from input 4: dark chocolate-brown tailored blazer, fitted ivory ribbed high-neck knit, dark-brown pleated short skirt that hangs/rests naturally and keeps full coverage, medium-thick soft-white MATTE pantyhose. NO SHOES in this picnic shot. Pantyhose is one continuous knit garment, including knees, calves, ankles, heels, insteps and closed toe tips. Use the approved matte white fabric response including fabric tension over toe tips. No bare toes, separate socks, leggings, or abrupt ankle transitions. No plastic, latex or wet sheen. Do not force nail polish through opaque fabric. Keep skirt coverage normal and casual, no lifted skirt, exposed underwear or exaggerated hip arch.

Keep natural adult body proportions from input 3. On visible face preserve source identity, original face width and natural eye/nose/lip/jaw relationships, warm-neutral skin without beautification, eye enlargement, face slimming, whitening, smoothing, muddy relighting, patches or blotches. Adapt normal facial projection to the actual selfie camera. Hair must obey gravity with prone pose, not a standing cutout.
Surroundings remain the SAME picnic spot and SAME blanket/snack group from input 5. Camera angle changes but object relationships remain coherent. The food remains beside her on the blanket, not under her torso/elbow. Autumn grass and fallen golden leaves at edges. Warm real afternoon sunlight and soft coherent shadows. Natural handheld casual photo, believable contact and fabric wrinkles, anatomically consistent knees/ankles/feet/hands, exactly one person, two legs, no duplicated body. No artificial UI, text, watermark, logos, studio backdrop, road mirror, café door, evening lighting or added props.
Output exactly one image, target portrait 4:5. This is an L3 REVIEW_REQUIRED candidate, not an approved asset.
HAIRSTYLE_A is specified in text from the approved method: long straight loose dark-brown hair, short near-center naturally imperfect part, low close-to-scalp roots, modest face-framing strands, tapered ends; adapt fall to gravity. No hairstyle B or blend.


PRIMARY REVISION FOR THIS NEW CANDIDATE — FEET AND ANKLES: Keep the thighs resting on the blanket and lower legs upright. The feet must NOT continue vertically upward in line with the shins. Let both feet bend loosely at the ankles under gravity, each foot projecting toward her back/head with its forefoot and toe end visibly lower than its heel. Show an easy approximately right-angle transition between shin and foot with a soft slightly downward droop at the forefoot. Ankles are limp, toes relaxed, no dancer-like plantar extension or toe clenching. One may droop slightly more than the other. Frame feet in three-quarter SIDE profile so the narrow instep, heel-to-arch transition and slender forefoot are readable, not broad full soles presented to camera. Foot length/width stays naturally proportioned to the approved slender ankles and body: relatively narrow adult feet, no swollen/puffy insteps, thick balloon-like rounded toes, oversized heels or chunky cylindrical feet. Keep toes enclosed by the same continuous matte-white hosiery with a subtle natural toe outline; do not exaggerate toe details. The ankle remains anatomically connected and smooth, not sharply broken. This foot relaxation and natural narrowness is the main required change. Preserve the picnic selfie concept, warm light, source-approved wardrobe, slim natural body proportions, partial face crop, mat and grouped snacks.

## Generation result

- generated_at: 2026-10-27
- dimensions: 1122 x 1402
- output_path: social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_02/candidates/SOC_OUTFIT_002_IMG_02_CAND_14/SOC_OUTFIT_002_IMG_02_CAND_14.png
- SHA-256: d6c8ae9f544fe33cb203fc461c1f2865498971a651585615fe18b9d79607f609
- status: REVIEW_REQUIRED; no automatic approval or downstream use

## User approval — 2026-10-27

User accepted with “好” and moved to third image. Approved L3 only. Current authoritative image: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_02/approved/SOC_OUTFIT_002_IMG_02_APPROVED_v1.png`; SHA-256 `d6c8ae9f544fe33cb203fc461c1f2865498971a651585615fe18b9d79607f609`. Original candidate raster moved, not copied. Earlier QA observations remain historical.
