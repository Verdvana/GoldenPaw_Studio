# Batch 001｜ID01 与 ID02

日期：2026-09-05  
工具：Codex 内置 `image_gen`  
状态：v001 已完成用户首轮审核并停止下游使用；保留用于与 v002 比较，没有文件进入 `approved/`。

## ID01

- 任务：正面中性半身母版，发型 A。
- 输出：`face/candidates/CHR_WOMAN_001_ID01_HAIR_A_v001.png`
- 尺寸：1024×1536 PNG。
- 真人参考及职责：
  - `source_photos/DSC01015.JPG`：主身份与发型 A。
  - `source_photos/DSC00847.jpg`：三分之四面部结构补充。
  - `source_photos/DSC00079.JPG`：肩、躯干和腰部体积补充。
- 连裤袜商品图：未使用；半身图不承担腿脚材质验证。
- 初检：单人、正面、闭口、无配饰、粉色一件式测试泳衣、中性背景和柔光成立；未见明显随机色块。身份和体型仍须用户决定是否通过。

### ID01 最终提示词

```text
Use case: photorealistic-natural
Asset type: CHR_WOMAN_001 ID01 front-facing neutral half-body identity master for a live-action cinematic AI drama
Primary request: Generate one new, highly photorealistic studio reference photograph of the authorized adult Chinese woman shown in the input photos. Preserve her recognizable real facial identity, natural face shape, facial proportions, eye shape and spacing, nose, lips, jaw, skin tone, realistic skin texture, shoulder width and natural body volume. She is 26 years old and 168 cm tall by character specification. Do not beautify or reinterpret her.
Input images: Image 1 is the primary identity and required Hair A reference; Image 2 supplements the same person's three-quarter facial structure and must not replace Image 1 identity; Image 3 supplements natural shoulder, torso, waist and body-volume proportions only, while its pose, outfit and environment must not be copied.
Subject: one adult woman only, standing upright, square to camera, shoulders relaxed, arms hanging naturally outside the crop, direct gaze, closed mouth, neutral calm expression. Required Hair A: long dark brown-black hair worn down, natural side-to-near-center part and natural volume, matching Image 1's hair length and silhouette; no hairstyle redesign.
Wardrobe: simple pink high-cut one-piece body-test swimsuit, opaque, non-sheer, modest photographic presentation, no padding that enlarges the bust, no corsetry, no waist shaping, no logos. The lower body and feet are outside this half-body crop; do not invent shoes or hosiery detail in view.
Scene/backdrop: seamless neutral warm-gray studio backdrop with no set, props, text or visible equipment.
Style/medium: live-action photorealistic cinematic reference photography, natural pores and small real skin variations, not illustration, not glamour retouching.
Composition/framing: vertical single image, eye-level camera, medium telephoto portrait perspective around 70–85mm equivalent, centered symmetrical front view, crop from just above the head to upper hip, generous safe margin around hair and shoulders, no grids or multi-panel layout.
Lighting/mood: large diffused neutral key light, soft controlled fill, stable neutral white balance, gentle film-quality modeling, smooth continuous tonal gradients with retained three-dimensional facial and body form.
Color palette: faithful neutral skin color, restrained natural pink swimsuit, neutral warm-gray background.
Constraints: preserve real asymmetry; natural minimal everyday makeup only; no earrings, necklace, watch, hair accessory, jewelry or tattoo invention; correct adult anatomy; no text, logo, watermark or border.
Avoid: face slimming, larger eyes, pointed chin, smaller nose, altered mouth, age change, body slimming, waist compression, breast enlargement, leg-length alteration, artificial porcelain skin, beauty filter, heavy makeup, glamour pose, sexualized pose, cleavage emphasis, colored rim light, hard spotlight, heavy LUT, vignette, film grain, over-sharpening, banding, mottled patches, checkerboard artifacts, random discoloration, inconsistent skin blocks.
```

## ID02

- 任务：正面自然站立全身母版，发型 A。
- 输出：`body/candidates/CHR_WOMAN_001_ID02_HAIR_A_v001.png`
- 尺寸：1024×1536 PNG。
- 身份参考：ID01 v001。
- 真人比例参考：`source_photos/DSC00079.JPG`、`source_photos/IMG_4971.jpeg`；后者通过未修饰的 PNG 工作副本输入。
- 商品图：最终成功调用未使用。第一次包含 `15d_nude_matte/IMG_2550.JPG` 的调用因 MPO 输入格式失败；转换格式后的调用又在输出阶段被安全系统拦截，均未产生候选图。成功调用删去商品图及不必要的足趾特写语言，将袜尖细节留给 FT01／鞋袜验证任务。
- 初检：正面完整全身、发型 A、粉色泳衣、无鞋和包脚肉色连裤袜成立；未见明显随机色块。脸部相似度、身体胖瘦与头身比例、泳衣剪裁及袜面是否足够可见，须由用户审核。当前全身分辨率不足以批准精确趾端张力。

### ID02 最终成功提示词

```text
Use case: photorealistic-natural
Asset type: CHR_WOMAN_001 ID02 neutral full-body continuity reference for a live-action cinematic AI drama
Primary request: Create one realistic, professional studio continuity photograph of the same authorized adult Chinese woman. Preserve the recognizable facial identity, natural asymmetry, Hair A, skin tone and realistic body build established by Image 1 and the real-person proportion references. She is 26 years old and 168 cm tall by character specification. This is a neutral production reference, not a fashion or glamour image.
Input images: Image 1 is the face, skin and Hair A anchor. Images 2 and 3 show the same real adult and are used only to preserve her natural shoulder, torso, waist, hip, arm, leg and overall proportions; do not copy their clothing, pose, footwear, objects or environment.
Subject and pose: one adult woman only, standing upright and directly front-facing, natural balanced posture, feet parallel about hip-width apart, arms resting at her sides, hands visible, direct gaze, closed mouth, calm neutral expression.
Hair: match Image 1's long dark brown-black worn-down hair, natural part, length and silhouette.
Wardrobe: a plain opaque pink high-leg one-piece athletic swim garment used only as a body-proportion test layer, with conservative upper-body coverage, no padding, corsetry, shapewear, transparent panels, logos or decorative details. Under it she wears one continuous pair of nude, lightly translucent, matte velvet-look closed-foot pantyhose. The pantyhose waistband and seams remain hidden under the garment. She wears no shoes; both feet remain completely covered by the same hosiery, with smooth continuous fabric from legs through ankles and feet. Any red toenail polish is only very subtly perceived beneath the hosiery and is not emphasized.
Scene/backdrop: seamless neutral warm-gray studio cyclorama and matte neutral floor, with no props, furniture, text or visible equipment.
Style/medium: live-action photorealistic reference photography with natural skin texture, accurate adult anatomy and fine even textile texture; not illustration and not beauty-retouched advertising.
Composition/framing: single vertical image, centered straight-on full figure from above the hair to below both covered feet, generous safe margin, realistic 70–85mm equivalent perspective, level camera near mid-torso height to minimize distortion, no grid and no multi-panel layout.
Lighting/mood: broad diffused neutral key light with restrained soft fill, stable neutral white balance, gentle film-quality modeling and smooth continuous tonal gradients across skin, pink fabric, legs and feet.
Color palette: faithful neutral skin, restrained natural pink garment, neutral nude semi-sheer matte hosiery and warm-gray background.
Constraints: keep Image 1 face unchanged; preserve the real person's natural body volume from Images 2 and 3; no slimming, leg lengthening or waist reshaping; correct hands, feet and limb count; natural minimal everyday makeup; no earrings, necklace, watch, jewelry, hair accessory, tattoos, text, logo, watermark or border.
Avoid: glamour posing, sexualized presentation, cleavage emphasis, enlarged bust, tiny waist, fashion-model proportions, altered face, larger eyes, pointed chin, porcelain skin, heavy makeup, footwear, bare legs, bare feet, bare toes, open-foot hosiery, visible waistband, sagging fabric, random wrinkles, colored rim light, hard spotlight, strong LUT, color cast, vignette, grain, over-sharpening, banding, checkerboard blocks, mottled patches and discontinuous color or texture.
```

## 审核闸门

- 两张都是候选，不等于身份／体型母版已批准。
- 用户须分别判断：脸像不像本人、发型 A 是否准确、身体胖瘦与比例是否准确、泳衣剪裁是否合适、袜面是否满足基础层级。
- 未获批准前，不用这两张生成 FC、BD、HA 等下游资产。
