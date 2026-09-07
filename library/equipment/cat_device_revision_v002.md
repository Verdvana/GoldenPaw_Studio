# 猫用设备 v002 编辑记录

## 已确认变更

MacBook Pro 改为银色；Vision Pro 移除外挂电池及连接线，仅保留主机与佩戴头带。M4 与猫用改装设定不变。

## 方式与审核

使用内置 imagegen，以各自 v001 作为编辑目标，分别执行局部修改。未提供模型版本或种子。

- MacBook：银色外壳已实现，黑色键盘和屏幕保留；键帽字符与接口错误仍在，状态 CONCEPT_ONLY / NEEDS_CORRECTION。
- Vision Pro：电池、连接线及凸出插头已移除，主机和后带保留；状态 DESIGN_CANDIDATE，尚未验证猫头适配。
- 编辑图并非像素级不变，细微纹理/键帽变化不作为新结构标准。
- 当前使用 v002；v001 仅保留历史，不能混用配色与电池配置。

## 保存路径（相对本目录）

- `EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_DESIGN_OPEN_3Q_v002.png`
- `EQP_VISIONPRO_CAT_001/candidates/EQP_VISIONPRO_CAT_001_DESIGN_3Q_v002.png`

## 原始输出

- `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-324956b4-05bb-4801-a896-b50590a87416.png`
- `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-5c348195-6e6f-493f-9625-a6663f87a135.png`

## 实际输入与提示词

### EQP_MACBOOKPRO_CAT_001

输入：`/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_DESIGN_OPEN_3Q_v001.png`

```text
Use case: precise-object-edit
Input image 1: edit target, existing fictional cat-sized M4 MacBook Pro candidate.
Change only the metal finish from space black to the classic light silver anodized aluminum MacBook Pro finish, including palm rest, trackpad surface, chassis edges and visible metal display shell. Keep the keyboard keys and keyboard well black, display bezel black and screen off. Preserve the exact device design, proportions, camera angle, open-lid angle, composition, neutral studio background and lighting. Photorealistic silver metal, not white paint or chrome. No new objects, labels or watermark.
```

### EQP_VISIONPRO_CAT_001

输入：`/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_VISIONPRO_CAT_001/candidates/EQP_VISIONPRO_CAT_001_DESIGN_3Q_v001.png`

```text
Use case: precise-object-edit
Input image 1: edit target, existing fictional feline-adapted Vision Pro candidate.
Remove the external silver battery pack, the entire connecting fabric cable, and its protruding plug from the headset. Restore clean neutral studio surface and natural shadows where the battery and cable were. Leave only the headset assembly including its existing rear knitted headband and side arms. Finish the former plug location flush with the side-arm surface, without a dangling socket, wire or stump. Preserve the headset position, scale, curved dark glass front, silver frame, cushion, rear gray knitted headband, camera angle, background and lighting. This is a fictional standalone cat-adapted prop; do not add any replacement power pack or other objects. No labels or watermark.
```

