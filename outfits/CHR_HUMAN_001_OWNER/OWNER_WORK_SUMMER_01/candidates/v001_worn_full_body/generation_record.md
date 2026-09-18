# OWNER_WORK_SUMMER_01_WORN_FULL_BODY_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_WORK_SUMMER_01_WORN_FULL_BODY
outfit_id: OWNER_WORK_SUMMER_01
level: L2
candidate_version: v001
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
  - {asset_id: OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_07_15D_GRAY_MATTE_FRONT/OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001.png", responsibility: "gray 15D matte hosiery color, textile texture and continuous leg-to-foot coverage", must_not_define: "face, body anatomy, skirt, shoe design or background"}
  - {asset_id: OWNER_WORK_SUMMER_01_SHOE_REFERENCE_TOP_SIDE_FRONT, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/reference_inputs/garment_references/unnamed.jpg", responsibility: "supplied shoe top, side and front views for taupe color, square toe, rectangular vamp buckle and block heel", must_not_define: "owner identity, body, hosiery, clothing other than footwear or background"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and face-contamination QA only"}
  - {asset_id: OWNER_BODY_01_FRONT_CANON_007, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png", purpose: "post-generation body proportion comparison only"}
  - {asset_id: OWNER_WORK_SUMMER_01_DESIGN_REFERENCE_v006, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/candidates/v006_design_reference/OWNER_WORK_SUMMER_01_DESIGN_REFERENCE_v006.png", purpose: "post-generation outfit-shape comparison only; not a generation input"}
authoritative_for:
  - "L2 summer officewear worn full-body presentation"
  - "full outfit fit over current Body01 proportions"
must_not_define:
  - "new Character Canon or permanent identity facts"
  - "AI-to-AI face or body lineage"
  - "future video keyframe identity"
output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/candidates/v001_worn_full_body/OWNER_WORK_SUMMER_01_WORN_FULL_BODY_v001.png
sha256: e0d2aefb21b46340461305d6e86cf4de6e72d2185e2b7c8573ae4413702236ba
dimensions: 1086x1448
qa_status: TECHNICAL_PRECHECK_PASS_PENDING_USER_REVIEW
```

## Prompt assembly

Use case: identity-preserve
Asset type: L2 summer officewear worn full-body fit-validation candidate

Generate one fresh photorealistic full-body frontal neutral-standing image of the same adult woman, from the top of the head to the floor, with the complete outfit worn on her. Reference 1 is the sole body-proportion authority below the face: reproduce current Body01 neck, shoulders, torso, waist/hip relationship, naturally full thighs and calves, straight parallel leg axes, close neutral leg spacing, foot scale and stance. Reference 2 defines the face and skin from source-derived recovery only. Reference 3 defines Hairstyle A only. Reference 4 defines gray 15D matte hosiery only. Reference 5 defines the supplied shoes only. Do not use any generated Face/Body/outfit image as a generation input.

Preserve Body01 proportions exactly. Do not slim, widen, lengthen, shorten or redesign the neck, torso, waist, hips, thighs, calves, ankles or feet. Keep the neck upright and natural, head level, face neutral, eye-level camera, arms relaxed at the sides, legs straight and close together without crossing, both feet grounded and fully visible.

Dress her in the complete summer officewear outfit: a black fitted short-sleeve top with a distinctly low rounded neckline, lower than a standard crew neck but still rounded and not V-shaped; a short skirt with a white base shifted slightly warm toward champagne and medium-small black polka dots, moderately spaced with visible base fabric. The skirt is tailored and narrowed, slim straight-to-soft-tapered, not umbrella-shaped, not strongly A-line and not bodycon. Add gray ultra-sheer 15D matte pantyhose continuously from waist through thighs, knees, calves, ankles, heels, insteps and toes. The hosiery must visibly show matte gray textile texture while allowing natural skin tone to remain perceptible beneath the thin veil; no bare gaps, hard toe-cap seam, latex, PVC, plastic, rubber, liquid or body paint. Add the supplied gray-beige/light-champagne taupe closed-toe square-toe pumps with rectangular vamp buckles and modest block heels; no open-toe shoes, ankle straps, logos or text.

Neutral gray-white seamless studio, soft even 5200–5600K light, 70–85mm-equivalent eye-level camera, exact native 3:4 portrait, full head/hands/legs/feet in frame, no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Check source-derived face compliance and no AI contamination; exact Body01 full-body proportions; Hairstyle A; complete worn outfit; low rounded neckline; tailored skirt; clearly visible gray matte 15D hosiery texture and continuous toe/foot coverage; supplied shoe geometry; straight close legs; full-foot grounding. No promotion without explicit user approval.
