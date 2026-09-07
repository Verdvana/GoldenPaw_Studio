# 猫咪运动与休息资产：提示词与审核

落地最新修正版为 `candidates/CHR_CAT_001_POSE_LAND_LEFT_v002.png`，前肢压缩与后腿收折已改善，仍为候选待确认；详见 [修订审核](landing_revision_v002.md)。以下 LAND_LEFT 为首版历史记录。

生成方式：内置 image_gen，每个资产独立调用。以下通用提示词加各项变量为实际提交的完整提示词；输入文件如下。模型版本、种子和参考权重未由工具返回，不作推断。

## 输入参考

- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_IDENTITY_FRONT_STANDING_v001.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_TURN_LEFT_PROFILE_STANDING_v001.png`

## 通用提示词

```text
Use case: photorealistic-natural
Asset type: single feline pose reference, not a multi-panel sheet.
Input images: Image 1 is the authoritative face/coat identity reference; Image 2 is the body-proportion reference. Generate a new view of this exact same fictional five-year-old male golden-shaded British Shorthair.
Identity: broad round face and cheeks, gray-green eyes, dusty-pink nose, cream muzzle/throat/chest, warm golden-apricot plush short fur, subtle dark-golden shading, compact chubby adult torso, short sturdy limbs, thick tail with brown-gold tip, never black.
Scene: seamless neutral light-gray studio floor, neutral soft daylight, realistic contact shadows. Photorealistic animal photography with sharp diagnostic detail.
Composition: landscape single full-body image with generous margins, all ears and complete tail visible. No props, people, clothes, collars, devices, text or watermark.
Anatomy: exactly four coherent feline limbs, realistic joints and weight; natural occlusion allowed, do not invent extra paws to expose hidden limbs. No human expression, cartoon, long legs, slim torso or identity drift.
```

## STRETCH

```text
Primary request: natural waking forward stretch, in left-facing side profile. Both front paws extended on the floor, chest lowered, hips raised, hind paws planted, spine naturally arched through the stretch, tail relaxed. Four limb chains remain coherent. Calm closed mouth.
```

## CURLED_SLEEP

```text
Primary request: comfortably curled sleeping cat seen from a slightly elevated three-quarter view. Broad body curled into a compact oval, eyes fully closed, nose near tucked forepaws, tail wrapped around the outside without merging into paws, relaxed ears and realistic compressed fur. No exposed belly pose.
```

## RUN_LEFT

```text
Primary request: left-facing natural running bound, exact side view. Capture the compact gathered phase of a feline gallop: spine gently flexed, rear legs coming forward beneath hips, forelegs gathering beneath chest, paws subtly staggered and readable. Cat is just above the floor with a close coherent shadow, tail extended for balance. Short-exposure sharp action photo, no motion blur or speed lines.
```

## JUMP_TAKEOFF_LEFT

```text
Primary request: left-facing small forward-upward jump TAKEOFF, exact side view. Hind paws are still pushing against the floor with hind limbs extending naturally; front paws have left the floor and reach forward, chest rising diagonally. Realistic heavy adult cat, modest height, tail behind for balance. Clearly show floor contact at the rear paws. Sharp action photo.
```

## LAND_LEFT

```text
Primary request: left-facing small-jump LANDING, exact side view. Front paws make first floor contact slightly staggered, wrists and elbows flex naturally to absorb weight, head aligned with spine; hindquarters remain slightly raised with hind paws approaching the floor behind. Tail counterbalances. Realistic modest jump, no crash, no twisted joints. Sharp action photo.
```

## 审核结论

- STRETCH：静态参考通过；前后爪着地、躯干弯曲及尾巴可读。
- CURLED_SLEEP：静态参考通过；自然遮挡允许，不用此图推断隐藏肢体结构。
- RUN_LEFT：候选；远侧后肢被遮挡，尚无连续步态验证。
- JUMP_TAKEOFF_LEFT：候选；后爪接地可读，尚需验证蹬地到腾空的重量和衔接。
- LAND_LEFT：候选；前爪接地，但前肢缓冲偏僵硬，应先修正或完成连续视频测试后再批准。

本批是独立姿态，不是同一个跳跃的连续首尾帧。不得直接当作已匹配的跳跃序列。女主比例与双角色互动继续暂缓。
