# Batch 016｜HA02 v001

- 日期：2026-09-06
- 状态：用户已批准
- 任务：发型 A 右侧结构
- 生成方式：全新生成，不镜像 HA01
- 工具：Codex 内置 image_gen
- 项目文件：`hair/candidates/CHR_WOMAN_001_HA02_HAIR_A_v001.png`
- 原始成功输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-64c9d63c-e935-4e88-ae21-ad0aaa251963.png`
- 身份与正面发型参考：`face/candidates/CHR_WOMAN_001_ID01_HAIR_A_v004.png`
- 严格右侧脸参考：`face/candidates/CHR_WOMAN_001_FC05_HAIR_A_v001.png`
- 发长与分布参考：`body/candidates/CHR_WOMAN_001_ID02_HAIR_A_v003.png`
- 后脑发流参考：`body/candidates/CHR_WOMAN_001_BD05_HAIR_A_v002.png`
- 授权真人发型来源：`source_photos/DSC01015.JPG`
- 实际成功提交规格：见 `prompt_HA02_v001.md`

## 生成筛选

- 首次输出朝画面右，与 HA01 同向，不符合 HA02 要与 FC05 一致、朝画面左的成对要求。BD04 本身与 BD03 方向相反且有效，但其画面朝向与 HA02 所需 FC05 朝向相反，用在本次提示中造成方向职责冲突。该输出未保存到项目。原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-7c3e3220-05e0-4c1b-bc7c-95ab060c2c62.png`。
- 第二次移除 BD04，以 FC05 作为最高优先级方向参考并明确鼻尖朝画面左，完成正确右侧输出。

## 初检

- 人物自身严格右侧成立，鼻尖朝画面左，远侧眼隐藏，右耳为近侧可见耳。
- 头顶至发梢完整保留；右侧发际、分缝过渡、耳周关系、肩后发流及末端层次可读取。
- 发色、顺直质感和长度与发型 A 的正式资产基本连续，同时没有机械镜像 HA01。
- 画面保持竖幅、暖中性光和干净大色块，没有明显发丝噪点、文字或多余配饰。
- 当前仅为候选，不写入正式资产索引。

## 用户审核结论

- 2026-09-06：用户确认 HA02 OK，v001 写入正式资产索引。
