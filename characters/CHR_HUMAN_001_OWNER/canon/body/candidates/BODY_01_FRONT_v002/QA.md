# BODY_01_FRONT_v002 — Asset QA

- asset_id: `BODY_01_FRONT_v002`
- asset_level: `L1 Candidate`
- reviewer: `Codex pre-review`
- review_date: `2026-09-11`
- overall: **FAIL**
- approval_status: `REVIEW_REQUIRED`

## Responsibility checks

- The image is usable for reviewing a proposed front body silhouette and neutral stance, but it does not satisfy all mandatory visible constraints.
- The scoped sources and their exclusions are recorded in `generation_record.md`.
- It is not approved, not Canon, and may not become a downstream L1 reference.

## Domain checks

| Domain | PASS/FAIL/N/A | Evidence | Required correction |
|---|---|---|---|
| Identity | FAIL | The result resembles the approved front Master, but the facial geometry reads somewhat narrower and more generic; exact preservation is not established. | User comparison required; any retry must start again from the same approved/source references, never from this candidate. |
| Body/geometry | PASS | Full front body is visible in an even, uncrossed stance with readable shoulder, torso, waist, hip, limb and foot proportions. | User must decide whether the proposed body proportions match the intended Canon. |
| Appearance | FAIL | HAIRSTYLE_A category is present, but length/face-framing distribution is shorter and less faithful than the scoped hair reference. | Restore the approved Hairstyle A structure without letting hair redefine face or body. |
| Cat identity/coat | N/A | No cat. | None. |
| Outfit | PASS | Plain pink high-cut one-piece swimsuit, no shoes, no decoration. | None for the swimsuit itself. |
| Hosiery/material | FAIL | Legs have a soft finish, but the toes, insteps and heels visually read as bare skin; no reliable continuous 15D textile layer is visible over the feet. | Make fine textile continuity visibly legible from legs through ankles, heels, insteps and every toe while avoiding gloss or coating. |
| Hands/feet anatomy | PASS | Two hands and two feet are complete; no obvious missing or extra digits at full-image inspection. | Recheck at approval resolution; hosiery failure is separate. |
| Prop geometry/scale | N/A | No props. | None. |
| Environment | PASS | Neutral gray-white seamless studio and restrained lighting. | None. |
| Continuity | N/A | First successful Body candidate; no previous candidate was used. | None. |

## Promotion decision

Reject for Canon promotion in its current state. QA does not authorize a retry lineage from this image. If the user requests a revision, create an independent candidate from the same approved Face Master, L0 body context and masked Hairstyle A reference.
