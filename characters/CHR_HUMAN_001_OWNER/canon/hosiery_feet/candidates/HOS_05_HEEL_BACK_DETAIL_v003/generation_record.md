# HOS_05_HEEL_BACK_DETAIL_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_05_HEEL_BACK_DETAIL
candidate_id: HOS_05_HEEL_BACK_DETAIL_v003
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen edit"
status: PROMOTED_TO_L1_COMPONENT
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - HOS_05_HEEL_BACK_DETAIL_v002_EDIT_TARGET
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_05_HEEL_BACK_DETAIL/OWNER_HOS_05_HEEL_BACK_DETAIL_CANON_001.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "a921ad8fce232516e7696733c9c6351ef1b7c3ee3a0c85323c5a00246b8dff7b"
qa_status: PASS_BY_EXPLICIT_USER_REVIEW
promoted_asset_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_05_HEEL_BACK_DETAIL/OWNER_HOS_05_HEEL_BACK_DETAIL_CANON_001.png"
approval_record: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_05_HEEL_BACK_DETAIL/approvals/APPROVAL_OWNER_HOS_05_HEEL_BACK_DETAIL_001.md"
```

## Authorization and lineage

This candidate is a targeted non-destructive material edit requested by the user. The v002 image is the edit target only; it is not treated as a new identity, body, pose or hosiery authority. Preserve the existing geometry and composition, and change only the subtle textile response.

## Edit target responsibility

- `HOS_05_HEEL_BACK_DETAIL_v002_EDIT_TARGET`
  - path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_05_HEEL_BACK_DETAIL_v002/HOS_05_HEEL_BACK_DETAIL_v002.png`
  - responsibility: preserve exact rear-view framing, lower-leg/heel anatomy, foot placement, floor contact, background and existing continuous coverage.
  - must_not_define: any new identity, body, pose, hosiery construction, seam, opacity break or exposed skin.

## Authoritative candidate scope

Only refine the hosiery appearance: add a very slight realistic textile sheen and a soft pale edge response along the ankle, Achilles and heel contours where light naturally catches the thin fabric. Keep the effect restrained and integrated into the 15D sheer textile; it must not become glossy or create a boundary.

## Prompt assembly

```text
Use case: precise-object-edit.
Asset type: neutral clinical textile quality-control reference; exactly one HOS_05_HEEL_BACK_DETAIL_v003 candidate, REVIEW_REQUIRED.
Edit target: Image 1, the existing HOS_05_HEEL_BACK_DETAIL_v002 candidate.
Primary request: make one subtle material-only refinement. Preserve the exact straight rear view, both lower legs, ankles, Achilles contours, heels, feet, floor contact, light-gray studio background, framing and 3:4 composition.
Materials/textures: make the 15D light-nude sheer pantyhose slightly more visibly textile-like by adding a very restrained soft satin-like hosiery sheen, not a hard highlight. Add a delicate pale edge lift/faint whitish translucency exactly where the thin fabric catches light along the outer ankle, Achilles and heel contours. Keep the effect soft, diffuse and naturally blended, with fine knit presence and continuous coverage.
Constraints: change only the hosiery material response. Do not change anatomy, proportions, foot separation, pose, camera, crop, background, skin tone, color balance or floor shadows. No sock edge, seam, band, opacity break, bare skin gap, exposed heel, shoe, nail paint on top of fabric, plastic, latex, PVC, rubber, wet gloss, liquid coating or body paint.
Output one REVIEW_REQUIRED candidate only.
```

## QA status

The edited raster was moved to the approved Canon path after the user's explicit approval on 2026-09-16. The candidate directory retains this record and provenance only; the candidate raster is not duplicated.

## Technical pre-check

- Material-only edit preserved the exact rear view, foot geometry, floor contact, framing and background from v002.
- 15D hosiery now has a restrained soft sheen and faint pale edge lift along ankle/Achilles/heel contours.
- No hard highlight, sock edge, seam, opacity break, exposed heel, shoe or plastic/latex appearance observed.
- Candidate was promoted to `OWNER_HOS_05_HEEL_BACK_DETAIL_CANON_001` after explicit user approval.
