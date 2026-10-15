# Generation Record — SOC_CAMPUS_001_IMG_01_CAND_02

- post_id: `SOC_CAMPUS_001`
- image_asset_id: `SOC_CAMPUS_001_IMG_01`
- candidate_id: `SOC_CAMPUS_001_IMG_01_CAND_02`
- asset_level: `L3`
- status: `REVIEW_REQUIRED`
- authorization: user requested one preview; after reviewing Candidate 01, user said “衣服可以 长相不对”, authorizing this focused correction while retaining clothing
- owner spec revision: `draft_1.234`
- reference_plan: `REFERENCE_PLAN.md`
- prompt_assembly: `PROMPT_ASSEMBLY.md`
- reference budget: `4 / 8 images`
- independent generation: `yes`; Candidate 01 is not an image input

## generation_inputs

1. `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — L0-derived identity/feature geometry only; SHA-256 `1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91`.
2. `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` — natural L0 skin color/texture only; SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12a6b79182026bd788`.
3. `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — neck-below body proportions only; SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`.
4. `L0_HOS_30_BM_003` — black hue/matte textile response only; SHA-256 `302c10d81dc753490029aa392b45664c21d09eb6f7aa2e81f09a355f91a150bd`.

## qa_comparison_only

- `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001` — post-generation identity/face-contamination comparison only. Never a generation input.

## Prompt and output record

- prompt: `PROMPT_ASSEMBLY.md`
- generated_at: `2026-10-15` (Asia/Shanghai)
- seed/settings: seed unavailable; built-in ImageGen native output
- output_path: `social_posts/CAMPUS/SOC_CAMPUS_001/images/SOC_CAMPUS_001_IMG_01/candidates/SOC_CAMPUS_001_IMG_01_CAND_02/SOC_CAMPUS_001_IMG_01_CAND_02.png`
- output_checksum: `a99c48b51a41791e1d06eb2d5b304c797b97de163dd9b746578507ed1acdec86`
- QA: `QA.md` (`REVIEW_REQUIRED`; user identity review pending)
- tool artifact path: `/home/verdvana/.codex/generated_images/01a13f7d-e6e0-7332-b1b3-495fd70ef882/exec-518431a1-1d65-424c-bebf-e149bd3e9553.png`
- approval/promotion: none
