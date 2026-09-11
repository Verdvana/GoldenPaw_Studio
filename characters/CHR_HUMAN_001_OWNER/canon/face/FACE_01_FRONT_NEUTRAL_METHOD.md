# FACE_01_FRONT_NEUTRAL — Approved Reproduction Method

```yaml
method_id: OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1
status: APPROVED_METHOD
approved_component: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
identity_revision: draft_0.11
spec_revision: draft_1.11
reference_set: OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
output_status: REVIEW_REQUIRED
```

This method records the v010 face/skin success plus the v011 crown correction. It is used only when a new L1 `FACE_01_FRONT_NEUTRAL` must be recreated or recovered. Ordinary L2/L3 shots should use the approved Canon component directly as their identity master.

## Current downstream Master index

- approved asset: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
- current path: `approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
- current format/dimensions: user-transcoded JPEG, 1086×1448, exact 3:4
- current SHA-256: `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`
- approved source-candidate PNG SHA-256: `efda86babb6caeac5991515979e77ddf61e5a2776cd8e0819c9215b125d9f374`
- format note: the JPG is the active transfer-efficient downstream Master; L1 recovery still follows this method's source-derived inputs rather than transcoding or chaining the Master

## Minimal reference set and strict roles

1. `B_FACE_SKIN_CONTEXT_NO_CROWN.png`: exclusive authority for exact face, facial-feature relationships, natural face shape, apparent age, skin texture and warm-neutral skin tone. It must not define hair, crown, camera, clothes, lighting or background.
2. `DSC00847_HAIR_ONLY_MASKED.png`: exclusive authority for Hairstyle A front pixels. The gray oval means deleted information and must not define any visual property.

Never attach v005, v006, v010, v011 or any other generated Face candidate when recreating the L1 master.

## v010 face / skin block — preserve verbatim in intent

- reproduce the exact target face and all relationships among forehead, eyes, eyelids, eye spacing, eyebrows, nose, cheeks, lips, jaw and chin;
- preserve natural face width and proportions; add no widening, narrowing, slimming, fullness adjustment, V-line shaping, eye enlargement, nose refinement, jaw sharpening, chin pointing, age change or generic beautification;
- match warm-neutral skin hue, saturation, depth, luminance and natural texture; forbid whitening, cooling, brightening, pink cast, high-key washout and smoothing;
- neutral closed-mouth expression, direct gaze, no inherited B hairstyle or source lighting.

## Hairstyle A block

- very flat close-to-scalp roots and low crown;
- near-center naturally imperfect part and narrow upper silhouette;
- long straight loose dark-brown lengths with restrained density;
- fine separated strand groups, modest asymmetry, slim face-framing locks;
- tapered, wispy, slightly uneven ends;
- forbid dome volume, blowout, dense symmetric curtain, waves, curls, bun, updo, ponytail and long exposed scalp track.

## v011 crown / camera correction

- 105mm-equivalent lens from sufficient distance;
- corrective optical center approximately 4–5 cm below pupil midpoint and optical pitch upward approximately 2.5–3°;
- final image must still look visually neutral and eye-level, not low-angle;
- upright head/neck, neutral chin, gaze into lens;
- face, forehead, hairline, temples, ears, cranium, crown, jaw and chin share one projection;
- crown is seen mainly from the front; horizontal top surface is only a very narrow sliver;
- center part is visible only near the frontal roots and disappears after a short distance;
- forbid overhead oval crown, broad top-head patch, long backward scalp line, top-down skull, excessive crown proportion and face/crown angle mismatch.

## Output controls

- exact 3:4 portrait, preferred 1536×2048 or nearest native 3:4;
- standard centered head-to-upper-chest framing, full hair silhouette, modest headroom;
- plain pink Calibration Outfit upper portion if clothing is visible;
- neutral gray-white seamless studio, soft even 5200–5600K illumination;
- one candidate only, `REVIEW_REQUIRED`; never auto-promote or overwrite the current Canon;
- record seed/settings when available, final path, checksum and QA status.

## Required QA order

1. exact face and facial relationships;
2. skin depth and hue versus the B-derived input;
3. crown horizontal visible area and center-part length;
4. visual eye-level and lack of face/crown mismatch;
5. Hairstyle A construction;
6. expression, 3:4 framing, neutral light and absence of reference leakage.
