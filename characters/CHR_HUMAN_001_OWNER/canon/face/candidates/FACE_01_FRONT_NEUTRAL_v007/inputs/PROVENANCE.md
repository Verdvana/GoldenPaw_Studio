# v007 Input Derivative Provenance

## B_FACE_SKIN_CROP.png

- source: `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001`
- stored path: `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CROP.png`
- operation: reused the single v006 crop derivative by path; crop only, no generation, scaling, retouching or color adjustment
- original crop geometry: `620x680+230+380`
- checksum SHA-256: `760bb537c1062390d2334c0bf8b138f279ed776a1fc04c382e7ae2ca6c53a12c`
- responsibility: face identity and B-anchor skin tone only
- independent authority: none

## DSC00847_HAIR_ONLY_MASKED.png

- source: `L0_OWNER_017` / `characters/CHR_HUMAN_001_OWNER/source/identity/raw/DSC00847.jpg`
- stored path: `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`
- operation: exact-size PNG derivative with one opaque neutral-gray ellipse over the face; no crop, scaling, color adjustment, retouching or hair alteration
- mask geometry: ellipse centered at `(370,270)`, radii `(165,205)`
- dimensions: `769x1080`, identical to source dimensions
- checksum SHA-256: `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`
- responsibility: visible Hairstyle A pixels only
- mask meaning: excluded/unknown region; must not define head shape, hairstyle, color or background
- independent authority: none

Both original source files remain unchanged. This candidate directory retains provenance only and no input image copies.
