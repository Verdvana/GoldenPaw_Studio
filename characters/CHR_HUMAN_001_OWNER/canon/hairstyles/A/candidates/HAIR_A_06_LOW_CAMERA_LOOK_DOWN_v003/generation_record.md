# HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.168
identity_md_revision: draft_0.156
asset_id: HAIR_A_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v003
gate: "Gate 4 — Hairstyle Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE]
reference_count: 2
previous_ai_hairstyle_a_candidate_count: 0
rejected_candidate_pixels_used: false
measurement_only_asset_not_supplied: OWNER_HAIR_A_01_FRONT_CANON_001
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_06_LOW_CAMERA_LOOK_DOWN/OWNER_HAIR_A_06_LOW_CAMERA_LOOK_DOWN_CANON_001.png"
checksum_sha256: "2a1c53cd28c397b3a019ced39a4dc55aebe9c8ab7881518cb4516dc2ef341ded"
qa_status: PASS_USER_APPROVED
```

## Scoped correction

- Preserve approved soft/flatter face identity from `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`.
- Hair A comes only from the masked L0 derivative.
- Low-camera view shows no crown/scalp line; the hidden-part-derived frontal root-flow apex must sit slightly image-left of center at approximately 47–48% of image width.
- v001/v002 and approved Hair-A pixels are not supplied.

## QA status

Attempt 1 generated a 1086x1448 exact-3:4 PNG. Technical precheck passes: frontal root-flow apex lies slightly image-left of center; no crown plane or long scalp part appears; low-camera projection, soft facial relief, complete straight panels and all tapered ends remain readable. Output SHA-256: `2a1c53cd28c397b3a019ced39a4dc55aebe9c8ab7881518cb4516dc2ef341ded`. Candidate remains `REVIEW_REQUIRED`.

User approved with “批准，下一项”. The sole raster was moved to `approved/HAIR_A_06_LOW_CAMERA_LOOK_DOWN/OWNER_HAIR_A_06_LOW_CAMERA_LOOK_DOWN_CANON_001.png`; full release remains unlocked.
