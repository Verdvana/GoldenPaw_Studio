# HAIR_A_01_FRONT_v001 — Asset QA

- asset_id: `HAIR_A_01_FRONT_v001`
- asset_level: `L1 Candidate`
- reviewer: `Codex technical precheck`
- review_date: `2026-09-12`
- overall: `FAIL — FRAMING; REVIEW_REQUIRED`
- approval_status: `REVIEW_REQUIRED`

## Responsibility checks

| Check | Result | Evidence |
|---|---|---|
| Scoped source roles | PASS | Approved Face defines identity/projection only; deterministic L0 derivative defines Hairstyle A only. |
| Lineage | PASS | No prior Hairstyle-A candidate, Body image, Hairstyle-B image, previous shot or mirror was supplied. |
| Single-file candidate storage | PASS | One authoritative candidate PNG exists in the project candidate directory. |

## Domain checks

| Domain | PASS/FAIL/N/A | Evidence | Required correction |
|---|---|---|---|
| Identity | PASS, USER REVIEW | Front-neutral adult identity is broadly coherent with the scoped Face Master. | User confirms exact identity preservation. |
| Hairstyle-A design | PASS, USER REVIEW | Near-center part, low-to-moderate crown volume, long straight loose front panels, dark-brown restrained highlights, fine strands and natural left/right asymmetry are present. | User confirms exact match to the intended A design. |
| Hair length/end visibility | FAIL | The longest left and right tips meet and are clipped by the bottom image boundary; complete length and tapered ends are not inspectable. | Reframe wider/lower through more upper torso, retaining 5–8% clear space beneath every hair tip. |
| Face/skin/expression authority | N/A | Visible face, skin and neutral expression are contextual only and cannot be redefined by this Hair candidate. | None. |
| Outfit | PASS | Only the upper portion of the pink Calibration Outfit appears; source jacket is absent. | None. |
| Framing/camera | FAIL | Exact 3:4 and visual eye-level intent pass, but the hair-bottom breathing-room contract fails. | Preserve 3:4 while showing all hair ends. |
| Body/hosiery/props/environment | N/A | Not authoritative for these domains; no props or scene elements appear. | None. |

## Promotion decision

Not promoted. Technical correction is recommended before approval because the asset cannot fully define front hair length or end geometry while tips are cropped. A new version must be generated from the same two scoped references, never from this candidate.
