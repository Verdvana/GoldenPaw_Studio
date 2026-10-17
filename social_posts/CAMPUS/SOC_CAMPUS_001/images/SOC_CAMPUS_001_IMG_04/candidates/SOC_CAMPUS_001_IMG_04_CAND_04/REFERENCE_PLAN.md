# Social Post Reference Plan — SOC_CAMPUS_001_IMG_04_CAND_04

- post_id: `SOC_CAMPUS_001`
- image_asset_id: `SOC_CAMPUS_001_IMG_04`
- candidate_id: `SOC_CAMPUS_001_IMG_04_CAND_04`
- asset_level: `L3`
- status: `READY_FOR_USER_AUTHORIZED_REVISION_CANDIDATE`
- reference_count: `3`
- budget_limit: `8`
- selected_reference_set_ids: `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `HOS_30D_BLACK_MATTE_OVERALL`

| Priority | Reference ID/path | Level/status/version | Use | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|---|
| 1 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | Approved deterministic L0-derived face-excluded derivative | generation_input | Neck-down body and leg proportions only | Face, skin identity, hair, clothing design, hosiery, pose, light or background | Keeps visible limbs/feet within approved proportions
| 2 | `L0_HOS_30_BM_003` — `materials/hosiery/source_library/raw/30d_black_matte/IMG_2557.JPG`, SHA-256 `302c10d81dc753490029aa392b45664c21d09eb6f7aa2e81f09a355f91a150bd` | L0 material source | generation_input | Charcoal-black matte full-leg hosiery hue/texture | Person, identity, body, skin, pose, outfit, dorm/background | Full-leg textile appearance
| 3 | `L0_HOS_30_BM_005` — `materials/hosiery/source_library/raw/30d_black_matte/IMG_2559.JPG`, SHA-256 `6c5ad8b48eec9ca82a8ea6c82ca11369dab3fadc9590f93ec7f6ba3dd6690180` | L0 material source | generation_input | Closed-toe hosiery coverage and fabric response over foot/toes | Person, identity, body/foot geometry, nails, pose, outfit or background | The user's no-shoes request leaves hosiery-covered feet visible

## Face-safe declaration

- face visible: `no`
- applicable source-derived Face method: `not applicable; head/face excluded from frame`
- L0 or deterministic L0-derived face inputs: `none`
- approved AI Face Canon QA comparison only: `none; face is out of frame`
- face-excluded body derivative and checksum: listed above; neck-down proportions only

## Conflict resolution

Scoped responsibility prevails. IMG_01–03 approved L3 photos are not generation inputs. They inform only the text description of the approved wardrobe continuity; they do not define identity/body/material/pose.

## Excluded references

All generated images and AI Face/Body Canons are excluded as inputs. No face, hair, or non-clothing identity content is in frame. Bedroom/bunk, bedding, fried chicken, clothing, lamp and phone-camera viewpoint are L2 text-only design.

- CAND_01 was internally rejected for pose/food packaging; CAND_02 was output-blocked; CAND_03 had no visible cutlet inside the inner paper bag. None is a generation input or reference. This candidate is built independently from scoped master assets and text design.
