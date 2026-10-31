# Outfit Design — 夏季约会套装 01

- outfit_id: `OWNER_DATE_SUMMER_01`
- display_name: 夏季约会套装01
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- episode/scene scope: reusable owner date outfit / summer
- character_outfit_root: `outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01`
- status: `DESIGN_REFERENCE_AND_WORN_FRONT_APPROVED`
- asset_purpose: reusable L2 outfit package
- design_reference_status: `APPROVED` (v003 broad shallow round neckline)
- worn_validation_status: `APPROVED_BY_USER` (v005; prior v004 remains rejected)
- approved_design_reference: `approved/design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v003.png`
- approved_worn_views: [approved/worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v005.png]
- approved_worn_front: `approved/worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v005.png`
- worn_front_approval_date: 2026-10-30
- worn_front_approval_evidence: “这就对了，批准”
- worn_front_sha256: b93f96f8d354cf3aa1b434ee19d9acd90777937c1bf1471611f0cd798710b801
- created_date: 2026-10-30
- design_source: user text request in this conversation, 2026-10-30
- generation_status: `COMPLETE`; v005 approved and moved to approved/worn_front
- current_design_candidate: null (v003 moved on approval)

## Design direction

夏季约会穿搭：长袖、常规圆领的轻薄纱质短上衣，下摆止于胸下，露出腹部区域；
搭配常规中腰牛仔短裤、白色半透明高腰连裤丝袜和高跟细跟露趾凉鞋。
最重要的视觉关系是“上衣短、短裤常规腰位、丝袜腰更高”：丝袜腰头必须明显高出短裤，
覆盖肚脐以上，向上接近短上衣下摆。露腹指腹部不被上衣或短裤遮住，
并不表示整段腹部裸露；腹部大部分应能看到白色半透明丝袜覆盖。

## Garment inventory and layering

| Layer | Asset/material ID | Construction | Color / finish | Coverage |
|---|---|---|---|---|
| 上衣 | `OWNER_DATE_SUMMER_01_TOP` | 长袖、常规圆领、纱质短上衣；下摆止于胸下 | 白色；轻薄纱织物，胸前不透明内衬 | 胸部与手臂；下摆以下露出腹部区域 |
| 贴身内层 | `OWNER_DATE_SUMMER_01_TIGHTS` | 高腰、白色半透明连裤丝袜，闭趾连续结构 | 白色；半透明织物；具体 D 数与光泽待定 | 腰头在肚脐以上，接近上衣下摆；连续覆盖腹部、腰臀、双腿、脚跟、脚背与脚趾 |
| 外层下装 | `OWNER_DATE_SUMMER_01_SHORTS` | 常规中腰牛仔短裤，穿在丝袜外面 | 浅蓝水洗牛仔，翻边裤脚 | 常规中腰位置，约在肚脐附近，覆盖腰臀与大腿上部 |
| 鞋履 | `OWNER_DATE_SUMMER_01_SANDALS` | 高跟、细跟、露趾凉鞋 | 银色细带（踝带及趾带）；细高跟，精确高度未测量 | 鞋带位于丝袜外；露趾口内仍有丝袜完整包覆 |

## Silhouette and fit

### Validation targets

- 肩颈与胸口：常规圆领位于颈根下方，胸前不透明完整覆盖；保留长袖，不使用低胸、深领、杯型胸衣或胸口透视结构。
- 上衣长度：下摆明确位于胸下，不延长至肚脐或塞进短裤。
- 高度关系（从上到下）：胸下短上衣下摆 → 接近其高度的丝袜腰头 → 远低于丝袜腰头的常规中腰短裤腰头（肚脐附近）。
- 丝袜腰头：明显高出短裤，绝非只露出一条窄边；肚脐以上仍有白色半透明织物覆盖。
- 露腹效果：短上衣与常规中腰短裤之间形成明显腹部区域，丝袜是该区域的实际覆盖层；
  上衣下摆与丝袜腰头接近但不要求相接，具体间距留待设计审核。
- 腰臀张力：丝袜高腰结构独立于短裤；短裤采用普通中腰和正常前裆长度，不再采用低腰；也不抬至丝袜的超高腰线，丝袜不得被压低到短裤腰线。
- 材质：纱质上衣与牛仔短裤保持各自织物特性；丝袜从高腰到足部保持同一套白色半透明材质逻辑。
- 鞋袜关系：凉鞋必须高跟、细跟、露趾；脚趾透过丝袜自然可见，不能出现裸趾或开趾丝袜。

## Hosiery and footwear contract

- hosiery_material_id: `OWNER_DATE_SUMMER_01_TIGHTS` (outfit-local design ID; no material image approved)
- denier/color/finish: 白色、半透明；具体 D 数与表面光泽未指定，不能擅自记为已批准
- waistband/panel notes: 高腰覆盖肚脐以上并接近胸下上衣；腹部可见区保留半透明效果，不自动加入不透明控制裤腹片、蕾丝宽腰封或束腰结构
- toe construction: 闭趾、连续织物包覆；露趾凉鞋不改变丝袜闭趾结构
- footwear: 已批准图示银色细带踝带露趾细高跟凉鞋；设计约 9 cm，实际跟高未测量
- continuous coverage required: yes — 高腰/腹部 → 腰臀 → 大腿 → 膝 → 小腿 → 脚踝 → 脚跟 → 脚背 → 脚趾
- burgundy toenail polish: 保留既有稳定外观属性；仅在白色半透明织物下自然透出时可见，不涂在袜面或强行增强
- QA authority: `docs/qa/hosiery_material_rules.md`

## Asset package and approval gate

- 本轮为 v003 常规圆领修订的单张 clothing-only 设计图；不自动生成试穿或自动批准。
- 设计图需能读清短上衣、丝袜高腰与常规中腰短裤的层次和高度；不含人物、脸或人体身份信息。
- `worn_front` 为后续头部完整入画的试穿验证，需检查腹部层次、腰线、织物透明度与鞋袜关系。
- 仅在有具体未解决问题时增加 `worn_3q`、背面或材质/结构细节；不批量生成。
- 每次生成前使用 `templates/outfit/GENERATION_RECORD.md`，分别记录 `generation_inputs` 与 `qa_comparison_only`。
- 设计 v001 已由用户批准并移动；生成记录位于 `candidates/v001_design_reference/generation_record.md`；批准仅限 L2 设计，不得晋升为 L1。

## Reference responsibilities and exclusions

当前服装生成输入为已批准的常规中腰 v002 设计图；原低腰 v001 仅保留为 v002 编辑来源的历史证据。无独立批准材质图。
后续先从 `registries/reference_sets.yaml` 与最近的 `REFERENCE_GUIDE.md` 解析所需参考；
本套装不直接沿用其他套装的袜料、鞋型或生成图。

- 服装/材质参考仅定义本套指定的轮廓、结构、颜色、层次、透明度与鞋袜关系。
- `must_not_define`: owner face, body geometry/proportions, skin, hair, identity, pose, lighting, background, photography style.
- 所有 `worn_*` 仅用于试穿 QA，不作为后续生成输入、身份谱系或视频关键帧参考。
- 试穿中可见脸部仅由适用的 L0 真人输入及 source-derived Face 方法生成；
  AI Face Canon、AI Body Canon、既有套装/镜头/候选不得作为脸部生成输入。
- Body 输入必须为有来源与校验和的确定性去脸衍生参考；AI Face Canon 仅限生成后比较 QA，
  检查身份漂移与脸部污染，不进入生成视觉输入。

## Approved styling and remaining precision

白色浅圆领不透明胸前片、长纱袖与收口、浅蓝水洗翻边短裤、图示白色半透明高腰丝袜及银色细带露趾细跟鞋已随设计 v003 与试穿 v005 批准。丝袜具体 D 数、精确腰头宽度及鞋跟实测高度未建立数值规格，不从图像推断为已批准数字。
这些细节不能削弱已明确的长袖常规圆领胸下短上衣、常规中腰短裤、白色半透明高腰丝袜及细高跟露趾凉鞋要求。

## Current revision scope

用户于 2026-10-30 要求短裤改为“正常的”，解释为常规中腰、正常前裆、常规短裤裤长；丝袜腰头仍远高于短裤并接近上衣。原 v001 设计批准仅适用于历史低腰方案。v002 已由用户“好 继续生成”明确批准；其首次试穿 v003 未返回图片。

## Normal-neck revision

用户要求上衣不再低胸，改正常款；本次具体化为常规圆领（颈根下方）、胸前完整不透明内衬，去掉杯型胸衣与低胸结构。保留胸下短款下摆、长袖纱质、常规中腰短裤、高腰白色半透明丝袜及银色细高跟凉鞋。新图待用户审核，不修改已批准的历史 v002 图像。

## Approved worn-front usage

Current approved fitting image is v005. Approval is scoped to this L2 outfit and its front fit/appearance; it does not redefine Face, Body, Hair or skin Canon. The raster is validation-only and must not be supplied as any future generation input, identity lineage or video keyframe. Use independent master/source assets and approved clothing-only design v003 for later authorized generation.

## Change log

- 2026-10-30: 根据用户要求新建夏季约会套装文字设计，登记为 L2 DRAFT，未生成图片。
- 2026-10-30: 用户授权开始；v001 暂用白色纱上衣（低心形领、胸部内衬）、浅蓝水洗短裤、银色细带约 9 cm 细高跟凉鞋及柔和微光丝袜作为待审核方案。具体 D 数仍未指定；这些候选细节不视为用户批准。

- 2026-10-30: 完成单张 v001 clothing-only 设计图与初步 QA；状态 REVIEW_REQUIRED，未批准、未生成试穿。

- 2026-10-30: 用户“可以 继续”批准 v001 设计；原图移动至 approved/design_reference，授权单张正面试穿候选。

- 2026-10-30: 单张正面试穿 v001 请求被服务输出阶段安全审核拦截，无图片返回；试穿未完成，设计批准继续有效。

- 2026-10-30: 用户“重新来”授权原提示词、原五项输入重试；worn-front v002 再次被服务输出阶段安全审核拦截，未返回图片。试穿仍未完成。

- 2026-10-30: 用户要求取消低腰短裤，改普通常规中腰牛仔短裤，保留丝袜腰头远高于短裤；创建单张 v002 clothing-only 设计修订，未更改历史批准文件。

- 2026-10-30: v002 常规中腰短裤设计候选生成完成；前裆与裤腿较 v001 加长，丝袜腰头仍远高于短裤。已做设计 QA，待用户审核；未生成试穿。

- 2026-10-30: 用户“好 继续生成”批准 v002 常规中腰设计，图像原样移动到 approved/design_reference 的 v002 路径；授权单张 worn-front v003。

- 2026-10-30: 常规中腰 v002 的首次正面试穿 v003 被服务输出阶段安全审核拦截；无图像返回，未做视觉 QA，未批准试穿。无法确定拦截具体原因。

- 2026-10-30: 用户要求上衣取消低胸，改常规领口。建立 v003 常规圆领/完整胸前内衬设计候选，其他衣物及高低腰线关系保留。

- 2026-10-30: v003 已生成，低胸杯型结构改为较宽浅圆领及完整不透明胸前片；实际不是贴颈圆领，具体领口由用户审核。其他衣物与腰线关系保留，未生成试穿。

- 2026-10-30: 用户“可以，继续试试”批准 v003 实际浅圆领设计，原图移动至 approved/design_reference 的 v003 路径；授权单张 worn-front v004。

- 2026-10-30: worn-front v004 成功返回并保存；服装腰线层次可见，但生成后对照 Face Canon 的五官关系偏移，整体 QA 标记 REJECTED。不得作为下游参考，未批准试穿。

- 2026-10-30: 用户要求参考已登记正脸资产生产方式。核对 FACE_01 v011 原始记录后，本次 v005 按用户当前指示使用原 B_FACE_SKIN_CONTEXT_NO_CROWN 脸肤裁切和 A 发型遮脸参考，不再替换为另一套 L0 脸肤裁切。此 B 裁切源为生成的 B 外观资产，不伪称 L0；仅此候选的方法选择例外，不更改全局规则。Body 仍去脸，服装仍 v003；禁止输入 v004 或批准 Face Canon。

- 2026-10-30: v005 按登记 Face 方法成功生成；脸部初步比较较 v004 接近目标，无明显斑块污染。精确相似度、发顶/分缝及脚趾袜面细节待用户审核，状态 REVIEW_REQUIRED，未批准或晋升。

- 2026-10-30: 用户“这就对了，批准”明确批准 worn-front v005；唯一图像原样移动到 approved/worn_front，候选目录仅留生成/QA/提示词与原路径校验和。套装登记 DESIGN_REFERENCE_AND_WORN_FRONT_APPROVED，批准仅为 L2，未晋升 L1。

## User clarification — visible true high waistband, 2026-10-30

用户明确要求高腰丝袜的真实袜边露在短上衣下摆下方，不能向上深入上衣而完全不可见。上衣下摆与真实高腰袜头之间应保留可读的小间距，真实袜边独立可见；其下腹部仍为连续白色半透明织物，不能另加中腹或短裤上沿的第二条横带。不建立精确间距/腰头宽度数值，不修改已批准图像。当前社媒第二张须从原始登记参考独立重生成，不得编辑此前社媒 AI 图。
