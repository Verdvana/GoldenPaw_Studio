# BODY_01_FRONT_v018 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v018
target_canon_version: owner_v1.0
gate: Gate 3 — Body Canon
status: REVIEW_REQUIRED
approval_status: PENDING_USER_REVIEW
spec_revision: draft_1.226
identity_revision: draft_0.178
body_method_id: OWNER_BODY_01_FRONT_METHOD_V2
body_revision: draft_0.18
generation_tool: built_in_image_gen
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_BODY_FRONT_RECOVERY_V1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 5
previous_generated_body_inputs: 0
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v018/BODY_01_FRONT_v018.png
sha256: 03da72ffaedc07ce6560879bc96cf4c9f407c5ceb08d5d59add7edf1a540869a
dimensions: 1086x1448
qa_status: PRELIMINARY_REVIEW_REQUIRED
```

## Inputs and exclusions

1. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` — source-derived face/skin context only; no body, hair, clothing, hosiery, lighting or background authority.
2. `L0_OWNER_002` / `source/identity/raw/3.jpg` — stature and body context only; no face, hair, clothing, shoes, props or background authority.
3. `L0_OWNER_003` / `source/identity/raw/4.jpg` — natural torso, waist, hip, thigh, calf and limb-volume cross-check only; no face, hair, clothing or environment authority.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — Hairstyle A only; masked area defines nothing.
5. `OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001` — hosiery textile behavior only: pale slightly-whiter 15D surface, soft toe haze, continuous coverage and interdigital tension; no identity or body authority.

`OWNER_BODY_01_FRONT_CANON_004` and `BODY_01_FRONT_v017` are `qa_comparison_only`, never generation inputs.

## Prompt assembly

Create exactly one neutral, full-length, front-view technical anthropometric fitting reference of an adult woman, fully clothed and non-erotic. Image 1 defines the recognizable front face and neutral skin only. Images 2–3 define natural body context only. Image 4 defines Hairstyle A only. Image 5 defines 15D hosiery textile behavior only. Do not use any generated Body image or approved Body image as an image input.

Preserve the accepted v017 lower-leg axis: both tibial shafts descend almost collinearly with the thigh axes, with nearly no bend; outer contours stay close to the thigh outer contours; inner contours leave only a very narrow natural gap and remain separate. Preserve the accepted face, Hairstyle A, pink high-cut one-piece calibration garment and pale slightly-whiter 15D matte/velvet hosiery. Make only these additional corrections: slightly increase the natural volume of both thighs and calves; narrow the waist slightly while retaining a smooth ribcage-to-waist-to-hip transition, no corset compression and no exaggerated hourglass.

Foot and hosiery correction is exact: both feet must be fully planted on the floor, with heel, forefoot and toes resting and visibly weight-bearing; no tiptoe, no heel lift, no hovering, no toe-standing. The hosiery is one continuous pale sheer surface over every toe. Remove all white rings, white circles, pale bands or hard boundaries at the toe roots. Every burgundy toenail is beneath the same soft hazy hosiery veil, with no crisp exposed nail edge. Between adjacent toes, show clear but natural V-shaped textile tension/valley curves and fabric convergence; these must read as stretched hosiery, never bare gaps, seams or painted lines. Keep the slight whitening and diffuse 15D material quality consistent from legs through feet.

Neutral gray-white seamless studio, soft even clinical light, level 70–85mm-equivalent camera, exact 3:4 framing, complete head and feet visible, even weight, relaxed arms, legs uncrossed. No camera distortion, pose trick, slimming, artificial lengthening, props, text, watermark, collage, latex, PVC, plastic, wet coating or body paint. One `REVIEW_REQUIRED` candidate only; not Canon.

## QA plan

Check: straight v017 lower-leg axes; slightly increased thigh/calf volume; slightly narrower waist with smooth transition; full-foot contact; no toe-root white rings/bands; all burgundy nails diffused under hosiery; readable interdigital textile tension curves; continuous pale hosiery; no exposed bare toe gaps; face contamination against approved Face Canon; no promotion.

## Generation output

- Generated source: `/home/verdvana/.codex/generated_images/01a0aeda-94e0-7940-aa23-e89d1ec0cff1/exec-4f26b51d-234c-49ab-ad27-0b480b7d0b79.png`
- Repository candidate: `BODY_01_FRONT_v018.png`
- Visual precheck: thighs and calves are visibly fuller, waist is slightly narrower, lower-leg axes remain straight, and both feet appear fully planted. No obvious toe-root white ring is visible. The toe nail color is heavily diffused beneath the hosiery; interdigital tension remains a user-review point because it is subtle at this view.
