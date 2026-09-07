# 猫用设备设计候选 v001

日期：2026-09-04

## 生成方式

内置 imagegen，两个独立文本生成调用；没有输入参考图片。官方页面只用于区分真实产品资料与虚构设计，不声称已向模型输入官方产品图。模型版本、种子未提供，未编造。

## 来源及边界

- [Apple：MacBook Pro 16-inch 2024 技术规格](https://support.apple.com/en-gb/121554)：真实产品该尺寸列 M4 Pro/M4 Max；项目用户说 M4，不擅自替换芯片。候选只借用宽机身外形比例，虚构改装不对应零售 SKU。
- [Apple：Vision Pro 设置](https://support.apple.com/en-us/120144)：产品包含电池及连接线；猫用外形、头带路径、减重和尺寸全部属于本项目设计，不是官方规格。
- [Apple：头带拆装](https://support.apple.com/en-euro/118499)：真实产品头带有不同版本；本项目当前只采用灰色针织后带的候选视觉语言，不锁定真实代际。

## 输出与审核

| 路径（相对本目录） | 状态 | 审核 |
|---|---|---|
| `EQP_MACBOOKPRO_CAT_001/candidates/EQP_MACBOOKPRO_CAT_001_DESIGN_OPEN_3Q_v001.png` | CONCEPT_ONLY / NEEDS_CORRECTION | 轮廓和深色材质可讨论；键帽字符重复/错乱、侧面接口布局不可靠，不可作为键盘或接口结构母版 |
| `EQP_VISIONPRO_CAT_001/candidates/EQP_VISIONPRO_CAT_001_DESIGN_3Q_v001.png` | DESIGN_CANDIDATE | 面罩、后带、电池可见；连接点细节和侧臂功能件仍需明确，未检查实际猫头的耳根、脸颊、口鼻和佩戴稳定性 |

两图仅展示外观。没有比例标尺或猫同框，不能据此证明 25cm/14cm、合适猫咪操作或佩戴。不得用于证明真实产品安全性或可制造性。下一步先修正电脑结构，再做猫咪试配；需要时可将候选用于明确标记的试配探索，但不得因此晋升为正式设备母版。

原始输出：
- `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-40970778-d900-46cb-8c25-104d6f780548.png`
- `/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-f6cb9c70-5b4a-4200-916a-7094a8ba504f.png`

## 实际提示词

### EQP_MACBOOKPRO_CAT_001

```text
Use case: product-mockup
Asset type: first design candidate for a fictional cat-adapted M4-era MacBook Pro film prop, not a real Apple product or specification diagram.
Primary request: one photorealistic standalone miniature MacBook Pro inspired by the 2024 design, retaining the wide 16-inch-model chassis proportions but reduced to a proposed 25 cm body width for a large adult British Shorthair cat. Deep space-black anodized aluminum, thin flat rounded chassis, black keyboard well, conventional compact QWERTY keyboard with a function row and no numeric pad, symmetrical speaker grilles, generous centered trackpad, notched display. Preserve laptop recognizability, no whimsical paw-shaped keys or neon modifications.
Scene/backdrop: neutral light-gray seamless studio table, clean soft daylight-balanced product lighting, subtle realistic contact shadow.
Composition/framing: single front-left elevated three-quarter view, entire opened laptop visible with margin; display approximately 105 degrees relative to base. Show keyboard, trackpad, front lip and left edge. Screen off, black glass with subtle reflections, no desktop content.
Constraints: one device only, no cat, no person, no hands, no ruler, no text annotations, no watermark, no panels. Realistic metal and glass, straight aligned key rows, coherent hinge, physically grounded base. This isolated view communicates design only; absolute scale will be tested later with the approved cat reference.
```

### EQP_VISIONPRO_CAT_001

```text
Use case: product-mockup
Asset type: first design candidate for a fictional feline-adapted Apple Vision Pro film prop, not a commercial product or engineering drawing.
Primary request: a photorealistic cat-sized Vision Pro-inspired headset placed on a neutral studio surface, designed for a broad round British Shorthair head. Retain the recognizable curved dark laminated-glass front visor, thin silver aluminum surround, pale side arms, charcoal soft face cushion, and light-gray ribbed knitted rear band. The fictional adaptation has a shorter, wider feline face seal with a generous shallow muzzle clearance, side arms routed below the ear bases, a compact rear cradle and no over-the-crown strap so both ears can remain free. Proposed visor width 14 cm, not visually certified dimensions.
Include one small silver rounded-rectangular external battery beside the headset, joined by one continuous light-gray fabric-sheathed cable connected at the headset's wearer-left side arm; no loose unconnected cable, no extra battery or charger.
Composition/framing: one elevated front-left three-quarter product view showing the front visor, left arm and cable connector, the rear knit band visible behind; headset and full battery cable in frame. Neutral light-gray studio floor, soft neutral product lighting, restrained reflections and realistic contact shadows.
Constraints: no cat, people, mannequin, eyes rendered on glass, cartoon cat-ear decorations, crown strap, helmet, neon effects, labels, text, panels or watermark. This is an external concept only; actual ear and muzzle clearance must be checked in later cat fitting images.
```

