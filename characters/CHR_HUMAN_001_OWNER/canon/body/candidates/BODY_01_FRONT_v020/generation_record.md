# BODY_01_FRONT_v020 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v020
target_canon_version: owner_v1.0
gate: Gate 3 — Body Canon
status: GENERATION_BLOCKED_NO_OUTPUT
approval_status: PENDING_USER_REVIEW
spec_revision: draft_1.232
identity_revision: draft_0.183
body_method_id: OWNER_BODY_01_FRONT_METHOD_V2
body_revision: draft_0.20
generation_tool: built_in_image_gen
use_case: identity-preserve
reference_set_ids:
  - OWNER_BODY_FRONT_RECOVERY_V1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
generation_inputs:
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", responsibility: "source-derived front face/skin only", must_not_define: "body, hair, clothing, hosiery, lighting, background"}
  - {asset_id: L0_OWNER_002, path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/3.jpg", responsibility: "stature and body context", must_not_define: "face, hair, clothing, shoes, props, background"}
  - {asset_id: L0_OWNER_003, path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/4.jpg", responsibility: "natural torso and limb-volume cross-check", must_not_define: "face, hair, clothing, shoes, environment"}
  - {asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png", responsibility: "Hairstyle A only", must_not_define: "face, body, skin, clothing, lighting, background"}
  - {asset_id: OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001, path: "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png", responsibility: "15D continuous foot-to-toe textile behavior only", must_not_define: "identity, body/foot anatomy, nail color, clothing, lighting, floor contact"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and face-contamination QA only"}
  - {asset_id: OWNER_BODY_01_FRONT_CANON_006, path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v017/BODY_01_FRONT_v017.png", purpose: "post-generation proportion/leg/waist comparison only"}
reference_count: 5
previous_generated_body_inputs: 0
authoritative_for:
  - "new BODY_01_FRONT candidate waist/leg proportion revision"
  - "front standing pose and straight leg-axis presentation"
must_not_define:
  - "new permanent identity facts or face Canon"
  - "any other body angle or pose"
  - "other hosiery colors, deniers or finishes"
  - "lighting/background design, props, text or watermark"
aspect_ratio: "3:4"
resolution: "1536x2048"
prompt_assembly: "See generation prompt in the assistant generation call; source-derived inputs are parallel and no prior generated body pixels are used."
seed: null
settings: {tool: "built_in_image_gen", output: "single candidate", preferred_resolution: "1536x2048"}
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v020/BODY_01_FRONT_v020.png
sha256: PENDING
dimensions: PENDING
qa_status: GENERATION_BLOCKED_NO_OUTPUT
```

## Generation attempt

- Built-in ImageGen: blocked at output moderation stage with `sexual`; no image was returned or saved.
- No candidate raster exists. This record must not be promoted or used as a downstream reference.
- CLI/API fallback was not invoked; it requires explicit user authorization and `OPENAI_API_KEY`.

## Prompt assembly

Create exactly one neutral, full-length, front-view technical anthropometric fitting reference of an adult woman, fully clothed and non-erotic. Use the four source-derived recovery inputs for their declared responsibilities only and the scoped 15D textile crop only for hosiery behavior. Do not use any generated Body image, approved Body image, generated Face image or approved Face image as a generation input.

Preserve the same face identity from the source-derived face/skin context, Hairstyle A, 168 cm / approximately 60 kg coherent stature, pink high-cut one-piece calibration garment, and the currently accepted front stance. Compared with the current accepted v019 proportions, make the waist approximately 5% narrower through a smooth natural ribcage-to-waist-to-existing-hip transition; do not corset-compress, pinch, or exaggerate the hourglass. Increase both thighs and calves by approximately 5% in natural soft-tissue volume, evenly and anatomically, while keeping stature, torso length, hip width, foot size and arm proportions coherent.

Both legs must remain nearly perfectly straight in front view: each knee center, tibial shaft centerline and ankle center nearly collinear with the thigh axis; outer calf edge continues nearly flush with the same-side outer thigh edge; no inward bow, outward O-leg bulge, crossed legs or fused legs; retain a tiny natural inner-leg gap. Both feet are fully flat and weight-bearing with heel, forefoot and toes on the floor.

The pantyhose is one continuous pale light-nude 15D velvet-finish sheer textile from thighs through knees, calves, ankles, heels, insteps, forefeet and every toe. It must fully cover every toenail. Absolutely no white line, white ring, pale transverse band, hard toe-root boundary, reinforced-toe edge, exposed crisp nail edge, uncovered nail, bare toe gap, seam or material discontinuity. Burgundy polish may appear only as a diffuse low-saturation haze beneath the same fabric. Between toes, show readable but natural V-shaped fabric tension valleys and converging stretch curves; these are textile responses, not bare skin gaps or painted lines. Keep the textile surface coherent and slightly lighter than the underlying skin, matte/velvet sheer, never latex, PVC, plastic, wet coating or body paint.

Neutral gray-white seamless studio, soft even 5200–5600K light, level 70–85mm-equivalent camera centered between waist and lower chest, exact 3:4 framing, complete head/hands/feet visible, square torso, relaxed arms, uncrossed legs, no props, no text, no watermark, no collage, no dramatic styling. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Hard checks: face contamination against the comparison-only Face Canon; waist approximately 5% narrower without pinching; thighs/calves approximately 5% fuller without changing stature or hip width; knee–tibia–ankle collinearity and straight outer-leg contours; flat heel/forefoot/toe contact; uninterrupted hosiery from legs through every toe; no white toe-root line/ring/band; every toenail fully under the fabric with no crisp exposed edge; readable V-shaped interdigital textile tension; no bare gaps, fused/duplicated toes, plastic/latex appearance or generation artifacts. Reject if any hard check fails. No promotion without explicit user approval.
