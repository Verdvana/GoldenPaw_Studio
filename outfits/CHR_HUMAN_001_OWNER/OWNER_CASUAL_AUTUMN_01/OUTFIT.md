# Outfit Design

- outfit_id: `OWNER_CASUAL_AUTUMN_01`
- display_name: 秋季休闲穿搭01
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- episode/scene scope: reusable owner casualwear / autumn
- character_outfit_root: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01`
- garment_reference_dir: `reference_inputs/garment_references/`
- garment_reference_files: `IMG_2812.jpg`, `IMG_2814.jpg`, `IMG_2816.JPG`, `IMG_2819.JPG`
- status: `DESIGN_REFERENCE_CANDIDATE_IN_PROGRESS`
- approval_status: `NOT_APPROVED`

## Reference boundary

Images in `reference_inputs/garment_references/` define only the declared garment,
footwear, accessories, construction, color, fit, pattern and material properties.
They must not define the owner's face identity, body geometry, skin, hair, pose,
lighting, background, or photography style. A person visible in a garment photo is
not an identity reference.

## Registered garment inventory

| Source | Declared responsibility | Must not define |
|---|---|---|
| `IMG_2812.jpg` | Black mini skirt: elastic waistband, layered ruffles, black lace trim, opaque black fabric | person, body, legs, proportions, lighting, background |
| `IMG_2814.jpg` | White fitted long-sleeve top: high ruffled neckline, upper lace yoke, fine floral lace texture, small centered gold button detail | person, face, body, hands, denim, belt, lighting, background |
| `IMG_2816.JPG` | Gunmetal/silver Mary Jane flats: glitter textile body, glossy black toe cap, black strap with small round metal button, low block heel | person, feet, leg proportions, lighting, background |
| `IMG_2819.JPG` | Silver-gray subtly sparkling sheer pantyhose: continuous waist-to-toe textile, soft hosiery sheen, non-oily finish | person, body, skin, feet, shoe pairing, lighting, background |

## Workflow

1. User adds clothing reference images to `reference_inputs/garment_references/`.
2. Register filenames, garment inventory and scoped responsibilities here.
3. Create a separate L2 candidate only after the reference set and design brief are ready.
4. Promotion to an approved L2 outfit requires explicit user approval.

## Must not redefine

The owner Face Canon, Body Canon, skin, hairstyle, or any L1 asset.
