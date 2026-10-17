# Social Post Reference Plan — SOC_CAMPUS_001_IMG_04_CAND_10

- post_id: `SOC_CAMPUS_001`
- image_asset_id: `SOC_CAMPUS_001_IMG_04`
- candidate_id: `SOC_CAMPUS_001_IMG_04_CAND_10`
- asset_level: `L3`
- status: `READY_FOR_USER_AUTHORIZED_REVISION_CANDIDATE`
- reference_count: `4`
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

All generated images are excluded from appearance and identity generation duties. The one failed prior candidate listed above is continuity-only and cannot define body, skin, material, clothing, or toe appearance. AI Face/Body Canons are excluded. No face or hair content is in frame.

- CAND_01 was internally rejected for pose/food packaging; CAND_02 was output-blocked; CAND_03 lacked visible cutlet; CAND_04 and CAND_05 were rejected for angle/framing; CAND_06, CAND_07, and CAND_09 were rejected for inadequate hosiery toe rendering; CAND_08 was blocked by moderation. CAND_09 is continuity-only for this edit and defines no appearance/material. All generated images are excluded as inputs and references. This candidate is built independently from the scoped body/material masters and text design.

| 4 | `SOC_CAMPUS_001_IMG_04_CAND_09` (candidate image) | L3 failed candidate, not approved | continuity_only | Camera composition, pose, leg crossing, bag placement and dorm layout only | Face, body identity/proportions, skin, hosiery/material, clothing details, toe appearance, lighting | Preserve layout during localized fabric correction only |
