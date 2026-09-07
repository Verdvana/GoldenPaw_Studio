# 赛博工程师表演包 v001

日期：2026-09-04

## 生成与审核范围

使用内置 imagegen 工具，以批准身份图为参考生成；不涉及女主、双角色比例、设备或服装。未记录工具未提供的模型版本或随机种子。

本批状态 APPROVED_STATIC 仅代表人工视觉检查可用的静态表演参考，不替代身份母版，也不代表连续动作验证通过。表演标签是镜头意图，故障或解决问题的含义仍需剧情与剪辑建立。

## 输出清单

| 项目 | 项目内保存路径（相对角色目录） | 原始输出 |
|---|---|---|
| 技术专注 | `approved/expressions/CHR_CAT_001_EXPR_TECH_FOCUS_v001.png` | `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-1e3c6740-4f5a-4ffd-931f-6d807f2babee.png` |
| 故障困惑 | `approved/expressions/CHR_CAT_001_EXPR_FAULT_PUZZLED_v001.png` | `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-4beeb65b-8daa-42b6-b165-e9b274680d24.png` |
| 解决问题后的镇定 | `approved/expressions/CHR_CAT_001_EXPR_SOLVED_COMPOSED_v001.png` | `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-8d50cb54-62cf-47d3-833b-167373b20c34.png` |
| 食物期待（修正版） | `approved/expressions/CHR_CAT_001_EXPR_FOOD_ANTICIPATION_v002.png` | `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-6feaffcb-c3d3-402f-8f70-923f27d76b96.png` |
| 扑玩具前的低伏准备 | `approved/poses/CHR_CAT_001_POSE_HUNT_READY_v001.png` | `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-cd6c94b4-b7c7-4b0b-86d6-3d6982c5347c.png` |

## 审核备注

- 技术专注：降低视线与收窄眼睑，身份视觉一致，可作近景表演参考。
- 故障困惑：歪头幅度较提示词约 8 度更明显，接受为本张表演变化；不作为中性头位基准。
- 镇定：保持猫科自然表情，不以拟人微笑表达；是否解决问题取决于上下文。
- 食物期待：首版眼睛开度偏大、嘴微张，未纳入白名单；修正版降低偏差，可作仰视期待参考，眼睛大小仍以中性脸母版为准。
- 低伏准备：近侧肢体结构可辨，远侧后肢部分遮挡；只用于预备姿态，不可据此推定扑跳动作或关节轨迹已验证。
- 本轮未删除既有源文件。首版食物期待留在工具输出目录，不作为生产输入。

## 实际提示词与参考

前三张分别使用以下公共段落 + 对应请求段落（换行连接），参考路径相同。

参考：
- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/face/CHR_CAT_001_FACE_FRONT_NEUTRAL_v001.png`

公共段落：
```text
Use case: photorealistic-natural
Asset type: single static feline acting reference for a recurring cinematic series.
Input image: the approved neutral face is the authoritative identity reference, not an instruction to copy its expression.
Subject: the exact same fictional five-year-old male golden-shaded British Shorthair. Preserve broad round face, full cheeks, original eye size and gray-green irises, dusty pink nose, short cream muzzle, forehead markings, golden-apricot short plush fur.
Scene: neutral light-gray studio, identical soft daylight-balanced lighting and realistic fur detail.
Composition: frontal head and upper chest portrait, entire ears visible with margin, eye-level camera, matching perspective. One cat, no objects, devices, clothes, text, panels or watermark.
Expression rules: emotion through feline eyelids, ear orientation, gaze and small head angles only. No human eyebrows, smile, wrinkles, tears, speech, teeth or cartoon face. Keep skull and eye geometry unchanged. Mouth closed.

```

### TECH_FOCUS

```text
Primary request: intense but calm technical concentration. Chin lowered slightly, gaze fixed at an unseen point just below camera, eyelids modestly narrowed without angry brows, ears forward and still, whiskers subtly forward. Attentive and awake, not sleepy or aggressive.
```

### FAULT_PUZZLED

```text
Primary request: a small moment of puzzled investigation after an unexpected fault. Head tilted about eight degrees, gaze attentive toward camera, one ear rotates slightly outward while the other listens forward, eyes normally open. Curious uncertainty, not fear, sadness or comic bulging eyes.
```

### SOLVED_COMPOSED

```text
Primary request: quietly composed after solving a difficult problem. Head upright, gaze settled slightly to camera side, relaxed eyelids but fully awake, ears neutral upright, whiskers at rest. No grin, pride smirk or humanized expression; understated professional calm.
```

### FOOD_ANTICIPATION（首次生成）

参考：
- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/face/CHR_CAT_001_FACE_FRONT_NEUTRAL_v001.png`

```text
Use case: photorealistic-natural
Asset type: single static feline acting reference for a recurring cinematic series.
Input image: the approved neutral face is the authoritative identity reference, not an instruction to copy its expression.
Subject: the exact same fictional five-year-old male golden-shaded British Shorthair. Preserve broad round face, full cheeks, original eye size and gray-green irises, dusty pink nose, short cream muzzle, forehead markings, golden-apricot short plush fur.
Scene: neutral light-gray studio, identical soft daylight-balanced lighting and realistic fur detail.
Composition: frontal head and upper chest portrait, entire ears visible with margin, eye-level camera, matching perspective. One cat, no objects, devices, clothes, text, panels or watermark.
Expression rules: emotion through feline eyelids, ear orientation, gaze and small head angles only. No human eyebrows, smile, wrinkles, tears, speech, teeth or cartoon face. Keep skull and eye geometry unchanged. Mouth closed.
Primary request: eager food anticipation toward an unseen fish treat held just above camera. Nose slightly lifted, gaze upward, ears forward, whiskers forward, eyes attentive with subtly enlarged pupils while original eyeball size remains unchanged. Mouth closed; no drool, tongue, teeth, fish or other object in frame. Restrained realistic feline eagerness, not a human smile.
```

### HUNT_READY（首次生成）

参考：
- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_IDENTITY_FRONT_STANDING_v001.png`
- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/CHR_CAT_001_TURN_FRONT_LEFT_3Q_STANDING_v001.png`

```text
Use case: photorealistic-natural
Asset type: single full-body feline hunting-preparation static reference.
Input images: Image 1 is authoritative facial and coat identity; Image 2 is three-quarter body structure.
Subject: exact same five-year-old male golden-shaded British Shorthair, broad round face, gray-green eyes, pink nose, cream muzzle/chest, golden-apricot short plush fur, compact chubby torso, short sturdy legs, thick brown-gold-tipped tail.
Primary request: low playful stalking crouch toward an unseen colorful wool ball just outside frame to camera-left. Front paws grounded and slightly staggered, chest lowered, hind legs flexed beneath broad hips ready to spring, ears forward, attentive eyes, tail low behind. Both hindquarters and all four limb chains anatomically coherent; natural occlusion allowed.
Scene: neutral gray studio floor, soft neutral daylight, realistic contact shadows. Photorealistic diagnostic full-body landscape view from front-left three-quarter at cat eye level, complete ears and tail visible.
No ball or props in frame, no people, equipment, clothing, text, watermark, panels, extra limbs, fused paws, long legs, black tail tip or human/cartoon expression. This is a pre-pounce pose, not an airborne jump.
```

### FOOD_ANTICIPATION 修正

参考：
- `/Users/verdvana/Project/GoldenPaw_Studio/library/characters/CHR_CAT_001/approved/face/CHR_CAT_001_FACE_FRONT_NEUTRAL_v001.png`
- `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-283cc9ca-8845-4996-bf34-242da84f249f.png`

```text
Use case: identity-preserve
Input images: Image 1 is the approved facial identity and eye-proportion reference; Image 2 is the food-anticipation image to correct.
Change only Image 2's excessive eye opening/eyeball size and slightly parted mouth. Restore original eye geometry from Image 1, moderately alert eyelids, same gray-green irises, and a naturally fully closed feline mouth with no visible mouth cavity. Keep Image 2's upward head tilt, upward gaze, pink nose, face width, ears, fur colors, lighting and composition unchanged. Convey eager attention through gaze and forward whiskers, not enlarged cartoon eyes. No other edits, props, text or watermark.
```

