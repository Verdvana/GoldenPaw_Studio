# HOS_05A_SOLE_UNDERSIDE_DETAIL_v008 — Deterministic Crop Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_05A_SOLE_UNDERSIDE_DETAIL
candidate_id: HOS_05A_SOLE_UNDERSIDE_DETAIL_v008
asset_level: L1_CANDIDATE
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "ImageMagick deterministic crop"
status: USER_REJECTED
approval_status: REJECTED
aspect_ratio: "3:4"
reference_set_ids: [HOS_05A_SOLE_UNDERSIDE_DETAIL_v006]
reference_count: 1
previous_generated_hosiery_inputs: []
source_candidate: HOS_05A_SOLE_UNDERSIDE_DETAIL_v006
operation: "crop 826x1000+130+50, then extend to 826x1101 with neutral studio background at bottom"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_05A_SOLE_UNDERSIDE_DETAIL_v008/HOS_05A_SOLE_UNDERSIDE_DETAIL_v008.png"
actual_dimensions_px: "826x1101"
checksum_sha256: "5f600b459cd1e5c01a7ed665405abf4c8339edaaff063c52db87bed5ffe41cc3"
qa_status: FAIL_USER_REJECTED_UNWANTED_PLANTAR_WRINKLES
```

## Scope and limitation

This is a user-requested deterministic framing derivative intended to remove the artificial lower-leg/model termination from the material-study view. It preserves the v006 pixel content in the retained region and does not regenerate or retouch the textile. The cropped composition is a sole/heel material detail and must not be used to define complete owner body or ankle anatomy.

## QA

- Retains both soles, heels, arches and toe-region textile texture.
- Removes the long lower-leg model forms from the main view.
- Maintains 3:4 dimensions without stretching the retained pixels.
- Candidate remains `REVIEW_REQUIRED`; no Canon promotion performed.
- User rejected v008 because the plantar area contains excessive, unnatural wrinkle/fold structures inconsistent with smooth 15D velvet-matte hosiery.
- Candidate is excluded from Canon promotion and downstream use.
