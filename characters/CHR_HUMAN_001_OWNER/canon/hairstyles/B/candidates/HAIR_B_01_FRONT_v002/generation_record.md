# HAIR_B_01_FRONT_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
spec_revision: draft_1.171
identity_md_revision: draft_0.159
asset_id: HAIR_B_01_FRONT
candidate_id: HAIR_B_01_FRONT_v002
gate: "Gate 4 — Hairstyle Canon"
status: USER_REJECTED
approval_status: REJECTED
aspect_ratio: "3:4"
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
rejected_candidate_pixels_used: false
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_01_FRONT_v002/HAIR_B_01_FRONT_v002.png"
checksum_sha256: "08b1bc7b57faafb1df11da41f51e3cdd627d0d7fd23808f59e6db48dcf9c51fa"
qa_status: USER_REJECTED_FACE_AND_CROWN_REFINEMENT
```

## Correction contract

- Preserve the approved face identity and the accepted B design from the same three scoped references; v001 is not supplied.
- Strict eye-level neutral head. Reduce apparent hairline-to-top silhouette height by about 20–25% relative to v001's written measurement; show less top/crown than the existing high-camera B design anchor.
- Retain a realistic cranial contour and low-to-moderate volume; do not flatten hair against the skull.

## QA status

Attempt 1 generated a 1086x1448 exact-3:4 PNG. The hairline-to-top silhouette height is visibly reduced while natural cranial curvature and low-to-moderate root volume remain; standard eye-level identity context and Hairstyle-B center-part/pulled-back/wisp structure pass technical precheck. SHA-256: `08b1bc7b57faafb1df11da41f51e3cdd627d0d7fd23808f59e6db48dcf9c51fa`. Candidate remains `REVIEW_REQUIRED`.

User requested further refinement: shorter and narrower nose, move philtrum/lips/chin upward together, and reduce crown height again. v002 is rejected and prohibited from v003.
