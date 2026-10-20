# Generation Record — SOC_OUTFIT_003_IMG_02_CAND_01

- asset_id: `SOC_OUTFIT_003_IMG_02`
- candidate_id: `SOC_OUTFIT_003_IMG_02_CAND_01`
- post_id: `SOC_OUTFIT_003`
- asset_level: `L3`
- status: `REVIEW_REQUIRED`
- generation_mode: `built-in image_gen image edit`
- source_lineage: one real L0 edit target plus scoped face-excluded body, L0 face geometry and approved hair references; no generated candidate lineage
- reference_plan: `../../REFERENCE_PLAN.md`
- generation_inputs: four images total; see `../../REFERENCE_PLAN.md`
- qa_comparison_only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
- generation_edit_input: `/private/tmp/SOC_OUTFIT_003_IMG_9106_clean.png`, metadata-stripped pixel conversion of the original; SHA-256 `59f34ea4443ea347a3606f6ebaa80950f22cdd8abdc76214344a75c1c1be4ffb`; temporary, not stored in repository
- source_path: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_003/source_inputs/IMG_9106.HEIC`
- source_sha256: `d155486d1be5582ab3747f631375c14bba49a269a86af506624ae2c7ba5852f1`
- user_gate: authorized by the user on 2026-10-20 for one IMG_02 candidate only
- generated_at: `2026-10-20`
- generation_settings: one image edit call; seed not exposed by tool
- output_path: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_003/images/SOC_OUTFIT_003_IMG_02/candidates/SOC_OUTFIT_003_IMG_02_CAND_01/SOC_OUTFIT_003_IMG_02_CAND_01.png`
- output_sha256: `1c2afcc085aa742820dc3e58af5c59d11ad4ef2f731269986443c392bf31224a`
- output_dimensions: `941x1672`
- qa_status: `REVIEW_REQUIRED`
- approval_status: `REVIEW_REQUIRED`
- must_not_define: any L1 Canon, identity lineage, or another carousel image

## QA declarations

- face_generation_rule_followed: `true`; source-derived L0 face geometry only, AI Face Canon comparison-only
- generation_inputs and qa_comparison_only are separate as required
- face_contamination_check: `REVIEW_REQUIRED`; only the lower face is visible, so feature-level identity QA is limited; no obvious face contamination observed
- overall_qa: hosiery continuity and garment retention pass; exact scene/signage preservation needs user review because details were re-rendered
