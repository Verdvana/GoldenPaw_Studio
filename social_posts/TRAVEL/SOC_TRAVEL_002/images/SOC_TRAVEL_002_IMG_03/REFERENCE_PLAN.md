# Reference Plan — SOC_TRAVEL_002_IMG_03

Fresh L3 generation, independent of shots 01–02. Input 1 is the sole authority for shot-03 pose mechanics, friendly smile action, high camera angle, close vertical composition, and cruise-deck/ocean layout. The visible person in it is not an identity, body, hair or wardrobe source.

## Generation inputs

| Order | Asset ID | Path | Responsibility | Must not define |
|---|---|---|---|---|
| 1 | `SOC_TRAVEL_002_REF_003` | `social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/3.jpg` | Low seated/crouched pose, bent knees, hands near legs, friendly closed-mouth smile action, high camera, close vertical framing, glass-deck/ocean composition | Identity/face features, body proportions, hair, outfit, hosiery, sandals/shoes, watermark/text, exact ship finishes |
| 2 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` | Owner neck-below body proportions and limb scale only | Face, hair, clothing, hosiery material/color, pose, camera, light, background |
| 3 | `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` | Source-derived L0 facial identity/feature geometry and adult age only; apply `FACE_01_FRONT_NEUTRAL_METHOD.md` identity and natural-skin prompt constraints | Source hairstyle, makeup, jewelry, retouched skin texture/color, source camera/light, clothing, body or background |
| 4 | `L0_OWNER_006` | `characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg` | Real-source Hairstyle B construction only | Face/identity/expression, body, clothing, pose, camera, lighting or environment |
| 5 | `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001` | `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/CHR_WOMAN_001_HB04_HAIR_B.jpg` | Approved B design, color and surface appearance only | Face generation/identity, body, clothing, pose, camera, lighting or environment |

`OWNER_CASUAL_SUMMER_01` is an approved text-only wardrobe authority for this shot: white floral lace-trim camisole, light-blue denim shorts, continuous light-nude sheer pantyhose, and earrings. No shoes may appear in frame. No wardrobe image is attached.

## QA comparison only

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — face identity drift, feature relationship, skin contamination and patch/artifact comparison only; never a generation input.
- `OWNER_BODY_01_FRONT_CANON_007` — body proportions comparison only; never a generation input.

## Series continuity

Use the shared daylight/phone-camera/color contract in `../SHOT_DESIGN.md`. Keep this a close high-angle cruise-deck snapshot with glass/reflective deck and ocean geometry; simplify the ship environment while matching the same bright cruise day. Remove the source watermark and all overlay text. Shoes are excluded from the frame, not replaced with reference sandals.
