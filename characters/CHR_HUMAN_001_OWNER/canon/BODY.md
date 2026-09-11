# Owner Body Canon — Working Draft

```yaml
document_id: OWNER_BODY_CANON_WORKING
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
revision: draft_0.12
status: PARTIAL_APPROVED
calibration_outfit: OWNER_L1_CALIBRATION_OUTFIT
camera_setup: OWNER_BODY_NEUTRAL_STUDIO_V1
updated_at: "2026-09-11"
```

`OWNER_BODY_01_FRONT_CANON_001`, promoted from `BODY_01_FRONT_v008`, is the approved front-view Body L1 component. The remaining five Body views are still pending, and the complete `owner_v1.0` release remains unlocked.

## Geometry contract pending BODY_01 review

- head-to-body ratio: derive conservatively from registered real full-body context; no height or leg-length enhancement
- shoulder width: natural, relaxed, and cross-checked across `3.jpg` and `4.jpg`; no narrowing or broadening by styling
- torso length and waist position: preserve the natural range visible across both real context images
- chest/waist/hip relationship: natural adult soft-tissue distribution; no exaggerated hourglass or flattening
- hip silhouette: conservative midpoint across real context, unaffected by dress flare or fitted fabric
- arm length: fingertips naturally reach the upper-to-mid thigh region; no shortening or model-like elongation
- thigh/calf relationship and leg length: natural real-person proportions; do not inherit hosiery/shoe shaping or walking foreshortening
- foot proportions: anatomically natural and consistent with body scale; no shoe-derived foot shape

## BODY_01 front contract

- squarely front-facing, neutral head and torso, weight distributed evenly;
- arms relaxed with a small readable gap from the torso, hands open and fingers natural;
- legs uncrossed, feet flat and approximately parallel with only slight natural toe-out;
- complete head top, hands, legs, heels and toes visible;
- 70–85mm-equivalent perspective, camera between waist and lower chest, level optical axis;
- neutral gray-white seamless studio, soft 5200–5600K illumination;
- exact Calibration Outfit: pink high-cut one-piece swimsuit, continuous nude 15D velvet-finish sheer pantyhose, no shoes;
- HAIRSTYLE_A and approved front Face identity remain scoped authorities and are not redefined by Body approval.
- presentation is an adult, non-sexual, technical character-proportion calibration reference; hosiery is text-specified for this Body candidate and its detailed material authority remains Gate 7.

## Required neutral views

- BODY_01 front — `OWNER_BODY_01_FRONT_CANON_001` APPROVED, component unlocked
- BODY_02 left 3/4 — pending
- BODY_03 right 3/4 — pending
- BODY_04 left side — pending
- BODY_05 right side — pending
- BODY_06 back — pending

## Authority boundary

Approved Body images will define body geometry only. They must not independently redefine face identity, hairstyle design, hosiery material, Calibration Outfit design, skin color, or episode wardrobe.

## Approved front Master routing

- downstream set: `OWNER_BODY_FRONT_CANON_L1`
- approved Master: `canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_001.jpg`
- recovery set: `OWNER_BODY_FRONT_RECOVERY_V1`
- reproduction method: `canon/body/BODY_01_FRONT_METHOD.md`
- rule: ordinary downstream work may use the approved Master for front body geometry; L1 recreation must use the recovery set and method, never v008 or the approved Master as a pixel input
