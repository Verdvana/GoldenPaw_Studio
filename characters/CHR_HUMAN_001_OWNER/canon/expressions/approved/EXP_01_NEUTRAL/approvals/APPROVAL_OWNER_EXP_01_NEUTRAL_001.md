# Canon Approval Record

- approval_id: `APPROVAL_OWNER_EXP_01_NEUTRAL_001`
- asset_id: `OWNER_EXP_01_NEUTRAL_CANON_001`
- asset_path: `../OWNER_EXP_01_NEUTRAL_CANON_001.jpg`
- approved_level: `L1 component`
- decision: `APPROVED`
- approver: `user`
- decision_date: `2026-09-12`
- lock_status: `UNLOCKED_COMPONENT`
- source_candidate: `none; user supplied directly`
- current_checksum: `20baf37d87dcce168ff7ab43288613043538c8cbe983f21e9b2e520168ce2350`

## Approval evidence

The user stated: “女主待生成的资产中，表情部分的第一项资产我已经放在…/canon/expressions/approved/路径下的一个jpg文件了，请把它作为第一个表情资产登记”.

## Approved authoritative scope

- relaxed neutral brows and eyelids;
- calm direct gaze;
- naturally closed mouth without smile, frown or visible tension;
- the combined transient neutral expression defined by `EXP_01_NEUTRAL`.

## Explicit exclusions

- permanent skull or facial-feature geometry, skin tone, age or identity;
- Hairstyle A or any other hairstyle;
- body geometry or Calibration Outfit design;
- lighting, background or rendering artifacts;
- other Expression components and the complete `owner_v1.0` release.

## QA evidence

- JPEG decodes successfully at 1086×1448 and exact 3:4 aspect ratio;
- standard front, visually eye-level presentation;
- eyebrows and eyelids appear relaxed, gaze is calm and direct, and mouth is naturally closed;
- no smile, frown, surprise, squint or other competing expression action is visible;
- user directly placed the file in the approved directory and explicitly requested registration as the first Expression asset.

## Registration action

- physical operation: `MOVE/RENAME`, never `COPY`;
- original user-placed path/checksum: `characters/CHR_HUMAN_001_OWNER/canon/expressions/approved/exec-97ba0918-3cbf-465b-a171-db2da1f198b9.jpg` / `20baf37d87dcce168ff7ab43288613043538c8cbe983f21e9b2e520168ce2350`;
- current approved path/checksum: `characters/CHR_HUMAN_001_OWNER/canon/expressions/approved/EXP_01_NEUTRAL/OWNER_EXP_01_NEUTRAL_CANON_001.jpg` / `20baf37d87dcce168ff7ab43288613043538c8cbe983f21e9b2e520168ce2350`;
- pixel modification: `none`;
- generation provenance: `not provided by user`.

This approval registers only EXP_01. Thirteen Expression components remain pending, and the full `owner_v1.0` remains unlocked.
