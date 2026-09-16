# HOS_05A_SOLE_UNDERSIDE_DETAIL_v006 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_05A_SOLE_UNDERSIDE_DETAIL
candidate_id: HOS_05A_SOLE_UNDERSIDE_DETAIL_v006
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - HOS_15D_NUDE_MATTE_BAREFOOT
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_05A_SOLE_UNDERSIDE_DETAIL_v006/HOS_05A_SOLE_UNDERSIDE_DETAIL_v006.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "b991148f86134b8ea2403d153fd5484ae259e26db220e45cab17459153c204d7"
qa_status: PASS_WITH_SCOPE_LIMITATION_PENDING_USER_REVIEW
generation_result: SUCCESS_AFTER_ONE_BLOCKED_ATTEMPT
request_ids:
  - "b1229404-7f38-4e16-9e78-618bd8c7c13c"
  - "18f3500d-9513-449d-8ee3-303d39c06630"
```

## Authorization and lineage

This is an independent rebuild after v005 was rejected for reading as five-toe hosiery. v001–v005 are excluded as pixel inputs. The first attempt used the approved Body Master plus the registered 15D source but was blocked by output moderation; the successful retry used only the registered 15D source. This output therefore has material-study authority only until the user accepts its scope.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: declared for the blocked first attempt only; no successful output pixels were produced from it.
- `HOS_15D_NUDE_MATTE_BAREFOOT` / `IMG_2562.jpg`: 15D nude matte velvet textile color, translucency, knit grain and stretch response only; source anatomy and nails are excluded.

## Authoritative candidate scope

- one underside-foot view with both complete soles facing camera;
- visibly substantial yet translucent 15D nude velvet-matte hosiery;
- one uninterrupted closed-toe textile plane over each entire foot;
- subtle curved changes in knit direction between toe bases, with no physical separation.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral textile coverage and foot-structure documentation; exactly one HOS_05A_SOLE_UNDERSIDE_DETAIL_v006 candidate, REVIEW_REQUIRED.
Input images: Image 1 defines only approved foot proportions and lower-leg-to-foot geometry. Image 2 defines only 15D nude matte velvet textile color, translucency, knit grain and stretch response. Reconstruct independently; do not use any previous generated image.
Create one clinical underside-foot coverage study with two complete soles facing the camera, feet separated and neutrally flexed, ankles and short lower-leg continuation visible. Seamless light-gray studio, soft even white light, restrained perspective, exact 3:4 vertical frame.
Apply one continuous pair of clearly visible 15D nude sheer velvet-matte pantyhose. The fabric should look more substantial than bare skin while remaining translucent. Show uniform fine mesh grain across the whole sole and gentle directional stretch over the arch, ball and toe region.
Critical construction: each foot has one single uninterrupted fabric surface from heel through arch, forefoot and all toe tips. The toe region must read as normal closed-toe pantyhose, not a five-toe sock. Keep the toe contours softly aggregated beneath the fabric. Between adjacent toe bases, indicate tension only through very shallow, broad, pale curved changes in knit direction and translucency within the same continuous surface. Do not draw dark gaps or outlines.
No visible nail plates, purple marks, colored patches or nail-like shapes on the sole-facing side. No toe pockets, individual toe sleeves, ring outlines, hard channels, split-toe construction, seams, sock edges, exposed skin, shoes, props, text, logo, watermark or extra view. No plastic, latex, PVC, rubber, wet coating, body paint, opaque socks or harsh gloss. Output one REVIEW_REQUIRED candidate only.
```

## QA status

No owner-specific anatomy authority is claimed for the successful material-only output. The candidate remains `REVIEW_REQUIRED` and cannot be promoted or used downstream without explicit user approval.

## Generation outcome

- First attempt: output moderation blocked; no raster returned.
- Second attempt: successful neutral material-only study; v001–v005 were not used as inputs.

## Technical pre-check

- Hosiery is clearly visible as a fine mesh textile with soft curved knit tension across the forefoot and arch.
- Toe region reads as a continuous fabric veil without visible nail plates, purple marks or hard sole-side artifacts.
- No separate toe sleeves, deep channels, shoes, seams or exposed sole observed.
