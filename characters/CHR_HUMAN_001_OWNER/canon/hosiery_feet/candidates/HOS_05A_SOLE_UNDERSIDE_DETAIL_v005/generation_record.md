# HOS_05A_SOLE_UNDERSIDE_DETAIL_v005 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_05A_SOLE_UNDERSIDE_DETAIL
candidate_id: HOS_05A_SOLE_UNDERSIDE_DETAIL_v005
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_BODY_FRONT_CANON_L1
  - HOS_15D_NUDE_MATTE_BAREFOOT
reference_count: 2
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_05A_SOLE_UNDERSIDE_DETAIL_v005/HOS_05A_SOLE_UNDERSIDE_DETAIL_v005.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "66f1f9b1e2d3723b01bb28c3b8db2a00bb68c7f8d3e8444b8dc56e352fffd2d9"
qa_status: PASS_PENDING_USER_REVIEW
```

## Authorization and lineage

This is an independent rebuild explicitly requested after v004 was rejected for nail-like artifacts on the sole-side forefoot. v001–v004 are excluded as pixel inputs. Only the approved Body Master and registered 15D material source are used.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: approved foot proportions and lower-leg-to-foot geometry only; no sole-side nail or hosiery appearance authority.
- `HOS_15D_NUDE_MATTE_BAREFOOT` / `IMG_2562.jpg`: 15D nude matte velvet textile color, transparency, knit grain and tension only; source anatomy and nails are excluded.

## Authoritative candidate scope

- one technical underside-foot view with both complete soles facing camera;
- clearly visible but translucent 15D nude velvet-matte hosiery;
- fine knit grain and soft curved tension between toe bases and across the arch;
- continuous closed-toe textile surface with no sole-side nail shapes.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral textile coverage and foot-structure documentation; exactly one HOS_05A_SOLE_UNDERSIDE_DETAIL_v005 candidate, REVIEW_REQUIRED.
Input images: Image 1 defines only approved foot proportions and lower-leg-to-foot geometry. Image 2 defines only 15D nude matte velvet textile color, translucency, knit grain and stretch response. Reconstruct independently; do not use any previous generated image.
Create one clinical underside-foot coverage study: both complete soles face the camera, feet separated and neutrally flexed, with ankles and short lower-leg continuation visible. Use a seamless light-gray studio background, soft even white light, restrained perspective and exact 3:4 vertical framing.
The entire visible foot area is covered by one continuous pair of 15D nude sheer velvet-matte hosiery. Make the textile clearly visible and slightly substantial, with fine uniform mesh grain across the sole, directional knit stretch over the arch and ball, and soft curved tension folds between adjacent toe bases. The tension curves must be pale diffuse changes in textile weave and translucency, never painted lines.
Important anatomy and nail rule: from the sole-facing view, show NO nail plates, no purple marks, no colored patches and no hard shapes at the bottoms of the toes. Do not invent nails on the plantar surface. All toe tips remain covered by one continuous plain textile veil with softly rounded toe relief only.
Keep the garment continuous over heel, arch, ball, forefoot and closed toe tips. No individual toe sleeves, pockets, ring outlines, hard channels, split-toe construction, sock edge, seam, exposed sole, bare gap, shoes, props, text, logo, watermark or extra view. Never use plastic, latex, PVC, rubber, wet coating, body paint or opaque socks. Output one REVIEW_REQUIRED candidate only.
```

## QA status

Awaiting generated raster and visual review. This candidate cannot be promoted or used downstream without explicit user approval.

## Technical pre-check

- Independent rebuild from the registered 15D material source; v001–v004 were not used as pixel inputs.
- Hosiery is visibly present through fine mesh grain and denser translucent textile response across heel, arch, ball and toes.
- Soft curved tension changes are visible between adjacent toe bases and along the arch; no purple marks, nail plates or hard nail-like artifacts appear on the sole-facing surface.
- Continuous closed-toe textile coverage is maintained; no separate toe sleeves, seams, exposed sole or material break observed.
- Candidate remains `REVIEW_REQUIRED`; no Canon promotion was performed.
