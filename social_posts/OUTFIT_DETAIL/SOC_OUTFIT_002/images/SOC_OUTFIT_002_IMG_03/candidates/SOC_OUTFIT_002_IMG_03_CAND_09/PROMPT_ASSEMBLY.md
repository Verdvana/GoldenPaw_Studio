# Prompt Assembly / Generation Record — IMG_03 Candidate 06

- tool: OpenAI ImageGen
- status: GENERATED; REVIEW_REQUIRED
- candidate: `SOC_OUTFIT_002_IMG_03_CAND_09`
- generation_inputs: source-derived face geometry crop (identity/feature geometry only), source-derived skin-context crop (skin color/texture only), face-excluded body derivative (neck-below proportions only), Autumn 02 clothing design reference (garment design only), Autumn 02 worn-front reference (white matte pantyhose and continuous sole/toe coverage only)
- qa_comparison_only: approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` only; never a generation input
- reference budget: five images, maximum five accepted by ImageGen tool
- seed/settings: not exposed by ImageGen
- output path: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_03/candidates/SOC_OUTFIT_002_IMG_03_CAND_09/SOC_OUTFIT_002_IMG_03_CAND_09.png`
- output checksum: `b50c42e54cb46ec5fe2b74f2b2e3239d21c669afa7863ccfdd8dc428284c85dc`; dimensions: 1122x1402 PNG (approximately 4:5)
- QA: `../qa/QA_CAND_09.md`; visual QA confirms continuous white textile over visible sole surfaces; awaiting user review

## Final assembled prompt

A casual autumn forest-park outfit selfie, vertical 4:5 phone snapshot. An adult woman wears the brown blazer, ivory knit, pleated skirt and thick white matte tights. She rests on her stomach on an orange picnic blanket, supported on her elbows, taking a handheld front-camera selfie angled along her outfit. Her face is nearly outside the frame, only a tiny edge glimpse. Knees bent, lower legs lifted upright in a relaxed stretch. She gently flexes her ankles so the toes draw up toward the top of the feet, with the toe ends bending upward rather than tucked under. Keep the foot pose natural. The white tights are opaque and fabric-like over legs and toes; only the heel panel is a little more sheer from stretch, still covered by hosiery. No shoes.

Autumn trees, fallen leaves, grass, orange mat and simple picnic snacks. Natural light, candid unposed fashion photo. Use source-derived face crops only for the tiny visible face area, body derivative for proportions, outfit references for clothing and tights. Keep Hairstyle A. No prior candidate input, stand, second photographer, text, logos, signage, UI or watermark.

Attempt 1 was rejected by the ImageGen output safety system (sexual category); no image was returned. The successful retry used this concise everyday styling prompt. Seed/settings were not exposed by ImageGen.
