# Asset QA

- asset_id:
- asset_level:
- reviewer:
- review_date:
- overall: FAIL
- approval_status: REVIEW_REQUIRED

## Responsibility checks

- Does the asset satisfy every declared `authoritative_for` property?
- Has it avoided redefining every `must_not_define` property?
- Are source IDs, versions, and generation records complete?

## Domain checks

| Domain | PASS/FAIL/N/A | Evidence | Required correction |
|---|---|---|---|
| Identity | | | |
| Body/geometry | | | |
| Appearance | | | |
| Cat identity/coat | | | |
| Outfit | | | |
| Hosiery/material | | | |
| Hands/feet anatomy | | | |
| Prop geometry/scale | | | |
| Environment | | | |
| Continuity | | | |

## Promotion decision

QA does not itself promote an asset. Explicit user approval is still required for L1, followed by a separate version lock decision.
