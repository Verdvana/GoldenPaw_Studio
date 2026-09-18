# BODY_01_FRONT — Approved Reproduction Method

```yaml
method_id: OWNER_BODY_01_FRONT_METHOD_V2
status: APPROVED_METHOD
approved_component: OWNER_BODY_01_FRONT_CANON_007
identity_revision: draft_0.184
body_revision: draft_0.20
spec_revision: draft_1.233
reference_set: OWNER_BODY_FRONT_RECOVERY_V1
output_status: REVIEW_REQUIRED
```

This method records the source/reference construction and user-reviewed corrections that produced the active approved v009 front Body component. Ordinary L2/L3 front-view work should use the active approved Master through `OWNER_BODY_FRONT_CANON_L1`. This method is only for recreating the L1 Master; every recreation returns to `REVIEW_REQUIRED` and requires new approval.

## User-scoped recovery override — 2026-09-17

For `BODY_01_FRONT_v010`, the user explicitly requires that no approved L1 Face raster be supplied as an image input. The face must be reconstructed from the source-derived Face recovery method instead, to avoid iterative-generation contamination. This override supersedes the Face-raster input in the fixed list below for this candidate only; it does not alter or deprecate the approved Face Canon.

Input order for this candidate:

1. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` — source-derived face/skin context only, following `FACE_01_FRONT_NEUTRAL_METHOD.md`; must not define hair, body, clothing, lighting or background.
2. `L0_OWNER_002` (`3.jpg`) — body context only.
3. `L0_OWNER_003` (`4.jpg`) — body volume cross-check only.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — Hairstyle A pixels only; masked area defines nothing.

This override also records the user's specific correction: the front lower legs should be visibly straight because the anatomy is straight, not because of a pose trick; knee, tibial shaft and ankle centers should track one near-vertical line on each side, with realistic calf mass and a naturally proportioned ankle that is not pinched or unnaturally thin.

## User-scoped geometry refinement — 2026-09-17 (v011)

The user further clarified that the visible tibial contour should not look bowed: in front view, the lower-leg bone/shaft silhouette is substantially straighter with only minimal natural soft-tissue variation. The inter-leg gap should be a small natural standing gap, not a wide separation. This refinement changes only lower-leg straightness and stance spacing; it does not redefine the user's body size, waist/hip ratio, face, hair or clothing.

## User-scoped hosiery refinement — 2026-09-17 (v012)

The user accepted the remaining body geometry and requested only these hosiery refinements: muted red/burgundy toenail polish should remain naturally visible beneath the sheer toe fabric; the light-nude hosiery should read slightly lighter than the underlying skin rather than darker; and the textile should show natural tension spanning the interdigital toe spaces, without seams, bands or bare gaps.

## User-scoped foot QA correction — 2026-09-17 (v013)

The user confirmed the face and Hairstyle A reconstruction are excellent and must retain the current source-derived generation method. Correct only the toe defects: each foot's second toe must have exactly one single, anatomically coherent nail plate; prohibit duplicated, split or extra nail shapes. Remove the incorrect transverse line at the toe roots; the hosiery must continue smoothly from each toe into the forefoot with natural interdigital tension, without a seam, hard boundary, ring or artificial crease.

## User-scoped lower-leg and color refinement — 2026-09-17 (v014)

The user clarified the intended front-view tibial path: each lower-leg shaft begins only slightly lateral to the knee/upper-shin line, follows a small gentle continuous curve inward, and returns to the central ankle axis. Do not create the previously seen large outward-to-center bow. Interdigital hosiery tension must be visibly readable between adjacent toes. Toenail polish is specifically deep burgundy/wine red, never pink.

## User-scoped waist and hosiery integration refinement — 2026-09-17 (v015)

The user accepted the current face and leg shape. Make the waist slightly narrower, with a normal continuous ribcage-to-waist-to-existing-hip-width transition; no corset compression, pinched waist or exaggerated hourglass. The leg covering must read as one continuous pale sheer textile from calf through ankle, forefoot and toes, with a soft hazy veil over the toes that matches the leg surface. Interdigital tension curves must be visible as textile stretch/valley responses, not bare-foot separations.

## User-scoped registration refinement — 2026-09-17 (v016)

The user explicitly approved BODY_01_FRONT_v016 for registration, highlighting that the hip and upper-thigh-root reconstruction is very accurate. The v016 candidate is now the active Master. Its substantially straighter front lower-leg axes, small natural inner-leg gap, pale slightly-whiter 15D hosiery, continuous toe veil and readable interdigital textile tension are retained within this component scope. The full owner release remains unlocked.

## User-scoped lower-leg axis refinement — 2026-09-17 (v017)

The user authorized one new `REVIEW_REQUIRED` candidate because the lower legs in v016 still read as insufficiently straight. Change only the front lower-leg geometry: each tibial shaft should descend almost collinearly with the thigh axis, with nearly no visible bend; the outer calf contour should continue close to the thigh's outer contour without a lateral bulge; the inner calf contours should nearly meet, leaving only a very narrow natural air gap so the legs never fuse or cross. Preserve the v016-approved waist/hip ratio, hip and upper-thigh-root reconstruction, face identity, Hairstyle A, pale slightly-whiter 15D hosiery appearance, interdigital textile tension, toe haze and burgundy polish. Do not use v016 pixels as a generation input; it remains comparison-only QA.

## User-scoped hosiery, volume and grounding refinement — 2026-09-17 (v018)

The user accepted the v017 lower-leg straightness and authorized a new `REVIEW_REQUIRED` candidate. Preserve the v017 calf axes and near-closed natural inner gap. Remove every artificial white ring or pale hard band at the toe roots. All burgundy toenails must remain under one continuous hosiery surface with a soft hazy veil and no exposed crisp nail edge. Reintroduce readable, natural textile tension curves converging between the toes; these are fabric valleys/stretch responses, never bare toe gaps or seams. Increase thigh and calf volume slightly while keeping the same natural adult proportions, and narrow the waist slightly with a smooth ribcage-to-waist-to-hip transition. Both feet must be fully planted: heel, forefoot and toes all rest on the floor; no tiptoe, heel lift, hovering heel or weight shifted onto the toes.

## User-scoped lower-leg contour reset — 2026-09-17 (v019)

The user accepted the v018 hosiery appearance but rejected its lower-leg geometry as still bowed and too far inside the thigh contour. Preserve v018 hosiery, leg volume, waist, toe coverage and full-foot grounding. Rebuild only the front lower-leg silhouette so each knee center, tibial shaft and ankle center are nearly collinear with the thigh axis; the visible outer calf edge should track almost flush with the same-side outer thigh edge as it descends, without inward taper that makes the calf look bowed and without outward O-leg bulge. Keep a tiny natural inner gap; never fuse or cross the legs.

## Current approved Master

- asset: `OWNER_BODY_01_FRONT_CANON_007`
- path: `approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png`
- format/dimensions: PNG, 1086×1448, exact 3:4
- current PNG SHA-256: `90e021fcf5c72416b2b3c640c5fe2abe2d43c28e49da6dbabc250f73da306978`
- source candidate: `BODY_01_FRONT_v025`, moved unchanged to the approved path after explicit approval
- superseded components: `OWNER_BODY_01_FRONT_CANON_001` through `OWNER_BODY_01_FRONT_CANON_006`; retain for history but do not route as current
- lineage note: the L1 recovery method remains source-derived and never chains either approved Master or any candidate pixels
- lock status: `UNLOCKED_COMPONENT`; complete `owner_v1.0` is not locked

## User-scoped body and toe correction — `BODY_01_FRONT_v020` (2026-09-18)

The user authorized one new independent candidate. Preserve the v019-approved near-vertical leg axes, outer-leg continuity, flat-foot grounding, face recovery method, Hairstyle A, calibration outfit and continuous 15D hosiery intent. Reduce the waist width by approximately 5% with a smooth ribcage-to-waist-to-hip transition, and increase overall leg soft-tissue volume by approximately 5% across thighs and calves without changing stature, knee/ankle alignment or creating an exaggerated hourglass. The lower legs remain nearly collinear and straight in front view.

Toe hosiery is a hard QA gate: one continuous sheer textile must cover every toe and every toenail, with no exposed crisp nail edge, uncovered nail, white line, white ring, reinforced-toe boundary, hard band, bare toe gap or material discontinuity. Burgundy toenails may show only as a low-saturation diffuse signal beneath the textile. Interdigital separations must read as natural V-shaped fabric tension valleys/convergence, not painted lines or bare skin. This candidate returns to `REVIEW_REQUIRED` and must not be promoted automatically.

## User-scoped v025 refinement and approval — 2026-09-18

The user requested a narrower waist, further straightening of the lower legs, and removal of all toe-root color segmentation. The approved v025 candidate keeps the native exact 3:4 output and uses only the source-derived recovery inputs. Its approved scope includes a smoother narrower waist, outer calf contours descending almost directly from the outer thigh contours, slightly-whitish continuous 15D hosiery, hazy burgundy polish beneath the textile and readable interdigital fabric tension. The user explicitly approved v025 and it was moved unchanged to `OWNER_BODY_01_FRONT_CANON_007`; future recreation remains source-derived and must not use this approved raster as a generation input.

## Fixed minimal input order and roles

1. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001`: source-derived Face recovery input for recognizable front face, adult age, neutral expression and neutral skin appearance only; must not define body, outfit, hosiery, lighting or background. The approved Face Canon may be used only for post-generation QA comparison, never as an image input.
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
