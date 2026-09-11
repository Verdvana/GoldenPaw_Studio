# BODY_01_FRONT — Approved Reproduction Method

```yaml
method_id: OWNER_BODY_01_FRONT_METHOD_V2
status: APPROVED_METHOD
approved_component: OWNER_BODY_01_FRONT_CANON_002
identity_revision: draft_0.38
body_revision: draft_0.15
spec_revision: draft_1.40
reference_set: OWNER_BODY_FRONT_RECOVERY_V1
output_status: REVIEW_REQUIRED
```

This method records the source/reference construction and user-reviewed corrections that produced the active approved v009 front Body component. Ordinary L2/L3 front-view work should use the active approved Master through `OWNER_BODY_FRONT_CANON_L1`. This method is only for recreating the L1 Master; every recreation returns to `REVIEW_REQUIRED` and requires new approval.

## Current approved Master

- asset: `OWNER_BODY_01_FRONT_CANON_002`
- path: `approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_002.png`
- format/dimensions: PNG, 1086×1448, exact 3:4
- current SHA-256: `cbb08e1799a6d6d3d9e00b600ceaab294a36a2b04a170ae1a367e28578cd0164`
- source candidate: `BODY_01_FRONT_v009`, moved to the approved path after explicit approval
- superseded component: `OWNER_BODY_01_FRONT_CANON_001`; retain for history but do not route as current
- lineage note: the L1 recovery method remains source-derived and never chains either approved Master or any candidate pixels
- lock status: `UNLOCKED_COMPONENT`; complete `owner_v1.0` is not locked

## Fixed minimal input order and roles

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`: exact recognizable front face, adult age, neutral expression and neutral skin appearance only; must not define body, outfit, hosiery, lighting or background.
2. `L0_OWNER_002` (`3.jpg`): primary real front standing context for stature, head-to-body scale, shoulder/torso length, waist/hip placement, limb length and natural stance range; must not define face, hair, qipao, shoes, umbrella, asymmetry, background or retouching.
3. `L0_OWNER_003` (`4.jpg`): cross-check for natural torso, waist, hip, thigh, calf and limb volumes; must not define walking pose, bags, dress, legwear, shoes, face, hair, environment or final body alone.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001`: Hairstyle A only; the mask carries no visual authority and the source must not define face, body, skin, clothing, lighting or background.

Never attach BODY_01 v001–v009, `OWNER_BODY_01_FRONT_CANON_001`, `OWNER_BODY_01_FRONT_CANON_002`, another generated Body asset, or a previous shot when recreating this L1 Master.

## Stable user-reviewed body contract

- user-confirmed physical target: 168 cm and approximately 60 kg (120 jin);
- natural adult body rather than a generic fashion model, with coherent tall stature conveyed by head-to-body, torso and limb relationships rather than camera distortion or mechanical stretching;
- front shoulders and torso retain natural volume;
- waist/hip ratio and the smooth lower-ribcage–waist–hip transition are accepted as shown in v009;
- no corset compression, tiny waist or exaggerated hourglass;
- natural chest and hip volume without enlargement or flattening;
- front arm/leg/foot proportions are accepted as shown in v009;
- both knee–shin–ankle axes are straight, symmetric and balanced with natural calf volume and no O-leg impression;
- full head, hands, heels and toes remain inside the frame;
- even weight, square torso, relaxed arms, uncrossed legs and flat feet.

## Calibration presentation contract

- Hairstyle A from the scoped masked source;
- plain opaque pink high-cut one-piece athletic swimsuit;
- continuous light-nude 15D velvet-finish sheer pantyhose and no shoes;
- soft broad leg sheen, fine textile veil over feet/toes and muted burgundy polish beneath fabric;
- no toe seam, color band, reinforced/opaque toe, bare foot, latex, PVC or wet coating;
- the user approved the visible leg/foot hosiery presentation only as a `15D matte nude` reference; every other color, finish/material behavior or denier must exclude this appearance and use its own material reference.

## Successful v009 prompt — preserve in intent

```text
Create exactly one neutral full-length front-view technical character reference of the adult woman whose front face identity is defined only by Image 1. Images 2–3 provide real-person body context only, and Image 4 defines Hairstyle A only. Use no previous generated Body image or approved Body Master.

The user's physical measurement is authoritative: 168 cm, 60 kg (120 jin). Reproduce the coherent natural proportions and visual stature of that adult body, with the approved face, Hairstyle A, shoulder/torso volume, waist/hip ratio and realistic soft tissue. Express stature through head-to-body, torso and limb relationships; no small-head fashion stylization, wide-angle/low-angle elongation or mechanical stretching.

Both legs must be anatomically straight in front view: knee centers, tibial axes and ankle centers near-vertical, symmetric and parallel, with natural calf volume and no outward-bowed/O-leg silhouette. Feet remain flat and approximately parallel.

Standard calibration clothing: opaque plain pink high-cut one-piece athletic swimsuit, continuous light-nude closed-foot 15D velvet-finish sheer pantyhose, no shoes. Preserve the accepted subtle broad sheen and translucent textile veil through thighs, knees, calves, ankles, heels, insteps and toes; muted burgundy polish may show beneath the fabric. No toe seam, color band, reinforced toe, bare toes, latex, PVC, plastic, wet coating or body paint.

Exact 3:4 full body with complete head, hands, heels and toes, neutral gray-white seamless studio, soft even 5200–5600K light and a level 70–85mm-equivalent camera centered between waist and lower chest. Square torso, even weight, relaxed arms and uncrossed legs. No other identity, hairstyle, outfit, material or anatomy changes; no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.
```

## Output and QA controls

- built-in ImageGen, one candidate per approval cycle;
- preferred 1536×2048 or nearest native exact 3:4;
- 70–85mm-equivalent lens, level camera centered between waist and lower chest;
- neutral gray-white seamless studio and soft even 5200–5600K light;
- record output path, checksum, tool settings and QA;
- compare face, body geometry, leg share, waist width, calf axes, outfit and hosiery continuity separately;
- never auto-promote a recreation or edit this approved component in place.
