# SOC_COMMUTE_001 — 下班后的 30 分钟

- post_id: SOC_COMMUTE_001
- series_id: COMMUTE
- asset_level: L3
- status: PUBLISHED
- content_pillar: MICRO_STORY
- format: CAROUSEL
- image_count: 3
- primary_platform: social feed
- primary_aspect_ratio/resolution: 4:5 / 2160x2700 px delivery target
- requested_publish_window: null
- approval_status: PUBLISHED

## Everyday moment

同一天下班后的连续生活片段：办公楼电梯自拍、步行经过公园、搭乘晚间地铁。它是初次见面帖，不是商业棚拍，不出现住宅或猫资产。

## Image list

| Image asset ID | Candidate ID | Intended framing/action | Aspect ratio | Status |
|---|---|---|---|---|
| SOC_COMMUTE_001_IMG_01 | SOC_COMMUTE_001_IMG_01_CAND_06 | 电梯全身镜面自拍 | 4:5 | PUBLISHED_L3 |
| SOC_COMMUTE_001_IMG_02 | SOC_COMMUTE_001_IMG_02_CAND_11 | 公园边走边高机位前置自拍 | 4:5 | PUBLISHED_L3_V2 |
| SOC_COMMUTE_001_IMG_03 | SOC_COMMUTE_001_IMG_03_CAND_09 | 地铁坐姿、高位远景俯拍；对侧连凳与紧凑横向过道 | 4:5 | PUBLISHED_L3_V2 |

## Visible asset versions

- owner source-derived Face method and L0/L0-derived inputs: per-image `REFERENCE_PLAN.md`; no AI Face/Body Canon is a generation input.
- owner face QA comparison only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` and view-matched approved Face Canon if applicable.
- body: `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1`, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`.
- hairstyle: HAIRSTYLE_A, selected per camera projection.
- cat: none.
- outfit: `OWNER_WORK_SUMMER_01_WORN_FULL_BODY`, approved worn full-body v002.
- hosiery/material: the outfit’s approved 15D gray matte pantyhose and gray-beige/light-champagne taupe buckle pumps.
- fixed props: none.
- temporary dressing: `TEMPORARY_ASSET_BRIEF.md` only.

## Platform and crop contract

- must preserve: one clear full-body read in image 01, a partial-face walking view with legs and shoes visible in image 02, and a non-face-visible seated commute point-of-view in image 03.
- safe areas / prohibited edge crops: do not crop through the primary thigh-to-knee area, a visible portion of the phone edge, or the meaningful passenger-density context; do not place essential details in the outer 5% of any edge.
- text, logo, UI, watermark policy: no readable brand, company name, personal name, QR code, barcode, watermark, fake interface or garbled text.

## Carousel-only continuity

The same workday, same approved summer work outfit, silver iPhone 17 Pro, white-and-blue generic work badge and natural canvas tote are retained. HAIRSTYLE_A is not visible in image 03 and therefore is not a generation requirement for that image. Permitted continuity is limited to time progression, wardrobe, temporary object placement and action. Every image remains an independent generation from approved sources; no generated image is an identity, body, hair, prop, material or environment input for another.

## Acceptance criteria

Each image must pass its independent QA; the three together must read as one plausible commute without forcing identical camera position, lighting or background. Explicit publishing approval is required after QA and does not promote any image to Canon.

## Publication record

- published_by: user
- published_date: 2026-09-18
- publication_evidence: user statement “很好，已发布，这篇帖子已完结。”
- final_state: COMPLETE
- note: The post's approved L3 images remain post-specific assets only. None is promoted to Canon or authorized as a downstream visual generation input.

## Final asset record

- Image 01: `images/SOC_COMMUTE_001_IMG_01/approved/SOC_COMMUTE_001_IMG_01_APPROVED_v1.png`
- Image 02: `images/SOC_COMMUTE_001_IMG_02/approved/SOC_COMMUTE_001_IMG_02_APPROVED_v2.png`
- Image 03: `images/SOC_COMMUTE_001_IMG_03/approved/SOC_COMMUTE_001_IMG_03_APPROVED_v2.png`
- All three are published L3 post assets only; no Canon or downstream-reference authority.
