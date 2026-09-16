# HOS_07_30D_GRAY_MATTE_FRONT_v005 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.214
identity_md_revision: draft_0.175
asset_id: HOS_07_30D_GRAY_MATTE_FRONT
candidate_id: HOS_07_30D_GRAY_MATTE_FRONT_v005
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
denier_revision_note: "User states v004 thickness is acceptable as 15D gray matte; this retry uses 15D gray matte behavior while retaining HOS_07 working asset slot."
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_07_30D_GRAY_MATTE_FRONT_v005/HOS_07_30D_GRAY_MATTE_FRONT_v005.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "d914de0331383d0c535ceb9647dcfcec571946de2e0cfae49f414c183f88f705"
qa_status: TECHNICAL_PRECHECK_PASS_REVIEW_REQUIRED
generation_result: SUCCESS
request_id: "not_returned_by_tool"
```

## Generation outcome and technical pre-check

- Generated successfully; output is 1086×1448 PNG.
- The requested 15D light smoke-gray matte behavior is present.
- Interdigital textile tension is visibly expressed as short, shallow local V-shaped/converging curves between adjacent toes.
- The curves remain embedded in one continuous textile surface; no obvious transverse toe-root line or separate toe compartments were observed in the initial review.
- Candidate remains `REVIEW_REQUIRED`; it is not approved and must not be used as a downstream pixel reference.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: approved lower-leg and foot geometry, proportions and neutral contact only. Its surface appearance is excluded.
- No L0 gray hosiery source exists; 15D gray matte is an explicitly authorized design reconstruction from text only for this retry.
- No HOS_01–06 pixels and no HOS_07 v001–v004 pixels are used.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral lower-leg textile color/material design study; one HOS_07_30D_GRAY_MATTE_FRONT_v005 candidate, REVIEW_REQUIRED.
Use the supplied approved Body Master only for lower-leg and foot geometry, proportions and neutral contact. Reconstruct the textile independently from the written specification; no material photograph or previous candidate is used.
Create one neutral straight-on technical studio photograph matching HOS_01 framing: crop from just below both knees to both complete feet, with both feet separate and flat on one light-gray studio surface. Use even white-balanced clinical lighting, restrained perspective and exact 3:4 vertical framing.
Apply one continuous 15D light smoke-gray matte textile layer. It is sheer, fine and softly translucent, with a delicate woven presence and restrained matte response. The gray is light smoke-gray, not charcoal. Keep the appearance clearly textile, never bare skin, opaque gray paint or plastic.
Show a smooth vertical translucency gradient: lower legs and insteps are only subtly translucent; across the forefoot the underlying warm tone becomes gradually more visible toward the rounded toe tips. Keep the change continuous with no step or boundary.
Make the interdigital fabric tension visibly readable at inspection scale. Between each pair of adjacent toes, draw a shallow, short V-shaped or gently curved convergence of the same fabric toward the natural toe valley. Each curve follows the local gap between two toes, is narrow and low-contrast, and represents fabric tension and knit-direction convergence. There should be several separate local curves, one per interdigital valley, not one line across the foot. The curves must remain embedded in the same continuous fabric surface, with no open gaps, no separate toe sleeves, no seams and no transverse forefoot line.
The entire lower leg and foot remain one uninterrupted textile surface. Preserve natural anatomy, five toes per foot, separate feet and stable contact. No footwear, props, text, logo, watermark, collage, artificial coating, hard shine, duplicated/fused/missing anatomy or sexualized framing. Output one REVIEW_REQUIRED candidate only.
```
