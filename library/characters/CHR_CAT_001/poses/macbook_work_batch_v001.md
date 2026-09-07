# MacBook 中性工作与双爪接触 v001

日期：2026-09-04。内置 imagegen，有参考编辑；未使用 CLI。两张新图尚待用户确认，未加入猫身份 approved。

## 已确认资产

用户本轮明确认可左右侧接口 v001、单爪操作全景 v004 三张，记为 USER_APPROVED_STATIC。仍保留原位置并由设备参考入口管理，不等于动态验证通过。

## 新增与审核

- [中性工作坐姿 v001](equipment_candidates/CHR_CAT_001_MACBOOK_WORK_NEUTRAL_v001.png)：两前爪落地，猫看向屏幕，未操作设备。可供静态候选审核。
- [双爪键盘 v002](equipment_candidates/CHR_CAT_001_MACBOOK_KEYBOARD_BOTH_PAWS_v002.png)：修正版向键区移动，趾端与键区边缘发生重叠，但近侧爪主体仍接近掌托／键区边界，不能称为双爪完整落在键帽上的合格母版。状态 CONTACT_QA_PENDING。猫姿态前倾，设备透视与原全景略有变化，不作为匹配首尾帧。
- 双爪首版落在掌托附近，不采用作键盘锚点，仅留工具原始输出供追溯。
- 没有修改女主或 VP；没有生成视频。键盘跨角度、触控板近景、双爪接触仍待进一步核对，不能因用户认可上批三图便认定全部设备资产完成。

## 输出路径与实际提示词

### WORK_NEUTRAL

原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-d4cfbcf2-4045-4edb-b7d0-95243bc803cb.png`

参考顺序：

- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v004.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_IDENTITY_FRONT_SEATED_v001.png`

```text
Use case: identity-preserve
Image 1 is the approved cat/laptop scene to derive a new static pose from; it locks cat-to-laptop scale, silver fictional cat-sized M4 laptop, right edge ports, camera, lighting and background. Image 2 supports the exact same cat's facial identity and compact chubby seated body, not a request to rotate him frontally.
Preserve broad round cheeks, gray-green eyes, pink nose, cream muzzle/chest, golden-apricot plush fur, short sturdy legs and thick brown-gold tail tip. Keep laptop position, size, silver blank back lid, opening angle and visible ports unchanged. Same neutral gray studio, whole cat and laptop visible, landscape 16:9 photorealistic cinematic still. No people, clothes, extra devices, text, watermark or human hands.
Change only the cat's working pose: lower the paw currently touching the trackpad onto the floor beside the other forepaw. Both forepaws naturally planted beneath the shoulders just behind the laptop front edge, with a small visible gap from the chassis, no device contact. Hindquarters seated and weight supported, same tail position. Cat calmly looks toward the screen, mouth closed, ears neutral-alert. Preserve original head shape and body volume. This is a resting work pose, not typing.
```

### KEYBOARD_BOTH_PAWS

原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-42024f63-4542-40a4-ada7-dc7596df30fa.png`

参考顺序：

- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_MACBOOK_TRACKPAD_v004.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_IDENTITY_FRONT_SEATED_v001.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_KEYBOARD_TOP_v001.png`

```text
Use case: identity-preserve
Image 1 is the approved cat/laptop scene to derive a new static pose from; it locks cat-to-laptop scale, silver fictional cat-sized M4 laptop, right edge ports, camera, lighting and background. Image 2 supports the exact same cat's facial identity and compact chubby seated body, not a request to rotate him frontally.
Preserve broad round cheeks, gray-green eyes, pink nose, cream muzzle/chest, golden-apricot plush fur, short sturdy legs and thick brown-gold tail tip. Keep laptop position, size, silver blank back lid, opening angle and visible ports unchanged. Same neutral gray studio, whole cat and laptop visible, landscape 16:9 photorealistic cinematic still. No people, clothes, extra devices, text, watermark or human hands.
Image 3 supplies the keyboard layout only.
Change only the cat's pose to a plausible seated two-paw keyboard contact: hindquarters and hind paws remain grounded, compact torso leans slightly forward, shoulders and bent forelegs reach naturally without lengthening limbs. Both rounded furry forepaws rest lightly on two separated lower-keyboard areas near the spacebar, NOT the trackpad or palm rest. Paw contact shadows visible; each paw naturally spans several keys. Maintain keyboard plane and coherent wrist-to-paw anatomy, no fingers, no spread human-like toes, no extra limbs, no claws, no floating or penetration. Cat gaze toward screen. Do not shrink laptop or elongate cat to reach; maintain overall approved scale. A static contact anchor only, not an actual typing demonstration.
```

### KEYBOARD_BOTH_PAWS_v002

原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-330786ac-4cc9-4fbc-ac05-e296941acecf.png`

参考顺序：

- `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-42024f63-4542-40a4-ada7-dc7596df30fa.png`

```text
Use case: precise-object-edit
Edit this image only. The two forepaws currently rest on silver palm rest, which is WRONG. Move BOTH forepaw contact patches forward onto the BLACK KEYCAP FIELD, towards the screen hinge, so each paw visibly covers and touches multiple black keys, with black keys visible immediately behind and beside each paw. Neither paw may remain on the silver palm rest or trackpad. Move the seated cat slightly closer to the laptop only if necessary for anatomically natural short forelegs; bend shoulders/elbows naturally, no elongated limbs or human fingers. Preserve the cat identity, broad cheeks, eyes, ears, compact chubby torso volume, fur, hindquarter grounded support, tail, camera, gray studio, silver laptop size/shape, exact visible ports and lid opening. Two separated compact round furry paws, no claws, no extra paws, coherent contact shadows. Static keyboard contact, no motion.
```

