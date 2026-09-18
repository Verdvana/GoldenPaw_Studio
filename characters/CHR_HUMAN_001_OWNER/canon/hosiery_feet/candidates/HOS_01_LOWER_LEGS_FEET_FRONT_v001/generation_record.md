# HOS_01_LOWER_LEGS_FEET_FRONT_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.141
identity_md_revision: draft_0.129
asset_id: HOS_01_LOWER_LEGS_FEET_FRONT
candidate_id: HOS_01_LOWER_LEGS_FEET_FRONT_v001
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in image_gen"
status: TECHNICAL_QA_FAILED_TOE_BOUNDARY
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_BODY_FRONT_CANON_L1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 2
previous_ai_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_01_LOWER_LEGS_FEET_FRONT_v001/HOS_01_LOWER_LEGS_FEET_FRONT_v001.png"
checksum_sha256: "0c85bf868f013ad332e13a090e349851b04e94f8b6792a6e43d462f7b92a9bc2"
qa_status: FAIL_HOSIERY_TOE_BOUNDARY
```

## Authorization and lineage

The user explicitly deferred the remaining blocked Pose items and requested the first asset of the next Gate. This authorizes exactly one `HOS_01_LOWER_LEGS_FEET_FRONT_v001` candidate. It is reconstructed independently from one approved Body Master and one deterministic material-only derivative. No generated Pose, previous hosiery candidate, Expression, Shot or failed image is supplied.

The preferred standing source `IMG_2581.jpg` is absent from the pruned physical library and is not supplied. The user-selected material derivative provides the available stronger lower-leg-to-foot textile presence. This source-coverage choice is explicit.

## Reference responsibilities

1. `OWNER_BODY_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v009/BODY_01_FRONT_v009.jpg`
   - SHA-256: `964c3b9d72c6688881b8ebfa4c6fc1bcfea04c998351352fabfdc8f4951666f6`
   - responsibility: exact approved owner front lower-leg proportions, knee/calf/ankle/heel/instep/toe geometry, symmetrical neutral standing contact, natural skin-tone baseline and burgundy toenail direction.
   - must_not_define: new face/overall body/hair identity, reusable final hosiery weave beyond its scoped 15D matte nude appearance, lighting or background.
2. `HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001`
   - path: `materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png`
   - SHA-256: `36fba906cfb47002f6669133b336b5d47b25c1763450db8fd4fbce7412eb8948`
   - responsibility: stronger readable 15D nude matte/velvet textile presence, opacity impression, smooth lower-leg-to-foot coverage and muted toe visibility.
   - must_not_define: owner identity, leg/foot anatomy, skin pigmentation, nail color, pose, clothing, shoes, floor contact, background, lighting or watermark.

Reference budget: 2 images. No previous generated candidate is attached.

## Authoritative candidate scope

- straight-on front view from just above both knees through both complete feet;
- approved owner lower-leg and foot proportions with knees, calves, ankles, heels, insteps and all toes intact;
- continuous light-nude 15D velvet/matte sheer textile response from the upper crop boundary through toes;
- natural tension and transparency changes across knees, calves, ankles, insteps, toe joints and floor contact;
- burgundy toenail polish softly visible beneath the fabric where lighting permits.

The candidate must not define face, full-body proportions above the visible crop, hairstyle, outfit design, pose beyond neutral front standing, episode wardrobe, lighting or environment.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: adult technical textile and lower-limb calibration reference; exactly one HOS_01_LOWER_LEGS_FEET_FRONT v001 candidate, REVIEW_REQUIRED.

Input images: Image 1 defines only the approved owner front lower-leg and foot anatomy, proportions, symmetrical neutral standing contact, natural skin-tone baseline and burgundy toenail direction. Image 2 defines only stronger visible 15D nude matte/velvet textile presence, smooth continuous coverage and muted toe visibility. Image 2 must not define anatomy, proportions, skin color, nail color, pose, background, footwear or floor contact.

Primary request: create a straight-on front clinical textile documentation image cropped from just above both knees through both complete feet. Preserve Image 1's exact lower-leg and foot geometry. Both legs remain parallel with natural spacing; both complete feet rest flat and separately on one seamless floor plane, pointing naturally forward with no overlap.

Materials/textures: one continuous light-nude 15D velvet-finish matte sheer pantyhose garment visibly covers the upper crop boundary, knees, calves, ankles, heels, insteps, forefeet and every toe. Maintain realistic translucent textile response, subtle knit/tension and gentle toe-detail softening. Burgundy toenail polish may show only softly and with reduced saturation beneath the fabric.

Style/medium: neutral photorealistic clinical material documentation, natural unretouched texture.
Composition/framing: exact 3:4 vertical frame; just above both knees to below the complete feet, equal clear margins, camera level with mid-shin, natural 85–100 mm perspective.
Lighting/mood: neutral light-gray seamless studio, soft even white-balanced light, restrained highlights.
Constraints: no shoes, but feet are fully covered by the continuous closed-toe textile; no person identity outside the cropped lower-limb region; one image only.
Avoid: bare toes, ankle cutoff, open-toe construction, sock edge, toe cap band, seam or color break, white/gray color shift, opaque fabric, latex/PVC/plastic/body-paint surface, polish painted on top, fused/missing/duplicated toes, broken heels, extra support pads, text, logo or watermark.
```

## QA status

### Attempt 1

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references supplied: both declared references; no previous generated candidate.
- request_id: `24937e45-4949-4757-a8cc-2850a09c6734`
- next action: one concise retry using only `OWNER_BODY_FRONT_CANON_L1`; rely on its approved scoped 15D nude matte appearance plus the written textile contract, and omit the material crop from pixel input to reduce combination ambiguity.

No reviewable raster exists after Attempt 1.

### Attempt 2

- result: generated successfully using only `OWNER_BODY_FRONT_CANON_L1`; the material derivative was omitted from pixel input as declared after Attempt 1.
- output: 1086x1448 PNG, exact 3:4.
- output path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_01_LOWER_LEGS_FEET_FRONT_v001/HOS_01_LOWER_LEGS_FEET_FRONT_v001.png`
- SHA-256: `0c85bf868f013ad332e13a090e349851b04e94f8b6792a6e43d462f7b92a9bc2`

## Visual QA result

- PASS: exact 3:4 framing; crop begins above both knees and includes both complete feet; straight-on neutral stance; no missing/duplicated toes or broken heels; light-nude overall color and restrained matte response.
- FAIL: a visible bilateral transverse boundary crosses the toe-root/forefoot region and reads as a toe-cap line or transparency/material discontinuity.
- FAIL: burgundy nail color remains too crisply exposed and locally saturated, reading closer to surface polish than color naturally softened beneath 15D textile.
- decision: retain as a failed `REVIEW_REQUIRED` candidate; do not promote or use downstream. A future v002 must be independently regenerated from approved sources and may preserve successful geometry/framing only as text, never as v001 pixel input.
