# Social Post Specification — 约会提前十分钟

- post_id: SOC_DATE_001
- series_id: MICRO_STORY
- asset_level: L3
- status: ALL_IMAGES_APPROVED
- content_pillar: MICRO_STORY
- format: CAROUSEL
- image_count: 4
- primary_platform: social carousel, unspecified
- primary_aspect_ratio/resolution: native 1122×1402, near 4:5
- approval_status: ALL_FOUR_IMAGES_APPROVED_BY_USER
- external_publishing_performed: no
- Canon_promotion: no

## Final image sequence

| Image | Scene | Approved candidate | Authoritative image path |
|---|---|---|---|
| IMG01 | Cafe entrance, full-body summer outfit | CAND06 | images/SOC_DATE_001_IMG_01/approved/SOC_DATE_001_IMG_01_APPROVED_v1.png |
| IMG02 | Window-side iced coffee, lowered gaze | CAND03 | images/SOC_DATE_001_IMG_02/approved/SOC_DATE_001_IMG_02_APPROVED_v1.png |
| IMG03 | Side-seated cafe chair, hands on backrest, sideward look | CAND03 | images/SOC_DATE_001_IMG_03/approved/SOC_DATE_001_IMG_03_APPROVED_v1.png |
| IMG04 | Street walk seen from behind, turned side face | CAND03 | images/SOC_DATE_001_IMG_04/approved/SOC_DATE_001_IMG_04_APPROVED_v1.png |

## Approval evidence

All decisions 2026-10-30, approver user. IMG01: “批准，下一张”; IMG02: “批准 下一张”; IMG04: “批准”; IMG03: “3也批准”. Each approved directory contains APPROVAL.md with original/current paths and SHA256. Images moved unchanged, candidate directories retain records but no promoted raster copies. Approval is scoped to the L3 photographs as shown; external posting is not performed and no asset is promoted to L1.

## Everyday moment and accepted visual direction

同一夏日下午，从咖啡馆门外到窗边喝冰饮、侧坐聊天，再到附近街道散步回眸。自然生活记录，非中心手持构图；实际画面以用户逐张批准为准。第三张最终采用成功的侧坐版本；背面椅姿请求未返回图像，不属于批准输出。

## Visible assets and responsibilities

Owner outfit: OWNER_DATE_SUMMER_01 clothing-only approved design v003 and user-visible high-waist clarification in OUTFIT.md. White lined chiffon crop with long sleeves, regular-rise denim shorts, white sheer high-waist closed-toe hosiery and silver sandals. True waistband visible below blouse with small gap where shown. No numeric denier assigned.

Original identity generation followed user-directed registered Face recipe: B-derived original face/skin source + masked L0 Hairstyle A; profile shots additionally use real L0 profile. Generated origin of B source is disclosed in individual candidate records and is not mislabeled L0. No global face policy rewrite. Approved Face Canons QA comparison only. Body input deterministic face-excluded v7; clothing/material inputs exclude identity/face/body/skin/hair/light authority. No previous shot supplies identity. Local corrections and their specific user authorizations remain recorded in candidate history.

## Environment and continuity

Generic cafe and nearby street, cream plaster/dark wood/wood furniture, summer afternoon light. Temporary L2 scene specification in TEMPORARY_ASSET_BRIEF.md, no residence/fixed-prop Canon. Each independent shot used scoped master/source assets; previous images never define identity, anatomy or permanent design. Future reuse is continuity-only within declared boundaries.

## Storage and QA

Four authoritative ordinary image files in approved paths above, each with metadata sidecar, approval evidence and checksum. Candidate records preserve original generation prompts, settings when exposed, provenance, local edits, moderation failures and QA. No copied input rasters, no symlink/hardlink deduplication. Final QA is PASS_USER_APPROVED per image; preliminary observations remain historical, not new Canon claims.

## Caption draft — not separately approved

标题：提前十分钟到，也挺好。

冰饮先到了，你还差一点。
今天穿了白色，想把下午过得慢一点。🤍

No new generation, publication or Canon promotion authorized by these image approvals.

## Revision requested — 2026-10-31

User explicitly authorizes regenerating all four with latest approved summer-date outfit/v015 hosiery and newly uploaded pointed closed-toe slingback heels. See SHOE_REFERENCE_20261031.md. Revision status: IN_PROGRESS / new outputs REVIEW_REQUIRED. Existing v1 approval table above remains historical and is not approval of the new revisions. Each shot is independently rebuilt with L0-only face/skin and scoped face-excluded references.

### Revision execution result — 2026-10-31

Four replacements are NOT complete. IMG01 CAND08, IMG02 CAND04 and IMG04 CAND04 returned native 1122×1402 candidates, all REVIEW_REQUIRED. IMG01 still fails face/hair QA; its CAND07 first attempt also lacks ankle straps and is not an input. IMG02/04 have unresolved identity/material-detail checks. IMG03 CAND05 returned no image: first output moderation blocked, two identical retries failed to connect. Exact prompts, input checksums and QA retained per candidate. No successor approved, no old approved images changed, no external posting. Latest results and clickable paths: REVISION_20261031.md.

## User rejects regeneration set; single-image gate — 2026-10-31

“都不合格，一张张来。先来第一张，注意参考的鞋脚脖子处没有带，脚背的带是斜的，参考正脸资产生产方式，参考白色丝袜参考。小腿要笔直”. All preceding returned replacement candidates rejected; old approved_v1 untouched. Only IMG01 CAND09 now authorized: original registered Face01 source recipe per current instruction, no ankle ring/diagonal instep shoe band, mandatory white source/v015 appearance, straight parallel lower legs. Later images wait for this review.

### First-image single candidate returned — CAND09

CAND09 returned1122x1402. Ankle ring removed and diagonal instep straps now visible; original registered Face recipe used. Initial QA still flags calf-axis divergence/curved alignment and held-back side hair; REVIEW_REQUIRED, no pass/approval claimed. Exact likeness/material/shoe geometry remain user review. No later image generated. Candidate record, exact prompt and QA are in its directory.

## First-image scoped acceptance and local correction — CAND10

2026-10-31 user: “鞋子不对称哦，丝袜质感也不对，请参考夏季约会穿搭资产。别的OK”. CAND09 accepted except shoe asymmetry/hosiery appearance, only this same-photo local correction authorized. Face/hair/body/leg geometry/pose/environment must be preserved; earlier agent calf/hair objections no longer current requested work. CAND10 references CAND09 only as same-photo edit target, not new identity lineage. V015 face-free material + original white L0 + approved Foot v002 define hosiery; real shoe crop defines a corresponding left/right mirrored pair with diagonal instep bands and NO ankle ring. One new candidate, no subsequent images.

### Local correction outcome — CAND11

CAND10 failed to mirror shoe diagonals, never downstream input. CAND11 independently edits accepted CAND09: viewer-left diagonal now reversed into corresponding left/right handed pair, white textile response adjusted with approved v015 + mandatory L0 + Foot v002. Same accepted face/hair/body/pose/scene retained at overall review. Initial shoe handedness check passes; precise shoe geometry/material appearance still REVIEW_REQUIRED, not approved. No subsequent image generated.

## Hosiery accepted; strap endpoint correction — CAND12

User: “袜子质感很好，就是鞋的带子反了，我给你的图片是从里面斜向下到外侧，你再研究研究”. CAND11 hosiery explicitly accepted. Same-photo local edit CAND12 only reverses both diagonal bands from MEDIAL HIGH to LATERAL LOW, preserving all accepted content. No new full-image/publication/Canon approval or subsequent-image authorization.

### CAND12 strap-only result

Returned1122x1402. Both diagonal straps now run inner-high to outer-low; initial direction check passes. Hosiery CAND11 acceptance preserved; all other photo attributes locked by edit instructions and visually broadly retained. Exact shoe decorations/endpoints and preservation still user review. No full-image approval or next-image generation.

## CAND13 requested revision — 2026-10-31

User: “还有要修改的，小腿不够直，鞋脚趾缝上面的边沿也有铆钉。画面太ai，光影，构图和色彩都要偏真实大光圈相机拍出来的”. Authorizes same first-photo revision: straight lower legs, toe-cap opening rim studs, realistic large-aperture-camera lighting/composition/color. Accepted hosiery and corrected strap direction remain. One candidate; no later carousel images or publication approved.

### CAND13 result

Returned1122x1402. Ankles moved beneath knees and shin axes straighter; both upper toe-cap vamp rims now have stud rows, correct diagonal band orientation retained. Material/identity/outfit broadly preserved. Photographic treatment remains substantially centered and polished; requested camera realism not fully resolved. REVIEW_REQUIRED, no approval or later images.
