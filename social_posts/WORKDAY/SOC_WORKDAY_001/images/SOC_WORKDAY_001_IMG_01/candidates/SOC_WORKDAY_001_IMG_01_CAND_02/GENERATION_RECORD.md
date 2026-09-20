# Generation Record — SOC_WORKDAY_001_IMG_01_CAND_02

- asset_id: `SOC_WORKDAY_001_IMG_01`
- candidate_id: `SOC_WORKDAY_001_IMG_01_CAND_02`
- asset_level: L3
- status: USER_REJECTED
- generation_date: 2026-09-20
- generation_gate: user correction — previous candidate was clearly third-person street photography, not a selfie
- output_path: `social_posts/WORKDAY/SOC_WORKDAY_001/images/SOC_WORKDAY_001_IMG_01/candidates/SOC_WORKDAY_001_IMG_01_CAND_02/SOC_WORKDAY_001_IMG_01_CAND_02.png`
- output_sha256: `6214be52b6b939417db3fe114160f3c33ee30ac46080eae1faae20a6fb19b66f`
- output_dimensions: `1122x1402` PNG, RGB
- settings: built-in ImageGen, photorealistic-natural, target 4:5 vertical social still; seed unavailable
- spec_revision: `draft_1.233`
- generation_inputs: same three scoped references as CAND_01; see sibling `../REFERENCE_PLAN.md`
- qa_comparison_only: none expected because the face is intentionally out of frame
- prompt_assembly: `PROMPT_ASSEMBLY.md`
- QA status: failed — visible arm/phone foreground did not match chest-level downward selfie framing
