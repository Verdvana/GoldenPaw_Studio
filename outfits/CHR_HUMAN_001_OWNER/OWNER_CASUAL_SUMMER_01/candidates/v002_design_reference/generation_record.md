# Generation Record

- asset_id: `OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_CASUAL_SUMMER_01`
- level: `L2`
- candidate_version: `v002`
- status: `REVIEW_REQUIRED`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/candidates/v002_design_reference/OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE_v002.png`
- output_sha256: `de5863d609070de6c790c7173a4d4625515279ffb6f6fccf7d1cb1d7983802ab`
- use_case: `product-mockup`
- reference_budget: `5 supplied garment/accessory photos; no identity references`

## Generation inputs and responsibilities

- `IMG_2780.jpg`: one-band open-toe mule high-heel silhouette and proportions only; source color is explicitly overridden to white suede.
- `IMG_2747.JPG`: denim shorts back construction, patch pockets and hem.
- `IMG_2748.JPG`: denim shorts front construction, waistband and pockets.
- `IMG_2749.jpg`: white floral lace-trim camisole construction and print.
- `IMG_2750.jpg`: gold-tone dangling earring construction with clear and blue-green stones.
- Text-only material contract: light nude sheer pantyhose with restrained micro-sheen and continuous waist-to-toes coverage.

These references define only the listed garment/accessory properties. They must not define any person, face, body, skin, hair, pose, identity, lighting or background.

## QA comparison only

- none; clothing-only asset

## Prompt assembly

Create one clean, photorealistic fashion catalog flat-lay / ghost-mannequin presentation of the complete summer casual outfit, with no visible person, mannequin body, hands or anatomical form. Arrange: a white lightweight floral lace-trim camisole with narrow straps; light-blue high-waisted denim shorts matching the supplied front and back construction with pockets and frayed/rolled hem; a folded light-nude sheer pantyhose layer with subtle micro-sheen and continuous textile concept; the supplied one-band open-toe mule high-heel silhouette recolored and remade as premium white suede with soft matte nap, clean edges and slim heel; and the supplied gold-tone dangling earrings with clear stones and blue-green teardrop stones.

Use a warm-white uncluttered studio catalog background, vertical 4:5 composition, soft diffused light and accurate textile/material texture. Preserve the supplied clothing/accessory construction while making the shoe unmistakably white suede rather than burgundy or metallic. No logos, readable text, watermark, model, face, body, skin, hair, extra garments, extra accessories, distorted clothing or plastic/latex/PVC/rubber/liquid appearance.

## Seed and settings

- seed: not exposed by built-in ImageGen
- settings: built-in ImageGen default; output rendered as 4:5 catalog composition

## QA status

- visual inspection: PASS — clothing-only composition; no person/body/face/hair
- garment fidelity: PASS — camisole, shorts, hosiery, earrings and updated shoe silhouette represented
- shoe silhouette and white suede: PASS_WITH_REVIEW — one-band mule heel preserved; shoe reads white with soft suede-like matte nap
- identity contamination: PASS — no identity-bearing subject appears
- hosiery material: PASS_WITH_REVIEW — light nude sheer textile rendered without obvious plastic/latex appearance; user review still required
