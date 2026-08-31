# 女主角核心基础资产

本目录是女主图片参考的唯一基础入口，共保留 6 张已确认图片。图片与对应提示词放在同一路径，不再按定妆、身份、身体和表情继续拆分子目录。

## 资产索引

| 职责 | 图片 | 对应提示词 | 状态 |
| --- | --- | --- | --- |
| 核心定妆与唯一身份主基准 | `female-lead-key-art-fresh-v1.png` | `key-art-fresh-v1.md` | 已锁定 |
| 脸部五视角身份结构 | `face-identity-master-v1.png` | `face-identity-master-v1.md` | 身份母版 v1 |
| 头部与机位角度 | `female-lead-head-angles-v1.png` | `head-angles-v1.md` | 角度扩展母版 v1 |
| 全身身体多视角 | `female-lead-body-turnaround-v1.png` | `body-turnaround-v1.md` | 比例母版 v1 |
| 六种表情与日常动作 | `female-lead-expressions-actions-v1.png` | `expressions-actions-v1.md` | 动作锚点 |
| 十二种自然微表情 | `female-lead-micro-expressions-v1.png` | `micro-expressions-v1.md` | 微表情母版 v1 |

## 优先级

1. `female-lead-key-art-fresh-v1.png` 始终决定人物身份、年龄感、脸型、发型、自然身材比例与写实质感。
2. `face-identity-master-v1.png` 和 `female-lead-head-angles-v1.png` 只补充脸部结构与观察角度，不覆盖核心定妆身份。
3. `female-lead-body-turnaround-v1.png` 只补充身体比例、背面和侧面结构，不作为服装或剧情姿势依据。
4. 两张表情图只补充表演范围，不得改变五官结构、年龄感或人物比例。

## 参考图选择

- 普通生成：核心定妆 1 张。
- 头部特写或复杂俯仰角：核心定妆＋最匹配的脸部或头部角度图。
- 全身或背侧面：核心定妆＋身体多视角图。
- 明确表情表演：核心定妆＋一张表情图。
- 不要默认一次上传全部 6 张；通常使用 1–3 张核心参考即可。

## 边界

这些图片中的衣服、鞋履、背景和构图只属于生成时的载体，除核心定妆本身的身份职责外，不自动成为新视频的服装或场景规范。具体造型由产品工程定义；丝袜另按 `../hosiery/README.md` 执行。
