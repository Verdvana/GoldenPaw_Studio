# 女主角丝袜资产生成提示词入口

本目录用于后续保存丝袜身份、结构、材质、花纹、鞋履和姿势参考图的生成提示词。资产规划与选择入口：

`assets/female-lead/hosiery/README.md`

## 每次生成必须加载

1. 女主核心身份或脚部身份母版。
2. 与目标最接近的已批准丝袜材质参考。
3. 与镜头最接近的结构视角或姿势参考。
4. `docs/media-generation-guardrails.md`。
5. 脚趾可见时，逐字加入 `prompts/_shared/closed-foot-pantyhose-toe-lock.md`。

## 参考图职责

- 女主身份图只负责人物、身材和脚型身份。
- `construction/` 参考只负责完整包脚结构、无连接线和袜面张力曲面。
- `materials/` 参考只负责厚度、颜色、透肤度与光泽。
- `patterns/` 参考只负责图案及其曲面变形。
- `footwear/` 参考只负责鞋口遮挡和接触关系。
- `poses/` 参考只负责蹲下、屈腿和运动中的张力与褶皱。

提示词必须明确这些职责，避免模型用材质图覆盖人物身份，或用姿势图改变目标丝袜规格。

## 推荐提示词顺序

1. 输出类型、构图、视角和姿势。
2. 人物身份和身体比例。
3. 厚度、颜色、材质、花纹和鞋履。
4. 纯正向的连续袜面描述。
5. 蹲姿时脚踝、脚背、膝前和膝窝的受力及褶皱描述。
6. 完整英文袜头硬锁。
7. 简短负面约束、画质和背景要求。

## 文件命名

提示词与目标图片保持相同主体名，仅扩展名改为 `.md`。例如：

```text
assets/female-lead/hosiery/materials/hosiery-nude-30d-velvet-matte-plain-top-three-quarter-standing-neutral-v01.png
prompts/female-lead/hosiery/hosiery-nude-30d-velvet-matte-plain-top-three-quarter-standing-neutral-v01.md
```

## 登记规则

- 生成结果必须先按 `assets/female-lead/hosiery/qa/README.md` 验收。
- 未通过结果不得保存为正式候选，也不得进入 `catalog/`。
- 视频姿势参考还需检查遮挡恢复和动作中的逐帧连续性。

