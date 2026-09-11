# Owner Body Canon Index

```yaml
index_id: OWNER_BODY_CANON_INDEX
character_id: CHR_HUMAN_001_OWNER
index_revision: 2
updated_at: "2026-09-11"
full_release_lock_status: UNLOCKED
approved_body_components: 1
```

## Current approved Masters

| Asset ID | View | Master | SHA-256 | Downstream set | L1 recovery method |
|---|---|---|---|---|---|
| `OWNER_BODY_01_FRONT_CANON_001` | front neutral standing | `approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_001.jpg` | `86455eafd8917022a45323835bf693d24dd86b618caac581f018063a17963a57` | `OWNER_BODY_FRONT_CANON_L1` | `BODY_01_FRONT_METHOD.md` |

This is an approved, unlocked L1 component. Its authority is limited to front-view body geometry and neutral stance. The full `owner_v1.0` remains unlocked, and BODY_02–BODY_06 remain pending.

The approved Master was user-transcoded from PNG to JPG for transfer efficiency. The original candidate PNG path and checksum remain as textual generation/approval provenance, while its raster was removed so the JPG is the single physical Master. Format conversion does not create a new body decision or change the approved scope.

Ordinary downstream work uses the approved Master. L1 recreation uses `OWNER_BODY_FRONT_RECOVERY_V1` and the method document; it must never use the approved Master or any generated BODY_01 candidate as an image input.
