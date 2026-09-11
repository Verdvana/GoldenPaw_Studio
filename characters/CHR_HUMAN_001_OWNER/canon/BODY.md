# Owner Body Canon — Working Draft

```yaml
document_id: OWNER_BODY_CANON_WORKING
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
revision: draft_0.15
status: PARTIAL_APPROVED
calibration_outfit: OWNER_L1_CALIBRATION_OUTFIT
camera_setup: OWNER_BODY_NEUTRAL_STUDIO_V1
updated_at: "2026-09-11"
```

`OWNER_BODY_01_FRONT_CANON_002`, promoted from `BODY_01_FRONT_v009`, is the current active approved front-view Body L1 component. The user approved its face, Hairstyle A, limb proportions, waist/hip ratio, leg/foot geometry and visible hosiery presentation. `OWNER_BODY_01_FRONT_CANON_001` remains a superseded historical component. The remaining five Body views are still pending, and the complete `owner_v1.0` release remains unlocked.

For downstream character assets and shot/video-frame image generation, component 002 may define the approved 168 cm / 60 kg target, visible face appearance, `HAIRSTYLE_A`, limb proportions and waist/hip ratio. View-specific Face/Hair Canon remains the preferred precision reference when applicable. Its hosiery scope is narrower: it may define only `15D matte nude` appearance and must not define any other color, finish, material behavior or denier.

## Geometry contract pending BODY_01 review

- physical baseline: 168 cm and approximately 60 kg (120 jin), as explicitly confirmed by the user
- head-to-body ratio and stature impression: naturally tall 168 cm adult proportions, avoiding the approximately 160 cm impression of the current Master; no small-head fashion stylization, low-angle/wide-angle elongation or mechanical stretching
- shoulder width: natural, relaxed, and cross-checked across `3.jpg` and `4.jpg`; no narrowing or broadening by styling
- torso length and waist position: preserve the natural range visible across both real context images
- chest/waist/hip relationship: natural adult soft-tissue distribution; no exaggerated hourglass or flattening
- hip silhouette: conservative midpoint across real context, unaffected by dress flare or fitted fabric
- arm length: fingertips naturally reach the upper-to-mid thigh region; no shortening or model-like elongation
- thigh/calf relationship and leg length: natural 168 cm / 60 kg real-person proportions; do not inherit hosiery/shoe shaping or walking foreshortening
- lower-leg axes: both knee–shin–ankle centerlines near vertical and symmetric in front view, with natural calf volume but no outward-bowed shin or O-leg silhouette
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

- BODY_01 front — `OWNER_BODY_01_FRONT_CANON_002` APPROVED and active, component unlocked (`OWNER_BODY_01_FRONT_CANON_001` superseded)
- BODY_02 left 3/4 — pending
- BODY_03 right 3/4 — pending
- BODY_04 left side — pending
- BODY_05 right side — pending
- BODY_06 back — pending

## Authority boundary

Component 002 has an explicit user-expanded scope: its 168 cm / 60 kg stature, visible face, `HAIRSTYLE_A`, limb proportions and waist/hip ratio may be reused by other character assets and shot/video-frame images. This does not erase the more precise view-specific Face/Hair Canon. Its hosiery appearance is authoritative only for 15D matte nude; other colors, finishes, materials and deniers require their own selected material reference. It must not define side/rear geometry, episode wardrobe, background or lighting.

## Approved front Master routing

- downstream set: `OWNER_BODY_FRONT_CANON_L1`
- approved Master: `canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_002.png`
- recovery set: `OWNER_BODY_FRONT_RECOVERY_V1`
- reproduction method: `canon/body/BODY_01_FRONT_METHOD.md`
- rule: ordinary downstream work may use the active approved Master within its scope; L1 recreation must use the recovery set and method, never v008/v009, either approved Body Master or another generated Body image as a pixel input
