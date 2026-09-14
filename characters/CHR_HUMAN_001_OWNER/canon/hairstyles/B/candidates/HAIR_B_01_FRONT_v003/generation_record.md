# HAIR_B_01_FRONT_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
spec_revision: draft_1.175
identity_md_revision: draft_0.163
asset_id: HAIR_B_01_FRONT
candidate_id: HAIR_B_01_FRONT_v003
gate: "Gate 4 — Hairstyle Canon"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
rejected_candidate_pixels_used: false
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/approved/HAIR_B_01_FRONT/OWNER_HAIR_B_01_FRONT_CANON_001.png"
checksum_sha256: "3692b4e2fd6da2607fd103b14d43d28afbbf66696861171b2ff5632dd3b07c35"
qa_status: PASS_USER_APPROVED
```

## Coupled correction contract

- Independently reconstruct from the same three scoped references; v001/v002 are excluded.
- Make the nose moderately shorter and narrower while retaining natural identity; move nasal base upward.
- Move philtrum, lips and chin upward together by a matching amount, shortening the complete nose-to-chin region without elongating the philtrum or distorting mouth/chin proportions.
- Reduce hairline-to-top silhouette height another 10–15% versus v002's written result, without cropping, raising the hairline or flattening the skull.
- Facial result is review context only; Hair authority remains limited to Hairstyle B.

## QA status

Attempt 1 generated a 1086x1448 exact-3:4 PNG. Technical precheck confirms a shorter/narrower natural nose, coherent upward compaction of philtrum/lips/chin, and further reduced crown silhouette without flattening or cropping. Standard eye-level Hairstyle-B structure remains intact. SHA-256: `3692b4e2fd6da2607fd103b14d43d28afbbf66696861171b2ff5632dd3b07c35`. Candidate remains `REVIEW_REQUIRED`; face changes have contextual authority only.

User approved with “批准，下一项”. The sole raster was moved as `OWNER_HAIR_B_01_FRONT_CANON_001`; facial context does not redefine Face Canon.
