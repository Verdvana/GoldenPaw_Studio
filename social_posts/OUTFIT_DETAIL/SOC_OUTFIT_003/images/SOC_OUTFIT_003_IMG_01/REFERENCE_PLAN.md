# Social Post Reference Plan

- post_id: `SOC_OUTFIT_003`
- image_asset_id: `SOC_OUTFIT_003_IMG_01`
- candidate_id: `SOC_OUTFIT_003_IMG_01_CAND_01`
- status: READY_FOR_ONE_CANDIDATE
- reference_count: 5
- budget_limit: 8
- budget_exception: none
- selected_reference_set_ids: `OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_BODY_REAR_CURRENT_LOWER_BODY_FACE_HAIR_EXCLUDED_DERIVATIVE`, `OWNER_HAIR_A_FRONT_CANON_L1`, `OWNER_HAIR_A_BACK_CANON_L1`

| Priority | Reference ID/path | Level/status/version | `generation_input` or `qa_comparison_only` | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|---|
| 1 | `L0_OWNER_SOC_OUTFIT_003_SOURCE_IMG_9103` — `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_003/source_inputs/IMG_9103.HEIC` — SHA-256 `c9d45c33c38c8c334384d127120c34aafd055206dd95e72a3df0e52b34964ee6` | L0 immutable user photo | generation_input / edit target | exact pose/action, camera framing, mirror geometry, shoe-store scene, existing lighting, sweater, skirt, visible hosiery, shoes and natural skin appearance in this shot | approved owner face geometry, body proportions, hairstyle design | Sole edit target; user requires the original photo's scene and styling to remain |
| 2 | `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` — SHA-256 `1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91` | L0-derived / approved deterministic crop | generation_input | face identity and facial feature geometry only | source hair, makeup, skin texture/retouch, lighting, clothing, body, background | Sole face geometry authority under the applicable source-derived Face method |
| 3 | `OWNER_BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1/BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_CROP.png` — SHA-256 `c3ce9451c3c328181a715f9efb4475f8ac69bf17259c51c2c9f513822944b10e` | deterministic face/hair-excluded derivative / approved derivative | generation_input | rear hip, thigh, calf, ankle and heel proportions only | face, skin identity, hair, upper body, clothing, hosiery material/color/denier, lighting, background, camera | View-matched lower-body shape reference; target source retains the actual bend and foot placement |
| 4 | `OWNER_HAIR_A_01_FRONT_CANON_001` — `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png` — SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219` | approved L1 / Hairstyle A front | generation_input | front hairline, near-center part and front-panel construction visible in mirror | face, skin, expression, body, clothing, other views, lighting, background | Needed for the reflected front view |
| 5 | `OWNER_HAIR_A_04_BACK_CANON_001` — `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_04_BACK/OWNER_HAIR_A_04_BACK_CANON_001.png` — SHA-256 `91128987bc4aade21f7b7fd3a7b9bd24d2ca3d0100847214844b702741852e53` | approved L1 / Hairstyle A rear | generation_input | rear crown, long straight loose hair mass and natural fall in the main view | face, skin, body, clothing, other views, lighting, background | Needed for the dominant rear view |

## Face-safe declaration

- face visible: yes, only in the mirror reflection
- applicable source-derived Face method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` prompt constraints; target reflection keeps its original downward gaze and head orientation
- L0 or deterministic L0-derived face inputs: `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` for identity/geometry; the original L0 edit target supplies only the natural skin appearance under this shot's actual lighting
- approved AI Face Canon QA comparison only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` at `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg` (not a generation input)
- face-excluded body derivative and checksum: `OWNER_BODY_06_BACK_V006_LOWER_BODY_FACE_HAIR_EXCLUDED_v1`, `c3ce9451c3c328181a715f9efb4475f8ac69bf17259c51c2c9f513822944b10e`

## Conflict resolution

Attribute-scoped references control only their declared scope. The source photo controls the actual scene, pose, lighting, garments, hosiery, shoe placement and the face's natural skin appearance in this lighting; the approved L0-derived Face crop controls facial identity/geometry; the body derivative controls rear lower-body proportions; the two Hairstyle A views control hair only. Preserve the user's original downward gaze, reflection perspective and all non-person scene pixels as closely as possible.

## Excluded references

- All other photos in this post's `source_inputs/`: not needed for this first candidate; they cannot define continuity or assets for this image.
- Approved AI Face/Body Canons and any generated image: forbidden as generation inputs; Face Canon is comparison-only after generation.
- Hosiery material library references: unnecessary because the user photo itself defines the existing hosiery appearance, which must remain unchanged.
- Outfit, environment, shoe or other post images: unnecessary; the edit target already supplies these responsibilities.
