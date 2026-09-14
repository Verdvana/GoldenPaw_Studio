# HAIR_B_02_3Q_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
spec_revision: draft_1.176
identity_md_revision: draft_0.164
asset_id: HAIR_B_02_3Q
candidate_id: HAIR_B_02_3Q_v001
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: REJECTED
aspect_ratio: "3:4"
view: {anatomical_side: left, face_points: image_left, projection: three_quarter}
reference_set_ids: [OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
previous_generated_hair_inputs: []
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_02_3Q_v001/HAIR_B_02_3Q_v001.png"
checksum_sha256: "7916aa48d385d8fcce415964d9a81466dac2498a186b9a7125330edbde18a051"
qa_status: USER_REJECTED_REAR_STRUCTURE
```

## Reference roles

- approved left-3/4 Face (`3f50c08e...b745`): identity/view/skin/neutral expression only; hair excluded.
- real B L0 (`73445832...8c17`): real hairline, rearward gathering, wisps and updo direction only; face/expression/clothes/light/background excluded.
- approved B appearance (`e83de808...13f`): final center part, smooth low bun, controlled crown, strands, dark brown/highlights only; face/high-camera/clothes/light/background excluded.
- No B01 or other generated Hair pixels.

## QA status

Attempt 1 generated a 1086x1448 exact-3:4 PNG. Technical precheck passes anatomical-left eye-level 3/4, near/far hairline projection, compact crown, near-ear/wisp relation, smooth rearward gathering and a clearly located partially visible low centered bun. SHA-256: `7916aa48d385d8fcce415964d9a81466dac2498a186b9a7125330edbde18a051`. Candidate remains `REVIEW_REQUIRED`.

User corrected the rear design: it must be secured by a claw clip with a small upward/backward rooster-tail tuft, not a low bun. v001 is rejected and prohibited from v002.
