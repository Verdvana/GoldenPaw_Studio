# VP 正面与桌面互动批次 v001

状态更新：用户于下一轮回复“可以 下一步”，本批三图记为 USER_APPROVED_STATIC，覆盖以下初始待确认状态；静态批准不代表动态验证。

日期：2026-09-04。使用内置 imagegen；前两张为参考生成，轻触为观察图局部编辑。没有 CLI 或视频制作。

## 输出与审核

三张状态：STATIC_CANDIDATE / USER_REVIEW_PENDING；未取代既有大面罩比例基准，未加入猫身份白名单。

- [CHR_CAT_001_FIT_VISIONPRO_FRONT_v001.png](equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_FRONT_v001.png)；原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-c21bebcd-fd4d-4267-99a4-f52debead322.png`
- [CHR_CAT_001_VISIONPRO_TABLE_OBSERVE_v001.png](equipment_candidates/CHR_CAT_001_VISIONPRO_TABLE_OBSERVE_v001.png)；原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-f28e0e92-0176-4d75-9d10-48353cdc6aa2.png`
- [CHR_CAT_001_VISIONPRO_TABLE_TOUCH_v001.png](equipment_candidates/CHR_CAT_001_VISIONPRO_TABLE_TOUCH_v001.png)；原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-9ef60b57-53c2-40ac-aaa7-055a3bcbfa8f.png`

- 正面佩戴：正视头位、耳朵与鼻口露出，面罩覆盖眼部；后带在正面大部被头遮挡，不能由此图验证完整后脑路线。尺寸仍以原 3Q v001 为源，不将新图作为反向缩放依据。
- 桌面观察：裸脸看向设备，双前爪着地，设备银框／深灰面垫支撑桌面，后带形成连续环路。受透视影响，未量化验证同框绝对尺寸。
- 单爪轻触：一前爪触及近猫侧上缘，另一前爪及后躯支撑；设备位置、方向与观察图视觉接近，未见明显穿模或悬空。抬爪后肩部／头位略有变化，不能声称像素级保持或动作轨迹已验证。
- 三图均无电池、线缆、跨顶带、后置大圆盘；没有女主、服装或永久场景设计。
- MacBook 双爪 v003 根据用户在待确认图后的“ok 继续”记录为用户静态确认，不扩大到连续打字通过。

## 实际参考与提示词

### FRONT

输入顺序：

- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_IDENTITY_FRONT_SEATED_v001.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v001.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_LEFT_PROFILE_v004.png`

```text
Use case: photorealistic-natural
Single static reference for a cinematic series, landscape 16:9. Exact same fictional golden British Shorthair: round broad cheeks, gray-green eyes, pink nose, cream muzzle/chest, golden-apricot plush short fur, chubby compact body, short sturdy limbs, thick brown-gold tail tip. Neutral gray studio with matte gray tabletop supporting cat and prop; no table edge required, no permanent scene design. Soft neutral light, photorealistic fur, clear contact shadows. No human, clothes, laptop, text, watermark, extra limbs, human fingers or claws.
Fictional cat-adapted Vision Pro: large black curved visor, silver rim, charcoal face cushion, pale rigid side arms joining continuous gray rib-knit rear headband; no rear adjustment disc, no top strap, NO external battery or cable.
Image 1 locks cat identity and seated body; image 2 locks LARGE visor-to-head proportion; image 3 locks side arms and rear band routing. Generate a straight-on frontal seated cat wearing the same large headset, centered symmetrical head (not three-quarter). Match visor size of image 2, eyes covered, nose/muzzle and both ears fully visible. Headband passes below ear bases around back of skull, naturally hidden behind head in front view, no invented visible band across forehead. Full body, paws and tail visible with margins. Calm neutral seated posture. Preserve head volume and avoid squeezing cheeks or reducing visor.
```

### OBSERVE

输入顺序：

- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_IDENTITY_FRONT_SEATED_v001.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/equipment/EQP_VISIONPRO_CAT_001/candidates/EQP_VISIONPRO_CAT_001_DESIGN_3Q_v004.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v001.png`

```text
Use case: photorealistic-natural
Single static reference for a cinematic series, landscape 16:9. Exact same fictional golden British Shorthair: round broad cheeks, gray-green eyes, pink nose, cream muzzle/chest, golden-apricot plush short fur, chubby compact body, short sturdy limbs, thick brown-gold tail tip. Neutral gray studio with matte gray tabletop supporting cat and prop; no table edge required, no permanent scene design. Soft neutral light, photorealistic fur, clear contact shadows. No human, clothes, laptop, text, watermark, extra limbs, human fingers or claws.
Fictional cat-adapted Vision Pro: large black curved visor, silver rim, charcoal face cushion, pale rigid side arms joining continuous gray rib-knit rear headband; no rear adjustment disc, no top strap, NO external battery or cable.
Image 1 locks cat identity; image 2 locks standalone headset design; image 3 supplies ONLY headset-to-cat size, not wearing pose. Cat seated on left, bare face uncovered, looking down curiously at headset resting on same tabletop just to cat's right, within one paw reach. Both forepaws planted, no contact. Headset same physical scale as image 3, visor roughly face-width not body-width, no enlargement from foreground perspective. Headset faces camera in three-quarter view, rim/cushion stably contacting tabletop and closed loop rear band extends behind it, not floating. Cat and device approximately same depth plane. Medium-wide full body, slightly elevated three-quarter camera showing device band and clear gap from paws.
```

### TOUCH

输入顺序：

- `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-f28e0e92-0176-4d75-9d10-48353cdc6aa2.png`

```text
Use case: precise-object-edit
Input image is edit target and locks cat identity, body volume, headset size/design, device position, camera, gray tabletop and light. Change only cat's foreleg nearest the headset (image-right foreleg): lift and extend it naturally so the compact round furry paw gently touches the TOP LEFT SILVER RIM of the headset nearest the cat, with an unambiguous small contact shadow. Slight shoulder lean toward device allowed, short feline foreleg with coherent elbow and wrist, no elongation, no fingers or claws. Other forepaw remains planted on tabletop supporting cat; hindquarters and hind paws grounded. Preserve head identity and curious downward gaze. The headset must stay resting in EXACT same location and orientation, no tilt, collapse, floating or size change; preserve closed continuous rib-knit band, pale side arms, black glass, silver rim, no battery or cable. No paw through glass or extra paws. Whole cat and device in same 16:9 framing. This is light touch, not pushing or wearing.
```
