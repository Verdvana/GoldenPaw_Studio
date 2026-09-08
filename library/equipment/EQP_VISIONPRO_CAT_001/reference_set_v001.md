# VP 静态参考组合 v001

状态：`CURRENT_STATIC_REFERENCE_SET`。这是 Vision Pro 猫用改装的唯一选图入口。

## 当前参考

| 作用 | 文件 | 状态与边界 |
|---|---|---|
| 大面罩佩戴比例 | `../../characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_3Q_v001.png` | 当前比例基准，不替代裸脸身份母版 |
| 侧臂与后脑绑带 | `../../characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_LEFT_PROFILE_v004.png` | 当前侧面参考，非严格正交图 |
| 后带包覆范围 | `../../characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_REAR_v003.png` | 当前后面参考 |
| 独立设备外观 | `candidates/EQP_VISIONPRO_CAT_001_DESIGN_3Q_v004.png` | 当前产品外观参考 |
| 正面佩戴 | `../../characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_FIT_VISIONPRO_FRONT_v001.png` | `USER_APPROVED_STATIC` |
| 桌面观察 | `../../characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_VISIONPRO_TABLE_OBSERVE_v001.png` | `USER_APPROVED_STATIC` |
| 单爪轻触 | `../../characters/CHR_CAT_001/poses/equipment_candidates/CHR_CAT_001_VISIONPRO_TABLE_TOUCH_v001.png` | `USER_APPROVED_STATIC` |

## 固定规则

- 黑色曲面玻璃、银色边框、深灰面垫；浅灰侧臂在耳根下方连接连续绕过后脑的灰色罗纹针织带。
- 不加跨头顶带、后置大圆调节盘、外挂电池或线缆；双耳和口鼻保持露出。
- 猫咪身份始终以 `approved/` 身份母版为最高优先级。佩戴镜头只加入与目标视角最接近的一至两张设备参考。
- 当前资产可用于静态镜头；精确三维尺寸、动态稳定性与真实动物佩戴安全性尚未验证。
