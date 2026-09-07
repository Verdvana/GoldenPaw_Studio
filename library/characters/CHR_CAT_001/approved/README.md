# CHR_CAT_001 批准资产

## 当前批准资产

| 文件 | 状态 | 用途 |
|---|---|---|
| `CHR_CAT_001_IDENTITY_FRONT_STANDING_v001.png` | APPROVED | 最高优先级正面身份母版、身体体积和毛色基准 |
| `CHR_CAT_001_IDENTITY_FRONT_SEATED_v001.png` | APPROVED | 中性坐姿身份基准 |
| `CHR_CAT_001_TURN_FRONT_LEFT_3Q_STANDING_v001.png` | APPROVED | 左前方三分之四转面 |
| `CHR_CAT_001_TURN_FRONT_RIGHT_3Q_STANDING_v001.png` | APPROVED | 右前方三分之四转面 |
| `CHR_CAT_001_TURN_LEFT_PROFILE_STANDING_v001.png` | APPROVED | 严格左侧身体结构参考 |
| `CHR_CAT_001_TURN_RIGHT_PROFILE_STANDING_v001.png` | APPROVED | 严格右侧身体结构参考 |
| `CHR_CAT_001_TURN_BACK_STANDING_v001.png` | APPROVED | 背面、背部毛色、后腿和尾巴结构参考 |

### 面部近景

| 文件 | 状态 | 用途 |
|---|---|---|
| `face/CHR_CAT_001_FACE_FRONT_NEUTRAL_v001.png` | APPROVED | 正脸身份细节、眼睛和额头纹理 |
| `face/CHR_CAT_001_FACE_FRONT_LEFT_3Q_NEUTRAL_v001.png` | APPROVED | 左前三分之四脸部结构 |
| `face/CHR_CAT_001_FACE_FRONT_RIGHT_3Q_NEUTRAL_v001.png` | APPROVED | 右前三分之四脸部结构 |
| `face/CHR_CAT_001_FACE_LEFT_PROFILE_NEUTRAL_v001.png` | APPROVED | 严格左侧鼻梁、口鼻、下颌和耳位 |
| `face/CHR_CAT_001_FACE_RIGHT_PROFILE_NEUTRAL_v001.png` | APPROVED | 严格右侧鼻梁、口鼻、下颌和耳位 |

### 身体与毛色细节

| 文件 | 状态 | 用途 |
|---|---|---|
| `details/CHR_CAT_001_COAT_TOP_VIEW_v001.png` | APPROVED | 头顶、脊线、背部、髋部和尾巴的俯视毛色分布 |
| `details/CHR_CAT_001_TAIL_STRUCTURE_v001.png` | APPROVED | 尾巴粗细、弧度、毛长和尾端色彩 |
| `details/CHR_CAT_001_FRONT_PAWS_AND_PADS_v001.png` | APPROVED | 前爪体积、趾部和肉垫颜色 |

### 日常微表情

| 文件 | 状态 | 用途 |
|---|---|---|
| `expressions/CHR_CAT_001_EXPR_CONTENT_SAFE_v001.png` | APPROVED | 安心、放松、具有安全感 |
| `expressions/CHR_CAT_001_EXPR_SLEEPY_v001.png` | APPROVED | 舒适困倦 |
| `expressions/CHR_CAT_001_EXPR_CURIOUS_ALERT_v001.png` | APPROVED | 好奇、轻度警觉 |
| `expressions/CHR_CAT_001_EXPR_MILDLY_WORRIED_v001.png` | APPROVED | 轻微担忧与不确定 |

### 基础猫科姿态

| 文件 | 状态 | 用途 |
|---|---|---|
| `poses/CHR_CAT_001_POSE_WALK_LEFT_MIDSTRIDE_v001.png` | APPROVED | 左向自然行走步态锚点 |
| `poses/CHR_CAT_001_POSE_LOAF_RESTING_v001.png` | APPROVED | 香箱趴卧与静态休息 |
| `poses/CHR_CAT_001_POSE_GROOM_LICK_PAW_v001.png` | APPROVED | 坐姿舔爪理毛 |
| `poses/CHR_CAT_001_POSE_HIND_LEG_HEAD_SCRATCH_v001.png` | APPROVED | 后脚挠头标志动作 |
| `poses/CHR_CAT_001_POSE_STRETCH_v001.png` | APPROVED_STATIC | 伸懒腰静态姿态参考，未验证运动 |
| `poses/CHR_CAT_001_POSE_CURLED_SLEEP_v001.png` | APPROVED_STATIC | 蜷缩睡眠静态姿态参考 |

### 赛博工程师与趣味表演

| 文件 | 状态 | 用途 |
|---|---|---|
| `expressions/CHR_CAT_001_EXPR_TECH_FOCUS_v001.png` | APPROVED_STATIC | 技术专注静态参考 |
| `expressions/CHR_CAT_001_EXPR_FAULT_PUZZLED_v001.png` | APPROVED_STATIC | 故障困惑静态参考 |
| `expressions/CHR_CAT_001_EXPR_SOLVED_COMPOSED_v001.png` | APPROVED_STATIC | 解决问题后的镇定静态参考 |
| `expressions/CHR_CAT_001_EXPR_FOOD_ANTICIPATION_v002.png` | APPROVED_STATIC | 食物期待（修正版）静态参考 |
| `poses/CHR_CAT_001_POSE_HUNT_READY_v001.png` | APPROVED_STATIC | 扑玩具前的低伏准备静态参考 |

本组不替代身份母版，不代表连续动作验证完成。详见 `../expressions/engineer_acting_batch_v001.md` 的提示词与审核记录。

## 使用优先级

1. 正面站姿身份母版决定脸部身份、基础毛色和身体体积。
2. 与目标镜头角度最接近的转面图补充身体结构。
3. 正面坐姿图仅用于坐姿体积和爪部布局。
4. `source_assets/` 中的旧资产只作概念与历史参考。

不得将所有参考图无差别同时输入模型。根据目标镜头选择正面身份母版加一至两张最接近角度的辅助图。

## 暂缓资产

以下内容等待女主身份资产建立后再制作：

- 女主 168cm 与猫咪的严格身高比例
- 抱猫、抚摸、膝上趴卧、蹭腿等双角色互动

## 下一批计划

VP 最新回选为较大的佩戴三分之四 v001，不再使用小面罩 v002；侧面/后面 v002 和独立设备 v003 已关联重制，仍待结构统一，未纳入本白名单。

设备比例已获用户确认，但不等于整张试配图结构批准。新增四张侧后面/键盘/接触候选，详见 `../poses/equipment_angles_batch_v001.md`；当前仍不新增身份/动作白名单资产。

- 奔跑、起跳、落地候选已生成，位于 `../poses/candidates/`；需进一步结构和运动验证，不在批准白名单中
- 赛博工程师三种表演、食物期待与扑玩具前准备姿态已完成静态参考；真实道具接触及运动尚未验证
- MacBook 单爪触控板与 Vision Pro 佩戴已完成首轮试配及修正，位于 `../poses/equipment_candidates/`；尚需结构、比例及侧后面验证，不在批准白名单内。详见 `../poses/equipment_fitting_batch_v001.md`
