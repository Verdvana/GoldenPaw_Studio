# HAIR_A_02_3Q_v001 — Asset QA

- asset_id: `HAIR_A_02_3Q`
- asset_level: `L1 Candidate`
- reviewer: `Codex technical precheck`
- review_date: `2026-09-14`
- overall: `PASS — USER APPROVED`
- approval_status: `APPROVED`

## Responsibility checks

| Check | Result | Evidence |
|---|---|---|
| Scoped source roles | PASS | Approved left-3/4 Face defines identity/view only; deterministic masked L0 derivative defines Hairstyle A only. |
| Lineage | PASS | No approved HAIR_A_01 raster, Hair candidate, Expression, Pose or Shot was supplied. |
| Single-file candidate storage | PASS | One authoritative candidate PNG exists in the declared project directory. |

## Domain checks

| Domain | Result | Evidence | User review point |
|---|---|---|---|
| Identity/context | PASS, REVIEW | Left-3/4 adult identity, eye-level head and neutral expression remain broadly aligned with the approved Face Master. | Confirm exact identity preservation; Hair approval cannot redefine it. |
| Hairstyle-A 3/4 design | PASS, REVIEW | Near-center part, controlled crown, readable near/far contours, long straight loose panels, dark-brown restrained highlights and natural asymmetry are present. | Confirm the 3/4 silhouette and face-side relationship. |
| Hair length/end visibility | PASS | All longest tips are visible and none touch or exit the frame. | Lower clearance below the near-side tips is narrower than the prompted ideal but remains reviewable. |
| Outfit | PASS | Only the upper portion of the pink Calibration Outfit appears. | None. |
| Framing/camera | PASS | Exact 3:4, visual eye-level intent, full crown and complete side/bottom hair edges. | None. |
| Body/props/environment | N/A | Not authoritative; no props or scene elements appear. | None. |

## Promotion decision

The user explicitly stated “不错，合格” on 2026-09-14. Promote by move as `OWNER_HAIR_A_02_3Q_CANON_001`. Approval is limited to the visible Hairstyle-A left-three-quarter attributes; all contextual face, skin, expression, body and outfit properties remain outside Hair authority. Full `owner_v1.0` remains unlocked.
