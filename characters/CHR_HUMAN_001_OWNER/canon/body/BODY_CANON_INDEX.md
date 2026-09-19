# Owner Body Canon Index

```yaml
index_id: OWNER_BODY_CANON_INDEX
character_id: CHR_HUMAN_001_OWNER
index_revision: 20
updated_at: "2026-09-19"
full_release_lock_status: UNLOCKED
approved_body_components: 6
```

## Current approved Masters

| Asset ID | View | Master | SHA-256 | Downstream set | L1 recovery method |
|---|---|---|---|---|---|
| `OWNER_BODY_01_FRONT_CANON_007` | front neutral standing, 168 cm / 60 kg target, narrower natural waist, straighter outer lower-leg contours, slightly-whitish continuous 15D hosiery and hazy burgundy toe polish | `approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png` | `90e021fcf5c72416b2b3c640c5fe2abe2d43c28e49da6dbabc250f73da306978` | `OWNER_BODY_FRONT_CANON_L1` | `BODY_01_FRONT_METHOD.md` |
| `OWNER_BODY_02_LEFT_3Q_CANON_002` | anatomical left 3/4 neutral standing, 168 cm / 60 kg target, neutral cervical stacking and lower legs brought forward into closer thigh-axis alignment | `approved/BODY_02_LEFT_3Q/OWNER_BODY_02_LEFT_3Q_CANON_002.png` | `8f887e81ffe517099fb9af25cf010f8dc33deeace9f8f55253b4641ac8876db1` | `OWNER_BODY_LEFT_3Q_CANON_L1` | source/reference responsibilities preserved in v003 record |
| `OWNER_BODY_03_RIGHT_3Q_CANON_002` | anatomical right 3/4 neutral standing, 168 cm / 60 kg target, Body01/06-aligned straight lower-leg axes | `approved/BODY_03_RIGHT_3Q/OWNER_BODY_03_RIGHT_3Q_CANON_002.png` | `2a18d38fb4441d50427753263700699a6ce2f571ae5a497720c8c4158fd658a7` | `OWNER_BODY_RIGHT_3Q_CANON_L1` | source/reference responsibilities preserved in v006 record |
| `OWNER_BODY_04_LEFT_SIDE_CANON_002` | anatomical left side neutral standing, 168 cm / 60 kg target, Body01/06-aligned geometry and straight loose HAIRSTYLE_A | `approved/BODY_04_LEFT_SIDE/OWNER_BODY_04_LEFT_SIDE_CANON_002.png` | `7c1c7f5eaf5699f4e39493ad4cfe120ee42497b2bc405137c901b87df843abd1` | `OWNER_BODY_LEFT_SIDE_CANON_L1` | source/reference responsibilities preserved in v003 record |
| `OWNER_BODY_05_RIGHT_SIDE_CANON_002` | anatomical right side neutral standing, 168 cm / 60 kg target, straight loose HAIRSTYLE_A and aligned lower-leg axes | `approved/BODY_05_RIGHT_SIDE/OWNER_BODY_05_RIGHT_SIDE_CANON_002.png` | `93a2dd69e4789878067943cca8b5f08ec849a39c140ed170f7e24d3e3e13d74b` | `OWNER_BODY_RIGHT_SIDE_CANON_L1` | source/reference responsibilities preserved in v003 record |
| `OWNER_BODY_06_BACK_CANON_004` | exact 180-degree back neutral standing aligned to current front Canon 007, corresponding high-cut opening and increased smooth heel translucency | `approved/BODY_06_BACK/OWNER_BODY_06_BACK_CANON_004.png` | `7bcaec66bf4ff9c4c4c2016d7578b2f88d79e3b3f9ec8502a24d0535d3007c0b` | `OWNER_BODY_BACK_CANON_L1` | source/reference responsibilities preserved in v006 record |

These are the six current active approved, unlocked L1 Body components. Their shared 168 cm / 60 kg target, visible face where applicable, `HAIRSTYLE_A`, limb proportions and waist/hip ratio may be referenced within each component's view scope. Dedicated view-specific Face/Hair Canon remains the preferred precision authority when applicable. Hosiery scope is strictly limited to the accepted `15D nude matte/velvet` appearance within each Body component; final reusable material authority remains Gate 7. Gate 3 is complete and Gate 4 is open, while the full `owner_v1.0` remains unlocked.

The v025 candidate PNG was moved unchanged to the approved path after explicit user approval as `OWNER_BODY_01_FRONT_CANON_007.png`. It is the active front Body Master. All superseded front rasters, including Canon 006 (from v017) and Canon 005, were returned to their original candidate directories on 2026-09-18; they are not active routing targets.

The v006 candidate PNG was moved unchanged to the approved path after explicit user approval as `OWNER_BODY_06_BACK_CANON_004.png`. It is the active back Body Master. All superseded back rasters, including Canon 003 and earlier components, were returned to their original candidate directories on 2026-09-18; they are not active routing targets.

The v003 candidate PNG was moved unchanged to the approved path after explicit user approval as `OWNER_BODY_02_LEFT_3Q_CANON_002.png`. It is the active left-three-quarter Body Master. Canon 001 was returned unchanged to `candidates/BODY_02_LEFT_3Q_v001/` as a superseded historical component and is not the active Body02 routing target.

The v006 candidate PNG was moved unchanged to the approved path after explicit user approval as `OWNER_BODY_03_RIGHT_3Q_CANON_002.png`. It is the active right-three-quarter Body Master. Canon 001 was returned unchanged to `candidates/BODY_03_RIGHT_3Q_v005/` as a superseded historical component and is not the active Body03 routing target.

The v003 candidate PNG was moved unchanged to the approved path after explicit user approval as `OWNER_BODY_05_RIGHT_SIDE_CANON_002.png`. It is the active right-side Body Master. Canon 001 was returned unchanged to `candidates/BODY_05_RIGHT_SIDE_v001/` as a superseded historical component and is not the active Body05 routing target.

The v003 candidate PNG was moved unchanged to the approved path after explicit user approval as `OWNER_BODY_04_LEFT_SIDE_CANON_002.png`. It is the active left-side Body Master. Canon 001 was returned unchanged to `candidates/BODY_04_LEFT_SIDE_v002/` as a superseded historical component and is not the active Body04 routing target.

Ordinary downstream work uses the active approved Master. L1 recreation uses `OWNER_BODY_FRONT_RECOVERY_V1` and the method document; it must never use either approved Master or any generated BODY_01 candidate as an image input.

## Superseded approved component

`OWNER_BODY_01_FRONT_CANON_001` remains a historically approved but superseded component in textual records only. Its former JPG raster and sidecar metadata were removed by the user during the 2026-09-12 single-file cleanup. The original approval evidence and checksums remain as provenance; there is no live path and it must not be selected as the current front Body Master.
