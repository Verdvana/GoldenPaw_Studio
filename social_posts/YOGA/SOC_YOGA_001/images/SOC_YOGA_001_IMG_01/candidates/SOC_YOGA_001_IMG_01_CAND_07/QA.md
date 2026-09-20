# QA — CAND_07

- result: REJECTED_COMPOSITION
- candidate status: unapproved L3; not Canon, not a downstream visual input, and not a replacement for the published image.

## Checks

| Check | Result | Notes |
|---|---|---|
| Overhead selfie viewpoint | PASS | Raised-arm, downward-looking direct-selfie composition reads clearly. |
| Required body coverage | PASS | Both legs and white shoes are visible; framing extends below the knees. |
| Mall and tourists | PASS | Indoor mall concourse and anonymous passers-by are clear. |
| Motion blur | PASS | Motion is limited to background passers-by; subject remains readable. |
| Hair / body / outfit responsibility | PASS | Hair-A read, grounded body proportions, registered yoga outfit plus permitted hoodie/shoes, mat and bottle are preserved. |
| Face-safe generation lineage | PASS | Only L0 face inputs were supplied for the visible face; body input was face-excluded. |
| Face QA comparison only | PASS WITH LIMITATION | Compared post-generation against `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` only; no obvious muddy relighting, blotches, smudges, or iterative-generation contamination. This image was never used as an input. |
| Small-face crop | FAIL | The visible face occupies materially more than the requested incidental edge fragment. |
| Approval | PENDING | User review required; no promotion performed. |
