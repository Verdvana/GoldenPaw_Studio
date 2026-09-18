# OWNER_SPORT_YOGA_01_WORN_FRONT_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_SPORT_YOGA_01_WORN_FRONT
outfit_id: OWNER_SPORT_YOGA_01
level: L2
candidate_version: v003
target_canon_version: owner_v1.0
spec_revision: draft_1.235
identity_revision: draft_0.185
status: APPROVED
approval_status: APPROVED_BY_USER
gate: L2 yoga full-body front fit-validation
generation_tool: built_in_image_gen
reference_set_ids:
  - OWNER_YOGA_01_DESIGN_REFERENCE_CURRENT
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
  - OWNER_HOS_15D_NUDE_MATTE_MATERIAL_CROP
reference_budget: 5 images
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced resize"
generation_inputs:
  - {asset_id: OWNER_SPORT_YOGA_01_DESIGN_REFERENCE, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/approved/design_reference/OWNER_SPORT_YOGA_01_DESIGN_REFERENCE.png", responsibility: "current short light-pink open-back crop tank, warm apricot-pink opaque matte yoga pants, light-skin-tone matte 15D pantyhose and no footwear", must_not_define: "owner face, body, skin, hair, pose, lighting or background"}
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", responsibility: "latest Body01 neck-below proportions, waist/hip relation, leg axes, foot scale and neutral stance", must_not_define: "face, facial identity, hair, clothing, hosiery material, lighting or background"}
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", responsibility: "source-derived face geometry, facial relationships, natural skin and neutral expression", must_not_define: "body, hair, clothing, pose, lighting or background"}
  - {asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png", responsibility: "Hairstyle A only", must_not_define: "face, body, skin, clothing, hosiery, lighting or background"}
  - {asset_id: OWNER_HOS_15D_NUDE_MATTE_MATERIAL_CROP_001, path: "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png", responsibility: "light-skin-tone matte sheer 15D hosiery, continuous foot coverage and toe tension", must_not_define: "owner identity, body anatomy, yoga clothing, pose or background"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and face-contamination QA only"}
  - {asset_id: OWNER_BODY_01_FRONT_CANON_007, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png", purpose: "post-generation body proportion comparison only"}
  - {asset_id: OWNER_SPORT_YOGA_01_WORN_FRONT_v002, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/candidates/v002_worn_front/OWNER_SPORT_YOGA_01_WORN_FRONT_v002.png", purpose: "previous oily-hosiery candidate comparison only; never a generation input"}
authoritative_for:
  - "L2 yoga worn-front presentation"
  - "full outfit fit over latest Body01 proportions"
must_not_define:
  - "new Character Canon or permanent identity facts"
  - "AI-to-AI face or body lineage"
  - "future video keyframe identity"
original_candidate_path: outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/candidates/v003_worn_front/OWNER_SPORT_YOGA_01_WORN_FRONT_v003.png
approved_path: outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/approved/worn_front/OWNER_SPORT_YOGA_01_WORN_FRONT.png
sha256: c5608be7d74607b5babd4158fe2b31f492f0c9b99ddcd224770c0901fd1bc59d
dimensions: 1086x1448
approval_date: 2026-09-18
approved_by: user
qa_status: APPROVED
```

## Prompt assembly

Use case: identity-preserve
Asset type: L2 yoga worn-front full-body fit-validation candidate

Generate one fresh photorealistic full-body frontal neutral-standing image of the same adult woman, from the top of the head to the floor. Use the current approved unworn yoga design only for clothing and hosiery design. Use the face-excluded Body01 reference as the sole authority for all neck-below body proportions. Use the source-derived face and Hairstyle A only for face and hair. Do not use any previous generated worn candidate as input.

Preserve Body01 proportions exactly: upright neck, natural shoulders and torso, accepted waist/hip relation, naturally full thighs and calves, straight parallel leg axes, close uncrossed stance, matching feet and full-foot grounding. Keep the legs visibly straight, especially through the lower legs; no bowing, knee drift or asymmetrical calf contour. Do not slim, widen, lengthen, shorten or reshape the body.

Dress her in the updated yoga outfit: same-color light-pink short cropped strappy open-back athletic yoga tank, warm apricot-pink smooth opaque matte full-length yoga pants ending just above the ankles, and light-skin-tone matte sheer 15D pantyhose from waist through thighs, knees, calves, ankles, heels, insteps and toes. No shoes.

The hosiery must show realistic matte 15D textile presence: pale nude/light-skin color, subtle fine knit veil, soft diffuse light response, gentle fabric tension across each toe and visible tension lines between adjacent toes. The toe area must clearly read as hosiery wrapped continuously over the toes, with slight gathering and stretch at the toe roots and between toes, but no bare toe gaps, no toe-cap seam and no exposed toenails. Do not use oily gloss, pearlescent shine, broad highlights, wet skin, latex, PVC, vinyl, rubber, plastic, liquid or body paint. Keep yoga pants opaque and matte, clearly separate from the sheer hosiery.

Neutral light gray seamless studio, soft even catalog lighting, eye-level 70–85mm-equivalent camera, exact native 3:4 portrait, full head/hands/legs/feet in frame, no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Check latest Body01 proportions and straight leg shape; updated short open-back crop tank; warm apricot-pink matte yoga pants; light-skin-tone matte 15D hosiery; continuous toe coverage and toe-to-toe fabric tension; no glossy/oily/plastic material; no shoes; source-derived face compliance. No promotion without explicit user approval.
