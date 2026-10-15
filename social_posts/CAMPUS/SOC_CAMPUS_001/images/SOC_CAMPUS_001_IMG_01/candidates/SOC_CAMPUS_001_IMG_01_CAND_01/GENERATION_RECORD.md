# Generation Record — SOC_CAMPUS_001_IMG_01_CAND_01

- post_id: `SOC_CAMPUS_001`
- image_asset_id: `SOC_CAMPUS_001_IMG_01`
- candidate_id: `SOC_CAMPUS_001_IMG_01_CAND_01`
- asset_level: `L3`
- status: `REVIEW_REQUIRED`
- user authorization: “可以，先生成一张看看” (`2026-10-15`, one IMG_01 candidate only)
- owner spec revision: `draft_1.234`
- reference_plan: `social_posts/CAMPUS/SOC_CAMPUS_001/images/SOC_CAMPUS_001_IMG_01/REFERENCE_PLAN.md`
- prompt_assembly: `social_posts/CAMPUS/SOC_CAMPUS_001/images/SOC_CAMPUS_001_IMG_01/PROMPT_ASSEMBLY.md`
- reference budget: `4 / 8 images`

## Generation inputs

1. `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — L0-derived identity/feature geometry only; SHA-256 `1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91`.
2. `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` — natural L0 skin color/texture context only; SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12a6b79182026bd788`.
3. `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — deterministic face-excluded body derivative only; SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`.
4. `L0_HOS_30_BM_003` — black hue and matte textile surface only; 30D appearance/opacity excluded; SHA-256 `302c10d81dc753490029aa392b45664c21d09eb6f7aa2e81f09a355f91a150bd`.

No hairstyle, outfit or environment image is used; the user-directed L2 hairstyle and episode design are text-defined. No prior shot or generated candidate is used.

## QA comparison only

- `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001`: post-generation identity drift, feature relationship, skin contamination, projection and framing QA only. Never a generation input.

## Prompt assembly

See `../PROMPT_ASSEMBLY.md`. The single candidate depicts a full-body friend snapshot mid-conversation at a generic campus building exit, in the specified 2018 phone-camera style.

## Generation settings and output

- tool: `OpenAI ImageGen`
- generated_at: `2026-10-15` (Asia/Shanghai)
- seed/settings: seed unavailable; built-in ImageGen native output
- requested output: portrait 4:5 PNG, 2160x2700 target if supported; returned native output `1122x1402`
- output_path: `social_posts/CAMPUS/SOC_CAMPUS_001/images/SOC_CAMPUS_001_IMG_01/candidates/SOC_CAMPUS_001_IMG_01_CAND_01/SOC_CAMPUS_001_IMG_01_CAND_01.png`
- tool artifact path: `/home/verdvana/.codex/generated_images/01a13f7d-e6e0-7332-b1b3-495fd70ef882/exec-3c96e37d-12b2-4d88-81a4-b2b38f6a169c.png`
- output_checksum: `dc3f1f961cd19ba6f228d5bd8d6cfd39bb33ecabead538b661001a6081e46880`
- QA status: `REVIEW_REQUIRED — see QA.md`
- approval/promotion: none; no automatic Canon or publication promotion
