# Reference Plan — SOC_TRAVEL_002_IMG_01

Fresh L3 candidate. Generate from approved master assets and the scoped incoming pose reference. No prior/generated shot is an input. The reference person defines no owner identity, body, hair, face or clothing.

## Generation inputs

| Order | Asset ID | Path | Responsibility | Must not define |
|---|---|---|---|---|
| 1 | `SOC_TRAVEL_002_REF_001` | `social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/1.jpg` | Prone/reclined pose, leg/arm placement as visible, behind-the-subject camera position, centered cabin-door/ocean framing, broad cruise-cabin/balcony context | Person identity/face/body shape/hair/clothing/hosiery, exact room decor, lighting/color grade, text/watermark |
| 2 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` | Owner neck-below body proportions, limb mass, leg/foot scale; deterministic face-excluded geometry only | Face, hair, outfit, hosiery material, pose, lighting, environment |
| 3 | `L0_OWNER_006` | `characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg` | Real-source Hairstyle B construction only | Face identity or expression, body, clothing, pose, lighting, environment |
| 4 | `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001` | `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/CHR_WOMAN_001_HB04_HAIR_B.jpg` | Approved Hairstyle B design/color/exposure and surface appearance only | Face generation/identity, body, clothing, pose, lighting, environment |
| 5 | `OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE` | `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/design_reference/OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE.png` | Approved summer outfit design: camisole, denim shorts, light-nude hosiery, white suede mule heels and earrings | Owner identity/face/body/skin/hair/pose, shot lighting or background |

The interface allows at most five image references. The approved rear B hairstyle Canon was reviewed for planning but is not attached; rear hair geometry is described from the L0 hairstyle source and scoped B appearance Canon.

## QA comparison only

- `OWNER_BODY_01_FRONT_CANON_007` — body-proportion comparison only; not a generation input.
- Face Canon comparison is not applicable because the reference framing hides the owner's face. If a face becomes visible in the output, add the approved Face Canon only to QA and reject the candidate unless its face was generated from the applicable source-derived L0 Face method.

## Common series look

Apply the post-wide look: same bright late-morning/midday cruise day, same modern phone main camera character (about 26 mm equivalent), natural daylight, consistent neutral white balance/exposure/contrast/color and sharpness. Match the reference's camera placement and composition; reframe minimally to 4:5 vertical. No ultra-wide distortion, portrait cutout blur, filters, text, logo, watermark or social UI.
