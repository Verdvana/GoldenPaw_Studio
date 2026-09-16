# HOS_07_30D_GRAY_MATTE_FRONT_v006 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.215
identity_md_revision: draft_0.175
asset_id: HOS_07_30D_GRAY_MATTE_FRONT
candidate_id: HOS_07_30D_GRAY_MATTE_FRONT_v006
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
denier_revision_note: "Maintain the v005 15D gray matte thickness baseline; increase only visual readability of color, gradient and interdigital tension."
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_07_30D_GRAY_MATTE_FRONT_v006/HOS_07_30D_GRAY_MATTE_FRONT_v006.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "e5b99bd2f8be4ba922e528e2016b21d0bf07c5fad6b4f66e0ba0f0cf079204e8"
qa_status: TECHNICAL_PRECHECK_PASS_REVIEW_REQUIRED
generation_result: SUCCESS
request_id: "not_returned_by_tool"
```

## Generation outcome and technical pre-check

- Generated successfully; output is 1086×1448 PNG.
- Smoke-gray readability, stronger gradient and more visible local interdigital tension curves are present.
- The tension remains local to the toe valleys without an obvious continuous transverse forefoot line or separate toe compartments.
- Candidate remains `REVIEW_REQUIRED`; it is not approved and must not be used as a downstream pixel reference.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: approved lower-leg and foot geometry, proportions and neutral contact only. Its 15D nude appearance is excluded.
- No L0 gray hosiery source exists; gray 15D matte is an explicitly authorized design reconstruction from text only.
- No HOS_01–06 pixels and no HOS_07 v001–v005 pixels are used.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral lower-leg textile color/material design study; one HOS_07_30D_GRAY_MATTE_FRONT_v006 candidate, REVIEW_REQUIRED.
Use the supplied approved Body Master only for lower-leg and foot geometry, proportions and neutral contact. Reconstruct the textile independently from the written specification; no material photograph or previous candidate is used.
Create one neutral straight-on technical studio photograph matching HOS_01 framing: crop from just below both knees to both complete feet, with both feet separate and flat on one light-gray studio surface. Use even white-balanced clinical lighting, restrained perspective and exact 3:4 vertical framing.
Apply one continuous light smoke-gray 15D matte textile layer. Make the smoke-gray color clearly visible and consistent across the legs, lighter than charcoal but unmistakably gray rather than nude. Keep the textile fine, sheer and softly matte.
Make the translucency gradient clearly readable: from just below the knees through calves, ankles and insteps, the warm underlying skin is only faintly visible through the gray textile; across the forefoot it becomes progressively more visible; at the rounded toe tips it is distinctly more visible and translucent. The transition must be smooth and continuous, with no step, band or boundary.
Make interdigital fabric tension clearly readable at this inspection scale. Between every pair of adjacent toes, show a distinct but shallow curved or V-shaped convergence of the same fabric into the natural toe valley. The curves should be visibly darker or slightly denser at their center than the surrounding textile, with nearby knit direction bending toward each valley. Keep each curve local to its toe gap; do not connect them into a crosswise line across the forefoot. They are fabric-tension curves embedded in one surface, not seams, gaps or separate toe sleeves.
Keep the entire lower leg and foot as one uninterrupted textile surface. No transverse forefoot line, continuous stripe, band, seam, ring, edge, separate toe compartment, abrupt color change or abrupt opacity change. Preserve natural anatomy, five toes per foot, separate feet and stable contact.
No footwear, props, text, logo, watermark, collage, artificial coating, hard shine, duplicated/fused/missing anatomy or sexualized framing. Output one REVIEW_REQUIRED candidate only.
```
