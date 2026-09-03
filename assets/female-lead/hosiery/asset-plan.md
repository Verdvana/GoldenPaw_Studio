# 丝袜视觉模板与露趾鞋适配计划

本文件集中管理丝袜视觉模板与露趾鞋适配清单。每完成一项，只有通过 `qa.md` 验收并在 `README.md` 的正式资产索引登记后，才能把状态改为 `[x]`。正式视觉文件统一放入 `visuals/`。

## 固定生成基准

除单项另有说明外，所有穿着图统一使用：

- 女主已锁定的脚部身份与自然身体比例；以 `../core/female-lead-body-turnaround-v1.png` 为比例基准，保持自然饱满大腿、正常膝位、适度饱满并向踝部收窄的小腿，以及与小腿和身高匹配的正常足长、足宽，禁止长腿模特化、过细小腿或小脚漂移。
- 肉色 30D、天鹅绒哑光、无花纹、完整包脚连裤丝袜。
- 暗红色甲油只存在于脚趾背侧甲板，并仅在该甲板实际可见时作为袜面下的朦胧酒红色块；足底、前掌、趾腹和脚趾下侧禁止出现甲油色块。
- 袜面从脚踝连续覆盖脚背、全部脚趾和足底。
- 趾间为一整片受横向张力的连续曲面，不陷入趾缝，不逐趾包裹。
- 袜头前缘无可见缝合线、横线、补强带或任何连接线。
- 褶皱按姿势深度与 30D 轻薄尺度控制：站立、提踵/跖屈和半蹲时脚踝前后侧、脚背、膝窝与膝前均贴体平顺，不出现可辨认的织物褶皱组；全蹲时脚踝前侧只允许 2–3 条极细浅低对比纹，膝窝至多一条柔和浅线，跟腱—后踝与膝前保持平顺；禁止厚重横纹、堆叠褶、深沟槽、袋状松弛、袜面离体或近似 150D 的体积感。
- 中性浅灰背景、标准白平衡、柔和主光加轻微侧光。
- 脚部清晰对焦，长边不低于 2048 px；不使用景深、阴影或鞋面遮挡掩盖袜头结构。
- 脚趾可见时逐字加入 `assets/female-lead/hosiery/closed-foot-pantyhose-toe-lock.md`。

鞋型母版只定义鞋子的颜色、鞋面、鞋口、鞋底、鞋跟和带扣结构。穿着适配图才负责证明丝袜与鞋口的正确关系。不得使用穿着裸脚的鞋履照片作为主要参考。

## 生成顺序和状态

状态说明：

- `[ ]`：尚未生成。
- `[~]`：已有候选，尚未通过全部验收。
- `[x]`：已通过验收并登记为正式资产。
- `[!]`：暂停或存在结构冲突，必须先解决说明中的问题。

---

## 已有视觉模板

- [x] `MAT-N15-L01`｜`visuals/hosiery-nude-15d-velvet-matte-plain-none-front-standing-neutral-v01.png`｜肉色 15D 天鹅绒哑光全腿正面模板；用于透肤度、颜色、织物感和腿脚整体连续性。2026-09-03 按女主身体转面重做，修正旧版高挑纤细身型和脚部偏小问题；绿色泳装与泳池背景另经用户确认为 `LOOK-SWIM-GREEN-POOL-V1` 固定参考，上肢伸展动作不固定。
  - 提示词版本：`MAT-N15-L01-P2`；内置 ImageGen 精确重生成；完整逐字加入三段脚趾/足底硬锁，并明确禁止长腿模特化、小脚和广角拉伸。
  - 输入参考：旧正式图（只锁定泳池场景、绿色泳装、正面站姿与 15D 材质方向）、`../core/female-lead-body-turnaround-v1.png`（唯一身体比例基准）、`../core/female-lead-key-art-fresh-v1.png`（唯一身份基准）。
  - 生成与 QA：2026-09-03；原生输出 899 × 1750 PNG；A–F 通过，G 的整体材质可读性通过但长边低于 2048 px 建议值；身型、腿长、腿围、膝位及脚相对小腿的比例已回归女主基准，15D 袜面从腰部连续覆盖至趾端，隔袜酒红甲油可辨。旧版按 `proportion-drift` 移入 `rejected/`。
- [x] `MAT-N15-L02`｜`visuals/hosiery-nude-15d-velvet-matte-plain-none-front-three-quarter-standing-neutral-v01.png`｜前侧约 45°全身中性站立；补充女主正确比例和 15D 材质的斜向轮廓。
  - 提示词版本：`MAT-N15-L02-P1`；内置 ImageGen；以身份保持方式改为前侧约 45°中性站立，完整逐字加入三段脚趾/足底硬锁。
  - 输入参考：MAT-N15-L01（唯一材质、修正后身型、绿色泳装与泳池摄影基准）、`../core/female-lead-body-turnaround-v1.png`（比例）、`../core/female-lead-key-art-fresh-v1.png`（身份）。
  - 生成与 QA：2026-09-03；原生输出 899 × 1749 PNG；A–F 通过，G 的整体可读性通过但长边低于 2048 px 建议值；躯干、腿围、膝位、足长与正面版一致，15D 袜面和隔袜甲油连续。
- [x] `MAT-N15-L03`｜`visuals/hosiery-nude-15d-velvet-matte-plain-none-back-standing-neutral-v01.png`｜正背面全身中性站立；检查后腰—大腿—膝窝—小腿—跟腱—足跟比例与材质连续性。
  - 提示词版本：`MAT-N15-L03-P1`；内置 ImageGen；严格正背面中性站立，完整逐字加入三段脚趾/足底硬锁。
  - 输入参考：MAT-N15-L01（材质、身型与摄影）、MAT-N15-L02（跨视角一致性）、`../core/female-lead-body-turnaround-v1.png`（背部比例）。
  - 生成与 QA：2026-09-03；原生输出 899 × 1748 PNG；A–F 通过，G 的整体可读性通过但长边低于 2048 px 建议值；背部、腿脚比例与前两图一致，后腿、跟腱和足跟处 15D 袜面连续；背侧甲板不可见，因此无甲油色块。
- [!] `MAT-N15-P01`｜`visuals/hosiery-nude-15d-velvet-matte-plain-none-back-half-squat-v01.png`｜正背面半蹲；目标锁定同一女主比例、双脚全掌着地及 15D 袜面在屈髋屈膝下的连续性。
  - 生成状态：2026-09-03 使用内置 ImageGen 连续三次在输出阶段被安全系统按 `sexual` 误判拦截，均未产生文件或候选；不得以不同人物、不同身型、不同服装或不同丝袜材质替代。
  - 后续要求：若恢复生成，必须以 MAT-N15-L03 为唯一姿态编辑目标，并以身体转面锁定比例；采用中性运动生物力学／服装贴合技术图表达，保持正背面、适度半蹲、双脚平放、脚跟不抬和 15D 袜面轻薄平顺。
- [x] `MAT-N15-P02`｜`visuals/hosiery-nude-15d-velvet-matte-plain-none-front-three-quarter-deep-squat-v01.png`｜前侧约 45°严格全蹲；检查女主固定身体比例、落跟受力与 15D 袜面在深度屈髋屈膝下的连续性。
  - 提示词版本：`MAT-N15-P02-P6`；内置 ImageGen 从干净参考单次重生成；保持前侧约 45°、全深度蹲姿、双脚全掌着地与已确认身体比例，上肢为前臂自然搭在大腿、双手松弛交叠；同时一次性生成 15D 包趾袜膜、隔袜甲油与全身统一柔光，明确禁止斑驳光、泳池焦散投影、局部蒙版边界及重复重绘噪点；完整逐字加入三段脚趾/足底硬锁。
  - 输入参考：MAT-N15-L02（唯一干净人物、15D 材质、绿色泳装、泳池摄影与均匀光照基准）、`../core/female-lead-body-turnaround-v1.png`（最高身体比例基准）、BASE-C01（只锁定统一包趾袜膜、趾间浅弧与隔袜酒红甲油）；不再以任何多次局部编辑结果作为输入。
  - 生成与 QA：2026-09-03；原生输出 899 × 1748 PNG；A–F 通过，G 的整体可读性通过但长边低于 2048 px 建议值；骨段长度、腿围与足长保持，双脚全掌着地且脚跟未抬；前臂由大腿自然承托，肩、肘、腕与双手放松；全身由同一柔光照明，面部、手臂、躯干、双腿和袜面明暗连续，无块状光斑、局部曝光岛、泳池焦散或蒙版叠加痕迹；15D 袜面连续覆盖脚趾和足底，趾间为柔和浅过渡，无袜头横缝，暗红甲油仅隔袜朦胧位于可见背侧甲板。
  - 尝试记录：原 `P1` 身体比例与全蹲几何合格，但用户指出脚趾呈裸脚感且双臂悬空不自然，已移入 `rejected/`；`P2` 修正上肢动作但趾缝仍过深；`P3` 统一袜膜后甲油过淡；`P4` 虽修正甲油，但用户复检发现多轮编辑累积出全图明暗光斑，已移入 `rejected/hosiery-nude-15d-velvet-matte-plain-none-front-three-quarter-deep-squat-mottled-lighting-cumulative-edit-rejected-v01.png`；首次干净重生成 `P5` 在输出阶段被安全系统误判拦截、未产生文件；`P6` 改用三张干净参考一次合成并通过 QA。

## A0｜前置视觉模板

鞋履适配开始前，先完成以下肉色 30D 天鹅绒哑光无花纹基准。所有脚部均已穿完整包脚丝袜；不使用裸脚图作为模型正向参考。

- [x] `BASE-L01`｜`visuals/hosiery-nude-30d-velvet-matte-plain-none-front-standing-neutral-v01.png`｜下半身正面站立｜检查大腿—膝—小腿—脚踝—脚趾的材质连续性。
  - 提示词版本：`BASE-L01-P1`；内置 ImageGen；单张竖幅写实技术参考；完整逐字加入 closed-foot toe lock 与 deep-red toenail visibility lock。
  - 输入参考：`core/female-lead-key-art-fresh-v1.png`（唯一身份）、`core/female-lead-body-turnaround-v1.png`（正面身体比例）、`visuals/hosiery-nude-15d-velvet-matte-plain-none-front-standing-neutral-v01.png`（肉色哑光材质与连续性；目标提升为 30D）。
  - 生成与 QA：2026-08-31；原生输出 899 × 1750 PNG；用户确认通过并批准入库。首轮定向编辑因安全过滤未产生文件，不属于本项资产。
- [x] `BASE-L02`｜`visuals/hosiery-nude-30d-velvet-matte-plain-none-top-three-quarter-standing-neutral-v01.png`｜下半身高位三分之四站立｜作为后续服装生成的主要全腿材质参考。
  - 提示词版本：`BASE-L02-P1`；内置 ImageGen；单张竖幅高机位三分之四写实技术参考；完整逐字加入 closed-foot toe lock 与 deep-red toenail visibility lock。
  - 输入参考：`core/female-lead-key-art-fresh-v1.png`（唯一身份）、`core/female-lead-body-turnaround-v1.png`（身体比例）、`visuals/hosiery-nude-30d-velvet-matte-plain-none-front-standing-neutral-v01.png`（已批准的 30D 材质与连续性）。
  - 生成与 QA：2026-08-31；原生输出 899 × 1749 PNG；A–F 通过，G 的清晰可读性通过但长边低于 2048 px 建议值；后脚部分脚趾因三分之四透视自然遮挡，可见趾均通过硬锁。
- [x] `BASE-C01`｜`visuals/hosiery-nude-30d-velvet-matte-plain-none-front-standing-neutral-toe-closeup-v01.png`｜脚趾正面结构特写｜检查无袜头横线和连续趾间浅弧。
  - 提示词版本：`BASE-C01-P3`；内置 ImageGen 精确编辑；以已批准 BASE-L01 为唯一编辑目标，仅收紧为膝下—双脚正面构图并提升织物结构清晰度；完整逐字加入 closed-foot toe lock 与 deep-red toenail visibility lock。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-front-standing-neutral-v01.png`（编辑目标，同时锁定女主腿—踝—脚比例、姿势、30D 材质、光照与背景）。
  - 生成与 QA：2026-09-01；原生输出 900 × 1747 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；十枚甲油均隔袜可辨，袜头无横线，趾间连续浅弧与微织纹可读。
  - 尝试记录：`P1`、`P2` 均在输出阶段被安全过滤器拒绝，未产生图片；用户要求重试后，`P3` 以 BASE-L01 精确编辑成功。
- [x] `BASE-C02`｜`visuals/hosiery-nude-30d-velvet-matte-plain-none-top-three-quarter-standing-neutral-foot-closeup-v01.png`｜脚背高位三分之四结构特写｜检查脚踝—脚背—趾尖连续性。
  - 提示词版本：`BASE-C02-P2`；内置 ImageGen 精确编辑；以已批准 BASE-C01 为唯一编辑目标，仅改为高位三分之四机位；完整逐字加入 closed-foot toe lock 与 deep-red toenail visibility lock。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-front-standing-neutral-toe-closeup-v01.png`（编辑目标，同时锁定女主小腿—脚踝—脚部比例、十趾结构、30D 材质、光照与背景）。
  - 生成与 QA：2026-09-01；原生输出 900 × 1747 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；脚踝—脚背—趾尖织纹连续，双脚前后轻微错位，可见趾均通过硬锁。
  - 尝试记录：`P1` 使用 BASE-C01、BASE-L02 与女主核心身份三参考时在输出阶段被安全过滤器拒绝，未产生图片；`P2` 改用 BASE-C01 单一编辑目标后成功。
- [x] `BASE-C03`｜`visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-standing-neutral-foot-closeup-v01.png`｜脚部外侧结构特写｜检查小脚趾侧和袜头前缘。
  - 提示词版本：`BASE-C03-P3`；内置 ImageGen 精确编辑；由已批准 BASE-C02 延续比例与材质，最终收敛为单脚外侧三分之四结构模板；完整逐字加入 closed-foot toe lock 与 deep-red toenail visibility lock。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-top-three-quarter-standing-neutral-foot-closeup-v01.png`（初始编辑目标，锁定女主小腿—脚踝—脚部比例、30D 材质、光照与背景）；`P3` 以 `P1` 前景主脚为编辑目标，移除被遮挡的后脚。
  - 生成与 QA：2026-09-01；原生输出 899 × 1748 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；单脚五枚隔袜甲油均可辨，小脚趾侧、外踝、袜头前缘与可见足底边缘无遮挡。
  - 尝试记录：`P1` 双脚外侧构图中后脚甲油被遮挡；`P2` 调整后脚位置仍未满足五枚甲油全部可辨；两者均未入库。`P3` 改为职责单一的单脚外侧模板后通过。
- [x] `BASE-C04`｜`visuals/hosiery-nude-30d-velvet-matte-plain-none-sole-heel-lift-v03.png`｜足底结构图｜检查足底、前掌、趾腹连续覆盖及四处趾间袜面张力曲线。
  - 提示词版本：`BASE-C04-P9`；内置 ImageGen 精确编辑；以原正式 `v02` 为唯一编辑目标，只在四处趾间区域重建与周围同色、同密度、同微织纹的局部连续袜膜；完整逐字加入更新后的 closed-foot toe lock、deep-red toenail visibility lock 与 plantar-view anatomy lock。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-sole-heel-lift-v02.png`（唯一编辑目标，锁定单脚比例、纯足底抬脚构图、肉色 30D 天鹅绒哑光材质、光照与背景）。
  - 生成与 QA：2026-09-02；原生输出 898 × 1752 PNG；用户确认通过，A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；足跟、足弓、前掌、五枚趾腹与趾端织纹连续，纯足底视角无任何甲油色块，四处趾间可见低对比、局部化的连续袜面张力过渡。
  - 尝试记录：原 `P1`–`P6` 记录保留；用户指出 `v02` 的趾间袜面张力曲线不足后启动修订。`P7` 出现偏深纵向暗沟，按 `toe-glove` 风险不入库；`P8` 形成横贯趾根的浅色带状边界，按 `toe-seam` 与 `reference-conflict` 不入库；`P9` 消除带状伪影并保留纯足底无甲油结构，经用户确认作为 `v03` 入库。原 `v02` 保留为历史版本，不再作为 BASE-C04 首选参考。
- [x] `BASE-P01`｜`visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-half-squat-v01.png`｜侧面半蹲｜检查 30D 袜面在中等屈膝下仍贴体平顺、无可辨认褶皱组。
  - 提示词版本：`BASE-P01-P4`；内置 ImageGen 精确编辑；以原 P2 为编辑目标，只移除前踝与膝窝的可见织物横纹，保持严格侧视半蹲、自然比例、落跟受力和袜头结构；完整逐字加入三段脚趾/足底硬锁。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-half-squat-v01.png` 的原 P2 正式版（唯一编辑目标）。
  - 生成与 QA：2026-09-01；原生输出 1024 × 1536 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；大腿—膝—小腿—脚踝—足部比例与落跟姿势保持，半蹲脚踝、脚背、膝窝和膝前不再形成可数织物褶皱组，只保留自然关节曲面明暗；五趾与连续袜面通过。
  - 尝试记录：原 `P1`、`P2` 的姿势与结构记录保留；用户进一步指出原 P2 褶皱量偏厚。`P3` 首次减量后前踝仍残留三条明显横纹，未入库；`P4` 再次局部弱化后通过。原 P2 已移入 `rejected/`。
- [x] `BASE-P02`｜`visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-heel-lift-v02.png`｜侧面提踵｜检查脚背伸展、前掌受力及后踝贴合张力。
  - 提示词版本：`BASE-P02-P5`；内置 ImageGen 精确编辑；采用严格侧视、近侧单腿完整可见且远侧腿自然完全遮挡的温和日常提踵构图；完整逐字加入更新后的 closed-foot toe lock、deep-red toenail visibility lock、plantar-view anatomy lock 与后踝防松垮约束。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-half-squat-v01.png`（锁定女主自然腿脚比例、肉色 30D 材质与摄影语言）和 `visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-standing-neutral-foot-closeup-v01.png`（仅辅助初始侧面脚型与袜头结构）；最终 `P5` 以 `P4` 为唯一编辑目标，只重建跟腱—后踝袜面。
  - 生成与 QA：2026-09-01；原生输出 1024 × 1536 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；膝部自然微屈、小腿温和发力、脚跟轻度抬升，跖骨头与五趾趾腹形成宽而连续的前掌承重面；跟腱—后踝袜面纵向贴体张紧，无多层横褶、堆叠或松袋感；背侧甲油隔袜朦胧可见，足底及趾腹无甲油色块。
  - 尝试记录：`P1` 脚跟过高、受力集中趾端且脚趾抓地卷曲，按 `anatomy`、`toe-glove` 与 `wrinkle-physics` 判定不入库；`P2` 定向修复在输出阶段被安全过滤器拒绝，未产生图片；`P3` 仍接近足尖动作、趾屈曲且后踝出现过多平行褶皱，后由用户指出并新增 `ankle-slack` 失败类别；`P4` 修正前掌受力后曾入库，现由 `P5` 进一步消除后踝松垮观感并替换。旧 v01 已移至 `rejected/` 隔离。

前置模板全部通过后才开始 S01。其他颜色、厚度、光泽和花纹按实际服装需求逐项增加；硬锁改为材质中性版本前，不启动非肉色、非天鹅绒哑光的露趾模板。

## P0｜当前项目核心鞋型

居家拖鞋范围固定为 S01 宽面薄底零跟与 S02 窄面薄底零跟两种。原计划中的 S03 双带薄底平底居家拖鞋及其全部视角已于 2026-09-02 取消，不再进入生成队列。现有两种居家拖鞋仍可补齐计划内缺失视角和必要受力姿势。

### S01｜宽面薄底零跟居家拖鞋

浅粉色、单条宽鞋面、露趾、后跟开放、5–6 mm 柔性薄底，全长完全水平，无鞋跟、坡跟或厚底。当前居家造型的最高优先级。

- [x] `FW-S01-M`｜`visuals/shoe-wide-band-flat-home-slide-multiview-v01.png`｜无脚产品多视角鞋型母版。
  - 提示词版本：`FW-S01-M-P1`；内置 ImageGen；单张 2 × 2 写实产品总览，同一只右脚拖鞋依次展示高位三分之四、严格外侧、低位正面和大底视角；本项无脚、无女主、无丝袜，因此不加入脚趾硬锁。
  - 输入参考：无；完全按 S01 受控鞋型规格生成。
  - 生成与 QA：2026-09-01；原生输出 1402 × 1122 PNG；浅粉色单条宽鞋面、宽阔露趾口、开放后跟、5–6 mm 全长水平柔性薄底、零跟、零坡跟、零厚底均通过；四格无脚、无人物、无品牌与文字。
  - 使用边界：多格总览只供人工检查鞋型一致性；后续穿着适配生成前，应裁出与目标机位对应的单一视角，不直接提交整张多格图作为正向参考。
- [x] `FW-S01-F`｜`visuals/hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-front-standing-neutral-v01.png`｜正面站立，检查鞋口内全部可见脚趾。
  - 提示词版本：`FW-S01-F-P1`；内置 ImageGen 精确编辑；以已批准 BASE-L01 为编辑目标，只为双脚穿上 S01 宽面薄底零跟居家拖鞋；完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock、plantar-view anatomy lock 与物理褶皱分区规则。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-front-standing-neutral-v01.png`（编辑目标，锁定女主自然腿脚比例、正面站姿、肉色 30D 材质、光照和背景）；由 `visuals/shoe-wide-band-flat-home-slide-multiview-v01.png` 裁出的低位正面单视角临时图（只锁定浅粉宽鞋面、露趾口和薄底结构，未作为正式资产保存）。
  - 生成与 QA：2026-09-01；原生输出 900 × 1747 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；双脚居中入鞋并平整承重，十趾完整入镜，肉色 30D 袜面和十枚隔袜酒红甲油可读；宽鞋面位于甲板后方，浅粉鞋底与肉色袜面分界清楚。
  - 尝试记录：`P1` 继承已批准 BASE-L01 的纯色微织纹和袜头结构并完成鞋履适配；`P2` 虽减弱趾间凹陷，却在丝袜表面引入旋涡状伪花纹，按 `reference-conflict` 判定不入库；`P3` 纹理修复在输出阶段被安全过滤器拒绝，未产生图片；`P4` 再次出现伪花纹且部分甲油辨识度下降，未入库。最终保留职责最纯净的 `P1`。
- [x] `FW-S01-T`｜`visuals/hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-top-three-quarter-standing-neutral-v01.png`｜高位三分之四，检查脚踝—脚背—袜头连续性。
  - 提示词版本：`FW-S01-T-P1`；内置 ImageGen 精确编辑；以已批准 BASE-L02 为编辑目标，只为双脚穿上 S01 宽面薄底零跟居家拖鞋；完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock、plantar-view anatomy lock 与物理褶皱分区规则。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-top-three-quarter-standing-neutral-v01.png`（编辑目标，锁定女主自然腿脚比例、高位三分之四站姿、肉色 30D 材质、光照和背景）；由 `visuals/shoe-wide-band-flat-home-slide-multiview-v01.png` 裁出的高位三分之四单视角临时图（只锁定浅粉宽鞋面、露趾口、开放后跟和薄底结构，未作为正式资产保存）。
  - 生成与 QA：2026-09-01；原生输出 899 × 1748 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；前脚五枚隔袜酒红甲油完整可辨，后脚受自然透视与鞋面遮挡但所有可见甲板均正确；双脚完整入鞋，脚踝—脚背—趾端纯色微织纹连续，鞋底保持 5–6 mm 薄底零跟。
  - 尝试记录：`P1` 首轮通过，无失败候选。
- [x] `FW-S01-L`｜`visuals/hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-lateral-side-standing-neutral-v01.png`｜外侧，检查小脚趾侧、鞋底边缘和袜头前缘。
  - 提示词版本：`FW-S01-L-P2`；内置 ImageGen 精确编辑；以已批准 BASE-C03 为编辑目标，为单脚穿上 S01 宽面薄底零跟居家拖鞋，随后对首轮结果局部修复趾间张力弧和鞋底厚度；两轮均完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock、plantar-view anatomy lock 与物理褶皱分区规则。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-standing-neutral-foot-closeup-v01.png`（编辑目标，锁定单脚外侧三分之四比例、中性承重、肉色 30D 材质、光照和背景）；由 `visuals/shoe-wide-band-flat-home-slide-multiview-v01.png` 裁出的严格外侧单视角临时图（只锁定浅粉宽鞋面、开放后跟和 5–6 mm 水平薄底，未作为正式资产保存）；P2 以 P1 为唯一编辑目标。
  - 生成与 QA：2026-09-01；原生输出 901 × 1746 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；脚跟居中落在后掌，鞋底全长贴地且保持零跟薄底，外踝—脚背—袜头纯色微织纹连续；趾间袜面跨接为浅张力弧，可见背侧甲板均有隔袜酒红甲油，趾腹与足底无甲油色块；中性站立脚踝、跟腱和脚背无松垮褶皱。
  - 尝试记录：`P1` 完成鞋履适配，鞋型、脚跟落位和脚踝贴合正确，但趾间凹陷偏深，按逐趾包裹风险不入库；`P2` 仅修复趾间连续薄膜、浅弧张力和薄底边缘后通过，未改变腿脚比例与站立物理。
- [x] `FW-S01-Q`｜`visuals/hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-lateral-side-half-squat-v01.png`｜侧面半蹲，检查宽带拖鞋下 30D 袜面整体贴体平顺。
  - 提示词版本：`FW-S01-Q-P2`；内置 ImageGen 精确编辑；以原 P1 为唯一编辑目标，只移除前踝与膝窝可见横纹，保持 S01 宽带鞋型、半蹲姿势、自然比例和袜头结构；完整逐字加入三段脚趾/足底硬锁。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-lateral-side-half-squat-v01.png` 的原 P1 正式版（唯一编辑目标）。
  - 生成与 QA：2026-09-01；原生输出 1024 × 1536 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；脚跟完整居中且鞋底全长贴地，半蹲前踝、后踝、膝窝与膝前无可数织物褶皱组；S01 宽带、五趾和连续袜面保持。
  - 尝试记录：原 P1 因用户指出褶皱量偏厚而被替换，已移入 `rejected/`；`P2` 首轮减量通过。
- [x] `FW-S01-D`｜`visuals/hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-lateral-side-deep-squat-v01.png`｜侧面全蹲，检查落跟受力和不超过旧半蹲尺度的极轻量压缩纹。
  - 提示词版本：`FW-S01-D-P3`；内置 ImageGen 精确编辑；以原 P2 为唯一编辑目标，只把前踝褶皱栈缩减为 2–3 条极细浅低对比纹并把膝窝压缩减至至多一条浅线；完整逐字加入三段脚趾/足底硬锁。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-lateral-side-deep-squat-v01.png` 的原 P2 正式版（唯一编辑目标，锁定全蹲几何、自然比例、S01 鞋型、袜头、光照和背景）。
  - 生成与 QA：2026-09-01；原生输出 1024 × 1536 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；全蹲姿势、自然比例、脚跟和鞋底接地保持；前踝仅余少量极细浅低对比纹，膝窝压缩极弱，膝前与跟腱—后踝平顺，无 150D 般体积感；五趾与连续袜面通过。
  - 尝试记录：原 `P1`、`P2` 记录保留；用户指出 P2 褶皱偏厚后，P2 已移入 `rejected/`，`P3` 定向减量通过。

### S02｜窄面薄底零跟居家拖鞋

浅象牙粉色、单条窄鞋面、露出更多脚背，薄底零跟。用于检验鞋面遮挡减少后袜面是否仍连续。

- [x] `FW-S02-M`｜`visuals/shoe-narrow-band-flat-home-slide-multiview-v01.png`｜无脚产品多视角鞋型母版。
  - 提示词版本：`FW-S02-M-P1`；内置 ImageGen 精确编辑；以已批准 FW-S01-M 为编辑目标，保留单张 2 × 2 写实产品总览、鞋床轮廓、开放前后结构和 5–6 mm 零跟薄底，只把宽鞋面收窄为覆盖前掌跖骨区域的单条窄带，并把颜色调整为浅象牙粉；本项无脚、无女主、无丝袜，因此不加入脚趾硬锁。
  - 输入参考：`visuals/shoe-wide-band-flat-home-slide-multiview-v01.png`（编辑目标，锁定同一只右脚拖鞋的高位三分之四、严格外侧、低位正面和大底四视角，以及统一摄影布局、光照、鞋床和薄底结构）。
  - 生成与 QA：2026-09-01；原生输出 1402 × 1122 PNG；浅象牙粉单条窄鞋面在四格中的位置与连接一致，沿脚长方向覆盖深度约为 S01 宽带的 40–50%，脚背开放区明显增加；露趾、开放后跟、5–6 mm 全长水平柔性薄底、零跟、零坡跟、零厚底、大底微纹理均通过；无脚、人物、品牌或文字。
  - 尝试记录：`P1` 首轮通过，无失败候选。
  - 使用边界：多格总览只供人工检查鞋型一致性；后续穿着适配生成前，应裁出与目标机位对应的单一视角，不直接提交整张多格图作为正向参考。
- [x] `FW-S02-F`｜`visuals/hosiery-nude-30d-velvet-matte-plain-narrow-band-flat-home-slide-front-standing-neutral-v01.png`｜正面站立。
  - 提示词版本：`FW-S02-F-P2`；内置 ImageGen 精确编辑；最终以已批准 BASE-C01 为编辑目标，只为双脚穿上 S02 窄面薄底零跟居家拖鞋；完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock、plantar-view anatomy lock，并明确中性站立时脚踝、跟腱、脚背与趾端无可见褶皱或松垮。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-front-standing-neutral-toe-closeup-v01.png`（最终编辑目标，唯一锁定膝下比例、正面中性站姿、肉色 30D 材质、十趾结构、光照和背景）；由 `visuals/shoe-narrow-band-flat-home-slide-multiview-v01.png` 裁出的低位正面单视角临时图（只锁定浅象牙粉窄带、露趾口和薄底结构，未作为正式资产保存）。
  - 生成与 QA：2026-09-01；原生输出 901 × 1746 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；双脚完整居中入鞋并平整承重，十趾由连续袜面覆盖，趾间为柔和浅弧，十枚隔袜酒红甲油均清楚可辨且足底无甲油色块；窄带位于跖骨区域并留出更多脚背与趾根袜面，正面鞋底保持薄底零跟。
  - 尝试记录：`P1` 使用全腿正面模板时在输出阶段被安全系统误判拦截，未产生图片；`P2` 改用已批准的膝下正面结构特写作为编辑目标后首轮通过。
- [x] `FW-S02-T`｜`visuals/hosiery-nude-30d-velvet-matte-plain-narrow-band-flat-home-slide-top-three-quarter-standing-neutral-v01.png`｜高位三分之四。
  - 提示词版本：`FW-S02-T-P1`；内置 ImageGen 精确编辑；以已批准 BASE-L02 为编辑目标，只为双脚穿上 S02 浅象牙粉窄面薄底零跟居家拖鞋；完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock、plantar-view anatomy lock，并明确中性站立无褶皱、恰好五趾、窄带覆盖深度和鞋底全长水平。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-top-three-quarter-standing-neutral-v01.png`（编辑目标，唯一锁定女主自然腿脚比例、高位三分之四中性站姿、肉色 30D 材质、前后脚轻微错位、光照和背景）；由 `visuals/shoe-narrow-band-flat-home-slide-multiview-v01.png` 裁出的高位三分之四单视角临时图（只锁定浅象牙粉窄带、开放前后结构和 5–6 mm 薄底零跟，未作为正式资产保存）。
  - 生成与 QA：2026-09-02；原生输出 900 × 1748 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；前脚五枚隔袜酒红甲油完整可辨，后脚受自然三分之四透视但所有可见背侧甲板均正确；双脚完整居中入鞋，脚踝—脚背—趾端肉色 30D 微织纹连续，趾间保持柔和浅弧，袜头无横线；S02 单条窄带位于跖骨区域，脚背开放区充足，鞋底全长保持薄底零跟。
  - 尝试记录：`P1` 首轮通过，无失败候选。
- [x] `FW-S02-L`｜`visuals/hosiery-nude-30d-velvet-matte-plain-narrow-band-flat-home-slide-lateral-side-standing-neutral-v01.png`｜外侧站立。
  - 提示词版本：`FW-S02-L-P3`；内置 ImageGen 精确编辑；放弃从失败的穿鞋图继续修补，改以已批准 BASE-C03 五趾无鞋结构图为编辑目标，只增加 S02 浅象牙粉窄带拖鞋；完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock、plantar-view anatomy lock，并额外硬锁恰好五趾、自然趾序、均匀细密微织纹和中性站立无褶皱。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-standing-neutral-foot-closeup-v01.png`（最终编辑目标，唯一锁定单脚五趾解剖、外侧三分之四比例、肉色 30D 材质、光照和背景）；由 `visuals/shoe-narrow-band-flat-home-slide-multiview-v01.png` 裁出的严格外侧单视角临时图（只锁定浅象牙粉窄带、开放后跟和薄底结构，未作为正式资产保存）。
  - 生成与 QA：2026-09-01；原生输出 899 × 1748 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；单脚恰好五趾且趾序、间距与甲板位置自然；袜面从小腿、脚踝、脚背到趾端保持连续均匀细密微织纹，无涂抹、融化、旋涡或局部皮肤化；脚跟居中且薄底全长贴地，中性站姿脚踝、跟腱和脚背平顺无褶皱。
  - 尝试记录：`P1` 从 FW-S01-L 改鞋后出现六趾且袜头偏裸，按 `anatomy` 与 `bare-toe` 不入库；`P2` 局部重建后仍为六趾，并产生明显袜面涂抹/融化感，用户判定不合格，已移入 `rejected/`；`P3` 从 BASE-C03 五趾基准重新开始后通过。
- [x] `FW-S02-Q`｜`visuals/hosiery-nude-30d-velvet-matte-plain-narrow-band-flat-home-slide-lateral-side-half-squat-v01.png`｜侧面半蹲，检查窄带拖鞋下 30D 袜面整体贴体平顺。
  - 提示词版本：`FW-S02-Q-P4`；内置 ImageGen 精确编辑；以原 P3 为唯一编辑目标，只移除前踝与膝窝可见横纹，保持 S02 窄带宽度、姿势、比例和袜头结构；完整逐字加入三段脚趾/足底硬锁。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-narrow-band-flat-home-slide-lateral-side-half-squat-v01.png` 的原 P3 正式版（唯一编辑目标，锁定半蹲比例、S02 窄带、袜头、光照和背景）。
  - 生成与 QA：2026-09-01；原生输出 1024 × 1536 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；半蹲比例、脚跟接地和 28–35 mm S02 窄带保持；前后踝、膝窝和膝前无可数织物褶皱组；五趾、连续袜面与隔袜甲油通过。
  - 尝试记录：原 `P1`–`P3` 记录保留；用户指出 P3 褶皱量偏厚后，P3 已移入 `rejected/`，`P4` 定向减量通过。
- [x] `FW-S02-D`｜`visuals/hosiery-nude-30d-velvet-matte-plain-narrow-band-flat-home-slide-lateral-side-deep-squat-v01.png`｜侧面全蹲，检查落跟受力和不超过旧半蹲尺度的极轻量压缩纹。
  - 提示词版本：`FW-S02-D-P3`；内置 ImageGen 精确编辑；以原 P2 为唯一编辑目标，只把前踝褶皱栈缩减为 2–3 条极细浅低对比纹并把膝窝压缩减至至多一条浅线；完整逐字加入三段脚趾/足底硬锁、恰好五趾与窄带宽度约束。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-narrow-band-flat-home-slide-lateral-side-deep-squat-v01.png` 的原 P2 正式版（唯一编辑目标，锁定全蹲几何、自然比例、S02 窄带、袜头、光照和背景）。
  - 生成与 QA：2026-09-01；原生输出 1024 × 1536 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；全蹲姿势、自然比例、脚跟和鞋底接地、28–35 mm 窄带保持；前踝仅余少量极细浅低对比纹，膝窝压缩极弱，膝前与跟腱—后踝平顺，无 150D 般体积感；五趾、连续袜面与隔袜甲油通过。
  - 尝试记录：原 `P1`、`P2` 记录保留；用户指出 P2 褶皱偏厚后，P2 已移入 `rejected/`，`P3` 定向减量通过。

### S04｜一字带踝带 15 mm 微方跟露趾凉鞋

低饱和裸粉色，方圆头、单条前掌一字带、细踝带、两侧斜向后跟支撑带、露趾、开放后跟；前掌底约 4–5 mm，鞋床腰部收窄并自然上扬，后掌为独立 15 mm 微方跟。用于锁定鞋带压迫、脚背连续性、踝带上下丝袜材质一致性及低跟站姿受力；禁止回退为全长水平直板鞋底或居家拖鞋轮廓。

- [x] `FW-S04-M`｜`visuals/shoe-single-band-ankle-strap-15mm-low-block-heel-sandal-multiview-v01.png`｜无脚产品多视角鞋型母版。
  - 提示词版本：`FW-S04-M-P2`；内置 ImageGen 精确编辑；以旧 P1 四格图为编辑目标，保留四视角布局与摄影语言，统一重建为低饱和裸粉色、方圆头、单条前掌一字带、细踝带、两侧斜向后跟支撑、收腰鞋床和独立 15 mm 微方跟；本项无脚、无女主、无丝袜，因此不加入脚趾硬锁。
  - 输入参考：原 `visuals/shoe-ankle-strap-flat-sandal-multiview-v01.png` P1（仅锁定 2 × 2 布局、高位三分之四、严格外侧、低位正面和大底四视角，以及中性浅灰背景与柔和布光；旧直板平底鞋型明确不具约束力，现已移入 `rejected/`）。
  - 生成与 QA：2026-09-02；原生输出 1402 × 1122 PNG；鞋型 QA 通过但长边低于 2048 px 建议值；四格保持同一只右脚凉鞋，方圆头、前掌一字带、细踝带、斜向后跟支撑、外侧小扣具、收窄腰线、4–5 mm 前掌底和独立 15 mm 微方跟一致；外侧视角可清楚辨认前掌—足弓—后跟层次，大底视角显示独立前掌纹路与后跟落地片，无脚、人物、丝袜、品牌或文字。
  - 尝试记录：`P1` 虽通过原平底规格，但用户指出全长水平直板鞋底过于接近拖鞋，现按鞋型风格不匹配移入 `rejected/shoe-ankle-strap-flat-sandal-multiview-slide-like-rejected-v01.png`，严禁作为正向参考；`P2` 按用户确认的新样式首轮通过。
  - 使用边界：多格总览只供人工检查鞋型一致性；后续穿着适配生成前，应裁出与目标机位对应的单一视角，不直接提交整张多格图作为正向参考。
- [x] `FW-S04-F`｜`visuals/hosiery-nude-30d-velvet-matte-plain-single-band-ankle-strap-15mm-low-block-heel-sandal-front-standing-neutral-v01.png`｜正面站立。
  - 提示词版本：`FW-S04-F-P1`；内置 ImageGen 精确编辑；以已批准 BASE-C01 为编辑目标，只为双脚穿上新版 S04 一字带踝带 15 mm 微方跟凉鞋，并允许脚踝做适配低跟所需的极轻微跖屈；完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock 与 plantar-view anatomy lock。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-front-standing-neutral-toe-closeup-v01.png`（编辑目标，唯一锁定膝下比例、正面中性站姿、双脚十趾解剖、肉色 30D 材质、光照和背景）；由 `visuals/shoe-single-band-ankle-strap-15mm-low-block-heel-sandal-multiview-v01.png` 裁出的低位正面单视角临时图（只锁定方圆头、一字带、细踝带与两侧斜向支撑，未作为正式资产保存）。
  - 生成与 QA：2026-09-02；原生输出 900 × 1748 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；双脚各五趾且十枚隔袜酒红甲油清楚可辨，趾间为连续柔和浅弧，袜头无横线；30D 微织纹从小腿经踝带上下、脚背到趾端保持连续，踝带未形成材质分界或松垮褶皱；双脚居中入鞋，方圆头、一字带、踝带、斜向支撑与低跟站姿成立。
  - 尝试记录：`P1` 首轮通过，无失败候选。
- [x] `FW-S04-T`｜`visuals/hosiery-nude-30d-velvet-matte-plain-single-band-ankle-strap-15mm-low-block-heel-sandal-top-three-quarter-standing-neutral-v01.png`｜高位三分之四。
  - 提示词版本：`FW-S04-T-P8`；内置 ImageGen 精确编辑；在 P2 的低跟鞋型与高位构图基础上重新构建暴露趾端，消除逐趾纵向深沟，把五趾收束在同一片横向受力袜膜下，并将四处趾间限制为短、浅、柔和凹弧；完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock 与 plantar-view anatomy lock。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-top-three-quarter-standing-neutral-v01.png`（初始站姿与材质参考）；`visuals/shoe-single-band-ankle-strap-15mm-low-block-heel-sandal-multiview-v01.png` 的高位三分之四裁图（鞋型参考）；`visuals/hosiery-nude-30d-velvet-matte-plain-none-front-standing-neutral-toe-closeup-v01.png`（P8 的连续包趾袜膜与十趾解剖参考）；P8 以 P5 构图为编辑目标，仅重建暴露趾端。
  - 生成与 QA：2026-09-02；原生输出 902 × 1743 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；前脚五枚隔袜酒红甲油完整可辨，后脚可见甲板正确；脚踝—脚背—趾端 30D 微织纹连续，袜头无横线，四处趾间不再形成向后延伸的深沟，而由同一片袜面跨接为短浅凹弧；两脚居中入鞋，一字带、踝带、斜向支撑、收腰鞋床和低位独立微方跟成立。
  - 尝试记录：`P1` 方跟接近 3 cm，未保存；`P2` 修正为 15 mm 低跟后曾入库，但用户复检指出脚趾处袜面张力曲线不足，现移入 `rejected/hosiery-nude-30d-velvet-matte-plain-single-band-ankle-strap-15mm-low-block-heel-sandal-top-three-quarter-standing-neutral-missing-toe-tension-rejected-v01.png`；`P3` 局部修复仍无可读跨接弧，`P4` 放大脚部后仍有深趾缝，`P5`–`P7` 分别因仅淡化趾缝、仍呈逐趾纵沟或趾部遮挡而未入库；`P8` 改用统一袜膜包覆逻辑，消除长纵沟并形成四处短浅张力过渡后替换正式图。
- [x] `FW-S04-L`｜`visuals/hosiery-nude-30d-velvet-matte-plain-single-band-ankle-strap-15mm-low-block-heel-sandal-lateral-side-standing-neutral-v01.png`｜外侧站立。
  - 提示词版本：`FW-S04-L-P2`；内置 ImageGen 精确编辑；以已批准 BASE-C03 单脚外侧无鞋结构图为编辑目标，只穿上 S04 一字带踝带 15 mm 微方跟凉鞋，并允许脚踝做适配低跟所需的极轻微跖屈；完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock 与 plantar-view anatomy lock。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-standing-neutral-foot-closeup-v01.png`（编辑目标，锁定单脚外侧三分之四解剖、肉色 30D 材质、构图、光照和背景）；由 `visuals/shoe-single-band-ankle-strap-15mm-low-block-heel-sandal-multiview-v01.png` 裁出的严格外侧单视角临时图（只锁定方圆头、一字带、细踝带、外侧扣具、斜向后跟支撑、收腰鞋床和独立 15 mm 微方跟，未作为正式资产保存）。
  - 生成与 QA：2026-09-02；原生输出 899 × 1748 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；单脚恰好五趾，五枚隔袜酒红甲油位于可见背侧甲板，趾端由连续 30D 微织袜膜覆盖，趾间仅保留短浅过渡且无袜头横线；小腿—踝带上下—脚背—趾端材质连续，站立脚踝平顺无可数褶皱；脚跟居中落于独立微方跟，前掌、一字带、踝带、外侧扣具、斜向支撑、收腰鞋床与低跟侧面层次成立。
  - 尝试记录：`P1` 在输出阶段被安全系统误判拦截，未生成或保存候选；`P2` 改为非性感的服装工程与鞋履适配技术图表述后通过。
  - 使用边界：单脚外侧三分之四结构特写，不承担双脚站姿、正面十趾或纯足底参考；脚趾背侧甲板因外侧透视存在自然遮挡。
- [x] `FW-S04-Q`｜`visuals/hosiery-nude-30d-velvet-matte-plain-single-band-ankle-strap-15mm-low-block-heel-sandal-lateral-side-half-squat-v01.png`｜侧面半蹲。
  - 提示词版本：`FW-S04-Q-P1`；内置 ImageGen 精确编辑；以已批准 FW-S02-Q 为编辑目标，只把窄带平底拖鞋替换为 S04 一字带踝带 15 mm 微方跟凉鞋，并做适配低跟所需的极轻微足踝调整；完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock 与 plantar-view anatomy lock。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-narrow-band-flat-home-slide-lateral-side-half-squat-v01.png`（编辑目标，锁定严格侧面半蹲、单侧腿完整可见、远侧腿遮挡、肉色 30D 材质、受力、构图、光照和背景）；`visuals/hosiery-nude-30d-velvet-matte-plain-single-band-ankle-strap-15mm-low-block-heel-sandal-lateral-side-standing-neutral-v01.png`（只锁定 S04 方圆头、一字带、细踝带、外侧扣具、斜向后跟支撑、收腰鞋床、独立 15 mm 微方跟及穿鞋后的连续袜面）。
  - 生成与 QA：2026-09-02；原生输出 1024 × 1536 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；近侧单腿严格侧面半蹲，远侧腿完全遮挡，膝前、膝窝、前后踝、跟腱与脚背均平顺，无可数织物横纹或厚重堆叠；单脚恰好五趾，五枚隔袜酒红甲油可辨，趾端 30D 微织袜膜连续且无袜头横线；脚跟居中落于独立微方跟，前掌底与跟块同时着地，一字带、踝带、外侧扣具、斜向支撑和收腰鞋床完整。
  - 尝试记录：`P1` 首轮通过，无失败候选。
  - 使用边界：侧面单腿半蹲受力模板，不承担双脚站姿、正面十趾或足底参考；脚趾背侧甲板受严格侧面透视自然压缩。

P0 完成条件：现保留的 17 项全部通过后，才开始 P1。若同一鞋型连续三次无法通过袜头结构验收，应先修正参考和构图，不继续批量生成其他角度。

---

## P1｜常用外出鞋型

### S06｜圆润尖头单带露趾 5 cm 细跟穆勒鞋

浅粉色、圆润尖头式鞋床前端轮廓、露趾、前掌只有一根鞋面带；鞋面带中央较细、向左右两端逐渐变宽并连接鞋底。大面积露出脚背，后跟完全开放且没有后跟带或踝带，搭配约 5 cm 细跟。露趾口必须足够完整，使丝袜覆盖、趾间张力曲面和隔袜甲油能够验收。

- [x] `FW-S06-M`｜`visuals/shoe-rounded-point-open-toe-single-band-5cm-slim-heel-mule-multiview-v01.png`｜无脚产品多视角鞋型母版。
  - 提示词版本：`FW-S06-M-P1`；内置 ImageGen 生成；沿用既有 2 × 2 鞋型母版的高位三分之四、严格外侧、低位正面和大底四视角布局，重建为浅粉色圆润尖头式鞋床、前掌单带中央收窄并向两端加宽、开放脚背与后跟、4–5 mm 前掌底和约 5 cm 细跟；本项无脚、无女主、无丝袜，因此不加入脚趾硬锁。
  - 输入参考：`visuals/shoe-single-band-ankle-strap-15mm-low-block-heel-sandal-multiview-v01.png`（只锁定 2 × 2 布局、四个机位、中性浅灰背景、柔和布光和同一只右脚鞋的跨视角一致性；其方圆头、一字带、踝带、后跟支撑和 15 mm 微方跟均不作为鞋型约束）。
  - 生成与 QA：2026-09-03；原生输出 1402 × 1122 PNG；用户按整体视觉效果指定采用首轮 P1，鞋跟依据成图比例登记为约 5 cm；四格保持同一只右脚穆勒鞋，圆润收尖的前端轮廓、单条前掌带中央窄而两端渐宽、大面积开放脚背、完整露趾口、全开放后跟、薄前掌底、自然上扬鞋床与独立约 5 cm 细跟一致；大底视角显示连续前掌纹路、收腰轮廓与小型后跟落地片，无人物、脚、丝袜、品牌或文字。
  - 尝试记录：`P1` 的整体比例与视觉效果由用户确认并设为正式版本；`P2` 曾将跟高压低至约 15–20 mm，`P3` 曾回调至约 30 mm，二者均不再采用且未入库。
  - 使用边界：多格总览只供人工检查鞋型一致性；后续穿着适配生成前，应裁出与目标机位对应的单一视角，不直接提交整张多格图作为正向参考。
- [x] `FW-S06-F`｜`visuals/hosiery-nude-30d-velvet-matte-plain-rounded-point-open-toe-single-band-5cm-slim-heel-mule-front-standing-neutral-v01.png`｜正面站立。
  - 提示词版本：`FW-S06-F-P3`；内置 ImageGen 精确编辑；以已批准 BASE-C01 为编辑目标，为双脚穿上 S06 圆润尖头单带露趾约 5 cm 细跟穆勒鞋并调整为相应跖屈站姿；P2、P3 仅重建鞋带前方趾端，最终采用 P3 在保留十趾和十枚甲油的同时缩短深纵沟；完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock 与 plantar-view anatomy lock。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-front-standing-neutral-toe-closeup-v01.png`（初始编辑目标，锁定正面膝下比例、双脚十趾解剖、肉色 30D 材质、光照和背景）；由 `visuals/shoe-rounded-point-open-toe-single-band-5cm-slim-heel-mule-multiview-v01.png` 裁出的低位正面单视角临时图（只锁定圆润收尖前端、中央窄两端宽的单带、完整露趾口、开放脚背与浅粉色，未作为正式资产保存）；P3 另引用 `visuals/hosiery-nude-30d-velvet-matte-plain-single-band-ankle-strap-15mm-low-block-heel-sandal-front-standing-neutral-v01.png` 约束清楚五趾与统一跨接袜膜之间的平衡。
  - 生成与 QA：2026-09-03；原生输出 902 × 1743 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；双脚各五趾且十枚隔袜酒红甲油清楚可数，四处趾间分界均止于趾蹼附近并缩短为局部浅过渡，袜头无横线；30D 微织纹从小腿经脚踝、脚背、鞋带下方到趾端连续，跖屈站姿无可数踝部褶皱；双脚居中入鞋，圆润收尖鞋头、单带、完整露趾口、大面积开放脚背、开放后跟、薄前掌底与约 5 cm 细跟成立。
  - 尝试记录：`P1` 鞋型和十趾成立，但右脚前三趾及左脚局部出现向后延伸的深纵沟，未保存；`P2` 消除纵沟时融合过度，部分趾形和甲油不再稳定可数，未保存；`P3` 回到 P1 并只缩短软化八处趾间过渡后通过。
  - 使用边界：正面膝下结构特写，不承担身份或严格侧面跟高参考；细跟在正面机位下自然部分重叠，应由鞋型母版与后续外侧模板补充。
- [x] `FW-S06-T`｜`visuals/hosiery-nude-30d-velvet-matte-plain-rounded-point-open-toe-single-band-5cm-slim-heel-mule-top-three-quarter-standing-neutral-v01.png`｜高位三分之四。
  - 提示词版本：`FW-S06-T-P1`；内置 ImageGen 精确编辑；以已批准 BASE-L02 为编辑目标，为双脚穿上 S06 圆润尖头单带露趾约 5 cm 细跟穆勒鞋并调整为相应跖屈站姿；完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock 与 plantar-view anatomy lock。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-top-three-quarter-standing-neutral-v01.png`（编辑目标，锁定高位三分之四构图、下半身比例、双脚前后错位、肉色 30D 材质、光照和背景）；由 `visuals/shoe-rounded-point-open-toe-single-band-5cm-slim-heel-mule-multiview-v01.png` 裁出的高位三分之四单视角临时图（只锁定圆润收尖前端、中央窄两端宽的单带、开放脚背与后跟、薄前掌底、约 5 cm 细跟和浅粉色，未作为正式资产保存）；`visuals/hosiery-nude-30d-velvet-matte-plain-rounded-point-open-toe-single-band-5cm-slim-heel-mule-front-standing-neutral-v01.png`（只补充 S06 穿着后的袜面、甲油、鞋脚接触与颜色一致性）。
  - 生成与 QA：2026-09-03；原生输出 899 × 1748 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；前后脚各五趾，前脚五枚与后脚五枚可见隔袜酒红甲油均可辨，趾间仅有止于趾蹼附近的短浅过渡且袜头无横线；30D 微织纹从腿部经脚踝、脚背、鞋带下方到趾端连续，跖屈站姿无可数踝部褶皱；双脚居中入鞋，圆润收尖鞋头、中央窄两端宽单带、开放脚背与后跟、薄前掌底和约 5 cm 细跟成立。
  - 尝试记录：`P1` 首轮通过，无失败候选。
  - 使用边界：高位三分之四下半身模板，不承担身份、正面十趾等距对比或严格侧面跟高参考；后脚受透视缩小但五枚背侧甲油仍可辨。
- [ ] `FW-S06-L`｜`hosiery-nude-30d-velvet-matte-plain-rounded-point-open-toe-single-band-5cm-slim-heel-mule-lateral-side-standing-neutral-v01.png`｜外侧站立。

### S07｜一字带高跟凉鞋

裸粉或暖灰色、前掌一条平直简洁的一字带、细踝带、露趾、细高跟。用于锁定极简鞋带遮挡下的脚背连续性、高跟站姿及前掌受力；具体跟高在生成鞋型母版前确认。

- [ ] `FW-S07-M`｜`shoe-single-band-high-heel-sandal-multiview-v01.png`｜无脚产品多视角鞋型母版。
- [ ] `FW-S07-F`｜`hosiery-nude-30d-velvet-matte-plain-single-band-high-heel-sandal-front-standing-neutral-v01.png`｜正面站立。
- [ ] `FW-S07-T`｜`hosiery-nude-30d-velvet-matte-plain-single-band-high-heel-sandal-top-three-quarter-standing-neutral-v01.png`｜高位三分之四。
- [ ] `FW-S07-L`｜`hosiery-nude-30d-velvet-matte-plain-single-band-high-heel-sandal-lateral-side-standing-neutral-v01.png`｜外侧站立。

### S08｜多细带高跟凉鞋

黑色或深灰色、多条细带、踝带、细高跟。属于高复杂度鞋型；细带不得切断袜面或被误画为皮肤分界。

- [ ] `FW-S08-M`｜`shoe-strappy-high-heel-sandal-multiview-v01.png`｜无脚产品多视角鞋型母版。
- [ ] `FW-S08-F`｜`hosiery-nude-30d-velvet-matte-plain-strappy-high-heel-sandal-front-standing-neutral-v01.png`｜正面站立。
- [ ] `FW-S08-T`｜`hosiery-nude-30d-velvet-matte-plain-strappy-high-heel-sandal-top-three-quarter-standing-neutral-v01.png`｜高位三分之四。
- [ ] `FW-S08-L`｜`hosiery-nude-30d-velvet-matte-plain-strappy-high-heel-sandal-lateral-side-standing-neutral-v01.png`｜外侧站立。

---

## P2｜高风险与低频鞋型

### S09｜露趾坡跟凉鞋

暖米色、前掌露趾、踝带、连续坡跟。鞋底与袜头前缘必须保持清楚分离，不能把坡跟边缘误生成袜头横线。

- [ ] `FW-S09-M`｜`shoe-open-toe-wedge-sandal-multiview-v01.png`｜无脚产品多视角鞋型母版。
- [ ] `FW-S09-F`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-wedge-sandal-front-standing-neutral-v01.png`｜正面站立。
- [ ] `FW-S09-T`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-wedge-sandal-top-three-quarter-standing-neutral-v01.png`｜高位三分之四。
- [ ] `FW-S09-L`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-wedge-sandal-lateral-side-standing-neutral-v01.png`｜外侧站立。

### S10｜夹趾平底凉鞋

低饱和浅粉色、平底、夹趾柱。该鞋型与“袜面不陷入趾缝”的结构存在天然冲突，只有明确剧情需求时才生成。

- [!] `FW-S10-M`｜`shoe-toe-post-flat-sandal-multiview-v01.png`｜无脚产品多视角鞋型母版；可先建立鞋型。
- [!] `FW-S10-F`｜`hosiery-nude-30d-velvet-matte-plain-toe-post-flat-sandal-front-standing-neutral-v01.png`｜正面站立；生成前先确认夹趾柱与连续袜面的物理方案。
- [!] `FW-S10-T`｜`hosiery-nude-30d-velvet-matte-plain-toe-post-flat-sandal-top-three-quarter-standing-neutral-v01.png`｜高位三分之四。
- [!] `FW-S10-L`｜`hosiery-nude-30d-velvet-matte-plain-toe-post-flat-sandal-lateral-side-standing-neutral-v01.png`｜外侧站立。

S10 不得通过让丝袜陷入趾缝、开孔或变成五指袜来适配夹趾柱。在物理方案确认前保持 `[!]`，不进入正式生成队列。

---

## P3｜姿势和受力扩展

P0–P2 的站立结构通过后，再补以下鞋型专属姿势：

- [ ] `FW-S06-Q`｜`hosiery-nude-30d-velvet-matte-plain-rounded-point-open-toe-single-band-5cm-slim-heel-mule-lateral-side-half-squat-v01.png`｜圆润尖头单带露趾 5 cm 细跟穆勒鞋侧面半蹲。
- [ ] `FW-S07-Q`｜`hosiery-nude-30d-velvet-matte-plain-single-band-high-heel-sandal-lateral-side-half-squat-v01.png`｜一字带高跟凉鞋侧面半蹲。
- [ ] `FW-S07-H`｜`hosiery-nude-30d-velvet-matte-plain-single-band-high-heel-sandal-lateral-side-heel-lift-v01.png`｜一字带高跟凉鞋侧面提踵/前掌受力。
- [ ] `FW-S08-Q`｜`hosiery-nude-30d-velvet-matte-plain-strappy-high-heel-sandal-lateral-side-half-squat-v01.png`｜多细带高跟凉鞋侧面半蹲。
- [ ] `FW-S08-H`｜`hosiery-nude-30d-velvet-matte-plain-strappy-high-heel-sandal-lateral-side-heel-lift-v01.png`｜多细带高跟凉鞋侧面提踵/前掌受力。
- [ ] `FW-S09-Q`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-wedge-sandal-lateral-side-half-squat-v01.png`｜露趾坡跟凉鞋侧面半蹲。
- [ ] `FW-S01-U`｜`hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-sole-raised-heel-v01.png`｜宽面居家拖鞋脚跟轻抬，显示脚趾下方与足底袜面连续性。

## 材质兼容性扩展

以上鞋型全部先以肉色 30D 天鹅绒哑光完成结构验证。后续只有在实际服装需要时，才增加其他丝袜组合，不为每双鞋机械复制全部材质矩阵。

建议首批兼容性测试：

- [!] `FW-MAT-01`｜`hosiery-white-15d-pearl-plain-single-band-ankle-strap-15mm-low-block-heel-sandal-top-three-quarter-standing-neutral-v01.png`｜S04 一字带踝带 15 mm 微方跟凉鞋 × 白色 15D 珠光；等待材质中性硬锁。
- [!] `FW-MAT-03`｜`hosiery-nude-15d-oil-gloss-plain-single-band-high-heel-sandal-top-three-quarter-standing-neutral-v01.png`｜S07 一字带高跟凉鞋 × 肉色 15D 油亮；等待材质中性硬锁。
- [!] `FW-MAT-04`｜`hosiery-black-50d-velvet-matte-plain-strappy-high-heel-sandal-top-three-quarter-standing-neutral-v01.png`｜S08 多细带高跟凉鞋 × 黑色 50D 天鹅绒哑光；等待材质与甲油可见性规则。
- [!] `FW-MAT-05`｜`hosiery-black-80d-wool-plain-rounded-point-open-toe-single-band-5cm-slim-heel-mule-top-three-quarter-standing-neutral-v01.png`｜当前露趾规则下不生成；原则上改配闭趾鞋。

每项兼容性测试至少生成高位三分之四视角；通过后再按实际镜头补正面、侧面或姿势图。

## 单项生成流程

1. 确认前置鞋型母版和丝袜结构母版已为正式资产。
2. 在本文件对应条目下记录提示词版本、输入参考和生成参数；不再为每张图建立同名说明文件。
3. 只提交女主身份、当前鞋型母版、目标丝袜材质和最接近的结构/姿势参考。
4. 生成后按丝袜 QA、鞋脚解剖和鞋型一致性逐项验收。
5. 失败结果记录失败类别，不覆盖已有正式版本。
6. 通过后保存到 `visuals/`、更新本文件状态，并在 `README.md` 的正式资产索引登记。

## 单项完成定义

一项只有同时满足以下条件才可以标记 `[x]`：

- 目标鞋型、颜色、鞋底和鞋跟结构正确。
- 脚处于正确穿鞋位置，鞋与身体连续，无空鞋和多余鞋。
- 完整袜面覆盖全部可见脚趾，具有可读的趾间张力曲面。
- 无裸趾、五指袜、袜头缝合线或连接线。
- 暗红甲油只隔着袜面朦胧透出。
- 脚踝、脚背、脚趾及可见足底的丝袜密度和材质一致。
- 对应姿势中的褶皱和高光符合 30D 天鹅绒哑光材质。
- 文件名、提示词版本、输入参考、版本号和 README 正式索引登记完整。
