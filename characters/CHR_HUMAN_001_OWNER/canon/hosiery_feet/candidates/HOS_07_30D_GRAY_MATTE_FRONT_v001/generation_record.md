# HOS_07_30D_GRAY_MATTE_FRONT_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.210
identity_md_revision: draft_0.175
asset_id: HOS_07_30D_GRAY_MATTE_FRONT
candidate_id: HOS_07_30D_GRAY_MATTE_FRONT_v001
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: GENERATION_BLOCKED_NO_OUTPUT
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_BODY_FRONT_CANON_L1
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
design_reconstruction_authorized: true
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_07_30D_GRAY_MATTE_FRONT_v001/HOS_07_30D_GRAY_MATTE_FRONT_v001.png"
actual_dimensions_px: null
checksum_sha256: null
qa_status: NOT_APPLICABLE_NO_OUTPUT
generation_result: BLOCKED
block_reason: "Built-in ImageGen output safety moderation rejected the request; no raster output was returned."
request_id: "52ff8798-eafa-4500-8aa0-29528711c598"
generated_output_path: null
```

## Generation outcome

- One explicitly authorized no-L0 design-reconstruction attempt was blocked at output moderation (`sexual`).
- No raster was returned, stored, inspected, promoted, or used downstream.
- HOS 07 remains `BLOCKED_BY_GENERATION_SAFETY`; no further built-in retry is made automatically.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: approved front lower-leg and foot geometry, proportions and neutral contact only. Its 15D nude appearance must not define this asset.
- No L0 gray hosiery material source is used. Gray 30D matte appearance is an explicitly authorized design reconstruction, not evidence of a real material source.
- No HOS_01–06 pixels and no previous candidate pixels are used.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral technical textile color/material design study; one HOS_07_30D_GRAY_MATTE_FRONT_v001 candidate, REVIEW_REQUIRED.
Use the supplied approved Body Master only for approved front lower-leg and foot geometry, proportions and neutral standing contact. Do not copy its nude 15D surface appearance. Reconstruct the gray 30D textile as an explicitly authorized design study from text only; there is no material photograph.
Create one neutral straight-on technical studio photograph of the front lower body, framed from upper thigh through both complete feet, on a seamless light-gray background with even white-balanced light and exact 3:4 vertical framing. This is apparel-material documentation, not fashion or glamour.
Apply one continuous pair of 30D gray matte hosiery over the visible legs and complete feet. The textile is moderately dense, cool neutral medium-gray, softly matte, finely woven and translucent enough for restrained underlying form. It is more substantial than 15D but not opaque, plastic-like or painted onto the body.
Keep the material response uniform and continuous through thigh, knee, calf, ankle, heel, instep, forefoot and toe tips. At the toes, the gray textile may become very slightly more translucent toward the rounded tips through a smooth broad gradient; there must be no structural division or visible construction feature.
The forefoot is one uninterrupted continuous fabric surface with smooth longitudinal flow. Show only soft anatomical toe relief beneath the textile. No transverse marks, stripes, bands, seams, rings, sock edges, separate toe compartments, abrupt opacity changes or color breaks. Preserve natural anatomy, five toes per foot, separate feet and stable floor contact.
No footwear, props, text, logo, watermark, collage, artificial coating, hard shine, duplicated/fused/missing anatomy or sexualized framing. Output one REVIEW_REQUIRED candidate only.
```
