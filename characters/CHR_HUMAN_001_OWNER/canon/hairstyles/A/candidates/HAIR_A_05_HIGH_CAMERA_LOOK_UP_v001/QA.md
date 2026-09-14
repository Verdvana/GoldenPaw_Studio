# HAIR_A_05_HIGH_CAMERA_LOOK_UP_v001 — Asset QA

- asset_id: `HAIR_A_05_HIGH_CAMERA_LOOK_UP`
- asset_level: `L1 Candidate`
- reviewer: `Codex technical precheck`
- review_date: `2026-09-14`
- overall: `PASS — USER APPROVED`
- approval_status: `APPROVED`

## Responsibility checks

| Check | Result | Evidence |
|---|---|---|
| Scoped source roles | PASS | Approved front Face defines identity only; masked L0 derivative defines Hairstyle A only. |
| Perspective isolation | PASS | High-camera/raised-head geometry is the candidate's calibration scope and cannot redefine the neutral eye-level Face Canon. |
| Lineage | PASS | No approved HAIR_A_01/02/03/04 raster, generated Hair candidate, Expression, Pose or Shot was supplied. |
| Single-file candidate storage | PASS | One authoritative candidate PNG exists in the declared project directory. |

## Domain checks

| Domain | Result | Evidence | User review point |
|---|---|---|---|
| Camera/head relationship | PASS, REVIEW | The camera is visibly elevated and pitched downward; the whole head is raised toward the lens, with strong crown visibility and plausible facial foreshortening. | Confirm the desired degree of high-camera exaggeration. |
| Identity context | PASS, REVIEW | Stable facial relationships remain recognizable under the intended foreshortening; no overt beautification or childlike redesign is present. | Confirm identity match; this Hair approval cannot redefine the face. |
| Hairline/part/crown | PASS, REVIEW | Upper forehead hairline, full top surface and extended near-center part are readable; crown stays controlled and non-puffy. | Confirm part path and visible crown area. |
| Face-side projection | PASS | Both long straight panels shift backward/outward consistently with raised-head gravity while remaining readable. | Confirm the panel relationship. |
| Length/end visibility | PASS | Both outer edges and all tapered irregular ends remain visible with clear space below. | Confirm foreshortened apparent length. |
| Outfit/background | PASS | Pink Calibration Outfit upper portion and neutral gray-white studio only; no source jacket, props, text, logo or watermark. | None. |

## Promotion decision

The user explicitly approved the candidate with “批准 下一个”. Promote by move as `OWNER_HAIR_A_05_HIGH_CAMERA_LOOK_UP_CANON_001`. Authority remains limited to Hairstyle-A behavior under this high-camera/subject-looking-up perspective. Full `owner_v1.0` remains unlocked.
