# 女主 L1 Canon 资产生成总规格

```yaml
document_id: OWNER_L1_GENERATION_SPEC
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.50
status: DRAFT
authority: USER_APPROVAL_REQUIRED
default_aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
created_at: "2026-09-09"
```

本文件是女主 `owner_v1.0` 全部 L1 候选资产的统一生成规格。任何新对话、代理或生成批次在制作女主 L1 前，必须完整读取本文件、当前工作版 `IDENTITY.md`、所选 Reference Set 及相关素材规则。不得凭上一次对话记忆自行补全规则。

本文件定义“生成什么、如何生成、什么不能改变”。它不代表任何图片已获批准，也不授权一次性批量生成。

---

## 1. 层级与权威关系

### 1.1 L0 与 L1

- L0：真实人物照片，永不由 AI 生成，永不被 AI 图片替代。
- L1 Candidate：依据 L0、工作版 `IDENTITY.md` 和本规格生成的候选图片。
- L1 Approved：经用户明确批准、通过 QA、写入审批记录的单项资产。
- L1 Locked Canon：全部必要组件通过 Gate 8 后写入 `canon/versions/owner_v1.0/` 并锁定。

禁止把生成图片重新登记成 L0。生成结果也不得自动升级为 L1。

### 1.2 身份决策来源

女主 L1 候选由以下信息共同决定，优先级从高到低：

1. 用户最新明确决定；
2. 当前工作版 `IDENTITY.md`；
3. 按职责选择的 L0 真人照片；
4. 已批准的同级属性 Canon；
5. 本文件的中性校准规则。

未经批准的 AI 图片不能决定身份。AI 候选只能暴露问题，不能自行成为新的身份事实。

### 1.3 `IDENTITY.md` 生命周期

计划工作文件：

`characters/CHR_HUMAN_001_OWNER/canon/IDENTITY.md`

其流程为：

```text
L0 跨照片分析
  -> IDENTITY.md（DRAFT）
  -> 单项候选生成
  -> 用户指出保留/调整事项
  -> 人工更新 IDENTITY.md 修订号
  -> 继续下一候选
  -> 用户批准最终身份
  -> 复制到 canon/versions/owner_v1.0/IDENTITY.md
  -> 记录校验值并 LOCKED
```

允许根据用户反馈逐步调整工作版文字；不得因为某张 AI 图看起来不错就自动把其光照、皮肤、妆容、脸型伪影或身体比例写回 `IDENTITY.md`。锁定后不再编辑 `owner_v1.0/IDENTITY.md`；变更建立 `owner_v1.1` 或 `owner_v2.0`。

---

## 2. 全局视觉标准

### 2.1 文件与画幅

- 所有单张权威参考统一为 3:4 竖幅。
- 推荐输出尺寸：1536×2048；若工具不支持，使用最接近的原生 3:4 尺寸。
- 禁止拉伸非 3:4 图片来伪造比例。
- 一个文件只展示一个角度、一个姿态或一个表情。
- 不用多视角拼图作为主要权威图片；Character Sheet 只能是便于浏览的派生索引。
- 候选优先保存为无损 PNG；若工具只输出 JPEG，则保留原始输出，不反复转码。
- 每张图片必须有同名 metadata 和 generation record。

当前五个 Face 组件均已批准，并已由用户从批准 PNG 转码为 JPG，以降低后续传输量；索引文件记录各自当前 JPG 路径和校验值。候选 PNG 继续作为生成与批准溯源。格式转换不等于重新生成或重新批准，也不得把批准 JPG 或候选 PNG 用于同一属性的 L1 串图恢复。统一查找入口为 `canon/face/FACE_CANON_INDEX.md`。

现有发型 B 候选为 1086×1448，比例正好为 3:4，保持原文件不变。

### 2.2 统一中性风格

- photorealistic / photographic realism；
- 中性浅灰或灰白无缝影棚背景；
- 中性白平衡，约 5200–5600K；
- 大面积柔光，低对比度，面部和身体阴影结构清晰但不过度；
- 不使用戏剧性侧光、彩色环境光、逆光光斑、霓虹、强高光或电影调色；
- 不使用美颜滤镜、过度磨皮、塑料皮肤、夸张锐化；
- 不继承 L0 照片中的婚纱棚拍风格、户外背景、广告文字或手机自拍透视；
- 不继承任何上一张 AI 候选的背景、明暗斑块或渲染伪影。

### 2.3 镜头规则

| 资产类型 | 建议等效焦段 | 相机高度 | 构图 |
|---|---:|---|---|
| Face / Expression | 85–105mm | 眼睛高度 | 头顶至上胸，头部约占画面高度 65–72% |
| Hair | 85–105mm | 眼睛高度 | 头顶至胸部，头发边缘完整 |
| Body / Pose | 70–85mm | 腰部至下胸之间 | 头顶和脚底完整，上下各留约 5–8% |
| Hosiery / Feet | 70–100mm | 与目标区域近似平齐 | 需要检查的脚踝、脚跟、脚背、脚趾全部完整 |

相机保持水平，禁止用广角、低机位或高机位人为改变头身比、腿长、脚大小和脸型。除非资产名称明确要求转面，人物相对相机距离和画面占比保持一致。

正面 Face 的“平视”必须同时满足：

- 相机光心与人物双眼中心在同一水平高度；
- 镜头光轴水平并近似垂直于面部正面平面；
- 人物头部保持中立，不仰头、不低头，下巴不前伸或回收；
- Frankfort horizontal plane（耳孔上缘至眼眶下缘的解剖水平参考）近似水平；
- 不因参考图俯视而显示过多头顶，不因人物仰视而压缩额头或抬高下巴；
- 双眼、眉毛、耳朵高度关系和鼻唇投影呈标准眼平证件照透视。
- 平视约束必须覆盖整颗头颅，而不只是眼睛视线：脸部、额头、发际线、头盖骨、头顶轮廓、耳位与下颌必须共享同一个水平投影；不得出现“眼睛平视但头顶仍被俯拍”的混合透视。
- 正面平视时只自然显示很少的前部头顶曲面；禁止从上方可见的大面积椭圆头盖面、向后延伸过长的头皮分缝或被压低的发际—头顶关系。
- 对 `FACE_01_FRONT_NEUTRAL`，发际线至头顶最高点的可见区域应主要表现为正面轮廓高度，而不是水平头皮表面积；中央分缝在额前短距离内消失，不得一路向后展示至头冠。
- 若含俯视偏差的身份锚持续污染头顶，可使用该锚的无调色像素裁切，仅保留脸与肤色区域并排除头顶；裁切属于可追溯输入派生物，不是新 Canon，也不得覆盖原图。
- 允许在候选生成时采用轻微反向机位补偿（相机低于瞳孔中心约 2–3 cm、光轴上仰约 1–2°），其目的仅是抵消参考图俯视偏差；最终画面仍必须视觉上呈中性平视，不得呈明显仰拍。
- 若发型 L0 照片中的脸造成身份混合，可制作不调色、不缩放的面部遮蔽派生图；遮蔽图只传递头发像素，遮蔽区域不得被解释为造型、头型、颜色或背景设计，并必须保留来源与处理记录。
- 身份裁切可以做常规非 AI 插值放大以提高输入权重，但不得锐化、补细节、修脸或调色；放大图不增加权威，仅继承原裁切的职责，并记录算法、尺寸和校验值。

### 2.4 全局身份负面约束

- 不是泛化的东亚女性，也不是根据某一张精修照重新设计的人；
- 不改变头骨宽长关系、下颌、下巴、颧骨、额头、眼距、鼻子、嘴唇和耳朵关系；
- 不擅自瘦脸、放大眼睛、缩鼻、尖下巴或改变年龄；
- 不让不同角度看起来像不同的人；
- 不让表情重新定义身份；
- 不让发型参考图重新定义脸、身体或皮肤；
- 不让衣服重新定义胸腰胯和腿部比例；
- 不从 Previous Shot 或其他 AI 候选复制灯光、阴影、背景和皮肤斑块。

### 2.5 全局 Calibration Outfit 规则

Calibration Outfit 不只用于 Gate 3。女主当前 `owner_v1.0` 的任何 L1 候选，只要画面中出现衣服，就必须使用同一套：

```text
粉色高叉连体泳衣
+ 15D 天鹅绒质感连裤丝袜
+ 无鞋
```

按构图执行：

- Face / Hair / Expression 头肩或胸像：显示到衣服时，只显示同一粉色连体泳衣的真实上半部分；不得换成背心、礼服、针织衫或其他粉色衣物；
- Body / Pose：完整穿着同一泳衣、15D 丝袜和无鞋状态；
- Hosiery / Feet：即使泳衣在画外，也必须视为仍穿完整 Calibration Outfit；
- Appearance：只要出现服装，同样使用 Calibration Outfit；
- 服装只负责校准和跨资产视觉一致性，不代表 Episode 剧情服装；
- L0 发型参考中的粉色外套、针织衫或其他衣物永远不得进入 L1。

### 2.6 全局发型选择规则

- 除专门生成 `HAIRSTYLE_B` 的资产外，女主所有 L1 资产只要头发可见，统一使用 `HAIRSTYLE_A`；
- Face、Body、Expression、Pose、Appearance 以及包含头部的 Hosiery/Feet 图均使用 A；
- 不再使用 `CALIBRATION_HAIR` 或其他临时第三发型；
- 仅 `HAIR_B_*` 及明确标记为 HAIRSTYLE_B 专属的资产使用 B；
- A 的 L0 权威参考为 `DSC00847.jpg`，B 的 L0 权威参考为 `8.jpg`；
- 用户指定的 B 图 L1 资产同时作为正脸长相与肤色锚，但在非 B 发型资产中只传递脸和肤色，不传递 B 发型。

---

## 3. 每次生成前的固定输入合同

每一次 L1 候选生成必须建立 Generation Record，并明确列出：

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.3
identity_md_revision: "draft_0.3 or later"
asset_id: ""
gate: ""
reference_set_ids: []
authoritative_for: []
must_not_define: []
aspect_ratio: "3:4"
resolution: "1536x2048"
approval_status: REVIEW_REQUIRED
```

### 默认 Reference Budget

- L0/L1 Face Identity：1–2 张；
- Body Canon：0–1 张；
- Hairstyle：0–1 张；
- Outfit：0–1 张；
- Hosiery Material：0–1 张，足部缺失时最多补第 2 张；
- Previous AI Candidate：默认 0 张；
- 总图片数：通常不超过 5 张，绝对上限遵循项目 8 张预算。

生成下一角度时不得默认引用上一张候选。每张候选都重新从 L0/L1 Master Assets 和文字规格平行生成。

---

## 4. Gate 1 — L0 与 Identity 准备

本 Gate 不生成图片。

完成条件：

- L0 真人照片已登记；
- 使用 `registries/reference_sets.yaml`，不每次加载全部照片；
- 完成工作版 `IDENTITY.md`；
- 将跨照片稳定特征与受妆容、镜头、光照影响的特征分开；
- 用户确认允许的脸型和身体轻微调整方向；
- `IDENTITY.md` 具有修订号和状态 `DRAFT`。

Gate 1 未完成时不得生成 Face Canon 候选。

---

## 5. Gate 2 — Face Identity Canon

### 5.1 资产清单

| Asset ID | 视角 | 表情 | 推荐 L0 Reference Set |
|---|---|---|---|
| FACE_01_FRONT_NEUTRAL | 标准正面 | neutral | `OWNER_FACE_APPEARANCE_L1` + `OWNER_HAIRSTYLE_A_L0` |
| FACE_02_LEFT_3Q_NEUTRAL | 人物左侧 3/4 | neutral | 使用最匹配的已登记 3/4 图并记录画面方向 |
| FACE_03_RIGHT_3Q_NEUTRAL | 人物右侧 3/4，鼻尖朝画面右 | neutral | `OWNER_L0_FACE_RIGHT_3Q_LIMITED`；仅提供方向与真人右侧自然差异，精细身份以批准的 FACE_01 + IDENTITY 为准 |
| FACE_04_LEFT_PROFILE_NEUTRAL | 人物左侧面，鼻尖朝画面右 | neutral | 用户授权的受限重建：批准 FACE_01 + `OWNER_L0_FACE_RIGHT_3Q_LIMITED` + 遮脸 HAIRSTYLE_A；不得镜像或引用其他生成角度 |
| FACE_05_RIGHT_PROFILE_NEUTRAL | 人物右侧面 | neutral | `OWNER_L0_FACE_PROFILE_IMAGE_LEFT` 对应的真实可见侧面 |

最终元数据必须同时记录 anatomical side 和 `face_points_image_left/right`，避免左右命名歧义。

`FACE_01_FRONT_NEUTRAL` 当前已批准组件为 `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`。下游正面身份引用使用 `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`；若需要重新制作该 L1 Master，必须使用 `OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1` 和 `canon/face/FACE_01_FRONT_NEUTRAL_METHOD.md`，不得把已生成 Canon 图串联成新的 L1。

`FACE_02_LEFT_3Q_NEUTRAL` 当前已批准组件为 `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001`。方向固定为人物 anatomical left facial plane principally visible、鼻尖朝画面左。普通下游左 3/4 身份引用使用 `OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1`；若需要重新制作该 L1 Master，必须使用 `OWNER_FACE_LEFT_3Q_NEUTRAL_RECOVERY_V1` 和 `canon/face/FACE_02_LEFT_3Q_NEUTRAL_METHOD.md`，严格恢复 v001 提示结构并仅保留已批准的颧骨/下巴/眼神三项短约束。不得把 v001–v004 或批准图作为新的 L1 像素输入。

`FACE_03_RIGHT_3Q_NEUTRAL` 当前已批准组件为 `OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001`。方向固定为人物 anatomical right facial plane principally visible、鼻尖朝画面右。普通下游右 3/4 身份引用使用 `OWNER_FACE_RIGHT_3Q_NEUTRAL_CANON_L1`；若需要重新制作该 L1 Master，必须使用 `OWNER_FACE_RIGHT_3Q_NEUTRAL_RECOVERY_V1` 和 `canon/face/FACE_03_RIGHT_3Q_NEUTRAL_METHOD.md`，保持固定三输入顺序与 v002 的下巴底部圆润约束。不得镜像 FACE_02，也不得把 FACE_03 v001、v002 或批准图作为新的 L1 像素输入。

`FACE_04_LEFT_PROFILE_NEUTRAL` 当前已批准组件为 `OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001`，当前下游文件为用户转码的 JPG。方向固定为人物 anatomical left facial plane visible、鼻尖朝画面右。它是在缺少同方向标准真人侧脸 L0 的条件下由用户审核批准的受限重建：普通下游左侧面身份引用使用 `OWNER_FACE_LEFT_PROFILE_NEUTRAL_CANON_L1`；重新制作该 L1 Master 必须使用 `OWNER_FACE_LEFT_PROFILE_NEUTRAL_RECOVERY_V1` 和 `canon/face/FACE_04_LEFT_PROFILE_NEUTRAL_METHOD.md`。固定输入顺序为批准 FACE_01 JPG、只负责同侧方向/自然差异/粗略深度的 `14.jpg`、只负责发型的遮脸 HAIRSTYLE_A。不得使用本批准 JPG 或候选 PNG 重新生成，不得使用或镜像 FACE_05，也不得引用 FACE_03、其他生成角度或历史候选。其批准范围包括用户接受的生成侧面轮廓，但方法文档必须永久保留“无同方向真人纯侧脸验证”的证据限制。

`FACE_05_RIGHT_PROFILE_NEUTRAL` 当前已批准组件为 `OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001`。方向固定为人物 anatomical right facial plane visible、鼻尖朝画面左。普通下游右侧面身份引用使用 `OWNER_FACE_RIGHT_PROFILE_NEUTRAL_CANON_L1`；重新制作该 L1 Master 必须使用 `OWNER_FACE_RIGHT_PROFILE_NEUTRAL_RECOVERY_V1` 和 `canon/face/FACE_05_RIGHT_PROFILE_NEUTRAL_METHOD.md`，保持固定三输入顺序与已批准的轻微缩小鼻尖体量/突出度约束。不得使用 v001、v002、批准图、其他生成角度或镜像作为新的 L1 像素输入。

### 5.2 Face 固定规则

- 中性、自然闭嘴表情；
- 最少妆容；
- 眼睛看向镜头，侧面图自然平视；
- 使用 `HAIRSTYLE_A`；其长度、分缝、直发质感和脸侧关系由 `DSC00847.jpg` 负责；
- 耳朵、下颌边缘、额头和发际关系尽量可见；
- 五张保持相同头部尺寸、镜头、灯光和皮肤处理；
- Face 图片只负责身份几何，不负责最终发型、服装、身体和背景。

### 5.3 Face QA

逐对比较五张图：同一头骨、眼距、眉形、鼻子、嘴唇、下颌和耳朵。任一角度明显像另一个人，整张拒绝；不得用局部修补后的失败图继续繁殖。

五张分别批准后才能进入 Gate 3。

不新增 `FACE_06_BACK_OF_HEAD`。后脑视角不包含脸部几何，若放入 Face Canon 会混淆身份与发型职责；完整背面头部朝向和身体比例由 `BODY_06_BACK` 负责，后脑轮廓、后颈、发量和发型结构分别由 `HAIR_A_04_BACK` 与 `HAIR_B_04_BACK` 负责。若未来出现剃发、极短发或需要独立验证裸露后脑/耳后结构的新设计，再单独建立 scoped Head Anatomy 资产，而不是扩充当前 Face Canon。

---

## 6. Gate 3 — Body Canon

### 6.1 Calibration Outfit

所有 Body Canon 统一：

```text
粉色高叉连体泳衣
+ 15D 天鹅绒质感连裤丝袜
+ 无鞋
```

这是身体校准着装，不是剧情默认服装。

### 6.2 资产清单

| Asset ID | 视角/要求 |
|---|---|
| BODY_01_FRONT | 正面自然站立，双臂自然，双脚不交叉 |
| BODY_02_LEFT_3Q | 左 3/4，保持相同站姿基准 |
| BODY_03_RIGHT_3Q | 右 3/4，保持相同站姿基准 |
| BODY_04_LEFT_SIDE | 完整左侧，身体不扭转 |
| BODY_05_RIGHT_SIDE | 完整右侧，身体不扭转 |
| BODY_06_BACK | 完整背面，头部和身体朝向一致 |

### 6.3 Body 固定规则

- 使用已批准 Face Canon，而不是某张全身 L0 的脸；
- 用户确认的现实身体基准为身高 `168 cm`、体重约 `60 kg`（120 斤）。Body 候选必须呈现与 168 cm 成年女性相符的偏高身高感和自然 60 kg 体量，不能回落成约 160 cm 的较矮视觉比例，也不能通过广角、低机位、缩头或不自然拉伸伪造身高；
- L0 全身照片只能提供身体上下文，最终比例由 `IDENTITY.md`、用户调整决定和当前 Body Candidate Brief 共同确定；
- 锁定头身比、肩宽、胸腰胯关系、躯干长度、腰线、臀胯轮廓、臂长、腿长、大腿/小腿关系及足部比例；
- 六张使用相同身体，不因转面改变胸围、腰围、臀围、腿粗和身高；
- 手指和脚趾自然，不依赖鞋履遮挡错误；
- 正面小腿须在自然肌肉体量下保持膝—胫骨—踝关节轴线竖直、左右对称；避免胫骨向外弯、腓肠肌外轮廓造成 O 形腿观感或脚踝向内/向外偏移；
- 校准丝袜必须连续覆盖到脚趾，但丝袜精细材质最终由 Gate 7 决定。

`BODY_01_FRONT_v001` 是 Gate 3 的首张基准候选。固定最小参考职责为：批准 FACE_01 只定义正面脸部身份；`OWNER_L0_BODY_FRONT_CONTEXT` 中的 `3.jpg` 与 `4.jpg` 只交叉提供真实身高感、头身比、肩宽、躯干/腰胯、四肢长度和自然体型范围；遮脸 Hairstyle A 只定义头发。15D nude velvet/matte sheer textile 本轮只由 `CALIBRATION_OUTFIT.md` 与 `docs/qa/hosiery_material_rules.md` 的文字合同定义，不附带带床景/广告文字的材质照片；精细丝袜权威仍留给 Gate 7。L0 衣服、鞋、走路姿势、手持物、背景、脸、腿部塑形和丝袜颜色偏差均不得进入候选。用户尚未指定主动身材改造，因此 v001 采用跨两张真人全身照的保守自然中间值，禁止瘦身、增高、拉腿、夸张胸腰臀或塑造成通用模特身材。画面必须明确为成年角色的非性感、技术性比例校准照。

`BODY_01_FRONT_v009` 已由用户明确批准为当前活动正面 Body L1 Canon 组件 `OWNER_BODY_01_FRONT_CANON_002`，取代旧活动组件 001。普通 L2/L3 正面身体引用使用更新后的 `OWNER_BODY_FRONT_CANON_L1`；如需重新制作该 L1 Master，必须使用 `OWNER_BODY_FRONT_RECOVERY_V1` 和 `canon/body/BODY_01_FRONT_METHOD.md`，从批准 FACE_01、两张 L0 身体上下文与遮脸 Hairstyle A 按固定顺序平行重建。不得使用 v001–v009、任一批准 Body Master 或任何其他生成身体图作为新 L1 像素输入。批准范围包括用户确认的 168 cm / 60 kg 正面身体比例、四肢比例、腰臀比、腿脚几何与中性站姿，以及本资产中获确认的可见脸、发型和腿脚丝袜表现；独立 Face/Hair Canon 与可复用精细丝袜 Material Canon 仍由各自组件/Gate 负责。

组件 002 的下游职责经用户进一步明确：生成其他角色资产和视频镜头所需图片时，可引用其中获批的 168 cm / 60 kg、可见长相、`HAIRSTYLE_A`、四肢比例及腰臀比；若任务需要不同脸部/发型视角或更精细权威，仍选择对应的专用 Face/Hair Canon。该图中的丝袜只可定义 `15D + 哑光 + 肉色` 三项组合外观；任何其他颜色、材质/光泽或厚度必须排除本图的丝袜职责并另选对应 Material Reference。

六张分别批准后才能进入 Gate 4。

---

## 7. Gate 4 — Hairstyle Canon

### 7.1 HAIRSTYLE_A

| Asset ID | 视角 |
|---|---|
| HAIR_A_01_FRONT | 标准正面 |
| HAIR_A_02_3Q | 最能说明轮廓和脸侧关系的 3/4 |
| HAIR_A_03_SIDE | 标准侧面 |
| HAIR_A_04_BACK | 完整背面结构 |
| HAIR_A_05_HIGH_CAMERA_LOOK_UP | 镜头高于人物并向下拍摄、人物抬头看向镜头；验证发际线、头顶、分缝、脸侧发束和抬头时的发型投影 |
| HAIR_A_06_LOW_CAMERA_LOOK_DOWN | 镜头低于人物并向上拍摄、人物低头看向镜头；验证下颌侧发束、耳侧、发尾遮挡和低机位下的头发投影 |

HAIRSTYLE_A 的主 L0 参考固定为 `OWNER_HAIRSTYLE_A_L0`，即 `DSC00847.jpg`。它定义长直披发、中央附近分缝、自然贴顺的低至中等顶部体积、长脸侧发束、胸部以下长度及自然渐细发尾。户外色偏、高光、脸、身体、粉色外套和背景不得进入 Canon。缺失的侧面和背面依据文字定义 + 已批准 Face Canon 平行生成，不得使用上一张 A 候选连续繁殖。

### 7.2 HAIRSTYLE_B

现有候选：

`OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001` — `CHR_WOMAN_001_HB04_HAIR_B.jpg`

HAIRSTYLE_B 的主 L0 真人参考固定为 `OWNER_HAIRSTYLE_B_L0`，即 `8.jpg`。它负责真实发际关系、向后收拢的前部结构、脸侧自然碎发、盘发方向和正面体积；惊讶表情、针织衫、暖色灯光、背景、脸和身体均不具权威性。

现有 AI 候选保持 3:4 原图，不覆盖。经用户明确批准后，仅作为 B 的最终设计补充，定义分缝、平顺收拢/发髻结构、头顶受控蓬松度、脸侧碎发、深棕色及克制高光。

该现有批准图同时履行 `HAIR_B_05_HIGH_CAMERA_LOOK_UP` 专项视角槽位：镜头俯视、人物仰视。它不替代标准眼平正面 `HAIR_B_01_FRONT`，也不因此取得身体、服装、灯光或背景权威；不再为相同 B 高机位视角生成重复 Canon 文件。

需要补齐：

| Asset ID | 视角 |
|---|---|
| HAIR_B_01_FRONT | 标准眼平正面，不沿用原图俯拍透视 |
| HAIR_B_02_3Q | 3/4，说明脸侧碎发和发髻位置 |
| HAIR_B_03_SIDE | 侧面，说明发际线、耳侧和发髻深度 |
| HAIR_B_04_BACK | 背面，说明盘发完整结构 |
| HAIR_B_05_HIGH_CAMERA_LOOK_UP | 已由 `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001` 履行；镜头俯视、人物仰视，不重复生成 |
| HAIR_B_06_LOW_CAMERA_LOOK_DOWN | 镜头仰视、人物俯视；验证下颌/耳侧碎发、收拢方向及发髻在低机位下的结构 |

所有新角度必须使用批准后的 Face Canon + B 的 L0 真人锚 + 经批准的 B 设计锚；不得仅以 B 的 AI 图片连续繁殖。参考图中的脸、身体、衣服、灯光和皮肤均不具发型以外的权威性。

### 7.3 发型通用规则

- 正式 Shot 只能选择 `HAIRSTYLE_A` 或 `HAIRSTYLE_B`；
- 不融合 A/B，不自动创造第三种长期发型；
- 每张 Hair Canon 只负责头发；
- 标准四视角与两个高低机位专项视角必须具有一致长度、体积、分缝、卷度、发际关系、耳侧关系、背面结构和高光行为；专项视角只验证透视/头部俯仰下的发型响应，不重新定义脸部身份。

---

## 8. Gate 5 — Expression Canon

| Asset ID | 表情定义 |
|---|---|
| EXP_01_NEUTRAL | 中性 |
| EXP_02_SUBTLE_SMILE | 嘴角轻微上扬 |
| EXP_03_NATURAL_SMILE | 自然微笑，不必露齿 |
| EXP_04_SMILE_WITH_TEETH | 自然露齿笑 |
| EXP_05_HAPPY_LAUGHING | 开心大笑 |
| EXP_06_SURPRISED | 自然惊讶，不夸张变形 |
| EXP_07_CONFUSED_CURIOUS | 困惑/好奇 |
| EXP_08_MILDLY_ANNOYED | 轻微不悦 |
| EXP_09_SAD_CONCERNED | 难过/担忧 |
| EXP_10_FOCUSED_SERIOUS | 专注/认真 |
| EXP_11_ANGRY | 明确愤怒；眉间、眼睑和口周产生自然张力，但不夸张成漫画式暴怒，不改变脸型 |
| EXP_12_SHY | 害羞；目光轻微回避或下移、克制的小表情，可有自然轻微泛红但不得永久改变肤色 |
| EXP_13_SLIGHT_FROWN | 轻微皱眉；眉间和眉头小幅收紧，保持嘴部与其他五官中性 |
| EXP_14_EYES_CLOSED | 自然闭眼；双眼轻闭、不挤压面颊、不改变眉形或头骨关系 |
| EXP_15_MOUTH_SLIGHTLY_OPEN | 嘴唇自然微张；下颌只做极小幅度开启，不夸张露齿、不改变嘴唇或下巴几何 |

规则：

- 使用批准后的 Face Canon；
- 统一正面或轻微 3/4 的头肩构图；
- 默认选择一个已批准发型并保持十五张一致；
- L0 表情照片只定义肌肉和软组织变化；
- 允许眼睑、嘴角、面颊和眉毛自然运动；
- 不允许头骨、鼻子、眼距、下颌、耳朵或年龄变化。

---

## 9. Gate 6 — Body / Pose Canon

| Asset ID | 姿态定义 |
|---|---|
| POSE_01_RELAXED_STANDING | 放松站立 |
| POSE_02_WALKING_NEUTRAL_STRIDE | 自然行走中步态 |
| POSE_03_SEATED_UPRIGHT | 坐姿挺直 |
| POSE_04_SEATED_RELAXED | 放松坐姿 |
| POSE_05_SLIGHT_BODY_TURN | 轻微转身 |
| POSE_06_BENDING_REACHING | 自然弯身/伸手；列为必需 |
| POSE_07_KNEELING_CROUCHING | 跪姿/蹲姿；列为必需 |
| POSE_08_SEATED_LEGS_EXTENDED | 坐姿、躯干自然稳定，双腿向前伸直；验证坐姿下髋膝踝长度、膝部伸展和脚部方向 |
| POSE_09_PRONE_ARMS_KNEES_SUPPORTED | 身体俯向地面，双臂/手掌稳定按地支撑，双膝着地；技术性关节校准姿态，验证肩肘腕、脊柱、髋膝与小腿折叠关系，禁止性感化或夸张拱背 |

规则：

- 使用已批准 Face + Body Canon；
- 默认继续使用 Calibration Outfit；
- 四肢长度、关节位置和头身比不得随动作变化；
- 动作只验证铰接后的身体身份，不定义剧情表演风格；
- 以上九项均列为 L1 Pose 计划；剧情特有表演、极端动作和未列姿态仍留在 L3 Shot，不自动进入 L1。

---

## 10. Gate 7 — Hosiery / Feet Canon

### 10.1 固定校准材质

```text
15D velvet-finish sheer pantyhose
continuous coverage
thigh -> knee -> calf -> ankle -> heel -> instep -> toes
burgundy toenail polish visible naturally beneath the fabric when lighting permits
```

禁止：latex、rubber、PVC、plastic、liquid coating、body paint、湿亮塑料皮肤。

### 10.2 资产清单

| Asset ID | 构图与职责 |
|---|---|
| HOS_01_LOWER_LEGS_FEET_FRONT | 双小腿和双脚正面，检查整体连续性 |
| HOS_02_FEET_3Q | 双脚 3/4，检查脚踝、脚背和脚趾 |
| HOS_03_FEET_SIDE | 足部侧面，检查脚跟、足弓和袜尖 |
| HOS_04_TOES_FRONT_DETAIL | 脚趾正面细节，检查织物位于指甲上方 |
| HOS_05_HEEL_BACK_DETAIL | 脚跟后视，检查脚踝至脚跟连续性 |
| HOS_06_30D_NUDE_SOFT_SHEEN_FRONT | 30D 微光肉色正面全腿/足部；定义肉色、30D 厚度、微光响应及连续闭趾覆盖，不引用 15D Body Canon 的丝袜质感 |
| HOS_07_30D_GRAY_MATTE_FRONT | 30D 灰色哑光正面全腿/足部；定义灰色色相、30D 厚度、哑光响应及连续闭趾覆盖；当前缺少匹配的 L0 材质源，状态 `BLOCKED_BY_SOURCE_COVERAGE` |

### 10.3 Hosiery QA

- 无鞋，但“无鞋”不等于“无丝袜”；
- 脚踝、脚背、脚跟和脚趾不得突然裸露或换材质；
- 15D 应有真实纺织物透明度和轻微张力变化；
- 酒红色脚趾甲可以透出，但必须在丝袜下面；
- 不强行增强脚趾甲，不把指甲画在丝袜表面；
- 不出现袜口停在脚踝、隐形短袜、露趾袜或身体涂层；
- 不出现重复/缺失脚趾、融合脚趾、断裂脚跟或左右足不一致。

这一组既验证女主足部比例，也建立校准丝袜 L1 Material Canon；它不得重新定义脸部或整体身材。

`HOS_06` 可优先使用已登记但单图覆盖有限的 `HOS_30D_NUDE_SOFT_SHEEN_LIMITED`，生成前须披露单一素材限制。`HOS_07` 在补入并登记真实 30D 灰色哑光材质照片或用户明确授权无 L0 的设计重建前不得生成。两个 30D 资产都不得让 `OWNER_BODY_01_FRONT_CANON_002` 中的 15D 哑光肉色丝袜定义其颜色、厚度或光泽；该 Body Master 仅负责人物身份与身体几何。

---

## 11. Appearance Canon 补充资产

必要文字资产：`APPEARANCE.md`，包含肤色/底色、发色、HAIRSTYLE_A/B、酒红色脚趾甲和妆容规则。

可选图片：

| Asset ID | 用途 |
|---|---|
| APP_01_NEUTRAL_COLOR | 中性灯光下的面部、发色和皮肤色彩校准；不重新定义几何 |
| APP_02_BURGUNDY_TOENAIL | 酒红色脚趾甲颜色参考；只负责颜色，不能定义足部身份和材质 |

若可靠的文字色值和 Gate 7 图片已经足够，可不单独生成这两张。

---

## 12. 数量与优先级

| Gate | 必需图片数 | 可选图片数 | 累计最低数量 |
|---|---:|---:|---:|
| Face | 5 | 0 | 5 |
| Body | 6 | 0 | 11 |
| Hair A | 6（四个标准角度 + 两个高低机位专项视角） | 0 | 17 |
| Hair B | 5 张待制作；另有 1 张现有批准高机位设计锚 | 0 | 22 + 现有 1 |
| Expression | 15 | 0 | 37 + 现有 1 |
| Pose | 9 | 0 | 46 + 现有 1 |
| Hosiery/Feet | 7（其中 HOS_07 暂受素材覆盖阻塞） | 0 | 53 + 现有 1 |
| Appearance | 0 | 2 | 53–55 + 现有 1 |

这些是资产计划数量，不是一次生成数量。默认一次只生成一个 Asset ID 的少量候选，先 QA、再由用户决定是否批准或修改。

---

## 13. 统一 Prompt Assembly 骨架

每次生成按以下顺序组装，不得自由交换职责：

```text
[ASSET TASK]
Create exactly one <ASSET_ID> L1 Canon candidate for CHR_HUMAN_001_OWNER.
3:4 portrait, preferred 1536x2048.

[IDENTITY AUTHORITY]
Follow the current IDENTITY.md revision and the listed scoped identity references.
Preserve the same person and approved facial geometry.

[DOMAIN AUTHORITY]
State exactly whether this image is authoritative for face, body, hairstyle,
expression, pose, appearance, or hosiery/material.

[CALIBRATION CAMERA]
Insert the camera, framing, lighting, white balance, background, and posture rules
from this specification for the selected asset category.

[OUTFIT / MATERIAL]
Insert only the approved Calibration Outfit or the selected scoped material.

[MUST NOT DEFINE]
List every visible property that this candidate is forbidden to redefine.

[NEGATIVE CONSTRAINTS]
Inject identity drift, beauty-filter, anatomy, hosiery, material, and iterative
pollution exclusions applicable to this asset.

[OUTPUT CONTRACT]
One image, one angle, no collage, no text, no watermark, no dramatic styling,
status REVIEW_REQUIRED, not automatically Canon.
```

Prompt 中必须使用具体 Asset ID、Identity 修订号、Reference Set ID 和路径，不能只写“参考之前的图片”。

---

## 14. 候选、批准与锁定

建议候选路径：

```text
canon/face/candidates/
canon/body/candidates/
canon/hairstyles/A/candidates/
canon/hairstyles/B/candidates/
canon/expressions/candidates/
canon/poses/candidates/
canon/hosiery_feet/candidates/
```

单项流程：

```text
DRAFT brief
-> generate candidate
-> QA
-> user rejects / requests revision / explicitly approves
-> approval record
-> component status APPROVED
```

整版流程：

```text
all required components APPROVED
-> final Character Canon review
-> write exact assets and hashes into owner_v1.0 CANON_MANIFEST.yaml
-> user explicitly says LOCK owner_v1.0
-> lock_status: LOCKED
```

锁定后：

- 普通 Shot 只引用 `owner_v1.0` 的确切组件；
- 不再修改锁定图片、metadata 或 `IDENTITY.md`；
- 不用“最新文件”替代固定版本；
- 任何身份、身体或长期外观调整进入新版本。

---

## 15. 新对话执行检查表

新的生成对话在行动前必须确认：

- [ ] 已完整读取本文件；
- [ ] 已读取当前 `IDENTITY.md` 及修订号；
- [ ] 已确认当前 Gate 开放；
- [ ] 本次只处理明确的 Asset ID；
- [ ] 已从 `registries/reference_sets.yaml` 选择最小引用集合；
- [ ] 每张参考图的职责和排除项已写明；
- [ ] 未使用上一张 AI 候选作为身份来源；
- [ ] 画幅为 3:4，使用本类别统一相机和灯光；
- [ ] 输出状态为 `REVIEW_REQUIRED`；
- [ ] 生成后先 QA，不自动进入下一 Gate；
- [ ] 只有用户明确批准后才更新组件状态；
- [ ] 只有用户明确锁定后才创建不可变 Canon 版本。

若用户的新决定与本文件冲突，应先更新本文件的 `spec_revision` 和变更记录，再开始生成，避免不同对话分别采用不同规则。

---

## 16. 变更记录

| Revision | Date | Change | Approval |
|---|---|---|---|
| draft_1.0 | 2026-09-09 | 建立 owner_v1.0 全部 L1 候选资产、统一 3:4 标准、Gate、引用和锁定规则 | awaiting user review |
| draft_1.1 | 2026-09-09 | 固定 A=`DSC00847.jpg`、B=`8.jpg` 的 L0 发型职责；所有出现服装的 owner_v1.0 L1 资产统一使用 Calibration Outfit | user instruction incorporated |
| draft_1.2 | 2026-09-09 | 除 B 专属资产外所有可见头发统一使用 A；B 图 L1 资产新增正脸长相与肤色权威职责 | user instruction incorporated |
| draft_1.3 | 2026-09-10 | 将正面平视细化为眼高水平光轴 + 中立头位 + Frankfort horizontal；禁止继承 B 图俯视和人物仰头透视 | user review incorporated |
| draft_1.4 | 2026-09-10 | 平视扩展为整颗头颅统一投影，禁止“眼睛平视、头顶俯拍”的混合透视；FACE_01 的 A 发型允许直接使用 DSC00847 像素参考并严格限制其职责 | user review incorporated |
| draft_1.5 | 2026-09-10 | 针对 v005 残留俯视与肤色变浅：允许使用 B 锚无调色人脸裁切及轻微反向机位补偿；肤色必须逐项对齐 B 图，A 发型需复现 DSC00847 的具体结构而非仅匹配类别 | user review incorporated |
| draft_1.6 | 2026-09-10 | 固化 v006 已确认的发型与视觉平视方法；允许遮蔽 DSC00847 面部以阻断其身份/肤色泄漏，下一候选重新从 B 裁切与发型 L0 派生图平行生成 | user review incorporated |
| draft_1.7 | 2026-09-10 | 固化 v007 再次确认的发型/角度，记录 v005 正确长相的文字化差异；允许非 AI 插值放大 B 人脸裁切以增强身份权重，仍禁止候选图像级串联 | user review incorporated |
| draft_1.8 | 2026-09-10 | 针对 v008 脸宽反馈：只允许轻微收窄面颊与下颌总宽，不改变五官；恢复标准头肩至上胸构图，避免紧裁切造成脸宽感知偏差 | user review incorporated |
| draft_1.9 | 2026-09-10 | v009 保留为备选；v010 恢复 v005 的完整 B 图脸/肤色约束且取消额外脸宽塑形，叠加 v006 已确认的 A 发型与反向机位/头顶投影约束 | user instruction incorporated |
| draft_1.10 | 2026-09-10 | 固化 v010 完美五官/肤色方法；v011 仅修正头顶占比，使用排除主要头顶的 B 全脸上下文裁切，并限制分缝后退和水平头皮面 | user review incorporated |
| draft_1.11 | 2026-09-10 | 用户批准 v011 为当前 FACE_01 L1 Canon 组件；新增稳定复现方法、源派生恢复集和下游 Canon 引用集，明确 v010 脸/肤色方法 + v011 头顶修正 | user approved component |
| draft_1.12 | 2026-09-10 | 用户审核 FACE_02 左 3/4 v001：整体方向保留；后续仅轻微降低颧骨显高度、将下巴收束改得更圆润，并让眼神更柔和；不得改变已批准身份、角度、肤色、发型或构图 | user scoped review incorporated |
| draft_1.13 | 2026-09-10 | 用户确认 FACE_02 左 3/4 v002 除下巴外均符合目标；下一版只进一步圆润下巴末端，锁定 v002 已确认的身份方向、颧骨、眼神、角度、肤色、发型与构图，且不得以 v002 图像串联 | user scoped review incorporated |
| draft_1.14 | 2026-09-10 | 用户判定 FACE_02 v003 五官偏离；后续恢复 v001 完整提示结构，仅追加颧骨略低柔、下巴圆润和眼神柔和三项约束，所有候选图均不得作为像素输入 | user correction incorporated |
| draft_1.15 | 2026-09-10 | 用户批准 FACE_02 v004 为当前左 3/4 L1 Canon 组件；登记批准 Master、下游引用集、源参考恢复集和详细复现方法，固化 v001 提示结构 + 三项短约束 | user approved component |
| draft_1.16 | 2026-09-10 | 为 FACE_03 纠正参考路由：现有高分辨率 3/4 均朝画面左，不能镜像冒充；新增 `OWNER_L0_FACE_RIGHT_3Q_LIMITED`，由 14.jpg 仅负责画面右向、真人右侧自然差异和粗略深度，批准 FACE_01 与文字身份锚负责精细身份 | generation preparation |
| draft_1.17 | 2026-09-10 | 用户审核 FACE_03 右 3/4 v001：整体方法保留，下巴仍略尖；v002 只进一步圆润下巴底部弧线，保持下巴长度/投影、下颌宽度及其他五官不变，并继续禁止候选图像串联 | user scoped review incorporated |
| draft_1.18 | 2026-09-10 | 用户批准 FACE_03 v002 为当前右 3/4 L1 Canon 组件；登记批准 Master、下游引用集、三输入恢复集和详细复现方法，固化真实右向证据与下巴底部圆润约束 | user approved component |
| draft_1.19 | 2026-09-10 | 用户审核 FACE_05 右侧面 v001：除鼻子外均符合目标；v002 仅轻微缩小鼻尖体量和前向突出度，锁定鼻根/鼻梁、鼻翼/鼻孔、唇颏关系及其他全部属性，并继续禁止候选图像串联 | user scoped review incorporated |
| draft_1.20 | 2026-09-10 | 用户批准 FACE_05 v002 为当前右侧面 L1 Canon 组件；登记批准 Master、下游引用集、三输入恢复集和完整复现方法，固化批准的鼻尖比例及纯侧面约束 | user approved component |
| draft_1.21 | 2026-09-10 | 用户将四个批准 Face Master 从 PNG 转码为 JPG 以降低传输量；更新当前文件指纹、元数据、引用路由和统一 Face 索引，同时保留候选 PNG 作为生成/批准溯源 | user format decision incorporated |
| draft_1.22 | 2026-09-10 | 用户授权在缺少同方向标准侧脸 L0 的情况下生成一张 FACE_04 v001 受限候选；固定为批准 FACE_01 + 14.jpg 同侧有限证据 + 遮脸 HAIRSTYLE_A，禁止镜像 FACE_05 或引用任何其他生成角度，并保留未验证侧面几何警示 | user generation authorization incorporated |
| draft_1.23 | 2026-09-10 | 用户批准 FACE_04 v001 为当前左侧面 L1 Canon 组件；登记批准 Master、下游引用集、三输入恢复集和详细复现方法，同时永久保留缺少同方向真人纯侧脸验证的证据限制 | user approved component |
| draft_1.24 | 2026-09-10 | Gate 2 五个 Face 组件完成后启动 BODY_01_FRONT v001；固定正面 Face、两张真人身体上下文、遮脸 Hairstyle A 和 15D nude velvet/matte 足部材质的五输入职责，并采用不主动塑形的保守身体基线 | user generation authorization incorporated |
| draft_1.25 | 2026-09-10 | BODY_01 首次调用因校准着装与丝袜照片组合触发安全拦截且无输出；重试明确为成年、非性感的技术比例校准照，移除带床景/广告文字的丝袜像素输入，材质暂由文字合同约束 | safe generation retry |
| draft_1.26 | 2026-09-10 | BODY_01 安全重试在无丝袜照片且明确非性感技术语境后仍被输出安全系统拦截；两次均无图，停止继续改词尝试，等待用户决定是否修订 Body 校准服装合同 | generation blocked pending user decision |
| draft_1.27 | 2026-09-11 | 用户将 FACE_04 批准 Master 从 PNG 转码为 JPG 并删除批准目录中的 PNG；纠正其误写为 FACE_05 的 JPG 文件名，更新当前路径、校验值、元数据、引用路由和索引，候选 PNG 继续保留生成溯源 | user format decision incorporated |
| draft_1.28 | 2026-09-11 | 用户精简 15D 肉色哑光 L0 素材：IMG_2562 固定负责脚底，IMG_2579/2580 负责蹲姿，IMG_2581 负责站姿；移除旧活动路由并保留已删除文件 ID 的退役记录 | user material routing decision incorporated |
| draft_1.29 | 2026-09-11 | 用户明确要求保持原 Calibration Outfit，不采用短裤替代，因为短裤不能完全体现身体比例；解除 BODY_01 暂停，授权以相同服装合同、四项最小参考和非性感技术校准语境生成新的 v002 独立候选 | user generation authorization incorporated |
| draft_1.30 | 2026-09-11 | BODY_01 v002 用户复核：脸和发型方向确认良好；下一独立 v003 将腿部视觉占比约增加 5%，校正轻微 O 形小腿为更直的髋膝踝轴线，并强化 15D 丝袜在脚背与脚趾上的连续包覆和横向张力曲线，避免每根脚趾像裸足般清晰分离；v002 像素不得输入 | user scoped review incorporated |
| draft_1.31 | 2026-09-11 | 用户拒绝 BODY_01 v003：腿轴仍不够直，腿部占比需再增加约 5%（累计约高于初始保守基线 10%）；脚趾处不得有颜色分割线或强化袜尖，酒红色趾甲油须从连续 15D 面料下自然透出。v004 继续从四项批准/L0 源参考独立生成，不使用 v002/v003 像素 | user rejection and revision authorization incorporated |
| draft_1.32 | 2026-09-11 | 用户拒绝 BODY_01 v004：腿部占比保持不再调整；下一 v005 只修正小腿 O 形为膝—踝垂直对齐，并强化全腿至脚趾的朦胧 15D 织物覆盖与微微天鹅绒光泽，同时保留面料下自然透出的酒红色趾甲、禁止袜尖分割线。v004 像素不得输入 | user rejection and revision authorization incorporated |
| draft_1.33 | 2026-09-11 | 用户拒绝 BODY_01 v005 的小腿直轴与足部织物表现，同时确认腿部占比和腿部微光泽均可保持；v006 仅把小腿轮廓再收直，并让连续 15D 面料对脚背、趾缝和酒红色甲油产生明确但自然的柔化/朦胧覆盖，不增加袜尖接缝、色带或不透明袜头。v005 像素不得输入 | user rejection and revision authorization incorporated |
| draft_1.34 | 2026-09-11 | 用户拒绝 BODY_01 v006：小腿轴线需继续收直；保留足部朦胧织物覆盖但提高至真实 15D 透明度，使酒红色甲油以柔化低饱和方式重新透出。腿部占比和微光泽保持，禁止使用 v006 像素 | user rejection and revision authorization incorporated |
| draft_1.35 | 2026-09-11 | 用户复核 BODY_01 v007：除腰部过粗外其余方向均确认可保持，包括腿部占比、腿轴、丝袜光泽、足部朦胧覆盖与甲油透出；v008 只轻微收窄腰围并保持自然胸—腰—胯过渡，不制造夸张沙漏形，禁止使用 v007 像素 | user scoped review incorporated |
| draft_1.36 | 2026-09-11 | 用户明确批准 BODY_01 v008 为正面 Body L1 Canon 组件；登记批准 Master、审批证据、下游引用集、源参考恢复集和稳定复现方法。完整 owner_v1.0 仍未锁定，丝袜细节仍不由 Body 组件定 Canon | user approved component |
| draft_1.37 | 2026-09-11 | 用户将批准的 BODY_01 Master 从 PNG 转换为 JPG 并删除批准目录中的 PNG；更新当前下游路径、格式、校验值、元数据、审批记录、Body 索引和引用路由。候选 v008 PNG 继续作为生成与批准溯源，L1 恢复方法不变 | user format decision incorporated |
| draft_1.38 | 2026-09-11 | 用户复核当前 BODY_01 Canon：确认本人真实基准为 168 cm、120 斤（约 60 kg），当前图视觉身高约 160 cm 且小腿仍不够直；授权从四项源参考独立生成 v009，保留已认可的脸、HAIRSTYLE_A 与丝袜质感，只修正偏高身高感/头身肢体比例和膝—胫—踝直轴；禁止使用当前 Body Master 或任何历史 Body 候选像素 | user correction and revision authorization incorporated |
| draft_1.39 | 2026-09-11 | 用户明确批准 BODY_01 v009 的长相、发型、四肢比例、腰臀比、腿脚几何与腿脚丝袜质感；晋升为活动正面 Body 组件 `OWNER_BODY_01_FRONT_CANON_002`，将旧 001 保留为历史 superseded 组件，并更新下游路由与源恢复方法 | user approved component |
| draft_1.40 | 2026-09-11 | 用户澄清 002 的跨资产/镜头职责：168 cm / 60 kg、长相、HAIRSTYLE_A、四肢比例与腰臀比均可供其他资产及视频镜头图片引用；丝袜外观只授权 15D 哑光肉色组合，禁止外推到其他颜色、材质/光泽或厚度 | user scope clarification incorporated |
| draft_1.41 | 2026-09-12 | 用户调整女主资产计划：决定不增加职责混淆的 Face 后脑视角，由 Body/Hair 背面覆盖；A 增加高机位仰视与低机位俯视，B 现有批准图履行高机位仰视并新增低机位俯视；Expression 增至 15 项；Pose 06/07 改为必需并新增伸腿坐姿与双臂/双膝支撑俯姿；Hosiery 新增 30D 微光肉色正面与 30D 灰色哑光正面，后者因缺少匹配 L0 暂阻塞 | user plan revision incorporated |
| draft_1.42 | 2026-09-12 | 用户将活动 BODY_01 Canon 组件 002 从批准 PNG 转换为 `OWNER_BODY_01_FRONT_CANON.jpg` 并删除 PNG；更新唯一活动文件路径、JPEG 校验值、元数据、索引、批准记录、候选指针和引用集，批准范围与四输入源恢复方法保持不变 | user format decision incorporated |
| draft_1.43 | 2026-09-12 | 用户批准 `BODY_02_LEFT_3Q_v001` 为 `OWNER_BODY_02_LEFT_3Q_CANON_001`；登记左 3/4 身体轮廓与深度、168 cm / 60 kg 比例保持、单文件晋升和下游引用范围，并开放 BODY_03 右 3/4 候选 | user approved component and requested next asset |
| draft_1.44 | 2026-09-12 | 用户拒绝 BODY_03 右 3/4 v001：一只脚后跟悬空，脚趾—前脚掌连接处出现异常横线；v002 必须两只脚跟与承重脚掌自然贴在同一地面，并让15D面料从脚踝、脚背、前脚掌至脚趾无接缝、色带或透明度分割线连续过渡，同时禁止使用 v001 像素 | user rejection and revision authorization incorporated |
| draft_1.45 | 2026-09-12 | 用户纠正 v002 QA：模型在脚跟下添加了肉色垫块/多余组织来伪造接地，脚趾—前脚掌横线仍存在；v003 必须采用左右脚错开但互不遮挡的清晰站距，每只脚仅有一个正常解剖脚跟直接接地，禁止肉色垫块、复制脚跟、组织延伸或隐形支撑，并完全消除脚趾根部至前脚掌的线、折痕、色差和材质边界；v001/v002 均不得输入 | user rejection and QA correction incorporated |
| draft_1.46 | 2026-09-12 | 用户确认 BODY_03 v003 除丝袜质感外均完美，但脚部丝袜存在感不足；新登记用户指定 L0 素材 `L0_HOS_15_NM_011` (`15d_nude_matte/1.jpg`)，v004 仅用它定义更明显的15D肉色哑光/天鹅绒织物覆盖、透明度与脚部柔化，严格排除其坐姿、身体/足部几何、肤色、甲色、衣物、鞋、背景和水印；v003 像素不得输入 | user material-reference instruction incorporated |
| draft_1.47 | 2026-09-12 | 用户明确批准 `BODY_03_RIGHT_3Q_v005` 为 `OWNER_BODY_03_RIGHT_3Q_CANON_001`；登记右 3/4 身体轮廓/深度、168 cm / 60 kg 比例保持、正常双脚接地及由 `L0_HOS_15_NM_011` scoped derivative 指导的可见15D肉色哑光/天鹅绒丝袜表现，执行单文件晋升并开放 BODY_04 | user approved component |
| draft_1.48 | 2026-09-12 | 用户授权生成 `BODY_04_LEFT_SIDE_v001`；依次尝试四项及三项最小参考，三次均在输出阶段被安全系统拦截且无图片产生。BODY_04 保持 pending，禁止把失败调用视为候选或下游参考 | generation blocked; no output |
| draft_1.49 | 2026-09-12 | 用户要求按原计划重新生成 BODY_04；新建独立 `BODY_04_LEFT_SIDE_v002`，恢复左侧面 Face、正面 Body、`17.jpg` 侧后粗略轮廓和用户指定丝袜材质派生图四项职责。首次调用无输出，保持四参考仅精简提示后成功生成候选；状态 REVIEW_REQUIRED，未晋升 | user retry authorization incorporated |
| draft_1.50 | 2026-09-12 | 用户明确批准 `BODY_04_LEFT_SIDE_v002` 并要求登记记录；晋升为 `OWNER_BODY_04_LEFT_SIDE_CANON_001`，批准左侧面轮廓/深度、168 cm / 60 kg 比例保持、中性接地站姿、自然侧面遮挡及本组件内15D肉色哑光/天鹅绒丝袜表现，执行单文件移动并开放 BODY_05 | user approved component |
