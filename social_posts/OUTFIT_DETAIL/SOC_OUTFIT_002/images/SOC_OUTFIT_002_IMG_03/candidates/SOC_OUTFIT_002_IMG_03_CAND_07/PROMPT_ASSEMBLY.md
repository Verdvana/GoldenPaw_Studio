# Prompt Assembly / Generation Record — IMG_03 Candidate 06

- tool: OpenAI ImageGen
- status: GENERATED; REVIEW_REQUIRED
- candidate: `SOC_OUTFIT_002_IMG_03_CAND_07`
- generation_inputs: source-derived face geometry crop (identity/feature geometry only), source-derived skin-context crop (skin color/texture only), face-excluded body derivative (neck-below proportions only), Autumn 02 clothing design reference (garment design only), Autumn 02 worn-front reference (white matte pantyhose and continuous sole/toe coverage only)
- qa_comparison_only: approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` only; never a generation input
- reference budget: five images, maximum five accepted by ImageGen tool
- seed/settings: not exposed by ImageGen
- output path: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_03/candidates/SOC_OUTFIT_002_IMG_03_CAND_07/SOC_OUTFIT_002_IMG_03_CAND_07.png`
- output checksum: `c1b62d73ddc4c0060b9984344ab7914feec4af4d42735fa7d528deefc2a92716`; dimensions: 1122x1402 PNG (approximately 4:5)
- QA: `../qa/QA_CAND_07.md`; visual QA confirms continuous white textile over visible sole surfaces; awaiting user review

## Final assembled prompt

A casual, candid autumn fashion selfie, vertical 4:5 phone photo, at a public forest park. An adult woman wears the referenced brown blazer, ivory knit top, pleated skirt and opaque matte white tights. She is relaxing on her stomach on an orange picnic mat, upper body lifted on her elbows, taking a handheld front-camera selfie angled down the length of her outfit. Keep the established composition: the face is almost entirely cropped out, only a tiny edge sliver visible; her outfit, body and legs are the focus. Knees bent, lower legs lifted straight upward so the calves are vertical relative to the ground, feet raised above them in a playful stretch. No shoes.

Keep the tights visibly thick, opaque and fabric-like, with a soft matte textile surface. They cover legs and feet continuously. Most of each foot remains opaque white; only the very tips of the toes and the heel may look slightly more sheer where the fabric stretches, but remain fully covered. No skin-like smooth white soles. Natural anatomy and proportions.

Autumn trees, fallen leaves, grass, orange mat and simple picnic snacks. Natural daylight, realistic unposed phone snapshot, no studio finish. Use the source-derived face crops only for the small visible face area; use the body derivative only for body proportions; use outfit references only for clothing and hosiery appearance. Keep Hairstyle A. Do not use previous candidate images as input. No stand, other photographer, text, logos, signage, UI or watermark.

Attempt 1 was rejected by the ImageGen output safety system (sexual category); no image was returned. The successful retry used this broader everyday fashion-photo description. Seed/settings were not exposed by ImageGen.
