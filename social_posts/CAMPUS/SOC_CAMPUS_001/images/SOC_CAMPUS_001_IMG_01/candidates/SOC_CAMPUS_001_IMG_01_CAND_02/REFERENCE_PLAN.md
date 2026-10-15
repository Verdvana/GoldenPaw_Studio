# Reference Plan — SOC_CAMPUS_001_IMG_01_CAND_02

- post_id: `SOC_CAMPUS_001`
- image_asset_id: `SOC_CAMPUS_001_IMG_01`
- candidate_id: `SOC_CAMPUS_001_IMG_01_CAND_02`
- status: `USED_FOR_CAND_02`
- reference_count: `4`
- budget_limit: `8`
- budget_exception: `none`
- selected_reference_set_ids: [`OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `HOS_30D_BLACK_MATTE_OVERALL`]

| Priority | Reference ID/path | Level/status/version | `generation_input` or `qa_comparison_only` | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|---|
| 1 | `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` (SHA-256 `1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91`) | deterministic L0 derivative, v1 | `generation_input` | Owner face identity and feature geometry, adult identity only | Hair, bangs, makeup, jewelry, source retouch/color, camera, body, outfit, hosiery, lighting or background | Sole geometric identity authority for this attempt |
| 2 | `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png` (SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12a6b79182026bd788`) | deterministic L0 derivative, v1 | `generation_input` | Natural warm-neutral skin tone and texture only | Fine geometry, identity, hair, bangs, makeup, camera, body, outfit, lighting or background | Provides skin context separate from feature geometry |
| 3 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` (SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`) | deterministic approved-Body derivative, v1 | `generation_input` | Neck-below proportions and body/leg anatomy | Face, identity, skin pigmentation, hair/bangs, outfit design, hosiery, lighting or background | Meets face-excluded body-reference rule |
| 4 | `L0_HOS_30_BM_003` — `materials/hosiery/source_library/raw/30d_black_matte/IMG_2557.JPG` (SHA-256 `302c10d81dc753490029aa392b45664c21d09eb6f7aa2e81f09a355f91a150bd`) | L0 material source, 30D black matte | `generation_input` | Black hue and matte surface response only | Denier/opacity, person/body/pose, garment design, shoe design, text/watermark, light or background | Closest registered black matte visual reference; target semisheer 20D stays text-defined |

## Face-safe declaration

- face visible: yes — soft three-quarter view, nose toward image-left, gaze just past the camera toward the speaking companion
- applicable method: `canon/face/FACE_01_FRONT_NEUTRAL_METHOD.md` source-derived Face constraints per `source/identity/REFERENCE_GUIDE.md`
- generation face authority: L0-derived `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` only; separate L0 skin context is strictly color/texture only
- approved AI Face Canon comparison only: `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001`, after generation only
- body derivative and checksum: `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1`, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`

## Excluded from generation

- Candidate 01 and every other AI-generated image: no AI-to-AI face lineage. Outfit, scene and timing are restated in text.
- All AI Face/Body Canons as face inputs; Face Canon is QA-only.
- Hairstyle A/B references; this post uses the scoped user-authorized L2 straight-bang design from text only.
- 30D hosiery opacity and denier; target 20D semisheer is text-defined.
- Material-source model, pose, clothing, writing and watermark.
