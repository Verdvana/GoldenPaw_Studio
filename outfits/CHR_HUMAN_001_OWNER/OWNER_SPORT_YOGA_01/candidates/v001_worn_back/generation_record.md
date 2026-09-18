# OWNER_SPORT_YOGA_01_WORN_BACK_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_SPORT_YOGA_01_WORN_BACK
outfit_id: OWNER_SPORT_YOGA_01
level: L2
candidate_version: v001
target_canon_version: owner_v1.0
spec_revision: draft_1.235
identity_revision: draft_0.185
status: APPROVED
approval_status: APPROVED_BY_USER
gate: L2 yoga full-body back fit-validation
generation_tool: built_in_image_gen
reference_set_ids:
  - OWNER_YOGA_01_DESIGN_REFERENCE_CURRENT
  - OWNER_BODY_06_BACK_CANON_CURRENT
  - OWNER_HAIRSTYLE_A_BACK_CANON_CURRENT
  - OWNER_HOS_15D_NUDE_MATTE_MATERIAL_CROP
reference_budget: 4 images
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced resize"
generation_inputs:
  - {asset_id: OWNER_SPORT_YOGA_01_DESIGN_REFERENCE, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/approved/design_reference/OWNER_SPORT_YOGA_01_DESIGN_REFERENCE.png", responsibility: "current short light-pink open-back crop tank, warm apricot-pink opaque matte yoga pants, light-skin-tone matte 15D hosiery and no footwear", must_not_define: "body proportions, face, identity, pose, lighting or background"}
  - {asset_id: OWNER_BODY_06_BACK_CANON_004, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_06_BACK/OWNER_BODY_06_BACK_CANON_004.png", responsibility: "registered back-view body proportions, shoulder/torso/waist/hip relation, glute/thigh/calf shape, straight leg axes, foot scale and neutral back stance", must_not_define: "current yoga clothing design, hosiery material, face identity, lighting or background"}
  - {asset_id: OWNER_HAIR_A_04_BACK_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_04_BACK/OWNER_HAIR_A_04_BACK_CANON_001.png", responsibility: "Hairstyle A back length, fall and tapered ends only", must_not_define: "body, clothing, face, identity, hosiery, lighting or background"}
  - {asset_id: OWNER_HOS_15D_NUDE_MATTE_MATERIAL_CROP_001, path: "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png", responsibility: "light-skin-tone matte sheer 15D hosiery, continuous foot coverage and toe tension", must_not_define: "owner identity, body anatomy, yoga clothing, pose or background"}
qa_comparison_only:
  - {asset_id: OWNER_BODY_06_BACK_CANON_004, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_06_BACK/OWNER_BODY_06_BACK_CANON_004.png", purpose: "registered back-body comparison only; generation role is declared above"}
  - {asset_id: OWNER_SPORT_YOGA_01_WORN_FRONT, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/approved/worn_front/OWNER_SPORT_YOGA_01_WORN_FRONT.png", purpose: "front outfit continuity comparison only"}
authoritative_for:
  - "L2 yoga worn-back presentation"
  - "back fit over registered Body06 back proportions"
must_not_define:
  - "new Character Canon or permanent identity facts"
  - "AI-to-AI face or body lineage"
  - "future video keyframe identity"
original_candidate_path: outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/candidates/v001_worn_back/OWNER_SPORT_YOGA_01_WORN_BACK_v001.png
approved_path: outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/approved/worn_back/OWNER_SPORT_YOGA_01_WORN_BACK.png
sha256: fa66c55a8c1b7e3f90403c55256f103388a763986579e3d2070579be2228b8d4
dimensions: 1086x1448
approval_date: 2026-09-18
approved_by: user
qa_status: APPROVED
```

## Prompt assembly

Use case: identity-preserve
Asset type: L2 yoga worn-back full-body fit-validation candidate

Generate one fresh photorealistic full-body rear-view neutral-standing image of the same adult woman, from the top of the head to the floor. Use the registered Body06 back asset as the direct back-view body proportion authority: preserve its shoulder width, back/waist/hip relationship, glute and thigh volume, straight leg axes, calf contours, foot scale and neutral stance. Use the approved yoga design only for clothing. Use Hairstyle A back only for hair length and tapered fall. Use the matte 15D reference only for hosiery material. Do not use any prior generated yoga worn image as a generation input.

Show the updated short light-pink strappy open-back athletic crop tank from the back: clearly exposed upper back, narrow shoulder straps, a restrained central rear strap connection, and the short cropped hem. Keep the warm apricot-pink yoga pants opaque, smooth and matte, full length to just above the ankles. No shoes.

Cover the feet continuously with light-skin-tone matte sheer 15D pantyhose. Show realistic matte textile presence, gentle ankle/heel fabric tension and subtle toe-to-toe tension where the toes are visible from behind; no bare gaps, toe-cap seam, pearlescent or oily gloss, latex, PVC, vinyl, rubber, plastic, liquid or body paint. Keep the legs straight, close and parallel, with both heels grounded and aligned. Neutral light gray seamless studio, soft even catalog lighting, eye-level rear camera, exact native 3:4 portrait, no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Check registered Body06 back proportions and straight leg axes; open-back crop-tank geometry; matte apricot-pink opaque pants; light-skin-tone matte 15D hosiery and continuous feet; no shoes; no front-face leakage; full-foot grounding. No promotion without explicit user approval.
