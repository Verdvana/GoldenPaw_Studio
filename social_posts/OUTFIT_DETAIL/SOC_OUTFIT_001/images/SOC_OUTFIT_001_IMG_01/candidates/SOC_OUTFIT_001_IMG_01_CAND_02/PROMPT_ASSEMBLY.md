# Candidate 02 Prompt Assembly / Generation Record

- model/tool: OpenAI ImageGen
- status: CANDIDATE_GENERATED_REVIEW_REQUIRED
- user authorization: 2026-10-17, “第一版比较好，但是有点ai味道，能不能二次加工一下去除ai味”
- generation_inputs: L0-derived face geometry crop (face only); L0-derived natural skin crop (skin context only); deterministic face-excluded body derivative (neck-below proportions only); Hair A Canon (hair only); approved text outfit specification from `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/OUTFIT.md`
- continuity_only_input: Candidate 01 (composition, selfie camera angle/crop, window/reflection placement only; expressly excluded from face, skin, body, hair, outfit/material, identity and rendering authority)
- qa_comparison_only: approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` after generation only
- reference_count: 6 (five attached refs plus QA-only face Canon declared in record; QA Canon not attached to generator)
- face_generation_rule: source-derived L0 inputs plus `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`; no AI face/body input

## Refinement targets

Keep the successful broad composition and Autumn-02 outfit. Reduce the beauty-filter look: restore subtle natural skin texture and tonal variation, reduce eyeliner/eye emphasis and glossy uniform skin, retain the owner's natural facial proportions. Make the result resemble a spontaneous phone selfie rather than a polished campaign image. Preserve a plausible but imperfect glass reflection, softer mixed outdoor/café light, and ordinary street detail with naturally varied focus. Do not add artificial grain as a cover-up.

## Final assembled prompt

Create a fresh photorealistic 4:5 vertical front-camera selfie of the adult owner by a generic café street window on an autumn walk. Use the previous candidate only as a guide to the broad crop, arm-length selfie camera placement, window position, and secondary reflection location. Do not copy its face, expression, identity, skin, body, hair, outfit, lighting or image-rendering characteristics. Generate the face only from the two supplied L0-derived face/skin references under the source-derived face method. Preserve natural facial geometry and warm-neutral skin. Keep makeup restrained and close to the source's natural appearance: no heavy eyeliner, enlarged-looking eyes, beauty filter, porcelain skin, over-smoothing, brightening, color cast, facial slimming or retouching. Allow subtle real skin texture and small natural tonal variation without blemishes being exaggerated or adding blotches. Use the face-excluded body derivative only for neck-below proportions; Hair A Canon only for hair; approved written Autumn 02 spec only for clothing. Outfit: dark chocolate-brown tailored blazer and fitted ivory fine-ribbed high-neck knit. Keep a relaxed, slightly off-center spontaneous selfie composition and a mild natural smartphone perspective without facial distortion. The café window reflection is faint, incomplete and angle-correct, not a duplicate mirror portrait. Light should have believable soft daylight mixed with warmer café interior spill, with coherent shadows and no dramatic grading. Let background sharpness vary naturally; avoid uniformly creamy synthetic bokeh. Add no film grain, text, logos, watermark, UI, or private-home cues. Output one new candidate; do not overwrite Candidate 01. Face Canon is a post-generation QA comparison only and is not a generation reference.

## Generation settings/result

- generated_at: 2026-10-17
- seed/settings: not exposed by ImageGen; native 1122×1402 PNG, approximately 4:5
- output_path: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_001/images/SOC_OUTFIT_001_IMG_01/candidates/SOC_OUTFIT_001_IMG_01_CAND_02/SOC_OUTFIT_001_IMG_01_CAND_02.png`
- output_checksum: `26d4f1a265a439fa60af227aa083591091170bba2a61a758000dec65950fd11a`
- QA_record: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_001/images/SOC_OUTFIT_001_IMG_01/candidates/SOC_OUTFIT_001_IMG_01_CAND_02/QA.md`
