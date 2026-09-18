# OWNER_WORK_SUMMER_01_WORN_LOWER_BODY_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_WORK_SUMMER_01_WORN_LOWER_BODY
outfit_id: OWNER_WORK_SUMMER_01
level: L2
candidate_version: v001
target_canon_version: owner_v1.0
status: REVIEW_REQUIRED
approval_status: PENDING_USER_REVIEW
gate: L2 officewear lower-body fit-validation
generation_tool: built_in_image_gen
reference_set_ids:
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_L1
  - OWNER_WORK_SUMMER_01_SHOE_REFERENCE
reference_budget: 4 images
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced resize"
generation_inputs:
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", responsibility: "current Body01 waist-down proportions, waist/hip relationship, thigh/calf volume, straight leg axes and foot scale", must_not_define: "face, facial identity, hair, upper-body clothing, skirt design, hosiery material, shoe design, lighting or background"}
  - {asset_id: OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_07_15D_GRAY_MATTE_FRONT/OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001.png", responsibility: "gray 15D matte hosiery, continuous waist-to-toes coverage, foot and toe material behavior", must_not_define: "face, body anatomy, skirt, shoe design, pose or background"}
  - {asset_id: OWNER_WORK_SUMMER_01_SHOE_REFERENCE_FRONT_SIDE, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/reference_inputs/garment_references/IMG_2791.JPG", responsibility: "reference shoe shape, color/material and front/side three-quarter construction views", must_not_define: "owner identity, body, hosiery, clothing other than footwear or background"}
  - {asset_id: OWNER_WORK_SUMMER_01_SHOE_REFERENCE_TOP_SIDE_FRONT, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/reference_inputs/garment_references/unnamed.jpg", responsibility: "reference shoe top, side and front views for buckle, toe box, vamp and heel geometry", must_not_define: "owner identity, body, hosiery, clothing other than footwear or background"}
qa_comparison_only:
  - {asset_id: OWNER_BODY_01_FRONT_CANON_007, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png", purpose: "post-generation waist-down proportion comparison only"}
  - {asset_id: OWNER_WORK_SUMMER_01_DESIGN_REFERENCE_v002, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/candidates/v002_design_reference/OWNER_WORK_SUMMER_01_DESIGN_REFERENCE_v002.png", purpose: "historical design-candidate comparison only; not a generation input"}
authoritative_for:
  - "L2 summer officewear lower-body presentation"
  - "skirt, gray 15D matte hosiery and reference-shoe fit over current Body01 lower-body proportions"
must_not_define:
  - "face, head, hair or upper-body identity"
  - "new Character Canon or permanent identity facts"
  - "AI-to-AI face or body lineage"
  - "future full-body or video identity"
output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/candidates/v001_worn_lower_body/OWNER_WORK_SUMMER_01_WORN_LOWER_BODY_v001.png
sha256: 52041357e09a4d0588942a9120074026e03423ace2856305272ded1810c72e1e
dimensions: 1086x1448
qa_status: TECHNICAL_PRECHECK_PASS_PENDING_USER_REVIEW
```

## Prompt assembly

Use case: photorealistic-natural
Asset type: L2 summer officewear lower-body fit-validation candidate

Generate one fresh photorealistic waist-down front neutral-standing outfit-fit image, cropped from just above the waist to the floor. No face, head, hair, neck, shoulders, chest, arms or upper body may appear. Use the face-excluded Body01 reference only for current waist-down body proportions, waist/hip relationship, naturally full thighs and calves, straight parallel leg axes and foot scale. Keep the legs straight, close together but not crossed, with the outer calf contours descending continuously from the outer thigh contours.

Dress the lower body in a short skirt with a white base that is visibly shifted slightly warm toward champagne, covered in dense small black polka dots. The skirt is fitted through the hips but deliberately intermediate between a slim straight skirt and a restrained A-line: not bodycon/hip-hugging, not a flared A-line, no pleats, no slit, no belt, no extra trim. The hem is around mid-thigh. The black top is excluded from this lower-body asset; do not show any upper torso or top hem.

Use continuous gray 15D matte pantyhose from the waist under the skirt through thighs, knees, calves, ankles, heels, insteps and toes. The gray color and matte textile must be clearly visible without latex, PVC, plastic, rubber, liquid or body-paint appearance. No hard waistband line, toe-cap seam, bare gaps or material discontinuity.

Use the supplied shoe reference exactly: gray-beige/light-champagne taupe closed-toe pump, slightly square toe, rectangular buckle across the vamp, clean low-to-moderate block heel, refined office shoe proportions. Preserve the reference shoe construction across both feet; no open-toe sandal, ankle strap, stiletto, logo or text.

Neutral gray-white seamless studio, soft even light, eye-level lower-body camera, full skirt hem and both feet in frame, no pose twist, no props, text, watermark or collage. Native exact 3:4 portrait. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Check no upper-body/face leakage; Body01 lower-body proportion and straight-leg correspondence; skirt base color and polka-dot density; intermediate straight-to-restrained-A silhouette; gray 15D matte hosiery continuity; shoe color, buckle, toe box and heel geometry; no logos, text or extra anatomy. No promotion without explicit user approval.
