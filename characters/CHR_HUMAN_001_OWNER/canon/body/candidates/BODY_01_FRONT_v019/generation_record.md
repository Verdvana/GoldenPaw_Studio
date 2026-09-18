# BODY_01_FRONT_v019 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v019
target_canon_version: owner_v1.0
gate: Gate 3 — Body Canon
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
spec_revision: draft_1.227
identity_revision: draft_0.179
body_method_id: OWNER_BODY_01_FRONT_METHOD_V2
body_revision: draft_0.19
generation_tool: built_in_image_gen
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_BODY_FRONT_RECOVERY_V1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 5
previous_generated_body_inputs: 0
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v019/BODY_01_FRONT_v019.png
sha256: 9438c2e7d005c546f214f441174437072bf1e277f70668bd4a977ff2288d2083
dimensions: 1086x1448
qa_status: APPROVED
```

## Inputs and exclusions

1. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` — source-derived face/skin context only.
2. `L0_OWNER_002` / `source/identity/raw/3.jpg` — stature and body context only.
3. `L0_OWNER_003` / `source/identity/raw/4.jpg` — natural torso and limb-volume cross-check only.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — Hairstyle A only.
5. `OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001` — hosiery textile only; no identity or body geometry authority.

`OWNER_BODY_01_FRONT_CANON_004`, `BODY_01_FRONT_v017` and `BODY_01_FRONT_v018` are `qa_comparison_only`; no generated Body pixels are generation inputs.

## Prompt assembly

Create one neutral, full-length, front-view apparel-fit calibration image of an adult woman, fully clothed and non-erotic. Image 1 defines the face only; Images 2–3 define body context only; Image 4 defines Hairstyle A only; Image 5 defines the accepted 15D hosiery material only.

Preserve the accepted v018 face, Hairstyle A, pink athletic one-piece, slightly fuller thighs and calves, slightly narrower waist, pale slightly-whiter matte sheer hosiery, toe coverage, burgundy nail diffusion, interdigital fabric tension and fully planted feet. The only priority correction is the lower-leg silhouette. Make each lower leg almost perfectly straight in front view: knee center, tibial shaft centerline and ankle center nearly share the thigh axis from top to bottom, with almost no visible inward or outward bend. The same-side outer calf edge should remain nearly flush and aligned with the same-side outer thigh edge as it descends, with no inwardly displaced calf contour and no lateral O-leg bulge. Keep only a tiny natural inner-leg air gap; legs remain separate, never fused or crossed.

Both feet must stay fully flat and weight-bearing on the floor, with heel and forefoot contact; no tiptoe, raised heel, hovering heel, toe-standing or pose trick. Maintain neutral stance, relaxed arms, level camera, gray-white seamless studio and soft even clinical light. Exact 3:4 framing with complete head and feet visible. No camera distortion, slimming, lengthening, props, text, watermark, collage, latex, PVC, plastic, wet coating or body paint. One `REVIEW_REQUIRED` candidate only; not Canon.

## QA plan

Prioritize knee–tibia–ankle collinearity, outer lower-leg/outer-thigh alignment, absence of inward bow and O-leg, tiny non-fused inner gap, preservation of v018 volume/waist, full-foot contact and hosiery continuity. Face Canon is comparison-only for contamination QA. Do not promote automatically.

## Generation output

- Generated source: `/home/verdvana/.codex/generated_images/01a0aeda-94e0-7940-aa23-e89d1ec0cff1/exec-10e784b7-9dd8-4b30-9b73-1cf87628cf31.png`
- Repository candidate: `BODY_01_FRONT_v019.png`
- Visual precheck: lower-leg axes read straighter than v018 and outer contours track closer to the thigh lines; v018 hosiery appearance, fuller leg volume, narrower waist and full-foot grounding are retained for user review.

## Approval and promotion

- User approval: “非常不错，登记”
- Approved asset: `OWNER_BODY_01_FRONT_CANON_005`
- Promoted path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v019/BODY_01_FRONT_v019.png`
- Original candidate path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v019/BODY_01_FRONT_v019.png`
- Promotion operation: moved unchanged; no duplicate candidate raster retained
