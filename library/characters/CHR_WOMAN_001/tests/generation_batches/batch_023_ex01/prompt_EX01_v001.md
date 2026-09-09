# EX01 v001｜实际成功生成规格

## 输入职责

- `face/candidates/CHR_WOMAN_001_ID01_HAIR_A_v004.png`：编辑目标及最高优先级的已批准身份、发型 A、服装、构图和灯光母版。
- 本次未输入其他图片；仅改变局部表情肌肉状态。

## 实际成功提示词

```text
Use case: identity-preserve
Asset type: CHR_WOMAN_001 EX01 natural closed-mouth smile expression continuity candidate
Input image: Image 1 is the edit target and the highest-priority locked production identity/composition master, approved ID01 v004.
Primary request: Change only the facial expression from neutral to a subtle, warm, natural closed-mouth smile. The smile should be small and restrained: both mouth corners rise gently by a few millimeters, lips remain together with no teeth visible, cheeks lift only slightly, and the lower eyelids/outer eye corners show a faint natural friendly engagement. It should feel like quiet recognition or a warm response, not posing for a cheerful photograph.
Identity invariants: preserve exactly the same adult Chinese woman, 26-year-old presentation, face width, cheek volume, jaw, chin, eye shape and spacing, irises, brows, nose, philtrum, lip volume, facial asymmetry, skin tone, natural makeup and skin texture. Do not beautify, reshape, de-age, enlarge the eyes, narrow the jaw, or alter the nose or lips beyond the tiny muscle movement required for the smile.
Composition and body invariants: preserve the exact frontal camera angle, portrait perspective, crop, scale, head position, gaze direction, upright neck, relaxed level shoulders, torso, arms, and posture from Image 1.
Hair and wardrobe invariants: preserve hairstyle A exactly—same part, front strands, volume, length, silhouette and hair color. Preserve the same plain medium-pink sleeveless continuity garment exactly, including neckline, straps, opacity, smooth matte material and body fit. No jewelry or accessories.
Background and lighting invariants: preserve the identical warm-neutral gray studio background, soft large-source lighting, fill, white balance, exposure, shadows, color fields and photorealistic finish.
Constraints: edit only the localized facial expression muscles around the mouth, cheeks and eye corners. Everything else must remain visually unchanged. Exactly one woman and one view.
Avoid: open mouth, visible teeth, broad grin, laughter, exaggerated cheek lift, squinting, asymmetric smirk, pursed lips, surprised eyes, head tilt, pose change, face reshaping, identity drift, hairstyle change, garment change, background change, new objects, text, watermark, border, collage, plastic skin or blotchy texture.
```
