# HOS_07_30D_GRAY_MATTE_FRONT_v004 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.213
identity_md_revision: draft_0.175
asset_id: HOS_07_30D_GRAY_MATTE_FRONT
candidate_id: HOS_07_30D_GRAY_MATTE_FRONT_v004
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_07_30D_GRAY_MATTE_FRONT_v004/HOS_07_30D_GRAY_MATTE_FRONT_v004.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "f09f783065223c94adb96cb704abff05597ab881cc70d13b70cb16da9369277d"
qa_status: TECHNICAL_PRECHECK_PASS_REVIEW_REQUIRED
generation_result: SUCCESS
request_id: "not_returned_by_tool"
```

## Generation outcome and technical pre-check

- Generated successfully; output is 1086×1448 PNG.
- Lighter smoke-gray, increased density, stronger continuous translucency gradient and subtle interdigital textile tension are directionally present.
- No obvious transverse toe-root line or separate toe construction was observed in the initial review.
- Candidate remains `REVIEW_REQUIRED`; it is not approved and must not be used as a downstream pixel reference.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: approved lower-leg and foot geometry, proportions and neutral contact only. Its 15D nude appearance is excluded.
- No L0 gray hosiery source exists; gray 30D matte is an explicitly authorized design reconstruction from text only.
- No HOS_01–06 pixels and no HOS_07 v001–v003 pixels are used.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral lower-leg textile color/material design study; one HOS_07_30D_GRAY_MATTE_FRONT_v004 candidate, REVIEW_REQUIRED.
Use the supplied approved Body Master only for lower-leg and foot geometry, proportions and neutral contact. Do not copy its 15D nude surface. Reconstruct the gray textile independently from the written specification; no material photograph or previous candidate is used.
Create one neutral straight-on technical studio photograph matching HOS_01 framing: crop from just below both knees to both complete feet, with both feet separate and flat on one light-gray studio surface. Use even white-balanced clinical lighting, restrained perspective and exact 3:4 vertical framing.
Apply one continuous 30D light smoke-gray matte textile layer. Make the gray visibly lighter and softer than v003, never charcoal. Increase the textile density again so the fabric reads thicker and more substantial than v003, while remaining a matte translucent woven veil rather than opaque gray covering.
Make the translucency gradient more legible but perfectly continuous: from just below the knees through calves, ankles and insteps, only a restrained hint of warm underlying skin is visible; across the forefoot and toward the rounded toe tips, the warm underlying tone gradually becomes more visible. The toe tips are the most translucent area, with no step, line, band or change-point.
Between adjacent toes, show subtle localized fabric tension: the same continuous textile gently narrows and gathers optically into the natural interdigital valleys, with delicate converging knit direction and slightly increased translucency at the valleys. This must be soft, shallow and anatomically natural, not separate toe sleeves, not open gaps and not a seam.
The entire lower leg and foot remain one uninterrupted surface with no transverse forefoot marks, stripes, bands, seams, rings, edges, separate toe compartments, abrupt opacity changes or color breaks. Preserve natural anatomy, five toes per foot, separate feet and stable contact.
No footwear, props, text, logo, watermark, collage, artificial coating, hard shine, duplicated/fused/missing anatomy or sexualized framing. Output one REVIEW_REQUIRED candidate only.
```
