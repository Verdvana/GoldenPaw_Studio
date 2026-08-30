# 女主角身份参考

## face-identity-master-v1.png

- 状态：脸部身份母版 v1
- 身份基准：`assets/female-lead/key-art/female-lead-key-art-fresh-v1.png`
- 内容：正面、左三分之四、左侧面、右三分之四、右侧面。
- 用途：锁定脸型、五官比例、鼻型、脸颊体积、下颌、肤色、年龄感与发型。
- 对应提示词：`prompts/female-lead/face-identity-master-v1.md`
- 生成方式：Codex 内置图像生成。

后续生成优先级：核心定妆照决定整体身份，脸部身份母版补充不同角度的面部结构；不得用表情图反向覆盖身份母版。

## female-lead-head-angles-v1.png

- 状态：头部与机位角度扩展母版 v1
- 身份基准：`assets/female-lead/key-art/female-lead-key-art-fresh-v1.png`
- 脸部结构基准：`assets/female-lead/identity/face-identity-master-v1.png`
- 当前服装基准：`assets/female-lead/outfits/female-lead-homewear-anchor-fresh-v1.png`
- 内容：正面、左右三分之四、左右侧面、低头、抬头、高机位左三分之四、低机位右三分之四。
- 对应提示词：`prompts/female-lead/head-angles-v1.md`
- 生成方式：Codex 内置图像生成。

本图用于补充俯仰角和机位高度参考。标准脸部结构仍以 `face-identity-master-v1.png` 为最高优先级；在视频运动中应连续插值头部姿态，避免遮挡恢复后脸型或鼻型跳变。
