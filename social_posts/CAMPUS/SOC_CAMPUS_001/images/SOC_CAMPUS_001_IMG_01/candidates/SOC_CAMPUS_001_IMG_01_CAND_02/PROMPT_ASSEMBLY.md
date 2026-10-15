# Prompt Assembly — SOC_CAMPUS_001_IMG_01_CAND_02

- post_id: `SOC_CAMPUS_001`
- image_asset_id: `SOC_CAMPUS_001_IMG_01`
- candidate_id: `SOC_CAMPUS_001_IMG_01_CAND_02`
- model/tool: `OpenAI ImageGen`
- status: `READY_FOR_ONE_REVISED_CANDIDATE`
- generation_inputs: [`OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001`, `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001`, `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1`, `L0_HOS_30_BM_003`]
- qa_comparison_only: [`OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001`]
- face_generation_rule: source-derived L0 inputs and Face-method constraints only; no AI Face Canon or previous generated image as generation input

## Face correction

Keep the exact facial identity from the L0 geometry crop. Match the approved textual identity description without stylizing it into a generic influencer face: soft oval to gently rounded-oval outline; naturally soft, moderately full cheeks; cheekbones not prominent; jaw gently narrows into a rounded, non-pointed chin; medium naturally almond-shaped eyes with modest natural asymmetry and coordinated spacing; gently shaped natural brows; a natural, not overly high nose bridge with a soft rounded tip and restrained nostril width; natural lips. Do not narrow or sharpen the face, enlarge the eyes, refine the nose, point the chin, beautify, de-age, or copy the source photo’s makeup/retouching. Keep facial identity grounded in the provided real-source derivative; Face Canon is post-generation QA only.

## Keep the approved look

Exactly preserve the accepted wardrobe concept from Candidate 01 as text: relaxed cream knit cardigan, plain light T-shirt, dark charcoal/navy plaid A-line skirt, charcoal-black matte semisheer 20D pantyhose, white low-top canvas sneakers and plain navy backpack. Keep the same generic campus doorway and 2018 consumer-phone aesthetic. Do not use Candidate 01 pixels as an image reference.

## Revised prompt

Create exactly one photorealistic 4:5 vertical candid smartphone photo at a generic university building exit on an ordinary 2018 school day. An adult East Asian woman is caught mid-step while talking to a classmate just beside the camera. She glances toward the classmate, not into the lens. One arm holds two ordinary books at her side; the other hand is casually adjusting one backpack strap. The instant feels genuinely unplanned, with a slightly imperfect camera tilt and timing, not an editorial pose or fashion shoot. Keep the full figure, head, legs and both shoes inside frame with safe space below the soles. Frame her large enough that her face is clearly readable; keep her a little off-center. Natural late-morning doorway light, ordinary background activity, generic campus architecture without signs, crests, logos or legible writing.

Use the supplied L0-derived face-geometry crop as the sole authority for her exact facial identity and feature relationships, following the source-derived Face-method constraints. Use the separate L0-derived skin crop only for natural skin tone and texture. Use the supplied face-excluded body derivative only for neck-below body proportions and walking anatomy. After generation, the approved left-three-quarter Face Canon may be used only for QA comparison; it is not a generation input. Face details must stay close to the owner’s natural source identity: soft oval/rounded-oval facial outline, natural softly full cheeks, gentle cheekbones, softly narrowing jaw and rounded chin, medium natural almond eyes with their modest natural asymmetry, relaxed natural brows, a natural nose bridge and soft rounded tip, and natural lips. Do not make her face slimmer, sharper, more symmetrical, more doll-like or younger; no beauty-filter skin, exaggerated lashes, heavy makeup or generic face replacement.

Hair is this post’s user-authorized L2 design: long, dark-brown, fully loose hair with clean straight bangs just above the eyebrows. All hair stays down; no ponytail, bun, half-up twist, clip, braid or tied crown. A few ends may move naturally with her walking. Keep it distinct from Hairstyle A and B, without blending them.

Keep the accepted outfit: relaxed cream knit cardigan over a plain light T-shirt, dark charcoal/navy plaid A-line skirt at a practical everyday length, charcoal-black matte 20D semisheer pantyhose, simple white low-top canvas sneakers and an unbranded navy backpack. The pantyhose are continuous textile from waist/hips down both legs and over heels, insteps and toes, with closed-toe construction; softly visible skin tone through the 20D material, never bare/naked toes or a break at ankle/heel/instep. Use the black 30D matte reference only for black hue and matte fabric response; it must not make the 20D target opaque or thicker. No latex/PVC/plastic/rubber/liquid/body-paint finish and no sexualized styling.

Render like a 2017–2018 consumer-phone main-camera snapshot with ordinary wide perspective, moderate automatic HDR, slightly imperfect doorway exposure, mild local sharpening and naturally imperfect framing. Keep the face readable and recognizable. No fake film grain, sepia, date stamp, portrait-mode cutout blur, watermark, fake UI, logo, readable text or copied reference background/person. One image only; no contact sheet, variations or other carousel frames.

## Output contract

- platform: social feed
- aspect ratio/resolution: 4:5, native size if exact 2160x2700 unavailable; do not stretch
- output path: `social_posts/CAMPUS/SOC_CAMPUS_001/images/SOC_CAMPUS_001_IMG_01/candidates/SOC_CAMPUS_001_IMG_01_CAND_02/SOC_CAMPUS_001_IMG_01_CAND_02.png`
- QA: `social_posts/CAMPUS/SOC_CAMPUS_001/images/SOC_CAMPUS_001_IMG_01/candidates/SOC_CAMPUS_001_IMG_01_CAND_02/QA.md`
