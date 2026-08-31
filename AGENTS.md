# GoldenPaw Studio 媒体生成强制规则

## 路径与读取顺序

- 处理通用角色资产时，先读 `assets/README.md`、对应角色的 `README.md`，再读目标素材类型的 `README.md`。
- 处理具体视频时，先读该 `products/<视频工程>/README.md`；工程 README 会列出本片必需的本地文件和全局角色资产。
- 不要从文件名猜测工作流，也不要绕过工程 README 直接批量生成。

生成或修改含女主丝袜的图片、分镜、关键帧、视频提示词或视频成片前，必须读取：

- `assets/female-lead/hosiery/README.md`
- `assets/female-lead/hosiery/qa.md`

规划或生成丝袜视觉模板时，还必须读取：

- `assets/female-lead/hosiery/asset-plan.md`

女主脚趾通过露趾鞋或拖鞋可见时，还必须逐字加载：

- `assets/female-lead/hosiery/closed-foot-pantyhose-toe-lock.md`

## 女主丝袜不可省略

- 女主穿裙装或设定中要求连裤丝袜时，丝袜必须在所有适用画面和视频帧中连续存在，不得因远景、动作、光照或肉色材质而变成裸腿。
- 女主穿露趾鞋或露趾拖鞋时，必须把 `assets/female-lead/hosiery/closed-foot-pantyhose-toe-lock.md` 的英文硬锁原文完整加入实际生成提示词；不能只写 “pantyhose-covered toes”。
- 脚趾入镜时，构图与分辨率必须足以看清：脚趾前端没有可见缝合线或加深横线；完整袜面以一整片高弹薄膜覆盖五趾，并在相邻脚趾之间跨接成柔和浅弧，而不是陷入趾缝或逐根紧贴；脚趾轮廓被丝袜柔化；暗红色甲油仅隔着丝袜朦胧透出。
- 视频中上述结构必须逐帧连续，禁止丝袜在脚趾处闪烁、消失或变成裸脚。
- 若任一可见脚趾看起来像裸脚，或红色甲油呈现为清晰裸露的高光甲面，该图片或视频必须判定为不合格，不得保存为正式候选；应重新生成。

## 当前居家造型

- 浅粉偏象牙色短款莫代尔睡裙。
- 肉色约 30D、微透肉、天鹅绒哑光、完整包脚连裤袜。
- 浅粉色露趾、薄底、零跟平底居家拖鞋。
- Apple Watch 与小耳钉。
