# SOC_OUTFIT_003 — 商场试鞋的一下午

- post_id: `SOC_OUTFIT_003`
- series_id: `OUTFIT_DETAIL`
- asset_level: L3
- status: DRAFT
- content_pillar: `OUTFIT_DETAIL`
- format: `CAROUSEL`
- image_count: 3
- primary_platform: social feed (draft)
- primary_aspect_ratio/resolution: portrait; image-specific crop/output ratio recorded per image
- requested_publish_window: null
- approval_status: REVIEW_REQUIRED
- generation_gate: AUTHORIZED_FOR_IMG_01_AND_IMG_02_ONLY_BY_USER_ON_2026-10-20

## Everyday moment

周末在商场逛鞋，试穿几双后挑中一双。轮播记录进店挑款、试穿看效果、拿着鞋盒准备离开的三个自然片段。地点为一次性、无品牌标识的公共商场鞋店，不建立固定环境 Canon。

## Image list

| Image asset ID | Candidate ID | Intended framing/action | Aspect ratio | Status |
|---|---|---|---|---|
| `SOC_OUTFIT_003_IMG_01` | `SOC_OUTFIT_003_IMG_01_CAND_01` | 使用 `IMG_9103.HEIC`：商场试鞋镜前弯腰查看鞋履的全身记录；背面为主、镜中保留小幅正面倒影，浅色连裤袜和鞋完整可见 | 9:16 source framing | CANDIDATE_GENERATED; REVIEW_REQUIRED |
| `SOC_OUTFIT_003_IMG_02` | `SOC_OUTFIT_003_IMG_02_CAND_01` | 使用 `IMG_9106.HEIC`：鞋店内正面全身记录，保留原站姿、针织开衫、格纹裙、浅色连裤袜与玛丽珍鞋；面部上缘按原始取景保留 | 9:16 source framing | CANDIDATE_GENERATED; REVIEW_REQUIRED |
| `SOC_OUTFIT_003_IMG_03` | pending | 拿着选中的鞋盒离店前的轻松记录；可见鞋款或穿着效果 | 4:5 | DRAFT; source photo pending |

## Visible asset versions

- owner source-derived Face method and L0/L0-derived inputs: pending user photo ingestion and per-image view selection; face-visible images must use the applicable source-derived Face method as the sole face-generation authority
- owner face QA comparison only: approved view-matched Face Canon, after generation only
- body: if needed, deterministic face-excluded derivative only; pending framing
- hairstyle: choose exactly `HAIRSTYLE_A` or `HAIRSTYLE_B` after source photos arrive; do not blend; hair-only reference responsibilities must remain scoped
- cat: none
- outfit: pending user photos/design direction; shoe and clothing references define only those items, never face, skin, body, hair, or identity
- hosiery/material: pending photo visibility and wardrobe; if visible, declare material reference and inspect continuous coverage
- footwear: shoe design and fit from the provided real photos or a scoped shoe-only reference; do not infer a brand
- fixed props: none
- environment: generic temporary public shopping-mall shoe store; no recurring location Canon
- temporary dressing: unbranded shoe boxes, try-on bench and generic shelves; no readable logos, signage or prices

## Platform and crop contract

- must preserve: candid shopping context, plausible shoe fit/contact, natural store lighting, and any selected shoe details that are central to the post
- safe areas / prohibited edge crops: keep face, selected shoes and meaningful shoe-shopping action within the central 90%; do not crop through the shoe being shown or distort feet to force a product angle
- text, logo, UI, watermark policy: none unless explicitly specified; avoid readable brands, prices and store signage

## Carousel-only continuity

Use only the same outing, selected outfit, selected shoe/box and broad time-of-day progression for continuity. Each image is independently generated or edited from its own approved source materials. No generated image defines identity, face, body, hair, shoe design, hosiery material or environment for another image.

## Acceptance criteria

The set should read as a believable shopping moment rather than a product shoot. Preserve the subject's recognizable identity using the applicable source-derived face method; any face styling remains identity-preserving and is checked against the approved Face Canon for QA only. Use only one permitted hairstyle, A or B. Shoes must sit naturally on the feet with plausible scale, fit and floor contact. Reject face contamination, identity drift, malformed footwear, impossible foot/shoe contact, brand text, fake UI, watermark or an environment that implies a locked real store.

## Draft caption

本来只想随便看看，最后还是试了好几双。👟

## Explicit generation gate

- approved by: user
- approval date: 2026-10-20
- approval evidence: “ok，我放进去了，只能按照资产修改长相发型体型。其它光线环境衣着都要保持，尤其丝袜要明显。先来第一张” — authorizes one candidate for IMG_01 only; edits limited to owner face/hair/body attributes, with original scene, lighting, outfit and conspicuous hosiery preserved
- additional approval date: 2026-10-20
- additional approval evidence: “继续修改9106这张图” — authorizes one independent candidate for IMG_02 from `source_inputs/IMG_9106.HEIC`; edits remain limited to owner face/hair/body attributes while preserving the source lighting, environment, outfit and conspicuous hosiery
