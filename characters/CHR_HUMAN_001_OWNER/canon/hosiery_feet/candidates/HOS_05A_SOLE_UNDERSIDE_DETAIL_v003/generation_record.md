# HOS_05A_SOLE_UNDERSIDE_DETAIL_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_05A_SOLE_UNDERSIDE_DETAIL
candidate_id: HOS_05A_SOLE_UNDERSIDE_DETAIL_v003
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen edit"
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids: [HOS_05A_SOLE_UNDERSIDE_DETAIL_v002_EDIT_TARGET]
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: [HOS_05A_SOLE_UNDERSIDE_DETAIL_v002]
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_05A_SOLE_UNDERSIDE_DETAIL_v003/HOS_05A_SOLE_UNDERSIDE_DETAIL_v003.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "eeedcf6c3c121c70c4fbb50de82b87c68c5b8af01771b3d8cf0e4b492e76b926"
qa_status: PASS_PENDING_USER_REVIEW
```

## Authorization and lineage

This is a targeted material-only edit explicitly requested by the user. The v002 image is the edit target only. Preserve its exact sole-facing geometry, foot arrangement, framing and background; do not create a new identity or anatomy authority.

## Edit target responsibility

- `HOS_05A_SOLE_UNDERSIDE_DETAIL_v002_EDIT_TARGET`
  - path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_05A_SOLE_UNDERSIDE_DETAIL_v002/HOS_05A_SOLE_UNDERSIDE_DETAIL_v002.png`
  - responsibility: preserve exact feet, toes, ankles, pose, composition and studio treatment.
  - must_not_define: any new anatomy, identity, pose or other hosiery view.

## Authoritative candidate scope

Only increase the visible density of the 15D nude velvet-matte sheer hosiery slightly and add realistic shallow curved fabric tension between adjacent toe bases. The curves must be soft changes in translucency and knit direction on one continuous textile surface, never separate toe sleeves or hard seams.

## Prompt assembly

```text
Use case: precise-object-edit.
Asset type: neutral textile and underside-foot coverage inspection reference; exactly one HOS_05A_SOLE_UNDERSIDE_DETAIL_v003 candidate, REVIEW_REQUIRED.
Edit target: Image 1, the existing HOS_05A_SOLE_UNDERSIDE_DETAIL_v002 candidate.
Change only the hosiery material response. Preserve the exact two sole-facing feet, toe count and arrangement, foot proportions, ankle/lower-leg continuation, separation, framing, 3:4 crop, light-gray background, camera angle and shadows.
Make the 15D nude sheer velvet-matte hosiery visibly a little denser than the edit target, but still translucent and clearly thin hosiery. Add more readable fine-knit texture and natural fabric tension over the soles, especially through the arches, balls of the feet and toe pads. Between adjacent toe bases, add shallow soft curved tension arcs caused by the continuous textile stretching over the toe relief; these are diffuse changes in fabric density and knit direction, not drawn lines.
Keep one uninterrupted garment across heel, arch, forefoot and all closed toe tips. Do not create individual toe sleeves, toe pockets, ring-like outlines, hard channels, seams or a split-toe construction.
Do not change anatomy, pose, crop, background or color balance. No bare gaps, exposed sole, shoe, nail color on top of fabric, plastic, latex, PVC, rubber, wet coating, body paint, harsh gloss, text, logo, watermark or extra view. Output one REVIEW_REQUIRED candidate only.
```

## QA status

Awaiting edited raster and visual review. This candidate cannot be promoted or used downstream without explicit user approval.

## Technical pre-check

- Sole-facing geometry, toe arrangement, framing and background preserved from v002.
- Hosiery is visibly denser while remaining translucent 15D nude velvet-matte.
- Fine knit texture and shallow curved tension changes are visible between adjacent toe bases; they read as one continuous textile surface, not separate toe sleeves.
- No exposed sole, hard seam, shoe, material break or plastic appearance observed.
