# Fresh redo QA

- candidate_id: SOC_DATE_001_IMG_01_CAND_05
- reviewer: Codex preliminary visual review
- review_date: 2026-10-30
- overall: FAIL_PRELIMINARY_REVIEW
- approval_status: REVIEW_REQUIRED
- eligible_for_publishing: no
- eligible_as_continuity_reference: no

| Domain | Result | Evidence |
|---|---|---|
| Original face recipe | PASS process | Original B face/skin + L0 masked A restored; no previous social image input. |
| Face likeness / contamination | REVIEW | Compared after generation with approved FACE_01; natural skin without obvious patches, exact likeness remains user review. Fresh sources do not guarantee accepted likeness. |
| Lower-leg axes | IMPROVED / REVIEW | Fairly straight knee-to-ankle alignment with natural calf contour; user confirmation pending. |
| Toe detail diffusion / fabric curves | FAIL | Some haze and nail detail softening, but foreground individual toe tips remain clearly separated; suspended intertoe textile geometry not sufficiently resolved. |
| Waist layering | FAIL | Pale edging immediately above denim appears again, conflicting with explicit lower-ring exclusion. |
| Candid action | FAIL | Hand touching hair reads staged and contradicts prompt; scene has less camera roll than intended. |
| Hair A | REVIEW | Long straight hair retained; sides swept back/crown remain potential A drift. |
| Clothing / anatomy / crop | PASS preliminary otherwise | Whole body and both shoes retained, coherent cafe light, no obvious extra limbs. |
| Text / watermark | PASS | No overlay or watermark observed. |

## Decision

Fresh independent candidate saved, not accepted. Required toe geometry still unresolved and lower-ring/staged-action defects appeared. No auto retry, publication, Canon promotion or downstream use. One authoritative raster in repository, no copied reference images.

## Subsequent user review supersedes preliminary objections

User accepts all non-shin attributes in USER_REVIEW.md; only further shin straightening requested. Preserve accepted content exactly. Historical model observations above are not current user blockers.
