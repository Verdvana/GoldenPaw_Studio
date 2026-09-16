# HOS_05A_SOLE_UNDERSIDE_DETAIL_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_05A_SOLE_UNDERSIDE_DETAIL
candidate_id: HOS_05A_SOLE_UNDERSIDE_DETAIL_v002
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen edit"
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - HOS_05A_SOLE_UNDERSIDE_DETAIL_v001_EDIT_TARGET
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: [HOS_05A_SOLE_UNDERSIDE_DETAIL_v001]
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_05A_SOLE_UNDERSIDE_DETAIL_v002/HOS_05A_SOLE_UNDERSIDE_DETAIL_v002.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "28637e1123d1d7cd1bd768c647e3b943c998d78561744fd51c4222e7c6a3b9a1"
qa_status: PASS_PENDING_USER_REVIEW
```

## Authorization and lineage

This is a targeted material-only edit explicitly requested by the user. The v001 image is the edit target only. Preserve the exact underside-foot geometry, toe arrangement, framing and background; do not create a new identity, pose or anatomy authority.

## Edit target responsibility

- `HOS_05A_SOLE_UNDERSIDE_DETAIL_v001_EDIT_TARGET`
  - path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_05A_SOLE_UNDERSIDE_DETAIL_v001/HOS_05A_SOLE_UNDERSIDE_DETAIL_v001.png`
  - responsibility: preserve the exact sole-facing composition, foot proportions, ankle continuation and floor/background treatment.
  - must_not_define: changes to anatomy, pose, identity or other hosiery views.

## Authoritative candidate scope

Only make the hosiery visually a little denser than v001 while retaining 15D sheer nude matte velvet character. Add localized natural fabric tension and fine knit definition over the sole, arch, ball and toe areas. Do not make it opaque, glossy or plastic.

## Prompt assembly

```text
Use case: precise-object-edit.
Asset type: neutral textile and underside-foot coverage inspection reference; exactly one HOS_05A_SOLE_UNDERSIDE_DETAIL_v002 candidate, REVIEW_REQUIRED.
Edit target: Image 1, the existing HOS_05A_SOLE_UNDERSIDE_DETAIL_v001 candidate.
Change only the hosiery material response. Preserve the exact two sole-facing feet, toe arrangement, foot proportions, ankle/lower-leg continuation, separation, framing, 3:4 crop, light-gray background, shadows and camera angle.
Make the 15D nude sheer velvet-matte hosiery just slightly denser and more visibly present than the edit target, while remaining translucent and delicate. In the sole close-up, add subtle realistic fabric tension and fine knit texture following the arch, ball of foot and toe pads, with gentle soft matte shading. Keep the textile continuous across heel, arch, forefoot and all closed toe tips.
Do not change anatomy or pose. Do not add seams, toe pockets, bands, sock edges, bare gaps, exposed skin, nail color on top of fabric, shoes, props, text, logo, watermark or extra views. Never make the material opaque, glossy, wet, plastic, latex, PVC, rubber, liquid coating or body paint. Output one REVIEW_REQUIRED candidate only.
```

## QA status

Awaiting edited raster and visual review. This candidate cannot be promoted or used downstream without explicit user approval.

## Technical pre-check

- Exact sole-facing composition, foot geometry, toe arrangement, framing and background preserved from v001.
- Hosiery reads slightly denser while remaining 15D sheer nude velvet-matte; fine knit/tension is more visible across the arches, balls and toe pads.
- Continuous coverage remains visible across heel, arch, forefoot and closed toe tips; no shoe, seam, exposed skin or material break observed.
- Candidate remains `REVIEW_REQUIRED`; no Canon promotion was performed.
