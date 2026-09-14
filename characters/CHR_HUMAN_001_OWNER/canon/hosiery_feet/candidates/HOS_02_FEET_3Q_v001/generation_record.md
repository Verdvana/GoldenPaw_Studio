# HOS_02_FEET_3Q_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.148
identity_md_revision: draft_0.136
asset_id: HOS_02_FEET_3Q
candidate_id: HOS_02_FEET_3Q_v001
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in image_gen"
status: GENERATION_BLOCKED_NO_OUTPUT
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: null
reference_set_ids:
  - OWNER_BODY_LEFT_3Q_CANON_L1
  - HOS_15D_NUDE_MATTE_FOOT_CROP
reference_count: 2
previous_ai_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_02_FEET_3Q_v001/HOS_02_FEET_3Q_v001.png"
checksum_sha256: null
qa_status: NOT_APPLICABLE_NO_OUTPUT
```

## Authorization and lineage

The user's instruction to begin the next item authorizes exactly one independent `HOS_02_FEET_3Q_v001` candidate. No HOS_01 raster, previous hosiery candidate, Pose, Expression or Shot is attached. The approved HOS_01 remains excluded because its authority is front-view only.

## Reference responsibilities

1. `OWNER_BODY_LEFT_3Q_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_02_LEFT_3Q/OWNER_BODY_02_LEFT_3Q_CANON_001.png`
   - SHA-256: `f364b5c9b398c0c786964ffb8932707c7d657f997b8344abdd31a47b4322f4aa`
   - responsibility: approved owner anatomical-left 3/4 lower-leg, ankle and foot geometry/proportions, direction, natural neutral stance and floor contact, natural skin-tone baseline, and burgundy toenail direction.
   - must_not_define: final reusable Gate-7 hosiery material detail, other views, new identity/body design, lighting or background.
2. `HOS_15D_NUDE_MATTE_FOOT_CROP`
   - path: `materials/hosiery/reference_inputs/15d_nude_matte/IMG_2562_FOOT_MATERIAL_CROP.png`
   - SHA-256: `8b41b8ac49bd0095b926ce6d16c8ba439daef26d22c32032bb2ed8f3ea0b6b69`
   - responsibility: fine 15D nude matte/velvet textile presence, transparency, tension and continuous coverage across ankle, heel, instep, forefoot and closed toes.
   - must_not_define: owner identity, body/foot anatomy, skin pigmentation, nail color, pose, floor contact, background, lighting or text.

Reference budget: 2 images. No previous generated candidate is attached.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: adult clinical footwear-free textile and foot-calibration reference; exactly one independent HOS_02_FEET_3Q v001 candidate, REVIEW_REQUIRED.

Image 1 defines only the approved owner's anatomical-left 3/4 lower-leg, ankle and foot geometry/proportions, direction, neutral standing contact, natural skin-tone baseline and burgundy toenail direction. Image 2 defines only realistic light-nude 15D matte/velvet sheer textile presence, transparency, tension and uninterrupted closed-toe coverage. Image 2 must not define anatomy, foot shape, pose, skin pigmentation, nail color, floor contact, lighting or background. Do not use HOS_01 pixels or any generated candidate.

Create a straight technical 3/4 close view cropped from mid-calf through both complete feet. Preserve Image 1's anatomical-left 35–45-degree orientation and natural separated flat-foot stance. Both heels, outer and inner ankle contours, arches, insteps, forefeet, all toe silhouettes and toe tips must be readable without one foot hiding the other.

Show exactly one continuous closed-toe light-nude 15D velvet-finish matte sheer pantyhose garment. The same fine textile layer flows from calves across ankles and heels, over insteps and forefeet, over every toenail and toe tip. No ankle cutoff, bare toes, toe-cap border, transverse toe-root line, seam, band, opacity/color break or reinforced toe. Burgundy toenails remain muted, low-saturation and soft-edged beneath the fabric, never painted on top. Realistic fine knit and subtle matte/velvet response; not white, gray, opaque, glossy, latex, PVC, plastic, wet coating or body paint.

Exact 3:4 vertical frame, camera near ankle/instep height, natural 85–100 mm perspective, neutral light-gray seamless studio and soft even white-balanced light. Avoid fused/missing/duplicated toes, broken heels, deformed arches, extra pads/supports, shoes, text, logo or watermark.
```

## QA status

### Attempt 1

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references supplied: both declared references; no previous candidate.
- request_id: `de0403b4-1a1e-44c5-a6bd-72aa7c238c09`
- next action: one concise retry using only `OWNER_BODY_LEFT_3Q_CANON_L1`; the material crop is omitted from pixel input and the 15D continuity contract remains textual.

No reviewable raster exists after Attempt 1.

### Attempt 2

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references supplied: only `OWNER_BODY_LEFT_3Q_CANON_L1`; the material crop was omitted and no previous candidate was supplied.
- request_id: `011258c7-2da4-441b-8492-cf18012c47df`
- prompt was reduced to orthopedic apparel-fit documentation, lower-limb/foot geometry and textual continuous textile behavior.
- final state: `GENERATION_BLOCKED_NO_OUTPUT`.

No output image, metadata raster record or QA image exists. The failed calls provide no new geometry or material evidence. Built-in generation stops here under the ImageGen skill; no CLI/API fallback is used without explicit user authorization.
