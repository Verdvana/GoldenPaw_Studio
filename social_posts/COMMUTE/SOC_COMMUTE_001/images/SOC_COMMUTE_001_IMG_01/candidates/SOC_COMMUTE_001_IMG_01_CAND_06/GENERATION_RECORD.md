# Generation Record — SOC_COMMUTE_001_IMG_01_CAND_06

- asset_id: SOC_COMMUTE_001_IMG_01
- candidate_id: SOC_COMMUTE_001_IMG_01_CAND_06
- asset_level: L3
- status: USER_APPROVED_L3
- generation_date: 2026-09-18
- generation_gate: User instruction “再试一次，同时注意丝袜颜色是眼灰色”; interpreted as 烟灰色.
- original_candidate_path: `social_posts/COMMUTE/SOC_COMMUTE_001/images/SOC_COMMUTE_001_IMG_01/candidates/SOC_COMMUTE_001_IMG_01_CAND_06/SOC_COMMUTE_001_IMG_01_CAND_06.png`
- current_approved_path: `social_posts/COMMUTE/SOC_COMMUTE_001/images/SOC_COMMUTE_001_IMG_01/approved/SOC_COMMUTE_001_IMG_01_APPROVED_v1.png`
- output_sha256: `e596f826a73215258c774d0911b37a163a044e4823859029f13809d1c1a747e5`
- settings: ImageGen, 4:5 vertical social still; seed unavailable

## Generation inputs

| Asset / path | Responsibility | Must not define |
|---|---|---|
| `L0_OWNER_012` — `characters/CHR_HUMAN_001_OWNER/source/identity/raw/14.jpg` | Owner identity features and natural facial relationships | Outfit, hair style, body scale, scene, lighting |
| `FACE_L0_OWNER_013_FEATURES_CROP_v1` — `reference_inputs/FACE_L0_OWNER_013_FEATURES_CROP_v1/FACE_L0_OWNER_013_FEATURES_CROP.png` | Lower-face contour and feature geometry from L0 source | Wedding styling, hair, body, clothing, lighting |
| `HAIR_A_01_FRONT` — `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png` | HAIRSTYLE_A structure only | Face, body, clothing, lighting, environment |
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` | 168 cm barefoot body proportions and neutral standing anatomy | Face, skin, hair, outfit, environment |
| `OWNER_WORK_SUMMER_01_WORN_FULL_BODY` — `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/approved/worn_full_body/OWNER_WORK_SUMMER_01_WORN_FULL_BODY.png` | Summer work outfit, smoke-gray 15D matte pantyhose, taupe buckle pumps | Face, skin, hair, body identity, environment |

## QA comparison only

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`: comparison for identity drift, jaw width, face scale and contamination only; never a generation input.

## Prompt assembly

Create one photorealistic 4:5 vertical iPhone social-media photograph: a neutral after-work full-body mirror selfie inside a generic modern office elevator. Use only the supplied L0 identity inputs for her face and the supplied face-excluded Body01 reference for her body. She is 168 cm barefoot in proportion; preserve a slender, balanced adult body and natural head-to-body scale. Her face must match the L0 inputs: refined smaller lower face, gently narrowed jawline, no broad square jaw, no enlarged cheeks, no face drift. Use HAIRSTYLE_A exactly: natural dark brown loose long waves, worn down, no gathered half-up styling.

She stands calmly with both feet together in a normal professional posture, weight balanced, knees and lower legs naturally straight and aligned without bowing. She wears the registered summer work outfit: fitted black low round-neck top, warm-champagne white short skirt with irregular black dots, smoke-gray 15D matte sheer pantyhose as one continuous textile garment, and light taupe-gray square-toe buckle pumps. The skirt has an asymmetric, incidental soft compression/rumple only at the tote side; avoid mirrored or evenly spaced pleats. A natural off-white canvas tote hangs from her free left hand. A plain white-and-blue generic work badge is visible, with no readable text.

She holds a silver-white iPhone 17 Pro in her right hand at face height, partially covering but not obscuring the face. Its rear has a wide horizontal raised camera plateau across most of the top, with three lenses grouped on the left. Frame the full body, including shoes, in the elevator mirror. Use a plausible handheld mirror-selfie viewpoint: phone and body are slightly off-center, with mild 3/4 oblique angle, subtle 2–3 degree roll and natural perspective/converging elevator lines; do not make a perfectly level, symmetrical, front-on elevator composition. Light only with cool-neutral elevator ceiling fixtures; no daylight, no mixed lighting. Generic brushed-metal elevator, clean mirror, restrained realism. No text, logos, watermark, beauty filter, stretched limbs, oversized head, oversized feet, oversized phone, duplicate limbs, warped reflection, fashion-poster pose, or artificial symmetry.

## QA targets

- Face: L0-consistent identity; smaller refined lower face and jaw; no contamination.
- Anatomy: 168 cm proportion, straight aligned lower legs, normal feet and phone scale.
- Material: smoke-gray 15D matte pantyhose, continuous and non-plastic.
- Composition: full body, credible handheld mirror perspective rather than centered architectural symmetry.
- Candidate remains L3 / REVIEW_REQUIRED; it cannot become Canon or downstream input.

## Approval record

- approved_by: user
- approval_date: 2026-09-18
- approval_evidence: “我觉得还行，登记，下一张”
- promotion: moved (not copied) to the approved L3 post-image path.
- scope: approval for publication review within this social post only; not Canon and not a generation input for subsequent images.
