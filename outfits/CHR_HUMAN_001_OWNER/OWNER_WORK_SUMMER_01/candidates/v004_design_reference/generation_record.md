# OWNER_WORK_SUMMER_01_DESIGN_REFERENCE_v004 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_WORK_SUMMER_01_DESIGN_REFERENCE
outfit_id: OWNER_WORK_SUMMER_01
level: L2
candidate_version: v004
target_canon_version: owner_v1.0
status: REVIEW_REQUIRED
approval_status: PENDING_USER_REVIEW
gate: L2 outfit-shape design reference
generation_tool: built_in_image_gen
reference_set_ids:
  - OWNER_WORK_SUMMER_01_SHOE_REFERENCE
  - OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_L1
reference_budget: 3 images
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced resize"
generation_inputs:
  - {asset_id: OWNER_WORK_SUMMER_01_SHOE_REFERENCE_FRONT_SIDE, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/reference_inputs/garment_references/IMG_2791.JPG", responsibility: "reference shoe shape, color/material and front/side construction", must_not_define: "owner identity, body, hosiery, clothing other than footwear or background"}
  - {asset_id: OWNER_WORK_SUMMER_01_SHOE_REFERENCE_TOP_SIDE_FRONT, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/reference_inputs/garment_references/unnamed.jpg", responsibility: "reference shoe top, side and front views for buckle, toe box, vamp and heel geometry", must_not_define: "owner identity, body, hosiery, clothing other than footwear or background"}
  - {asset_id: OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_07_15D_GRAY_MATTE_FRONT/OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001.png", responsibility: "gray ultra-sheer 15D matte hosiery color and textile behavior", must_not_define: "owner identity, body anatomy, pose or background"}
qa_comparison_only:
  - {asset_id: OWNER_WORK_SUMMER_01_DESIGN_REFERENCE_v003, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/candidates/v003_design_reference/OWNER_WORK_SUMMER_01_DESIGN_REFERENCE_v003.png", purpose: "visual comparison only; never a generation input"}
authoritative_for:
  - "L2 summer officewear garment shape and material arrangement"
must_not_define:
  - "owner face, body, skin, hair or identity"
  - "worn fit, pose or anatomy"
  - "new Character Canon or future identity lineage"
output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/candidates/v004_design_reference/OWNER_WORK_SUMMER_01_DESIGN_REFERENCE_v004.png
sha256: 366ffd53a89f24a0b0923a35bce81fd9a055dc1e2edd26c1b196405238b5149f
dimensions: 1086x1448
qa_status: TECHNICAL_PRECHECK_PASS_PENDING_USER_REVIEW
```

## Prompt assembly

Use case: product-mockup
Asset type: L2 summer officewear unworn design reference

Create one clean photorealistic studio product-board image of the complete summer officewear outfit, entirely unworn and without any human, mannequin, torso form, hands, legs or body. Arrange the garments as a coherent flat-lay/catalog presentation on a neutral warm-gray background, with each item clearly separated and its silhouette unambiguous.

Show the full set: a black fitted short-sleeve top with a noticeably lower round neckline than a standard crew neck, still a clean round neckline and not a V-neck; a short skirt in a white base shifted slightly warm toward champagne, with black polka dots that are visibly larger than fine pin dots and more sparsely spaced, leaving more base fabric visible. The skirt should be narrowed and more tailored: a slim straight-to-soft-tapered silhouette with only a restrained ease toward the hem, clearly not an umbrella shape, not a strong A-line, and not bodycon or hip-hugging. No pleats, slit, belt or extra trim. Include one complete pair of gray ultra-sheer 15D matte pantyhose laid flat from waistband through both legs and feet. It must be visibly thinner and more transparent than ordinary opaque gray tights: natural skin tone should be clearly perceptible through the gray veil while the matte gray textile remains readable, with continuous waist-to-toes construction and no toe-cap seam. Include the supplied pair of gray-beige/light-champagne taupe closed-toe square-toe pumps with rectangular vamp buckles and modest block heels, matching the original shoe references.

Keep all items physically plausible as unworn objects with natural folds, seams, waistbands, sleeve openings, skirt hem, pantyhose waistband and toe shapes. Do not put anything on a body. Do not add jewelry, bag, jacket, belt, coat, mannequin, hangers, model, face, skin, hair or anatomy. Neutral soft even catalog lighting, orthographic-ish top/front product-board view, exact native 3:4 portrait, no watermark, logos, text or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Check no human or mannequin contamination; lower round neckline; sparse larger polka dots; tailored non-umbrella, non-bodycon skirt silhouette; visibly ultra-sheer gray 15D matte hosiery with skin showing through; complete hosiery shape; supplied shoe geometry; no extra wardrobe, logos or text. No promotion without explicit user approval.
