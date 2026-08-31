# GoldenPaw Studio

“赛博金渐层”IP 的可复用角色资产库与独立视频工程仓库。

## 一级目录

项目内容只沿两条主线组织：

- `assets/`：跨视频复用的角色资产。二级目录是角色，三级目录是该角色的素材类型。
- `products/`：独立视频工程。二级目录是一条视频工程，工程内只保存该视频专属的策划、分镜、关键帧、提示词、输出与验收记录。

根目录只保留仓库入口文件，例如本 README、`AGENTS.md`、许可证和版本控制配置，不承载媒体素材。

## 开始工作

- 创建或维护通用角色素材：先读 `assets/README.md`，再读对应角色及素材类型的 README。
- 生成或维护某条视频：先读 `products/<视频工程>/README.md`。该文件是视频生成类 AI 的工程入口与执行清单。
- 任何媒体生成或修改：同时遵守 `AGENTS.md`。

## 当前入口

- 赛博金渐层：`assets/cyber-golden-shaded/README.md`
- 女主角：`assets/female-lead/README.md`
- 双角色组合：`assets/female-lead-and-cyber-golden-shaded/README.md`
- 视频工程索引：`products/README.md`
- 当前视频：`products/pilot-01-cabinet/README.md`

## 归档边界

- 能被多个视频复用、用于锁定角色身份或长期视觉设定的内容，归入 `assets/`。
- 只服务于一个视频的剧本、镜头、场景图、关键帧、生成提示词、成片和 QA 记录，归入该 `products/<视频工程>/`。
- 产品可以引用全局资产，但不得把通用母版复制进产品目录。
- 资产目录不得收纳某条视频的剧情镜头或成片。
