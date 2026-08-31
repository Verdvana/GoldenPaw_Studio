# 试播短片 01：《打不开的柜门》

本文件是本视频工程的唯一工作入口。视频生成类 AI 开始工作前必须完整读取本文件，并按下方顺序加载文件；不得仅凭文件名推断任务。

## 目标

- 形式：竖屏短片，9:16。
- 总时长：20.5 秒。
- 对白：无。
- 核心事件：猫咪为打开防宠物锁制作遥控执行器，被女主撞见后装作只是在测试设备，最终获得鱼肉零食。
- 叙事边界：只讲清这个事件，不加入旅行、Vision Pro、毛球弱点或旁白设定。
- 当前任务：先生成并验收镜头 1；通过后依次处理镜头 2–6。

## 必读顺序

1. 仓库强制规则：`AGENTS.md`。
2. 本片剧本：`brief/script.md`。
3. 本片镜头表：`brief/shot-list.md`。
4. 本片连续性：`brief/continuity.md`。
5. 全片平台无关提示词：`video/platform-neutral-v2.md`。
6. 当前镜头的运动提示词：`video/shot-NN-motion-v1.md`。
7. 当前镜头的首尾帧：`keyframes/shot-NN-start-v1.png` 与 `keyframes/shot-NN-end-v1.png`。
8. 输出前验收：`qa/video-checklist.md`。

若当前镜头包含女主可见脚部，还必须完整读取：

- `assets/female-lead/hosiery/media-generation-guardrails.md`
- `assets/female-lead/hosiery/closed-foot-pantyhose-toe-lock.md`

## 工程目录

- `brief/`：本片剧本、镜头表与连续性；内容优先级最高。
- `storyboards/`：本片分镜图、分镜提示词与历史状态。
- `keyframes/`：本片逐镜头首尾帧、对应提示词与登记说明。
- `video/`：本片全片和逐镜头视频提示词；生成结果放入 `video/outputs/`。
- `qa/`：本片验收清单与后续抽帧记录。

本目录不得放入可复用的角色母版，也不得收纳其他视频的文件。

## 本片引用的全局角色资产

以下文件只引用、不复制。单角色核心身份优先；双角色资产只补充相对比例与互动关系。

- 猫咪身份：`assets/cyber-golden-shaded/key-art/cyber-golden-shaded-key-art-reference-v1.png`
- 女主身份：`assets/female-lead/core/female-lead-key-art-fresh-v1.png`
- 双角色比例：`assets/female-lead-and-cyber-golden-shaded/scale/female-lead-cat-height-scale-v1.png`
- 双角色互动气质：`assets/female-lead-and-cyber-golden-shaded/key-art/female-lead-cat-official-key-art-v1.png`

女主居家造型不再引用全局服装图片。本片服装、丝袜、拖鞋和配饰以 `brief/continuity.md` 的文字要求及当前镜头的本地首尾帧为准。

## 每个镜头的执行方式

1. 一次只处理一个镜头。
2. 以上述首帧为起始画面、尾帧为结束目标；平台只支持一张参考图时优先首帧，尾帧用于第二轮校正。
3. 直接使用对应运动提示词中的“实际提交提示词”，不得删改时长、固定机位、动作因果或负面约束。
4. 先生成无声版本，文件写入 `video/outputs/`，命名为 `shot-NN-video-vNN.<扩展名>`。
5. 按 `qa/video-checklist.md` 抽帧验收，并把结果记录为 `qa/shot-NN-video-vNN.md`。
6. 未通过的输出不得标记为正式候选；修订时递增版本号，不覆盖旧结果。

## 镜头特殊约束

- 镜头 1 与镜头 6：女主脚部可见，必须逐帧检查完整包脚丝袜、暗红甲油和露趾拖鞋。
- 镜头 4 与镜头 5：女主脚部必须始终在画外，不得出现鞋脚残片。
- 所有镜头：固定机位，禁止自动运镜、自动变焦和镜头重构。
- 角色身份、柜体、手机、鱼肉袋、遥控器、执行器、LED 状态及柜门方向必须遵守 `brief/continuity.md`。

## 当前状态

- 分镜 v1：停用，女主服装错误。
- 分镜 v2：停用，脚趾处丝袜覆盖证据不足。
- 六个镜头共 12 张 9:16 首尾帧：已登记为正式候选。
- 六个逐镜头视频生成包：已完成。
- 尚未登记视频成片；下一步为镜头 1 运动一致性测试。
