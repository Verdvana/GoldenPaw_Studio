# 女主静态资产画幅统一记录

- 日期：2026-09-06
- 原因：BD02–BD05 误继承剧集镜头的 16:9 横屏规格，与既有竖幅身份资产不一致。
- 正式规则：BD 类全身静态资产统一为约 0.53:1 竖幅，标准尺寸 913×1723；16:9 仅用于剧集成片镜头。
- 处理方式：对横幅生成源作居中裁切，只移除左右摄影棚空白；随后等比例缩放到标准尺寸。没有生成式补画、人物重绘、局部修图或调色。
- 原横幅：1672×941。
- 中间裁切：499×941。
- 正式竖幅：913×1723。

| 任务 | 横幅来源 | 竖幅派生 | 正式状态 |
|---|---|---|---|
| BD02 | `body/candidates/CHR_WOMAN_001_BD02_HAIR_A_v002.png` | `body/candidates/CHR_WOMAN_001_BD02_HAIR_A_v003.png` | 继承已批准内容，正式索引已切换 |
| BD03 | `body/candidates/CHR_WOMAN_001_BD03_HAIR_A_v001.png` | `body/candidates/CHR_WOMAN_001_BD03_HAIR_A_v002.png` | 继承已批准内容，正式索引已切换 |
| BD04 | `body/candidates/CHR_WOMAN_001_BD04_HAIR_A_v001.png` | `body/candidates/CHR_WOMAN_001_BD04_HAIR_A_v002.png` | 继承已批准内容，正式索引已切换；再次复核确认与 BD03 方向相反 |
| BD05 | `body/candidates/CHR_WOMAN_001_BD05_HAIR_A_v001.png` | `body/candidates/CHR_WOMAN_001_BD05_HAIR_A_v002.png` | 用户已批准，正式索引已切换 |

后续 BD、全身姿势及全身鞋袜关系资产的生成提示必须明确写入“竖幅完整全身构图”，不得再写 16:9 横屏。
