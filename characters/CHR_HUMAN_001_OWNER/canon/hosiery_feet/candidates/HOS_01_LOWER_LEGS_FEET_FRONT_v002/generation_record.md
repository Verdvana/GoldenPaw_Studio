# HOS_01_LOWER_LEGS_FEET_FRONT_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.143
identity_md_revision: draft_0.131
asset_id: HOS_01_LOWER_LEGS_FEET_FRONT
candidate_id: HOS_01_LOWER_LEGS_FEET_FRONT_v002
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in image_gen"
status: TECHNICAL_QA_FAILED_TOE_BOUNDARY
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_BODY_FRONT_CANON_L1
  - HOS_15D_NUDE_MATTE_FOOT_CROP
reference_count: 2
previous_ai_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_01_LOWER_LEGS_FEET_FRONT_v002/HOS_01_LOWER_LEGS_FEET_FRONT_v002.png"
checksum_sha256: "66a49dcc8970eb2a6fb2a6e71f87dfaa57d95293fdd66d5d4518147bc680896a"
qa_status: FAIL_HOSIERY_TOE_BOUNDARY
```

## Authorization and lineage

The user explicitly authorized correction of the two v001 QA failures. v002 is independently reconstructed from approved/source-derived Masters. v001 is excluded as pixel input, as are all Pose, Expression, Shot and other generated candidates. Successful v001 framing/geometry is retained only as text.

## Reference responsibilities

1. `OWNER_BODY_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v009/BODY_01_FRONT_v009.jpg`
   - SHA-256: `964c3b9d72c6688881b8ebfa4c6fc1bcfea04c998351352fabfdc8f4951666f6`
   - responsibility: approved owner front lower-leg and foot anatomy/proportions, symmetrical neutral standing contact, natural skin-tone baseline and burgundy toenail direction.
   - must_not_define: new face/overall body/hair identity, final reusable weave beyond its scoped 15D matte nude appearance, lighting or background.
2. `HOS_15D_NUDE_MATTE_FOOT_CROP`
   - path: `materials/hosiery/reference_inputs/15d_nude_matte/IMG_2562_FOOT_MATERIAL_CROP.png`
   - SHA-256: `8b41b8ac49bd0095b926ce6d16c8ba439daef26d22c32032bb2ed8f3ea0b6b69`
   - responsibility: fine 15D nude matte/velvet behavior, transparency, tension and uninterrupted textile layer across ankle, heel, instep and toes.
   - must_not_define: owner identity, body/foot anatomy, skin pigmentation, nail color, pose, background, lighting or text.

Reference budget: 2 images. No previous generated candidate is attached.

## Scoped correction

- preserve the approved/body-derived straight-on knee-to-foot framing, proportions, stance and intact anatomy as text;
- remove every line, seam, band, ridge, color change or transparency boundary at the toe roots and across the forefeet;
- make the 15D textile visibly continuous over each nail and toe with gentle optical diffusion;
- burgundy polish remains beneath the textile, lower saturation and softer-edged than bare painted nails.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: adult clinical textile and lower-limb calibration reference; exactly one independent HOS_01_LOWER_LEGS_FEET_FRONT v002 candidate, REVIEW_REQUIRED.

Input images: Image 1 defines only the approved owner front knee/calf/ankle/foot anatomy and proportions, neutral front standing contact, natural skin-tone baseline and burgundy toenail direction. Image 2 defines only the fine 15D nude matte/velvet textile layer, transparency and uninterrupted ankle-to-toe coverage. Image 2 must not define anatomy, foot shape, pose, skin pigmentation, nail color, lighting or background. Do not use or imitate v001 or any generated candidate.

Primary request: straight-on front clinical textile documentation cropped from just above both knees through both complete feet. Preserve Image 1's lower-leg and foot geometry. Both legs remain parallel with natural spacing; both complete feet rest flat, separate and forward on one seamless floor plane.

Correction priority: there must be absolutely no transverse line, toe-cap border, seam, band, ridge, color change or transparency change anywhere across the toe roots or forefeet. The same single sheer textile layer flows smoothly from ankles over insteps, toe joints, every nail and toe tip. Nail outlines and burgundy color are optically softened by fabric above them: muted, low-saturation and soft-edged, never crisp or painted on the surface.

Materials/textures: continuous light-nude 15D velvet-finish matte sheer pantyhose, realistic fine knit, translucent skin response and natural tension without becoming white, gray, opaque, glossy, plastic or body paint.

Composition/framing: exact 3:4 vertical frame; just above both knees to below complete feet, equal margins, mid-shin camera height, natural 85–100 mm perspective. Neutral light-gray seamless studio and soft even white-balanced light.

Avoid: v001 pixels, bare toes, ankle cutoff, open-toe construction, sock edge, toe band, seam or material break, polish on top, fused/missing/duplicated toes, broken heels, extra pads, text, logo or watermark.
```

## QA status

### Attempt 1

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references supplied: both declared references; no previous candidate.
- request_id: `896dbb87-dc5f-9686-ac68-b458a1ac1fdf`
- next action: one concise retry using only `OWNER_BODY_FRONT_CANON_L1`, retaining the two user-requested corrections in text and omitting the material crop from pixel input.

No reviewable raster exists after Attempt 1.

### Attempt 2

- result: generated successfully using only `OWNER_BODY_FRONT_CANON_L1`; the material crop was omitted from pixel input as declared after Attempt 1.
- output: 1086x1448 PNG, exact 3:4.
- output path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_01_LOWER_LEGS_FEET_FRONT_v002/HOS_01_LOWER_LEGS_FEET_FRONT_v002.png`
- SHA-256: `66a49dcc8970eb2a6fb2a6e71f87dfaa57d95293fdd66d5d4518147bc680896a`

## Visual QA result

- PASS: exact 3:4 knee-to-foot framing, straight-on stance, intact lower-leg/foot anatomy and neutral floor contact.
- PASS/IMPROVED: burgundy nail color is softer and less saturated than v001 and reads more plausibly beneath a sheer layer.
- FAIL: a bilateral transverse boundary remains visible across the toe-root/forefoot region. Although lighter than v001, it still reads as a toe-cap edge or material/transparency discontinuity and violates the Gate-7 continuity rule.
- decision: retain as a failed `REVIEW_REQUIRED` candidate; do not promote or use downstream. A future v003 must be independently regenerated without v001/v002 pixels. Preserve the improved nail treatment only as text and focus the next correction solely on uninterrupted forefoot-to-toe material.
