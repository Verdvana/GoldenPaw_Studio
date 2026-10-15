# Social Post Reference Plan — SOC_CAMPUS_001_IMG_01

- post_id: `SOC_CAMPUS_001`
- image_asset_id: `SOC_CAMPUS_001_IMG_01`
- candidate_id: `SOC_CAMPUS_001_IMG_01_CAND_01`
- status: `READY_FOR_ONE_CANDIDATE`
- reference_count: `4`
- budget_limit: `8`
- budget_exception: `none`
- selected_reference_set_ids: [`OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `HOS_30D_BLACK_MATTE_OVERALL`]

| Priority | Reference ID/path | Level/status/version | `generation_input` or `qa_comparison_only` | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|---|
| 1 | `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` (SHA-256 `1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91`) | deterministic L0 derivative, v1 | `generation_input` | Owner face identity and facial-feature geometry, adult identity only | Hair, bangs, makeup, jewelry, source retouch/color, camera angle, body, outfit, hosiery, lighting or background | Source-derived identity authority; matches the three-quarter face turned toward image-left |
| 2 | `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png` (SHA-256 `89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12a6b79182026bd788`) | deterministic L0 derivative, v1 | `generation_input` | Natural warm-neutral skin color/texture context only | Fine geometry, identity, hair, bangs, makeup, camera, body, outfit, lighting or background | Complements the geometry-only source crop without adding an AI face input |
| 3 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` (SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`) | deterministic approved-Body derivative, v1 | `generation_input` | Neck-below body scale, proportions, waist/hip relationship, leg axes and foot scale | Face, identity, skin pigmentation, hair/bangs, outfit design, hosiery material, camera rendering, lighting or background | Required face-excluded body authority for a full-body frame |
| 4 | `L0_HOS_30_BM_003` — `materials/hosiery/source_library/raw/30d_black_matte/IMG_2557.JPG` (SHA-256 `302c10d81dc753490029aa392b45664c21d09eb6f7aa2e81f09a355f91a150bd`) | L0 material source, 30D black matte, full-leg | `generation_input` | Black color family, matte surface response, continuous leg-to-foot hosiery coverage only | Denier/opacity (target is text-defined 20D), person/body/pose, garment design, shoe choice, brand/text/watermark, lighting or background | Closest registered black-matte material reference; target 20D semisheer is specified separately in text |

## Face-safe declaration

- face visible: yes — three-quarter view, nose toward image-left, gaze at an off-camera companion
- applicable source-derived Face method: `characters/CHR_HUMAN_001_OWNER/canon/face/FACE_01_FRONT_NEUTRAL_METHOD.md` prompt constraints, as routed by `characters/CHR_HUMAN_001_OWNER/source/identity/REFERENCE_GUIDE.md`; L0-derived sources remain the only face-generation authority
- L0 or deterministic L0-derived face inputs: `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` for face geometry/identity; `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` for natural skin context only
- approved AI Face Canon QA comparison only: `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001`; QA only, never generation input
- face-excluded body derivative and checksum: `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1`, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`

## Scoped design by text only

- Hairstyle: user-authorized L2-only long dark-brown hair with straight blunt bangs and natural loose lengths. No hair image input; A/B Canons do not define this hairstyle. Do not blend A/B. The approved post-specific exception is recorded in `OWNER_L1_GENERATION_SPEC.md` draft_1.234.
- Outfit and environment: text-defined from this post's L2 brief; no image input.
- Hosiery denier and opacity: text-defined as charcoal-black 20D matte semisheer; the 30D L0 source above is expressly excluded from defining denier/opacity.

## Conflict resolution

Scoped asset responsibility wins. A prior social image may not define identity, face, body, hair, fixed props or hosiery. The 2018 look is conveyed through scene, wardrobe and phone-camera rendering; do not de-age the face.

## Excluded references

- Any AI Face/Body Canon as a generation input: excluded by the global face-safe rule.
- Any hairstyle-A/B image as a generation input: excluded because this post uses a user-specified distinct L2 hairstyle.
- Nude/gray hosiery Canons and black high-gloss references: excluded because their color/finish do not match the target.
- The original full L0 15.jpg: excluded; use only the named deterministic face-geometry derivative.
- Reference image 30D black-matte marketing text and photographed pose/person: explicitly excluded; only the scoped textile responsibility is used.
