# HAIR_A_03_SIDE_v001 — Asset QA

- asset_id: `HAIR_A_03_SIDE`
- asset_level: `L1 Candidate`
- reviewer: `Codex technical precheck`
- review_date: `2026-09-14`
- overall: `PASS — USER APPROVED`
- approval_status: `APPROVED`

## Responsibility checks

| Check | Result | Evidence |
|---|---|---|
| Scoped source roles | PASS | Approved left-profile Face defines identity/view only; deterministic masked L0 derivative defines Hairstyle A only. |
| Evidence limitation | DISCLOSED | The approved left-profile face silhouette lacks matching-direction true-profile L0 verification. |
| Lineage | PASS | No approved HAIR_A_01/02 raster, Hair candidate, Expression, Pose or Shot was supplied. |
| Single-file candidate storage | PASS | One authoritative candidate PNG exists in the declared project directory. |

## Domain checks

| Domain | Result | Evidence | User review point |
|---|---|---|---|
| Identity/context | PASS, REVIEW | Anatomical-left adult profile, nose image-right, eye-level head and neutral expression remain broadly aligned with the approved profile Face Master. | Confirm exact identity preservation; Hair approval cannot redefine it. |
| Hairstyle-A side design | PASS, REVIEW | Readable hairline/near ear, controlled crown and rear contour, unobscured profile, distinct front/rear long straight fall and restrained dark-brown highlights are present. | Confirm side silhouette, ear-side relation and rear-hair depth. |
| Hair length/end visibility | PASS | All outer hair edges and longest tapered tips are visible with clear lower breathing room. | Confirm the below-chest length and end density. |
| Outfit | PASS | Only the upper portion of the pink Calibration Outfit appears. | None. |
| Framing/camera | PASS | Exact 3:4, visual eye-level intent, full crown and complete side/bottom hair edges. | None. |
| Body/props/environment | N/A | Not authoritative; no props or scene elements appear. | None. |

## Promotion decision

The user explicitly stated “批准” on 2026-09-14. Promote by move as `OWNER_HAIR_A_03_SIDE_CANON_001`. Approval is limited to the visible anatomical-left standard-side Hairstyle-A attributes; all contextual face, skin, expression, body and outfit properties remain outside Hair authority. The underlying left-profile Face evidence limitation remains disclosed. Full `owner_v1.0` remains unlocked.
