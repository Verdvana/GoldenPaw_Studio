# BODY_01_FRONT_v021 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v021
target_canon_version: owner_v1.0
gate: Gate 3 — Body Canon
status: REVIEW_REQUIRED
approval_status: PENDING_USER_REVIEW
spec_revision: draft_1.233
identity_revision: draft_0.184
body_method_id: OWNER_BODY_01_FRONT_METHOD_V2
generation_tool: built_in_image_gen
use_case: identity-preserve
reference_set_ids:
  - OWNER_BODY_FRONT_RECOVERY_V1
edit_target:
  asset_id: OWNER_BODY_01_FRONT_CANON_006
  path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v017/BODY_01_FRONT_v017.png
  responsibility: "current Body01 visual baseline; neck-only edit target"
  must_not_define: "new face identity, new body proportions, new hairstyle, new clothing, new hosiery, lighting or background"
generation_inputs: []
qa_comparison_only:
  - {asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and face-contamination QA only"}
  - {asset_id: OWNER_BODY_01_FRONT_CANON_006, path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v017/BODY_01_FRONT_v017.png", purpose: "post-generation comparison for all non-neck invariants"}
reference_count: 1
previous_generated_body_inputs: 0
authoritative_for:
  - "candidate neck length and upright neck carriage only"
must_not_define:
  - "new permanent identity facts or face Canon"
  - "body proportions, shoulders, chest, waist, hips, arms, legs or feet"
  - "Hairstyle A, swimsuit, hosiery, lighting, background, props, text or watermark"
aspect_ratio: "3:4"
resolution: "1536x2048"
prompt_assembly: "See prompt below; edit only the visible neck carriage while preserving all other attributes as closely as possible."
seed: null
settings: {tool: "built_in_image_gen", output: "single candidate", preferred_resolution: "1536x2048"}
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v021/BODY_01_FRONT_v021.png
sha256: 2d73ede6c71f50f99ef415164cacbd35f68f235a95532f87a6d2deb4ee627d44
dimensions: 1087x1446
qa_status: TECHNICAL_PRECHECK_PASS_PENDING_USER_REVIEW
```

## Prompt assembly

Use case: identity-preserve
Asset type: L1 Body01 front technical calibration candidate
Input image: Image 1 is the current Body01 edit target and visual baseline.
Primary request: Make only the neck look slightly longer and more upright so the subject no longer appears to draw the neck inward or hunch. Create a natural, modest increase in visible neck length and a relaxed upright carriage: shoulders remain at the same height, head remains the same size and position, chin and face geometry remain unchanged, and the neck transitions naturally into the existing shoulders and collarbones.
Constraints: preserve the exact same person, face, Hairstyle A, expression, camera, framing, background, lighting, pink one-piece swimsuit, 15D hosiery, leg axes, foot placement, body proportions and hand positions. Do not slim or widen the shoulders, change the torso, stretch the whole body, lift the chin, tilt the head, alter the jaw, or create a swan-like neck. One neutral full-body candidate only; REVIEW_REQUIRED; not Canon.
Avoid: short compressed neck, hunched shoulders, tucked chin, head enlargement, facial drift, long-stretched neck, visible seams, artifacts, text, watermark, collage.

## QA plan

Hard checks: neck reads modestly longer and more upright; shoulders and head position remain coherent; no face identity drift or face contamination; no chin lift or head tilt; all non-neck body geometry, outfit, hosiery, feet, lighting and background remain unchanged; no generation artifacts. Reject if any hard check fails. No promotion without explicit user approval.
