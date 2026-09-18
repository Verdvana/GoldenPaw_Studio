# OWNER_CASUAL_SUMMER_01_WORN_FRONT_v006 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_CASUAL_SUMMER_01_WORN_FRONT
outfit_id: OWNER_CASUAL_SUMMER_01
level: L2
candidate_version: v006
target_canon_version: owner_v1.0
spec_revision: draft_1.235
identity_revision: draft_0.185
status: APPROVED
approval_status: APPROVED_BY_USER
gate: L2 episode outfit fit-validation
generation_tool: built_in_image_gen
reference_set_ids:
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
  - OWNER_HAIRSTYLE_B_L0
  - OWNER_HAIRSTYLE_B_APPEARANCE_L1
  - OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_budget: 6 images
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced resize"
generation_inputs:
  - {asset_id: OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/design_reference/OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE.png", responsibility: "approved summer outfit design", must_not_define: "owner face, body, skin, hair, pose, lighting or background"}
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", responsibility: "current Body01 neck-below proportions, waist/hip relationship, straight leg axes, close leg spacing, outer contours, foot scale and stance", must_not_define: "face, facial identity, hair, clothing, hosiery material, lighting or background"}
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", responsibility: "source-derived face geometry, facial relationships, natural skin and neutral expression", must_not_define: "body, hair, clothing, pose, lighting or background"}
  - {asset_id: L0_OWNER_006, path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg", responsibility: "real-source Hairstyle B hairline, rearward gathering, face-framing strands and gathered-updo relationship only", must_not_define: "face identity, body, clothing, pose, lighting or background"}
  - {asset_id: OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/CHR_WOMAN_001_HB04_HAIR_B.jpg", responsibility: "approved Hairstyle-B design/color/exposure calibration only", must_not_define: "owner face generation, face identity, body, clothing, pose, lighting or background"}
  - {asset_id: OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001, path: "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png", responsibility: "continuous light-nude 15D matte/velvet sheer hosiery, visible textile at toes, fabric tension and foot coverage", must_not_define: "identity, body/foot anatomy, clothing design, nail color, pose or background"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and face-contamination QA only"}
  - {asset_id: OWNER_BODY_01_FRONT_CANON_007, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png", purpose: "post-generation body proportion comparison only"}
  - {asset_id: OWNER_CASUAL_SUMMER_01_WORN_FRONT_v005, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/candidates/v005_worn_front/OWNER_CASUAL_SUMMER_01_WORN_FRONT_v005.png", purpose: "previous candidate comparison only; never a generation input"}
authoritative_for:
  - "L2 summer casual outfit worn-front presentation"
  - "outfit fit over current Body01 proportions"
must_not_define:
  - "new Character Canon or permanent identity facts"
  - "AI-to-AI face or body lineage"
  - "other outfit designs, body angles or poses"
  - "video keyframe identity"
original_candidate_path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/candidates/v006_worn_front/OWNER_CASUAL_SUMMER_01_WORN_FRONT_v006.png
approved_path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/worn_front/OWNER_CASUAL_SUMMER_01_WORN_FRONT.png
sha256: 81b48490f4789c9b9cee6a34130206d770b01e1480871c24f2a5e4104e6421c0
dimensions: 1086x1448
approval_date: 2026-09-18
approved_by: user
qa_status: APPROVED
```

## Prompt assembly

Use case: photorealistic-natural
Asset type: L2 summer casual outfit fit-validation candidate

Generate one fresh photorealistic full-body frontal neutral-standing image of the same adult woman. Image 1 defines only the approved summer outfit. Image 2 defines current Body01 neck-below proportions and straight-leg silhouette only. Image 3 defines the face and skin from source-derived recovery only. Images 4–5 define Hairstyle B only. Image 6 defines hosiery textile only. Do not use any generated Face/Body image or previous worn-front candidate as a generation input.

Keep current Body01 proportions exactly: adult 168 cm / approximately 60 kg scale, narrow natural waist, accepted hip and thigh-root relationship, naturally full thighs and calves, straight knee–tibia–ankle axes. Bring the legs closer together than v005 while keeping them uncrossed: inner leg spacing should be narrow and controlled, with both leg axes visibly vertical and parallel, and the outer calf contours descending continuously from the outer thigh contours. Do not slim, widen, shorten, lengthen or redesign the body. Upright natural neck, neutral face, eye-level camera, full head/hands/feet in frame, both feet grounded.

Use the approved OWNER_CASUAL_SUMMER_01 design exactly: white lightweight V-neck floral lace-trim camisole with narrow straps and sparse small blue floral motifs; high-waisted light-blue denim shorts with tall waistband, front pockets and slightly rolled/frayed hem; white suede one-band open-toe mule heels with a tapered non-uniform vamp and modest slim heel; gold-tone dangling floral cluster earrings with blue teardrop stones.

Use Hairstyle B only: a compact center-parted front, smooth rearward gathering, controlled crown volume, bilateral face-framing wisps and the approved gathered-updo/claw-clip logic. Do not blend Hairstyle A or long loose hair.

Make the light-nude sheer hosiery unmistakable at the toes: one continuous realistic textile from waistband through thighs, knees, calves, ankles, heels, insteps and toes. At both open-toe shoes, show a clearly visible pale sheer veil over every toe, with fine fabric grain, restrained micro-sheen, realistic toe-box tension and softly diffused burgundy nail color beneath the hosiery. The toe hosiery must not disappear into skin and must not create a hard color boundary at the toe roots. No bare leg/foot gaps, latex, PVC, plastic, rubber, liquid or body-paint appearance.

Neutral gray-white seamless studio, soft even 5200–5600K light, level 70–85mm-equivalent camera, exact native 3:4 portrait, relaxed arms, no twist, no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Check source-derived face compliance and no AI contamination; Hairstyle B only; Body01 waist/hip, thigh/calf volume and parallel straight-leg correspondence; narrow leg spacing; outfit fidelity; clearly visible continuous hosiery at both toe areas; no bare toe gaps, hard rings or plastic appearance; full-foot grounding; framing and absence of extra anatomy. No promotion without explicit user approval.
