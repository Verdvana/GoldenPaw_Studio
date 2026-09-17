# 女主身份锚 — 工作版

```yaml
document_id: OWNER_IDENTITY_ANCHOR
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
revision: draft_0.183
status: DRAFT
source_manifest: source/identity/SOURCE_MANIFEST.md
updated_at: "2026-09-17"
```

本文件是 L0 真人照片、用户指定的 L1 目标外观锚与 L1 Face Canon 候选之间的文字身份锚。当前版本尚未获得最终身份批准，可根据用户对候选图的明确反馈继续修订。

当前五个 Face 组件均已批准，当前下游 Master 均为用户转码的 JPG，统一索引见 `face/FACE_CANON_INDEX.md`。格式变化不改变已批准的身份属性；原候选 PNG 仍保留生成溯源。

## 全局脸部生成规则（用户确认，2026-09-17）

所有后续 L1/L2/L3 资产只要脸部可见，均必须依据对应的 L0 真人素材、职责隔离的 L0 派生脸部/肤色裁切或遮蔽图，以及对应 Face generation method 的 prompt 约束生成脸部。任何 AI Face Canon、AI Body Canon 或历史 AI 候选都不得作为脸部生成输入。已批准 AI Face Canon 只允许在生成完成后作为 `qa_comparison_only` 对照，用于检查身份漂移、五官关系、肤色污染、头部投影和渲染伪影；不得进入生成 lineage。

## 用户指定的目标外观锚

- `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001` 仅是 Hairstyle-B 的设计/色彩校准锚，不是脸部生成输入或脸部身份权威；
- 新的 Face Canon 生成必须通过 L0/源派生 Face recovery 方法保持可辨识正脸、面部整体关系与肤色观感；已批准 AI Face Canon 只能作为生成后 QA 对照；
- 该图在 Face 任务中不负责脸部生成、身体、衣服、俯拍机位、灯光、阴影或背景；仅在 HAIRSTYLE_B 专属任务中定义已声明的发型设计属性；
- 除 HAIRSTYLE_B 专属资产外，所有可见头发的女主 L1 资产使用 `HAIRSTYLE_A`；
- Face 候选通过用户审核后，才把成功生成中经用户确认的稳定经验写回本文件，不从失败候选学习。

## 用户已确认的生成经验

- `FACE_01_FRONT_NEUTRAL_v003` 的目标长相与肤色方向正确；
- 成功的引用隔离方式是：只把 `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001` 作为人脸像素输入，HAIRSTYLE_A 使用从 `DSC00847.jpg` 固化的文字规格，避免第二张人脸混入；
- 不得把 v003 本身作为后续像素参考，本条只记录用户确认的方法和属性；
- B 图原始视角是镜头略微俯视、人物略微仰视，不能作为相机/头部姿态权威；
- 正面 Canon 必须重建为真正平视：相机光心与双眼中心同高，光轴水平，人物 Frankfort horizontal plane 近似水平，头部不仰不俯，下巴中立。
- `FACE_01_FRONT_NEUTRAL_v004` 的长相和肤色再次获得用户确认，但发型 A 不正确；其双眼已呈平视，整颗头颅/头顶仍残留俯视投影，造成脸部与头顶透视不一致；不得把 v004 图片用于下游。
- 下一版允许将 `L0_OWNER_017`（`DSC00847.jpg`）直接作为发型 A 像素参考，但它只定义头发的分缝、贴顺体积、轮廓、长度、发束与发尾，不得定义脸、肤色、身体、衣服、光线或背景。
- 平视必须是整颗头颅的统一投影，不只是让眼睛看平：额头、发际线、头盖骨、头顶轮廓、耳位、脸和下颌必须共同符合眼高水平机位；头顶不得呈现从上方观察的椭圆头盖面或过长头皮分缝。
- `FACE_01_FRONT_NEUTRAL_v005` 的长相仍获用户确认，但肤色比 B 图略浅；发型虽直接引用 `DSC00847.jpg`，仍只做到了长直发大类而没有充分复现原图；头顶俯视感也没有实质改善。v005 图片不得作为后续参考。
- 后续肤色必须直接对齐 `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001` 的面颊、额头与颈部基准，不得因灰白背景和柔光自动提亮或美白。
- 为隔离 B 图的俯视头顶偏差，允许从该已批准 L1 图制作仅裁切、不生成、不调色的人脸/肤色派生输入；派生输入必须记录裁切参数、校验值和来源，不具有独立 Canon 权威。
- `FACE_01_FRONT_NEUTRAL_v006` 的发型 A 与视觉平视角度已获用户确认；其脸仍是正确身份方向，但长相细节和肤色与 B 锚有轻微偏差。v006 图片不得作为后续像素参考，只能复用经确认的文字化发型规格、机位补偿方法和源参考组合。
- 当 `DSC00847.jpg` 直接作为发型像素输入时，必须遮蔽其中的真人面部，防止其面部特征和肤色与 B 锚发生平均；遮蔽派生图只负责可见头发轮廓、发量、贴顺度、发束和发尾。
- `FACE_01_FRONT_NEUTRAL_v007` 的发型 A 与角度再次获用户确认，但长相仍不正确；不得将 v007 图片用于下游。
- 用户将 v005 的长相指定为当前正确目标。该结论只转换为文字差异，不把 v005 作为像素参考：相较 v007，保持更柔和饱满的中下脸与面颊、更宽且圆润的下颌收束、更克制的自然眼睛开度、不过度提拉的外眼角、自然宽度的鼻部与不锐化的鼻尖、柔和自然的唇形和圆下巴；禁止瘦脸、大眼化、尖下巴或把五官改成更精致的泛化模板。
- `FACE_01_FRONT_NEUTRAL_v008` 与此前两版的长相差异不足，且用户指出脸整体偏宽。下一版仅将双侧面颊与下颌总宽轻微收窄，目标是柔和的圆润椭圆脸而非宽圆脸；保持五官、肤色、发型和机位不变，不得转向尖瘦脸。
- `FACE_01_FRONT_NEUTRAL_v009` 获用户评价“还可以”，保留为备选候选，但未获 Canon 批准、不得作为生成参考。
- v010 按用户指定组合原始约束：恢复 v005 的完整 B 图脸部方法（精确脸、五官关系、自然年龄与肤色，不追加人工脸宽重塑），叠加 v006 的发型 A 与头顶/反向机位约束。v005、v006 图片本身均不输入模型。
- `FACE_01_FRONT_NEUTRAL_v010` 的五官与肤色获用户评价“完美”，当前唯一失败项是头顶可见面积仍过多、视觉上不像真正平视。v010 图片不得作为下游输入；其成功只固化为“完整 B 锚、不追加脸型塑形”的文字方法。
- v011 对脸部、五官、肤色、发型与标准构图全部保持 v010 方法不变，只把 B 锚改为保留全脸/肩颈但排除主要头顶的上下文裁切，并进一步要求发际线以上的水平头顶面只占极窄比例。
- `FACE_01_FRONT_NEUTRAL_v011` 已由用户明确批准为当前正面无表情 L1 Canon 组件，批准资产 ID 为 `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`；完整 `owner_v1.0` 仍未锁定。
- `FACE_02_LEFT_3Q_NEUTRAL_v004` 已由用户明确批准为当前左 3/4 无表情 L1 Canon 组件，批准资产 ID 为 `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001`。其稳定方法是恢复 v001 的完整提示结构，仅在 Identity block 增加颧骨略低柔、下巴圆润和眼神柔和三项短约束；完整方法见 `canon/face/FACE_02_LEFT_3Q_NEUTRAL_METHOD.md`。
- `FACE_03_RIGHT_3Q_NEUTRAL_v002` 已由用户明确批准为当前右 3/4 无表情 L1 Canon 组件，批准资产 ID 为 `OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001`。其稳定方法使用批准 FACE_01、真实右向 L0 `14.jpg` 和遮脸的 Hairstyle A 输入，以固定顺序平行生成；完整方法见 `canon/face/FACE_03_RIGHT_3Q_NEUTRAL_METHOD.md`。
- `FACE_04_LEFT_PROFILE_NEUTRAL_v001` 已由用户明确批准为当前左侧面无表情 L1 Canon 组件，批准资产 ID 为 `OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001`。其稳定方法使用批准 FACE_01、仅承担同侧方向/自然差异/粗略深度的低分辨率真人 `14.jpg` 和遮脸 Hairstyle A 输入；不使用或镜像 FACE_05，也不引用其他生成角度。完整方法见 `canon/face/FACE_04_LEFT_PROFILE_NEUTRAL_METHOD.md`。
- `FACE_05_RIGHT_PROFILE_NEUTRAL_v002` 已由用户明确批准为当前右侧面无表情 L1 Canon 组件，批准资产 ID 为 `OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001`。其稳定方法使用批准 FACE_01、真实侧脸 L0 `11.jpg` 和遮脸的 Hairstyle A 输入，以固定顺序平行生成，并保留轻微缩小鼻尖体量/突出度的单项约束。

## 当前已批准 Face 身份组件

### FACE_01 正面

- asset_id: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
- role: 正面、无表情、视觉平视的脸部身份与中性影棚肤色基准；同时记录 HAIRSTYLE_A 的正面呈现与头顶投影
- approved path: `canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
- approval: `canon/face/approved/FACE_01_FRONT_NEUTRAL/approvals/APPROVAL_OWNER_FACE_01_FRONT_NEUTRAL_001.md`
- regeneration method: `canon/face/FACE_01_FRONT_NEUTRAL_METHOD.md`
- downstream rule: 该已批准 Master 仅用于生成后 QA 对照；所有未来可见脸部生成使用对应 Recovery Set 的 L0/源派生输入与方法文档 prompt，禁止将本图作为生成输入

### FACE_02 左 3/4

- asset_id: `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001`
- role: 人物 anatomical left facial plane principally visible、鼻尖朝画面左的中性左 3/4 身份；定义该视角的眼眶/鼻梁投影、近远眼、面颊—下颌深度、可见耳位、柔和颧骨、圆润下巴末端和柔和中性眼神
- approved path: `canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg`
- approval: `canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/approvals/APPROVAL_OWNER_FACE_02_LEFT_3Q_NEUTRAL_001.md`
- regeneration method: `canon/face/FACE_02_LEFT_3Q_NEUTRAL_METHOD.md`
- downstream rule: 该已批准 Master 仅用于生成后 QA 对照；未来左 3/4 可见脸部生成使用 `OWNER_FACE_LEFT_3Q_NEUTRAL_RECOVERY_V1` 与方法文档，禁止使用本批准图或历史候选像素

### FACE_03 右 3/4

- asset_id: `OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001`
- role: 人物 anatomical right facial plane principally visible、鼻尖朝画面右的中性右 3/4 身份；定义该视角的近远眼、鼻部投影、右侧面颊—下颌深度、可见耳位、柔和颧骨、圆润下巴底部和柔和中性眼神
- approved path: `canon/face/approved/FACE_03_RIGHT_3Q_NEUTRAL/OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001.jpg`
- approval: `canon/face/approved/FACE_03_RIGHT_3Q_NEUTRAL/approvals/APPROVAL_OWNER_FACE_03_RIGHT_3Q_NEUTRAL_001.md`
- regeneration method: `canon/face/FACE_03_RIGHT_3Q_NEUTRAL_METHOD.md`
- downstream rule: 该已批准 Master 仅用于生成后 QA 对照；未来右 3/4 可见脸部生成使用 `OWNER_FACE_RIGHT_3Q_NEUTRAL_RECOVERY_V1` 与方法文档，禁止镜像或使用本批准图/历史候选像素

### FACE_05 右侧面

- asset_id: `OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001`
- role: anatomical right facial plane visible、鼻尖朝画面左的纯右侧面身份；定义额头—鼻—唇—下巴剪影、批准的鼻尖比例、眼眶深度、耳位、下颌—颈部关系、圆润下巴和柔和前视眼神
- approved path: `canon/face/approved/FACE_05_RIGHT_PROFILE_NEUTRAL/OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001.jpg`
- approval: `canon/face/approved/FACE_05_RIGHT_PROFILE_NEUTRAL/approvals/APPROVAL_OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_001.md`
- regeneration method: `canon/face/FACE_05_RIGHT_PROFILE_NEUTRAL_METHOD.md`
- downstream rule: 该已批准 Master 仅用于生成后 QA 对照；未来右侧面可见脸部生成使用 `OWNER_FACE_RIGHT_PROFILE_NEUTRAL_RECOVERY_V1` 与方法文档，禁止使用任何 FACE_05 生成图、其他生成角度或镜像作为 L1 输入

### FACE_04 左侧面

- asset_id: `OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001`
- role: anatomical left facial plane visible、鼻尖朝画面右的纯左侧面身份；定义用户批准的额头—鼻—唇—下巴剪影、眼眶深度、耳位、下颌—颈部关系、圆润下巴和柔和前视眼神
- approved path: `canon/face/approved/FACE_04_LEFT_PROFILE_NEUTRAL/OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001.jpg`
- approval: `canon/face/approved/FACE_04_LEFT_PROFILE_NEUTRAL/approvals/APPROVAL_OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_001.md`
- regeneration method: `canon/face/FACE_04_LEFT_PROFILE_NEUTRAL_METHOD.md`
- downstream rule: 该已批准 Master 仅用于生成后 QA 对照；未来左侧面可见脸部生成使用 `OWNER_FACE_LEFT_PROFILE_NEUTRAL_RECOVERY_V1` 与方法文档，禁止使用本批准 JPG、候选 PNG、FACE_03、FACE_05、其他生成角度或镜像作为 L1 输入；始终披露该侧面缺少同方向真人纯侧脸验证

## 当前可靠身份观察

以下内容来自多张 L0 照片的交叉观察，不依赖单张精修图：

- 成年女性，整体面部轮廓偏柔和的椭圆至圆润椭圆形；
- 额头宽度与中面部协调，发际线自然，不做夸张缩窄；
- 面颊具有自然柔和饱满度，颧骨不过度突出；
- 下颌线圆润、缓慢收窄，下巴为柔和圆形，不做尖下巴；
- 双眼大小中等，偏自然杏仁形，眼距协调；左右细微自然差异应保留，不做模板化大眼；
- 眉毛整体自然平缓，带轻微弧度，不做高挑锐利眉峰；
- 鼻梁自然、不过度高挺，鼻头柔和圆润，鼻翼比例克制；
- 上下唇比例自然，下唇略有柔和饱满感，唇峰不过度锐利；
- 中性状态保留自然面部体积，不做过度瘦脸、磨皮或幼态化；
- 微笑时面颊自然抬起，露齿笑保持同一眼睛、鼻子、下颌和头骨关系。
- 用户明确指出并由 `L0_OWNER_001` (`2.jpg`) 核对：露齿笑时，人物解剖学右侧上排犬齿（正面画面左侧）呈轻微自然突出的“虎牙”特征；它仍属于正常成人牙列，不得夸张成细长尖牙、獠牙或额外牙齿。
- 微笑时面颊抬起伴随自然酒窝/笑窝响应；`2.jpg` 中正面画面右侧更清楚。该特征只随笑容软组织运动出现，不应做成静态深孔、疤痕或两侧机械对称压痕。

## FACE_02 左 3/4 当前反馈

- `FACE_02_LEFT_3Q_NEUTRAL_v001` 整体方向获用户认可，但仍为未批准候选，不得作为 v002 的像素参考；
- 保持 v001 已实现的身份方向、左 3/4 转角、鼻梁投影、肤色、HAIRSTYLE_A、眼平机位和构图方法；这些只以文字约束复用；
- v002 仅作三项克制修正：颧骨视觉最高点略降、颧区轮廓更柔和，不削平面颊；下巴尖度略减并恢复更柔和圆润的收束，不缩短下巴也不扩大下颌；眼神更柔和放松，通过眼睑张力和注视强度调整，不改变眼睛大小、眼距、眼型或瞳孔位置；
- 禁止将“颧骨降低”做成扁平脸、幼态脸或增加面颊膨胀；禁止将“下巴变圆”做成宽重下巴；禁止用微笑、眯眼、改变眉形或美颜来制造柔和眼神。
- `FACE_02_LEFT_3Q_NEUTRAL_v002` 的身份方向、颧骨、柔和眼神、左 3/4 角度、肤色、HAIRSTYLE_A、机位与构图已获用户确认；v003 必须锁定这些文字属性，只将下巴末端再圆润一小步；不得改变下巴长度、下颌宽度、下颌角、嘴唇位置或脸部其他结构，也不得使用 v002 像素。
- `FACE_02_LEFT_3Q_NEUTRAL_v003` 因五官偏离被用户拒绝，不得用于下游或后续生成。下一候选恢复 v001 的完整核心提示结构，只追加三项简短约束：颧骨略低且轮廓柔和、下巴更圆润但不变宽变短、眼神更柔和但不改变眼睛几何。
- `FACE_02_LEFT_3Q_NEUTRAL_v004` 已获用户明确批准。其像素仅作为批准 Master 做生成后 QA 对照；未来 L1/L2/L3 脸部生成复用源派生方法、输入顺序和文字约束，不使用 v004 像素。

## FACE_03 右 3/4 当前反馈

- `FACE_03_RIGHT_3Q_NEUTRAL_v001` 的右向重建方法、身份方向、角度、眼神、肤色、发型、机位与构图继续保留为文字方法，但候选图仍未批准且不得作为 v002 像素输入；
- 用户指出唯一明确调整项为下巴仍略尖。v002 只将下巴最下端中央轮廓变得更圆、更钝柔一些；保持下巴垂直长度、前后投影、下颌宽度、下颌角、嘴唇位置、面颊、颧骨、鼻子、眼睛和其他五官不变；
- 禁止把圆下巴做成缩短、后缩、宽重、双下巴、幼态或肿胀，也不得借此改变整体脸型。

## 当前不确定或易受照片影响的部分

- L0 照片跨越不同妆容、精修、手机焦段、光照和可能的不同生活阶段；
- 婚纱及棚拍照片只可辅助几何与表情，不负责皮肤纹理和中性妆容；
- `12.jpg`、`14.jpg` 分辨率较低且属于近距离手机视角，不能单独决定镜头中性的脸宽和鼻部透视；
- 身体比例、肤色、发型、妆容、服装和灯光不由本次 Face 候选锁定。

## FACE_03 右 3/4 已确认方法

- v001 的整体身份、方向、机位、发型与构图方法被保留，但下巴仍略尖；v001 未获批准且像素不得复用；
- v002 仍从批准 FACE_01、`14.jpg` 和遮脸 Hairstyle A 三项原始输入平行生成，只增加“下巴底部中央弧线更柔和圆润”这一项约束；
- 圆润下巴不得改变下巴长度、前向投影、下颌宽度、下颌角、下唇位置或其他五官；
- `14.jpg` 只定义真实画面右向、右侧自然差异和粗略深度，不能定义精细身份或中性镜头比例；
- 用户已批准 v002；后续普通镜头使用批准 Master，重新制作 L1 使用方法与恢复集，不复用任何 FACE_03 生成图像。

## FACE_05 右侧面当前反馈

- `FACE_05_RIGHT_PROFILE_NEUTRAL_v001` 的身份、标准侧面方向、眼神、嘴唇、圆润下巴、下颌—颈部关系、耳位、肤色、HAIRSTYLE_A、机位和构图均获用户确认；
- 用户指定唯一调整项为鼻子略小。v002 只轻微减小侧面鼻尖体量与前向突出度，不把鼻子改成窄尖模板；
- 保持鼻根位置、鼻梁长度与走势、鼻背角度、鼻翼/鼻孔结构、鼻唇角、嘴唇位置、下巴投影及其他全部五官不变；
- v001 未获批准且不得作为 v002 像素输入；v002 继续使用批准 FACE_01、真人 `11.jpg` 和遮脸 Hairstyle A 三项源参考平行生成。
- `FACE_05_RIGHT_PROFILE_NEUTRAL_v002` 已获用户明确批准；批准方法只继承源参考组合和文字化鼻尖修正，不继承 v001/v002 像素用于 L1 再生成。

## FACE_04 左侧面已批准方法与证据限制

- 当前没有鼻尖朝画面右的标准真人纯侧脸 L0；用户已明确批准 `FACE_04_LEFT_PROFILE_NEUTRAL_v001` 为当前左侧面 Canon，因此其生成侧面轮廓进入该组件的批准范围，但不应被描述成已由同方向真人纯侧脸独立验证。
- v001 只使用三项固定输入：批准 FACE_01 JPG 负责精细身份；真实 `14.jpg` 只负责鼻尖朝画面右、真人同侧自然差异和粗略深度；遮脸的 Hairstyle A 派生图只负责头发。
- 不使用、不镜像 `FACE_05`，也不引用 `FACE_03`、其他生成角度或历史候选；不存在 AI A → AI B 的身份谱系。
- 因 `14.jpg` 是低分辨率 3/4 手机图，不能单独定义镜头中性的鼻部突出度、额头—鼻—唇—下巴纯侧面剪影或精细耳位；这些部分必须依据批准正面身份做克制、自然、非模板化的保守重建。
- 批准目标固定为人物 anatomical left facial plane visible、鼻尖朝画面右、85–90° 真侧面；只显一只主要眼睛，远侧虹膜不得越过鼻梁；眼神自然向画面右平视，闭嘴、柔和中性。
- 保持用户批准的柔和饱满面颊、不过高锐的颧骨、圆润下颌与圆而不尖的下巴；鼻子不得被美化为高、尖、翘或夸张突出。任何重新生成仍从源参考平行构建并恢复为 `REVIEW_REQUIRED`，不得从批准 JPG 或候选 PNG 继续繁殖。

## owner_v1.0 默认调整策略

用户允许后续对脸型和身材作轻微调整，但尚未指定具体调整方向。因此当前工作版默认：

- 不主动改变真人可辨识身份；
- 不主动瘦脸、尖下巴、放大眼睛、缩鼻或改变年龄；
- 只消除单张照片的镜头畸变、极端光照、妆容和精修差异；
- 等用户审核 Face 候选后，再将明确的保留或调整意见写入下一修订。

## BODY_01 正面首版基线

- Gate 2 五个 Face 角度已分别批准，现进入 Gate 3；`BODY_01_FRONT_v001` 只建立待用户校准的正面身体基线，不自动成为身体事实。
- 脸部生成身份由对应 L0 真人素材、确定性源派生输入和 Face method prompt 共同定义；批准的 `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` 仅作生成后 QA 对照。真人 `3.jpg` 与 `4.jpg` 继续只交叉提供身高感、头身比、肩宽、躯干长度、腰线、胸腰胯自然范围、臂腿长度和真实非模特化体态。
- 用户尚未指定主动身材调整。v001 不瘦身、不增高、不拉腿、不夸大胸腰臀差、不收窄肩胯，也不把单张衣物塑形或走路姿态当成裸体几何。
- 身体正面自然直立、重量均匀、双臂自然下垂、手掌靠近大腿但不贴死、双脚平行或自然微外展且不交叉；头部正面平视、闭嘴中性。
- 完整使用粉色高叉连体泳衣、15D nude velvet-finish sheer pantyhose 和无鞋状态；丝袜从腰胯连续覆盖至脚趾，但 BODY_01 只做连续性预检，最终材质权威属于 Gate 7。
- HAIRSTYLE_A 只由遮脸发型输入定义；真人全身照中的发型、衣服、鞋、手持物、背景、脸和腿部视觉塑形不得传入。
- BODY_01 首次调用未产出图片；安全重试移除带床景/广告文字的丝袜照片，并将画面明确限定为成年、非性感的技术性身体比例校准照。该执行调整不改变身份或身体目标，丝袜连续性仍按文字合同检查。
- BODY_01 安全重试仍在输出阶段被拦截且无图；当前不存在 BODY_01 候选。不得把失败调用当作身体反馈或新身份事实，等待用户明确决定是否修改 Body 校准服装合同后再生成。

## BODY_01 当前批准结果

- 用户确认本人现实身体基准为身高 `168 cm`、体重 `120 斤`（约 `60 kg`）。该数值是当前 Body 身份事实，优先于 L0 全身照因服装、镜头和姿态产生的矮化观感。
- `BODY_01_FRONT_v015` 已由用户明确批准并晋升为当前活动正面 Body 组件 `OWNER_BODY_01_FRONT_CANON_003`；`OWNER_BODY_01_FRONT_CANON_002` 与旧 `OWNER_BODY_01_FRONT_CANON_001` 保留为历史已批准但已被替代的组件，不再作为当前 Body01 下游路由目标。
- 当前活动组件呈现与 168 cm / 60 kg 相符的自然成年女性比例：整体偏高但不是夸张模特身材，保持真实肩胸腰胯和软组织体量；通过正确头身比、躯干与四肢长度关系表达身高，不得缩头、广角拉腿、低机位仰拍或机械纵向拉伸。
- 小腿需进一步收直：双侧膝、胫骨中线与踝中心形成自然近竖直轴，胫骨不向外弯，左右小腿肌肉保留自然体量但外轮廓不制造 O 形腿观感，双脚仍平放且方向对称。
- 用户明确批准 v015 的身体比例、HAIRSTYLE_A、略收窄且自然过渡到既有胯宽的腰部、四肢比例、腿型和腿脚丝袜表现。活动 Body Master 下游只定义其批准的身体/发型/丝袜职责，不定义可见脸部；重新制作 L1 或可见脸部资产仍按 Face recovery method 的源派生输入、两张 L0 身体上下文和遮脸发型 A 平行生成，不使用任何 Body Master 或历史候选像素。
- 用户进一步明确：`OWNER_BODY_01_FRONT_CANON_003` 中的 168 cm / 60 kg、HAIRSTYLE_A、四肢比例、腰臀比和本组件批准的正面腿脚表现可用于生成其他角色资产及视频镜头所需图片；可见脸部必须另行使用源派生 Face recovery inputs + Face method prompt，批准 Face/Hair Canon 只按各自职责或生成后 QA 对照使用。丝袜职责仍限于本组件声明的 15D 浅肉色、连续脚趾覆盖、酒红甲油下透和趾间袜面张力，不得外推至其他颜色、材质/光泽或厚度。
- 用户授权 `BODY_01_FRONT_v017` 仅修正小腿直度：小腿腿骨/胫骨轴线几乎顺着大腿轴线向下，几乎无弯曲；外轮廓不明显偏离大腿外轮廓；内侧基本贴近，仅留极窄自然间隙，禁止融合、交叉或 O 型腿。v016 已确认的腰臀比、胯与大腿根部、长相、丝袜质感、略微发白袜色、趾间张力和酒红色指甲油保持不变；v017 仍为待审核候选，不写回批准事实。
- 用户确认 v017 小腿直度可以，授权 `BODY_01_FRONT_v018` 修正脚趾根部莫名白色环、统一让酒红指甲位于连续袜面下的朦胧覆盖、恢复趾间袜面张力曲线；同时让大腿与小腿略增自然体量、腰部略细，并要求双脚全脚掌平放着地，禁止垫脚。v018 仍为待审核候选，不自动晋升。
- 用户指出 v018 小腿仍有弯曲，且外侧轮廓没有与大腿基本齐平；授权 `BODY_01_FRONT_v019` 仅强化小腿近乎直下轴线和外侧轮廓连续下行，保留 v018 已认可的丝袜质感、腿部体量、腰部比例及全脚掌着地。v019 仍为待审核候选，不自动晋升。
- 用户明确批准 `BODY_01_FRONT_v019` 并要求登记；其小腿近乎直下、外侧轮廓与大腿基本齐平、v018 的腿部体量与腰部比例、丝袜质感及全脚掌着地现已成为当前正面 Body 组件 `OWNER_BODY_01_FRONT_CANON_005` 的批准范围。v004 及更早正面组件降为历史版本。
- 用户授权根据当前 `OWNER_BODY_01_FRONT_CANON_005` 生成对应背面 Body 候选 `BODY_06_BACK_v004`；背面保持相同 168 cm / 60 kg 体量、腰臀比、略细腰、较丰满腿部、近乎直下腿轴和全脚掌着地，沿用当前浅肉色略发白 15D 丝袜质感及背面脚跟渐变。背面候选仍需单独审核，不自动替代当前 `OWNER_BODY_06_BACK_CANON_002`。
- 用户指出 v004 背面腿部轮廓与正面不一致；授权 `BODY_06_BACK_v005` 使用从当前正面 Canon 005 确定性脸部排除裁切派生的腰臀、腿轴、外侧腿线和脚部比例作为跨视角对齐依据，背面 L0 仅补充背部深度，丝袜与脚跟渐变保持不变。v004 不作生成输入。
- 用户明确批准 `BODY_06_BACK_v005` 并要求登记；该背面组件已按当前正面 005 对齐腿部轮廓和体量，成为 `OWNER_BODY_06_BACK_CANON_003`，并保留当前背面高叉开口、浅白 15D 丝袜、脚跟渐变和全脚掌着地职责。
- `BODY_02_LEFT_3Q_v001` 已由用户明确评价“完美”并晋升为 `OWNER_BODY_02_LEFT_3Q_CANON_001`；它在左 3/4 视角内批准身体轮廓、保守深度关系及 168 cm / 60 kg、四肢比例和腰臀比的保持，不重新定义脸、发型、正面比例、其他方向或 Gate-7 丝袜材质。
- `BODY_03_RIGHT_3Q_v001` 因脚后跟悬空及脚趾—前脚掌处异常横线被用户拒绝。v002 仍从批准 FACE_03 与活动 BODY_01 Master 独立生成，不使用 v001；两脚必须完整自然贴地，15D丝袜从脚踝至脚趾无袜尖边界、色带或透明度突变。
- `BODY_03_RIGHT_3Q_v002` 仍被拒绝：脚跟下出现肉色垫块/多余组织，且脚趾—前脚掌横线未消失。v003 不使用 v001/v002，双脚以足够间距分别呈现完整轮廓；每只脚只能有一个正常脚跟直接接地，不得增加任何支撑物或肉色形体，丝袜在脚趾根部不得出现线、折痕、色带或透明度边界。
- 用户确认 `BODY_03_RIGHT_3Q_v003` 除丝袜质感外均完美；v004 只把新登记的 `L0_HOS_15_NM_011` 用于增强全腿至脚部的15D肉色哑光/天鹅绒织物存在感、透明度与柔化覆盖，不继承该素材的坐姿、身体/脚形、肤色、甲色、服装、背景或水印，也不输入 v003 像素。
- `BODY_03_RIGHT_3Q_v005` 已由用户明确批准为 `OWNER_BODY_03_RIGHT_3Q_CANON_001`；批准范围包括右 3/4 身体轮廓与深度、168 cm / 60 kg 比例保持、正常双脚接地，以及本 Body 组件内由 `L0_HOS_15_NM_011` scoped derivative 指导的15D肉色哑光/天鹅绒丝袜呈现。Gate-7 最终丝袜材质权威仍独立建立。
- `BODY_04_LEFT_SIDE_v002` 已由用户明确批准为 `OWNER_BODY_04_LEFT_SIDE_CANON_001`；批准范围包括完整左侧面身体轮廓与保守深度、168 cm / 60 kg 比例保持、中性双脚接地、自然侧面肢体遮挡，以及本 Body 组件内由用户指定丝袜素材派生图指导的15D肉色哑光/天鹅绒丝袜呈现。Gate-7 最终丝袜材质权威仍独立建立。
- `BODY_05_RIGHT_SIDE_v001` 已由用户明确批准为 `OWNER_BODY_05_RIGHT_SIDE_CANON_001`；批准范围包括完整右侧面身体轮廓与保守深度、168 cm / 60 kg 比例保持、中性接地、自然侧面肢体/远侧脚跟遮挡，以及本 Body 组件内连续的15D肉色哑光/天鹅绒丝袜呈现。Gate-7 最终丝袜材质权威仍独立建立。
- `BODY_06_BACK_v001` 已由用户明确批准为 `OWNER_BODY_06_BACK_CANON_001`；批准范围包括完整180度背面身体轮廓与保守后侧深度、168 cm / 60 kg 比例保持、头身一致朝后、双脚跟直接接地、该 Body 组件内保守的 HAIRSTYLE_A 后落及连续15D肉色哑光/天鹅绒丝袜呈现。它不替代 `HAIR_A_04_BACK` 或 Gate-7 材质权威。六个 Body 组件已全部批准，Gate 4 开放。

## FACE_01 必须保持

- 正面、眼平、中性闭嘴表情；
- 同一个人的头骨、眼距、鼻子、嘴唇、面颊、下颌与下巴关系；
- 自然真实皮肤，不复制任何 L0 的色偏或强阴影；
- 使用 `HAIRSTYLE_A`，依据 `DSC00847.jpg` 的长直披发设计；不得使用临时校准发型或 HAIRSTYLE_B；
- 若画面出现服装，必须为粉色高叉连体泳衣的真实上半部分；
- 中性灰白影棚、柔和均匀光、3:4 头肩构图。

## HAIR_A_01 当前反馈

- 用户确认 `HAIR_A_01_FRONT_v001` 除鼻部视觉略大外其余方向可保持；这不修改已批准的脸部 Canon，而是记录该 Hair 候选发生了鼻部漂移。
- `HAIR_A_01_FRONT_v002` 必须通过源派生 Face recovery 输入和方法文档保持鼻梁宽度、鼻尖体量、鼻翼宽度和鼻部整体投影；`OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` 仅作生成后 QA 对照，不得借 Hair 任务重新塑造脸部。
- v001 的发型正面方向、近中分、贴顺低至中等顶部体积、长直脸侧发束、深棕色与自然细碎发丝只以用户反馈文字保留，不使用 v001 像素。
- v002 同时修正技术 QA 的发尾裁切：完整显示两侧最长发尾及其下方 5–8% 空间。
- 用户已于 2026-09-12 明确批准 v002，并将其按单文件规则晋升为 `OWNER_HAIR_A_01_FRONT_CANON_001`。批准职责只覆盖眼平标准正面的 Hairstyle-A：近中短分缝、低至中等顶部体积、长直披散脸侧发束、深棕克制高光、胸下完整长度与渐细发尾；不定义脸、鼻部、皮肤、表情、身体、服装、其他 Hair-A 角度或 Hairstyle B。
- Hairstyle-A 六视图当前完成 1/6；其余五项及完整 `owner_v1.0` 均未锁定。

## EXP_01 当前批准状态

- 用户于 2026-09-12 将 JPG 直接放入 Expression 批准目录，并明确要求作为第一项表情资产登记。
- 该文件已登记为 `OWNER_EXP_01_NEUTRAL_CANON_001`，只定义放松眉眼、平静直视和自然闭嘴的中性瞬时表情。
- 图中可见的脸部永久几何、肤色、Hair A、校准服装、灯光和背景均不因本次 Expression 批准取得新权威；文件生成溯源未由用户声明。

## EXP_02 当前候选目标

- 用户于 2026-09-12 授权继续生成下一项 `EXP_02_SUBTLE_SMILE_v001`。
- 目标只是在中性基线上让双侧嘴角轻微、自然地上扬，嘴唇保持闭合，不露齿，不升级为完整自然微笑。
- 使用批准 FACE_01、批准 HAIR_A_01 与真人 `L0_OWNER_007` 平行生成；真人图只负责轻微笑意的软组织方向，不定义身份、牙齿、近摄透视、服装、发型、灯光或背景。EXP_01、EXP_13 和任何候选图均不作为像素输入。
- `EXP_02_SUBTLE_SMILE_v001` 已按上述三项隔离职责生成，并于 2026-09-12 获用户明确批准、登记为 `OWNER_EXP_02_SUBTLE_SMILE_CANON_001`。批准只覆盖闭嘴无露齿、双侧嘴角轻微平衡上扬及最小自然面颊/下眼睑响应，不重新定义永久身份或其他可见属性。

## EXP_03 当前候选目标

- 用户于 2026-09-12 授权继续生成下一项 `EXP_03_NATURAL_SMILE_v001`。
- 目标为清晰自然、比 EXP_02 更明显但不过度的闭嘴微笑：双侧嘴角自然上扬，面颊适度抬起，下眼睑出现温和真实响应；不露齿、不张嘴，不升级成露齿笑或大笑。
- 使用批准 FACE_01、批准 HAIR_A_01 与真人 `L0_OWNER_007` 平行生成；真人图只负责自然笑的软组织联动，不定义牙齿、永久身份、近摄透视、服装、发型、灯光或背景。EXP_01、EXP_02、EXP_13 和任何候选图均不作为像素输入。
- `EXP_03_NATURAL_SMILE_v001` 已按上述三项隔离职责生成，并于 2026-09-12 获用户明确批准、登记为 `OWNER_EXP_03_NATURAL_SMILE_CANON_001`。批准只覆盖闭嘴无露齿、自然平衡的嘴角上扬、适度面颊抬起与温和下眼睑笑意，不重新定义永久身份或其他可见属性。

## EXP_04 当前候选目标

- 用户于 2026-09-12 授权继续生成下一项 `EXP_04_SMILE_WITH_TEETH_v001`。
- 目标为自然、中等强度的露齿笑：嘴角自然展开，面颊抬起，下眼睑温和响应，以上排牙齿自然可见为主；不露大量牙龈、不夸张张嘴、不升级为大笑。
- 使用批准 FACE_01、批准 HAIR_A_01 与真人 `L0_OWNER_008` 平行生成；真人图只负责露齿笑软组织联动与牙齿显露方式，不定义永久牙齿 Canon、身份、头部倾斜、妆容、卷发、服装、灯光或背景。任何已生成 Expression 图均不作为像素输入。
- `EXP_04_SMILE_WITH_TEETH_v001` 已按上述三项隔离职责生成；技术预检确认自然中等强度、以上排牙齿为主、无明显牙龈、下颌开启克制且未达到大笑。当前仅为 `REVIEW_REQUIRED` 候选，不得作为下游参考。
- 用户随后拒绝 v001，指出它遗漏人物右侧虎牙和微笑酒窝。v001 状态改为 `USER_REJECTED`，不得用于下游或作为任何后续像素输入。
- `EXP_04_SMILE_WITH_TEETH_v002` 改用批准 FACE_01、批准 HAIR_A_01 与用户点名的真人 `L0_OWNER_001` (`2.jpg`) 平行重建；`2.jpg` 仅定义人物右侧（正面画面左侧）自然突出虎牙、真实露齿方式和笑时酒窝/笑窝响应，排除婚纱妆容、精修、手部遮挡、另一人物、发型、服装、背景及永久身份几何。
- v002 已独立生成，并于 2026-09-12 获用户明确批准、登记为 `OWNER_EXP_04_SMILE_WITH_TEETH_CANON_001`。批准只覆盖自然中等强度露齿笑、人物右侧虎牙在正面画面左侧的自然显露、上排牙齿显露方式、面颊抬起及笑时酒窝/笑窝响应；不重新定义静止牙列/酒窝、永久身份或其他可见属性。

## EXP_05 当前候选目标

- 用户于 2026-09-13 授权继续生成 `EXP_05_HAPPY_LAUGHING_v001`。
- 目标为自然、真诚、明显开心的大笑：嘴巴比 EXP_04 更充分地自然张开，嘴角与面颊明显抬起，下眼睑随笑意收窄但不硬挤，允许自然显示上排牙齿、少量下排牙齿与口腔暗部；不得转成尖叫、惊讶、哭笑、夸张狂笑或漫画变形。
- 使用批准 FACE_01、批准 HAIR_A_01、真人 `L0_OWNER_016` (`DSC01015.JPG`) 与真人 `L0_OWNER_001` (`2.jpg`) 四项平行生成。`DSC01015.JPG` 只定义真实开心大笑的软组织联动和张嘴幅度；`2.jpg` 只补充人物右侧虎牙在正面画面左侧的方向及笑时酒窝响应；两者均不得定义永久身份、妆容、发型、服装、身体、光线或背景。
- EXP_04 批准图及任何其他生成 Expression 图均不作为像素输入；EXP_05 必须从声明的批准 Master 与真人 L0 独立构建。
- `EXP_05_HAPPY_LAUGHING_v001` 已按上述四项隔离职责生成，并于 2026-09-13 获用户追溯明确批准、登记为 `OWNER_EXP_05_HAPPY_LAUGHING_CANON_001`。批准只覆盖自然开心大笑、面颊/下眼睑联动、适中张嘴、人物右侧虎牙方向与笑时酒窝响应，不重新定义永久身份、静止牙列/酒窝或其他可见属性。

## EXP_06 当前候选目标

- 用户于 2026-09-13 要求继续生成下一项；EXP_05 保持 `REVIEW_REQUIRED`，不作为 EXP_06 像素输入。
- `EXP_06_SURPRISED_v001` 目标为自然、清晰但不过度的惊讶：双眉适度抬起，眼睑比中性状态打开但不夸张瞪眼，嘴唇自然分开形成克制的小至中等开口，下颌仅随表情适度下降。
- 使用批准 FACE_01、批准 HAIR_A_01 与真人 `L0_OWNER_006` (`8.jpg`) 三项平行生成。真人图只定义惊讶时眉眼与张嘴的软组织协调，不定义永久身份、盘发、双手托脸、针织衫、身体姿态、暖光或花园背景。
- 禁止恐惧、尖叫、哭泣、开心大笑、喜悦笑容、极端圆眼、眉毛过高、嘴巴大张或漫画式变形；不得改变永久眼睛、眉毛、鼻子、嘴唇、下颌或下巴几何。
- `EXP_06_SURPRISED_v001` 已按上述三项隔离职责生成，并于 2026-09-13 获用户明确审核通过、登记为 `OWNER_EXP_06_SURPRISED_CANON_001`。批准只覆盖自然适度抬眉、眼睑打开、克制微张嘴和警觉注视，不重新定义永久身份或其他可见属性。

## EXP_07 当前候选目标

- 用户于 2026-09-13 授权开始下一项 `EXP_07_CONFUSED_CURIOUS_v001`。
- 已复核完整 L0 身份目录及 `registries/reference_sets.yaml`；现有真人素材覆盖中性、微笑、露齿笑、大笑、惊讶、闭眼/低头等状态，但没有一张可可靠定义困惑/好奇，因此本候选明确保留 L0 表情覆盖缺口，不挪用不匹配表情。
- 只使用批准 FACE_01 与批准 HAIR_A_01 两项最小参考平行生成；前者负责永久正面身份，后者只负责 Hair A。EXP_05、EXP_06、其他批准/未批准 Expression、Body 和 Shot 图像均不得作为像素输入。
- 目标为自然、克制、可读的困惑/好奇：一侧眉毛适度抬起，另一侧内眉轻微向内下方收紧，眼睛保持真实大小并呈专注疑问感；嘴唇自然闭合或只极轻微分开，嘴角不笑、不下垂。头部保持正直眼平，不通过歪头替代表情。
- 禁止夸张高挑单眉、双眉大幅抬高、瞪眼、斗鸡眼、歪嘴、撇嘴、嘟嘴、明显皱鼻、深刻额纹、惊讶、恐惧、恼怒、悲伤、讥讽或漫画式困惑；不得改变永久眉形、眼形、鼻子、嘴唇、下颌、下巴、肤色或年龄。
- `EXP_07_CONFUSED_CURIOUS_v001` 已按两项批准 Master 独立生成，并于 2026-09-13 获用户明确批准、登记为 `OWNER_EXP_07_CONFUSED_CURIOUS_CANON_001`。批准只覆盖克制眉部不对称、疑问专注眼神、中性闭嘴和正直头位，不重新定义永久身份或其他可见属性；无匹配困惑/好奇 L0 表情照片的来源覆盖限制永久保留。

## EXP_08 当前候选目标

- 用户于 2026-09-13 授权生成下一项 `EXP_08_MILDLY_ANNOYED_v001`。
- 参考指南、完整 L0 清单与 `registries/reference_sets.yaml` 没有可靠的轻微不悦真人表情源；本候选保留该覆盖缺口，不用惊讶、笑容、闭眼或其他不匹配照片代替。
- 只使用批准 FACE_01 与批准 HAIR_A_01 两项最小参考；前者负责永久正面身份，后者只负责 Hair A。EXP_01–07、EXP_13、任何其他生成 Expression、Body 与 Shot 图像均不得作为像素输入。
- 目标为轻微、克制、日常可读的不悦：双侧内眉只小幅向内下方收紧，眼睑轻度收窄但不眯眼，视线直接且略显不耐；嘴唇自然闭合并轻微压紧，嘴角接近水平或仅极轻微下压。头部正直眼平。
- 必须弱于明确愤怒；禁止明显怒视、强烈眉间沟、鼻翼扩张、皱鼻、咬牙、露齿、明显撇嘴、歪嘴、翻白眼、讥讽/轻蔑、厌恶、悲伤、专注用力或漫画式不悦。与已撤销的“轻微皱眉”设计相比，本项包含轻度眼睑收窄和压唇不耐感。
- `EXP_08_MILDLY_ANNOYED_v001` 已按两项批准 Master 独立生成，并于 2026-09-13 获用户明确批准、登记为 `OWNER_EXP_08_MILDLY_ANNOYED_CANON_001`。批准只覆盖内眉小幅收紧、眼睑轻度收窄、克制不耐注视与轻微压唇，不重新定义永久身份；无匹配轻微不悦 L0 表情照片的覆盖限制永久保留。

## EXP_09 当前候选目标

- 用户于 2026-09-13 在批准 EXP_08 后授权生成下一项 `EXP_09_SAD_CONCERNED_v001`。
- 当前 Reference Guide、完整 L0 清单与注册表没有可靠的难过/担忧真人表情源；不挪用低头微笑、闭眼、惊讶或婚纱笑容图。本候选明确保留 L0 覆盖缺口。
- 只使用批准 FACE_01 与批准 HAIR_A_01 两项最小参考；任何批准/未批准 Expression、Body 和 Shot 图像均不得作为像素输入。
- 目标为自然、克制的难过/担忧：双侧内眉轻微抬起并靠拢，眉中外侧保持自然或略低；眼睑与凝视柔和、直接并带担心感，但眼睛保持真实大小；嘴唇自然闭合，嘴角轻微对称下垂，下巴只允许极小的软组织张力。
- 禁止眼泪、湿眼高光刻意强化、哭泣、抽泣、痛苦扭曲、眉毛高拱、额头深纹、嘴巴大张、噘嘴、儿童式委屈、惊讶、恐惧、恼怒、愤怒、专注、讥讽或漫画式悲伤；不得改变永久眉眼、嘴唇、下颌/下巴、肤色或年龄。
- `EXP_09_SAD_CONCERNED_v001` 已按两项批准 Master 独立生成，并于 2026-09-13 获用户明确批准、登记为 `OWNER_EXP_09_SAD_CONCERNED_CANON_001`。批准只覆盖轻微内眉上提靠拢、柔和担忧注视、闭嘴嘴角轻微下垂及极小下巴张力，不重新定义永久身份；无匹配难过/担忧 L0 表情照片的覆盖限制永久保留。

## EXP_10 当前批准范围

- 用户于 2026-09-13 在批准 EXP_09 后授权生成下一项 `EXP_10_FOCUSED_SERIOUS_v001`。
- 当前 Reference Guide、完整 L0 清单与注册表没有专门、可靠的专注/认真真人表情源；本候选保留该覆盖缺口，不挪用不悦、惊讶、低头或笑容图。
- 只使用批准 FACE_01 与批准 HAIR_A_01 两项最小参考；任何批准/未批准 Expression、Body 和 Shot 图像均不得作为像素输入。
- 目标为平静、稳定、任务导向的专注认真：视线直接、稳定并聚焦；眼睑只极轻微收束但不眯眼；眉毛接近中性，仅允许极小幅度内聚或降低松弛度；嘴唇自然闭合而不压紧，嘴角和下颌保持放松中性。
- 必须没有情绪性不悦：禁止内眉明显下压、怒视、压唇、嘴角下垂、鼻翼张力、皱鼻、咬牙、悲伤、担忧、惊讶、困惑、讥讽或漫画式“严肃脸”。与 EXP_08 的区别是本项没有不耐或压唇，与已撤销的“轻微皱眉”设计相比，本项不以明显皱眉为核心。
- `EXP_10_FOCUSED_SERIOUS_v001` 已按两项批准 Master 独立生成，并于 2026-09-13 获用户明确批准、登记为 `OWNER_EXP_10_FOCUSED_SERIOUS_CANON_001`。批准仅覆盖稳定直接注视、极轻眼睑收束、近中性眉毛、自然闭嘴与放松下颌，并与 EXP_08 的不耐压唇及现已撤销的轻微皱眉设计区分。

## EXP_13 当前批准范围

- 用户拒绝 `EXP_13_MOUTH_SLIGHTLY_OPEN_v001` 的“平静微张嘴”定义；v001 不得成为下游参考或后续像素输入。
- 当前第 13 项（原列表第 15 项）的用户指定表情为：皱眉、闭眼、嘴巴张开但不是大张。眉头通过自然肌肉张力向内下方收紧，双眼自然闭合，嘴部保持克制的中小幅度开启。
- 该表情只允许眉间、眉头、眼睑、唇周和下颌产生瞬时软组织变化；不得改变头骨、眼睛永久形状、眉毛永久设计、鼻子、嘴唇永久几何、下颌/下巴比例、肤色或年龄。
- 用户已于 2026-09-12 明确判定 v002 合格并登记为 `OWNER_EXP_13_MOUTH_SLIGHTLY_OPEN_CANON_001`。该组件只定义上述三项同时出现的瞬时表情动作；可见身份、Hair A 和校准服装不因本次 Expression 批准取得新权威。
- Expression 当前计划为十三项并已完成 13/13；原计划中的独立轻微皱眉和自然闭眼已由用户永久移除，原列表第 15 项复合表情现改编号为第 13 项。完整 `owner_v1.0` 仍未锁定。

## POSE_01 当前候选目标

- 用户于 2026-09-13 在 Expression 13/13 完成后授权生成下一项 `POSE_01_RELAXED_STANDING_v001`。
- 候选只使用批准正面 Face、活动正面 Body 与批准正面 Hair-A 三项 Master 平行生成；不得输入任何 Expression、历史 Pose/Body 候选或 Shot 图像。
- 目标为成年角色正面放松站立的技术性关节校准姿态：头颈中立、肩膀自然下沉、双臂沿身体两侧放松且肘部不锁死、手掌和手指自然松弛、骨盆中立、双腿自然承重、膝盖不过伸、双脚完整接地且不交叉。
- 保持已批准的 168 cm / 60 kg、头身比、四肢长度、腰臀比、正面脸部身份与 Hairstyle-A；完整使用粉色高叉连体泳衣、连续覆盖至脚趾的 15D 肉色哑光/天鹅绒连裤丝袜并无鞋。
- 本项只允许定义 Pose 铰接后的放松站姿，不重新定义永久脸部、身体比例、发型、Expression、校准服装设计、丝袜材质、灯光或背景；候选状态必须保持 `REVIEW_REQUIRED`。
- 首次调用与一次压缩后的成年、非性感技术校准安全重试均在输出阶段被安全系统拦截，未产生任何图片；当前 `POSE_01` 状态为 `NO_OUTPUT_MODERATION_BLOCKED`，未批准且无可审核候选。停止继续改词重试，也不把现有 BODY_01 自动提升为 Pose Canon。

## 禁止写回规则

本次或后续 AI 候选中的光斑、阴影、皮肤瑕疵、妆容、背景、随机脸型变化和生成伪影不得自动写回本文件。只有用户明确选择的设计调整才能进入下一修订。

## 变更记录

| Revision | Date | Change | Approval |
|---|---|---|---|
| draft_0.1 | 2026-09-09 | 根据已登记 L0 照片建立首个保守身份锚；默认不主动改变真人身份 | awaiting review |
| draft_0.2 | 2026-09-09 | 用户指定 B 图为正脸长相/肤色 L1 锚；除 B 专属资产外统一使用 A 发型；拒绝 v001 后不吸收其特征 | user instruction incorporated |
| draft_0.3 | 2026-09-10 | 用户确认 v003 的长相/肤色与隔离方法正确；记录 B 源图俯视/仰头偏差，要求真正眼平重建；v003 图片本身不作为后续参考 | user scoped review incorporated |
| draft_0.4 | 2026-09-10 | 用户确认 v004 长相/肤色，但拒绝其发型及脸—头顶透视不一致；要求直接参考 DSC00847 发型，并把平视约束扩展到整颗头颅 | user scoped review incorporated |
| draft_0.5 | 2026-09-10 | 用户确认 v005 长相，指出头顶仍俯视、发型未充分匹配 DSC00847、肤色略浅；允许裁切 B 锚隔离头顶并要求肤色精确回归 B 图 | user scoped review incorporated |
| draft_0.6 | 2026-09-10 | 用户确认 v006 发型和平视，长相方向正确但细节与肤色轻微偏离 B 锚；后续遮蔽 DSC00847 面部以降低身份混合，同时复用已确认的文字方法而非 v006 图片 | user scoped review incorporated |
| draft_0.7 | 2026-09-10 | 用户确认 v007 发型与角度、拒绝其长相，并指定 v005 长相为正确目标；将 v005→v007 的脸部差异写成约束，但继续禁止把 v005/v007 作为像素输入 | user scoped review incorporated |
| draft_0.8 | 2026-09-10 | 用户指出 v008 与前两版差异不足且脸偏宽；下一版只轻微收窄面颊—下颌总宽，并恢复标准头肩/上胸构图以避免紧裁切放大脸宽观感 | user scoped review incorporated |
| draft_0.9 | 2026-09-10 | 将 v009 保留为未批准备选；按用户要求为 v010 合并 v005 的完整 B 图脸部/肤色方法与 v006 的发型/头顶机位方法，继续禁止候选图片串联 | user instruction incorporated |
| draft_0.10 | 2026-09-10 | 用户确认 v010 五官与肤色完美，唯一失败为头顶占比过多；v011 使用排除主要头顶的 B 上下文裁切，仅收紧头顶平视投影 | user scoped review incorporated |
| draft_0.11 | 2026-09-10 | 用户批准 v011 为当前 FACE_01 L1 Canon 组件；固化 v010 脸/肤色方法与 v011 头顶修正，并登记稳定复现方法和批准路径 | user approved component |
| draft_0.12 | 2026-09-10 | 记录 FACE_02 左 3/4 v001 的用户反馈：整体保留，只轻微降低颧骨显高度、圆润下巴收束并放松眼神；继续禁止以 v001 图像串联生成 | user scoped review incorporated |
| draft_0.13 | 2026-09-10 | 用户确认 FACE_02 左 3/4 v002 除下巴外均符合目标；下一版只进一步圆润下巴末端，其他已确认属性全部锁定，继续禁止候选图像串联 | user scoped review incorporated |
| draft_0.14 | 2026-09-10 | 用户拒绝 FACE_02 v003 的五官；下一版回到 v001 原始提示，仅追加颧骨、下巴、眼神三项小约束，不再累积 v002/v003 提示扩展 | user correction incorporated |
| draft_0.15 | 2026-09-10 | 用户批准 FACE_02 v004 为当前左 3/4 L1 Canon 组件；登记批准路径、作用范围、下游引用集和详细稳定复现方法 | user approved component |
| draft_0.16 | 2026-09-10 | 记录 FACE_03 v001 用户反馈：整体方法保留，仅下巴仍略尖；下一版只圆润下巴末端，保持其他五官与画面属性不变，且不使用 v001 像素 | user scoped review incorporated |
| draft_0.17 | 2026-09-10 | 用户批准 FACE_03 v002 为当前右 3/4 L1 Canon 组件；记录批准范围、右向身份职责、固定三输入恢复方式与禁止镜像/候选图串联规则 | user approved component |
| draft_0.18 | 2026-09-10 | 用户确认 FACE_05 右侧面 v001 除鼻子外均符合目标；下一版仅轻微缩小鼻尖体量与前向突出度，锁定鼻根/鼻梁、鼻翼/鼻孔、唇颏及所有其他属性，且不使用 v001 像素 | user scoped review incorporated |
| draft_0.19 | 2026-09-10 | 用户批准 FACE_05 v002 为当前右侧面 L1 Canon 组件；记录批准范围、鼻尖比例、固定三输入恢复方法与禁止生成图/镜像串联规则 | user approved component |
| draft_0.20 | 2026-09-10 | 将四个用户转码后的 JPG 登记为当前批准 Face Master 路径，更新校验值与统一查找索引；身份批准范围不变，候选 PNG 保留为溯源 | user format decision incorporated |
| draft_0.21 | 2026-09-10 | 用户授权生成 FACE_04 左侧面受限 v001；记录固定三输入、同侧真人证据的有限职责、禁止镜像/生成图串联，以及纯侧面几何在人工批准前仍未验证 | user generation authorization incorporated |
| draft_0.22 | 2026-09-10 | 用户批准 FACE_04 v001 为当前左侧面 L1 Canon 组件；记录批准路径、作用范围、固定三输入恢复方法，并保留无同方向真人纯侧脸独立验证的长期证据声明 | user approved component |
| draft_0.23 | 2026-09-10 | 五个 Face 组件完成后启动 BODY_01_FRONT v001；记录正面脸、两张真人身体上下文、遮脸 Hairstyle A 和丝袜材质的隔离职责，并确定无主动塑形的保守自然身体基线 | user generation authorization incorporated |
| draft_0.24 | 2026-09-10 | 记录 BODY_01 首次调用无输出后的安全重试：移除带床景/广告文字的丝袜像素参考，保持文字材质合同，并明确成年、非性感、技术校准语境 | safe generation retry |
| draft_0.25 | 2026-09-10 | BODY_01 第二次调用仍被输出安全系统拦截且无图；确认当前没有身体候选、没有可写回的身体事实，等待用户决定是否修改校准服装合同 | generation blocked pending user decision |
| draft_0.26 | 2026-09-11 | 将用户转码后的 FACE_04 JPG 登记为当前批准 Master，纠正误写为 FACE_05 的文件名并更新路径与校验值；批准范围不变，候选 PNG 保留为生成溯源 | user format decision incorporated |
| draft_0.27 | 2026-09-11 | 用户明确维持原 Body Calibration Outfit，拒绝短裤替代，因为其不能完全体现身体比例；授权 BODY_01 以独立 v002 候选恢复生成，身体几何仍须等待图片审核与明确批准 | user generation authorization incorporated |
| draft_0.28 | 2026-09-11 | 用户确认 BODY_01 v002 的长相和发型很好；v003 继续使用相同批准正面 Face、L0 身体上下文和遮脸 Hairstyle A 的平行方法，不使用 v002 像素，仅调整用户指定的腿长占比、腿轴和丝袜脚趾张力 | user scoped review incorporated |
| draft_0.29 | 2026-09-11 | 用户拒绝 BODY_01 v003 的腿轴、腿部占比和丝袜脚趾呈现；v004 累计提高腿部占比约 10%，要求真正平行直轴、无袜尖颜色分割线且酒红色趾甲从 15D 面料下自然透出；脸和发型仍按已确认源方法保持，禁止输入 v003 | user rejection and revision authorization incorporated |
| draft_0.30 | 2026-09-11 | 用户拒绝 BODY_01 v004；锁定当前腿部占比方向不再调整，v005 仅继续修正小腿直轴和丝袜全腿/足部织物可见度。脸与发型仍从既定批准/源参考恢复，禁止输入 v004 | user rejection and revision authorization incorporated |
| draft_0.31 | 2026-09-11 | 用户确认 BODY_01 v005 的腿部占比与腿部微光泽方向，拒绝其小腿外弯和裸足感；v006 只修正小腿直轴与脚背/脚趾 15D 织物雾化覆盖，继续从既定批准/源参考平行生成，禁止输入 v005 | user rejection and revision authorization incorporated |
| draft_0.32 | 2026-09-11 | 用户拒绝 BODY_01 v006，要求小腿再直并在保留足部丝袜朦胧感的同时恢复面料下酒红色甲油；v007 保持已确认的腿部占比、光泽、脸与发型方向，从既定源参考独立生成 | user rejection and revision authorization incorporated |
| draft_0.33 | 2026-09-11 | 用户确认 BODY_01 v007 除腰部过粗外其余方向均可保持；v008 仅轻微收窄腰围，保留自然体型、腿部比例/直轴、丝袜表现、脸与发型方向，并继续禁止候选图像串联 | user scoped review incorporated |
| draft_0.34 | 2026-09-11 | 用户批准 BODY_01 v008 为当前正面 Body L1 Canon 组件 `OWNER_BODY_01_FRONT_CANON_001`；固化下游 Master 与四输入源参考恢复方法，禁止批准图或候选图参与新的 L1 串图 | user approved component |
| draft_0.35 | 2026-09-11 | 用户将批准 BODY_01 Master 转换为 JPG 并删除批准 PNG；更新当前文件路径与指纹，候选 v008 PNG 保留溯源，批准范围和源参考恢复方法不变 | user format decision incorporated |
| draft_0.36 | 2026-09-11 | 用户复核当前 BODY_01 Canon：登记本人真实身体基准 168 cm、120 斤（约 60 kg）；当前图视觉偏矮且小腿仍不够直。v009 只修正身高感/整体比例与小腿直轴，保留已认可的脸、发型和丝袜质感，并继续禁止使用任何 Body 生成图像作为 L1 输入 | user correction and revision authorization incorporated |
| draft_0.37 | 2026-09-11 | 用户批准 BODY_01 v009 的长相、发型、四肢比例、腰臀比、腿脚几何及腿脚丝袜表现；晋升为活动组件 `OWNER_BODY_01_FRONT_CANON_002`，旧 001 标记为历史 superseded，四输入源恢复规则不变 | user approved component |
| draft_0.38 | 2026-09-11 | 用户明确扩展 002 的下游职责：168 cm / 60 kg、长相、HAIRSTYLE_A、四肢比例与腰臀比可供其他资产及视频镜头图片引用；丝袜职责严格限定为 15D 哑光肉色，不外推至其他颜色、材质/光泽或厚度 | user scope clarification incorporated |
| draft_0.39 | 2026-09-12 | 用户将活动 BODY_01 组件 002 的批准 PNG 转换为 `OWNER_BODY_01_FRONT_CANON.jpg` 并删除 PNG；更新活动路径与 JPG 指纹，格式变化不改变资产 ID、批准范围或源恢复方法 | user format decision incorporated |
| draft_0.40 | 2026-09-17 | 用户明确批准 BODY_01_FRONT_v015 并要求登记；新组件 003 采用略收窄腰部自然过渡到既有胯宽、当前腿型、源派生 Face recovery 与 Hair A 方法，以及浅肉色连续袜面、酒红甲油和趾间张力。v015 PNG 移动为新的活动 Master，002 保留为历史 superseded 组件 | user approved component and refined scope incorporated |
| draft_0.41 | 2026-09-17 | 用户确认后续所有资产的脸部生成统一采用 L0 真人素材/确定性源派生输入 + Face method prompt；批准 AI Face Canon 仅作生成后 `qa_comparison_only`，不得作为生成输入或身份 lineage | user rule confirmed and incorporated |
| draft_0.40 | 2026-09-12 | 用户批准 BODY_02 左 3/4 v001 为 `OWNER_BODY_02_LEFT_3Q_CANON_001`；登记其左 3/4 身体轮廓、深度与既有 168 cm / 60 kg 比例保持范围，并继续推进 BODY_03 | user approved component |
| draft_0.41 | 2026-09-12 | 用户拒绝 BODY_03 v001 的悬空脚跟与脚趾—前脚掌异常横线；v002 只修正两脚完整贴地及15D面料无缝连续性，保持既定右 3/4 身份、比例与构图方法，并禁止输入 v001 | user rejection and revision authorization incorporated |
| draft_0.42 | 2026-09-12 | 用户指出 v002 用脚跟下肉色垫块/多余组织伪造接地且脚趾横线仍在；撤销此前技术 PASS，v003 要求双脚轮廓互不遮挡、单一正常脚跟直接接地、无任何支撑物，并彻底消除脚趾—前脚掌线条，禁止输入 v001/v002 | user rejection and QA correction incorporated |
| draft_0.43 | 2026-09-12 | 用户确认 BODY_03 v003 其它方面完美，仅丝袜与脚部织物质感不足；v004 新增 `L0_HOS_15_NM_011` 作为严格 material-only 参考并保持 v003 成功属性的文字意图，禁止使用 v003 像素 | user scoped material feedback incorporated |
| draft_0.44 | 2026-09-12 | 用户批准 BODY_03 右 3/4 v005 为 `OWNER_BODY_03_RIGHT_3Q_CANON_001`；登记右向身体轮廓、比例、接地脚部与本组件内15D肉色哑光/天鹅绒丝袜表现，完整 owner_v1.0 仍未锁定 | user approved component |
| draft_0.45 | 2026-09-12 | 用户批准 BODY_04 左侧面 v002 为 `OWNER_BODY_04_LEFT_SIDE_CANON_001`；登记左侧面轮廓/深度、比例、接地、自然遮挡及本组件内15D肉色哑光/天鹅绒丝袜表现，完整 owner_v1.0 仍未锁定 | user approved component |
| draft_0.46 | 2026-09-12 | 用户批准 BODY_05 右侧面 v001 为 `OWNER_BODY_05_RIGHT_SIDE_CANON_001`；登记右侧面轮廓/深度、比例、接地、自然遮挡及本组件内15D肉色哑光/天鹅绒丝袜表现，BODY_06 成为剩余 Body 视角 | user approved component |
| draft_0.47 | 2026-09-12 | 用户批准 BODY_06 背面 v001 为 `OWNER_BODY_06_BACK_CANON_001`；登记完整背面轮廓/深度、比例、头身朝向、接地、保守发型后落及本组件内丝袜表现。六个 Body 组件全部批准，Gate 4 开放，完整 owner_v1.0 仍未锁定 | user approved component |
| draft_0.48 | 2026-09-12 | 用户确认 HAIR_A_01 正面 v001 除鼻部略大外其余方向可保持；将鼻部判定为候选漂移而非新身份事实，v002 必须回归批准 FACE_01 鼻部比例并修正发尾裁切，禁止使用 v001 像素 | user scoped review incorporated |
| draft_0.49 | 2026-09-12 | 用户明确批准 `HAIR_A_01_FRONT_v002`；按单文件规则晋升为 `OWNER_HAIR_A_01_FRONT_CANON_001`，仅批准眼平标准正面 Hairstyle-A 的分缝、体积、长直披散发束、色调/高光、完整长度与渐细发尾，不取得脸部或其他发型角度权威。Hair A 完成 1/6，完整 owner_v1.0 仍未锁定 | user approved component |
| draft_0.50 | 2026-09-12 | 用户拒绝当时编号为 EXP_15 的 v001，并重定义第 15 项为皱眉、闭眼、嘴巴克制张开；登记瞬时眉间/眼睑/唇周/下颌运动范围，明确 v001 禁止作为 v002 像素输入且表情不得重定义永久脸部身份。该组件后来于 draft_0.88 改编号为 EXP_13 | user correction incorporated; later renumbered |
| draft_0.51 | 2026-09-12 | 用户判定当时编号为 EXP_15 的 v002 合格并要求登记；仅批准皱眉、双眼闭合和嘴巴克制张开的复合瞬时表情，Expression 当时完成 1/15，完整 owner_v1.0 仍未锁定。该批准组件后来于 draft_0.88 无像素变更改编号为 `OWNER_EXP_13_MOUTH_SLIGHTLY_OPEN_CANON_001` | user approved component; later renumbered |
| draft_0.52 | 2026-09-12 | 用户将 JPG 直接放入批准目录并要求登记为第一项 Expression；规范命名为 `OWNER_EXP_01_NEUTRAL_CANON_001`，仅批准放松眉眼、平静直视与自然闭嘴的中性表情，明确排除永久身份、Hair-A、服装、灯光和背景职责，并如实记录生成溯源未声明。Expression 完成 2/15 | user supplied and approved component |
| draft_0.53 | 2026-09-12 | 用户授权生成下一项 `EXP_02_SUBTLE_SMILE_v001`；登记批准 Face、批准 Hair-A 和真人 `9.jpg` 的三项隔离职责，目标限定为闭嘴无露齿的双侧嘴角轻微上扬，并禁止使用 EXP_01、EXP_13 或任何候选图像串联 | user generation authorization incorporated |
| draft_0.54 | 2026-09-12 | `EXP_02_SUBTLE_SMILE_v001` 已从三项声明参考独立生成；技术预检确认双侧嘴角轻微上扬、嘴唇闭合无露齿、笑意强度低于普通微笑，身份/发型/机位/校准服装保持。候选继续为 `REVIEW_REQUIRED`，不取得 Canon 或下游参考资格 | candidate generated; awaiting user review |
| draft_0.55 | 2026-09-12 | 用户明确批准 `EXP_02_SUBTLE_SMILE_v001` 并要求登记；晋升为 `OWNER_EXP_02_SUBTLE_SMILE_CANON_001`，仅批准闭嘴无露齿、双侧嘴角轻微上扬及最小自然面颊/下眼睑响应。Expression 完成 3/15，完整 owner_v1.0 仍未锁定 | user approved component |
| draft_0.56 | 2026-09-12 | 用户授权生成下一项 `EXP_03_NATURAL_SMILE_v001`；登记批准 Face、批准 Hair-A 与真人 `9.jpg` 的三项隔离职责，目标为强于 EXP_02 但仍自然克制的闭嘴无露齿微笑，并禁止输入任何已生成 Expression 图像 | user generation authorization incorporated |
| draft_0.57 | 2026-09-12 | `EXP_03_NATURAL_SMILE_v001` 已从三项声明参考独立生成；技术预检确认闭嘴无露齿、自然嘴角/面颊抬起强于 EXP_02、下眼睑温和响应且未硬眯眼，身份/发型/机位/校准服装保持。候选继续为 `REVIEW_REQUIRED` | candidate generated; awaiting user review |
| draft_0.58 | 2026-09-12 | 用户明确批准 `EXP_03_NATURAL_SMILE_v001` 并要求登记；晋升为 `OWNER_EXP_03_NATURAL_SMILE_CANON_001`，仅批准闭嘴无露齿、自然平衡嘴角上扬、适度面颊抬起与温和下眼睑笑意。Expression 完成 4/15，完整 owner_v1.0 仍未锁定 | user approved component |
| draft_0.59 | 2026-09-12 | 用户授权生成下一项 `EXP_04_SMILE_WITH_TEETH_v001`；登记批准 Face、批准 Hair-A 与真人 `10.jpg` 的三项隔离职责，目标为自然中等强度露齿笑，限制牙龈显露和张嘴幅度，并禁止输入任何已生成 Expression 图像 | user generation authorization incorporated |
| draft_0.60 | 2026-09-12 | `EXP_04_SMILE_WITH_TEETH_v001` 已从三项声明参考独立生成；技术预检确认自然中等强度露齿笑、以上排牙齿为主、无明显牙龈、下颌开启克制且未达到大笑，身份/发型/机位/校准服装保持。候选继续为 `REVIEW_REQUIRED` | candidate generated; awaiting user review |
| draft_0.61 | 2026-09-12 | 用户拒绝 EXP_04 v001 并补充稳定笑容特征：人物解剖学右侧（正面画面左侧）有自然轻微突出的虎牙，笑时出现自然酒窝/笑窝，`2.jpg` 正面画面右侧更清楚。v002 只从批准 Face、批准 Hair-A 与真人 `2.jpg` 平行重建，禁止输入 v001；同时排除婚纱妆容/精修、手、另一人物、服装与背景 | user identity correction incorporated |
| draft_0.62 | 2026-09-12 | EXP_04 v002 已按修正后的三项平行参考生成；技术预检确认右侧虎牙方向正确、突出度自然克制，并出现轻微笑窝响应。候选继续为 `REVIEW_REQUIRED`，不自动写回为已批准 Expression Canon | corrected candidate generated; awaiting user review |
| draft_0.63 | 2026-09-12 | 用户明确批准 EXP_04 v002 并要求登记；晋升为 `OWNER_EXP_04_SMILE_WITH_TEETH_CANON_001`，仅批准自然中等强度露齿笑、人物右侧虎牙的正确方向/自然显露、上排牙齿显露方式与笑时酒窝响应。Expression 完成 5/15，完整 owner_v1.0 仍未锁定 | user approved component |
| draft_0.64 | 2026-09-13 | 用户授权继续生成 EXP_05 开心大笑；登记批准 Face、批准 Hair-A、真人 `DSC01015.JPG` 大笑动作与真人 `2.jpg` 虎牙/酒窝补充的四项隔离职责，目标明显强于 EXP_04 但排除尖叫、惊讶与漫画式狂笑，并禁止输入任何生成 Expression 图 | user generation authorization incorporated |
| draft_0.65 | 2026-09-13 | EXP_05 v001 已从四项声明参考独立生成；技术预检确认自然开心大笑、适中张嘴、面颊/下眼睑联动、人物右侧虎牙方向及轻微笑窝响应，身份/发型/机位/校准服装保持。候选继续为 `REVIEW_REQUIRED` | candidate generated; awaiting user review |
| draft_0.66 | 2026-09-13 | 用户要求继续下一项，EXP_05 保持未批准且不输入后续；授权 EXP_06 自然惊讶，以批准 Face、批准 Hair-A 与真人 `8.jpg` 三项隔离职责生成，排除盘发、托脸双手、针织衫、暖光和背景，禁止恐惧/尖叫/大笑及漫画式变形 | user generation authorization incorporated |
| draft_0.67 | 2026-09-13 | EXP_06 v001 已从批准 Face、批准 Hair-A 与真人 `8.jpg` 独立生成；技术预检确认适度抬眉、眼睑打开、克制微张嘴和中性嘴角成立，无恐惧/尖叫/笑意及 L0 场景残留。候选继续为 `REVIEW_REQUIRED` | candidate generated; awaiting user review |
| draft_0.68 | 2026-09-13 | 用户明确表示 EXP_06 审核通过并要求开始下一项；晋升为 `OWNER_EXP_06_SURPRISED_CANON_001`，仅批准自然适度抬眉、眼睑打开、克制微张嘴和警觉注视。Expression 完成 6/15，EXP_05 仍未批准，完整 owner_v1.0 未锁定 | user approved component and requested next asset |
| draft_0.69 | 2026-09-13 | 用户授权生成 EXP_07 困惑/好奇；完整复核 L0 后确认无匹配真人表情源，登记该覆盖缺口并仅以批准 Face、批准 Hair-A 两项最小参考独立生成。目标限定为克制眉部不对称、疑问专注眼神与中性嘴部，禁止歪头、夸张单眉及向惊讶/恼怒/悲伤漂移，也禁止输入任何 Expression 生成图 | user next-candidate authorization incorporated; source-coverage gap recorded |
| draft_0.70 | 2026-09-13 | EXP_07 v001 已从批准 Face 与批准 Hair-A 两项 Master 独立生成；技术预检确认克制眉部不对称、疑问专注眼神、中性闭嘴和正直头位成立，身份/发型/机位/校准服装保持。候选继续为 `REVIEW_REQUIRED`，不自动取得 Canon 资格 | candidate generated; awaiting user review |
| draft_0.71 | 2026-09-13 | 用户明确批准 EXP_07，并追溯批准此前待审的 EXP_05；分别晋升为 `OWNER_EXP_07_CONFUSED_CURIOUS_CANON_001` 与 `OWNER_EXP_05_HAPPY_LAUGHING_CANON_001`。EXP_07 保留无匹配 L0 的覆盖限制；两项批准均只作用于声明的瞬时表情，不重定义永久身份。Expression 完成 8/15，完整 owner_v1.0 未锁定 | user approved two components |
| draft_0.72 | 2026-09-13 | 用户授权生成 EXP_08 轻微不悦；登记无匹配 L0 表情源的覆盖缺口，仅用批准 Face 与批准 Hair-A 两项 Master 独立生成。目标限定为小幅内眉张力、轻度眼睑收窄、克制不耐注视和轻微压唇，明确弱于愤怒，并与专注及后来撤销的独立轻微皱眉设计分离；禁止输入任何生成 Expression 图 | user next-candidate authorization incorporated; source-coverage gap recorded |
| draft_0.73 | 2026-09-13 | EXP_08 v001 已从批准 Face 与批准 Hair-A 两项 Master 独立生成；技术预检确认轻微不悦的眉眼/压唇组合成立且强度克制，身份、Hair-A、机位与校准服装保持。候选继续为 `REVIEW_REQUIRED`，不自动取得 Canon 资格 | candidate generated; awaiting user review |
| draft_0.74 | 2026-09-13 | 用户批准 EXP_08 并授权下一项；EXP_08 晋升为 `OWNER_EXP_08_MILDLY_ANNOYED_CANON_001`，批准范围限定为低强度轻微不悦并保留无匹配 L0 的来源限制。登记 EXP_09 难过/担忧目标与无匹配 L0 覆盖缺口，仅用批准 Face 与 Hair-A 独立生成，限定轻微内眉上提靠拢、柔和担忧注视、闭嘴嘴角轻微下垂和极小下巴张力 | user approved component and authorized next candidate |
| draft_0.75 | 2026-09-13 | EXP_09 v001 已从批准 Face 与批准 Hair-A 两项 Master 独立生成；技术预检确认克制难过/担忧的眉眼、嘴角与下巴软组织响应成立，无哭泣或漫画夸张，身份、Hair-A、机位与校准服装保持。候选继续为 `REVIEW_REQUIRED`，不自动取得 Canon 资格 | candidate generated; awaiting user review |
| draft_0.76 | 2026-09-13 | 用户批准 EXP_09 并授权下一项；EXP_09 晋升为 `OWNER_EXP_09_SAD_CONCERNED_CANON_001` 并保留无匹配 L0 的来源限制。登记 EXP_10 专注/认真目标与专门 L0 覆盖缺口，仅用批准 Face 与 Hair-A 独立生成；限定稳定直接注视、极轻眼睑收束、近中性眉毛和放松闭嘴，明确排除 EXP_08 式不耐压唇及后来撤销的独立轻微皱眉设计 | user approved component and authorized next candidate |
| draft_0.77 | 2026-09-13 | EXP_10 v001 已从批准 Face 与 Hair-A 两项 Master 独立生成；技术预检确认稳定专注注视、极轻眼睑参与、近中性眉毛与放松闭嘴成立，无不悦压唇或明显皱眉。候选保持 `REVIEW_REQUIRED` | candidate generated; awaiting user review |
| draft_0.78 | 2026-09-13 | 用户授权生成 EXP_11 明确愤怒；EXP_10 保持未批准且不输入后续。现有 L0 无可靠愤怒源，登记覆盖缺口并仅用批准 Face 与 Hair-A 两项 Master；瞬时动作限定为明确但受控的内眉内下收紧、自然眉间张力、收窄直接注视、闭嘴压唇及轻度下颌张力，排除暴怒、吼叫、露齿、仇恨威胁感和永久脸部几何改变 | user next-candidate authorization incorporated; source-coverage gap recorded |
| draft_0.79 | 2026-09-13 | EXP_11 v001 已从批准 Face 与 Hair-A 两项 Master 独立生成；技术预检确认明确但受控的愤怒眉眼、闭嘴压唇和轻度下颌张力成立，强于轻微不悦且无暴怒/吼叫/威胁化。身份、发型、机位与校准服装保持，候选继续为 `REVIEW_REQUIRED` | candidate generated; awaiting user review |
| draft_0.80 | 2026-09-13 | 用户明确确认 EXP_10 与 EXP_11 均合格并要求一起登记；分别晋升为 `OWNER_EXP_10_FOCUSED_SERIOUS_CANON_001` 与 `OWNER_EXP_11_ANGRY_CANON_001`。两项只取得各自瞬时表情动作权威并保留无匹配 L0 的来源限制，不重定义永久脸部或发型。Expression 完成 12/15，完整 `owner_v1.0` 未锁定 | user approved two components |
| draft_0.81 | 2026-09-13 | 用户授权生成 EXP_12 害羞；登记真人 `13.jpg` 仅提供轻微下移/回避目光、克制闭嘴小笑与害羞软组织方向，排除其低头转面、手势、婚纱妆容、服装、发型、背景、肤色与永久身份。候选保持正直眼平头位，仅允许极轻暂时性面颊暖意，禁止明显腮红或永久肤色改变，并禁止输入任何生成 Expression 图 | user next-candidate authorization incorporated; limited L0 expression scope registered |
| draft_0.82 | 2026-09-13 | EXP_12 v001 已从批准 Face、批准 Hair-A 与受限真人 `13.jpg` 独立生成；技术预检确认正直头位下的轻微侧下回避目光、克制闭嘴小笑与柔和眼睑/面颊响应成立，无手势、歪头、明显腮红或婚纱场景残留。永久身份、发型和肤色保持，候选为 `REVIEW_REQUIRED` | candidate generated; awaiting user review |
| draft_0.83 | 2026-09-13 | 用户拒绝 EXP_12 v001 并要求 v002 头部适度低下一些、脸颊出现轻微自然局部泛红、闭嘴笑意略增强。v001 禁止作为像素输入或下游参考；v002 继续从批准 Face、Hair-A 与受限真人 `13.jpg` 平行重建，泛红只属于瞬时害羞反应，不改变永久肤色 | user scoped rejection and regeneration authorization incorporated |
| draft_0.84 | 2026-09-13 | EXP_12 v002 已从批准 Face、Hair-A 与受限真人 `13.jpg` 独立生成，未输入 v001；技术预检确认适度低头、侧下回避目光、轻微对称局部泛红及略增强的闭嘴笑意同时成立，且基础肤色、永久身份与 Hair-A 保持。候选为 `REVIEW_REQUIRED` | corrected candidate generated; awaiting user review |
| draft_0.85 | 2026-09-13 | 用户明确确认 EXP_12 v002 合格；晋升为 `OWNER_EXP_12_SHY_CANON_001`，仅批准适度低头、侧下回避目光、轻微局部暂时性泛红和克制闭嘴笑意等瞬时害羞动作，不定义永久肤色或脸部身份。v001 保持拒绝。Expression 完成 13/15，完整 `owner_v1.0` 未锁定 | user approved corrected component |
| draft_0.86 | 2026-09-13 | 用户曾授权生成当时原第 13 项的独立轻微皱眉候选；现有 L0 无可靠匹配源，仅用批准 Face 与 Hair-A 独立生成。该计划项后来于 draft_0.88 被用户永久撤销 | historical generation authorization; later retired by user |
| draft_0.87 | 2026-09-13 | 当时原第 13 项独立轻微皱眉候选曾通过技术预检但从未获批；其候选图与记录后来于 draft_0.88 按用户要求删除，始终不具备下游参考资格 | historical unapproved candidate; later deleted by user |
| draft_0.88 | 2026-09-13 | 用户永久移除独立“轻微皱眉”和“自然闭眼”两项；轻微皱眉未批准候选及记录已删除，自然闭眼从未生成。原列表第 15 项已批准复合表情无重生成改编号为 `EXP_13_MOUTH_SLIGHTLY_OPEN` / `OWNER_EXP_13_MOUTH_SLIGHTLY_OPEN_CANON_001`，像素校验值不变。Expression 计划缩减并完成为 13/13，完整 `owner_v1.0` 未锁定 | user retired two assets and renumbered approved component |
| draft_0.89 | 2026-09-13 | 用户授权开始 `POSE_01_RELAXED_STANDING_v001`；固定批准正面 Face、活动正面 Body 与批准正面 Hair-A 三项并行来源，目标为保持 168 cm / 60 kg、身份、发型、校准服装和连续 15D 丝袜的正面放松站姿。Pose 只定义自然承重与关节松弛，不重定义永久身体或其他属性，状态 `REVIEW_REQUIRED` | user next-asset authorization incorporated |
| draft_0.90 | 2026-09-13 | POSE_01 首次调用及一次成年、非性感技术校准安全重试均在输出阶段被 sexual 类别拦截，无候选图片产生。停止继续改词重试；POSE_01 保持未生成、未批准，现有 BODY_01 不自动取得 Pose 权威 | generation blocked; no output |
| draft_0.91 | 2026-09-13 | 用户再次要求生成下一项，重新授权 `POSE_01_RELAXED_STANDING_v002` 独立尝试。继续只使用批准正面 Face、活动正面 Body 与批准正面 Hair-A，v001 无输出且不参与；Pose 只定义自然放松站姿与关节松弛，保持既有身份、168 cm / 60 kg 身体比例、Calibration Outfit 和连续 15D 肉色哑光丝袜 | user retry authorization incorporated |
| draft_0.92 | 2026-09-13 | `POSE_01_RELAXED_STANDING_v002` 的精简成年技术校准调用再次在输出阶段被 sexual 类别拦截，无图产生。该调用不提供任何身份或姿态证据，POSE_01 仍未生成、未批准；现有批准 Face、Body、Hair-A 状态不变 | generation blocked; no output |
| draft_0.93 | 2026-09-13 | 用户明确批准将活动 `OWNER_BODY_01_FRONT_CANON_002` 的既有中性正面站姿复用为 `POSE_01_RELAXED_STANDING` 姿态 Canon，不产生第二份像素；批准范围只增加该图可见的正面站姿，不扩展身体身份或其他动作。用户同时授权 `POSE_02_WALKING_NEUTRAL_STRIDE_v001`，使用 BODY_01 Master 与真人 `4.jpg` 的受限步态职责平行生成 | user approved reuse and authorized next candidate |
| draft_0.94 | 2026-09-13 | `POSE_02_WALKING_NEUTRAL_STRIDE_v001` 已从 BODY_01 Master 与真人 `4.jpg` 的步态职责独立生成，未输入 POSE_01。技术预检确认自然正面行走的腿部交替、动态承重和反向手臂摆动成立，批准身份、168 cm / 60 kg 身体基准、HAIRSTYLE_A 与 Calibration Outfit 基本保持；候选为 `REVIEW_REQUIRED` | candidate generated; awaiting user review |
| draft_0.95 | 2026-09-13 | 用户明确批准 `POSE_02_WALKING_NEUTRAL_STRIDE_v001`，其范围只覆盖当前自然行走的腿部交替、动态承重和反向手臂摆动，不重新定义永久身体。用户同时授权 `POSE_03_SEATED_UPRIGHT_v001`；由于无登记真人坐姿源，候选只使用活动 BODY_01 Master 并以文字约束直立坐姿，禁止使用任何生成 Pose 作为输入 | user approved component and authorized next candidate; seated-source gap disclosed |
| draft_0.96 | 2026-09-13 | `POSE_03_SEATED_UPRIGHT_v001` 已从活动 BODY_01 Master 独立生成；技术预检确认直立坐姿的骨盆/脊柱稳定、自然髋膝屈曲、竖直小腿、平放双脚和轻置大腿的双手成立，身份、168 cm / 60 kg 身体基准、HAIRSTYLE_A 与 Calibration Outfit 基本保持。无真人坐姿源限制继续保留，候选为 `REVIEW_REQUIRED` | candidate generated; awaiting user review |
| draft_0.97 | 2026-09-13 | 用户拒绝 `POSE_03_SEATED_UPRIGHT_v001` 的脸部，指出脸部应直接由专用 L1 Face 资产约束，当前图有迭代污染与明显敏感斑块；坐姿及其他属性可保持。v001 禁止作为 v002 像素输入。v002 使用批准 FACE_01、活动 BODY_01 与批准 HAIR_A_01 三项职责隔离 Master 平行生成，脸部要求保持批准五官、中性肤色与自然均匀皮肤，禁止斑驳红块、脏污阴影及皮肤伪影 | user identity/skin correction incorporated |
| draft_0.98 | 2026-09-13 | `POSE_03_SEATED_UPRIGHT_v002` 已从三个批准 L1 Master 独立生成，未使用 v001。技术预检确认脸部重新对齐批准 FACE_01 的五官、脸宽、下颌和中性肤色，皮肤自然均匀，未见明显敏感斑块、脏污阴影或不对称污染；坐姿与 Calibration Outfit 保持，候选为 `REVIEW_REQUIRED` | corrected candidate generated; awaiting user review |
| draft_0.99 | 2026-09-13 | 用户确认 `POSE_03_SEATED_UPRIGHT_v002` 脸部合格，其余属性亦可保持，唯一修正为恢复稳定外观特征酒红色脚趾甲油。v003 不输入 v002，仍从批准 Face/Body/Hair-A 三项 L1 Master 独立生成；十枚脚趾甲的深酒红色须在连续 15D 肉色丝袜纤维下自然柔化透出，不得画在面料表面或改变足部/丝袜几何 | user appearance correction incorporated |
| draft_0.100 | 2026-09-13 | `POSE_03_SEATED_UPRIGHT_v003` 已从三个批准 L1 Master 独立生成，未使用 v001/v002。技术预检确认已认可脸部与均匀中性皮肤保持，酒红色脚趾甲油在连续 15D 肉色丝袜下以柔和低饱和方式自然可见，未改变脚趾几何、丝袜连续性或手指甲；候选为 `REVIEW_REQUIRED` | corrected candidate generated; awaiting user review |
| draft_0.101 | 2026-09-13 | 用户明确批准并要求登记 `POSE_03_SEATED_UPRIGHT_v003`，晋升为 `OWNER_POSE_03_SEATED_UPRIGHT_CANON_001`。该组件只批准直立坐姿关节关系和本图中合规的丝袜下酒红色脚趾甲表现，不重新定义永久身份、身体比例、HAIRSTYLE_A、丝袜 Material Canon 或指甲色 Canon；v001/v002 继续禁止使用 | user approved component |
| draft_0.102 | 2026-09-13 | 用户授权生成 `POSE_04_SEATED_RELAXED_v001`。候选从批准 FACE_01、活动 BODY_01 与批准 HAIR_A_01 三项 L1 Master 平行生成，不使用 POSE_03 或其他生成 Pose；保持已确认的精确脸、均匀中性皮肤、168 cm / 60 kg 身体、HAIRSTYLE_A、Calibration Outfit、连续 15D 肉色丝袜及丝袜下酒红色脚趾甲，新增权威仅限自然轻靠的放松坐姿 | user next-candidate authorization incorporated |
| draft_0.103 | 2026-09-13 | POSE_04 v001 在一次无输出安全拦截后，从同一三项批准 Master 独立生成成功；未使用 POSE_03 或其他 Pose 像素。技术预检确认专用 Face 约束下的五官与均匀皮肤、168 cm / 60 kg 身体、HAIRSTYLE_A、Calibration Outfit、连续 15D 丝袜及丝袜下酒红色脚趾甲保持；候选只申请放松坐姿权威且继续待用户审核 | candidate generated; awaiting user review |
| draft_0.104 | 2026-09-13 | 用户明确批准 POSE_04 v001，晋升为 `OWNER_POSE_04_SEATED_RELAXED_CANON_001`。该组件只批准靠背支撑下的克制放松坐姿、松弛上肢、分置腿部的双手、非交叉膝部及前后错开的平放双脚，不重新定义永久身份、身体比例、HAIRSTYLE_A、服装、丝袜/甲色或椅子；完整 `owner_v1.0` 未锁定 | user approved component |
| draft_0.105 | 2026-09-13 | 用户明确批准避免重复，复用 `OWNER_BODY_02_LEFT_3Q_CANON_001` 的约 35–45° 左 3/4 中性站姿作为 `POSE_05_SLIGHT_BODY_TURN`。同一唯一物理文件同时承担 Body 左 3/4 几何与经单独批准的轻微转身姿态职责，不产生第二份像素，也不扩展永久身份、材质、服装或其他 Pose 权威 | user approved scoped reuse |
| draft_0.106 | 2026-09-13 | 用户授权生成 `POSE_06_BENDING_REACHING_v001`；登记无匹配真人动作源的覆盖缺口，并以批准左 3/4 Face、左 3/4 Body、正面 Hair-A 三项 Master 平行构建。候选只申请自然髋折叠、轻屈膝、稳定错步及单臂前下伸的动作权威，不使用任何 Pose 图，也不重新定义永久身份、168 cm / 60 kg 身体、HAIRSTYLE_A、服装或丝袜/甲色 | user next-candidate authorization incorporated; source gap disclosed |
| draft_0.107 | 2026-09-13 | POSE_06 v001 已从三项批准 Master 独立生成；身份、左 3/4 方向、HAIRSTYLE_A 与身体基准在技术预检范围内保持，但后侧脚跟抬起，未达到双脚稳定接地的动作合同。该问题只属于 Pose/接地 QA，不写回身份锚；v001 不具下游资格并建议独立重做 | candidate generated; pose QA failure |
| draft_0.108 | 2026-09-13 | 用户纠正：双脚完整平放仅为 Body 中性校准要求，Pose 应按动作本身判断；POSE_06 v001 的后脚自然抬跟不构成失败，姿态与身份均可保持。唯一修订项为脚部丝袜织物感不足、近似裸足；v002 不输入 v001，仍从批准 Face/Body/Hair-A 平行重建，并增加用户指定15D肤色哑光材质派生图，只增强连续织物存在、透明度与足部柔化，不改变动作、身份、身体、肤色、甲色或足部解剖 | user QA correction and scoped material revision |
| draft_0.109 | 2026-09-13 | POSE_06 v002 在一次无输出安全拦截后从批准 Face/Body/Hair-A 与用户指定15D肤色哑光材质派生图独立生成成功，未输入 v001。技术预检确认身份与 Hairstyle-A 保持、动作中自然抬跟的承重关系合理，腿脚及完整足部的15D哑光织物存在感明显增强且甲色仍在面料下柔化可见；候选待用户审核，不写回永久身份或 Material Canon | corrected candidate generated; awaiting user review |
| draft_0.110 | 2026-09-14 | 用户确认 POSE_06 v002 的动作、表情与身体比例合格，但拒绝其多余大腿上部褶皱、偏白袜色及脚趾刷白感。v002 不具下游资格；v003 不输入 v002，只从批准 Face/Body/Hair-A 与受限材质派生图平行重建。身份与身体成功项仅以文字保持；袜色由 Body Master 的浅肉色定义，材质图只传递15D织物/透明度/覆盖，脚趾必须呈织物在上、解剖与酒红甲色在下的柔和扩散关系 | user scoped material correction; identity anchors unchanged |
| draft_0.111 | 2026-09-14 | POSE_06 v003 的首次调用与一次精简技术表述重试均在输出阶段被安全系统拦截，无图产生。该失败不改变批准身份、身体或 Hair-A，也不提供新的 Pose/Material 证据；v003 未批准且不可用于下游 | generation blocked; identity anchors unchanged |
| draft_0.112 | 2026-09-14 | 用户明确批准 POSE_06 v002；其唯一图片移动晋升为 `OWNER_POSE_06_BENDING_REACHING_CANON_001`。批准只增加弯身/伸手动作权威，不重新定义永久身份、身体、Hair-A、服装或丝袜/甲色。此前指出的多余大腿褶皱、偏白袜色及脚趾刷白感记录为已知限制，严禁下游从该 Pose 提取材质或颜色；完整 `owner_v1.0` 未锁定 | user approved pose component with material exclusions |
| draft_0.113 | 2026-09-14 | 用户授权下一项 POSE_07。候选从批准右 3/4 Face、右 3/4 Body 和 Hair-A 三项 Master 独立生成，以文字定义稳定半跪—低蹲过渡位，只申请髋膝踝折叠、单膝接触、前脚承重与上肢平衡的 Pose 权威。不得输入 POSE_06 或其他生成 Pose；缺失的 `IMG_2579/2580` 不作为输入，身份、身体与丝袜规则不因该覆盖缺口改变 | user next-pose authorization; identity anchors unchanged |
| draft_0.114 | 2026-09-14 | POSE_07 v001 的完整技术调用及两次逐步精简的临床姿态调用均在输出阶段被安全系统拦截，无图产生。失败调用不提供新的动作、身份、身体或材质证据；POSE_07 保持未生成、未批准且不可用于下游 | generation blocked; identity anchors unchanged |
| draft_0.115 | 2026-09-14 | 用户授权独立重试 `POSE_07_KNEELING_CROUCHING_v002`。继续从批准右 3/4 Face、右 3/4 Body 与 Hair-A 三项 Master 平行生成，不输入无输出 v001、任何 Pose/Expression 候选或 Shot；本次只申请既定半跪—低蹲关节姿态权威，不改变永久身份、身体、发型或材质规则 | user retry authorization; identity anchors unchanged |
| draft_0.116 | 2026-09-14 | POSE_07 v002 的完整调用与一次定向精简调用均在输出阶段被安全系统拦截，无图产生。失败调用不提供新的身份、身体、发型、动作或材质证据；批准 Master 和身份锚均保持不变，v002 不可用于下游 | generation blocked; identity anchors unchanged |
| draft_0.117 | 2026-09-14 | 用户决定暂缓多次无输出的 POSE_07 并继续 POSE_08。`POSE_08_SEATED_LEGS_EXTENDED_v001` 从批准正面 FACE_01、活动正面 BODY_01 与批准 HAIR_A_01 三项 Master 平行重建，不输入任何 Pose/Expression/Shot；只申请坐地直立、双腿前伸、膝踝足方向与髋侧轻支撑的 Pose 权威。永久身份、168 cm / 60 kg 身体、HAIRSTYLE_A、服装及丝袜规则均不改变 | user next-pose authorization; identity anchors unchanged |
| draft_0.118 | 2026-09-14 | POSE_08 v001 在一次输出安全拦截后由同一三项批准 Master 独立生成成功；正面身份、身体基准与 Hair-A 在技术预检范围内保持，姿势关系成立，但腿脚 15D 织物存在感不足、脚趾近似裸足。该问题只属于候选材质呈现，不写回身份锚；v001 未批准且不可用于下游 | candidate generated; hosiery QA failure; identity anchors unchanged |
| draft_0.119 | 2026-09-14 | 用户拒绝 POSE_08 v001 的正面视角、绷直脚部与不可读的丝袜质感，并授权 v002 改为约 45° 左 3/4、自然松弛膝踝脚趾及清晰连续的15D肉色哑光织物。v002 不输入 v001，改用批准左 3/4 Face/Body、Hair-A 与受限材质派生图平行重建；永久身份、168 cm / 60 kg 身体、Hair-A、肤色、甲色与服装规则不改变 | user scoped pose/material correction; identity anchors unchanged |
| draft_0.120 | 2026-09-14 | POSE_08 v002 在一次输出安全拦截后成功生成；左 3/4 身份、身体与 Hair-A 在技术预检范围内保持，约45°视角和自然松弛膝踝脚趾成立。但丝袜偏白且不够透明、甲色灰白，属于材质参考颜色泄漏，不写回身份、肤色或甲色锚；v002 未批准且不可用于下游 | candidate generated; hosiery color/opacity failure; identity anchors unchanged |
| draft_0.121 | 2026-09-14 | 用户澄清 POSE_08 v003 应保持双腿完全伸直、双脚相对小腿约90°并以足底朝镜头，约45°左3/4视角中主要只见双脚脚底；丝袜为肤色15D且足底/趾端连续覆盖可读。v002 标记用户拒绝，不输入 v003；材质参考改用登记的足底 L0，仅定义织物而不定义身份、身体、姿势或场景。永久身份与身体锚不变 | user pose/sole-material clarification; identity anchors unchanged |
| draft_0.122 | 2026-09-14 | POSE_08 v003 的完整调用与一次精简重试均在输出阶段被安全系统拦截，无图产生。失败调用不提供新的身份、身体、姿势或材质证据；批准 Face/Body/Hair-A、肤色、甲色及丝袜规则均保持不变，v003 不可用于下游 | generation blocked; identity anchors unchanged |
| draft_0.123 | 2026-09-14 | 用户明确要求先登记 POSE_08 v002；其唯一图片移动晋升为 `OWNER_POSE_08_SEATED_LEGS_EXTENDED_CANON_001`。批准只增加约45°左3/4坐地、双腿前伸分离、自然松弛膝踝脚趾和髋侧手支撑的 Pose 权威；未完全直腿/非足底主视角、偏白偏厚丝袜及灰白甲色均为排除项，不改变永久身份、身体、肤色、甲色或丝袜锚 | user approved pose component with geometry/material exclusions |
| draft_0.124 | 2026-09-14 | 用户授权生成下一项 POSE_09。候选从批准左 3/4 Face、左 3/4 Body 与 Hair-A 三项 Master 独立生成，不输入任何 Pose、Expression 或 Shot；以文字定义中立四点支撑/手膝位，只申请双掌—肩肘腕支撑、水平中立脊柱、髋下双膝及向后折叠小腿/脚背接地的 Pose 权威。当前无匹配真人动作源；永久身份、168 cm / 60 kg 身体、HAIRSTYLE_A、Calibration Outfit 与连续 15D 肤色丝袜规则均不改变 | user next-pose authorization; identity anchors unchanged |
| draft_0.125 | 2026-09-14 | POSE_09 v001 的完整技术调用与一次物理治疗体位精简重试均在输出阶段被安全系统拦截，无图产生。失败调用不提供新的身份、身体、发型、动作或材质证据；批准 Face/Body/Hair-A 与现有身份锚保持不变，v001 不可审核或用于下游 | generation blocked; identity anchors unchanged |
| draft_0.126 | 2026-09-14 | 用户修正后续 POSE_09 脚部动作：双脚以前脚掌/脚趾腹着地，脚趾自然屈曲、脚跟抬起，不再采用脚背贴地。该变化只属于 Pose 的足踝/跖趾关节和接地合同，不改变永久足部比例、身体身份、丝袜规则或 v001 无输出状态；本轮不触发生成 | user pose correction; identity anchors unchanged |
| draft_0.127 | 2026-09-14 | 用户授权按修订后的前掌/脚趾腹接地合同继续生成 POSE_09 v002。v002 从批准左 3/4 Face、左 3/4 Body 与 Hair-A 三项 Master 独立调用，未输入任何 Pose；完整调用与一次临床四点支撑精简调用均在输出阶段被安全系统拦截，无图产生。失败调用不提供新的身份、身体、发型、动作或材质证据；现有身份锚保持不变，v002 不可审核或用于下游 | generation blocked; identity anchors unchanged |
| draft_0.128 | 2026-09-14 | 用户授权重新生成 POSE_07 v003。v003 从批准右 3/4 Face、右 3/4 Body 与 Hair-A 三项 Master 独立调用，未输入任何 Pose；动作采用直立临床半跪弓步评估。完整调用与一次精简调用均在输出阶段被安全系统拦截，无图产生。失败调用不提供新的身份、身体、发型、动作或材质证据；现有身份锚保持不变，v003 不可审核或用于下游 | generation blocked; identity anchors unchanged |
| draft_0.129 | 2026-09-14 | 用户决定暂缓 POSE_07/09 并开始 Gate 7。首项 `HOS_01_LOWER_LEGS_FEET_FRONT_v001` 只申请正面膝下至双脚的足部比例、连续15D肉色哑光/天鹅绒织物与织物下自然柔化酒红甲色权威；使用活动正面 Body Master 定义女主几何/肉色，用户指定材质裁切仅定义织物存在与覆盖。该 Gate 转换不改变永久脸、整体身体、发型、肤色或 Calibration Outfit 身份锚 | user Gate-7 authorization; identity anchors unchanged |
| draft_0.130 | 2026-09-14 | HOS_01 v001 在一次安全拦截后仅从活动正面 Body Master 成功生成。小腿/足部几何与正面构图基本保持，但脚趾根部横向材质边界和过于表面的酒红甲色触发技术 QA 失败；这些伪影不写回足部、甲色或丝袜身份锚。v001 未批准且不可用于下游 | candidate generated; material continuity QA failed; identity anchors unchanged |
| draft_0.131 | 2026-09-14 | 用户授权独立生成 HOS_01 v002，只修正趾根横向边界与表面化甲色。v001 不作为像素输入；活动正面 Body Master 定义女主足部几何，足部材质裁切仅定义15D织物在踝、脚背与脚趾上的连续覆盖和柔化层级。永久足形、肉色与酒红甲色规则不变 | user scoped hosiery correction; identity anchors unchanged |
| draft_0.132 | 2026-09-14 | HOS_01 v002 在一次两参考安全拦截后仅从活动正面 Body Master 成功生成。甲色柔化方向改善，但趾根仍有横向材质边界，技术 QA 继续失败；残留边界不写回丝袜锚，v002 未批准且不可用于下游。永久足形、肉色与酒红甲色规则不变 | candidate generated; nail improved; material continuity still failed |
| draft_0.133 | 2026-09-14 | 用户授权独立生成 HOS_01 v003，唯一目标是消除脚趾根部横向边界并恢复脚背—前掌—脚趾的连续袜面。v001/v002 均不作为像素输入；仅使用活动正面 Body Master，v002 的甲色柔化方向只以文字保留。本次修正不改变永久足形、肉色、酒红甲色或其他身份锚 | user single-issue hosiery correction; identity anchors unchanged |
| draft_0.134 | 2026-09-14 | HOS_01 v003 已仅从活动正面 Body Master 独立生成；整体丝袜均匀度和织物下甲色方向保持，但趾根仍有浅横向明暗/透明度边界，技术 QA 未通过。该伪影不写回丝袜、足形、肤色或甲色身份锚；v003 未批准且不可用于下游 | candidate generated; residual material boundary; identity anchors unchanged |
| draft_0.135 | 2026-09-14 | 用户明确判定 HOS_01 v003 合格并要求记录；人工审核将浅趾根明暗接受为自然足趾起伏而非丝袜断层。图片移动晋升为 `OWNER_HOS_01_LOWER_LEGS_FEET_FRONT_CANON_001`，仅批准正面膝下/足部比例、接地、该视角的连续15D肉色哑光闭趾丝袜与织物下柔化酒红甲色；不改变脸、整体身体、其他视角或其他丝袜规格，完整 owner_v1.0 仍未锁定 | user approved scoped hosiery/feet component |
| draft_0.136 | 2026-09-14 | 用户要求开始 Gate-7 下一项 `HOS_02_FEET_3Q_v001`。候选从批准左3/4 Body Master 与受限15D足部材质裁切独立生成，不输入已批准 HOS_01 或任何其他生成候选；只申请左3/4足踝/双脚几何、接地和该视角下15D肉色哑光闭趾丝袜连续呈现。永久身份、整体身体、肤色与酒红甲色锚不变 | user next-hosiery asset authorization; identity anchors unchanged |
| draft_0.137 | 2026-09-14 | HOS_02 v001 的双参考完整调用和仅使用批准左3/4 Body Master 的精简调用均在输出阶段被安全系统拦截，无图产生。失败调用不提供足形、3/4视角或丝袜证据；现有 HOS_01、永久身份、身体、肤色与酒红甲色锚均不改变，v001 不可用于下游 | generation blocked; identity anchors unchanged |
| draft_0.138 | 2026-09-14 | 用户要求按顺序回到 Hairstyle A，授权 `HAIR_A_02_3Q_v001`。候选仅从批准左3/4 Face Master 与 Hairstyle-A 的遮脸 L0 派生图平行生成，不输入 HAIR_A_01 或任何其他生成图；只申请左3/4发型轮廓、脸侧关系、分缝、体积、长度与完整发尾权威。永久脸部身份、肤色、身体和服装锚不变 | user next Hair-A asset authorization; identity anchors unchanged |
| draft_0.139 | 2026-09-14 | HAIR_A_02 v001 已从批准左3/4 Face 与遮脸 Hairstyle-A L0 派生图独立生成。技术预检范围内左3/4方向、近中分、受控顶部体积、远近侧长直发束、完整胸下长度和渐细发尾成立；可见脸部只作为上下文，不从本候选写回任何新身份事实。候选待用户审核，不可用于下游 | candidate generated; identity anchors unchanged |
| draft_0.140 | 2026-09-14 | 用户明确判定 HAIR_A_02 v001 “不错，合格”；图片移动晋升为 `OWNER_HAIR_A_02_3Q_CANON_001`。批准只增加 Hairstyle-A 左3/4轮廓、分缝投影、远近侧发束、体积、完整长度和渐细发尾权威；可见脸部仍由批准 Face 控制，不改变永久身份、肤色、身体或服装锚。Hairstyle A 完成2/6，完整 owner_v1.0 未锁定 | user approved scoped Hair-A component |
| draft_0.141 | 2026-09-14 | 用户要求继续 Hairstyle A 下一项，授权 `HAIR_A_03_SIDE_v001`。本候选采用人物 anatomical-left 纯侧面、鼻尖朝画面右，只从批准左侧面 Face Master 与遮脸 Hairstyle-A L0 派生图平行生成；不输入 HAIR_A_01/02 或任何生成 Hair 图。新增审核范围仅为左侧面的发际线、耳侧关系、后脑轮廓、前后发束深度、完整胸下长度与渐细发尾；永久脸部身份、肤色、身体、服装及其他发型角度均不改变 | user next Hair-A asset authorization; identity anchors unchanged |
| draft_0.142 | 2026-09-14 | HAIR_A_03 v001 已从批准左侧面 Face 与遮脸 Hairstyle-A L0 派生图独立生成。技术预检范围内左侧面方向、眼平头位、发际线/近耳关系、后脑轮廓、前后长直发束深度、完整胸下长度和渐细发尾成立；可见脸部仅为上下文，不从该 Hair 候选写回任何新身份事实。候选待用户审核，不可用于下游 | candidate generated; identity anchors unchanged |
| draft_0.143 | 2026-09-14 | 用户明确批准 HAIR_A_03 v001；图片移动晋升为 `OWNER_HAIR_A_03_SIDE_CANON_001`。批准只增加 Hairstyle-A anatomical-left 标准侧面的分缝/发际线、近耳关系、顶部与后脑轮廓、前后发束深度、完整长度和渐细发尾权威；可见脸部仍由批准 Face 控制，其同方向真人纯侧脸覆盖限制继续保留，不改变永久身份、肤色、身体或服装锚。Hairstyle A 完成3/6，完整 owner_v1.0 未锁定 | user approved scoped Hair-A component |
| draft_0.144 | 2026-09-14 | 用户要求并确认继续生成 `HAIR_A_04_BACK_v001`。候选从批准背面 Body Master 与遮脸 Hairstyle-A L0 派生图平行生成；Body 只定义180°背向头身/肩颈比例和可见校准服装，其现有头发被排除，L0 派生图只定义 Hair A 的长直披散、顶部流向/体积、深棕色、密度、长度与渐细发尾。A01–A03 及所有生成 Hair 图均不输入；本项不展示脸部，也不改变永久身份、身体或服装锚 | user next Hair-A asset authorization; identity anchors unchanged |
| draft_0.145 | 2026-09-14 | HAIR_A_04 v001 首次调用无图，随后以同一两项隔离参考进行一次中性技术档案重试并成功生成。技术预检范围内严格背面方向、无面部侧缘、完整顶部/后部结构、长直深棕披散发、完整长度与渐细发尾成立；该候选只供 Hair-A 背面属性审核，不从可见身体、皮肤、服装或灯光写回身份事实。候选待用户审核，永久身份锚保持不变 | candidate generated; identity anchors unchanged |
| draft_0.146 | 2026-09-14 | 用户明确批准 HAIR_A_04 v001；图片移动晋升为 `OWNER_HAIR_A_04_BACK_CANON_001`。批准只增加 Hairstyle-A 180°背面的顶部流向、后脑轮廓/发量、肩颈落发、完整外缘、长度与渐细发尾权威；不改变永久脸部身份、身体、肤色、服装或其他发型角度。Hairstyle A 完成4/6，完整 owner_v1.0 未锁定 | user approved scoped Hair-A component |
| draft_0.147 | 2026-09-14 | 用户授权继续生成 HAIR_A_05 高机位仰视镜头候选。本项从批准正面 Face 与遮脸 Hairstyle-A L0 派生图平行生成，不输入 A01–A04 或其他生成图；Face 只定义身份，L0 只定义 Hair A。高机位与人物抬头仅是透视校准，不写回标准眼平面部几何，也不改变永久身体、肤色或服装锚 | user next Hair-A asset authorization; identity anchors unchanged |
| draft_0.148 | 2026-09-14 | HAIR_A_05 v001 已从批准正面 Face 与遮脸 Hairstyle-A L0 派生图独立生成。技术预检范围内高机位/整头抬起关系、近正面身份上下文、完整发际线/头顶/分缝、长直脸侧发束及完整发尾成立；高机位造成的眼鼻下颌透视变化只属于本候选上下文，不从 Hair 候选写回标准眼平身份。候选待用户审核，永久身份锚保持不变 | candidate generated; identity anchors unchanged |
| draft_0.149 | 2026-09-14 | 用户明确批准 HAIR_A_05 v001；图片晋升为高机位/人物抬头 Hairstyle-A 组件。批准只增加该透视下的发际线、头顶/分缝、脸侧发束位移、外缘与发尾权威；高角度五官透视不写回标准身份。Hairstyle A 完成5/6，完整 owner_v1.0 未锁定 | user approved scoped Hair-A component |
| draft_0.150 | 2026-09-14 | 用户授权最后一项 HAIR_A_06 低机位/人物低头候选。本项仍从批准正面 Face 与遮脸 Hairstyle-A L0 派生图平行生成，不输入 A01–A05；低机位五官透视仅为上下文，不改变永久身份、身体、肤色或服装锚 | user final Hair-A candidate authorization; identity anchors unchanged |
| draft_0.151 | 2026-09-14 | HAIR_A_06 v001 首次视角技术失败未入库，定向重试后建立明确下巴以下向上机位及低位凝视。低角度下颌/鼻底透视只属于候选上下文，整头低头幅度列为人工复核点，不写回标准身份；永久身份锚保持不变 | candidate generated; identity anchors unchanged |
| draft_0.152 | 2026-09-14 | 用户指出 HAIR_A_06 v001 的五官过度立体，不符合本人较平缓柔和的面部起伏；同时否定低机位下过多头顶与长发缝。v002 必须回到批准 Face 身份比例，压低眉骨/鼻梁/中面部/下颌的立体夸张，并将头顶/冠部发缝从视野中移除；v001 不作像素输入 | user face-relief and projection correction; identity anchors clarified |
| draft_0.153 | 2026-09-14 | HAIR_A_06 v002 定向重试后，面部起伏回到较柔和方向，冠部与头皮分缝从低机位视野中移除。低角度鼻底/下颌仍仅为透视上下文，不写回标准身份；候选待用户审核 | corrected candidate generated; identity anchors unchanged |
| draft_0.154 | 2026-09-14 | 用户确认 v002 五官接近，指出发型根部发流/隐藏分缝位置错误：固定 Hair-A 应在画面中线左侧少许，而非明显偏右。该反馈只校正 Hair-A 位置合同，不改变脸部身份；v003 不输入 v002 或批准 A01 像素，A01 仅提供书面位置读数 | user Hair-A part-position correction; face anchors unchanged |
| draft_0.155 | 2026-09-14 | HAIR_A_06 v003 已独立生成；技术预检确认隐藏分缝对应的根部发流顶点回到画面中线左侧约2–3%，并保持无冠部/长头皮缝与较柔和五官方向。候选只供 Hair-A 低机位审核，不改变永久身份锚 | corrected candidate generated; identity unchanged |
| draft_0.156 | 2026-09-14 | 用户批准 HAIR_A_06 v003；Hair A 六视角组件完成。批准只增加低机位 Hair-A 投影权威，不改变脸、身体或服装，完整 owner_v1.0 未锁定 | user approved final Hair-A component |
| draft_0.157 | 2026-09-14 | 用户授权下一项 HAIR_B_01 标准眼平正面。批准 Face 定义身份，B 真人 L0 与批准 B 设计锚共同定义盘发且不得定义脸；现有 B 参考的高机位/仰头、惊讶表情、暖光和衣服全部排除 | user Hairstyle-B front authorization; identity unchanged |
| draft_0.158 | 2026-09-14 | HAIR_B_01 v001 已从三项隔离参考生成；标准眼平身份上下文在技术预检范围内保持，B 盘发只申请发际/分缝/收拢/碎发/顶部体积权威，不从候选写回脸或肤色。候选待用户审核 | candidate generated; identity unchanged |
| draft_0.159 | 2026-09-14 | 用户确认 HAIR_B_01 v001 长相可接受，仅拒绝标准眼平下过高的头顶轮廓。v002 保持批准脸部身份不变，把发际线至头顶高度相对 v001 压低约20–25%，并减少可见头盖曲面；该修订只属于 Hair-B 眼平投影 | user Hair-B crown-height correction; identity unchanged |
| draft_0.160 | 2026-09-14 | HAIR_B_01 v002 已独立生成；技术预检确认头顶轮廓高度降低且脸部身份方向保持。该变化只属于 Hair-B 标准眼平投影，不写回永久头骨或脸部身份 | corrected candidate generated; identity unchanged |
| draft_0.161 | 2026-09-14 | 用户要求 B01 候选中的鼻子更短、更窄，并将人中/嘴唇/下巴整体上移以同步压缩鼻下区域，同时再降低头顶。该脸部调整作为待审核上下文记录，不能由 Hair 候选自动覆盖已批准 Face Canon；v003 不输入 v002 | user coupled facial-context refinement; Face Canon not auto-promoted |
| draft_0.162 | 2026-09-14 | HAIR_B_01 v003 已生成；技术预检确认鼻子缩短变窄、鼻下区域整体上收以及头顶进一步降低。该脸部结果仍只属于 Hair 候选上下文，未经单独 Face 决策不改变已批准 Face Canon | candidate generated; Face Canon unchanged |
| draft_0.163 | 2026-09-14 | 用户批准 HAIR_B_01 v003；批准仅增加标准眼平正面 Hair-B 权威，脸部上下文不覆盖 Face Canon，完整 owner_v1.0 未锁定 | user approved scoped Hair-B component |
| draft_0.164 | 2026-09-14 | 用户授权 HAIR_B_02 人物左3/4候选；批准左3/4 Face 定义身份，真人 B L0 与批准 B 设计锚定义发型，B01 不作像素输入，永久身份不变 | user next Hair-B asset authorization |
| draft_0.165 | 2026-09-14 | HAIR_B_02 v001 已独立生成；左3/4身份上下文在技术预检范围内保持，候选仅申请该角度 Hair-B 发际/碎发/收拢/发髻位置权威，不写回脸部身份 | candidate generated; identity unchanged |
| draft_0.166 | 2026-09-14 | 用户将 Hair-B 后部固定为鲨鱼夹夹起的紧凑折叠发束 + 小型向上后翘鸡尾，取代低发髻解释；该发型决定需兼容已批准高机位正面轮廓，不改变脸部身份 | user Hair-B rear design decision |
| draft_0.167 | 2026-09-14 | HAIR_B_02 v002 已生成并在技术预检中符合鲨鱼夹+小鸡尾合同；只供 Hair-B 审核，不改变脸部身份 | candidate generated; identity unchanged |
| draft_0.168 | 2026-09-14 | 用户明确批准 HAIR_B_02 v002；新增权威仅限左3/4 Hair-B 鲨鱼夹/折叠发束/小鸡尾结构，不改变脸部、身体或完整 owner_v1.0 锁定状态 | user approved scoped Hair-B component |
| draft_0.169 | 2026-09-14 | 用户授权 HAIR_B_03 人物左纯侧面候选；批准左侧 Face 定义身份，B 真人 L0 与批准 B 设计锚定义发型，鲨鱼夹/小鸡尾仅按已批准文字合同重建，不输入其他 Hair 像素，身份锚不变 | user next Hair-B asset authorization |
| draft_0.170 | 2026-09-14 | HAIR_B_03 v001 已独立生成；技术预检范围内人物左纯侧面、受控冠部、后脑中线鲨鱼夹侧向结构和短小上后翘鸡尾成立。夹具下后方折叠发束的偏圆润体积只作为 Hair-B 候选复核点，不写回头骨、脸部或永久身份；候选待用户审核，完整 owner_v1.0 未锁定 | candidate generated; identity anchors unchanged |
| draft_0.171 | 2026-09-14 | 用户明确批准 HAIR_B_03 v001；新增权威仅限人物左纯侧面的 Hair-B 发际/耳侧/后收、后脑中线鲨鱼夹侧向结构、夹内折叠发束及短小上后翘鸡尾。可见脸部、头骨、身体、服装与其他角度不写回永久身份，完整 owner_v1.0 未锁定 | user approved scoped Hair-B side component |
| draft_0.172 | 2026-09-14 | 用户授权重新生成 POSE_09。候选从批准左3/4 Face、左3/4 Body 与 Hair-A 三项 Master 独立生成，不输入任何 Pose；采用修订后的前脚掌/脚趾腹着地、脚跟抬起合同，并使用严密的中性临床/物理治疗评估提示词组装以降低 AI 安全拦截风险 | user pose-09 retry authorization; identity anchors unchanged |
| draft_0.173 | 2026-09-14 | 用户明确批准 POSE_09 v003（“相当不错，批准了”）；物理文件按单文件规则移动晋升为 `OWNER_POSE_09_PRONE_ARMS_KNEES_SUPPORTED_CANON_001.jpg`。批准仅覆盖四点支撑/手膝姿态的关节承重关系、中立脊柱与前掌接地，不写回永久身份、身体、发型或材质；完整 owner_v1.0 未锁定 | user approved scoped POSE_09 component |
| draft_0.174 | 2026-09-14 | 用户授权重新生成 POSE_07。候选从批准右3/4 Face、右3/4 Body 与 Hair-A 三项 Master 独立生成，不输入任何 Pose；采用右3/4稳定半跪/低蹲关节姿态合同，并使用严密的中性临床/物理治疗评估提示词组装以降低 AI 安全拦截风险 | user pose-07 retry authorization; identity anchors unchanged |
| draft_0.175 | 2026-09-14 | 用户明确批准 POSE_07 v004（“不错，批准”）；物理文件按单文件规则移动晋升为 `OWNER_POSE_07_KNEELING_CROUCHING_CANON_001.jpg`。批准仅覆盖右3/4半跪/低蹲姿态的关节承重关系、90°前膝、平稳后膝与前掌接地，不写回永久身份、身体、发型或材质；Gate 6 姿态组件完成 9/9 项，完整 owner_v1.0 未锁定 | user approved scoped POSE_07 component; Gate 6 Pose complete |
| draft_0.177 | 2026-09-17 | 用户授权 `BODY_01_FRONT_v017`；仅修正小腿近乎直下与内侧极窄间隙，保留 v016 已确认的腰臀比、长相、丝袜质感和酒红甲油，候选不自动晋升 | user-scoped correction and retry authorization |
| draft_0.178 | 2026-09-17 | 用户确认 v017 小腿直度合格，授权 `BODY_01_FRONT_v018` 修正脚趾根部白环、袜面朦胧覆盖、趾间张力、腿部体量、腰部宽度及全脚掌着地 | user-scoped correction and retry authorization |
| draft_0.179 | 2026-09-17 | 用户指出 v018 小腿仍弯曲且外侧轮廓偏离大腿，授权 `BODY_01_FRONT_v019` 保留丝袜、体量、腰部和脚掌接地，仅强化小腿直下与外侧齐平 | user-scoped correction and retry authorization |
| draft_0.180 | 2026-09-17 | 用户明确批准 `BODY_01_FRONT_v019`；按单文件规则移动晋升为 `OWNER_BODY_01_FRONT_CANON_005`，批准范围包括小腿直下、外侧齐平、腿部体量、腰部比例、丝袜质感与全脚掌着地 | user approved scoped component; moved to Canon |
| draft_0.181 | 2026-09-17 | 用户授权根据当前正面 Body Canon 生成对应 `BODY_06_BACK_v004`，保持身体比例、腿部体量、丝袜材质、脚跟渐变和全脚掌着地 | user generation authorization |
| draft_0.182 | 2026-09-17 | 用户指出 v004 背面腿部轮廓与正面不一致，授权 `BODY_06_BACK_v005` 使用当前 005 的脸部排除身体派生图进行跨视角轮廓对齐 | user correction and retry authorization |
| draft_0.183 | 2026-09-17 | 用户明确批准 `BODY_06_BACK_v005`；按单文件规则移动晋升为 `OWNER_BODY_06_BACK_CANON_003`，更新背面当前活动路由 | user approved scoped component; moved to Canon |
