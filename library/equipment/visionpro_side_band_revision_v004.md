# VP 侧面绑带修正 v004

## 结果

用户指出侧面 v002 的针织带停在头侧，未覆盖后脑。本轮只修正该侧面，不修改已选大面罩比例或 MacBook。

当前侧面图：`../characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_LEFT_PROFILE_v004.png`。

视觉检查：浅色侧臂连接后段针织带，针织带延伸到后脑轮廓并弯曲至遮挡处，不再呈贴在头侧的短矩形块；大面罩、双耳及口鼻保留，无外挂电池或线缆。远侧连接被头遮挡，不能据单张图证明完整三维连接或动态稳定性。状态：修正候选，未晋升身份母版。

侧面 v002 标记 REJECTED_BAND_ROUTING。中间尝试 v003 虽延伸了绑带，但把整条侧臂变为针织，未采用；仅留工具输出，不作为生产资产。当前侧面入口以 v004 为准，后面仍为 v002，选定大面罩主图仍为三分之四 v001。

## 方式与提示词

使用内置 imagegen，两次局部编辑；依照 imagegen 流程分别检查绑带路径及材质，再另存版本，没有覆盖历史图。

### 第一次：延伸后脑绑带（未采用）

1. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_LEFT_PROFILE_v002.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_REAR_v002.png`
3. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v001.png`

```text
Use case: precise-object-edit
Image 1 is the edit target: a cat in side view with a BROKEN headband that wrongly ends as a small ribbed patch on the visible side of its head.
Image 2 is the rear-view band topology reference. Image 3 locks the selected LARGE visor size and cat identity.
Fix ONLY the headband routing in Image 1. Remove the small rectangular ribbed patch that terminates halfway along the side of the skull. Replace it with one continuous gray ribbed knitted rear band extending from the near-side pale arm BEHIND THE EAR all the way to the far-right rear silhouette of the skull. The band must visibly curve around the back of the head, foreshorten at that far-right contour, and disappear behind the skull to connect to the opposite side arm. Its upper and lower edges must both continue without interruption to the rear silhouette. No exposed end cap or free edge resting on side fur. No fur gap between the visible side strap and back-of-head wrap. Show the curved ribbed band hugging and covering the rear occiput, not the neck.
Preserve the exact original LARGE visor position, shape and size, near side connector, cat head/skull/ear shapes, pink nose, muzzle, whiskers, coat, framing, lighting and gray background. Do not compress the cat head or change camera angle. Ears stay upright and uncovered, band below ear bases. No top strap, battery, wires, text or watermark. A physically continuous closed-loop head strap, never a short fabric patch stuck to cheek.
```

输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-d3ea962f-207b-4ea6-9c13-5e1795938a53.png`

### 第二次：恢复前段侧臂（采用）

1. `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-d3ea962f-207b-4ea6-9c13-5e1795938a53.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_LEFT_PROFILE_v002.png`

```text
Use case: precise-object-edit
Image 1 edit target already has the correct continuous strap curving around the far-right back-of-head silhouette. Image 2 is ONLY the reference for the original smooth pale rigid side arm; its broken short rear band must NOT be copied.
Change only the FRONT PORTION of Image 1's ribbed band into the original smooth light-gray rigid side arm. From the oval visor connector on image-left to just behind the near ear base (approximately the horizontal middle of the visible strap), use smooth pale rigid material, not knit. From that single junction onward to the far-right rear skull silhouette, KEEP the existing ribbed knit band and its continuous wrap around the back of the head. Absolutely retain the full-length wrap with no exposed end or gap. The rear band must continue behind the occiput, NOT terminate as a rectangular patch on the side.
Keep large visor size, head, face, ear shapes, nose, fur, pose, camera, background, lighting and every other detail unchanged. No new fasteners, crown strap, battery, cable or text.
```

输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-344b1d76-329b-4eaa-9073-81342912dd05.png`

