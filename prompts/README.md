# 提示词使用规则

生成任何图片或视频前，先读取项目根目录 `AGENTS.md` 与 `docs/media-generation-guardrails.md`。

女主穿露趾鞋或露趾拖鞋且脚趾入镜时，实际提交给生成模型的提示词必须完整包含：

`prompts/_shared/closed-foot-pantyhose-toe-lock.md`

该固定段落不能缩写或仅以“脚趾被丝袜包裹”替代。生成结果不满足四项脚部验收时，不得登记为正式候选。

需要选择或生成丝袜参考资产时，从 `assets/female-lead/hosiery/README.md` 进入，并按 `prompts/female-lead/hosiery/README.md` 组合身份、材质、结构视角和姿势参考。不要把整个资产总览或互相冲突的多张参考一次性提交给模型。
