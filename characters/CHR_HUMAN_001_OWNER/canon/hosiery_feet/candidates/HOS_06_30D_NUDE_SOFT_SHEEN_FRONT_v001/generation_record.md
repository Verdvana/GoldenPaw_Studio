# HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_06_30D_NUDE_SOFT_SHEEN_FRONT
candidate_id: HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v001
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: GENERATION_BLOCKED_NO_OUTPUT
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids: [OWNER_BODY_FRONT_CANON_L1, HOS_30D_NUDE_SOFT_SHEEN_LIMITED]
reference_count: 2
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v001/HOS_06_30D_NUDE_SOFT_SHEEN_FRONT_v001.png"
actual_dimensions_px: null
checksum_sha256: null
qa_status: NOT_APPLICABLE_NO_OUTPUT
generation_result: BLOCKED
block_reason: "ImageGen output safety moderation rejected the request; no raster output was returned."
request_id: "70a3c430-bc34-48b9-93ca-945f3181877a"
generated_output_path: null
```

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: owner identity context, front body/leg/foot geometry and proportions only; it must not define 30D material.
- `HOS_30D_NUDE_SOFT_SHEEN_LIMITED` / `IMG_2682.jpg`: 30D nude soft-sheen color, thickness impression, subtle sheen and textile behavior only; single-source coverage limitation applies.

No HOS_01–05 pixels and no previous generated candidate are used.

## Generation outcome

- Attempted on 2026-09-15 using the two declared local references.
- Result: blocked at ImageGen output moderation (`sexual`).
- No candidate raster was created, copied, inspected, or made available for downstream reference.

## Prompt assembly

```text
Create one photorealistic, neutral technical apparel-material calibration image for adult character CHR_HUMAN_001_OWNER, asset HOS_06_30D_NUDE_SOFT_SHEEN_FRONT.

Use the approved Body Master only for the owner's front identity context, natural 168 cm / 60 kg body proportions, leg and foot geometry, and neutral standing contact. Use the single supplied 30D nude soft-sheen material reference only for color, thickness impression and restrained soft sheen. Do not let the material reference define anatomy, identity, pose or background. Do not use previous generated hosiery images.

Show a straight-on full front view from upper thigh through both complete feet, with both legs naturally separated and fully visible. Use a neutral technical studio setup, restrained perspective, even white-balanced lighting and a light gray seamless background. This is apparel-material calibration, not fashion or glamour.

Apply one continuous pair of 30D nude pantyhose from upper thigh through knees, calves, ankles, heels, insteps, forefeet and closed toe tips. Define a slightly denser, more substantial textile than 15D while keeping it smooth and translucent. Show a controlled soft sheen—not glossy, wet or reflective plastic—and fine textile presence over the legs and feet. The garment must have uninterrupted coverage with no waistband shown, no ankle cutoff, no exposed toes, no toe-cap seam, no reinforced toe boundary, no opacity break and no color break.

Preserve natural leg and foot proportions from the Body Master. Burgundy toenails may be faintly softened beneath the closed-toe fabric, never painted on top. No shoes, accessories, supports, text, logo, watermark, collage or extra views. Exact 3:4 vertical frame. Output one REVIEW_REQUIRED candidate only.
```
