# Scoped L1 Approval — Owner Left Three-Quarter Neutral Face

- approval_id: APPROVAL_OWNER_FACE_02_LEFT_3Q_NEUTRAL_001
- asset_id: OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001
- asset_path: `../OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg`
- source_candidate: FACE_02_LEFT_3Q_NEUTRAL_v004
- approved_level: L1 component
- decision: APPROVED
- approver: user
- decision_date: 2026-09-10
- lock_status: UNLOCKED_COMPONENT
- source_candidate_png_checksum: `34f1a633d37434c8bb17ba28259ff76fa0ba495abb02816979d6b2b6e8a265c3`
- current_jpg_checksum: `3f50c08e2993aa8dd406abd093d24f8a581b6e1475aa4dd57bda3884fed3b745`

The user later transcoded the promoted PNG to JPG for transfer efficiency. The asset ID and scoped approval remain unchanged; the JPG path and checksum above identify the single physical Master, while the former candidate PNG path/checksum remain textual provenance.

## Approval evidence

The user stated: “很好，定确认为canon,同样记得帮我把生成该资产的详细说明啥的加入相应文件，最大限度保证下次生成这个角度的女主的脸的稳定性”.

## Approved authoritative scope

- owner left-three-quarter neutral face identity and facial-feature relationships;
- anatomical left facial plane principally visible, with the face pointing image-left;
- approved orbital depth, nose projection, near/far eye relationship, cheek-to-jaw depth and visible-ear placement for this view;
- softly restrained cheekbone contour, soft rounded chin termination and gentle neutral gaze;
- neutral closed-mouth expression and neutral-studio skin-tone appearance;
- visually eye-level left-three-quarter head projection;
- Hairstyle A presentation within this Face asset.

## Explicit exclusions / must not define

- body geometry;
- final outfit design;
- Hairstyle A side/back Canon or Hairstyle B;
- episode lighting, background or color grade;
- makeup policy;
- incidental skin marks, stray hairs or AI artifacts.

## QA evidence

- exact 3:4 image, 1086×1448;
- SHA-256 verified before promotion;
- user accepted the v004 facial identity and the appended cheekbone, chin and gaze refinements;
- v004 used the complete v001 prompt structure plus only the three approved refinements;
- no FACE_02 candidate was supplied as an image input.

## Promotion action

At initial promotion, the candidate became the approved Master. The user later transcoded it to JPG as recorded above and the candidate raster was removed under the single-file rule. Candidate records remain provenance. The full `owner_v1.0` release remains unlocked until all required components are approved and the user explicitly locks the release.
