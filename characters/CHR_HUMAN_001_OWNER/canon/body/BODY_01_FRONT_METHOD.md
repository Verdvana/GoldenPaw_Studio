# BODY_01_FRONT — Approved Reproduction Method

```yaml
method_id: OWNER_BODY_01_FRONT_METHOD_V1
status: APPROVED_METHOD
approved_component: OWNER_BODY_01_FRONT_CANON_001
identity_revision: draft_0.35
body_revision: draft_0.12
spec_revision: draft_1.37
reference_set: OWNER_BODY_FRONT_RECOVERY_V1
output_status: REVIEW_REQUIRED
```

This method records the source/reference construction and user-reviewed corrections that produced the approved v008 front Body component. Ordinary L2/L3 front-view work should use the approved Master through `OWNER_BODY_FRONT_CANON_L1`. This method is only for recreating the L1 Master; every recreation returns to `REVIEW_REQUIRED` and requires new approval.

## Current approved Master

- asset: `OWNER_BODY_01_FRONT_CANON_001`
- path: `approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_001.jpg`
- format/dimensions: user-transcoded JPEG, 1086×1448, exact 3:4
- current JPG SHA-256: `86455eafd8917022a45323835bf693d24dd86b618caac581f018063a17963a57`
- source candidate: `BODY_01_FRONT_v008` PNG, SHA-256 `2f7f3828feb3a2e500482812a7a24f1284f87e71406b312ea579345293012a00`
- format note: the JPG is the active transfer-efficient downstream Master; the L1 recovery method remains source-derived and never chains either the JPG Master or candidate PNG
- lock status: `UNLOCKED_COMPONENT`; complete `owner_v1.0` is not locked

## Fixed minimal input order and roles

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`: exact recognizable front face, adult age, neutral expression and neutral skin appearance only; must not define body, outfit, hosiery, lighting or background.
2. `L0_OWNER_002` (`3.jpg`): primary real front standing context for stature, head-to-body scale, shoulder/torso length, waist/hip placement, limb length and natural stance range; must not define face, hair, qipao, shoes, umbrella, asymmetry, background or retouching.
3. `L0_OWNER_003` (`4.jpg`): cross-check for natural torso, waist, hip, thigh, calf and limb volumes; must not define walking pose, bags, dress, legwear, shoes, face, hair, environment or final body alone.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001`: Hairstyle A only; the mask carries no visual authority and the source must not define face, body, skin, clothing, lighting or background.

Never attach BODY_01 v001–v008, `OWNER_BODY_01_FRONT_CANON_001`, another generated Body asset, or a previous shot when recreating this L1 Master.

## Stable user-reviewed body contract

- natural adult body rather than a generic fashion model;
- leg share approximately 10% greater than the initial conservative source midpoint, then held unchanged through v008 review;
- front shoulders and torso retain natural volume;
- waist is modestly defined and narrower than v007, with a smooth lower-ribcage–waist–hip transition;
- no corset compression, tiny waist or exaggerated hourglass;
- natural chest and hip volume without enlargement or flattening;
- front leg direction is straight and balanced with natural calf volume;
- full head, hands, heels and toes remain inside the frame;
- even weight, square torso, relaxed arms, uncrossed legs and flat feet.

## Calibration presentation contract

- Hairstyle A from the scoped masked source;
- plain opaque pink high-cut one-piece athletic swimsuit;
- continuous light-nude 15D velvet-finish sheer pantyhose and no shoes;
- soft broad leg sheen, fine textile veil over feet/toes and muted burgundy polish beneath fabric;
- no toe seam, color band, reinforced/opaque toe, bare foot, latex, PVC or wet coating;
- these visible presentation properties do not transfer final material authority from Gate 7 into this Body component.

## Successful v008 prompt — preserve in intent

```text
Create one neutral full-length front-view technical character reference of the adult woman in Image 1. Images 2–3 provide natural body proportions only and Image 4 provides Hairstyle A only. Use no previous generated image.

Preserve the approved face, hairstyle and established natural body direction. Make only one body correction: reduce the waist width modestly at the natural waist and create a smoother, gently defined transition from lower ribcage through waist to hips. Keep realistic soft tissue and torso volume; no tiny waist, corset shape or exaggerated hourglass.

Hold the current leg length and straight parallel lower-leg direction. Standard calibration clothing: opaque plain pink high-cut one-piece athletic swimsuit, light nude closed-foot 15D velvet sheer tights, no shoes. Keep the subtle broad leg sheen and a soft translucent fabric veil over legs and feet; toe details and burgundy nail color remain gently muted beneath the fabric, with no toe seam or band.

Exact 3:4 full body, complete head, hands and feet, neutral gray-white seamless studio, soft even light and level lens-neutral camera. No other body changes, anatomy errors, props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.
```

## Output and QA controls

- built-in ImageGen, one candidate per approval cycle;
- preferred 1536×2048 or nearest native exact 3:4;
- 70–85mm-equivalent lens, level camera centered between waist and lower chest;
- neutral gray-white seamless studio and soft even 5200–5600K light;
- record output path, checksum, tool settings and QA;
- compare face, body geometry, leg share, waist width, calf axes, outfit and hosiery continuity separately;
- never auto-promote a recreation or edit this approved component in place.
