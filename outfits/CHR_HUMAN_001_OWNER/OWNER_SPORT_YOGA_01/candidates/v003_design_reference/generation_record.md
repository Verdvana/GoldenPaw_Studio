# OWNER_SPORT_YOGA_01_DESIGN_REFERENCE_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_SPORT_YOGA_01_DESIGN_REFERENCE
outfit_id: OWNER_SPORT_YOGA_01
level: L2
candidate_version: v003
target_canon_version: owner_v1.0
status: APPROVED
approval_status: APPROVED_BY_USER
gate: L2 yoga unworn outfit-shape update
generation_tool: built_in_image_gen
reference_set_ids:
  - OWNER_YOGA_01_APPROVED_DESIGN_PANTS_ONLY
  - OWNER_HOS_15D_NUDE_MATTE_MATERIAL
reference_budget: 2 images
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced resize"
generation_inputs:
  - {asset_id: OWNER_SPORT_YOGA_01_DESIGN_REFERENCE, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/approved/design_reference/OWNER_SPORT_YOGA_01_DESIGN_REFERENCE.png", responsibility: "warm apricot-pink opaque matte full-length yoga pants only", must_not_define: "top design, hosiery finish/color, owner identity, body, pose, lighting or background"}
  - {asset_id: OWNER_HOS_15D_NUDE_MATTE_MATERIAL_CROP_001, path: "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png", responsibility: "light-skin-tone matte sheer 15D hosiery material and continuous foot coverage", must_not_define: "owner identity, body anatomy, yoga clothing, pose or background"}
qa_comparison_only:
  - {asset_id: OWNER_SPORT_YOGA_01_DESIGN_REFERENCE_OLD_APPROVED, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/approved/design_reference/OWNER_SPORT_YOGA_01_DESIGN_REFERENCE.png", purpose: "historical pants-shape comparison only"}
authoritative_for:
  - "updated unworn yoga outfit garment arrangement"
  - "short light-pink open-back crop tank, warm apricot-pink matte yoga pants and light-skin-tone matte 15D hosiery"
must_not_define:
  - "owner face, body, skin, hair or identity"
  - "worn fit or video identity"
original_candidate_path: outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/candidates/v003_design_reference/OWNER_SPORT_YOGA_01_DESIGN_REFERENCE_v003.png
approved_path: outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/approved/design_reference/OWNER_SPORT_YOGA_01_DESIGN_REFERENCE.png
sha256: 18bdcf1c31ee4bfb63d7d5bdad75f41b265e7e5a81ae6efeaf25396a63939de9
dimensions: 1086x1448
approval_date: 2026-09-18
approved_by: user
qa_status: APPROVED
```

## Prompt assembly

Use case: product-mockup
Asset type: L2 yoga unworn outfit design reference

Create one clean photorealistic studio product-board image of the complete yoga outfit, entirely unworn and without any human, mannequin, torso form, hands, legs or body. Arrange each item separately on a neutral gray background: a light-pink short cropped strappy athletic yoga tank with a clearly open back and restrained non-crowded strap geometry, warm apricot-pink smooth opaque matte full-length yoga pants ending just above the ankles, and one complete pair of light-skin-tone matte sheer 15D pantyhose laid flat from waistband through both legs and feet. No shoes.

The short top must visibly be shorter than a regular tank, with a clean athletic crop length, same light-pink color as the prior top, narrow shoulder straps and an open-back design shown by front and back views. Keep the yoga pants shape and warm apricot-pink matte surface unchanged. The pantyhose must be pale/light skin tone, sheer 15D and matte: no pearlescent sheen, no oily gloss, no bright reflective streaks, no plastic, rubber, latex, vinyl, liquid or body-paint appearance. Show the complete closed-toe hosiery shape and natural textile folds without a toe-cap line.

Product-board/catalog arrangement, front and back views of the top, front and back views of the pants if space allows, hosiery laid flat separately, soft even studio light, exact native 3:4 portrait, no model, mannequin, face, skin, hair, anatomy, props, text, logo, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Check no human or mannequin contamination; top is short, light pink, strappy and open-back; pants remain warm apricot-pink, opaque and matte; hosiery is light-skin-tone 15D, matte and sheer rather than pearlescent/glossy; no shoes; complete garment shapes and no extra items. No promotion without explicit user approval.
