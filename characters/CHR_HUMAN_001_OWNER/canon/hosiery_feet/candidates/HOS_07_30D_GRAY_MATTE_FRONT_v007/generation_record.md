# HOS_07_15D_GRAY_MATTE_FRONT_v007 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.216
identity_md_revision: draft_0.175
asset_id: HOS_07_15D_GRAY_MATTE_FRONT
candidate_id: HOS_07_15D_GRAY_MATTE_FRONT_v007
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: PROMOTED_TO_L1_COMPONENT
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_BODY_FRONT_CANON_L1
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
design_reconstruction_authorized: true
denier_revision_note: "Retain the v005 15D gray matte baseline; reduce translucency and increase only the readability of local tension curves and burgundy nail color beneath the textile."
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_07_30D_GRAY_MATTE_FRONT_v007/HOS_07_30D_GRAY_MATTE_FRONT_v007.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "29833b2de7a2c91b822a542e42843b5902d80ce9597123dce481a9b1bb462df3"
qa_status: PASS_BY_EXPLICIT_USER_REVIEW
generation_result: SUCCESS
request_id: "not_returned_by_tool"
promoted_asset_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_07_15D_GRAY_MATTE_FRONT/OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001.png"
approval_record: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_07_15D_GRAY_MATTE_FRONT/approvals/APPROVAL_OWNER_HOS_07_15D_GRAY_MATTE_FRONT_001.md"
```

## Generation outcome and technical pre-check

- Generated successfully; output is 1086×1448 PNG.
- Pale smoke-gray color and reduced translucency are present.
- Soft burgundy toenail color is visible beneath the textile.
- Local interdigital curves are present but remain delicate; no obvious continuous transverse forefoot line was observed in the initial review.
- The user explicitly approved v007 and requested reclassification as 15D gray matte on 2026-09-16. The single raster was already moved to the approved Canon path; it is not copied.

## Approval outcome

- User approval evidence: `这版可以，但要登记为15d灰色哑光。`
- Approved scope: straight-on below-knee-to-feet view; light smoke-gray 15D matte textile, restrained leg/instep translucency, stronger toe-tip translucency, local interdigital tension curves and softened burgundy toenails beneath the fabric.
- This component does not define other views, other deniers/colors/finishes, complete owner identity, episode wardrobe, lighting or background.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: approved lower-leg and foot geometry, proportions and neutral contact only. Its 15D nude surface appearance is excluded.
- No L0 gray hosiery source exists; light smoke-gray 15D matte is an explicitly authorized design reconstruction from text only.
- No HOS_01–06 pixels and no HOS_07 v001–v006 pixels are used.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral lower-leg textile color/material design study; one HOS_07_30D_GRAY_MATTE_FRONT_v007 candidate, REVIEW_REQUIRED.
Use the supplied approved Body Master only for lower-leg and foot geometry, proportions and neutral contact. Reconstruct the textile independently from the written specification; no material photograph or previous candidate is used.
Create one neutral straight-on technical studio photograph matching HOS_01 framing: crop from just below both knees to both complete feet, with both feet separate and flat on one light-gray studio surface. Use even white-balanced clinical lighting, restrained perspective and exact 3:4 vertical framing.
Apply one continuous light smoke-gray matte 15D textile layer. The color must be pale smoke-gray, clearly lighter than v006 and never charcoal. Keep the textile softly matte and fine. Reduce overall translucency slightly from v006: the legs, ankles and insteps show only a restrained trace of warm skin beneath the gray textile, while remaining visibly textile-covered.
Create a controlled continuous translucency gradient toward the toe tips: the forefoot becomes only modestly more translucent, and the toe tips reveal a little more warm skin than the instep, without becoming bare-looking. Preserve soft, muted burgundy toenail color beneath the textile at the toe tips; it must be visible as low-saturation blurred reddish shapes under the fabric, never crisp nail plates or paint on the surface.
Make the interdigital textile tension clearly visible but local. Between each adjacent pair of toes, show one short, shallow, low-contrast curved tension arc or narrow V-shaped convergence following that individual toe valley. These local curves should be readable as knit-direction changes and slight fabric gathering inside the valley, with several separate curves across the toes. They must not connect into a single line across the forefoot and must remain within the same continuous textile surface.
Keep the entire lower leg and foot as one uninterrupted fabric surface. No continuous transverse forefoot line, no sock edge, no separate toe sleeves, no open gaps, no seam, no ring, no abrupt color or opacity change. Preserve natural anatomy, five toes per foot, separate feet and stable contact.
No footwear, props, text, logo, watermark, collage, artificial coating, hard shine, duplicated/fused/missing anatomy or sexualized framing. Output one REVIEW_REQUIRED candidate only.
```
