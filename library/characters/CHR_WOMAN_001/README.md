# CHR_WOMAN_001

当前已恢复生成。EX01 v001 已获用户确认并登记为正式资产；下一项 EX02 露齿笑已生成 `expressions/candidates/CHR_WOMAN_001_EX02_HAIR_A_v001.png`，等待用户审核。HB02 仍待独立审核。参考入口位于 `../../wardrobe/CHR_WOMAN_001/references/`，完整顺序见静态清单。

女主静态资产规划：[可编辑清单 v001](static_asset_plan_v001.md)。共 42 项候选任务，区分核心与按需扩展；目前仅规划，未生成女主母版。

26 岁中国女性主角，`CHR_CAT_001` 的主人。

## 原始照片投放位置

请将未经 AI 修改的真人原始参考照片放入：

```text
library/characters/CHR_WOMAN_001/source_photos/
```

建议优先准备：正脸、左右三分之二侧脸、左右侧脸、半身、正面全身、侧面全身、自然站姿、自然坐姿及常用表情。照片应尽可能清晰，避免重滤镜、美颜、夸张广角和大面积遮挡。

不要提前把照片分类复制到 `face/`、`body/` 等目录。导入后先建立来源清单，再进行无损筛选和分类，避免重复文件与来源混乱。

## 目录说明

- `source_photos/`：原始真人照片，只保存来源材料
- `face/`：经过筛选的面部角度参考
- `body/`：身材比例、体态和全身参考
- `hair/`：发型结构参考
- `expressions/`：表情参考
- `poses/`：姿态和动作参考
- `reference_sheets/`：统一角色参考板
- `model_assets/`：未来的角色模型、训练配置或适配文件
- `tests/`：身份稳定性测试结果
- `approved/`：批准用于正式生产的角色资产
