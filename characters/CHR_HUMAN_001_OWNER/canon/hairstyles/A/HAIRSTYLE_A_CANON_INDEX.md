# Owner Hairstyle A Canon Index

```yaml
index_id: OWNER_HAIRSTYLE_A_CANON_INDEX
character_id: CHR_HUMAN_001_OWNER
index_revision: 6
updated_at: "2026-09-14"
full_release_lock_status: UNLOCKED
approved_hairstyle_a_components: 6
```

## Current approved Masters

| Asset ID | View | Master | SHA-256 | Downstream set | L1 recovery basis |
|---|---|---|---|---|---|
| `OWNER_HAIR_A_01_FRONT_CANON_001` | standard eye-level front, complete long-hair ends | `approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png` | `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219` | `OWNER_HAIR_A_FRONT_CANON_L1` | approved Face scope + deterministic L0 Hairstyle-A derivative; never use generated Hair pixels for L1 recovery |
| `OWNER_HAIR_A_02_3Q_CANON_001` | anatomical-left eye-level 3/4, complete near/far panels and ends | `approved/HAIR_A_02_3Q/OWNER_HAIR_A_02_3Q_CANON_001.png` | `160fd3c30c2756d438877ee6508a3e424ec96aaecde84917610a92196e759919` | `OWNER_HAIR_A_LEFT_3Q_CANON_L1` | approved left-3/4 Face scope + deterministic L0 Hairstyle-A derivative; never use generated Hair pixels for L1 recovery |
| `OWNER_HAIR_A_03_SIDE_CANON_001` | anatomical-left eye-level true profile, readable hairline/ear/rear contour and complete ends | `approved/HAIR_A_03_SIDE/OWNER_HAIR_A_03_SIDE_CANON_001.png` | `3f1e9b07b7342f5ab1636d723c06fcbb299833d8ddaa521575711bb056ee2930` | `OWNER_HAIR_A_LEFT_SIDE_CANON_L1` | approved left-profile Face scope + deterministic L0 Hairstyle-A derivative; retain true-profile L0 evidence limitation and never use generated Hair pixels for L1 recovery |
| `OWNER_HAIR_A_04_BACK_CANON_001` | exact centered rear, complete crown/rear mass/outer silhouette and tapered ends | `approved/HAIR_A_04_BACK/OWNER_HAIR_A_04_BACK_CANON_001.png` | `91128987bc4aade21f7b7fd3a7b9bd24d2ca3d0100847214844b702741852e53` | `OWNER_HAIR_A_BACK_CANON_L1` | approved rear Body orientation scope + deterministic L0 Hairstyle-A derivative; never use generated Hair pixels for L1 recovery |
| `OWNER_HAIR_A_05_HIGH_CAMERA_LOOK_UP_CANON_001` | high camera looking down, subject raises head toward lens; crown/part and shifted panels visible | `approved/HAIR_A_05_HIGH_CAMERA_LOOK_UP/OWNER_HAIR_A_05_HIGH_CAMERA_LOOK_UP_CANON_001.png` | `0f8c8f5dfbfdc017df5082b79657e23657f52e520ea4d3d3f5d612dbade4404a` | `OWNER_HAIR_A_HIGH_CAMERA_LOOK_UP_CANON_L1` | approved front Face identity scope + deterministic L0 Hairstyle-A derivative; never use generated Hair pixels for L1 recovery |
| `OWNER_HAIR_A_06_LOW_CAMERA_LOOK_DOWN_CANON_001` | low camera looking up, subject looks down; hidden crown/scalp and slightly image-left root-flow apex | `approved/HAIR_A_06_LOW_CAMERA_LOOK_DOWN/OWNER_HAIR_A_06_LOW_CAMERA_LOOK_DOWN_CANON_001.png` | `2a1c53cd28c397b3a019ced39a4dc55aebe9c8ab7881518cb4516dc2ef341ded` | `OWNER_HAIR_A_LOW_CAMERA_LOOK_DOWN_CANON_L1` | approved front Face scope + deterministic L0 Hair-A derivative; A01 measurement-only, never use generated Hair pixels for recovery |

All six Hairstyle-A view components are approved and unlocked. Their authority is hair-only and angle-scoped. Face, skin, expression, body, outfit, lighting and background remain outside their scope. The complete `owner_v1.0` remains unlocked.
