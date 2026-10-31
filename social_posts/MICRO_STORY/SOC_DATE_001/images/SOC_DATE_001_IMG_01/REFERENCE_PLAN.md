# Social Post Reference Plan

- post_id: SOC_DATE_001
- image_asset_id: SOC_DATE_001_IMG_01
- candidate_id: SOC_DATE_001_IMG_01_CAND_01
- status: GENERATION_AUTHORIZED
- reference_count: 5
- budget_limit: 8
- selected_reference_set_ids: [OWNER_L0_FACE_013_GEOMETRY_CROP_V1, OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1, OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE, OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE]

| Priority | ID / path | Version | Use | Responsibility | Must not define |
|---|---|---|---|---|---|
| 1 | `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` / `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` | L0 deterministic v1 | generation_input | face identity and feature geometry | makeup, skin retouch, hair, jewelry, body, light, camera, scene |
| 2 | `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` / `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png` | L0 deterministic v1 | generation_input | natural skin baseline | fine geometry, hair, body, clothes, light, camera, scene |
| 3 | `OWNER_HAIRSTYLE_A_FACE_MASKED_001` / `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png` | L0 deterministic v1 | generation_input | Hairstyle A only | face, skin, body, clothing, pose, light, background, mask |
| 4 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` / `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` | approved Body007 deterministic v7 | generation_input | neck-below body proportions only | face generation, skin color, hair, static pose, swimsuit, hosiery, lighting, background |
| 5 | `OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v003` / `outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v003.png` | L2 APPROVED v003 | generation_input | clothing design and white sheer closed-toe coverage | face, body proportions, skin, hair, identity, pose, light, scene |
| QA | `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg` | approved L1 | qa_comparison_only | identity and face contamination comparison | all generation input authority |

## Face-safe declaration

Face visible: yes. L0 geometry + natural-skin derivatives are sole face authority under FACE_01 method prompt constraints. AI Body source is supplied only through the face-excluded v7 derivative for neck-below geometry. Full checksums in candidate record.

## Conflict resolution and excluded references

Global source-derived rule overrides stale registry recovery B-face routing. Generated B_FACE_SKIN_CONTEXT_NO_CROWN is excluded. Fitting v005 is validation-only and excluded. No prior shot, AI Face, full Body image, material from another outfit or residence reference is attached. Clothing-only v003 resolves through nearest OUTFIT.md. No independent denier is asserted.
