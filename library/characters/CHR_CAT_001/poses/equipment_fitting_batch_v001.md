# 猫咪设备首轮试配 v001

日期：2026-09-04

## 本轮范围与结论

使用内置 imagegen 完成五次调用：电脑结构修正一次、头显试戴及修正两次、触控板接触及修正两次。所有生成结果已保存到项目。没有生成女主、双角色互动或连续视频。

当前推荐继续迭代的试配图：两张 `FIT_*_v002`。状态均为 FITTING_CANDIDATE，不进入批准身份或动作资产。角色批准静态图仍为 30 张。

- MacBook 独立 v003：主字母行比 v002 更有序，重复接口减少，触控板和银色外壳保留；功能键、修饰键、接口形状/间距仍需可信产品图比对，不视为产品级精确复原。只用于本轮尺度探索。
- 电脑试配 v001：猫朝向键盘，支撑爪、坐姿和电脑在同一表面；接触爪趾部过度分离、卷曲，需修改。
- 电脑试配 v002：接触爪更紧凑圆润，无人手式长指。仍需近景确认触控板边界与真实接触点，近侧接口相对独立 v003 存在漂移；机盖无标识，未锁定机盖背面。脸部角度需与批准三分之四脸图再对照。不要将本图当作设备或身份母版。
- 头显试配 v001：双耳露出，但面罩下沿靠鼻头过近。
- 头显试配 v002：面罩高度降低，鼻头上方有可见毛发间隙，鼻孔/嘴/胡须可见，未出现外挂电池或线缆。后带大部分遮挡，不能证明后脑/耳根接触与佩戴稳定性；双眼被遮盖，不能用本图审核眼部身份。
- 两张试配的猫体积与毛色大体保持，但没有度量标定，不能认定此前假设的电脑宽 25cm、头显宽 14cm 已实现；画面透视亦不能作为严格比例测量。
- 减小设备并不自动证明猫咪能准确逐键输入；这里只检查静态接触，不推定真实动物可用或改装可制造。
- 头显佩戴 v002 的面罩高宽比不同于独立设备候选 v002；需选择试配方案后反向同步独立多角度设备图，不能直接混用。

## 输出映射

| 调用 | 项目保存路径（相对根目录） | 原始输出 |
|---|---|---|
| MAC_STRUCTURE_v003 | `library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_DESIGN_OPEN_3Q_v003.png` | `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-00e0b05d-3bce-4d18-a865-96e0e82253d4.png` |
| VISION_FIT_v001 | `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v001.png` | `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-e9787db6-8edf-4702-8ffd-3ef4e0bfa4d3.png` |
| VISION_FIT_v002 | `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v002.png` | `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-7abcab3e-6da0-4923-aa22-46ebf0089915.png` |
| MAC_FIT_v001 | `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v001.png` | `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-a828563d-4212-403d-92f7-0343f539dc76.png` |
| MAC_FIT_v002 | `library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v002.png` | `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-a5922f97-8891-4f90-bd1d-be4cd85c6054.png` |

## 来源

电脑结构修正前查询 [Apple 2024 16 英寸 MacBook Pro 规格](https://support.apple.com/en-gb/121554)，核对端口类别及键盘说明；未把网页图片作为生成输入。项目仍是用户指定 M4 的虚构猫用银色改装版，不宣称对应原装 16 英寸零售规格。

## 下一轮顺序

1. 头显：补严格侧面和后面试配，验证头带与耳根路径；确认方案后同步独立设备图。
2. 电脑：先补键盘俯视、接触爪近景与机盖背面，解决结构漂移；固定猫与电脑的比例，再扩展双爪键盘接触。
3. 仅通过结构与身份检查的静态图可纳入 APPROVED_STATIC；运动连续性另做视频测试。

## 实际提示词与输入

以下输入保留调用时原始路径；工具生成目录的中间输入已按上表一并复制到项目，可通过映射重建参考，不依赖缓存作为唯一资产。

### MAC_STRUCTURE_v003

1. `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_DESIGN_OPEN_3Q_v002.png`

```text
Use case: precise-object-edit
Input image 1: edit target, silver fictional cat-sized M4 MacBook Pro candidate.
Correct only the keyboard layout and the visible left-edge port layout. Keep silver color, exact camera angle, black inactive notched screen, lid angle, base proportions, trackpad, speaker grilles, background, shadows and product position unchanged.
Keyboard: realistic US English MacBook keyboard with one aligned number row, Q W E R T Y U I O P in the top letter row, A S D F G H J K L in the middle, Z X C V B N M in the bottom letter row, one long space bar, one set of correctly placed modifier keys, inverted-T arrows at bottom right, physical function row, Touch ID at top right. Crisp small white legends, no repeated or invented keys, no numpad. Match perspective.
Visible left edge: remove the spurious repeated rectangular openings. Replace with four correctly spaced openings: from hinge toward front, one slim MagSafe-style power connector, two small USB-C oval ports, and one round headphone jack. Smooth uninterrupted silver metal toward front. No USB-A ports. No extra holes.
This remains a fictional miniaturized prop, not a retail product specification. No cat, text annotations or watermark.
```

### VISION_FIT_v001

1. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_IDENTITY_FRONT_STANDING_v001.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_IDENTITY_FRONT_SEATED_v001.png`
3. `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_VISIONPRO_CAT_001/candidates/EQP_VISIONPRO_CAT_001_DESIGN_3Q_v002.png`

```text
Use case: photorealistic-natural
Asset type: diagnostic static fitting candidate for a fictional cinematic cat character; not a real animal equipment test.
Input images: Image 1 highest-priority cat identity/body/coat reference; Image 2 seated body structure reference; Image 3 headset external design reference.
Primary request: the exact same adult chubby golden-shaded British Shorthair sitting naturally on a neutral gray studio floor, wearing a MINIATURIZED fictional Vision Pro matching Image 3, with no external battery and no cable. Front-left three-quarter portrait of head and full seated body, entire ears and paws and tail in frame, normal perspective.
Preserve broad round skull, full cheeks, small dusty-pink nose, short cream muzzle, cream chest, original gold-apricot plush fur and forehead markings, short sturdy feline limbs, thick brown-gold-tipped tail. Do not shrink the cat's head to fit the device.
Fitting: compact curved dark-glass visor covers eyes only, approximately as wide as the face below the ears; silver rim, shallow charcoal seal fitted at brow/upper cheek area. Both ears fully upright and unobstructed, ear bases visible above side arms; side arms pass BELOW ear bases to gray ribbed rear knitted band around back of head. No top strap. Pink nose, nostrils, closed mouth, cream muzzle, cheeks and whiskers remain visibly unobstructed beneath the visor. No glass eyes drawn on visor.
Soft daylight-balanced studio lighting, sharp anatomical and contact detail. Keep nonhuman feline posture, both front paws planted. No computer, clothes, people, extra limbs, neck collar, helmet, battery, cable, annotations, multiple panels or watermark. Single calm static pose only; not a production-approved fitting.
```

### MAC_FIT_v001

1. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_IDENTITY_FRONT_STANDING_v001.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_IDENTITY_FRONT_SEATED_v001.png`
3. `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-00e0b05d-3bce-4d18-a865-96e0e82253d4.png`

```text
Use case: photorealistic-natural
Asset type: diagnostic static cat-to-device scale and contact fitting candidate.
Input images: Image 1 highest-priority identity/coat/body reference; Image 2 seated feline body structure; Image 3 silver miniature M4 MacBook Pro candidate design reference, not an exact keyboard master.
Primary request: same adult broad-faced chubby golden-shaded British Shorthair sitting in a natural feline seated posture immediately in front of and facing the keyboard of a small SILVER MacBook Pro. A near-side front paw rests gently on the center of its trackpad; other front paw supports the cat on the tabletop beside the front corner. Hindquarters and hind feet supported on the same plain gray table. One continuous anatomically coherent near foreleg from shoulder to wrist to rounded paw, no human fingers. Cat looks toward screen.
Composition: diagonal side view from the cat's near side, slightly above tabletop to reveal trackpad contact and keyboard, cat and laptop facing each other correctly. Full cat, tail and complete open laptop within a wide 16:9 frame. Keep face readable in three-quarter or side view; avoid lid hiding contact paw. Do not have cat reach from behind the screen.
Scale: proposed fictional laptop body width roughly 1.3 times the cat's seated chest width; compact enough to reach trackpad without leaning torso across keyboard. Do not enlarge/shrink the cat. Laptop may be adjusted to cat, never cat to laptop. Screen remains off for this geometry test. Screen open about 105 degrees, silver chassis, black keys, large trackpad. No extra objects or headsets.
Keep broad round cheeks, olive-gray-green eyes, pink nose, cream muzzle and chest, warm golden-apricot plush short fur, short sturdy legs, brown-gold tail tip, no black tip or narrow kitten face. Neutral studio daylight, realistic paw and device contact shadows, sharp detail, no labels, text overlays, panels, people, clothes or watermark. Static test only, not typing movement or an approved scale master.
```

### VISION_FIT_v002

1. `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-e9787db6-8edf-4702-8ffd-3ef4e0bfa4d3.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_IDENTITY_FRONT_STANDING_v001.png`

```text
Use case: precise-object-edit
Input image 1: edit target, cat wearing the fictional standalone Vision Pro. Image 2: cat identity reference.
Change only the worn headset fit: reduce the visor's vertical height approximately 12 percent while preserving its curved dark glass and silver outline design, and shift the visor slightly upward so there is a clearly visible narrow strip of fur between the lower nose-bridge cutout and the top of the pink nose. Keep eyes covered, nose/nostrils/mouth/muzzle/whiskers completely unobstructed, no contact with nose. Retain comfortable ear-base clearance and both ears fully upright; adjust side arms and rear band only enough to fit the revised visor, below ears, no crown strap. Keep cat face/skull/body/paws/tail/fur, pose, image framing, camera angle and studio lighting unchanged. No external battery, cable, new objects, eyes on glass, labels or watermark. Preserve feline anatomy; do not shrink the cat's face to fit equipment.
```

### MAC_FIT_v002

1. `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-a828563d-4212-403d-92f7-0343f539dc76.png`
2. `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/details/CHR_CAT_001_FRONT_PAWS_AND_PADS_v001.png`

```text
Use case: precise-object-edit
Input image 1: edit target, the cat using the miniature silver laptop. Image 2: approved feline paw anatomy reference.
Change ONLY the cat paw resting on the laptop trackpad and the immediately adjoining wrist fur. Replace the finger-like separated curled digits with a compact rounded furry feline paw like the grounded paw in Image 2, short closely grouped toes, claws fully retracted, no thumb, no long fingers or exposed pink pads. The underside gently contacts the same point on the trackpad with a subtle contact shadow; keep wrist anatomically connected to the existing foreleg. Preserve entire cat identity, face, expression, body, supporting paw, tail, limb placement, silver laptop geometry and size, background, camera angle, lighting and framing unchanged. No other edits.
```

