# HAIR_B_01_FRONT_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
spec_revision: draft_1.169
identity_md_revision: draft_0.157
asset_id: HAIR_B_01_FRONT
candidate_id: HAIR_B_01_FRONT_v001
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: REJECTED
aspect_ratio: "3:4"
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
previous_ai_candidate_chain: false
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_01_FRONT_v001/HAIR_B_01_FRONT_v001.png"
checksum_sha256: "caef1073d6d1d843435d32761ea0c35318c176086a720d21fc44e35bff5dd707"
qa_status: USER_REJECTED_EXCESS_CROWN_HEIGHT
```

## Reference responsibilities

- Approved front Face (`4d657954...90fc4`): identity, skin and neutral expression only; excludes hair and camera.
- Real B L0 `8.jpg` (`73445832...8c17`): real hairline, pulled-back front, natural side wisps, gathered-updo direction and front volume only; excludes identity, surprise, hands, sweater, warm light and background.
- Approved B appearance (`e83de808...13f`): final center part, smooth low updo/bun, controlled crown, face-framing strands, dark brown and restrained highlights only; excludes its face, high camera, looking-up pose, body, top, light and background.
- No Hair-A or other generated Hair candidate is supplied. The approved B design is never used alone; L0 remains the real-hair anchor.

## Candidate authority

Standard eye-level frontal Hairstyle-B hairline, center part, pulled-back front, controlled crown, symmetrical face-side wisps and visible low-bun side hints only. No authority for face, body, outfit, other B views, lighting, background or full release.

## QA status

Attempt 1 generated a 1086x1448 exact-3:4 RGB PNG from the three scoped references. Technical precheck passes standard eye-level front/neutral head, centered part, smooth pulled-back front, controlled crown, natural face-side wisps, neutral studio and pink Calibration Outfit. Output SHA-256: `caef1073d6d1d843435d32761ea0c35318c176086a720d21fc44e35bff5dd707`. Candidate remains `REVIEW_REQUIRED`.

User review: face is acceptable, but the hairline-to-top silhouette height is excessive for a standard eye-level view and reads no lower than the existing high-camera B asset. v001 is `USER_REJECTED` and prohibited from v002.
