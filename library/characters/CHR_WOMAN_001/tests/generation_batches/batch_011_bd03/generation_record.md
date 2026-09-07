# Batch 011｜BD03 v001

- 日期：2026-09-06
- 状态：用户已批准
- 任务：全身严格左侧站姿，发型 A
- 生成方式：全新生成；未编辑、旋转或派生 BD01、BD02
- 工具：Codex 内置 image_gen
- 项目文件：`body/candidates/CHR_WOMAN_001_BD03_HAIR_A_v001.png`
- 原始成功输出：`/Users/verdvana/.codex/generated_images/01a06a37-a2d3-7201-863b-6544d4a4d45c/exec-bcf6dc32-2d32-4c7a-8fac-5bab4e61b377.png`
- 身份参考：`face/candidates/CHR_WOMAN_001_ID01_HAIR_A_v004.png`
- 身材与造型参考：`body/candidates/CHR_WOMAN_001_ID02_HAIR_A_v003.png`
- 左侧脸参考：`face/candidates/CHR_WOMAN_001_FC04_HAIR_A_v001.png`
- 材质与灯光参考：`body/candidates/CHR_WOMAN_001_BD01_HAIR_A_v003.png`
- 实际成功提交规格：见 `prompt_BD03_v001.md`

## 过程说明

- 首次调用因身材参考路径拼写错误而在读取输入阶段终止，没有进入生成，也没有产生图片。
- 修正路径后按同一规格完成首次实际生成。

## 初检

- 人物自身左侧严格 90° 方向成立，头部、躯干、骨盆和双脚朝向一致。
- 身份、发型 A、身材比例及粉色测试造型保持在既定角色范围内。
- 躯干厚度与骨盆姿态自然，未出现明显收腹、挺胸或夸张腰椎曲线。
- 双脚全掌和足跟落地；严格侧视造成的双腿与双脚遮挡属于该视角的正常结果。
- 腿部轻哑光袜层连续，画面整体干净，未见明显色斑或肢体错误。
- 当前仅为候选，不写入正式资产索引。

## 用户审核结论

- 2026-09-06：用户确认“非常好”，v001 写入正式资产索引。

## 画幅统一

- 用户随后要求 BD 全身静态资产保持统一竖幅。
- 以 v001 为唯一像素来源，居中裁去左右纯背景，再等比例缩放为 913×1723；没有 AI 重绘、补画或调色。
- 竖幅派生文件：`body/candidates/CHR_WOMAN_001_BD03_HAIR_A_v002.png`，现为正式索引入口；v001 保留作横幅生成源。
