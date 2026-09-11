# v008 Input Derivative Provenance

## B_FACE_SKIN_CROP_2X.png

- source authority: `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001`
- stored path: `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CROP_2X.png`
- source derivative: v007 `B_FACE_SKIN_CROP.png`, originally cropped `620x680+230+380` without retouching or color change
- operation in v008: deterministic Lanczos resize from `620x680` to `1240x1360`; no AI upscaling, sharpening, restoration, facial edit or color adjustment
- checksum SHA-256: `c966a30809db371216973b259fd20152ba165ca5ef43d36748d2ca45b35b507e`
- responsibility: face identity and B-anchor skin tone only
- independent authority: none

## DSC00847_HAIR_ONLY_MASKED.png

- source: `L0_OWNER_017` / `DSC00847.jpg`
- stored path: `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`
- operation: reused the single exact-size face-masked derivative by path
- mask: neutral-gray ellipse centered at `(370,270)`, radii `(165,205)`
- checksum SHA-256: `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`
- responsibility: visible Hairstyle A pixels only
- independent authority: none

Original sources remain unchanged. No generated Face candidate is included, and no candidate-local input image copies are retained.
