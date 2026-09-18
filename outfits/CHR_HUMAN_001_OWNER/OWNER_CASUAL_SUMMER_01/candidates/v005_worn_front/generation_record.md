# OWNER_CASUAL_SUMMER_01_WORN_FRONT_v005 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_CASUAL_SUMMER_01_WORN_FRONT
outfit_id: OWNER_CASUAL_SUMMER_01
level: L2
candidate_version: v005
target_canon_version: owner_v1.0
spec_revision: draft_1.235
identity_revision: draft_0.185
status: REVIEW_REQUIRED
approval_status: PENDING_USER_REVIEW
gate: L2 episode outfit fit-validation
generation_tool: built_in_image_gen
reference_set_ids:
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
  - OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_budget: 5 images
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced 1536x2048 resize"
generation_inputs:
  - {asset_id: OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/design_reference/OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE.png", responsibility: "approved summer outfit design: camisole, shorts, shoes, earrings and hosiery concept", must_not_define: "owner face, body, skin, hair, pose, lighting or background"}
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", responsibility: "current Body01 neck-below proportions, waist/hip relationship, straight leg axes, outer contours, foot scale and neutral stance", must_not_define: "face, facial identity, hair, clothing, hosiery material, lighting or background"}
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", responsibility: "source-derived face geometry, facial relationships, natural skin and neutral expression", must_not_define: "body, hair, clothing, pose, lighting or background"}
  - {asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png", responsibility: "Hairstyle A only", must_not_define: "face, body, skin, clothing, lighting or background"}
  - {asset_id: OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001, path: "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png", responsibility: "continuous light-nude 15D matte/velvet sheer hosiery, visible textile presence, foot coverage and toe tension", must_not_define: "identity, body/foot anatomy, clothing design, nail color, pose or background"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and face-contamination QA only"}
  - {asset_id: OWNER_BODY_01_FRONT_CANON_007, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png", purpose: "post-generation body proportion comparison only"}
  - {asset_id: OWNER_CASUAL_SUMMER_01_WORN_FRONT, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/worn_front/OWNER_CASUAL_SUMMER_01_WORN_FRONT.png", purpose: "historical outfit-fit comparison only; never a generation input"}
authoritative_for:
  - "L2 summer casual outfit worn-front presentation"
  - "outfit fit over current Body01 proportions"
must_not_define:
  - "new Character Canon or permanent identity facts"
  - "AI-to-AI face or body lineage"
  - "other outfit designs, body angles or poses"
  - "video keyframe identity"
output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/candidates/v005_worn_front/OWNER_CASUAL_SUMMER_01_WORN_FRONT_v005.png
sha256: 9eae0d53f3f73da8732dcfdb5a54bccfbc9a22f58e8d7e871aa54bbedd
dimensions: 1086x1448
qa_status: TECHNICAL_PRECHECK_PASS_PENDING_USER_REVIEW
```

## Prompt assembly

Generate one fresh photorealistic full-body frontal neutral-standing L2 outfit-fit reference of the same adult woman. Image 1 defines only the approved summer outfit design. Image 2 defines current Body01 neck-below proportions and straight-leg silhouette only. Image 3 defines the face and skin from source-derived recovery only. Image 4 defines Hairstyle A only. Image 5 defines hosiery textile only. Do not use any generated Face/Body image or previous worn-front candidate as a generation input.

Use the current Body01 proportions exactly: coherent 168 cm / approximately 60 kg adult scale, current narrower natural waist, accepted hip and thigh-root relationship, naturally full thighs and calves, straight knee–tibia–ankle axes, outer calf contours descending continuously from the outer thigh contours, narrow non-fused leg gap, full head/hands/feet in frame and both feet flat. The outfit must fit this body without slimming, widening, shortening, lengthening or redesigning the body. Keep the neck upright and natural, face neutral, eye-level camera and Hairstyle A.

Use the approved OWNER_CASUAL_SUMMER_01 design exactly: white lightweight V-neck floral lace-trim camisole with narrow straps and sparse small blue floral motifs; clearly high-waisted light-blue denim shorts with tall waistband, front pockets and slightly rolled/frayed hem; white suede one-band open-toe mule heels with a tapered, non-uniform vamp strap and modest slim lower heel; gold-tone dangling floral earrings with blue/blue-green teardrop stones. No dress, skirt, leggings, jacket, extra shirt, logos or extra accessories.

The light-nude sheer hosiery must be unmistakably visible over both straight legs and feet as one continuous realistic textile from waist through thighs, knees, calves, ankles, heels, insteps and toes. Give it restrained micro-sheen and a slightly pale textile veil, with natural fabric tension around the toes; it must never look like bare skin, latex, PVC, plastic, rubber, liquid or body paint. Because the shoes are open-toe, keep the hosiery visible at the front feet and toes with a continuous material transition and softly diffused burgundy nail color beneath the fabric; no bare gaps, hard white rings, toe seams or material breaks.

Neutral gray-white seamless studio, soft even 5200–5600K light, level 70–85mm-equivalent camera, exact native 3:4 portrait, relaxed arms, uncrossed straight legs, no body twist, no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Check source-derived face compliance and no AI contamination; Body01 waist/hip, thigh/calf volume and straight-leg correspondence; outfit fidelity; high-waist shorts; tapered white mule strap; earrings; visible continuous hosiery; no bare leg/foot gaps or plastic appearance; full-foot grounding; framing and absence of extra anatomy. No promotion without explicit user approval.
