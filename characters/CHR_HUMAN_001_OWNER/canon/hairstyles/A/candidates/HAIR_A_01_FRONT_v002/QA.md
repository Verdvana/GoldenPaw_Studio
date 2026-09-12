# HAIR_A_01_FRONT_v002 — Asset QA

- asset_id: `HAIR_A_01_FRONT_v002`
- asset_level: `L1 Candidate`
- reviewer: `Codex technical precheck`
- review_date: `2026-09-12`
- overall: `PASS — USER APPROVED`
- approval_status: `APPROVED`

## Responsibility checks

| Check | Result | Evidence |
|---|---|---|
| Scoped source roles | PASS | Approved Face defines identity/nose/projection only; deterministic L0 derivative defines Hairstyle A only. |
| Lineage | PASS | v001 pixels were not supplied; no Body, Hairstyle-B, previous shot or adjacent Hair candidate was used. |
| Single-file candidate storage | PASS | One authoritative candidate PNG exists in the project candidate directory. |

## Domain checks

| Domain | PASS/FAIL/N/A | Evidence | Required correction |
|---|---|---|---|
| Identity/nose preservation | PASS, USER APPROVED CONTEXT | The nose is visibly more restrained than v001 and broadly matches the approved Face Master's natural bridge, tip and alar proportions; this Hair asset acquires no face authority. | None. |
| Hairstyle-A design | PASS, USER APPROVED | Near-center part, low-to-moderate crown volume, long straight loose front panels, dark-brown restrained highlights, fine strands and natural asymmetry are present. | None. |
| Hair length/end visibility | PASS | Both outer edges and all longest tapered tips are complete, with clear space beneath them. | None. |
| Face/skin/expression authority | N/A | Visible face, skin and expression remain contextual and cannot be redefined by this Hair candidate. | None. |
| Outfit | PASS | Only the pink Calibration Outfit upper portion is visible; source jacket is absent. | None. |
| Framing/camera | PASS | Exact 3:4, visual eye-level front projection, complete crown and hair edges, and adequate lower breathing room. | None. |
| Body/hosiery/props/environment | N/A | Not authoritative for these domains; no props or scene elements appear. | None. |

## Promotion decision

The user explicitly approved the candidate by stating “可以的，登记吧”. It was promoted unchanged to `OWNER_HAIR_A_01_FRONT_CANON_001`; the candidate directory retains records only. Five Hairstyle-A views remain pending, and the complete `owner_v1.0` release remains unlocked.
