# Reference Plan — SOC_OUTFIT_003_IMG_02

- post_id: `SOC_OUTFIT_003`
- image_asset_id: `SOC_OUTFIT_003_IMG_02`
- candidate_id: `SOC_OUTFIT_003_IMG_02_CAND_01`
- status: READY_FOR_ONE_CANDIDATE
- reference_count: 4 (including edit target)
- budget_limit: 8
- selected_reference_set_ids: `OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_BODY_FRONT_CURRENT_FACE_EXCLUDED_DERIVATIVE`, `OWNER_HAIR_A_FRONT_CANON_L1`

| Priority | Reference ID/path | Level/status/version | Use | Responsibility | Must not define |
|---:|---|---|---|---|---|
| 1 | `L0_OWNER_SOC_OUTFIT_003_SOURCE_IMG_9106` — `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_003/source_inputs/IMG_9106.HEIC` — SHA-256 `d155486d1be5582ab3747f631375c14bba49a269a86af506624ae2c7ba5852f1` | Immutable L0 user photo | generation input / edit target | Exact pose, crop, perspective, store, lighting, garments, shoes, visible hosiery, natural skin appearance in this shot | Owner face geometry, canon body proportions, hairstyle design |
| 2 | `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png` — SHA-256 `1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91` | Deterministic L0-derived crop | generation input | Face identity and feature geometry only; source-derived face authority | Source hair, skin retouch, lighting, clothing, body, background |
| 3 | `OWNER_BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` — SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | Deterministic face-excluded body derivative | generation input | Front-facing neck-below body proportions and leg/foot scale only | Face, identity, hair, clothes, hosiery material, lighting, background |
| 4 | `OWNER_HAIR_A_01_FRONT_CANON_001` — `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png` — SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219` | Approved scoped L1 Hairstyle A | generation input | Hairline, near-center part and long straight dark-brown front construction only | Face, skin, body, garment, lighting, background |

## Scope and face-safe declaration

- Face visible: only lower face/chin is partly visible at the top edge; retain the exact original crop. Use `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` source-derived constraints and L0 geometry crop. Source photo supplies only the natural skin appearance under its own lighting.
- Approved AI Face Canon `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` at `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg` (SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`) is comparison-only after generation.
- Body input is face-excluded, and defines only neck-below proportions. No AI Face/Body Canon or generated candidate is a generation input.
- The source image is the sole authority for the tan sheer pantyhose, their conspicuous appearance and continuous leg-to-foot coverage; no material reference is needed.
- Excluded: other post photos and generated candidates; materials library; any scene, outfit, shoe or hosiery redesign inputs.
- This image is built independently from its own L0 source. It does not take identity or appearance from IMG_01.
