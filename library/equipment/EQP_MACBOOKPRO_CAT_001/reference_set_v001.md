# MacBook 静态参考组合 v001

用户确认更新：用户在双爪 v003 待确认图后回复“ok 继续”，双爪 v003 记为 USER_APPROVED_STATIC。覆盖下方“待用户审核”状态，不代表连续打字或其他角度已通过。

双爪最新候选为 v003：两爪已移至黑色键区，等待用户审核；v002 保留历史。见 [修订记录](../../characters/CHR_CAT_001/poses/macbook_dual_paw_revision_v003.md)。不属于已确认三图，也不表示动态通过。

## 用户确认（2026-09-04）

新增中性工作坐姿 v001 和双爪键盘 v002 候选，见 [生成与审核](../../characters/CHR_CAT_001/poses/macbook_work_batch_v001.md)。双爪接触仍待修正／审核，不纳入已确认组合。

用户明确确认左右侧接口 v001 和操作全景 v004 三张均 OK，标记 USER_APPROVED_STATIC。当前操作参考使用全景 v004；v002 保留历史比例来源。文件暂不搬移，避免引用失效。此确认覆盖下方“v004 尚非用户批准图”等旧审核状态；不等于动态或所有角度像素级一致性已验证。

## 最新覆盖：左右侧与全景接口修订

新增 [左侧](candidates/EQP_MACBOOKPRO_CAT_001_PORTS_LEFT_v001.png)、[右侧](candidates/EQP_MACBOOKPRO_CAT_001_PORTS_RIGHT_v001.png) 与 [全景 v004](../../characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v004.png) 候选。全景 v004 保留双前爪姿态并改善右侧接口，原 v002 继续作为用户确认比例依据。下一步核对独立斜视键盘／接口和接触近景，不重复生成左右侧。细节与完整提示词见 [本轮记录](../macbook_ports_revision_v001.md)。

状态：PORT_LAYOUT_REFERENCED / CROSS_VIEW_QA_PENDING。下方 PORTS_UNRESOLVED 和“下一关”是此前批次状态，不覆盖本段。接口微细节未通过极近特写审核，v004 尚非用户批准图。

状态：PARTIAL / PORTS_UNRESOLVED / CANDIDATES_ONLY。2026-09-04。

此文件优先于设备库历史批次中的版本说明。用户确认的是银色、M4 款、猫用改装及全景 v002 中的猫／电脑视觉比例，不代表批准所有结构细节。

## 选图与用途

| 用途 | 文件 | 状态与限制 |
|---|---|---|
| 猫／电脑比例、姿态 | [全景 v002](../../characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v002.png) | 保留用户确认的比例；接口仍需修正 |
| 键盘布局设计参考 | [俯视 v001](candidates/EQP_MACBOOKPRO_CAT_001_KEYBOARD_TOP_v001.png) | 候选，不是精确产品规格依据 |
| 独立设备外观 | [斜视 v004](candidates/EQP_MACBOOKPRO_CAT_001_DESIGN_OPEN_3Q_v004.png) | 新增键盘修正候选；键帽字符、间距及接口跨角度一致性未通过 |
| 爪部接触研究 | [近景 v002](../../characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_MACBOOK_PAW_CONTACT_v002.png) | 接触区移入触控板、边界余量改善；不是已验证可直接剪接的全景同瞬间特写 |

## 不采用与历史

- [全景 v003](rejected/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v003.png) 未通过：猫咪前爪姿态及支撑关系变化，接口成为重复近似孔形，未解决连续性。禁止替换全景 v002，禁止作为后续生成参考。
- 独立 v003、接触近景 v001 保留历史，不能因 v004/v002 文件更新便推定结构已锁定。
- 本轮未覆盖、删除原资产；两张新候选未加入角色 approved。

## 下一关

1. 核定猫用银色 M4 设备左右侧接口的类型、顺序与相对位置，补无猫的左右侧参考。不得自行将 M4 改为 M4 Pro/Max。
2. 仅修复全景 v002 的设备区域，必须保留猫身份、姿态、支撑爪及已确认比例；改变猫即退回。
3. 再核对键盘各行、触控板比例及接触点，仍有差异则不能作为连续剪接组合。
4. 此后才补双爪键盘静态锚点；静态图不等于连续打字已验证。女主及双角色继续留空。

## 本轮实际生成记录

使用内置 imagegen，模式为有参考图编辑（referenced_image_paths）；未使用 CLI、掩模或后期拼接。以下为实际提交提示词；其中“exact / locked”等为生成目标，不代表输出达成。

### DEVICE_v004

输入（顺序一致）：

- `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_DESIGN_OPEN_3Q_v003.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_KEYBOARD_TOP_v001.png`

原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-7a7ebfd6-10ea-4359-89bb-e1569280ce0f.png`

项目保存：`library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_DESIGN_OPEN_3Q_v004.png`

实际提示词：

```text
Use case: precise-object-edit
Image 1 edit target: silver fictional cat-sized M4 MacBook Pro three-quarter view. Image 2 authoritative keyboard layout reference for this fictional prop.
Replace ONLY the keyboard keys and legends in Image 1 with the exact row layout, key shapes, modifiers, arrow cluster and Touch ID of Image 2, projected into Image 1's perspective. No duplicate keys, keep one long spacebar. Preserve Image 1's complete chassis outline, silver finish, trackpad size/position, speaker grilles, visible ports, black inactive screen, opening angle, camera, lighting and background. No added objects or text. Photorealistic product image.
```

### FULL_v003

输入（顺序一致）：

- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v002.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_DESIGN_OPEN_3Q_v003.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_KEYBOARD_TOP_v001.png`

原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-675b70fc-929d-4261-a253-8d721818d9e7.png`

项目保存：`library/equipment/EQP_MACBOOKPRO_CAT_001/rejected/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v003.png`

实际提示词：

```text
Use case: precise-object-edit
Image 1 edit target: cat resting one paw on a miniature silver MacBook. Its cat identity, pose, scale and contact point are LOCKED by user approval. Image 2 supports the device's left edge port layout, Image 3 supports keyboard layout.
Correct only visible laptop keyboard layout and malformed edge ports in Image 1 to be a consistent view of the same device. Preserve exact laptop footprint, screen/lid size, paw-to-trackpad scale, paw position, cat body/face/fur, supporting paw, framing and lighting. Keep the silver lid back unchanged without adding a logo. Keyboard keys must follow Image 3 with coherent perspective. On the visible edge, use coherent slim modern laptop ports rather than USB-A-looking rectangles; keep all openings aligned on chassis, never float or intersect hinge. Do not copy a different side's ports onto the visible edge. No external cable, new props, extra limbs or image annotations. This is a fictional prop continuity edit, not a claim of retail model precision.
```

### CONTACT_v002

输入（顺序一致）：

- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_MACBOOK_PAW_CONTACT_v001.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v002.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_KEYBOARD_TOP_v001.png`

原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-e96f7829-f64a-410a-9b79-4271d5460722.png`

项目保存：`library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_MACBOOK_PAW_CONTACT_v002.png`

实际提示词：

```text
Use case: precise-object-edit
Image 1: close-up edit target. Image 2: user-approved wide interaction frame, authoritative paw position and paw-to-trackpad relative scale. Image 3: keyboard row layout.
Correct the close-up to represent the SAME instant as Image 2: keep the touching paw compact and round, with short grouped furry toes and no human fingers, retracted claws, continuous wrist. Align its contact patch relative to the four trackpad corners to match Image 2, not touching the front-left border as Image 1 currently does. Place the entire paw contact patch inside the trackpad with visible silver clearance to its front and left edges, preserving relative paw-to-trackpad size from Image 2. Only adjust paw placement and immediately adjacent wrist as needed; do not change paw anatomy or action. Correct the small visible keyboard portion using Image 3. Retain silver finish, camera angle, lighting and background, photorealistic contact shadow; no hovering or penetration. No new objects or text.
```
