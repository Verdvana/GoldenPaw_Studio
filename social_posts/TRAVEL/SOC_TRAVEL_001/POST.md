# SOC_TRAVEL_001 — 南京秋日慢游

- post_id: SOC_TRAVEL_001
- series_id: TRAVEL
- asset_level: L3
- status: PLANNED
- content_pillar: MICRO_STORY
- format: CAROUSEL
- image_count: 4
- primary_platform: social feed
- primary_aspect_ratio/resolution: 4:5 / 2160x2700 px delivery target
- camera_language: third-person candid photography, Sony α7C II look
- approval_status: DESIGN_REVIEW_REQUIRED

## Story

一个秋天的南京半日散步：从梧桐街道出发，走到城墙边，再穿过有生活气的老街，最后在秦淮水岸收尾。四张图都由同行者在场外拍摄，不使用自拍、镜面自拍或“旅游打卡站姿”；人物是城市漫游中的自然主体，南京通过梧桐、砖墙、城墙与水岸层层出现。

四张图独立生成。允许的连续性只有同一半日、同一套秋季休闲穿搭、同一条散步路线、包和纸袋的有限出现，以及动作和光线从午后到傍晚的自然推进。上一张不能定义下一张的人脸、身体、发型、服装材质、固定道具或地点建筑身份。

## Image list

| Image asset ID | Intended framing/action | Location responsibility | Aspect ratio | Status |
|---|---|---|---|---|
| SOC_TRAVEL_001_IMG_01 | 同行者在梧桐树影下从三分之二后侧拍摄；人物自然向前行走，头部仅保留轻微侧脸轮廓，视线看向街道前方；全身与连续梧桐街道同框 | 南京秋季梧桐街区，生活化街道，不出现可读店名 | 4:5 | REVIEW_REQUIRED |
| SOC_TRAVEL_001_IMG_02 | 从斜前方三分之四视角拍人物停在明城墙边，抬头观察砖墙，一只手轻触墙面；人物占画面中下部，城墙砖面和秋色树冠形成纵深 | 南京明城墙步道的真实历史感，但不依赖可读景区牌匾 | 4:5 | APPROVED_L3 |
| SOC_TRAVEL_001_IMG_03 | 新街口步行街夜晚第三人称抓拍；人物蹲下抚摸街边奶牛猫，一条腿正常蹲下，另一条腿膝盖接近地面、前脚掌着地；人物露齿笑并看向猫 | 南京新街口步行街夜景，步行街灯光和城市人流，不出现可读品牌或广告 | 4:5 | APPROVED_L3 |
| SOC_TRAVEL_001_IMG_04 | 傍晚秦淮水岸的中远景背影；人物靠近栏杆看水，画面留出水面、树影和暖色倒影，人物不需要露脸；加入直闪抓拍效果 | 秦淮水岸的水面与晚秋傍晚氛围，不出现可读游船广告或地标文字 | 4:5 | APPROVED_L3 |

## Outfit continuity

- outfit_id: `OWNER_CASUAL_AUTUMN_01`
- outfit_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01/OUTFIT.md`
- visible contract: white fitted long-sleeve top with high ruffled neckline and upper lace yoke; black mini skirt with layered ruffles and lace trim; silver-gray subtly sparkling sheer pantyhose; gunmetal/silver Mary Jane flats
- optional temporary layer: plain warm-gray or muted camel short wool coat, worn open in images 01–03 and loosely carried or worn in image 04 only if needed for the cooler dusk; the coat is post-specific L2 dressing, not a new Canon
- hairstyle: HAIRSTYLE_A wherever hair is visible; no blending with HAIRSTYLE_B
- hosiery: one continuous sheer textile garment from waist/hips through legs, heels, insteps and toes; soft realistic hosiery sheen, never latex/PVC/plastic/body paint

## Camera and visual language

- camera: Sony α7C II, natural handheld third-person still-photography language
- suggested lens language: compact normal-to-short-telephoto perspective, approximately 35–50 mm equivalent; no ultra-wide distortion
- depth: subject readable against the city, with restrained background separation rather than heavy portrait blur
- light progression: clear late-afternoon daylight in images 01–02, softer warm low sun in image 03, blue-hour/warm practical mix in image 04
- photographer position: 2–6 m from subject, usually eye level or slightly below; no visible photographer, camera overlay, fake UI or watermark
- aesthetic: candid travel diary, quiet and lightly cinematic, not fashion editorial, not tourism-board postcard, not staged influencer pose

## Platform and crop contract

- all images: 4:5 vertical, central safe area; no essential face, hands, hem, hosiery, shoes, paper bag or railing detail in the outer 5%
- image 01: preserve full silhouette, walking direction and enough plane-tree canopy/street context
- image 02: preserve both the walking figure and the recognizable masonry texture; do not crop feet or turn the wall into an abstract texture
- image 03: preserve the 3/4 side action, paper bag and old-street depth; no readable shop text
- image 04: preserve the figure-to-water relationship and dusk reflection; keep the back of head and shoulders anatomically coherent
- no readable brand, store name, tourist sign, route number, map, QR code, watermark, fake UI or garbled text

## Face-safe generation rule

For any image where the owner's face is visible, use the applicable L0-derived Face method as the sole face-generation authority. Do not use an AI Face Canon, AI Body Canon or generated candidate as a generation input. Approved AI Canon images may appear only in `qa_comparison_only` for post-generation identity and contamination checks. Any body reference must be a deterministic face-excluded derivative with explicit provenance and exclusions.

## Temporary asset brief

See `TEMPORARY_ASSET_BRIEF.md`. These are post-specific L2/L3 design responsibilities only and do not create Canon.

## Shot design

See `SHOT_DESIGN.md` for the per-image pose, expression, background layering, light direction and camera placement.

## Explicit generation gate

- image 01 gate: approved by user on 2026-09-20 with evidence “应该是04登记吧”; active candidate CAND_04
- image 01 scope: approved L3 post image only; not Canon and not authorized as a downstream visual generation input
- image 02 gate: approved by user on 2026-09-20 with evidence “不错 批准。”; active candidate CAND_03
- image 02 scope: approved L3 post image only; not Canon and not authorized as a downstream visual generation input
- images 02–04 gate: still pending separate user approval before generation
