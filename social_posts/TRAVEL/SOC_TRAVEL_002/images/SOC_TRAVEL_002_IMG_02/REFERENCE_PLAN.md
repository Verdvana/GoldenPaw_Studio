# Reference Plan — SOC_TRAVEL_002_IMG_02

Fresh L3 generation, independent of shot 01. Input 1 is one-shot pose/camera/cruise-deck guidance; the person in it is not an identity, body, hair or wardrobe reference. No preceding/generated shot is attached.

## Generation inputs

| Order | Asset ID | Path | Responsibility | Must not define |
|---|---|---|---|---|
| 1 | `SOC_TRAVEL_002_REF_002` | `social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/2.jpg` | Reclined deck-chair articulation, leg/arm placement, side/rear camera angle, vertical medium-wide frame, railing/ocean layout | Identity/face, body proportions, hair, outfit, hosiery material, exact ship design, branded food/drink, text/watermark |
| 2 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` | Owner neck-below body proportions, limb mass and foot scale; face-excluded geometry | Face, hair, outfit, hosiery material, pose, lighting, environment |
| 3 | `L0_OWNER_006` | `characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg` | Real-source Hairstyle B construction only | Face identity/expression, body, clothing, pose, lighting or environment |
| 4 | `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001` | `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/CHR_WOMAN_001_HB04_HAIR_B.jpg` | Approved Hairstyle B design/color/exposure and surface appearance only | Face generation/identity, body, clothing, pose, lighting or environment |
| 5 | `OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001` | `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_07_15D_GRAY_MATTE_FRONT/OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001.png` | Interdigital fabric-tension pattern and softened burgundy nails beneath sheer textile only; ignore source hosiery color | Gray hue, target light-nude color, owner identity/body proportions, pose, outfit, lighting/background |

The five-image limit is filled by pose, face-excluded body, two required HAIRSTYLE_B sources and scoped hosiery-foot Canon. `OWNER_CASUAL_SUMMER_01` remains an approved **text-only wardrobe authority** from `OUTFIT.md` and its approval record; spell out the approved outfit in the prompt without attaching its design-reference raster. `OWNER_HOS_07` contributes only cloth tension and softened nail visibility; the target light-nude color comes from the outfit contract.

## QA comparison only

- `OWNER_BODY_01_FRONT_CANON_007` — body-proportion comparison only.
- Owner Face Canon comparison is required only if the generated output unexpectedly exposes facial features; it is QA-only and never a generation input. Target framing keeps the face turned away/obscured.

## Series continuity

Use the common phone-camera/daylight/white-balance/color specification in `../SHOT_DESIGN.md`. Match input 2's camera angle and composition closely while keeping this within the same bright late-morning/midday cruise day as all other shots. Keep the outfit, hair design, sea/sky look and deck finish consistent with shot 01, but generate independently.
