# CHR_CAT_001 固定资产扩展提示词 v001

本文件记录 2026-09-04 使用内置图像生成工具制作第二批固定资产时采用的提示词结构。每一张图均单独生成，没有使用一张多格图冒充多个稳定资产。

## 通用身份锁定

```text
Use case: identity-preserve
Input images: approved production identity references of the same fictional five-year-old male golden-shaded British Shorthair.
Preserve the exact same broad circular face, full cheeks, large gray-green eyes with dark rims, dusty-pink nose, cream muzzle/chin/throat/chest, warm golden-apricot coat, restrained darker-golden forehead and back shading, compact broad chubby adult body, short sturdy legs, round natural paws, and thick golden tail with a softly transitioning warm brown-gold tip.
High-end photorealistic animal studio photography, real feline anatomy, natural plush short fur, neutral daylight-balanced soft studio lighting, seamless neutral light-gray studio.
No collar, clothes, devices, props, text, labels or watermark. Avoid face drift, kitten proportions, humanized anatomy, extra limbs, merged paws, pure-black tail tip, orange-tabby color, illustration, cartoon or CGI sheen.
```

## 面部近景变量

所有面部近景保持相同裁切、焦段、相机高度、光线和中性闭嘴表情，每次只替换角度：

```text
FRONT: exact centered straight-on face, both eyes equally sized.
FRONT-LEFT THREE-QUARTER: approximately 45 degrees toward camera-left, both eyes visible.
FRONT-RIGHT THREE-QUARTER: approximately 45 degrees toward camera-right, both eyes visible.
LEFT PROFILE: exact 90-degree left profile, only the near eye visible.
RIGHT PROFILE: exact 90-degree right profile, only the near eye visible.
```

## 身体细节变量

```text
TOP VIEW: exact perpendicular overhead full-body view, complete silhouette, diagnostic back and spine coat distribution.
TAIL: complete attached tail from rump to rounded tip, thick realistic taper and warm brown-gold tip.
PAWS: coherent close-up of both front paws; claws retracted; one grounded paw and one plausibly lifted paw showing dusty rose-brown pads.
```

## 日常微表情变量

表情只允许通过眼睑、瞳孔、耳位、胡须和极小头部姿态变化，不允许人类眉毛或微笑：

```text
CONTENT_SAFE: relaxed eyelids, neutral relaxed ears and whiskers, quietly peaceful.
SLEEPY: naturally half-lowered eyelids, comfortable and drowsy, not ill.
CURIOUS_ALERT: slightly open eyes, modestly enlarged pupils, forward ears and whiskers.
MILDLY_WORRIED: subtly tense gaze, ears slightly outward, whiskers modestly lowered, no tears.
```

## 基础姿态变量

```text
WALK: exact left profile natural mid-stride feline gait with plausible alternating limbs.
LOAF: front-left three-quarter relaxed loaf, paws naturally tucked and body fully grounded.
GROOM: seated three-quarter pose, one front paw lifted for one small realistic lick, other limbs coherent.
HEAD_SCRATCH: seated three-quarter pose, one rear paw reaches behind the near ear with a visible realistic joint chain.
```

每次实际生成仍需重复完整身份约束，并选择正面母版加最接近目标角度的一至两张辅助图。
