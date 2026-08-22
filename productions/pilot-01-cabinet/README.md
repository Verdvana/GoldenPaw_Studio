# 试播短片01：《打不开的柜门》

- 形式：竖屏短片，9:16
- 目标时长：约20秒
- 对白：无
- 核心事件：猫咪为打开防宠物锁制作遥控执行器，被女主撞见后试图装作只是测试设备，最终获得鱼肉零食。
- 叙事原则：只讲清一个事件；技术能力服务于障碍，不额外塞入旅行、Vision Pro、毛球弱点或旁白设定。

## 文件

### 前期文档

- `docs/script.md`：锁定版剧本与节奏。
- `docs/shot-list.md`：逐镜头拍摄要求。
- `docs/continuity.md`：角色、空间、道具和动作连续性。

### 本片资产

- `assets/storyboards/`：历史分镜图、状态与对应提示词说明。
- `assets/keyframes/`：镜头1至镜头6共12张正式候选首尾帧。

### 本片提示词

- `prompts/storyboards/`：本片分镜生成提示词。
- `prompts/keyframes/`：本片六个镜头的首尾帧生成提示词。
- `prompts/video/platform-neutral-v2.md`：平台无关的全片视频提示词。
- `prompts/video/shot-01-motion-v1.md` 至 `shot-06-motion-v1.md`：逐镜头实际提交提示词。

### 验收

- `qa/video-checklist.md`：视频抽帧与连续性验收清单。

## 全局引用资产

本片只引用、不复制以下通用母版：

- `assets/character/`：赛博金渐层身份、动作与装备母版。
- `assets/female-lead/`：女主身份、服装、表情与体型母版。
- `assets/duo/key-art/`：双角色正式定妆。
- `assets/duo/scale/`：双角色身高比例。

## 当前阶段

旧版 v1 因女主服装错误已停用，v2 因脚趾处丝袜覆盖证据不足已停用。逐镜头9:16关键帧阶段和六镜头视频生成包均已完成，总目标时长20.5秒。下一步在支持首尾帧控制的视频工具中先运行镜头1运动一致性测试；通过后按镜头2至镜头6顺序生成。
