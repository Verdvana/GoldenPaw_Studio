# Generation Record — SOC_COMMUTE_001_IMG_03_CAND_09

- asset_id: SOC_COMMUTE_001_IMG_03
- candidate_id: SOC_COMMUTE_001_IMG_03_CAND_09
- asset_level: L3
- status: USER_APPROVED_L3
- generation_date: 2026-09-18
- generation_gate: User instruction “中间过道太宽了，缩短一半，别的完美，再来一版”.
- original_candidate_path: `social_posts/COMMUTE/SOC_COMMUTE_001/images/SOC_COMMUTE_001_IMG_03/candidates/SOC_COMMUTE_001_IMG_03_CAND_09/SOC_COMMUTE_001_IMG_03_CAND_09.png`
- current_approved_path: `social_posts/COMMUTE/SOC_COMMUTE_001/images/SOC_COMMUTE_001_IMG_03/approved/SOC_COMMUTE_001_IMG_03_APPROVED_v2.png`
- output_sha256: `cd3769237f564e791043357f2cbff6b49ce7548658be823e28855b4293e0484b`
- settings: ImageGen, 4:5 vertical social still; seed unavailable

## Generation inputs

| Asset / path | Responsibility | Must not define |
|---|---|---|
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png` | Same seated thigh-to-knee geometry and raised camera-to-lap proportion | Face, skin, hair, clothing, metro |
| `OWNER_WORK_SUMMER_01_WORN_FULL_BODY` — `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/approved/worn_full_body/OWNER_WORK_SUMMER_01_WORN_FULL_BODY.png` | Same warm-champagne white black-dot skirt, smoke-gray 15D matte pantyhose and taupe pumps | Face, skin, body identity, hair, metro |

## Excluded

- Face, hair and upper body are out of frame and not generation inputs.
- All prior social images/candidates are excluded; reuse only the master asset responsibilities and user-approved text constraints.

## Prompt assembly

Use case: photorealistic-natural. Asset type: 4:5 social-feed carousel photograph. Create the same seated commuter point-of-view inside a standard narrow metro carriage at early night: chest-height downward camera, lower edge of a warm champagne-white black-dot skirt, smoke-gray 15D matte pantyhose through both knees, no face/hair/upper body, and a continuous opposite horizontal bench with seated passengers facing the camera below face level.

Critical geometry correction: the transverse cross-aisle between the viewer's seat row and the opposite bench is only half the width shown in a typical spacious rendition—very compact and crowded, with the opposite bench visibly much closer to the viewer. There must be no large open floor. The few standing summer commuters occupy this compressed cross-aisle at irregular angles and unequal spacing: side-on, turned away and diagonally shifted, with varied bags and footwear. Preserve the correct continuous bench, transverse layout, narrow-carriage boundaries, non-identifiable passengers, cool-neutral light, no windows/reflections/text/logo/UI/watermark, and coherent anatomy. Avoid an orderly lineup, repeated stances, duplicate legs, malformed feet, impossible seating or fashion-editorial styling.

## QA targets

- Opposite connected bench and all prior successful geometry retained.
- Cross-aisle is visibly about half the width of CAND_08: packed, close, and without broad exposed floor.
- Random lower-body orientations in the compact aisle.
- Candidate remains L3 only and never a downstream visual input.

## Approval record

- approved_by: user
- approval_date: 2026-09-18
- approval_evidence: “完美 批准”
- promotion: moved (not copied) to the approved L3 post-image path as v2; v1 remains preserved.
- scope: approved only for this social post; not Canon and not a visual generation input.
