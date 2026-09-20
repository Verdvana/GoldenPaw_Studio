# Generation Record — SOC_TRAVEL_001_IMG_01_CAND_01

- asset_id: `SOC_TRAVEL_001_IMG_01`
- candidate_id: `SOC_TRAVEL_001_IMG_01_CAND_01`
- post_id: `SOC_TRAVEL_001`
- asset_level: `L3`
- status: `REVIEW_REQUIRED`
- generation_mode: `built-in image_gen`
- use_case: `photorealistic-natural`
- spec_revision: `OWNER_L1_GENERATION_SPEC draft_1.233`
- reference_set_ids: `OWNER_FACE_LEFT_3Q_NEUTRAL_RECOVERY_V1`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `OWNER_HAIR_A_LEFT_3Q_CANON_L1`, `OWNER_CASUAL_AUTUMN_01`
- authoritative_for: `this post image only; third-person candid travel composition, pose, lighting and city context`
- must_not_define: `new face/body/hair/outfit Canon; recurring Nanjing environment Canon; downstream identity lineage`
- aspect_ratio: `4:5`
- resolution_target: `2160x2700 delivery target; native tool output may be the nearest supported portrait size`
- generation_inputs: see `REFERENCE_PLAN.md`; five declared inputs only
- qa_comparison_only: approved Face 02 Left 3Q, approved Body 01 Front Canon, approved worn outfit front as scoped in `REFERENCE_PLAN.md`
- seed/settings: `not exposed by built-in tool`
- output_path: `social_posts/TRAVEL/SOC_TRAVEL_001/images/SOC_TRAVEL_001_IMG_01/candidates/SOC_TRAVEL_001_IMG_01_CAND_01/SOC_TRAVEL_001_IMG_01_CAND_01.png`
- output_checksum_sha256: `34a3b762599e9e615b0506a60eca5425f75731cc5d171cb9d27555d60c95f63a`
- output_dimensions: `1122x1402`
- qa_status: `PENDING`
- approval_status: `REVIEW_REQUIRED`

## Face-safe declaration

The visible face is generated from the applicable L0 source-derived face method inputs only. No approved AI Face Canon, approved AI Body Canon, or prior generated candidate is used as a generation input. Any AI Canon comparison occurs only after generation for QA.

## Prompt assembly

See `PROMPT_ASSEMBLY.md`.
