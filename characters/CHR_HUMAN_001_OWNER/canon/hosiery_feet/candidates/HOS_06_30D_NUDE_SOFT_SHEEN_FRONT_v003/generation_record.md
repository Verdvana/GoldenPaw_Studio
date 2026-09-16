# HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_06_30D_NUDE_SOFT_SHEEN_FRONT
candidate_id: HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v003
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: GENERATION_BLOCKED_NO_OUTPUT
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_BODY_FRONT_CANON_L1
  - HOS_30D_NUDE_SOFT_SHEEN_LIMITED
reference_count: 2
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v003/HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v003.png"
actual_dimensions_px: null
checksum_sha256: null
qa_status: NOT_APPLICABLE_NO_OUTPUT
generation_result: BLOCKED
block_reason: "Built-in ImageGen output safety moderation rejected the request; no raster output was returned."
request_id: "a7a4cb54-835c-488d-a3a3-04ed87197a4a"
```

## Authorization and lineage

This is a new independent regeneration explicitly requested by the user after v001 and v002 returned no raster due output moderation. Neither blocked attempt is used as a pixel input. No HOS_01–05 image or other generated hosiery candidate is used.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: front identity context, leg/foot geometry, proportions and neutral standing contact only; must not define 30D material.
- `HOS_30D_NUDE_SOFT_SHEEN_LIMITED` / `IMG_2682.jpg`: 30D nude soft-sheen color, thickness impression and textile behavior only; single-source limitation applies and the pictured person/background are excluded.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral hosiery textile inspection reference; one HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v003 candidate, REVIEW_REQUIRED.
Image 1 supplies only approved front leg and foot geometry, proportions and stable standing contact. Image 2 supplies only 30D nude textile color and soft-sheen behavior. Reconstruct independently; do not use previous generated hosiery images.
Show a neutral front-facing garment-fit study on a seamless light-gray studio background, framed from upper legs to both complete feet. Legs naturally separated, feet flat on one floor plane, simple clinical camera and even white light.
The garment is one continuous 30D nude sheer hosiery layer over the visible legs and complete feet, including knees, calves, ankles, heels, insteps and closed toe tips. It is visibly denser than 15D but translucent, with a restrained soft sheen and fine textile texture. Keep coverage continuous and anatomically aligned.
Preserve only the approved leg and foot proportions from Image 1. No shoes, accessories, text, logo, watermark, collage or extra views. No toe seam, reinforced toe boundary, ankle cutoff, bare toe, opacity break, color break, plastic, latex, PVC, rubber, wet coating or body paint. Exact 3:4 vertical frame. Output one REVIEW_REQUIRED candidate only.
```

## QA status

No raster output exists; visual QA and promotion are not applicable. This candidate cannot be used downstream.

## Generation outcome

- One explicitly authorized independent regeneration attempt was blocked at output moderation (`sexual`).
- No image was returned or stored.
- Built-in retries are stopped for this candidate. CLI/API fallback requires separate explicit authorization.
