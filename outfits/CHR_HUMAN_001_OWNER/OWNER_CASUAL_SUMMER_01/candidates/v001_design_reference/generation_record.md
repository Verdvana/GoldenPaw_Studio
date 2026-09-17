# Generation Record

- asset_id: `OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_CASUAL_SUMMER_01`
- level: `L2`
- candidate_version: `v001`
- status: `REVIEW_REQUIRED`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/candidates/v001_design_reference/OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE_v001.png`
- output_sha256: `a595415a2fc6148edfa8214b607c4591c033ccbea5740bfcb8af480fdd6d314b`
- use_case: `product-mockup`
- reference_budget: `5 supplied garment/accessory photos; no identity references`

## Generation inputs

The five supplied local photographs are clothing/accessory reference images only:

- `IMG_2744.jpg`: metallic strappy high-heel sandal construction and shine
- `IMG_2747.JPG`: denim shorts back construction, patch pockets, hem
- `IMG_2748.JPG`: denim shorts front construction, waistband and pockets
- `IMG_2749.jpg`: white floral lace-trim camisole construction and print
- `IMG_2750.jpg`: gold-tone dangling blue-stone earring construction

Additional text-only material contract: light nude sheer pantyhose with restrained
micro-sheen and continuous waist-to-toes coverage.

## QA comparison only

- none; this is a clothing-only, no-person asset

## Responsibilities and exclusions

The references define only garment/accessory silhouette, construction, color,
pattern, finish, and material behavior as listed above. They must not define any
person, face, body, skin, hair, pose, lighting, background, or photography style.

## Prompt assembly

Use case: product-mockup
Asset type: L2 clothing-only outfit design reference
Primary request: create a clean, photorealistic fashion catalog flat-lay / ghost-mannequin presentation of one complete summer casual outfit, with no visible person or body.
Input images: five supplied reference photos, each used only for its declared garment or accessory responsibility.
Scene/backdrop: neutral warm-white studio background, uncluttered catalog presentation.
Subject: white floral lace-trim camisole top; light-blue high-waisted denim shorts matching the supplied front and back construction; light nude sheer micro-sheen pantyhose shown as a folded/laid textile layer and visually continuous with the outfit concept; reflective metallic strappy open-toe high-heel sandals; gold-tone dangling earrings with clear stones and blue-green teardrop stones.
Style/medium: high-end photorealistic product catalog photography.
Composition/framing: vertical 4:5, complete outfit arranged front-facing from top to footwear, accessories placed beside the outfit; no mannequin head, no hands, no model, no body.
Lighting/mood: soft diffused studio light, accurate material texture, restrained shadows.
Constraints: preserve the supplied garment and accessory construction; no logos or readable brand text; show hosiery as sheer textile, not plastic; no person or anatomical form.
Avoid: face, body, skin, hair, mannequin, model, hands, extra garments, extra accessories, distorted clothing, extra limbs, typography, watermark, latex/PVC/rubber/liquid appearance.

## Seed and settings

- seed: not exposed by built-in ImageGen
- settings: built-in ImageGen default; output rendered as 4:5 catalog composition

## QA status

- visual inspection: PASS — clothing-only composition; no person/body/face/hair
- garment fidelity: PASS — top, shorts, earrings, and sandals visibly represented
- identity contamination check: PASS — no identity-bearing subject appears
- material QA: PASS_WITH_REVIEW — light nude micro-sheen hosiery rendered without obvious latex/PVC appearance; user review still required
