# MacBook 左右侧接口与全景修订 v001

日期：2026-09-04。使用内置 imagegen；两张参考生成、一张局部编辑。未使用 CLI。所有输出为候选，未新增角色 approved。

## 产物与审核

- [左侧 v001](EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_PORTS_LEFT_v001.png)：MagSafe、两枚 USB-C、耳机孔数量及顺序清楚；孔位间距未作精密测量。
- [右侧 v001](EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_PORTS_RIGHT_v001.png)：SDXC、USB-C、HDMI 次序清楚；卡槽内部接点表现不精确，不作为极近特写母版。
- [操作全景 v004](../characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v004.png)：从 v002 仅针对露出的右侧接口修正；视觉检查保留支撑前爪与接触前爪的姿态、猫体积及电脑比例，接口有明确形状区分。未证明像素级保持；键盘与接触近景尚未完成连续性审核。
- 原全景 v002 仍是用户确认比例依据，不覆盖；v003 继续停用。v004 是本轮修正候选，不表示用户已批准。

## 结构依据与来源

[Apple：MacBook Pro (14-inch, M4, 2024) 技术规格](https://support.apple.com/en-gb/121552) 提供 M4 接口种类及左右侧示意。仅借用接口组织方式，不把猫用虚构尺寸改成真实 14 英寸，不更改已确认猫／电脑比例。历史 16 英寸说明不作为 M4 型号或接口依据。

官方来源图，仅作参考，不是自有生成资产：

- `EQP_MACBOOKPRO_CAT_001/references/APPLE_M4_PORTS_LEFT.png`：https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/charging-expansion-uk-1.png
- `EQP_MACBOOKPRO_CAT_001/references/APPLE_M4_PORTS_RIGHT.png`：https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/charging-expansion-uk-2.png

左右定义以操作电脑时为准。左侧由后至前为 MagSafe、USB-C、USB-C、耳机孔；右侧由前至后为 SDXC、USB-C、HDMI。生成图细微间距和槽内接点不是实物规格依据。

## 实际提示词与输入

### LEFT

原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-be7ca955-96a1-486c-b0bc-0112fd883a70.png`

输入顺序：

- `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/references/APPLE_M4_PORTS_LEFT.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_DESIGN_OPEN_3Q_v004.png`

```text
Use case: product-mockup
Asset type: single diagnostic side-view reference for a fictional cat-sized silver M4 MacBook Pro prop.
Input image 1 is authoritative for this side's port silhouettes, count, order and relative positions ONLY. Input image 2 is the current SILVER finish and overall fictional prop style reference, NOT a port reference.
Generate a photorealistic CLOSED laptop strictly left side profile, level camera at chassis height, near-orthographic long lens, complete chassis visible with margins, neutral light gray studio background and gentle contact shadow. Match image 1 orientation and port locations; uniformly adapt to the fictional miniature prop, no actual size labels. Rear/hinge at image LEFT; from rear to front exactly one MagSafe recess with five subtle contact dots, two separate rounded USB-C ports, one circular headphone socket; remainder blank.
Silver aluminum not space black, thin closed lid seam, small black feet beneath, precise machined dark recessed port cavities. No extra openings, USB-A, cables, cat, props, labels, leader lines, text, watermark or multi-panel layout. This is a fictional scaled prop study, not a retail dimension drawing.
```

### RIGHT

原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-6f1560c4-db5b-4cf3-87ef-af6782b1dbe5.png`

输入顺序：

- `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/references/APPLE_M4_PORTS_RIGHT.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_DESIGN_OPEN_3Q_v004.png`

```text
Use case: product-mockup
Asset type: single diagnostic side-view reference for a fictional cat-sized silver M4 MacBook Pro prop.
Input image 1 is authoritative for this side's port silhouettes, count, order and relative positions ONLY. Input image 2 is the current SILVER finish and overall fictional prop style reference, NOT a port reference.
Generate a photorealistic CLOSED laptop strictly right side profile, level camera at chassis height, near-orthographic long lens, complete chassis visible with margins, neutral light gray studio background and gentle contact shadow. Match image 1 orientation and port locations; uniformly adapt to the fictional miniature prop, no actual size labels. Rear/hinge at image RIGHT; image left-to-right exactly SDXC narrow slot, one USB-C rounded socket, one HDMI trapezoidal socket; remainder blank.
Silver aluminum not space black, thin closed lid seam, small black feet beneath, precise machined dark recessed port cavities. No extra openings, USB-A, cables, cat, props, labels, leader lines, text, watermark or multi-panel layout. This is a fictional scaled prop study, not a retail dimension drawing.
```

### FULL_v004

原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-b3a7922e-4983-4429-b340-c6a4572bba03.png`

输入顺序：

- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v002.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/references/APPLE_M4_PORTS_RIGHT.png`

```text
Use case: precise-object-edit
Image 1 is the edit target. Image 2 supplies only the right-side port silhouettes and order. Make one tiny localized correction ONLY to the thin visible silver laptop side edge at bottom-right of Image 1: replace its three malformed openings with SDXC slot, USB-C socket, HDMI socket in this order from image-left toward image-right/hinge. SDXC is a thin elongated horizontal slit, USB-C is a small rounded oblong, HDMI is a wider trapezoidal opening. Project them onto the existing side edge plane and keep their scale small. Do NOT change the laptop silhouette or edge thickness.
Everything outside this narrow port strip MUST remain unchanged: exact cat face, eyes, ears, fur, chest, tail, both forelegs (one supporting paw on the floor and the other resting on trackpad), paw contact point, complete cat body proportions, laptop size and pose, silver blank lid, keyboard, trackpad, shadows, lighting and composition. No redesign, no pose change, no keyboard editing, no cat regeneration, no labels, no new objects.
```

