# OWNER_SPORT_YOGA_01_WORN_FRONT_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_SPORT_YOGA_01_WORN_FRONT
outfit_id: OWNER_SPORT_YOGA_01
level: L2
candidate_version: v002
target_canon_version: owner_v1.0
spec_revision: draft_1.235
identity_revision: draft_0.185
status: REVIEW_REQUIRED
approval_status: PENDING_USER_REVIEW
gate: L2 yoga full-body front fit-validation
generation_tool: built_in_image_gen
reference_set_ids:
  - OWNER_YOGA_01_DESIGN_REFERENCE_APPROVED
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
  - OWNER_HOS_15D_NUDE_HIGH_GLOSS_MATERIAL_SOURCE
reference_budget: 5 images
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced resize"
generation_inputs:
  - {asset_id: OWNER_SPORT_YOGA_01_DESIGN_REFERENCE, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/approved/design_reference/OWNER_SPORT_YOGA_01_DESIGN_REFERENCE.png", responsibility: "approved pink open-back yoga tank, warm apricot-pink matte yoga pants, no footwear and declared hosiery concept", must_not_define: "owner face, body, skin, hair, pose, lighting or background"}
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", responsibility: "latest Body01 neck-below proportions, waist/hip relation, torso/limb scale, straight leg axes, foot scale and neutral stance", must_not_define: "face, facial identity, hair, clothing, hosiery material, lighting or background"}
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", responsibility: "source-derived face geometry, facial relationships, natural skin and neutral expression", must_not_define: "body, hair, clothing, pose, lighting or background"}
  - {asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png", responsibility: "Hairstyle A only", must_not_define: "face, body, skin, clothing, hosiery, lighting or background"}
  - {asset_id: OWNER_HOS_15D_NUDE_HIGH_GLOSS_MATERIAL_SOURCE_001, path: "materials/hosiery/source_library/raw/15d_nude_high_gloss/IMG_2587.jpg", responsibility: "nude 15D high-gloss hosiery textile behavior: very fine narrow curved highlight lines over sheer fabric", must_not_define: "owner identity, body anatomy, yoga clothing, pose or background"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and face-contamination QA only"}
  - {asset_id: OWNER_BODY_01_FRONT_CANON_007, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png", purpose: "post-generation body proportion comparison only"}
  - {asset_id: OWNER_SPORT_YOGA_01_WORN_FRONT_v001, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/candidates/v001_worn_front/OWNER_SPORT_YOGA_01_WORN_FRONT_v001.png", purpose: "no-raster blocked historical attempt; comparison only"}
authoritative_for:
  - "L2 yoga worn-front presentation"
  - "full outfit fit over latest Body01 proportions"
must_not_define:
  - "new Character Canon or permanent identity facts"
  - "AI-to-AI face or body lineage"
  - "future video keyframe identity"
output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_YOGA_01/candidates/v002_worn_front/OWNER_SPORT_YOGA_01_WORN_FRONT_v002.png
sha256: 556743fef60418a1ebc4b784186d15fa4bbf433248f8f616d9b8322107d4246c
dimensions: 1086x1448
qa_status: TECHNICAL_PRECHECK_PASS_PENDING_USER_REVIEW
```

## Prompt assembly

Use case: identity-preserve
Asset type: L2 yoga worn-front full-body fit-validation candidate

Generate one fresh photorealistic full-body frontal neutral-standing image of the same adult woman, from the top of the head to the floor, in a professional sportswear catalog fitting reference. Reference 1 defines only the approved yoga outfit. Reference 2 is the sole authority for latest Body01 neck-below proportions, body scale, waist/hip relation, naturally full thighs and calves, straight parallel leg axes, foot scale and neutral stance. Reference 3 defines the face and skin from source-derived recovery only. Reference 4 defines Hairstyle A only. Reference 5 defines only the nude high-gloss hosiery material behavior. Do not use any generated Face/Body/outfit image as a generation input.

Preserve Body01 proportions exactly: upright natural neck, neutral head, correct shoulder-to-waist and hip relationships, straight legs with clean knee-to-tibia-to-ankle axes, natural thigh/calf volume, close uncrossed stance and matching foot scale. Do not slim, widen, lengthen, shorten or reshape the body. Keep both bare feet grounded and fully visible; no shoes.

Dress her in the approved yoga outfit: light-pink strappy yoga tank top with restrained open-back strap construction, smooth opaque matte full-length yoga pants in pink with a warm apricot undertone ending just above the ankles, and continuous nude 15D oil-sheen/high-gloss pantyhose over the body from waist through thighs, knees, calves, ankles, heels, insteps and toes. Keep the pants opaque and matte, separate from the hosiery.

The hosiery must read as very thin sheer fabric with a controlled oily gloss: natural skin tone remains visible beneath a nude veil, and the surface shows only very fine, narrow, elongated highlight lines following the curved leg and foot surfaces, broken naturally by anatomy and fabric tension. Use sparse hairline-width specular streaks, not broad white patches. The highlights should gently taper and vary in width, be brightest along a few curved ridges on the shin, calf, ankle and instep, and fade smoothly elsewhere. No wet skin, liquid coating, latex, PVC, vinyl, rubber, plastic, mirror-like reflection, uniform white stripe, opaque tights or painted body surface. Preserve continuous closed-toe hosiery over every toe with subtle toe tension and no bare gaps or toe-cap seam.

Neutral light gray seamless studio, soft even catalog lighting with controlled narrow highlights, eye-level 70–85mm-equivalent camera, exact native 3:4 portrait, full head/hands/legs/feet in frame, no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Check source-derived face compliance and no AI contamination; exact latest Body01 proportions and straight leg axes; approved yoga garments; separate opaque matte pants versus sheer glossy hosiery; fine narrow highlight lines only; no plastic/rubber/liquid appearance; continuous toe coverage; no footwear; full-foot grounding. No promotion without explicit user approval.
