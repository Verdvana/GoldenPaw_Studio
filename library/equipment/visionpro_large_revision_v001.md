# Vision Pro 大面罩版本回选与关联重制

最新侧面修正：`CHR_CAT_001_FIT_VISIONPRO_LEFT_PROFILE_v004.png` 替代绑带未绕后脑的 v002。后面 v002 与大面罩三分之四 v001 不变。详见设备库 `visionpro_side_band_revision_v004.md`；下方旧版本描述仅作历史。

## 当前唯一比例锚点

用户明确选择最初较大 VP 的佩戴图：`../characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v001.png`。后来的缩小面罩 `FIT_VISIONPRO_3Q_v002` 停用。不要因为编号较新就优先使用小面罩版。

MacBook 的比例锚点仍是 `CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v002.png`，本轮未改变。

## 关联重制清单

| 当前文件（相对根目录） | 来源 |
|---|---|
| `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_LEFT_PROFILE_v002.png` | `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-240f0921-3b9d-4a20-85ed-282ae0c88cbd.png` |
| `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_REAR_v002.png` | `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-2bf32b13-6d2b-4784-8f2c-d870f442f332.png` |
| `library/equipment/EQP_VISIONPRO_CAT_001/candidates/EQP_VISIONPRO_CAT_001_DESIGN_3Q_v003.png` | `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-871d8bf4-9eca-41b0-833c-e36d477d4c75.png` |

已重制全部现有衍生 VP 视角：侧面、后面与独立设备图。原选中的大面罩佩戴主图直接保留，不重新生成以免身份漂移。

## 审核与使用边界

- 侧面新图面罩明显恢复更高、更大的轮廓，鼻头与嘴可见，双耳露出；侧臂仍偏织物纹理，接头形状与主图尚非完全一致，仍是 CONTINUITY_CANDIDATE。
- 后面新图重新构建了后带和侧臂，未出现电池或线缆；前面罩被头部遮挡，不能凭后面图验证正面大小。后带端部结构仍待统一。
- 独立设备图已参考大面罩重制，保持较高面罩、无电池/线缆；无猫同框不能提供绝对尺寸，佩戴尺度仍以所选主图为准，结构细节为候选。
- 用户选型优先于之前为了鼻头间隙缩小面罩的判断。以后不得擅自回缩；若发现穿模，应保留已选比例，调整接触/遮挡而非改小整机。
- 小面罩佩戴 v002、侧面 v001、后面 v001、独立设备 v002 保留作历史，不再作为当前头显参考。更早带电池的独立 v001 仍停用。
- 比例选择不等同于设备三维结构或动态稳定性已验证。女主及双角色资产未改动。

## 生成方式与实际提示词

内置 imagegen，三个局部编辑调用，输入均已查看；没有调用 CLI。所有结果复制到项目，未覆盖历史文件。

### VP_SIDE_LARGE_v002

1. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_LEFT_PROFILE_v001.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v001.png`

```text
Use case: precise-object-edit
This is a fictional cat-adapted Vision Pro. Image 1 is the edit target for framing/anatomy only; Image 2 is the NEW AUTHORITATIVE worn headset design and size reference selected by the user: the LARGER, TALLER visor. Disregard all previous smaller/shorter visor proportions. Keep silver rim, dark curved glass, charcoal seal, pale hard side arms and gray rear knit band. No external battery, cable, top strap, new decorations or text. Preserve the cat's anatomy, coat, pose, background and lighting in Image 1. Do not shrink the cat's head.
Rebuild the headset in Image 1 to be the same large tall headset seen in Image 2 from this left-side angle. Match visor height relative to ear-to-nose distance, brow coverage and lower rim sitting close above the nose, keeping pink nose and mouth visible. Restore smooth rigid pale side arm and low-profile elongated oval attachment from Image 2, NOT Image 1's large circular disk and fabric-textured side arm. Ear remains upright above arm. Keep camera angle unchanged; this is a side-biased continuity view, not a new design.
```

### VP_REAR_LARGE_v002

1. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_REAR_v001.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v001.png`

```text
Use case: precise-object-edit
This is a fictional cat-adapted Vision Pro. Image 1 is the edit target for framing/anatomy only; Image 2 is the NEW AUTHORITATIVE worn headset design and size reference selected by the user: the LARGER, TALLER visor. Disregard all previous smaller/shorter visor proportions. Keep silver rim, dark curved glass, charcoal seal, pale hard side arms and gray rear knit band. No external battery, cable, top strap, new decorations or text. Preserve the cat's anatomy, coat, pose, background and lighting in Image 1. Do not shrink the cat's head.
Rebuild the rear headset assembly in Image 1 to correspond to Image 2's larger visor and its wearer-fit: smooth rigid pale side arms connect to ONE gray ribbed knitted band across the back of head below ear bases. Preserve the actual band height relative to ears in Image 2; do not enlarge the rear band arbitrarily just because the front visor is larger. Ear bases stay unobstructed, crown entirely fur. Match attachment profile from Image 2, no protruding circular dials. Rear head naturally occludes front glass; do NOT draw a visor on the back of the head. Keep rear camera framing unchanged.
```

### VP_DEVICE_LARGE_v003

1. `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_VISIONPRO_CAT_001/candidates/EQP_VISIONPRO_CAT_001_DESIGN_3Q_v002.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v001.png`

```text
Use case: precise-object-edit
Image 1: standalone headset edit target. Image 2: user-selected LARGE worn headset, authoritative front visor proportions and side-arm design.
Rebuild the standalone headset in Image 1 to match exactly the taller, broader visor silhouette and relatively shallow charcoal face seal of Image 2, as a matching detached fictional prop. Preserve Image 1 camera angle, gray studio background, materials, gray ribbed rear band and product-only composition. Match the smooth rigid pale side arms and low-profile elongated oval attachment of Image 2. The visor should retain the large/tall silhouette, not the later reduced-height goggles. No cat in final image. No battery, cable, crown strap, extra controls, text or watermark. Detached product image has no absolute scale cue; only preserve relative device component proportions from worn reference.
```
