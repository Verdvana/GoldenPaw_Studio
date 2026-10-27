# Social Post Reference Plan

- post_id: SOC_OUTFIT_002
- image_asset_id: SOC_OUTFIT_002_IMG_02
- candidate_id: SOC_OUTFIT_002_IMG_02_CAND_14
- status: READY_FOR_GENERATION
- reference_count: 5 generation + 1 QA-only; project budget_limit: 8; tool image-input limit: 5
- selected_reference_set_ids: OWNER_L0_FACE_013_GEOMETRY_CROP_V1, OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1, OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE, OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE, OWNER_CASUAL_AUTUMN_02_WORN_FRONT_APPROVED_V015 (face-excluded derivative)
- resolved_from: registries/reference_sets.yaml and owner source/identity/REFERENCE_GUIDE.md; global face-safe override takes precedence over old Canon routing.

| Image index | Asset / path / checksum | Version | Responsibility | Must not define |
|---|---|---|---|---|
| 1 | OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001 / `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` / `1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91` | deterministic L0 derivative v1 | face identity and feature relationships only | hair, makeup, retouched skin, body, lighting, background |
| 2 | OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001 / `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png` / `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd` | deterministic L0 derivative v1 | natural warm-neutral skin context only | fine geometry, hair, body, clothes, source lighting |
| 3 | OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1 / `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` / `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | approved body v025 deterministic derivative | neck-below body proportions only | face, hair, skin color, calibration clothes, material, pose, lighting, background |
| 4 | OWNER_CASUAL_AUTUMN_02_WORN_FRONT_V015_FACE_EXCLUDED_v1 / `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/reference_inputs/WORN_FRONT_V015_FACE_EXCLUDED_v1/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v015_FACE_EXCLUDED.png` / `91b0fec2a53d9902fdb189ee722e5defe040b845b63f22dd16cb4706491b5cf1` | approved L2 v015 deterministic derivative | Autumn 02 clothes, fit/drape and white matte continuous hosiery only | face, skin, identity, hair, body proportions, shoes selection, scene |
| 5 | SOC_OUTFIT_002_IMG_01_CAND_04 / `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_01/approved/SOC_OUTFIT_002_IMG_01_APPROVED_v1.png` / `9ab51017ebd8f51d1e95cff34030414a590ab76a40de0b1752456504378f18b8` | approved L3 2026-10-17 | continuity only: picnic blanket and snack placement, grass/leaves, warm daylight | identity, face, skin, hair, body, clothing construction, hosiery material |

## Face-safe declaration

Face visible: approximately one quarter at frame edge. Applicable method: OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1; preserve identity and natural skin constraints, adapt camera to direct wide-angle selfie rather than studio reproduction. QA-only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`, `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`, SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`. Never attach QA Canon to ImageGen. No generated Face or uncropped Body/worn-front input. Excluded: all former IMG_02/03 unapproved candidates, other hairstyles and unrelated sources. Derivative provenance resides alongside each reusable derivative, not in candidate inputs.

## Tool reference budget adjustment

The first tool attempt rejected six paths before generation. Hair-only reference was inspected but omitted from actual tool inputs; HAIRSTYLE_A is constrained by approved method text. No source folder reanalysis and no combined reference collage. Five actual inputs retain face geometry, skin, body, outfit/material and approved picnic continuity.

## Revision gate — 2026-10-27

User accepted other aspects of CAND_13 and requested narrower, relaxed hanging feet. This is attribute-scoped feedback, not approval of CAND_13 as a whole. Do not attach CAND_13; generate freshly from the five previously validated sources. Original one-quarter-face target is relaxed by latest user acceptance of other aspects.
