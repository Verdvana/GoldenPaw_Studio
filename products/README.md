# 视频产品工程

`products/` 的每个二级目录代表一条独立视频工程。

## 当前工程

- `pilot-01-cabinet/`：试播短片 01《打不开的柜门》。

## 新工程最低结构

```text
products/<视频工程>/
├── README.md
├── brief/
├── storyboards/
├── keyframes/
├── video/
│   └── outputs/
└── qa/
```

工程根 `README.md` 必须让视频生成类 AI 能独立开始工作，至少写明：目标与边界、必读顺序、本地文件清单、引用的全局角色资产、逐镜头执行方式、输出命名、验收标准、当前状态和下一步。

产品目录只保存本片专属内容。可复用角色母版保留在 `assets/`，由工程 README 明确引用，不得复制。
