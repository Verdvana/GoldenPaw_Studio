# HOS_08_30D_GRAY_MATTE_FRONT_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.218
identity_md_revision: draft_0.175
asset_id: HOS_08_30D_GRAY_MATTE_FRONT
candidate_id: HOS_08_30D_GRAY_MATTE_FRONT_v001
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
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_08_30D_GRAY_MATTE_FRONT_v001/HOS_08_30D_GRAY_MATTE_FRONT_v001.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "226f956fee32d382d7df53e53a292406c0cd99bd114ef2604b981e044aa483ba"
qa_status: PASS_BY_EXPLICIT_USER_REVIEW
generation_result: SUCCESS
request_id: "not_returned_by_tool"
promoted_asset_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_08_30D_GRAY_MATTE_FRONT/OWNER_HOS_08_30D_GRAY_MATTE_FRONT_CANON_001.png"
approval_record: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_08_30D_GRAY_MATTE_FRONT/approvals/APPROVAL_OWNER_HOS_08_30D_GRAY_MATTE_FRONT_001.md"
```

## Generation outcome and technical pre-check

- Generated successfully; output is 1086×1448 PNG.
- Lower legs through insteps read as effectively non-see-through gray 30D matte.
- Toe-region translucency increases toward the tips, with muted burgundy nail color visible beneath the textile.
- No obvious transverse toe-root line or separate toe construction was observed in the initial review.
- The user explicitly approved v001 on 2026-09-16. The single raster was moved to the approved Canon path; it is not copied.

## Approval outcome

- User approval evidence: `很好，登记`
- Approved scope: straight-on below-knee-to-feet view; 30D gray matte with effectively non-see-through legs/instep and smooth increasing translucency toward the toe tips.
- This component does not define other views, other deniers/colors/finishes, complete owner identity, episode wardrobe, lighting or background.

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: approved lower-leg and foot geometry, proportions and neutral contact only; its 15D nude hosiery appearance is excluded.
- No L0 gray hosiery source exists. 30D gray matte is an explicitly authorized design reconstruction from text only.
- HOS_07 and all previous candidate pixels are excluded.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral lower-leg textile color/material design study; one HOS_08_30D_GRAY_MATTE_FRONT_v001 candidate, REVIEW_REQUIRED.
Use the supplied approved Body Master only for lower-leg and foot geometry, proportions and neutral contact. Reconstruct the textile independently from the written specification; no material photograph or previous candidate is used.
Create one neutral straight-on technical studio photograph matching HOS_01 framing: crop from just below both knees to both complete feet, with both feet separate and flat on one light-gray studio surface. Use even white-balanced clinical lighting, restrained perspective and exact 3:4 vertical framing.
Apply one continuous 30D medium-light smoke-gray matte textile layer. It is visibly thicker, denser and more opaque than 15D. From just below both knees through the calves, ankles and insteps, the gray textile is effectively non-see-through: the underlying warm skin tone must not be visible through those regions. Keep the surface softly matte, evenly gray and woven, never glossy or plastic.
Beginning across the forefoot and continuing toward the rounded toe tips, introduce a smooth gradual translucency gradient. The toe region becomes progressively more transparent toward the tips, allowing increasing warm skin tone to show through; the toe tips have the strongest透肤感 but remain covered by the same textile. There must be no abrupt change-point, stripe, band or construction boundary.
Make the fabric one continuous surface across the feet. Show natural soft toe relief and low-contrast local interdigital knit-direction convergence, without open gaps, separate toe sleeves or a transverse forefoot line. Preserve natural anatomy, five toes per foot, separate feet and stable contact. Muted burgundy toenail color may be faintly visible only beneath the increasingly translucent toe-tip fabric.
No footwear, props, text, logo, watermark, collage, artificial coating, hard shine, duplicated/fused/missing anatomy or sexualized framing. Output one REVIEW_REQUIRED candidate only.
```
