# VP 参考组合 v001

用户确认更新（2026-09-04）：正面佩戴 v001、桌面观察 v001、单爪轻触 v001 三张得到“可以 下一步”的确认，标记 USER_APPROVED_STATIC。覆盖下方“等待用户确认”状态，文件保持原位置，原大面罩比例与四图基准不变；动态和精确三维一致性未验证。

新增正面佩戴、桌面观察、单爪轻触三张 v001 静态候选，等待用户确认；原四图参考与大面罩尺度来源保持不变。路径、审核和实际提示词见 [互动批次](../../characters/CHR_CAT_001/poses/visionpro_interaction_batch_v001.md)。

状态：CURRENT_STATIC_REFERENCE_SET（当前静态参考组合，非三维/运动验证通过）。本文件是 VP 当前版本入口，优先于历史批次记录；不要按文件编号自动选最大版本。

## 当前四张参考

| 作用 | 文件（相对工程根目录） | 使用边界 |
|---|---|---|
| 用户选定的大面罩比例 | `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v001.png` | 决定面罩与猫脸大小，不反向替代裸脸身份母版 |
| 侧臂与后脑绕带路线 | `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_LEFT_PROFILE_v004.png` | 侧偏视角，不称为严格 90 度正交图 |
| 后带包覆范围 | `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_REAR_v003.png` | 本轮更新；针织覆盖后脑主要可见弧段，侧臂在两侧收尾 |
| 独立设备外观 | `library/equipment/EQP_VISIONPRO_CAT_001/candidates/EQP_VISIONPRO_CAT_001_DESIGN_3Q_v004.png` | 本轮更新；浅色侧臂接连续针织后带，无旧圆形调节盘；不单独决定猫/设备大小 |

## 固定结构规则

- 大面罩比例使用佩戴三分之四 v001，禁止回缩为佩戴 v002 的矮面罩。
- 黑色曲面玻璃、银色边框、深灰面垫；浅灰侧臂位于耳根以下，前部低矮椭圆连接部。
- 浅色侧臂在两侧连接灰色竖向罗纹针织后带，针织带连续绕后脑，不在头侧形成无连接的短贴片。
- 后脑无长段浅色臂横贯，不加后置大圆调节盘；无跨头顶带，无外挂电池与线缆。
- 双耳和口鼻保持露出；有遮挡时不凭空添加第二层绑带或让绑带穿过耳朵。

## 如何输入参考

1. 猫咪身份仍从角色 approved 身份母版选取。
2. 佩戴镜头增加上述大面罩比例图；再根据目标视角加侧面或后面一张，不将全部历史图同时输入。
3. 设备单独出镜以独立 v004 为外观输入；涉及猫同框仍需佩戴比例图。
4. 当前支持静态镜头草图与后续测试。像素级吻合、精确三维尺寸、头显移动时稳定性以及真实动物佩戴安全性均未验证。

## 本轮视觉检查

- 后面 v003：针织带不再仅占后脑中央小块，向两侧连续延伸，双耳未被覆盖，无电池/线缆。
- 独立 v004：侧臂材质和前部椭圆连接部更接近侧面 v004；移除旧后侧圆盘，后带形成完整 U 形弧段。
- 两图的大结构关系可用于当前参考组合。细小接缝、罗纹密度、面垫厚度以及主图/侧图的透视差异仍不能视为完全一致；特写镜头需逐镜审核。
- 选择四张作为工作参考不新增猫咪 approved 身份/动作资产，也不表示所有候选已获得用户逐张批准。

## 停用参考

- 小面罩佩戴三分之四 v002。
- 侧面 v001/v002（后带截断）；未采用的全针织侧臂尝试。
- 后面 v001/v002，独立设备 v001/v002/v003。

停用表示不得作为新镜头输入，文件保留追溯；不删除用户文件。MacBook、女主与双角色资产未改动。

## 本轮实际生成记录

使用内置 imagegen 两次局部编辑，参考图已查看；没有 CLI、未提供模型版本或随机种子。

原始输出：
- `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-217bb0c8-09e7-44be-8406-9cae16e550c1.png` → 后面 v003
- `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-1aeaf6cc-4885-4c4f-ab10-00bbd4a4fc6d.png` → 独立 v004

### REAR_v003

1. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_REAR_v002.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_LEFT_PROFILE_v004.png`
3. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v001.png`

```text
Use case: precise-object-edit
Image 1 is the edit target. Image 2 is the authoritative corrected SIDE routing: pale smooth side arm followed by a continuous gray ribbed knit band wrapping around the occiput. Image 3 locks the user-selected large visor proportions. This is one fictional cat-adapted headset, no battery, cable, crown strap or extra hardware.
Change ONLY Image 1's headband assembly to match the routing in Image 2 viewed from behind. The GRAY RIBBED KNIT must extend continuously around the ENTIRE visible rear arc from behind one ear to behind the other, no small central knit patch with long pale sections crossing the back of skull. Pale rigid arms end on the SIDES, just behind ear bases; knit joins there and curves snugly across rear head. Same band height as Image 2, vertical ribs, no free band ends, no floating gaps. Preserve cat head/ear geometry, fur, rear camera angle, studio background and lighting. Both ears free; no rear visor.
```

### DEVICE_v004

1. `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_VISIONPRO_CAT_001/candidates/EQP_VISIONPRO_CAT_001_DESIGN_3Q_v003.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_LEFT_PROFILE_v004.png`
3. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v001.png`

```text
Use case: precise-object-edit
Image 1 is the edit target. Image 2 is the authoritative corrected SIDE routing: pale smooth side arm followed by a continuous gray ribbed knit band wrapping around the occiput. Image 3 locks the user-selected large visor proportions. This is one fictional cat-adapted headset, no battery, cable, crown strap or extra hardware.
Change ONLY Image 1's side-arm and rear-band connections to agree with Image 2. On each side the large visor's low-profile oval attachment joins a smooth pale rigid side arm; behind the ear-position the arm transitions directly to one continuous light-gray ribbed knitted rear band. The rear band wraps in a complete U-shaped rear arc to the opposite arm, never stops as a short patch. Remove the obsolete oversized round adjustment disk at the rear arm/band junction; use a simple flush junction consistent with Image 2. Keep the LARGE visor glass silhouette and size, silver rim, charcoal seal, product position, camera angle, neutral lighting and background unchanged. No cat in product image, no added objects, text or watermark.
```
