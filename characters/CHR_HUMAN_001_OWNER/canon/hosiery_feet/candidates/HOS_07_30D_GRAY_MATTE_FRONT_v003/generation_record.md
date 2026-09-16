# HOS_07_30D_GRAY_MATTE_FRONT_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.212
identity_md_revision: draft_0.175
asset_id: HOS_07_30D_GRAY_MATTE_FRONT
candidate_id: HOS_07_30D_GRAY_MATTE_FRONT_v003
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: GENERATED_REVIEW_REQUIRED
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_07_30D_GRAY_MATTE_FRONT_v003/HOS_07_30D_GRAY_MATTE_FRONT_v003.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "9262096f22f9ce2d32fac8da2a5d0b789962d1ff8a9bbc49ec1ea17828bd194f"
qa_status: TECHNICAL_PRECHECK_PASS_REVIEW_REQUIRED
generation_result: SUCCESS
request_id: "not_returned_by_tool"
```

## Generation outcome and technical pre-check

- Generated successfully; output is 1086×1448 PNG.
- Smoke-gray color, increased 30D density, subtle leg-to-instep translucency and stronger toe-tip translucency are directionally present.
- No obvious transverse toe-root line or separate toe construction was observed in the initial review.
- Candidate remains `REVIEW_REQUIRED`; it is not approved and must not be used as a downstream pixel reference.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: approved lower-leg and foot geometry, proportions and neutral contact only. Its 15D nude appearance is excluded.
- No L0 gray hosiery source exists; gray 30D matte is an explicitly authorized design reconstruction from text only.
- No HOS_01–06 pixels and no HOS_07 v001–v002 pixels are used.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral lower-leg textile color/material design study; one HOS_07_30D_GRAY_MATTE_FRONT_v003 candidate, REVIEW_REQUIRED.
Use the supplied approved Body Master only for lower-leg and foot geometry, proportions and neutral contact. Do not copy its 15D nude surface. Reconstruct the gray 30D textile independently from the written specification; no material photograph or previous candidate is used.
Create one neutral straight-on technical studio photograph matching HOS_01 framing: crop from just below both knees to both complete feet, with both feet separate and flat on one light-gray studio surface. Use even white-balanced clinical lighting, restrained perspective and exact 3:4 vertical framing.
Apply one continuous 30D smoke-gray matte textile layer. Use a light, soft smoke-gray rather than charcoal or dark gray. Increase the textile thickness slightly from v002: it should read as a denser, more substantial woven veil while remaining translucent and matte, never opaque.
Translucency must vary gradually along the vertical body-to-foot path. From just below the knees through the calves, ankles and insteps, show only a subtle suggestion of the underlying warm skin tone through the smoke-gray textile. As the surface continues across the forefoot toward the rounded toe tips, gradually increase the warm skin visibility and translucency. The toe tips should show noticeably more underlying skin tone than the leg or instep, but still remain covered by the same gray textile. This is a smooth continuous gradient with no step, band or boundary.
Keep the entire lower leg and foot as one uninterrupted textile surface with uniform longitudinal flow. No transverse marks, stripes, bands, seams, rings, edges, separate toe compartments, abrupt opacity changes or color breaks. Preserve natural anatomy, five toes per foot, separate feet and stable contact.
No footwear, props, text, logo, watermark, collage, artificial coating, hard shine, duplicated/fused/missing anatomy or sexualized framing. Output one REVIEW_REQUIRED candidate only.
```
