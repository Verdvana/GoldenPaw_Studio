# Owner Pose Canon Index

```yaml
index_id: OWNER_POSE_CANON_INDEX
character_id: CHR_HUMAN_001_OWNER
index_revision: 10
updated_at: "2026-09-14"
full_release_lock_status: UNLOCKED
approved_pose_components: 9
```

## Current approved components

| Pose | Physical Master | Reference set | Approval mode |
|---|---|---|---|
| `POSE_01_RELAXED_STANDING` | `../body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg` | `OWNER_POSE_01_RELAXED_STANDING_CANON_L1` | explicit scoped reuse; no duplicate raster |
| `POSE_02_WALKING_NEUTRAL_STRIDE` | `approved/POSE_02_WALKING_NEUTRAL_STRIDE/OWNER_POSE_02_WALKING_NEUTRAL_STRIDE_CANON_001.png` | `OWNER_POSE_02_WALKING_NEUTRAL_STRIDE_CANON_L1` | generated candidate moved after explicit approval |
| `POSE_03_SEATED_UPRIGHT` | `approved/POSE_03_SEATED_UPRIGHT/OWNER_POSE_03_SEATED_UPRIGHT_CANON_001.png` | `OWNER_POSE_03_SEATED_UPRIGHT_CANON_L1` | corrected v003 moved after explicit approval |
| `POSE_04_SEATED_RELAXED` | `approved/POSE_04_SEATED_RELAXED/OWNER_POSE_04_SEATED_RELAXED_CANON_001.png` | `OWNER_POSE_04_SEATED_RELAXED_CANON_L1` | v001 moved after explicit approval |
| `POSE_05_SLIGHT_BODY_TURN` | `../body/approved/BODY_02_LEFT_3Q/OWNER_BODY_02_LEFT_3Q_CANON_001.png` | `OWNER_POSE_05_SLIGHT_BODY_TURN_CANON_L1` | explicit scoped reuse; no duplicate raster |
| `POSE_06_BENDING_REACHING` | `approved/POSE_06_BENDING_REACHING/OWNER_POSE_06_BENDING_REACHING_CANON_001.png` | `OWNER_POSE_06_BENDING_REACHING_CANON_L1` | v002 moved after explicit approval; material appearance excluded |
| `POSE_07_KNEELING_CROUCHING` | `approved/POSE_07_KNEELING_CROUCHING/OWNER_POSE_07_KNEELING_CROUCHING_CANON_001.jpg` | `OWNER_POSE_07_KNEELING_CROUCHING_CANON_L1` | generated candidate v004 moved after explicit approval |
| `POSE_08_SEATED_LEGS_EXTENDED` | `approved/POSE_08_SEATED_LEGS_EXTENDED/OWNER_POSE_08_SEATED_LEGS_EXTENDED_CANON_001.png` | `OWNER_POSE_08_SEATED_LEGS_EXTENDED_CANON_L1` | v002 moved after explicit approval; intended straight-leg/sole view and material appearance excluded |
| `POSE_09_PRONE_ARMS_KNEES_SUPPORTED` | `approved/POSE_09_PRONE_ARMS_KNEES_SUPPORTED/OWNER_POSE_09_PRONE_ARMS_KNEES_SUPPORTED_CANON_001.jpg` | `OWNER_POSE_09_PRONE_ARMS_KNEES_SUPPORTED_CANON_L1` | generated candidate v003 moved after explicit approval |

`POSE_01` inherits only the visible front neutral relaxed-standing articulation. The underlying image remains the unique physical Master `OWNER_BODY_01_FRONT_CANON_002`; this Pose approval does not create a second image asset and does not expand authority to walking, seated, bending, kneeling, prone or other poses.

`POSE_05` inherits only the visible approximately 35–45-degree left-three-quarter neutral standing turn. The underlying image remains the unique physical Master `OWNER_BODY_02_LEFT_3Q_CANON_001`; this Pose approval creates no second image and does not authorize rightward turns, walking, seated, bending, kneeling, crouching, prone or other poses.

`POSE_06` is authoritative only for its bending/reaching articulation. Its upper-thigh folds, white-shifted hosiery hue and painted-white toe appearance are known presentation limitations and must never define hosiery material, color, foot treatment or nail color.

`POSE_07` is authoritative only for its visible approximately 45-degree right-three-quarter half-kneeling/crouching posture articulation (front knee 90 degrees flexed with planted flat foot, rear knee on floor plane, rear forefoot contacting floor, upright neutral spine).

`POSE_08` is authoritative only for its visible approximately 45-degree left-three-quarter seated articulation, separated forward legs, relaxed lower-limb joints and hand support. Its non-straight knees, non-sole-facing feet, pale/opaque hosiery and gray-white toenails are known limitations and must not define the intended straight-leg/sole-facing geometry, hosiery material/color/denier/toe treatment or nail color.

`POSE_09` is authoritative only for its visible approximately 45-degree left-three-quarter tabletop four-point posture articulation (palms flat under shoulders, knees under hips, horizontal neutral spine, forefoot/toe pad contact with elevated heels).

All 9 planned L1 Pose Canon components are now approved. Gate 6 Pose components are complete.
