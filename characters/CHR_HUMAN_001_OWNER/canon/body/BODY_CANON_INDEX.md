# Owner Body Canon Index

```yaml
index_id: OWNER_BODY_CANON_INDEX
character_id: CHR_HUMAN_001_OWNER
index_revision: 10
updated_at: "2026-09-12"
full_release_lock_status: UNLOCKED
approved_body_components: 6
```

## Current approved Masters

| Asset ID | View | Master | SHA-256 | Downstream set | L1 recovery method |
|---|---|---|---|---|---|
| `OWNER_BODY_01_FRONT_CANON_002` | front neutral standing, 168 cm / 60 kg target | `approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg` | `964c3b9d72c6688881b8ebfa4c6fc1bcfea04c998351352fabfdc8f4951666f6` | `OWNER_BODY_FRONT_CANON_L1` | `BODY_01_FRONT_METHOD.md` |
| `OWNER_BODY_02_LEFT_3Q_CANON_001` | anatomical left 3/4 neutral standing, 168 cm / 60 kg target | `approved/BODY_02_LEFT_3Q/OWNER_BODY_02_LEFT_3Q_CANON_001.png` | `f364b5c9b398c0c786964ffb8932707c7d657f997b8344abdd31a47b4322f4aa` | `OWNER_BODY_LEFT_3Q_CANON_L1` | source/reference responsibilities preserved in candidate record |
| `OWNER_BODY_03_RIGHT_3Q_CANON_001` | anatomical right 3/4 neutral standing, 168 cm / 60 kg target | `approved/BODY_03_RIGHT_3Q/OWNER_BODY_03_RIGHT_3Q_CANON_001.png` | `32f87f0232bb087b434d1818ec22d2db1ba4311ec73b7e0fe2ebf380279412fd` | `OWNER_BODY_RIGHT_3Q_CANON_L1` | source/reference responsibilities preserved in v005 record |
| `OWNER_BODY_04_LEFT_SIDE_CANON_001` | anatomical left side neutral standing, 168 cm / 60 kg target | `approved/BODY_04_LEFT_SIDE/OWNER_BODY_04_LEFT_SIDE_CANON_001.png` | `800d422c125fdaff24568355994633156f8e17b12fbfa292aa8e83ed13ed394a` | `OWNER_BODY_LEFT_SIDE_CANON_L1` | source/reference responsibilities preserved in v002 record |
| `OWNER_BODY_05_RIGHT_SIDE_CANON_001` | anatomical right side neutral standing, 168 cm / 60 kg target | `approved/BODY_05_RIGHT_SIDE/OWNER_BODY_05_RIGHT_SIDE_CANON_001.png` | `b71d47d932352985e0d8347ca7ddb485d86bc3b6ac3ddb8183ae02615c6a14cc` | `OWNER_BODY_RIGHT_SIDE_CANON_L1` | source/reference responsibilities preserved in v001 record |
| `OWNER_BODY_06_BACK_CANON_001` | exact 180-degree back neutral standing, 168 cm / 60 kg target | `approved/BODY_06_BACK/OWNER_BODY_06_BACK_CANON_001.png` | `2344a37e9355bbe1fb49865b5039275cebbbe5cfb043738b7e2edb6c777add7c` | `OWNER_BODY_BACK_CANON_L1` | source/reference responsibilities preserved in v001 record |

These are the six current active approved, unlocked L1 Body components. Their shared 168 cm / 60 kg target, visible face where applicable, `HAIRSTYLE_A`, limb proportions and waist/hip ratio may be referenced within each component's view scope. Dedicated view-specific Face/Hair Canon remains the preferred precision authority when applicable. Hosiery scope is strictly limited to the accepted `15D nude matte/velvet` appearance within each Body component; final reusable material authority remains Gate 7. Gate 3 is complete and Gate 4 is open, while the full `owner_v1.0` remains unlocked.

The candidate PNG was moved to the approved path after explicit user approval. The user later transcoded the active Master to `OWNER_BODY_01_FRONT_CANON.jpg` and deleted the PNG. The JPG is now the single physical active Master; the pre-transcode PNG checksum remains textual provenance only.

Ordinary downstream work uses the active approved Master. L1 recreation uses `OWNER_BODY_FRONT_RECOVERY_V1` and the method document; it must never use either approved Master or any generated BODY_01 candidate as an image input.

## Superseded approved component

`OWNER_BODY_01_FRONT_CANON_001` remains a historically approved but superseded component in textual records only. Its former JPG raster and sidecar metadata were removed by the user during the 2026-09-12 single-file cleanup. The original approval evidence and checksums remain as provenance; there is no live path and it must not be selected as the current front Body Master.
