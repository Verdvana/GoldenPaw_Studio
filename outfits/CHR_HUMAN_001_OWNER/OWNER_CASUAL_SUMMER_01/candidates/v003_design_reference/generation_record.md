# Generation Record

- asset_id: `OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_CASUAL_SUMMER_01`
- level: `L2`
- candidate_version: `v003`
- status: `APPROVED`
- original_candidate_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/candidates/v003_design_reference/OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE_v003.png`
- approved_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/design_reference/OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE.png`
- output_sha256: `a5e35b77fc25ba5ae80d6097c1138eaeba6bd3341360733912d8598f53d119c7`
- approval_date: `2026-09-18`
- approved_by: `user`
- use_case: `product-mockup`
- reference_budget: `5 supplied garment/accessory photos; no identity references`

## Correction focus from v002

- Camisole must match `IMG_2749.jpg`: thin white camisole, narrow straps, V-neckline with fine lace trim, lightweight drape, small sparse blue floral motifs; do not replace it with dense floral coverage or a different neckline.
- Shorts must match `IMG_2748.JPG` / `IMG_2747.JPG`: clearly high-waisted light-blue denim, tall waistband, front pockets, back patch pockets, and frayed/rolled hem.
- Shoe must match `IMG_2780.jpg` silhouette: one-band open-toe mule, vamp strap visibly tapered/non-uniform in width rather than a constant-width band, and a lower modest slim heel; recolor/material-convert from burgundy to white suede.

## Generation inputs and responsibilities

- `IMG_2780.jpg`: shoe silhouette, tapered vamp strap and lower heel proportions only; source color overridden to white suede.
- `IMG_2747.JPG`: shorts back construction, high waist, patch pockets and hem.
- `IMG_2748.JPG`: shorts front construction, high waist, waistband and pockets.
- `IMG_2749.jpg`: camisole neckline, lace trim, straps, lightweight white fabric and sparse blue floral print.
- `IMG_2750.jpg`: gold-tone dangling earring construction with clear and blue-green stones.
- Text-only material contract: light nude sheer pantyhose with restrained micro-sheen and continuous waist-to-toes coverage.

These references define only the listed clothing/accessory properties. They must not define any person, face, body, skin, hair, pose, identity, lighting or background.

## Prompt assembly

Create one photorealistic fashion catalog flat-lay of the complete summer casual outfit, with no person, mannequin, body, hands, head or anatomical form. Use a warm-white seamless studio background and vertical 4:5 composition.

Arrange the exact clothing details: a lightweight white camisole with narrow thin shoulder straps, a clear V-shaped neckline, delicate narrow lace trim following the V neckline, and a sparse small-scale floral print made of tiny blue flowers with restrained green stems; a clearly high-waisted pair of light-blue denim shorts with a tall structured waistband rising high above the hips, front pockets, button/zip fly, back patch-pocket construction implied by the companion reference, and a slightly rolled/frayed hem; a folded light-nude sheer pantyhose layer with subtle micro-sheen and realistic textile texture; a pair of open-toe one-band mule heels matching the supplied burgundy shoe silhouette, where the vamp strap is deliberately tapered and visibly non-uniform in width across its curve, with a lower modest slim heel that is only slightly elevated, not a tall stiletto, rendered in premium white suede with soft matte nap; and the supplied gold-tone dangling floral cluster earrings with clear stones and blue-green teardrop stones.

Prioritize faithful garment construction over generic fashion styling. The white camisole must visibly read as the supplied lace-trim sparse-blue-floral design; the shorts must visibly read as high-waisted; the shoes must visibly read as the supplied lower-heel tapered-band mule silhouette. No burgundy shoe color, no metallic shoe finish, no equal-width shoe strap, no tall heel, no generic tank top, no dense floral pattern, no low-rise shorts. No logos, readable text, watermark, extra garments, extra accessories, distorted objects, latex, PVC, rubber, liquid or body-paint appearance.

## Seed and settings

- seed: not exposed by built-in ImageGen
- settings: built-in ImageGen default; output rendered as 4:5 catalog composition

## QA status

- visual inspection: PASS — clothing-only composition; no person/body/face/hair
- top style and pattern: PASS_WITH_REVIEW — V lace trim, narrow straps and small sparse blue floral print present
- shorts high-waist and construction: PASS — visibly high-rise waistband, front pockets and frayed/rolled hem present
- shoe silhouette and white suede: PASS_WITH_REVIEW — tapered curved vamp strap and lower heel read correctly; user review still required for exact strap contour
- identity contamination: PASS — no identity-bearing subject appears
- hosiery material: PASS_WITH_REVIEW — light nude sheer textile rendered without obvious plastic/latex appearance
