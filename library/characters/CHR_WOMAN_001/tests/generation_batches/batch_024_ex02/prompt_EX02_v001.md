# EX02 v001｜实际成功生成规格

## 输入职责

- `face/candidates/CHR_WOMAN_001_ID01_HAIR_A_v004.png`：编辑目标及最高优先级的已批准身份、发型 A、服装、构图、身体与灯光母版。
- `source_photos/DSC01939.JPG`：同一真人的露齿笑肌肉运动、嘴宽、上排牙齿特点及面颊／眼周联动；不迁移侧转角度、坐姿、餐厅暖光、服装或背景。

## 实际成功提示词

```text
Use case: identity-preserve
Asset type: CHR_WOMAN_001 EX02 natural teeth-showing smile expression continuity candidate
Input images: Image 1 is the edit target and highest-priority approved ID01 v004 identity, hair, wardrobe, composition, body, studio and lighting master. Image 2 is an authorized real photograph of the same woman and supplies only her authentic smile mechanics, mouth width, upper-tooth character and cheek/eye response; ignore its three-quarter head angle, seated pose, restaurant lighting, clothing and background.
Primary request: Change only Image 1's facial expression into a natural, friendly, medium-intensity teeth-showing smile recognizable as the woman in Image 2. Her lips part modestly and the upper front teeth are naturally visible; show little or no lower teeth. Keep the mouth opening moderate and the smile warm, not a laugh. The mouth corners lift naturally, cheeks rise, and the lower eyelids and outer eye corners engage gently without closing or shrinking the eyes excessively.
Smile and teeth fidelity: follow Image 2's real mouth width and authentic upper dental arrangement rather than inventing a perfect cosmetic smile. Teeth must be individually plausible, correctly aligned inside the mouth, naturally off-white, normal in size and count, with realistic gums only if minimally visible. Preserve the woman's original lip volume and philtrum; allow only expression-driven stretching.
Identity invariants: preserve Image 1's exact same adult Chinese woman and 26-year-old presentation, face width, cheek volume, jaw, chin, eye shape and spacing, iris size, brows, nose, facial asymmetry, skin tone, natural makeup and skin texture. Do not reshape, beautify further, enlarge eyes, narrow the jaw, sharpen the chin, or alter the nose.
Composition and body invariants: preserve Image 1's exact frontal camera angle, portrait perspective, crop, scale, head position, direct gaze, upright neck, relaxed level shoulders, torso, arms and posture.
Hair and wardrobe invariants: preserve hairstyle A exactly—same part, front strands, volume, length, silhouette and dark-brown color. Preserve the identical plain medium-pink sleeveless continuity garment, neckline, straps, opacity, smooth matte surface and fit. No jewelry or accessories.
Background and lighting invariants: preserve the identical warm-neutral gray studio background, broad soft light, fill, white balance, exposure, shadows, even color fields and photorealistic finish.
Constraints: edit only the localized facial expression around lips, mouth interior, cheeks and eye corners. Everything else remains visually unchanged. Exactly one woman and one view.
Avoid: closed mouth, huge open-mouth laugh, exaggerated grin, excessive gums, perfect uniform veneers, duplicated or fused teeth, too many teeth, bright white teeth, strong squint, eyes closed, surprised expression, asymmetric smirk, head tilt, pose change, identity drift, face reshaping, hairstyle or garment change, background change, text, watermark, border, collage, plastic or blotchy skin.
```
