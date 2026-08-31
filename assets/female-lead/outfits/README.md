# 女主角服装锚点

## female-lead-outfit-anchor-sheet-v1.png

- 状态：首批四套造型锚点
- 身份基准：`assets/female-lead/key-art/female-lead-key-art-fresh-v1.png`
- 对应提示词：`assets/female-lead/outfits/outfit-anchor-sheet-v1.md`
- 生成方式：Codex 内置图像生成

### 四套造型

1. 白色短款运动上衣、粉色瑜伽裤、白粉跑鞋。
2. 米色羊绒连衣短裙、敞开棕色风衣、黑色微透肉连裤袜、棕色短靴。
3. 黑色短款上衣、白色波点短裙、灰色透肉丝袜、黑色绒面猫跟鞋。
4. 玫红色上衣、白色短裤、白色透肉丝袜、浅粉色露脚背中跟鞋。

## female-lead-homewear-anchor-fresh-v1.png

- 状态：当前正式居家服锚点，从核心定妆照全新生成
- 身份基准：`assets/female-lead/key-art/female-lead-key-art-fresh-v1.png`
- 对应提示词：`assets/female-lead/outfits/homewear-outfit-anchor-fresh-v1.md`
- 生成方式：Codex 内置图像生成；未输入或修改任何旧居家服图片
- 造型：浅粉白色短款睡裙、肉色天鹅绒哑光透肉连裤丝袜、浅粉色薄底平底露趾拖鞋
- 构图：单人全身主图与同次生成的鞋袜材质细节窗，无文字标注
- 关键结构：脚趾前缘连续受力线、覆盖并连接趾缝的朦胧纱层、丝袜下面柔化透出的暗红色甲油

### 使用规则

- 本图用于锁定服装组合、配色、材质与鞋袜关系；人物身份仍以核心定妆照为最高优先级。
- 所有后续图片、分镜、首尾帧和视频提示词，只要居家拖鞋与脚趾入镜，都必须逐字加入 `assets/female-lead/hosiery/closed-foot-pantyhose-toe-lock.md`；任何脚趾看似裸露的结果直接拒绝。
- 运动装后续生成时需特别强调：瑜伽裤与运动鞋之间的脚踝处，应能辨认内穿丝袜的轻微光泽和半透明质感。
- 不应把四栏画面直接当作剧情场景；单套造型进入视频前，应结合场景重新生成单人全身锚点。
