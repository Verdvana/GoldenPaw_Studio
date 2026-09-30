# L0 Face Derivative — OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001

- source_asset_id: `L0_OWNER_013`
- source_path: `characters/CHR_HUMAN_001_OWNER/source/identity/raw/15.jpg`
- source_sha256: `1851e8decaa3430f127c3e720f7fba8bb119370008ef7795313fd6e76b396af0`
- operation: deterministic crop `700x850+75+100`; apply a hand-specified polygon mask with vertices `(265,185) (305,165) (350,155) (395,165) (435,185) (475,220) (515,275) (540,350) (550,440) (545,530) (525,620) (495,700) (455,765) (405,815) (365,840) (325,825) (285,795) (245,755) (205,700) (170,630) (145,555) (125,480) (115,410) (120,345) (140,285) (180,230) (220,200)`; composite masked-out area onto neutral gray; no resize, retouch, AI upscaling or color adjustment
- output_path: `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png`
- output_sha256: `1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91`
- responsibility: real-source facial feature geometry, recognizable identity and adult age only
- must_not_define: visible source hair, makeup, jewelry, source skin retouch/color, camera angle, lighting, body, clothing or background
- note: crop is a deterministic L0 derivative, not an AI-generated face and not a Canon asset

## OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001

- source_asset_id: `L0_OWNER_012`
- source_path: `characters/CHR_HUMAN_001_OWNER/source/identity/raw/14.jpg`
- source_sha256: `f7a83644f202ebec95134c6d115397b9f52f12e79b5fb227a6b79182026bd788`
- operation: deterministic crop `210x230+15+20`; preserve the source pixels; apply an ellipse mask centered at `(105,112)` with radii `(87,102)`; composite masked-out area onto neutral gray; no resize, retouch or color adjustment
- output_path: `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png`
- output_sha256: `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd`
- responsibility: natural warm-neutral skin color/texture baseline only; low-resolution source cannot define fine face geometry or lens-neutral proportions
- must_not_define: exact face geometry, source hairstyle, makeup, camera angle, body, clothing, lighting or background
- note: deterministic derivative from real L0; gray mask is deleted information and has no design authority
