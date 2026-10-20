# Generation Record — SOC_OUTFIT_003_IMG_01_CAND_01

- asset_id: `SOC_OUTFIT_003_IMG_01`
- candidate_id: `SOC_OUTFIT_003_IMG_01_CAND_01`
- post_id: `SOC_OUTFIT_003`
- asset_level: `L3`
- status: `REVIEW_REQUIRED`
- generation_mode: `built-in image_gen image edit`
- source_lineage: `single real L0 edit target plus approved/scoped master references; no AI candidate input`
- reference_set_ids: `OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_BODY_REAR_CURRENT_LOWER_BODY_FACE_HAIR_EXCLUDED_DERIVATIVE`, `OWNER_HAIR_A_FRONT_CANON_L1`, `OWNER_HAIR_A_BACK_CANON_L1`
- generation_inputs: see `../../REFERENCE_PLAN.md`; five declared images, including the single original edit target
- qa_comparison_only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
- user_gate: `authorized by user on 2026-10-20 for IMG_01 only`
- authoritative_for: `this post image only; its source pose, mirror reflection, shoe-store scene, outfit and hosiery`
- must_not_define: `any new L1 Canon, downstream identity lineage, future shots, or another image in this carousel`
- aspect_ratio: `9:16 source framing`
- source_path: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_003/source_inputs/IMG_9103.HEIC`
- source_sha256: `c9d45c33c38c8c334384d127120c34aafd055206dd95e72a3df0e52b34964ee6`
- generation_edit_input: `/private/tmp/SOC_OUTFIT_003_IMG_9103_clean.png` (temporary metadata-stripped PNG conversion of the same original pixels; SHA-256 `7ee5c0a5bb61438153ab8a36fe54f848458ba459bc37e2c4c6b10b5f475c04d9`; not stored in the repository)
- generated_at: `2026-10-20`
- generation_settings: `one built-in image_gen edit call; seed not exposed`
- output_path: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_003/images/SOC_OUTFIT_003_IMG_01/candidates/SOC_OUTFIT_003_IMG_01_CAND_01/SOC_OUTFIT_003_IMG_01_CAND_01.png`
- output_checksum_sha256: `97e74af5ab97bc6b23eaf1a31d6ed7c9ef442a10fff7ba17cd40b64d9b223d0b`
- output_dimensions: `941x1672`
- qa_status: `PRELIMINARY_REVIEW_REQUIRED`
- approval_status: `REVIEW_REQUIRED`

## Face-safe declaration

The only visible owner face is the small mirror reflection. Its identity and feature geometry are generated from the source-derived L0 face crop under `FACE_01_FRONT_NEUTRAL_METHOD.md`; the real edit target supplies only the natural skin appearance under its actual lighting. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` is comparison-only after generation. The face-excluded rear lower-body derivative defines only rear lower-body proportions; it cannot define the face, hair, clothing, hosiery material or scene. The two approved Hairstyle A Canons define their respective front-in-mirror and rear views only.

## QA

- technical_status: `PASS`
- face_contamination_check: `REVIEW_REQUIRED`
- face_generation_method_followed: `true`
- downstream_identity_lineage_allowed: `false`
- decision: `candidate ready for user review; not approved for publishing or Canon`
- reviewer: `Codex preliminary visual QA`
- reviewed_at: `2026-10-20`
