# OWNER_WORK_SUMMER_01_WORN_FULL_BODY_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_WORK_SUMMER_01_WORN_FULL_BODY
outfit_id: OWNER_WORK_SUMMER_01
level: L2
candidate_version: v003
target_canon_version: owner_v1.0
spec_revision: draft_1.235
identity_revision: draft_0.185
status: REVIEW_REQUIRED
approval_status: PENDING_USER_REVIEW
gate: L2 summer officewear full-body fit-validation
generation_tool: built_in_image_gen
reference_set_ids:
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
  - OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_L1
  - OWNER_WORK_SUMMER_01_SHOE_REFERENCE
reference_budget: 5 images
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced resize"
generation_inputs:
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", responsibility: "current Body01 neck-below body proportions, waist/hip relation, thigh/calf volume, straight leg axes, foot scale and neutral stance", must_not_define: "face, facial identity, hair, clothing design, hosiery material, shoes, lighting or background"}
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", responsibility: "source-derived face geometry, facial relationships, natural skin and neutral expression", must_not_define: "body, hair, clothing, pose, lighting or background"}
  - {asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png", responsibility: "Hairstyle A only", must_not_define: "face, body, skin, clothing, pose, lighting or background"}
  - {asset_id: OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_07_15D_GRAY_MATTE_FRONT/OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001.png", responsibility: "smoky-gray 15D matte hosiery color, textile texture and continuous leg-to-foot coverage", must_not_define: "face, body anatomy, skirt, shoe design or background"}
  - {asset_id: OWNER_WORK_SUMMER_01_SHOE_REFERENCE_TOP_SIDE_FRONT, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/reference_inputs/garment_references/unnamed.jpg", responsibility: "supplied shoe top, side and front views for taupe color, square toe, rectangular vamp buckle and block heel", must_not_define: "owner identity, body, hosiery, clothing other than footwear or background"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and face-contamination QA only"}
  - {asset_id: OWNER_BODY_01_FRONT_CANON_007, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png", purpose: "post-generation body proportion comparison only"}
  - {asset_id: OWNER_WORK_SUMMER_01_WORN_FULL_BODY_v002, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/candidates/v002_worn_full_body/OWNER_WORK_SUMMER_01_WORN_FULL_BODY_v002.png", purpose: "previous candidate comparison only; never a generation input"}
authoritative_for:
  - "L2 summer officewear worn full-body presentation"
  - "full outfit fit over current Body01 proportions"
must_not_define:
  - "new Character Canon or permanent identity facts"
  - "AI-to-AI face or body lineage"
  - "future video keyframe identity"
output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/candidates/v003_worn_full_body/OWNER_WORK_SUMMER_01_WORN_FULL_BODY_v003.png
sha256: 1e68e636ad962852bb8145fa64ed5f39d0f99f3a30334b9582af3a1dcec7c10e
dimensions: 1086x1448
qa_status: TECHNICAL_PRECHECK_PASS_PENDING_USER_REVIEW
```

## Prompt assembly

Use case: identity-preserve
Asset type: L2 summer officewear worn full-body fit-validation candidate

Generate one fresh photorealistic full-body frontal neutral-standing image of the same adult woman, from the top of the head to the floor, with the complete outfit worn on her. Use the face-excluded Body01 reference as the sole body-proportion authority below the face. Preserve Body01 neck, shoulders, torso, waist/hip relationship, thigh/calf volume, foot scale and stance exactly. Use the source-derived face, Hairstyle A, hosiery material and supplied shoe only by their declared responsibilities. Do not use any generated Face/Body/outfit image as a generation input.

Keep the neck upright, head level, face neutral, eye-level camera, arms relaxed. Make the lower legs especially straight: each tibia/knee/ankle axis should read as a clean near-vertical line from knee through calf to ankle, with minimal outward or inward bowing and no lateral calf drift. Keep both legs close together but uncrossed, feet parallel and fully grounded. Do not slim, widen, lengthen, shorten or redesign Body01 proportions.

Dress her in the complete summer officewear outfit: black fitted short-sleeve top with a noticeably larger and lower rounded neckline, still rounded and not V-shaped; short warm-white/champagne polka-dot skirt with moderate black dots, moderate spacing and tailored slim straight-to-soft-tapered silhouette; not umbrella-shaped, not strongly A-line and not bodycon. Add clearly smoky-gray 15D matte pantyhose: darker and grayer than v002, a neutral charcoal-smoke gray veil, yet still thin and translucent enough for natural skin tone to remain visible underneath. Preserve continuous coverage from waist through thighs, knees, straight calves, ankles, heels, insteps and toes; no bare gaps, toe-cap seam, latex, PVC, plastic, rubber, liquid or body paint. Add supplied gray-beige/light-champagne taupe closed-toe square-toe pumps with rectangular vamp buckles and modest block heels; no open-toe shoes, ankle straps, logos or text.

Neutral gray-white seamless studio, soft even 5200–5600K light, 70–85mm-equivalent eye-level camera, exact native 3:4 portrait, full head/hands/legs/feet in frame, no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Check source-derived face compliance and no AI contamination; exact Body01 full-body proportions; especially straight lower-leg axes; Hairstyle A; larger/lower rounded neckline; smoky-gray yet translucent 15D matte hosiery; continuous toe/foot coverage; supplied shoe geometry; full-foot grounding. No promotion without explicit user approval.
