# HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_06_30D_NUDE_SOFT_SHEEN_FRONT
candidate_id: HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v002
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v002/HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v002.png"
actual_dimensions_px: null
checksum_sha256: null
qa_status: NOT_APPLICABLE_NO_OUTPUT
generation_result: BLOCKED
block_reason: "Two built-in ImageGen attempts were rejected at output safety moderation; no raster output was returned."
request_ids:
  - "9884c36d-e1f5-4a7e-853b-213f664fb6fd"
  - "03743cf1-9577-4a34-b29a-b7d356360a17"
```

## Authorization and lineage

This is one independent retry of the incomplete HOS_06 component. The v001 request returned no raster after output moderation and is not an input. No HOS_01–05 image or other generated hosiery candidate is used.

## Reference responsibilities

1. `OWNER_BODY_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v009/BODY_01_FRONT_v009.jpg`
   - SHA-256: `964c3b9d72c6688881b8ebfa4c6fc1bcfea04c998351352fabfdc8f4951666f6`
   - responsibility: owner front identity context, natural body/leg/foot geometry, proportions and neutral standing contact only.
   - must_not_define: 30D material color, denier, finish or textile response.
2. `HOS_30D_NUDE_SOFT_SHEEN_LIMITED`
   - path: `materials/hosiery/source_library/raw/30d_nude_soft_sheen/IMG_2682.jpg`
   - SHA-256: `46e3f2ce46c15839759e3602f174e0f1e329feffb046589e7adf3114d0248ff4`
   - responsibility: 30D nude color, thickness impression, restrained soft sheen and textile behavior only.
   - must_not_define: owner identity, body/foot anatomy, pose, skin pigmentation, nail color, clothing, lighting or background.

Coverage limitation: the 30D nude soft-sheen material set currently contains one source image; this candidate does not claim broader material coverage than that source supports.

## Authoritative candidate scope

- straight-on front view from upper thigh through both complete feet;
- 30D nude soft-sheen pantyhose, visibly denser than 15D but still translucent;
- uninterrupted closed-toe coverage across thighs, knees, calves, ankles, heels, insteps, forefeet and toe tips.

This candidate must not define the 15D calibration material, other hosiery colors/finishes, complete owner identity, episode wardrobe, lighting or background.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral apparel-material calibration reference; exactly one HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v002 candidate, REVIEW_REQUIRED.
Input images: Image 1 defines only the approved owner's front identity context, natural body/leg/foot geometry, proportions and neutral contact. Image 2 defines only 30D nude soft-sheen color, denier impression and restrained textile sheen. The material reference is a single-source limited set; do not import its person, pose or background. Do not use any previous generated hosiery image.
Primary request: show one straight-on full front view from upper thigh through both complete feet, legs naturally separated and fully visible, standing neutrally on one light-gray seamless studio surface. This is neutral technical apparel-material documentation, not fashion or glamour.
Materials/textures: apply one continuous pair of 30D nude pantyhose from upper thigh through knees, calves, ankles, heels, insteps, forefeet and closed toe tips. The fabric is slightly denser and more substantial than 15D while remaining translucent. Show a controlled soft sheen and fine textile presence, never a hard reflective highlight. Maintain uninterrupted coverage and natural tension through every joint and foot transition.
Composition/framing: exact 3:4 vertical frame; full lower body from upper thigh to complete feet inside frame; restrained natural perspective.
Lighting/mood: soft even white-balanced clinical studio lighting, neutral light-gray background.
Constraints: preserve the approved front body and foot proportions. Burgundy toenails, if faintly visible, remain beneath the closed-toe fabric and are not painted on top. No waistband shown, shoes, accessories, supports, text, logo, watermark, collage or extra views.
Avoid: 15D-thin appearance, opaque socks, open-toe construction, toe-cap seam, reinforced toe boundary, ankle cutoff, bare toes, opacity/color break, glossy wet plastic, latex, PVC, rubber, liquid coating, body paint, duplicated/fused/missing anatomy or sexualized framing.
Output one REVIEW_REQUIRED candidate only.
```

## QA status

No raster output exists after two built-in ImageGen attempts; visual QA and promotion are not applicable. This candidate cannot be used downstream.

## Generation outcome

- Attempt 1: output moderation blocked (`sexual`); no raster returned.
- Attempt 2: one targeted, more neutral garment-fit wording retry was also blocked (`sexual`); no raster returned.
- Decision: stop built-in retries under the ImageGen workflow. CLI/API fallback would require explicit user authorization and is not used.
