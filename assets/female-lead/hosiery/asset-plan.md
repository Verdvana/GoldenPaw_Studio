# 丝袜视觉模板与露趾鞋适配计划

本文件集中管理丝袜视觉模板与露趾鞋适配清单。每完成一项，只有通过 `qa.md` 验收并在 `README.md` 的正式资产索引登记后，才能把状态改为 `[x]`。正式视觉文件统一放入 `visuals/`。

## 固定生成基准

除单项另有说明外，所有穿着图统一使用：

- 女主已锁定的脚部身份与自然身体比例。
- 肉色 30D、天鹅绒哑光、无花纹、完整包脚连裤丝袜。
- 暗红色甲油只存在于脚趾背侧甲板，并仅在该甲板实际可见时作为袜面下的朦胧酒红色块；足底、前掌、趾腹和脚趾下侧禁止出现甲油色块。
- 袜面从脚踝连续覆盖脚背、全部脚趾和足底。
- 趾间为一整片受横向张力的连续曲面，不陷入趾缝，不逐趾包裹。
- 袜头前缘无可见缝合线、横线、补强带或任何连接线。
- 褶皱按关节受力分区：提踵/跖屈时脚踝前后侧、脚背与跟腱全部贴体张紧且无可见褶皱；下蹲/背屈时只允许脚踝前侧压缩区出现少量细浅横褶，后踝保持拉伸平顺；屈膝时只允许膝窝压缩区出现少量细软褶皱，膝前保持拉伸平顺；禁止任何堆叠、袋状松弛或袜面离体。
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

- [x] `MAT-N15-L01`｜`visuals/hosiery-nude-15d-velvet-matte-plain-none-front-standing-neutral-v01.png`｜肉色 15D 天鹅绒哑光全腿正面模板；用于透肤度、颜色、织物感和腿脚整体连续性。绿色泳装、泳池背景与上肢伸展动作不作为参考职责；脚部较小，不能替代袜头结构特写。

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
- [x] `BASE-C04`｜`visuals/hosiery-nude-30d-velvet-matte-plain-none-sole-heel-lift-v02.png`｜足底结构图｜检查足底、前掌和趾腹连续覆盖。
  - 提示词版本：`BASE-C04-P6`；内置 ImageGen 精确编辑；由已批准 BASE-C03 延续单脚比例与材质，最终采用纯足底抬脚构图；完整逐字加入更新后的 closed-foot toe lock、deep-red toenail visibility lock 与 plantar-view anatomy lock。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-standing-neutral-foot-closeup-v01.png`（初始比例与材质参考）；修复阶段以各前一版候选为单一编辑目标。
  - 生成与 QA：2026-09-01；原生输出 899 × 1750 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；足跟、足弓、前掌、五枚趾腹与趾端织纹连续，纯足底视角无任何甲油色块，趾间为浅弧跨接。
  - 尝试记录：`P1`、`P2` 存在深趾缝或逐趾包裹感；`P3` 虽修正趾间结构，却把甲油错误生成在趾腹，后由用户指出并按 `plantar-polish`、`anatomy`、`reference-conflict` 判定失效。`P4` 修复请求被安全过滤器拒绝；`P5` 清除甲油但重新出现深趾缝；`P6` 同时满足纯足底无甲油和连续浅弧袜面后通过。失效 `P3` 已移至 `rejected/` 隔离。
- [x] `BASE-P01`｜`visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-half-squat-v01.png`｜侧面半蹲｜检查脚踝、膝前和膝窝褶皱。
  - 提示词版本：`BASE-P01-P2`；内置 ImageGen 精确编辑；采用严格侧视、近侧单腿完整可见且远侧腿自然完全遮挡的职责单一构图；完整逐字加入更新后的 closed-foot toe lock、deep-red toenail visibility lock 与 plantar-view anatomy lock。
  - 输入参考：`core/female-lead-body-turnaround-v1.png`（只锁定女主自然身体比例）与 `visuals/hosiery-nude-30d-velvet-matte-plain-none-top-three-quarter-standing-neutral-v01.png`（只锁定肉色 30D 天鹅绒哑光材质）；`P2` 以 `P1` 为唯一编辑目标。
  - 生成与 QA：2026-09-01；原生输出 1024 × 1536 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；大腿—膝—小腿—脚踝—足部比例自然，近侧脚跟完整落地，膝前为张力平滑区、膝窝轻压缩、脚踝只有符合 30D 的细浅褶皱；背侧甲油仅隔袜朦胧可见，足底无甲油色块。
  - 尝试记录：`P1` 的半蹲比例、材质和落跟基本正确，但远侧脚从近侧腿后孤立露出，且袜头趾间分隔偏强，按 `anatomy` 与 `toe-glove` 判定不入库；首次双腿分离修复在输出阶段被安全过滤器拒绝，未产生图片；`P2` 收敛为严格侧视遮挡并修正连续袜面后通过。
- [x] `BASE-P02`｜`visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-heel-lift-v02.png`｜侧面提踵｜检查脚背伸展、前掌受力及后踝贴合张力。
  - 提示词版本：`BASE-P02-P5`；内置 ImageGen 精确编辑；采用严格侧视、近侧单腿完整可见且远侧腿自然完全遮挡的温和日常提踵构图；完整逐字加入更新后的 closed-foot toe lock、deep-red toenail visibility lock、plantar-view anatomy lock 与后踝防松垮约束。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-half-squat-v01.png`（锁定女主自然腿脚比例、肉色 30D 材质与摄影语言）和 `visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-standing-neutral-foot-closeup-v01.png`（仅辅助初始侧面脚型与袜头结构）；最终 `P5` 以 `P4` 为唯一编辑目标，只重建跟腱—后踝袜面。
  - 生成与 QA：2026-09-01；原生输出 1024 × 1536 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；膝部自然微屈、小腿温和发力、脚跟轻度抬升，跖骨头与五趾趾腹形成宽而连续的前掌承重面；跟腱—后踝袜面纵向贴体张紧，无多层横褶、堆叠或松袋感；背侧甲油隔袜朦胧可见，足底及趾腹无甲油色块。
  - 尝试记录：`P1` 脚跟过高、受力集中趾端且脚趾抓地卷曲，按 `anatomy`、`toe-glove` 与 `wrinkle-physics` 判定不入库；`P2` 定向修复在输出阶段被安全过滤器拒绝，未产生图片；`P3` 仍接近足尖动作、趾屈曲且后踝出现过多平行褶皱，后由用户指出并新增 `ankle-slack` 失败类别；`P4` 修正前掌受力后曾入库，现由 `P5` 进一步消除后踝松垮观感并替换。旧 v01 已移至 `rejected/` 隔离。

前置模板全部通过后才开始 S01。其他颜色、厚度、光泽和花纹按实际服装需求逐项增加；硬锁改为材质中性版本前，不启动非肉色、非天鹅绒哑光的露趾模板。

## P0｜当前项目核心鞋型

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
- [x] `FW-S01-Q`｜`visuals/hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-lateral-side-half-squat-v01.png`｜侧面半蹲，检查脚踝、脚背、膝前和膝窝褶皱。
  - 提示词版本：`FW-S01-Q-P1`；内置 ImageGen 精确编辑；以已批准 BASE-P01 为编辑目标，只为严格侧视的近侧脚穿上 S01 宽面薄底零跟居家拖鞋；完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock、plantar-view anatomy lock，并明确半蹲时脚踝前侧与膝窝为少量细浅压缩褶皱区、膝前与跟腱—后踝为平顺张力区。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-none-lateral-side-half-squat-v01.png`（编辑目标，唯一锁定女主自然腿脚比例、半蹲关节角度、严格侧视遮挡、肉色 30D 材质、光照和背景）；`visuals/hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-lateral-side-standing-neutral-v01.png`（辅助参考，只锁定 S01 浅粉宽鞋面、开放后跟、5–6 mm 零跟薄底、正确入鞋位置和已批准袜头结构，不覆盖目标姿势）。
  - 生成与 QA：2026-09-01；原生输出 1024 × 1536 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；半蹲深度、腿脚比例与落跟受力自然，脚跟完整居中于鞋床且鞋底全长贴地；脚踝前侧保留少量细浅横褶，跟腱—后踝平顺无松垮横褶，膝窝轻压缩而膝前平滑；可见趾端由连续袜面覆盖，隔袜酒红甲油只位于真实可见背侧甲板。
  - 尝试记录：`P1` 首轮通过，无失败候选。
- [x] `FW-S01-D`｜`visuals/hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-lateral-side-deep-squat-v01.png`｜侧面全蹲，检查深度屈膝与踝背屈时的受力、脚踝前侧细浅压缩褶皱、膝窝细软压缩褶皱，以及膝前和跟腱—后踝的平顺张力；禁止堆叠褶、袋状松弛或鞋脚错位。
  - 提示词版本：`FW-S01-D-P2`；内置 ImageGen 精确编辑；以已批准 FW-S01-Q 为唯一编辑目标，将半蹲推进为严格侧视、脚跟完全落地的全蹲，并把构图收紧为非叙事性的下肢服装材质技术参考；完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock、plantar-view anatomy lock 和全蹲褶皱分区规则。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-lateral-side-half-squat-v01.png`（编辑目标，锁定女主腿脚比例、肉色 30D 材质、S01 鞋型、袜头结构、光照和背景）；首轮曾加入 `core/female-lead-body-turnaround-v1.png` 只辅助自然身体比例，但输出被安全系统拦截且未产生图片；最终 P2 不再提交该辅助图。
  - 生成与 QA：2026-09-01；原生输出 1024 × 1536 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；全蹲深度清楚，近侧大腿与小腿自然接近，膝关节与踝背屈处于同一受力链；脚跟完整居中落在鞋床，鞋底全长贴地；前踝有少量细浅压缩纹、膝窝有柔和压缩线，膝前与跟腱—后踝平顺无松垮堆褶；可见趾端连续包袜，甲油只在真实可见背侧甲板下方朦胧透出。
  - 尝试记录：`P1` 在输出阶段被安全系统误判拦截，未产生图片；`P2` 改为大腿中段至完整脚部的中性下肢技术构图并移除多余躯干描述后通过。

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
- [ ] `FW-S02-T`｜`hosiery-nude-30d-velvet-matte-plain-narrow-band-flat-home-slide-top-three-quarter-standing-neutral-v01.png`｜高位三分之四。
- [x] `FW-S02-L`｜`visuals/hosiery-nude-30d-velvet-matte-plain-narrow-band-flat-home-slide-lateral-side-standing-neutral-v01.png`｜外侧站立。
  - 提示词版本：`FW-S02-L-P2`；内置 ImageGen 精确编辑；以已批准 FW-S01-L 为编辑目标，只把 S01 宽带浅粉拖鞋改为 S02 浅象牙粉窄带结构，随后对首轮结果局部重建趾间连续薄膜和隔袜甲油扩散；两轮均完整逐字加入 closed-foot toe lock、deep-red toenail visibility lock、plantar-view anatomy lock 与中性站立无褶皱规则。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-lateral-side-standing-neutral-v01.png`（编辑目标，锁定单脚外侧三分之四比例、肉色 30D 材质、脚跟落位、光照和背景）；由 `visuals/shoe-narrow-band-flat-home-slide-multiview-v01.png` 裁出的严格外侧单视角临时图（只锁定浅象牙粉窄带、开放后跟和薄底结构，未作为正式资产保存）；P2 以 P1 为唯一编辑目标。
  - 生成与 QA：2026-09-01；原生输出 927 × 1697 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；窄带覆盖深度约为 S01 宽带的 40–50%，脚背与趾根开放区增加，脚跟居中且薄底全长贴地；中立站姿脚踝、跟腱和脚背平顺无褶皱；可见趾间由连续浅弧袜面跨接，隔袜酒红甲油边缘柔化且足底无甲油色块。
  - 尝试记录：`P1` 鞋型与脚踝贴合正确，但趾间凹陷偏深且甲面高光略像裸甲，按 `toe-glove` 与 `nail-too-sharp` 不入库；`P2` 只重建窄带前方连续袜面与甲油扩散后通过。
- [x] `FW-S02-Q`｜`visuals/hosiery-nude-30d-velvet-matte-plain-narrow-band-flat-home-slide-lateral-side-half-squat-v01.png`｜侧面半蹲。
  - 提示词版本：`FW-S02-Q-P3`；内置 ImageGen 精确编辑；以已批准 FW-S01-Q 为编辑目标，只把宽带鞋型改为 S02 浅象牙粉窄带，继承半蹲比例、关节角度、落跟受力和褶皱分区；后续分别校正窄带覆盖深度和可见背侧甲油；各轮均完整逐字加入三段脚趾/足底硬锁。
  - 输入参考：`visuals/hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-lateral-side-half-squat-v01.png`（编辑目标，唯一锁定半蹲腿脚比例、姿势、肉色 30D 材质、褶皱物理、光照和背景）；`visuals/hosiery-nude-30d-velvet-matte-plain-narrow-band-flat-home-slide-lateral-side-standing-neutral-v01.png`（辅助参考，只锁定 S02 窄带宽度、颜色、开放结构和袜头表现，不覆盖目标姿势）；P3 以 P2 为唯一编辑目标。
  - 生成与 QA：2026-09-01；原生输出 1024 × 1536 PNG；A–F 通过，G 的结构可读性通过但长边低于 2048 px 建议值；半蹲比例与脚跟落地自然，S02 窄带保持 28–35 mm 受控覆盖深度；前踝只有少量细浅压缩纹，跟腱—后踝平顺无松垮横褶，膝窝轻压缩而膝前拉平；可见趾端由连续袜面覆盖，真实可见背侧甲板的酒红甲油隔袜可辨，趾腹与足底无甲油色块。
  - 尝试记录：`P1` 姿势和褶皱正确，但鞋带过细、接近细条带，与 S02-L 不一致；`P2` 修正为 28–35 mm 窄带后，小趾侧可见甲油仍偏淡；`P3` 只增强趾端微织纹和真实可见背侧甲油后通过。

### S03｜双带薄底平底拖鞋

浅粉灰色、两条平行鞋面带、露趾、后跟开放、薄底平底。用于检验袜面经过两段遮挡后的材质连续性。

- [ ] `FW-S03-M`｜`shoe-double-band-flat-slide-multiview-v01.png`｜无脚产品多视角鞋型母版。
- [ ] `FW-S03-F`｜`hosiery-nude-30d-velvet-matte-plain-double-band-flat-slide-front-standing-neutral-v01.png`｜正面站立。
- [ ] `FW-S03-T`｜`hosiery-nude-30d-velvet-matte-plain-double-band-flat-slide-top-three-quarter-standing-neutral-v01.png`｜高位三分之四。
- [ ] `FW-S03-L`｜`hosiery-nude-30d-velvet-matte-plain-double-band-flat-slide-lateral-side-standing-neutral-v01.png`｜外侧站立。
- [ ] `FW-S03-Q`｜`hosiery-nude-30d-velvet-matte-plain-double-band-flat-slide-lateral-side-half-squat-v01.png`｜侧面半蹲。

### S04｜踝带露趾平底凉鞋

低饱和裸粉色，前掌横带、细踝带、露趾、平底。用于锁定鞋带压迫、脚背连续性和踝带上下丝袜材质一致性。

- [ ] `FW-S04-M`｜`shoe-ankle-strap-flat-sandal-multiview-v01.png`｜无脚产品多视角鞋型母版。
- [ ] `FW-S04-F`｜`hosiery-nude-30d-velvet-matte-plain-ankle-strap-flat-sandal-front-standing-neutral-v01.png`｜正面站立。
- [ ] `FW-S04-T`｜`hosiery-nude-30d-velvet-matte-plain-ankle-strap-flat-sandal-top-three-quarter-standing-neutral-v01.png`｜高位三分之四。
- [ ] `FW-S04-L`｜`hosiery-nude-30d-velvet-matte-plain-ankle-strap-flat-sandal-lateral-side-standing-neutral-v01.png`｜外侧站立。
- [ ] `FW-S04-Q`｜`hosiery-nude-30d-velvet-matte-plain-ankle-strap-flat-sandal-lateral-side-half-squat-v01.png`｜侧面半蹲。

P0 完成条件：以上 21 项全部通过后，才开始 P1。若同一鞋型连续三次无法通过袜头结构验收，应先修正参考和构图，不继续批量生成其他角度。

---

## P1｜常用外出鞋型

### S05｜露趾平底穆勒鞋

玫瑰裸色、较完整鞋面、前端露趾、后跟开放、平底。鞋面不得变成居家拖鞋宽带。

- [ ] `FW-S05-M`｜`shoe-open-toe-flat-mule-multiview-v01.png`｜无脚产品多视角鞋型母版。
- [ ] `FW-S05-F`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-flat-mule-front-standing-neutral-v01.png`｜正面站立。
- [ ] `FW-S05-T`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-flat-mule-top-three-quarter-standing-neutral-v01.png`｜高位三分之四。
- [ ] `FW-S05-L`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-flat-mule-lateral-side-standing-neutral-v01.png`｜外侧站立。

### S06｜鱼嘴中跟单鞋

浅粉色、较小鱼嘴开口、包覆式鞋面、中等细跟。开口必须足够大，使丝袜覆盖证据能够验收；不能只露出无法判断材质的几个像素。

- [ ] `FW-S06-M`｜`shoe-peep-toe-mid-heel-pump-multiview-v01.png`｜无脚产品多视角鞋型母版。
- [ ] `FW-S06-F`｜`hosiery-nude-30d-velvet-matte-plain-peep-toe-mid-heel-pump-front-standing-neutral-v01.png`｜正面站立。
- [ ] `FW-S06-T`｜`hosiery-nude-30d-velvet-matte-plain-peep-toe-mid-heel-pump-top-three-quarter-standing-neutral-v01.png`｜高位三分之四。
- [ ] `FW-S06-L`｜`hosiery-nude-30d-velvet-matte-plain-peep-toe-mid-heel-pump-lateral-side-standing-neutral-v01.png`｜外侧站立。

### S07｜露趾粗跟凉鞋

裸粉或暖灰色、前掌横带、踝带、中等粗跟。用于锁定抬高后跟时的脚背伸展和前掌受力。

- [ ] `FW-S07-M`｜`shoe-open-toe-block-heel-sandal-multiview-v01.png`｜无脚产品多视角鞋型母版。
- [ ] `FW-S07-F`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-block-heel-sandal-front-standing-neutral-v01.png`｜正面站立。
- [ ] `FW-S07-T`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-block-heel-sandal-top-three-quarter-standing-neutral-v01.png`｜高位三分之四。
- [ ] `FW-S07-L`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-block-heel-sandal-lateral-side-standing-neutral-v01.png`｜外侧站立。

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

- [ ] `FW-S05-Q`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-flat-mule-lateral-side-half-squat-v01.png`｜露趾平底穆勒鞋侧面半蹲。
- [ ] `FW-S06-Q`｜`hosiery-nude-30d-velvet-matte-plain-peep-toe-mid-heel-pump-lateral-side-half-squat-v01.png`｜鱼嘴中跟鞋侧面半蹲。
- [ ] `FW-S07-Q`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-block-heel-sandal-lateral-side-half-squat-v01.png`｜露趾粗跟凉鞋侧面半蹲。
- [ ] `FW-S07-H`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-block-heel-sandal-lateral-side-heel-lift-v01.png`｜露趾粗跟凉鞋侧面提踵/前掌受力。
- [ ] `FW-S08-Q`｜`hosiery-nude-30d-velvet-matte-plain-strappy-high-heel-sandal-lateral-side-half-squat-v01.png`｜多细带高跟凉鞋侧面半蹲。
- [ ] `FW-S08-H`｜`hosiery-nude-30d-velvet-matte-plain-strappy-high-heel-sandal-lateral-side-heel-lift-v01.png`｜多细带高跟凉鞋侧面提踵/前掌受力。
- [ ] `FW-S09-Q`｜`hosiery-nude-30d-velvet-matte-plain-open-toe-wedge-sandal-lateral-side-half-squat-v01.png`｜露趾坡跟凉鞋侧面半蹲。
- [ ] `FW-S01-U`｜`hosiery-nude-30d-velvet-matte-plain-wide-band-flat-home-slide-sole-raised-heel-v01.png`｜宽面居家拖鞋脚跟轻抬，显示脚趾下方与足底袜面连续性。

## 材质兼容性扩展

以上鞋型全部先以肉色 30D 天鹅绒哑光完成结构验证。后续只有在实际服装需要时，才增加其他丝袜组合，不为每双鞋机械复制全部材质矩阵。

建议首批兼容性测试：

- [!] `FW-MAT-01`｜`hosiery-white-15d-pearl-plain-ankle-strap-flat-sandal-top-three-quarter-standing-neutral-v01.png`｜S04 踝带平底凉鞋 × 白色 15D 珠光；等待材质中性硬锁。
- [!] `FW-MAT-02`｜`hosiery-gray-30d-satin-plain-open-toe-flat-mule-top-three-quarter-standing-neutral-v01.png`｜S05 露趾平底穆勒鞋 × 灰色 30D 缎光；等待材质中性硬锁。
- [!] `FW-MAT-03`｜`hosiery-nude-15d-oil-gloss-plain-open-toe-block-heel-sandal-top-three-quarter-standing-neutral-v01.png`｜S07 粗跟凉鞋 × 肉色 15D 油亮；等待材质中性硬锁。
- [!] `FW-MAT-04`｜`hosiery-black-50d-velvet-matte-plain-strappy-high-heel-sandal-top-three-quarter-standing-neutral-v01.png`｜S08 多细带高跟凉鞋 × 黑色 50D 天鹅绒哑光；等待材质与甲油可见性规则。
- [!] `FW-MAT-05`｜`hosiery-black-80d-wool-plain-peep-toe-mid-heel-pump-top-three-quarter-standing-neutral-v01.png`｜当前露趾规则下不生成；原则上改配闭趾鞋。

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
