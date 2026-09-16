# HOS_07_30D_GRAY_MATTE_FRONT_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.211
identity_md_revision: draft_0.175
asset_id: HOS_07_30D_GRAY_MATTE_FRONT
candidate_id: HOS_07_30D_GRAY_MATTE_FRONT_v002
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_07_30D_GRAY_MATTE_FRONT_v002/HOS_07_30D_GRAY_MATTE_FRONT_v002.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "de92f9dd9f76b25498496fb96577e0a96c088edf9b97ada67f0822a4aedec13b"
qa_status: TECHNICAL_PRECHECK_PASS_REVIEW_REQUIRED
generation_result: SUCCESS
request_id: "not_returned_by_tool"
```

## Generation outcome and technical pre-check

- Generated successfully after changing the crop to below-knee-to-feet; output is 1086×1448 PNG.
- Gray 30D matte design reconstruction, continuous coverage, natural anatomy and stable contact pass the technical pre-check.
- No obvious transverse toe-root line or separate toe-compartment construction was observed in the initial review.
- Candidate remains `REVIEW_REQUIRED`; it is not approved and must not be used as a downstream pixel reference.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: approved lower-leg and foot geometry, proportions and neutral contact only. Its 15D nude appearance is excluded.
- No L0 gray hosiery source exists; gray 30D matte is an explicitly authorized design reconstruction from text only.
- No HOS_01–06 pixels and no HOS_07 v001 pixels are used.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral lower-leg textile color/material design study; one HOS_07_30D_GRAY_MATTE_FRONT_v002 candidate, REVIEW_REQUIRED.
Use the supplied approved Body Master only for lower-leg and foot geometry, proportions and neutral contact. Do not copy its 15D nude surface. Reconstruct the gray 30D textile independently from the written specification; no material photograph is used.
Create one neutral straight-on technical studio photograph matching HOS_01 framing: crop from just below both knees to both complete feet, with both feet separate and flat on one light-gray studio surface. Use even white-balanced clinical lighting, restrained perspective and exact 3:4 vertical framing.
Apply one continuous 30D cool medium-gray matte textile layer over the lower legs and complete feet. It is moderately dense, softly matte, finely woven and subtly translucent, more substantial than 15D but not opaque. Keep the gray neutral and even, with no shine or plastic-like surface.
The textile remains one uninterrupted continuous surface from below the knees through calves, ankles, heels, insteps, forefeet and toe tips. At each toe, allow only a smooth broad change in translucency along its length, with soft underlying toe relief and no construction feature.
Keep the forefoot smooth and continuous. Do not draw any straight or curved crosswise mark, stripe, band, seam, ring, edge, separate toe compartment, abrupt opacity change or color break. Preserve natural anatomy, five toes per foot, separate feet and stable contact.
No footwear, props, text, logo, watermark, collage, artificial coating, hard shine, duplicated/fused/missing anatomy or sexualized framing. Output one REVIEW_REQUIRED candidate only.
```
