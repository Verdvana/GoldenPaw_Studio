# OWNER_DATE_SUMMER_01 — Hosiery appearance method v015

- status: APPROVED_BY_USER
- level/scope: L2, this summer-date outfit only
- user/date: user, 2026-10-31
- evidence: “可以 批准，后面再用这套服装，就按照生成这张图的丝袜质感来生成”
- approved_result_asset: OWNER_DATE_SUMMER_01_WORN_FRONT_v015
- approved_result_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v015.png`
- approved_result_sha256: `e9d59c10a5a269c5aeeab777bc19f65fc041d9dab54642c8a175b34cdc199b25`
- material_generation_record: `candidates/v015_worn_front/generation_record.md`
- exact_successful_prompt: `candidates/v015_worn_front/PROMPT.txt`

## Mandatory behavior for later uses of this outfit

Every later OWNER_DATE_SUMMER_01 image must match the hosiery appearance of approved v015: its milky-white semi-sheer color, skin-through-textile softness, fine silk-like fiber sheen and observed leg/ankle/foot coverage. Preserve this accepted result as the outfit's appearance target rather than restarting earlier failed revisions or switching to a new matte/gloss variant. Do not continue treating the initial agent QA as an unresolved user rejection.

Retain one visible true high waistband below the cropped blouse, a navel readable through abdominal hosiery, no second extra strip immediately above the denim, closed-toe textile coverage and smooth wrinkle-free ankle drape. Keep general textile-continuity/anti-silicone QA. Exact denier remains unverified.

## Original material recipe and scoped input selection

1. `HOS_USER_SELECTED_WHITE_STRICT_WIDE_CROP_V2`: immutable user L0 white photo native crop, sole original-source white/translucency/finish authority. Keep this source in generation inputs for white hosiery as globally required.
2. `OWNER_DATE_SUMMER_01_FOOT_MATERIAL_DETAIL_APPROVED_V002`: user-approved L2 foot detail for continuous knit over nail/toe surfaces, intertoe tension, fine grain and wrinkle-free ankles. This was the actual second material input in v015. Use when foot detail must be established; never inherit its foot anatomy, pose or close-up framing.
3. `OWNER_DATE_SUMMER_01_HOSIERY_APPEARANCE_APPROVED_V015`: deterministic face-excluded approved-result crop for this outfit's material appearance transfer when needed, and post-generation material QA. Path `outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/reference_inputs/hosiery_v015/WORN_FRONT_v015_WAIST_TO_FEET_MATERIAL_CROP.png`, SHA-256 `3e77cd2c9e272ed869c1f5094326ba287add1bc23856412e3cd88436eeecc7a0`. It defines hosiery only, never the pictured body/pose/skin/leg shape/shoes.

Use the smallest required set: start with the original two material inputs and v015 appearance constraints. For direct approved-result appearance transfer, use the face-excluded v015 crop with original L0 source; add the foot-detail image only when a documented close-up/coverage need justifies it. Keep the tool reference budget; reorganize scoped non-material references if needed rather than attaching every image. A future generation record must list actual paths/checksums/responsibilities/exclusions and separate generation_inputs from qa_comparison_only.

The full v015 portrait is QA-only for likeness/body/overall outfit. Do not pass its generated face to future image generation. The material crop may be passed only within the explicit material scope above.

## Reuse limits

This user decision approves HOSIERY appearance for this outfit, not a new face/body/hair/skin Canon, universal leg shape, or a global hosiery replacement for other outfits. The successful v015 run's historical B face/skin recipe was a user-scoped method choice; outfit material approval does not extend it into blanket future generated-face permission. Future faces/body/hair follow their then-applicable independent sources and rules. Never use earlier rejected fitting images as downstream inputs.

Existing approved Foot v002 remains a fine-detail reference; approved Worn v005 remains historical and is no longer the current fitting or hosiery target. No L1 promotion/Canon lock occurs.
