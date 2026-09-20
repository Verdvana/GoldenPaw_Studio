# Generation Record — SOC_TRAVEL_001_IMG_03_CAND_01

- asset_id: `SOC_TRAVEL_001_IMG_03`
- candidate_id: `SOC_TRAVEL_001_IMG_03_CAND_01`
- post_id: `SOC_TRAVEL_001`
- asset_level: `L3`
- status: `REVIEW_REQUIRED`
- generation_mode: `built-in image_gen generate`
- source_lineage: `fresh parallel generation; no prior AI candidate input`
- reference_set_ids: `OWNER_FACE_LEFT_3Q_NEUTRAL_RECOVERY_V1`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `OWNER_HAIR_B_LEFT_3Q_CANON_L1`, `OWNER_CASUAL_AUTUMN_01`, `TECH_CAT_L0_FRONT_IDENTITY`
- generation_inputs: see `REFERENCE_PLAN.md`; five declared inputs only
- qa_comparison_only: approved owner Face 02 Left 3Q, approved owner Body 01 Front, approved worn outfit front
- authoritative_for: `this post image only; night Xinjiekou street context, crouch interaction and expression`
- must_not_define: `new owner or cat Canon, recurring Xinjiekou location Canon, downstream identity lineage`
- aspect_ratio: `4:5`
- output_path: `social_posts/TRAVEL/SOC_TRAVEL_001/images/SOC_TRAVEL_001_IMG_03/candidates/SOC_TRAVEL_001_IMG_03_CAND_01/SOC_TRAVEL_001_IMG_03_CAND_01.png`
- output_checksum_sha256: `29723f018d9a65f1dd8075ed78b6868e949d9d9e5e439117ba3d09bece986d17`
- output_dimensions: `1122x1402`
- qa_status: `PRELIMINARY_PASS_USER_REVIEW_REQUIRED`
- approval_status: `REVIEW_REQUIRED`

## Face-safe and cat-safe declaration

The owner's visible face is generated from L0/source-derived face responsibility only. Approved AI face/body images and previous post images are not generation inputs. The cat uses only L0_CAT_001 for its declared front identity traits; do not propagate a previous AI cat.
