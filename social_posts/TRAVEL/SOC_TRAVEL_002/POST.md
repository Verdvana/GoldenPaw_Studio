# SOC_TRAVEL_002 — 邮轮漫游

- post_id: `SOC_TRAVEL_002`
- series_id: `TRAVEL`
- asset_level: `L3`
- status: `SHOT_01_GENERATION_BLOCKED_SHOT_02_APPROVED_SHOT_03_GENERATION_BLOCKED_SAFETY_SHOT_04_CAND_06_REVIEW_REQUIRED_HOSIERY`
- content_pillar: `TRAVEL_DIARY`
- format: `CAROUSEL`
- image_count: `5`
- primary_platform: social feed
- primary_aspect_ratio/resolution: `4:5 / 2160x2700 px delivery target`
- approval_status: `DESIGN_REVIEW_REQUIRED`

## Concept

女主在邮轮上游玩的一组五张社交照片，依 `1.jpg` 至 `5.jpg` 顺序对应五个镜头。穿搭沿用已批准的 `OWNER_CASUAL_SUMMER_01`，发型使用 `HAIRSTYLE_B`。参考图只定义逐张登记的姿势、表情、机位和构图；人物长相、头发、衣着均由女主已批准资产定义。背景细节允许自然变化，但五张须呈现同一艘邮轮、同一天、同一摄影设备与一致的色调和曝光风格。

## Approved wardrobe and hair authorities

- outfit_id: `OWNER_CASUAL_SUMMER_01`
- outfit_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/OUTFIT.md`
- use its approved clothing, footwear and hosiery construction; do not use its wearer identity, face, body, hair, pose, lighting or background as generation authority.
- hairstyle: `HAIRSTYLE_B`
- use the applicable approved scoped Hairstyle B reference for hair attributes only; do not use it to define face, body, skin, clothing, pose, lighting or background.

## Shot-specific footwear and hosiery

- Image 02: owner wears no shoes; the approved white mule pair is casually/messily set on the deck floor near the chair.
- Images 03–04: hosiery-covered bare feet; shoes are entirely outside the frame.
- Image 05: wear the approved white mule heels and include the complete full body from head through both shoes, with safe margin below the feet.
- All five images: continuous light-nude sheer hosiery through legs, ankles, heels, insteps and toes; show natural fabric tension between toes where visible, with the red-burgundy toenail polish softened beneath the fabric. Do not paint polish on top of hosiery.
- Hosiery references are scoped per shot. For image 02, `OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001` defines only intertoe fabric tension and softly diffused burgundy nails under sheer cloth; its gray hue is excluded. The target light-nude color comes from the approved outfit contract.

## Reference intake

See `references/REFERENCE_INTAKE.md`. The five references have been reviewed and cataloged with checksums and scoped responsibilities. Follow them in numeric order. Their visible people are not identity, body, hair or wardrobe references.

## Generation and approval gates

- Resolve the smallest applicable approved reference set after intake.
- Use one consistent camera/look specification, daylight range, white balance, contrast, color treatment, and cruise-ship context across all five images; vary framing and viewpoint only as required by each reference.
- For any image showing the owner's face, use the applicable source-derived L0 Face method as the sole face-generation authority. AI Face/Body Canons and generated candidates are QA comparison only, never generation inputs.
- Every future generation record must separately list `generation_inputs` and `qa_comparison_only`.
- Create complete per-image `REFERENCE_PLAN.md`, `PROMPT_ASSEMBLY.md`, generation record and QA before any image generation.
- Each image requires its own review; no L3 image becomes L1 Canon without explicit user instruction “设为 Canon” or equivalent.
