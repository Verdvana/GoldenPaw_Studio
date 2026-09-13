# Owner Pose Canon Index

```yaml
index_id: OWNER_POSE_CANON_INDEX
character_id: CHR_HUMAN_001_OWNER
index_revision: 3
updated_at: "2026-09-13"
full_release_lock_status: UNLOCKED
approved_pose_components: 3
```

## Current approved components

| Pose | Physical Master | Reference set | Approval mode |
|---|---|---|---|
| `POSE_01_RELAXED_STANDING` | `../body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg` | `OWNER_POSE_01_RELAXED_STANDING_CANON_L1` | explicit scoped reuse; no duplicate raster |
| `POSE_02_WALKING_NEUTRAL_STRIDE` | `approved/POSE_02_WALKING_NEUTRAL_STRIDE/OWNER_POSE_02_WALKING_NEUTRAL_STRIDE_CANON_001.png` | `OWNER_POSE_02_WALKING_NEUTRAL_STRIDE_CANON_L1` | generated candidate moved after explicit approval |
| `POSE_03_SEATED_UPRIGHT` | `approved/POSE_03_SEATED_UPRIGHT/OWNER_POSE_03_SEATED_UPRIGHT_CANON_001.png` | `OWNER_POSE_03_SEATED_UPRIGHT_CANON_L1` | corrected v003 moved after explicit approval |

`POSE_01` inherits only the visible front neutral relaxed-standing articulation. The underlying image remains the unique physical Master `OWNER_BODY_01_FRONT_CANON_002`; this Pose approval does not create a second image asset and does not expand authority to walking, seated, bending, kneeling, prone or other poses.

`POSE_04_SEATED_RELAXED` and later Pose components remain unapproved until separately reviewed.
