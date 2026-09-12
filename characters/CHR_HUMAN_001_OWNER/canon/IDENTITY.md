# 女主身份锚 — 工作版

```yaml
document_id: OWNER_IDENTITY_ANCHOR
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
revision: draft_0.47
status: DRAFT
source_manifest: source/identity/SOURCE_MANIFEST.md
updated_at: "2026-09-12"
```

本文件是 L0 真人照片、用户指定的 L1 目标外观锚与 L1 Face Canon 候选之间的文字身份锚。当前版本尚未获得最终身份批准，可根据用户对候选图的明确反馈继续修订。

当前五个 Face 组件均已批准，当前下游 Master 均为用户转码的 JPG，统一索引见 `face/FACE_CANON_INDEX.md`。格式变化不改变已批准的身份属性；原候选 PNG 仍保留生成溯源。

## 用户指定的目标外观锚

- `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001` 是当前女主正脸长相与肤色的 L1 目标锚；
- 新的 Face Canon 必须严格保持该图中的可辨识正脸、面部整体关系与肤色观感；
- 该图在 Face 任务中不负责发型、身体、衣服、俯拍机位、灯光、阴影或背景；
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
- downstream rule: 普通 L2/L3 正面镜头可从该已批准 Master 直接引用脸部身份；重新制作 L1 正面 Master 时必须使用方法文档中的源派生输入平行重建，禁止以本图继续生成新 L1 链条

### FACE_02 左 3/4

- asset_id: `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001`
- role: 人物 anatomical left facial plane principally visible、鼻尖朝画面左的中性左 3/4 身份；定义该视角的眼眶/鼻梁投影、近远眼、面颊—下颌深度、可见耳位、柔和颧骨、圆润下巴末端和柔和中性眼神
- approved path: `canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg`
- approval: `canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/approvals/APPROVAL_OWNER_FACE_02_LEFT_3Q_NEUTRAL_001.md`
- regeneration method: `canon/face/FACE_02_LEFT_3Q_NEUTRAL_METHOD.md`
- downstream rule: 普通 L2/L3 左 3/4 镜头直接引用该 Master；重新制作 L1 时使用 `OWNER_FACE_LEFT_3Q_NEUTRAL_RECOVERY_V1` 的三项输入和方法文档中的固定顺序/提示结构，禁止以 v001–v004 或本批准图继续生成新的 L1 链条

### FACE_03 右 3/4

- asset_id: `OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001`
- role: 人物 anatomical right facial plane principally visible、鼻尖朝画面右的中性右 3/4 身份；定义该视角的近远眼、鼻部投影、右侧面颊—下颌深度、可见耳位、柔和颧骨、圆润下巴底部和柔和中性眼神
- approved path: `canon/face/approved/FACE_03_RIGHT_3Q_NEUTRAL/OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001.jpg`
- approval: `canon/face/approved/FACE_03_RIGHT_3Q_NEUTRAL/approvals/APPROVAL_OWNER_FACE_03_RIGHT_3Q_NEUTRAL_001.md`
- regeneration method: `canon/face/FACE_03_RIGHT_3Q_NEUTRAL_METHOD.md`
- downstream rule: 普通 L2/L3 右 3/4 镜头直接引用该 Master；重新制作 L1 时使用 `OWNER_FACE_RIGHT_3Q_NEUTRAL_RECOVERY_V1` 的固定三输入和方法文档，禁止镜像 FACE_02，禁止以 v001、v002 或本批准图继续生成新的 L1 链条

### FACE_05 右侧面

- asset_id: `OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001`
- role: anatomical right facial plane visible、鼻尖朝画面左的纯右侧面身份；定义额头—鼻—唇—下巴剪影、批准的鼻尖比例、眼眶深度、耳位、下颌—颈部关系、圆润下巴和柔和前视眼神
- approved path: `canon/face/approved/FACE_05_RIGHT_PROFILE_NEUTRAL/OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001.jpg`
- approval: `canon/face/approved/FACE_05_RIGHT_PROFILE_NEUTRAL/approvals/APPROVAL_OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_001.md`
- regeneration method: `canon/face/FACE_05_RIGHT_PROFILE_NEUTRAL_METHOD.md`
- downstream rule: 普通 L2/L3 右侧面镜头直接引用该 Master；重新制作 L1 时使用 `OWNER_FACE_RIGHT_PROFILE_NEUTRAL_RECOVERY_V1` 的固定三输入和方法文档，禁止使用任何 FACE_05 生成图、其他生成角度或镜像作为 L1 输入

### FACE_04 左侧面

- asset_id: `OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001`
- role: anatomical left facial plane visible、鼻尖朝画面右的纯左侧面身份；定义用户批准的额头—鼻—唇—下巴剪影、眼眶深度、耳位、下颌—颈部关系、圆润下巴和柔和前视眼神
- approved path: `canon/face/approved/FACE_04_LEFT_PROFILE_NEUTRAL/OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001.jpg`
- approval: `canon/face/approved/FACE_04_LEFT_PROFILE_NEUTRAL/approvals/APPROVAL_OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_001.md`
- regeneration method: `canon/face/FACE_04_LEFT_PROFILE_NEUTRAL_METHOD.md`
- downstream rule: 普通 L2/L3 左侧面镜头可在批准范围内直接引用当前 JPG Master；重新制作 L1 时使用 `OWNER_FACE_LEFT_PROFILE_NEUTRAL_RECOVERY_V1` 的固定三输入和方法文档，禁止使用本批准 JPG、候选 PNG、FACE_03、FACE_05、其他生成角度或镜像作为 L1 输入；始终披露该侧面缺少同方向真人纯侧脸验证

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

## FACE_02 左 3/4 当前反馈

- `FACE_02_LEFT_3Q_NEUTRAL_v001` 整体方向获用户认可，但仍为未批准候选，不得作为 v002 的像素参考；
- 保持 v001 已实现的身份方向、左 3/4 转角、鼻梁投影、肤色、HAIRSTYLE_A、眼平机位和构图方法；这些只以文字约束复用；
- v002 仅作三项克制修正：颧骨视觉最高点略降、颧区轮廓更柔和，不削平面颊；下巴尖度略减并恢复更柔和圆润的收束，不缩短下巴也不扩大下颌；眼神更柔和放松，通过眼睑张力和注视强度调整，不改变眼睛大小、眼距、眼型或瞳孔位置；
- 禁止将“颧骨降低”做成扁平脸、幼态脸或增加面颊膨胀；禁止将“下巴变圆”做成宽重下巴；禁止用微笑、眯眼、改变眉形或美颜来制造柔和眼神。
- `FACE_02_LEFT_3Q_NEUTRAL_v002` 的身份方向、颧骨、柔和眼神、左 3/4 角度、肤色、HAIRSTYLE_A、机位与构图已获用户确认；v003 必须锁定这些文字属性，只将下巴末端再圆润一小步；不得改变下巴长度、下颌宽度、下颌角、嘴唇位置或脸部其他结构，也不得使用 v002 像素。
- `FACE_02_LEFT_3Q_NEUTRAL_v003` 因五官偏离被用户拒绝，不得用于下游或后续生成。下一候选恢复 v001 的完整核心提示结构，只追加三项简短约束：颧骨略低且轮廓柔和、下巴更圆润但不变宽变短、眼神更柔和但不改变眼睛几何。
- `FACE_02_LEFT_3Q_NEUTRAL_v004` 已获用户明确批准。其像素只作为批准 Master 供普通下游按范围引用；L1 再生成复用已批准的方法、输入顺序和文字约束，不使用 v004 像素。

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
- 脸部身份只由批准的 `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` 定义；真人 `3.jpg` 与 `4.jpg` 只交叉提供身高感、头身比、肩宽、躯干长度、腰线、胸腰胯自然范围、臂腿长度和真实非模特化体态。
- 用户尚未指定主动身材调整。v001 不瘦身、不增高、不拉腿、不夸大胸腰臀差、不收窄肩胯，也不把单张衣物塑形或走路姿态当成裸体几何。
- 身体正面自然直立、重量均匀、双臂自然下垂、手掌靠近大腿但不贴死、双脚平行或自然微外展且不交叉；头部正面平视、闭嘴中性。
- 完整使用粉色高叉连体泳衣、15D nude velvet-finish sheer pantyhose 和无鞋状态；丝袜从腰胯连续覆盖至脚趾，但 BODY_01 只做连续性预检，最终材质权威属于 Gate 7。
- HAIRSTYLE_A 只由遮脸发型输入定义；真人全身照中的发型、衣服、鞋、手持物、背景、脸和腿部视觉塑形不得传入。
- BODY_01 首次调用未产出图片；安全重试移除带床景/广告文字的丝袜照片，并将画面明确限定为成年、非性感的技术性身体比例校准照。该执行调整不改变身份或身体目标，丝袜连续性仍按文字合同检查。
- BODY_01 安全重试仍在输出阶段被拦截且无图；当前不存在 BODY_01 候选。不得把失败调用当作身体反馈或新身份事实，等待用户明确决定是否修改 Body 校准服装合同后再生成。

## BODY_01 当前批准结果

- 用户确认本人现实身体基准为身高 `168 cm`、体重 `120 斤`（约 `60 kg`）。该数值是当前 Body 身份事实，优先于 L0 全身照因服装、镜头和姿态产生的矮化观感。
- `BODY_01_FRONT_v009` 已由用户明确批准并晋升为当前活动正面 Body 组件 `OWNER_BODY_01_FRONT_CANON_002`；旧 `OWNER_BODY_01_FRONT_CANON_001` 保留为历史已批准但已被替代的组件，不再作为活动下游路由目标。
- 当前活动组件呈现与 168 cm / 60 kg 相符的自然成年女性比例：整体偏高但不是夸张模特身材，保持真实肩胸腰胯和软组织体量；通过正确头身比、躯干与四肢长度关系表达身高，不得缩头、广角拉腿、低机位仰拍或机械纵向拉伸。
- 小腿需进一步收直：双侧膝、胫骨中线与踝中心形成自然近竖直轴，胫骨不向外弯，左右小腿肌肉保留自然体量但外轮廓不制造 O 形腿观感，双脚仍平放且方向对称。
- 用户明确批准 v009 的长相、HAIRSTYLE_A、四肢比例、腰臀比、腿脚几何和腿脚丝袜质感。普通下游可使用活动 Master 的批准范围；重新制作 L1 仍按批准 Face、两张 L0 身体上下文和遮脸发型 A 的四输入恢复方法平行生成，不使用 v008、v009 或任何 Body Master 像素。
- 用户进一步明确：`OWNER_BODY_01_FRONT_CANON_002` 中的 168 cm / 60 kg、可见长相、`HAIRSTYLE_A`、四肢比例和腰臀比可用于生成其他角色资产及视频镜头所需图片；当存在更匹配视角的专用 Face/Hair Canon 时仍优先使用专用组件。该图的丝袜只可作为 `15D 哑光肉色` 外观参考，不得用于其他颜色、材质/光泽或厚度。
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
| draft_0.40 | 2026-09-12 | 用户批准 BODY_02 左 3/4 v001 为 `OWNER_BODY_02_LEFT_3Q_CANON_001`；登记其左 3/4 身体轮廓、深度与既有 168 cm / 60 kg 比例保持范围，并继续推进 BODY_03 | user approved component |
| draft_0.41 | 2026-09-12 | 用户拒绝 BODY_03 v001 的悬空脚跟与脚趾—前脚掌异常横线；v002 只修正两脚完整贴地及15D面料无缝连续性，保持既定右 3/4 身份、比例与构图方法，并禁止输入 v001 | user rejection and revision authorization incorporated |
| draft_0.42 | 2026-09-12 | 用户指出 v002 用脚跟下肉色垫块/多余组织伪造接地且脚趾横线仍在；撤销此前技术 PASS，v003 要求双脚轮廓互不遮挡、单一正常脚跟直接接地、无任何支撑物，并彻底消除脚趾—前脚掌线条，禁止输入 v001/v002 | user rejection and QA correction incorporated |
| draft_0.43 | 2026-09-12 | 用户确认 BODY_03 v003 其它方面完美，仅丝袜与脚部织物质感不足；v004 新增 `L0_HOS_15_NM_011` 作为严格 material-only 参考并保持 v003 成功属性的文字意图，禁止使用 v003 像素 | user scoped material feedback incorporated |
| draft_0.44 | 2026-09-12 | 用户批准 BODY_03 右 3/4 v005 为 `OWNER_BODY_03_RIGHT_3Q_CANON_001`；登记右向身体轮廓、比例、接地脚部与本组件内15D肉色哑光/天鹅绒丝袜表现，完整 owner_v1.0 仍未锁定 | user approved component |
| draft_0.45 | 2026-09-12 | 用户批准 BODY_04 左侧面 v002 为 `OWNER_BODY_04_LEFT_SIDE_CANON_001`；登记左侧面轮廓/深度、比例、接地、自然遮挡及本组件内15D肉色哑光/天鹅绒丝袜表现，完整 owner_v1.0 仍未锁定 | user approved component |
| draft_0.46 | 2026-09-12 | 用户批准 BODY_05 右侧面 v001 为 `OWNER_BODY_05_RIGHT_SIDE_CANON_001`；登记右侧面轮廓/深度、比例、接地、自然遮挡及本组件内15D肉色哑光/天鹅绒丝袜表现，BODY_06 成为剩余 Body 视角 | user approved component |
| draft_0.47 | 2026-09-12 | 用户批准 BODY_06 背面 v001 为 `OWNER_BODY_06_BACK_CANON_001`；登记完整背面轮廓/深度、比例、头身朝向、接地、保守发型后落及本组件内丝袜表现。六个 Body 组件全部批准，Gate 4 开放，完整 owner_v1.0 仍未锁定 | user approved component |
