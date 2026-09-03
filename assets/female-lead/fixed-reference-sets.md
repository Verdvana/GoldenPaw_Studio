# 女主固定参考集

本文件只登记用户明确确认、允许跨视频复用的固定造型与场景。它不替代 `core/` 的身份和身体比例基准，也不复制专项资产图片；表中路径是唯一正式原图来源。

## LOOK-SWIM-GREEN-POOL-V1｜绿色泳装与室内泳池

状态：`approved`，2026-09-03，用户确认整组加入固定资产。

固定内容：

- 同一女主，橄榄绿色简洁连体泳装。
- 明亮整洁的室内泳池与浅灰米色池岸，柔和均匀自然光。
- 肉色约 15D、天鹅绒哑光、无花纹、完整包脚连裤丝袜。
- 自然饱满的固定身体比例及与小腿、身高匹配的正常足长和足宽。

| 正式原图 | 主要职责 | 使用边界 |
| --- | --- | --- |
| `hosiery/visuals/hosiery-nude-15d-velvet-matte-plain-none-front-standing-neutral-v01.png` | 正面全身、泳装正面剪裁、泳池场景、15D 全腿材质 | 上肢伸展动作不固定；身份仍以核心定妆为最高基准 |
| `hosiery/visuals/hosiery-nude-15d-velvet-matte-plain-none-front-three-quarter-standing-neutral-v01.png` | 前侧约 45°全身轮廓、泳装侧前方贴合、干净均匀光照 | 作为本组默认人物与场景参考；袜头微距仍使用 BASE-C01/C02 |
| `hosiery/visuals/hosiery-nude-15d-velvet-matte-plain-none-back-standing-neutral-v01.png` | 正背面全身、泳装背面剪裁、腰臀—腿部背侧比例 | 不承担正面脸部、脚趾甲油或袜头结构参考 |
| `hosiery/visuals/hosiery-nude-15d-velvet-matte-plain-none-front-three-quarter-deep-squat-v01.png` | 前侧约 45°完全蹲下、自然上肢支撑、落跟受力、统一无斑驳光照 | 使用单次干净重生成的 P6；禁止引用同名失败版或 `rejected/` 中的累积编辑图 |

## 调用规则

1. 具体视频需要这套造型时，在工程 README 中写明 `LOOK-SWIM-GREEN-POOL-V1`，并按目标视角选一张主参考；只有跨视角一致性确有需要时再补第二张。
2. 人物身份始终以 `core/female-lead-key-art-fresh-v1.png` 为最高基准，身体比例始终以 `core/female-lead-body-turnaround-v1.png` 为最高基准；本组图片负责泳装、泳池环境、15D 丝袜和对应视角。
3. 脚趾可见的图片、关键帧或视频提示词，必须读取并逐字加入 `hosiery/closed-foot-pantyhose-toe-lock.md` 的三段英文硬锁，并按 `hosiery/qa.md` 验收。
4. 未明确调用本参考集的项目，不应被绿色泳装或泳池背景自动约束。
5. `hosiery/rejected/` 只供人工识错，任何情况下都不得作为正向参考。
