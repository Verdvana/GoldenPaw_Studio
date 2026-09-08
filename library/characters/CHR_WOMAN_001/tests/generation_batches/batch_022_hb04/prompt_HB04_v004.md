# HB04 v004｜用户选定的本轮第二次生成规格

## 输入职责

- `DSC01015.JPG`：真人身份及头肩比例。
- `IMG_6123_input_working.png`：授权近景原照的无损格式副本，优先约束真实眼形、眼距、面颊、鼻唇、下颌和自然左右差异。
- `DSC01595.JPG`：自然脸型与发型 B 收发状态补充；不复制夜景光线、服装和背景。
- `DSC01276.JPG`：发型 B 的窄分缝、头顶体积、向后收发和碎发。
- `截屏2026-09-05 下午3.40.21.png`：仅提供既定年轻化影视呈现与克制眼妆；不迁移婚礼发型、耳饰、笑容、滤镜或面部重塑。
- 未输入任何 AI 生成图。

## 实际成功提示词

```text
Use case: photorealistic-natural
Asset type: production hairstyle continuity reference, CHR_WOMAN_001 HB04 fresh regeneration
Primary request: Create a new, highly realistic studio head-and-shoulders reference of the same Chinese woman from the authorized real photos only. This image is specifically a LIGHT HIGH-ANGLE CROWN VIEW for hairstyle B, not a straight-on ID portrait. The visible crown structure is the main technical purpose, while her real identity remains accurate.

Input images: Image 1 is primary real identity and body/shoulder evidence; ignore smile, loose hair, jacket and sunlight. Image 2 is strongest close facial evidence for her true almond eye shape and spacing, rounded broad cheeks, nose, lips, jaw, chin and asymmetry; remove green cast and phone distortion. Image 3 reinforces the same real face and the hair gathered up; ignore lighting, hoodie and background. Image 4 defines hairstyle B's near-center separation, upward/backward root direction, modest crown lift and sparse temple strands; ignore pose, expression, clothes and garden. Image 5 guides only youthful polished presentation and restrained eyeliner; do not copy wedding styling, earrings, smile, veil, smoothing or facial reshaping.

Identity invariants: unmistakably the woman in Images 1–4; about 26 in presentation. Preserve her real eye size, almond shape and spacing, broad softly rounded cheek structure, real nose bridge and rounded tip, philtrum, lips, jaw and chin. Do not beautify into a generic model, enlarge eyes or irises, make a V-shaped jaw, sharpen chin, lengthen nose, or change ethnicity. Calm closed mouth, neutral expression, subtle natural base, restrained brow, hairline-thin eyeliner, mild lashes, muted pink lips, realistic clean skin.

Hairstyle B: dark brown-black hair. Narrow soft near-center part from front hairline across the crown. Roots flow outward then distinctly upward and backward into gathered hair, with modest rounded lift and realistic grouped strands. All lengths are secured off the shoulders into one compact vertical folded/twisted updo at the middle back of the head by one dark translucent brown tortoiseshell claw clip at mid-occiput. Because this is a frontal elevated view, the clip and updo remain behind the crown silhouette: hidden, with at most a tiny plausible side edge. No bun above crown, no topknot, no ponytail, no long loose hair.

Critical camera geometry: vertical portrait, normal 70–85mm-equivalent perspective. The woman stands upright with level shoulders and level head—she does NOT bend, bow, hunch, or lower her chin. Place the camera physically about 25–30 cm above her eye line and tilt it downward about 16–18 degrees. She lifts only her eyes to meet the raised lens. This must visibly reveal a continuous oval area of crown surface behind the front hairline: the part and backward root flow occupy roughly the upper third of the head. The forehead and face show gentle high-angle foreshortening, but remain natural and recognizable. Her shoulders stay horizontal. Crop from clear space above the crown through shoulders and just below the scoop neckline. The face must not fill the frame like a passport photo.

Garment: exactly one plain medium-pink conservative sleeveless continuity top, fully opaque, smooth fine matte stretch surface, medium-width symmetric straps, modest rounded scoop neckline. No ribs, knit weave, zipper, bust seams, logo, jewelry, earrings or accessories.

Studio: seamless warm gray-beige background, broad soft neutral cinematic key, gentle fill, even white balance and color fields.

Constraints: exactly one woman and one view. Only these supplied real photographs may influence the generation. Prior generated images are not inputs. Crown readability and real-person identity are equally mandatory.

Avoid: straight-on eye-level passport framing, head bowed toward camera, hunched torso, extreme overhead shot, tiny eyes, oversized eyes, generic glamorous face, narrow V jaw, topknot, visible bun or claw clip above crown, wide scalp gap, radial cowlick, flat oily hair, loose shoulder hair, wedding elements, earrings, hands, text, watermark, collage, border, plastic or blotchy skin.
```
