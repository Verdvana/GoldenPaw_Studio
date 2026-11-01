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
- worn_validation_status: `APPROVED_BY_USER` (v015; previous approvals remain historical)
- approved_design_reference: `approved/design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v003.png`
- approved_worn_views: [approved/worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v015.png]
- approved_worn_front: `approved/worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v015.png`
- worn_front_approval_date: 2026-10-31
- worn_front_approval_evidence: “可以 批准，后面再用这套服装，就按照生成这张图的丝袜质感来生成”
- worn_front_sha256: e9d59c10a5a269c5aeeab777bc19f65fc041d9dab54642c8a175b34cdc199b25
- created_date: 2026-10-30
- design_source: user text request in this conversation, 2026-10-30
- generation_status: `COMPLETE`; v015 approved and moved to approved/worn_front
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
| 贴身内层 | `OWNER_DATE_SUMMER_01_TIGHTS` | 高腰、白色半透明连裤丝袜，闭趾连续结构 | 白色；半透明织物；具体 D 数未核实；光泽严格参考 HOS_USER_SELECTED_WHITE_STRICT | 腰头在肚脐以上，接近上衣下摆；连续覆盖腹部、腰臀、双腿、脚跟、脚背与脚趾 |
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

- hosiery_material_id: `OWNER_DATE_SUMMER_01_TIGHTS` (outfit-local construction ID; material appearance: HOS_USER_SELECTED_WHITE_STRICT)
- denier/color/finish: 白色、半透明；表面光泽与透肤效果严格遵循 HOS_USER_SELECTED_WHITE_STRICT，具体 D 数未核实
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

当前服装生成输入为已批准的常规圆领/中腰 v003 clothing-only 设计图；丝袜材质由 HOS_USER_SELECTED_WHITE_STRICT 独立定义，优先于旧设计/试穿图中的袜料表现。
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

Current approved fitting image is v015. User explicitly adopts its hosiery appearance for later uses of this outfit. Follow HOSIERY_APPEARANCE_METHOD_v015.md. The full portrait remains QA-only for face/body/likeness; only the registered face-excluded material derivative may define hosiery appearance. Approval is L2 and does not redefine Face, Body, Hair or skin Canon. Use independent character sources and scoped clothing/material references; never use earlier rejected fitting pixels.

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

## White hosiery revision — 2026-10-31

用户授权修改两张套装资产以参考最新白袜质感。建立 `candidates/v004_design_reference` 与 `candidates/v006_worn_front` 两个独立待审修订；旧设计 v003、试穿 v005 的批准及原图保持历史有效，新候选不自动取代它们。两张均强制使用 `HOS_USER_SELECTED_WHITE_STRICT` 的去脸材质裁切，材质呈乳白、半透明、平滑织物及柔和方向性光泽，准确 D 数未知。服装结构及真实高腰袜边的可见关系保留。试穿从 L0 脸/肤裁切、Hair-A、去脸 Body 与独立服装/材质参考构建，既有试穿仅做生成后 QA。

- 2026-10-31: 用户授权两张白袜材质修订；generation records and prompts created before generation. Review required.

### Revision execution result — 2026-10-31

- `v004_design_reference`: returned one 1024×1536 PNG; white material sheen improved, but product QA failed for a ghost navel and retained toe band. REVIEW_REQUIRED, not approved, not downstream input.
- `v005_design_reference`: independent correction prepared from approved v003 + strict L0 material crop; service connection failed, no output.
- `v006_worn_front`: five scoped inputs prepared; three service requests failed to connect, no output. First six-input preflight also rejected by the tool maximum-five-path constraint before generation.
- Both requested revisions remain incomplete. Existing approved v003 design and v005 worn files were not modified. Prompts, checksums, exact input responsibilities and failure records are retained for continuation.

### Explicit retry outcome — 2026-10-31

用户“重试”：`candidates/v005_design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v005.png` 成功生成，乳白半透明及柔和方向性光泽已应用，旧脚尖横带与肚脐状阴影已移除，初步 QA PASS，状态 REVIEW_REQUIRED，未批准替换。`v006_worn_front` 本轮原五参考、缩小传输文件、单张分区参考板三次调用均连接失败，无图。两张修订任务尚未整体完成；当前批准设计 v003/试穿 v005 不变。精确提示词、输入/派生来源与失败记录已保存。

### Worn generation outcome — 2026-10-31

用户“生成试穿图”：`candidates/v007_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v007.png` 成功生成 1086×1448 正面试穿候选；脸型/下颌较批准 QA 目标偏窄且有轻微微笑，白袜方向性光泽不足、脚趾织物柔化不足，初步 QA FAIL_FACE_DRIFT_AND_MATERIAL，禁止下游使用，未批准替换。v008 从相同原始分区参考独立修正，未使用 v007 图像，两次调用均因连接错误未返回图像。设计候选 v005 及旧批准设计 v003/试穿 v005 保持原状。

### Current user correction — 2026-10-31, v009

用户明确要求按女主现有正面资产的生成方式重做长相、白袜严格参考重新上传照片、小腿笔直。当前候选 v009 使用已核对的原始 B 脸肤裁切 + L0 Hair-A 遮脸输入、去脸 Body、批准服装 v003、新白袜材质裁切；对 B 的生成来源如实声明，按本次明确方法指令登记候选范围例外，不全局修改 L0-only 规则，不使用批准 Face/旧试穿或失败候选像素。膝—胫骨—踝保持自然近共线、双轴平行，无 O/X 型腿与过伸。新上传照片与已有原图 SHA-256 一致，不重复保存。生成与批准分离。

- 2026-10-31: v009 原始 B 脸肤配方五参考调用成功，1086×1448，候选文件 `candidates/v009_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v009.png`。初步观察脸部更接近原批准方法、白袜乳白半透明及纵向柔和光泽增强、双腿正面自然近直轴。精确长相/小腿直度与脚趾袜面细节仍由用户审核；REVIEW_REQUIRED，未自动替换旧批准试穿。

### v010 user corrections — 2026-10-31

用户仅接受 v009 长相，明确拒绝短裤上方多余白带、油水感高光、小腿弯曲及脚趾裸足刷白/无袜面张力。v009 整体 QA FAIL，不晋升。v010 保持原始成功脸肤配方，独立从五项原始参考重建；仅上方真实高腰袜头保留，下方腹部直入牛仔腰头不出现第二白带；袜面采用干燥细织物、宽柔低对比光泽；膝心—胫轴—踝心竖直平行、膝踝间距一致；闭趾为整前掌单一织物包络，趾间浅 V 张力谷而非裸趾深缝。新候选待审，不使用 v009 像素。

### Four-point correction execution — 2026-10-31

- v010: lower band/oily response improved, calf/toe issues remain, overall FAIL.
- v011: scoped body/garment input isolation attempted; actual upper high waistband disappeared, overall FAIL. Never downstream input.
- v012: isolated garment v2 preserves only true upper waistband while masking lower band/old hosiery geometry. Result retains true high waist, removes lower extra band and suppresses liquid-like highlights; wider bilateral stance improves ankle placement. Calf straightness and whole-toe textile tension remain insufficient, overall FAIL_UNRESOLVED_CALF_TOE_DETAIL, REVIEW_REQUIRED. Exact likeness remains user review although original accepted face recipe was retained.
- All are independently constructed from scoped original-source references, not one another. None approved, promoted, used as downstream source or substituted for existing approved files. Source/crop/mask provenance, actual checksums, prompts and QA recorded.

### v013 user correction — 2026-10-31

用户指出肚脐不清楚、袜面仍偏离上传图、脚趾覆盖与趾间张力不足。独立候选 v013 保留原成功脸部配方及去污染身体/服装参考，改用同一 L0 的宽下半身材质裁切（无缩放/重绘）以保留白色半透明丝感、腿弯及脚部的原始整体响应。肚脐必须透过连续腹部薄织物可读，不裸露、不画点；取消“全哑光/极低光泽”的过度压制，保留干燥丝线光泽而非油水感；脚趾为一个整前掌织物包络及趾间浅 V 张力桥。候选仍待审，不使用任何失败试穿像素。

- 2026-10-31: v013 单张生成成功，1086×1448，肚脐透过丝袜可读、白色半透明丝感较 v012 恢复；脚趾整层织物包覆/张力桥和小腿直度仍不足，整体 FAIL_UNRESOLVED_TOE_TENSION_AND_CALF_ALIGNMENT / REVIEW_REQUIRED。不声称材质完全匹配，不批准替换，不作为后续输入。

### v014 redo — 2026-10-31

用户接受 v013 腿上袜料方向，拒绝脚踝以下硅胶感、趾间无织物覆盖/张力和小腿不直。v014 独立原始来源重建：白袜原图仍管白色/透明度/光泽，补充登记 L0 袜脚近裁切仅管覆盖和织物张力；原始脸肤+发型以无缩放双区板合并输入保留参考额度。脚部需细织纹/屈曲处微褶而非光滑胶壳；小腿需轴线及内外侧直线自然收束，不仅是站姿加宽。肚脐透袜可见与上方真实高腰袜边保留。全部待审，无失败图输入。

### Foot detail diagnostic gate — 2026-10-31

v014 独立五参考重做仍未充分解决脚部织物覆盖/张力和小腿直度。按现有 Asset package gate“仅在有具体未解决问题时增加…材质/结构细节”，建立单张 `v001_foot_material_detail`，以两个既有 L0 材质来源直接验证脚趾袜面包络、趾间张力桥和脚踝微褶。白袜原图仍唯一控制颜色/透明度/光泽，补充图只管覆盖；无任何 AI 失败候选输入。细节图待用户审核，在审核前不得作为后续全身图参考；不替代未完成全身修正，也不自动批准。

- 2026-10-31: v014 全身重做未能解决脚趾织物包覆和小腿弯曲，QA FAIL，未批准。按具体未解决问题细节 gate 生成 FOOT_MATERIAL_DETAIL v001，1312×1199 原生PNG，初步可读到连续细织纹覆于甲面/趾面、趾间浅谷张力与脚踝微褶，未见明显平滑胶壳。颜色/光泽/透明度及精确结构仍待用户审核。该细节图不自动作为下游输入，不晋升 L1；全身修正仍未完成。

### Ankle-only material-detail correction — 2026-10-31

用户接受 FOOT_MATERIAL_DETAIL v001 除脚腕褶皱以外的效果。批准范围记录于候选 USER_REVIEW_SCOPED.md，不晋升 Canon。v002 作为该已审 L2 细节的局部编辑，仅去除双脚踝横向褶皱/堆积，袜面应平整拉伸且细织纹保留；已接受的趾间 V 张力谷、脚趾/甲面连续包覆、袜色/透明度等保持。原始白袜 L0 裁切同时作为材质一致性参考。新版本仍待审，不自动替换或作为下游。全身图及小腿直度任务仍未完成。

- 2026-10-31: FOOT_MATERIAL_DETAIL v002 局部编辑成功（1312×1199），初步检查双脚踝横褶/堆积已移除，细织纹、趾间张力谷和脚趾包覆保持。新图 REVIEW_REQUIRED，不自动晋升或替换；全身脚部整合/小腿直度任务尚未完成。

### Foot detail approved / full-body v015 — 2026-10-31

用户“脚部ok，批准，请生成全身试穿图”明确批准 FOOT_MATERIAL_DETAIL v002，原图移动至 `outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/foot_material_detail/OWNER_DATE_SUMMER_01_FOOT_MATERIAL_DETAIL_v002.png`，唯一文件 SHA-256 `02718418b7a55bd1fc44023ca5059b88b4dc5a42738f8c918458ce4a48178897`。批准仅为 L2 脚部袜面包覆/张力/织纹/无褶脚踝，不晋升 L1、不定义脚部身份/解剖或姿势。候选目录保留来源、原路径校验和、QA 与批准记录。v015 全身候选使用该批准细节及独立原始人物/服装/白袜输入，关注小腿直度和肚脐高腰层次；全身图不自动批准替换。

- 2026-10-31: v015 全身试穿使用已批准脚部 v002 及四项独立人物/服装/白袜参考生成成功，1086×1448，候选保存于 candidates/v015_worn_front。初步 QA 仍见小腿/踝轴不直且站姿不对称，脚趾织物迁移不够清晰，FAIL_INITIAL_LEG_AND_FOOT_INTEGRATION_QA / REVIEW_REQUIRED。脚部 v002 的独立批准继续有效；新全身不自动批准替换。

## Current final approval and future hosiery authority — 2026-10-31

用户已明确批准全身 v015，并要求“后面再用这套服装，就按照生成这张图的丝袜质感来生成”。当前全身试穿为 v015；以前 agent 初步 QA 作为历史保留，不再视为未解决批准门槛。后续本套装必须遵循 `HOSIERY_APPEARANCE_METHOD_v015.md`：v015 为丝袜最终外观目标，原始白袜 L0 与已批准 Foot v002 保留材质职责；需要像素迁移 v015 质感时只用登记的确定性去脸腰到脚材质裁切，不得继承脸、身体/小腿解剖、姿势或其他身份属性。不改变其他套装或全局 L1 Canon。
