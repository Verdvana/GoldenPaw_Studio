# Reference Plan — SOC_TRAVEL_002_IMG_04

Fresh L3 generation, built independently from scoped sources and this shot's design reference. Input 1 is the sole authority for pose, expression action, camera position and composition. The person and all styling in it are excluded.

## Generation inputs

| Order | Asset ID | Path | Responsibility | Must not define |
|---|---|---|---|---|
| 1 | `SOC_TRAVEL_002_REF_004` | `social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/4.jpg` | Side-seated lounger pose; torso/head turned back; open-mouth laughing action; bent/extended leg arrangement; side camera and vertical crop; passenger-deck layout | Owner identity/face/features, body proportions, hair, outfit, accessories, hosiery, footwear, exact ship details, watermark/text |
| 2 | `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` | Source-derived L0 owner identity and facial-feature geometry | Source hairstyle, makeup, jewelry, retouched skin, source lighting/camera, body, clothing, pose or environment |
| 3 | `L0_OWNER_006` | `characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg` | Real-source Hairstyle B construction only | Face identity/features/expression, body, outfit, pose, camera, light or environment |
| 4 | `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001` | `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/CHR_WOMAN_001_HB04_HAIR_B.jpg` | Approved B hairstyle appearance, color and construction detail only | Face generation/identity, skin, body, clothing, pose, camera, light or environment |
| 5 | `OWNER_HOS_02_FEET_3Q_CANON_001` | `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_02_FEET_3Q/OWNER_HOS_02_FEET_3Q_CANON_001.png` | Scoped light-nude 15D hosiery response over foot, textile diffusion, intertoe tension, softened burgundy nails | Owner identity/body proportions, other foot views, pose, outfit, light or background |

`OWNER_CASUAL_SUMMER_01` is the text-only wardrobe authority: approved white floral lace-trim camisole, light-blue denim shorts, continuous light-nude sheer pantyhose and approved earrings. Shoes are excluded from the image. No outfit raster is attached. The body reference is text-only (168 cm / about 60 kg, natural proportions); no body raster is attached.

## QA comparison only

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — compare identity drift, feature relationships, skin contamination and projection after generation; never a generation input.
- `OWNER_BODY_01_FRONT_CANON_007` — compare owner body proportions after generation; never a generation input.
- `SOC_TRAVEL_002_IMG_02_CAND_08` — series-level light/exposure/color/camera continuity comparison only; never a face, body, hair, clothing, hosiery, pose or environment-identity input.

## Series continuity

Follow the shared bright late-morning cruise-day phone-camera contract in `../SHOT_DESIGN.md`: vertical 4:5, natural main-camera perspective near 26 mm equivalent, moderate contrast, consistent daylight/white balance/exposure, no portrait-mode blur, filters, logos, text or UI. Simplify ship finishes while retaining a plausible passenger deck and lounger context. Preserve the side viewpoint and pose geometry from reference 4 while framing a single owner from the approved sources.
