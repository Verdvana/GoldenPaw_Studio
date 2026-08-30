# 女主角表情与动作

## female-lead-micro-expressions-v1.png

- 状态：微表情扩展母版 v1
- 身份基准：`assets/female-lead/key-art/female-lead-key-art-fresh-v1.png`
- 脸部结构基准：`assets/female-lead/identity/face-identity-master-v1.png`
- 当前服装基准：`assets/female-lead/outfits/female-lead-homewear-anchor-fresh-v1.png`
- 内容：12 种自然微表情，按从左到右、从上到下排列。
- 对应提示词：`prompts/female-lead/micro-expressions-v1.md`
- 生成方式：Codex 内置图像生成。

### 十二种微表情

1. 平静专注。
2. 温柔闭口微笑。
3. 明亮自然大笑。
4. 忍笑、略带调皮。
5. 好奇挑眉。
6. 轻度困惑。
7. 专注思考。
8. 吸气惊讶。
9. 担忧关切。
10. 尴尬害羞。
11. 温柔共情。
12. 困倦疲惫。

用于视频时，可把相邻强度的状态作为过渡参考，不要逐帧机械复刻；脸型、眼睛大小和年龄感仍以身份母版为最高优先级。

## female-lead-expressions-actions-v1.png

- 状态：首套表情与日常动作锚点
- 身份基准：`assets/female-lead/key-art/female-lead-key-art-fresh-v1.png`
- 脸部结构基准：`assets/female-lead/identity/face-identity-master-v1.png`
- 对应提示词：`prompts/female-lead/expressions-actions-v1.md`
- 生成方式：Codex 内置图像生成

### 六种反应

1. 温柔默认：柔和微笑、双手相握。
2. 活泼开心：自然笑、随手整理头发。
3. 宠溺互动：俯身低头看向画面外的猫咪。
4. 无奈纵容：一手叉腰、歪头带笑。
5. 技术震惊：自然惊讶、一手轻掩嘴。
6. 好奇骄傲：俯身指向画面外的电子作品并赞许微笑。

### 使用原则

- 这六种反应可以作为短视频表演母版，不要求每个镜头机械复刻姿势。
- 表情幅度应明显高于赛博金渐层，但保持真人自然表演，不能通过放大眼睛或改变五官结构制造情绪。
- 第3和第6种动作的视线落点需根据猫咪或电子作品在镜头中的实际位置调整。
