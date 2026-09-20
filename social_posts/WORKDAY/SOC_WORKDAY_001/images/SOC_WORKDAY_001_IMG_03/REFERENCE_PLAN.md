# Reference Plan — SOC_WORKDAY_001_IMG_03

- status: PLANNED / REVIEW_REQUIRED
- responsibility: downward workstation detail; right foot extended backward while the hand lowers the slingback strap

## Generation inputs

| Asset / path | Responsibility | Must not define |
|---|---|---|
| `OWNER_WORK_AUTUMN_01` — `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_AUTUMN_01/OUTFIT.md` | Trousers, black pointed-toe slingback, strap/buckle construction and outfit continuity | Owner face, identity, body, hair, environment |
| `OWNER_POSE_03_SEATED_UPRIGHT_CANON_001` — `characters/CHR_HUMAN_001_OWNER/canon/poses/approved/POSE_03_SEATED_UPRIGHT/OWNER_POSE_03_SEATED_UPRIGHT_CANON_001.png` | Neutral seated workstation mechanics only | Face, hair, outfit, hosiery material, lighting, background |
| `HOS_15D_NUDE_MATTE_CROUCHING` — `materials/hosiery/source_library/raw/15d_nude_matte/IMG_2579.jpg` | Oblique bent-leg/calf/ankle/heel textile response | Person identity, anatomy, pose proportions, clothing, background |
| `HOS_15D_NUDE_MATTE_BAREFOOT` — `materials/hosiery/reference_inputs/15d_nude_matte/IMG_2562_FOOT_MATERIAL_CROP.png` | Underside/heel/toe continuity and matte fabric behavior where visible | Owner identity, body proportions, clothing, pose, background |
| Deterministic face-excluded body derivative, if needed | Neck-below leg and foot proportions only | Face, hair, skin identity, clothing, environment |

## QA comparison only

- Approved owner Face Canon is not expected in frame; if any reflection or crop exposes the face, use it only for post-generation comparison.

## Exclusions

- Hosiery must remain continuous across ankle, heel, instep and toes.
- Show only a shallow temporary red pressure line/area from the lowered strap; no wound, swelling, blood or exaggerated bruising.
- Reject bare toes, material breaks, fused shoe/foot, duplicated toes, floating foot or plastic/latex appearance.
