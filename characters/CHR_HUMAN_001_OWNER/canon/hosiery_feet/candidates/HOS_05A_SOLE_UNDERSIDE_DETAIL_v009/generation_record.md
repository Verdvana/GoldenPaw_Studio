# HOS_05A_SOLE_UNDERSIDE_DETAIL_v009 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_05A_SOLE_UNDERSIDE_DETAIL
candidate_id: HOS_05A_SOLE_UNDERSIDE_DETAIL_v009
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: PROMOTED_TO_L1_COMPONENT
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - HOS_15D_NUDE_MATTE_BAREFOOT
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_05A_SOLE_UNDERSIDE_DETAIL/OWNER_HOS_05A_SOLE_UNDERSIDE_DETAIL_CANON_001.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "b71454c20f8db07cf7f85e83983b7f8c7af73a796be42faf320026dddec3f95b"
qa_status: PASS_BY_EXPLICIT_USER_REVIEW
promoted_asset_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_05A_SOLE_UNDERSIDE_DETAIL/OWNER_HOS_05A_SOLE_UNDERSIDE_DETAIL_CANON_001.png"
approval_record: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_05A_SOLE_UNDERSIDE_DETAIL/approvals/APPROVAL_OWNER_HOS_05A_SOLE_UNDERSIDE_DETAIL_001.md"
generation_result: SUCCESS_AFTER_ONE_BLOCKED_ATTEMPT
request_ids:
  - "1a685449-d364-4dd3-83e1-1a6465d2ba25"
  - "897ef60c-774e-4aa2-81e8-3d2d9bdedf9b"
```

## Authorization and lineage

This is an independent rebuild after v008 was rejected for excessive plantar wrinkles. v001–v008 are excluded as pixel inputs. The first attempt used the approved Body Master plus the registered 15D source but was blocked by output moderation; the successful retry used only the registered 15D source. This output therefore has material-study authority only until the user accepts its scope.

## Authoritative candidate scope

- complete paired sole-facing foot detail with natural heel, arch, ball and toe relief;
- 15D nude velvet-matte sheer hosiery visibly present but smooth and closely fitted;
- fine uniform knit grain with only shallow, broad, anatomically plausible tension changes;
- no prominent wrinkles, pleats, folds or radial creases across the plantar surface;
- one continuous closed-toe fabric surface with no five-toe construction.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral hosiery material and plantar-foot coverage documentation; exactly one HOS_05A_SOLE_UNDERSIDE_DETAIL_v009 candidate, REVIEW_REQUIRED.
Input images: Image 1 defines only approved foot proportions and lower-leg-to-foot geometry. Image 2 defines only 15D nude matte velvet textile color, fine knit grain, translucency and smooth stretch response. Reconstruct independently; do not use any previous generated image.
Create one clean clinical underside-foot study with two complete soles facing the camera, separated and naturally aligned, with short ankle continuation. Seamless light-gray studio background, soft even light, restrained perspective, exact 3:4 vertical frame.
Apply one continuous pair of light-nude 15D sheer pantyhose. The material must read as smooth, close-fitting velvet-matte hosiery: clearly visible fine uniform micro-mesh and soft translucent density, slightly more substantial than bare skin, with no glossy coating.
Material behavior: fabric follows the sole contours smoothly and evenly. Show only very shallow broad changes in knit direction at the arch, ball and between toe bases to suggest gentle tension. These are subtle low-contrast textile-direction changes, not wrinkles. Keep the plantar surface smooth: absolutely no radiating creases, deep folds, pleats, bunching, gathered fabric, ripples, crumpled areas or hard fold lines.
Toe construction: each foot has one uninterrupted continuous closed-toe fabric veil. Toes appear only as soft rounded relief beneath the textile. No visible nail plates or colored marks on the sole-facing side; no toe gaps, individual toe sleeves, pockets, ring outlines, dark channels or split-toe construction.
Preserve natural foot proportions and coherent anatomy. No shoes, supports, props, text, logo, watermark, collage, exposed sole, bare gaps, sock edges, seams, opaque socks, plastic, latex, PVC, rubber, wet coating, body paint, harsh gloss or sexualized framing. Output one REVIEW_REQUIRED candidate only.
```

## QA status

No owner-specific anatomy authority is claimed for the successful material-only output. The edited raster was moved to the approved Canon path after the user's explicit approval on 2026-09-16; the candidate directory retains provenance only and no duplicate raster.

## Generation outcome

- First attempt: output moderation blocked; no raster returned.
- Second attempt: successful neutral material-only study; v001–v008 were not used as inputs.

## Technical pre-check

- Hosiery reads as a smooth, fine-mesh velvet-matte textile with no prominent plantar wrinkles or folds.
- Toe region is a continuous fabric veil with no visible nail plates, colored marks, toe sleeves or split-toe construction.
- Only shallow natural relief remains at toe bases; the surface is not gathered, crumpled or radially creased.
