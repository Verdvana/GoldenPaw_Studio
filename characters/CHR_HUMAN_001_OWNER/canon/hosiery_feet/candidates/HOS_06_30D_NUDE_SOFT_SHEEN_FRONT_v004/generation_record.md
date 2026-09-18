# HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v004 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.175
asset_id: HOS_06_30D_NUDE_SOFT_SHEEN_FRONT
candidate_id: HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v004
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v004/HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v004.png"
actual_dimensions_px: null
checksum_sha256: null
qa_status: NOT_APPLICABLE_NO_OUTPUT
generation_result: BLOCKED
block_reason: "Built-in ImageGen output safety moderation rejected the request; no raster output was returned."
request_id: "9ab359ac-5646-4264-ae1b-b58d81af283e"
generated_output_path: null
```

## Reference responsibilities

1. `OWNER_BODY_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v009/BODY_01_FRONT_v009.jpg`
   - responsibility: approved owner identity context, natural body/leg/foot geometry, proportions and neutral standing contact only.
   - must_not_define: 30D material color, denier, finish or textile response; its visible 15D hosiery is excluded.
2. `HOS_30D_NUDE_SOFT_SHEEN_LIMITED`
   - path: `materials/hosiery/source_library/raw/30d_nude_soft_sheen/IMG_2682.jpg`
   - responsibility: 30D nude color, thickness impression, restrained soft sheen and textile behavior only.
   - must_not_define: owner identity, body/foot anatomy, pose, skin pigmentation, nail color, clothing, lighting or background.

Coverage limitation: this 30D material set contains one source image; this candidate does not claim broader material coverage than that source supports.

## Authoritative candidate scope

- straight-on front view from upper thigh through both complete feet;
- visibly denser-than-15D but translucent 30D nude soft-sheen pantyhose;
- uninterrupted closed-toe textile coverage through thighs, knees, calves, ankles, heels, insteps, forefeet and toe tips.

The candidate must not define 15D calibration material, other hosiery colors/finishes, complete owner identity, episode wardrobe, lighting or background. v001–v003 are no-output blocked attempts and are not inputs.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral technical hosiery textile inspection reference; one HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v004 candidate, REVIEW_REQUIRED.
Input images: Image 1 defines only approved owner front identity context, natural leg and foot geometry, proportions and neutral standing contact. Image 2 defines only limited-source 30D nude textile color, denier impression and restrained soft-sheen behavior. Reconstruct independently; do not import the material image's person, pose or background. Do not use previous generated hosiery images.
Primary request: create one neutral front-facing garment-fit documentation image on a seamless light-gray studio background, framed from upper thigh to both complete feet. Legs naturally separated, feet flat on one floor plane, simple clinical camera and even white light. This is adult apparel-material documentation, not fashion or glamour.
Materials/textures: one continuous pair of 30D nude pantyhose covers the visible legs and complete feet, including knees, calves, ankles, heels, insteps, forefeet and closed toe tips. The textile is visibly denser and more substantial than 15D while remaining translucent, with fine textile presence and controlled soft sheen, never hard reflective gloss.
Composition/framing: exact 3:4 vertical frame; full lower body from upper thigh to complete feet inside frame; restrained 70–100mm perspective.
Constraints: preserve only approved front leg and foot proportions from Image 1. Keep fabric coverage continuous and anatomically aligned across every joint and foot transition. Burgundy toenails, if visible, remain faintly beneath the closed-toe fabric and are never painted on top. No waistband shown, shoes, accessories, supports, text, logo, watermark, collage or extra views.
Avoid: 15D-thin appearance, opaque socks, open-toe construction, toe-cap seam, reinforced toe boundary, ankle cutoff, bare toes, opacity/color break, glossy wet plastic, latex, PVC, rubber, liquid coating, body paint, duplicated/fused/missing anatomy or sexualized framing.
Output one REVIEW_REQUIRED candidate only.
```

## Generation outcome

- One independent v004 attempt was blocked at output moderation (`sexual`).
- No image was returned, stored, inspected, promoted, or used downstream.
- v001–v004 remain non-authoritative; CLI/API fallback requires separate explicit user authorization.
