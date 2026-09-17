# Generation Record

- asset_id: `OWNER_CASUAL_SUMMER_01_WORN_FRONT`
- outfit_id: `OWNER_CASUAL_SUMMER_01`
- level: `L2`
- candidate_version: `v002`
- status: `REVIEW_REQUIRED`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/candidates/v002_worn_front/OWNER_CASUAL_SUMMER_01_WORN_FRONT_v002.png`
- use_case: `identity-preserve`
- reference_budget: `4 images; outfit, face-excluded body, source-derived face, masked Hairstyle-A`
- retry_reason: `v001 failed hosiery toe coverage and interdigital tension QA`

## Generation inputs

- `OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE`: latest generated outfit design; clothing/accessory styling only, not face, skin, body, hair, or identity.
- `OWNER_BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v3`: body proportions and front stance only; no face, hair, clothing, or hosiery authority.
- `B_FACE_SKIN_CONTEXT_NO_CROWN`: Face method source-derived input for face identity, facial-feature relationships, and warm-neutral skin tone only.
- `DSC00847_HAIR_ONLY_MASKED`: masked L0 Hairstyle-A source for hair only.

## QA comparison only

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`: post-generation comparison only; never a generation input.

## Prompt assembly

Use case: identity-preserve
Asset type: L2 worn-front outfit fit-validation image
Primary request: regenerate a full-body frontal neutral standing adult owner in the same summer casual outfit, preserving the source-derived Face method and body proportions while correcting the hosiery feet.
Input images: outfit design, face-excluded body derivative, B-derived face/skin context, and masked Hairstyle-A source, each used only for its declared responsibility.
Composition/framing: exact 3:4 portrait, eye-level frontal camera, full body and both feet fully visible, relaxed symmetric stance.
Materials/textures: one continuous light nude sheer micro-sheen pantyhose extends from waist over thighs, calves, ankles, heels, insteps, and the entire toe area. The hosiery is visibly present as a translucent fabric membrane over every individual toe. Burgundy toenail polish is visible only as soft blurred wine-red shapes beneath the fabric, with no exposed nail plate or bare toe skin. Add clear fabric tension arcs and shallow converging valleys between adjacent toes; these are hosiery folds, not open toe gaps. No toe-cap line, white ring, or hard boundary.
Constraints: keep the white floral camisole, light-blue high-waisted denim shorts, metallic strappy open-toe sandals, gold-tone blue-drop earrings, Hairstyle A, face-method identity, and body proportions. Open-toe sandals do not make the hosiery open-toe; the hosiery remains closed and continuous across every toe.
Avoid: exposed toes, bare nail surfaces, sharp toenail outlines, toe gaps, missing fabric between toes, opaque tights, latex/PVC/plastic/rubber/liquid hosiery, white bands, toe-cap seams, face/body drift, AI Face Canon or AI Body Canon input, extra toes/fingers, warped footwear, text, watermark.

## QA status

- v001 hosiery QA: FAIL — exposed toes and insufficient toe tension
- v002 fit/garment QA: pending
- v002 face method compliance: pending
- v002 face contamination comparison: pending
- v002 hosiery continuity/toe coverage: pending
- v002 interdigital tension curves: pending
