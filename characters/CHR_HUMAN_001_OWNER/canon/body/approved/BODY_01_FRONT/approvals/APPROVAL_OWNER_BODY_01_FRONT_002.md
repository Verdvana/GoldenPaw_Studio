# Scoped L1 Approval — Owner Front Body v2

- approval_id: APPROVAL_OWNER_BODY_01_FRONT_002
- asset_id: OWNER_BODY_01_FRONT_CANON_002
- asset_path: `../OWNER_BODY_01_FRONT_CANON_002.png`
- source_candidate: BODY_01_FRONT_v009
- approved_level: L1 component
- decision: APPROVED
- approver: user
- decision_date: 2026-09-11
- lock_status: UNLOCKED_COMPONENT
- checksum_sha256: `cbb08e1799a6d6d3d9e00b600ceaab294a36a2b04a170ae1a367e28578cd0164`

## Approval evidence

The user stated: “非常好长相发型，四肢比例，腰臀比，等等，以及腿部脚部丝袜质感都合格，可以作为正式资产”.

## Approved authoritative scope

- physical target of 168 cm and approximately 60 kg (120 jin), reusable when generating other character assets and shot/video-frame images;
- the approved visible face appearance and `HAIRSTYLE_A`, reusable for other character assets and shot/video-frame images; dedicated view-specific Face/Hair Canon remains the more precise authority when applicable;
- front-view head-to-body, torso-to-limb and arm/leg/foot proportions, reusable as the body baseline for other assets and shot/video-frame images;
- front shoulder, torso, waist, hip geometry and waist/hip ratio;
- straight, symmetric lower-leg axes and accepted leg/foot geometry;
- neutral square standing posture;
- hosiery appearance only as a scoped reference for `15D matte nude` presentation.

## Explicit exclusions / must not define

- side, rear or articulated body geometry;
- Calibration Outfit design outside this component;
- every hosiery color other than nude;
- every hosiery denier/thickness other than 15D;
- every hosiery finish or material behavior other than matte, including gloss, soft-sheen, velvet-gloss and opaque variants;
- using this image as a generic hosiery reference across variants; Gate 7 and the selected material reference remain responsible for each other color/finish/denier combination;
- episode wardrobe, lighting, background or rendering artifacts.

## Downstream reference rule

For other character assets and shot/video-frame images, this asset may jointly carry the approved 168 cm / 60 kg stature, visible face, `HAIRSTYLE_A`, limb proportions and waist/hip ratio. Use dedicated Face or Hairstyle Canon when the shot needs a different view or finer identity/hair authority. If hosiery differs in color, finish or denier, exclude this asset's hosiery appearance and select the matching material reference separately.

## Promotion action

The candidate image was moved to the approved Master path rather than copied. Its candidate directory retains only records and a promotion pointer. `OWNER_BODY_01_FRONT_CANON_002` becomes the active target of `OWNER_BODY_FRONT_CANON_L1`; `OWNER_BODY_01_FRONT_CANON_001` remains historical and superseded. The complete `owner_v1.0` release remains unlocked.
