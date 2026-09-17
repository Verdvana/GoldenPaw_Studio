# BODY_01_FRONT_v011 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.222
identity_md_revision: draft_0.39
body_md_revision: draft_0.16
method_id: OWNER_BODY_01_FRONT_METHOD_V2
user_scoped_override: "2026-09-17 source-derived Face recovery; no L1 Face raster; v011 lower-leg contour and stance-gap refinement"
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v011
gate: "Gate 3 — Body Canon"
model_tool: built-in image_gen
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
  - OWNER_L0_BODY_FRONT_CONTEXT
reference_count: 4
previous_ai_reference_count: 0
face_l1_raster_supplied: false
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v011/BODY_01_FRONT_v011.png"
qa_status: FAIL_MATERIAL_CONTRACT
checksum_sha256: d1cf0fe3705604233a86cc6d3f2d5e6c81d444fd4035b165e0cc75a708ef45a4
```

## Reference responsibilities and exclusions

1. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` — source-derived face/skin context only; no hair, body, clothing, lighting or background authority.
2. `L0_OWNER_002` (`3.jpg`) — stature and natural body-proportion context only; no face, hair, clothing, shoes, props, background or retouching authority.
3. `L0_OWNER_003` (`4.jpg`) — torso, waist, hip, thigh, calf and limb-volume cross-check only; no face, hair, outfit, legwear, shoes, environment or final-body authority.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — Hairstyle A pixels only; masked area defines nothing.

No approved Face raster, approved Body Master, BODY_01 v001–v010, previous shot or other generated image is supplied.

## Prompt assembly

```text
Use case: identity-preserve, clinical anthropometric reference
Create exactly one non-sexual neutral full-length 3:4 straight-on front-view technical body-proportion calibration plate of the adult woman. Reconstruct in parallel from the declared source-derived references only.

Image 1 is the source-derived face/skin context from the FACE_01 recovery method: use only for recognizable front-face geometry, natural facial relationships, adult age, realistic warm-neutral skin, direct gaze and closed mouth. Do not use any approved L1 Face image. Images 2–3 are real body-context references only: use for natural stature, torso, waist/hip, limb and soft-tissue proportions, while ignoring their faces, hair, clothing, shoes, props, environments, lighting and retouching. Image 4 is a face-masked Hairstyle A reference: use only visible long straight dark-brown Hair A construction; the gray mask defines nothing.

Physical baseline: 168 cm and approximately 60 kg. Preserve the accepted natural adult body volume, shoulder/chest/waist/hip relationship, torso length, limb length and 168 cm visual stature. Do not make a fashion-model body, tiny head, stretched legs, wide-angle or low-angle elongation, exaggerated hourglass or any identity change.

Critical v011 lower-leg geometry: the tibial shafts are substantially straight in the front view, not visibly bowed. From each knee center down to the ankle center, the bony lower-leg axis and the outer contour should remain nearly straight with only minimal natural soft-tissue curvature. Both knee–shin–ankle axes are parallel, symmetric and close to vertical. No outward bowing, O-leg silhouette, inward collapse or displaced ankles. Keep natural calf muscle volume, but do not let the calf bulge create the impression that the bone is bent. Keep naturally proportioned adult ankles with a smooth calf-to-ankle transition; do not pinch or over-narrow them.

Use a relaxed neutral standing stance with even weight, flat stable feet, feet approximately parallel and only a small natural gap between the inner legs. The legs should be close together without touching or crossing; do not create a wide triangular gap, wide turnout or pose-based separation. This is a subtle stance adjustment, not a change in body width or leg length.

Calibration outfit: plain opaque pink high-cut one-piece athletic swimsuit; continuous light-nude 15D velvet-finish sheer closed-foot pantyhose; no shoes. The pantyhose is one continuous matte textile from thighs through knees, calves, ankles, heels, insteps and toes. No bare toes, seams, bands, reinforced toe, latex, PVC, plastic, wet coating or body paint.

Neutral gray-white seamless studio, soft even 5200–5600K light, level 70–85mm-equivalent camera centered between waist and lower chest. Complete head, hands, heels and toes with 5–8% breathing room, square torso, relaxed arms, neutral direct gaze. No props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.
```

## QA checklist

- source-derived Face method followed; no L1 Face pixel contamination
- tibial shafts visually near-straight, not bowed
- knee–shin–ankle axes parallel and symmetric
- small natural inter-leg gap, no wide triangular opening
- calf volume and ankle width natural
- flat bilateral foot contact and complete anatomy
- 168 cm / 60 kg proportion and previously accepted torso/waist/hip preserved
- calibration outfit and continuous 15D hosiery coverage
- neutral technical presentation; no text/watermark/collage

## Attempt result and QA

- generated_at: 2026-09-17
- built-in output was saved to the project candidate path as a unique candidate raster.
- body geometry review: lower-leg axes are visibly straighter than the prior attempt, and the inter-leg gap is reduced to a small natural standing gap.
- material/outfit review: FAIL. The output shows bare legs and bare feet rather than continuous 15D closed-foot pantyhose. This is a hard rejection under `docs/qa/hosiery_material_rules.md`.
- status remains `REVIEW_REQUIRED`; no promotion, no Canon replacement, and no downstream reference use.
