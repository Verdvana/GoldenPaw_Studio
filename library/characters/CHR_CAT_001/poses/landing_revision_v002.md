# 落地姿态修订 v002

日期：2026-09-04。使用内置 imagegen，参考编辑；未使用 CLI、未生成视频。

## 结果

[落地压缩候选 v002](candidates/CHR_CAT_001_POSE_LAND_LEFT_v002.png)

状态：STATIC_CANDIDATE / USER_REVIEW_PENDING，不新增 approved 白名单。

- 前肢弯曲、胸部降低，相比 v001 的直腿支撑更有压缩感；后腿向腹下收折，后爪仍略离地。
- 保留左向侧面、金色短绒毛、厚躯干和粗尾；无设备与服装。
- 腹部离地较低，近远侧前肢有遮挡，不能视为精确关节结构或真实落地受力验证通过。
- 此图仅为落地压缩瞬间，不是与已有起跳图匹配的连续帧。实际运动、重心轨迹、缓冲与恢复站姿需要视频测试。
- v001 保留历史，v002 为当前待审核版本。

## 实际输入与提示词

原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-2772c6ab-e0c4-4780-9996-808d9fadc126.png`

输入顺序：

- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/candidates/CHR_CAT_001_POSE_LAND_LEFT_v001.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_TURN_LEFT_PROFILE_STANDING_v001.png`

```text
Use case: identity-preserve
Image 1 is the landing pose edit target. Image 2 is the same cat's authoritative compact body and short limb proportions, not the requested standing pose.
Correct image 1 into a believable low-jump landing COMPRESSION phase, facing left in full side profile. Both front paws planted on the floor with slightly staggered contact, elbows clearly flexed and tucked alongside ribcage rather than rigid straight struts; shoulders and chest descend closer to ground, paws beneath/slightly ahead of shoulders, not stretched far forward. Forelimb chains must remain anatomically coherent, soft bent wrists not collapsed or reversed. Hindquarters still a little higher than shoulders, rear legs folding forward beneath hips and hind paws just above ground about to land, not dangling vertically. Keep belly clear of ground, no crash. Preserve compact heavy adult golden British Shorthair body volume, short sturdy limbs, same broad cheeks and side-profile face, gray-green eye, pink nose, cream muzzle/chest, golden-apricot plush fur and thick brown-gold tail tip. Tail extends rearward for balance. Do not slim or lengthen the torso. Exactly four limbs with natural occlusion, no duplicated paws, no human features. Neutral gray studio and soft light, crisp photorealistic full-body landscape with generous margins and coherent contact shadows, no motion blur, no text, no props. Single static pose, not a multi-frame action sequence.
```

