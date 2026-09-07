# Batch 010｜BD02 v001

- 日期：2026-09-06
- 状态：v001 未通过；脚趾区域的袜面可读性需要加强，已转入 v002
- 任务：全身右前三分之四站姿，发型 A
- 生成方式：全新生成，不编辑既有图片，不镜像 BD01
- 工具：Codex 内置 image_gen
- 项目文件：`body/candidates/CHR_WOMAN_001_BD02_HAIR_A_v001.png`
- 原始成功输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-d44f1da8-3b4f-450f-b820-f3d5a4ed858b.png`
- 身份参考：`face/candidates/CHR_WOMAN_001_ID01_HAIR_A_v004.png`
- 身材与造型参考：`body/candidates/CHR_WOMAN_001_ID02_HAIR_A_v003.png`
- 右前三分之四脸部参考：`face/candidates/CHR_WOMAN_001_FC03_HAIR_A_v001.png`
- 配对身体与丝袜参考：`body/candidates/CHR_WOMAN_001_BD01_HAIR_A_v003.png`
- 实际成功提交规格：见 `prompt_BD02_v001.md`

## 生成筛选

- 首次输出整体身份和袜面尚可，但一只脚跟抬起、脚尖点地，形成时装式站姿，不符合身体转面要求；未保存到项目。原始输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-7e19ca9c-2b82-4091-ba43-9f4ed8044c33.png`。
- 第二次仍从正式参考重新生成，增加双脚全掌着地和足跟落地约束，作为 BD02 v001 保存。

## 初检

- 人物自身右前三分之四方向成立，不是 BD01 的机械镜像。
- 双脚全掌着地、双跟落地、双腿不交叉，重心接近均匀中性站姿。
- 身份、身材比例、发型 A、粉色测试造型与 BD01 v003 基本连续。
- 腿部轻哑光丝袜、脚部连续覆盖和袜下酒红甲油可读；精确趾端结构仍由 FT01 独立验证。
- 未见明显肢体错误、脏色斑、文字或多余配饰。
- 当前只是候选，不自动写入正式资产索引。

## 用户审核结论

- 长相、身材比例和腿部丝袜质感符合要求。
- 脚趾区域的丝袜质感仍略弱，需要重新独立生成并加强。
- v002 不以 v001 为输入，也不在 v001 上局部修改。
