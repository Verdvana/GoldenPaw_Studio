# 设备多角度与接触补图 v001

## 用户确认与边界

用户本轮确认「比例可以的，继续吧」。确认对象为上一轮已展示的 `CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v002.png` 与 `CHR_CAT_001_FIT_VISIONPRO_3Q_v002.png` 中的视觉大小关系。建立 USER_CONFIRMED_VISUAL_SCALE；不扩张为用户批准所有设备细节、动作或精确厘米尺寸。

后续猫/设备大小以两张 v002 为锚点，不能再按新镜头主观缩放；猫身份仍以批准身份母版为最高优先级。旧 25cm、14cm 是早期设计假设，不可作为已确认尺寸。

## 输出与审核

全部使用内置 imagegen，以已查看的项目图片为参考，一图一调用，共四张。未使用 CLI。模型版本/随机种子未提供。

| 调用 | 保存路径（相对工程根目录） | 审核 |
|---|---|---|
| VISION_LEFT_PROFILE_v001 | `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_LEFT_PROFILE_v001.png` | 侧面偏三分之四，圆形连接件与织带感侧臂偏离原试配；待统一，不作严格正侧母版 |
| VISION_REAR_v001 | `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_REAR_v001.png` | 后带可见且未跨头顶，无电池线；后方结构为新增候选，仍需与侧面接头统一 |
| MAC_KEYBOARD_TOP_v001 | `library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_KEYBOARD_TOP_v001.png` | 字母行清晰、键盘/触控板/扬声器区域可辨；功能图标、键距与已有设备角度仍需统一，不宣称真实产品复原 |
| MAC_PAW_CONTACT_v001 | `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_MACBOOK_PAW_CONTACT_v001.png` | 圆润猫爪、连续手腕毛发与接触阴影可辨；接触点偏触控板前侧，爪/板局部比例及键盘仍需和原全景对齐，不能直接作连续剪辑匹配 |

四张均为 CONTINUITY_CANDIDATE，不纳入批准身份/动作白名单。角色原有 30 张批准静态图不变。没有女主、双角色或视频生成。

## 优先处理的连续性问题

1. 头显侧臂材质与连接件：以上轮三分之四试配 v002 为锚点，统一为其硬质浅色侧臂与连接形状；本轮侧面新圆形连接件不能自动成为新设定。侧面图也不是严格 90 度。
2. 头显后带：本轮补出后方路径，但仅有静态图片，不代表不滑落或真实佩戴舒适性已验证。
3. 电脑：俯视图可用于整理键盘布局，仍需与斜视图统一后才能认定为同一设备母版。
4. 接触近景：不把「有接触阴影」等同于与全景完美匹配；下一步对齐爪中心在触控板中的相对位置与遮挡比例。

## 原始输出映射

- `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-ed0ce80b-e290-42e7-b030-d9faa82b4311.png` → `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_LEFT_PROFILE_v001.png`
- `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-b1f6cc65-f368-451a-bb82-3accaf4987b6.png` → `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_REAR_v001.png`
- `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-d583e95c-d23b-4921-a2df-5bf60dd96f91.png` → `library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_KEYBOARD_TOP_v001.png`
- `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-87c94659-fb35-4f4a-a81d-a58de26f9f6d.png` → `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_MACBOOK_PAW_CONTACT_v001.png`

## 实际输入与提示词

### VISION_LEFT_PROFILE_v001

1. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v002.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/face/CHR_CAT_001_FACE_LEFT_PROFILE_NEUTRAL_v001.png`

```text
Use case: photorealistic-natural
Asset type: static continuity diagnostic, fictional cat-adapted headset.
Image 1 is the user-confirmed cat/headset visual size and worn design anchor. Image 2 is supplementary feline anatomy and coat only. Preserve the exact same adult broad-headed golden British Shorthair and SAME compact visor-to-head size as Image 1, not the old larger visor. Silver rim, short dark-glass visor, charcoal seal, pale side arms below ear bases and one gray ribbed rear band. Nose and whiskers unobstructed; ears upright and uncompressed. No battery, wires, crown straps, extra buckles, helmet, text, panels or watermark. Neutral gray studio, soft neutral daylight, sharp diagnostic detail. New camera angle of the same setup, not a redesign.
Primary request: strict LEFT PROFILE head-and-upper-chest portrait, cat nose points image-left. Entire near ear, nose, muzzle and back of head visible. Show near-side visor depth, face-seal contact above muzzle, complete side-arm-to-knit-band junction, band passing below and behind ear base. Keep a visible fur gap above pink nose. Avoid three-quarter front view. No full body needed.
```

### VISION_REAR_v001

1. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v002.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_TURN_BACK_STANDING_v001.png`

```text
Use case: photorealistic-natural
Asset type: static continuity diagnostic, fictional cat-adapted headset.
Image 1 is the user-confirmed cat/headset visual size and worn design anchor. Image 2 is supplementary feline anatomy and coat only. Preserve the exact same adult broad-headed golden British Shorthair and SAME compact visor-to-head size as Image 1, not the old larger visor. Silver rim, short dark-glass visor, charcoal seal, pale side arms below ear bases and one gray ribbed rear band. Nose and whiskers unobstructed; ears upright and uncompressed. No battery, wires, crown straps, extra buckles, helmet, text, panels or watermark. Neutral gray studio, soft neutral daylight, sharp diagnostic detail. New camera angle of the same setup, not a redesign.
Primary request: straight REAR head-and-shoulders close-up of the seated cat, looking directly away from camera. Show both ears and all of the gray knitted band across the back of head, linked symmetrically to side arms below both ears. Back of crown stays entirely fur, no top strap. Band is supported against rear head rather than floating, does not wrap around the neck. The front visor is naturally hidden behind the head except possible small side edges. Image 2 supplies rear fur and ear shape only; do not copy its standing body pose.
```

### MAC_KEYBOARD_TOP_v001

1. `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_DESIGN_OPEN_3Q_v003.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v002.png`

```text
Use case: product-mockup
Asset type: overhead keyboard structure candidate for the same fictional silver cat-sized M4 MacBook Pro.
Input image 1: laptop design; Image 2: user-confirmed cat-to-laptop visual size only. No cat in output.
Create a straight top-down orthographic-like product photograph of the keyboard deck, trackpad and complete silver base. Hinge is at top of frame, front lip at bottom. Screen remains opened about 105 degrees, mostly outside top frame; do not flatten laptop to 180 degrees. Preserve base width/depth, keyboard well size, two speaker grilles and centered trackpad proportions from Image 1. Silver anodized metal, black keys, neutral gray table, soft even lighting, minimal perspective.
Correct coherent US QWERTY keyboard: physical function row, number row, Q W E R T Y U I O P, A S D F G H J K L, Z X C V B N M, one spacebar, standard modifiers, inverted-T arrows, Touch ID at top right. No duplicated letters or numeric pad, no extraneous keys. White key legends, no annotations or watermark. Candidate only, not a real product specification. Do not redesign the computer or add props.
```

### MAC_PAW_CONTACT_v001

1. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v002.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/details/CHR_CAT_001_FRONT_PAWS_AND_PADS_v001.png`
3. `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_DESIGN_OPEN_3Q_v003.png`

```text
Use case: photorealistic-natural
Asset type: continuity insert, close-up of one cat paw touching the miniature silver MacBook trackpad.
Input image 1: user-confirmed interaction, device/paw relative size and pose anchor. Image 2: anatomical reference only. Image 3: keyboard and trackpad layout support only.
Create a closer camera view of the SAME trackpad contact from Image 1, with a modest elevated side angle that clearly reveals the rectangular trackpad outline, touching paw, continuous furry wrist and lower foreleg, silver palm rest and a small portion of black keyboard near hinge. Preserve paw-to-trackpad size, contact location and device orientation. Do not change the cat's action. Paw is compact, round, furry, with short closely grouped toes and retracted claws; pads on surface, not facing camera, no fingers/thumb. Subtle contact shadow, no hovering or penetration. Trackpad lies between front lip and keyboard, not on keyboard or beside it. Keep most of trackpad border visible to inspect contact.
Neutral studio daylight, photorealistic fur/metal textures. No full cat face needed, no extra paw on laptop, no battery, cables, other devices, text overlays, diagrams or watermark. A static contact study, not proof of movement.
```

