# Reference Plan — SOC_TRAVEL_001_IMG_01

## Generation inputs

| Asset ID | Path | Responsibility | Must not define |
|---|---|---|---|
| L0_OWNER_013 | `characters/CHR_HUMAN_001_OWNER/source/identity/raw/15.jpg` | source-derived left 3/4 face identity and natural facial-plane evidence | outfit, body below neck, background, camera style, lighting |
| OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001 | `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png` | source-derived skin/face context without crown and without AI-generated face pixels | hair silhouette, outfit, body, background, lighting |
| OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1 | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` | neck-below body proportions, limb mass and leg/foot scale | face, hair, clothing design, hosiery material, lighting, background |
| OWNER_HAIR_A_02_3Q_CANON_001 | `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_02_3Q/OWNER_HAIR_A_02_3Q_CANON_001.png` | Hairstyle A left 3/4 projection: near-center part, long straight dark-brown fall and face-side panels | face, skin, body, outfit, lighting, background |
| OWNER_CASUAL_AUTUMN_01_DESIGN_REFERENCE | `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01/approved/design_reference/OWNER_CASUAL_AUTUMN_01_DESIGN_REFERENCE.png` | white lace-yoke top, black ruffled mini skirt, silver-gray micro-sparkle sheer pantyhose, gunmetal/silver Mary Jane flats | owner identity, face, body, hair, pose, lighting, background |

## QA comparison only

- `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001` — identity drift and facial-plane comparison only; never a generation input.
- `OWNER_BODY_01_FRONT_CANON_007` — body proportion comparison only; never a generation input.
- `OWNER_CASUAL_AUTUMN_01_WORN_FRONT` — outfit fit/pantyhose presentation comparison only if needed; its HAIRSTYLE_B content is excluded.

## Reference budget

- generation input image count: 5
- previous shot / prior AI candidate: none
- no reference image defines the environment;南京梧桐街道 is text-only temporary environment design
