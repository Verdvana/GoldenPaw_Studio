# Social Post Reference Plan

- post_id: `SOC_CAMPUS_001`
- image_asset_id: `SOC_CAMPUS_001_IMG_05`
- candidate_id: `SOC_CAMPUS_001_IMG_05_CAND_01`
- status: `READY_FOR_SINGLE_CANDIDATE`
- reference_count: `0`
- budget_limit: `8`
- budget_exception: `none`
- selected_reference_set_ids: `[]`

| Priority | Reference ID/path | Level/status/version | `generation_input` or `qa_comparison_only` | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|---|

## Face-safe declaration

- face visible: `no`
- applicable source-derived Face method: `not applicable; face/head outside frame`
- L0 or deterministic L0-derived face inputs: `none`
- approved AI Face Canon QA comparison only: `none`
- face-excluded body derivative and checksum: `none; no body image reference used`

## Conflict resolution

Registered outfit is carried forward in text only from approved campus images. Their pixels and all generated images are excluded as generation inputs. The new dorm is a generic temporary environment and is not based on the owner's residence Canon. No image references are needed for this crop-focused everyday scene.

## Excluded references

- Approved `SOC_CAMPUS_001_IMG_01`–`IMG_03`: text-only wardrobe continuity; image pixels excluded to avoid generated identity/body/environment lineage.
- `SOC_CAMPUS_001_IMG_04` candidates: excluded as prior unapproved/failed outputs.
- Owner Face/Body Canon images: excluded; face is outside frame and no body reference is needed.
- Material source images: excluded; hosiery is not the focus and retains the registered text-defined campus appearance.
