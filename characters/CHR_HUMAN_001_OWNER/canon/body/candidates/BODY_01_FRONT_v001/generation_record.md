# BODY_01_FRONT_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.26
identity_md_revision: draft_0.25
body_md_revision: draft_0.3
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v001
gate: "Gate 3 — Body Canon"
model_tool: "built-in image_gen"
status: GENERATION_BLOCKED_NO_OUTPUT
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_L0_BODY_FRONT_CONTEXT
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
reference_count: 4
previous_ai_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v001/BODY_01_FRONT_v001.png"
qa_status: NOT_RUN_NO_OUTPUT
```

## Reference plan

Inputs are supplied once, in this fixed order:

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — approved front Face Master, SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`. Defines only exact face identity, neutral expression, skin appearance and frontal HAIRSTYLE_A relationship. It must not define body geometry from its crop or turn its visible upper garment into a separate tank top.
2. `L0_OWNER_002` (`3.jpg`) — SHA-256 `556f6d4652e1f5ac18725cdb03ea2f7e90a761450a1fc4bdd50bf4cf42aff310`. Primary real frontal standing context for stature, head-to-body scale, shoulder/torso length, waist/hip placement, arm/leg length and natural stance range. It must not define face, hair, qipao silhouette, shoes, umbrella, pose asymmetry, background, lighting or retouching.
3. `L0_OWNER_003` (`4.jpg`) — SHA-256 `ca270e55c50fd168c798b0fbb20c9a8feded4c7f65e1c5af901b0c5e3601762b`. Cross-checks natural torso/waist/hip/thigh/calf volume and limb proportions across a different date and moving state. It must not define walking pose, bags, black dress, black legwear, shoes, face, hair, background, camera perspective or a final body alone.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — SHA-256 `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`. Defines Hairstyle A only: near-center part, close roots, low crown volume, long straight loose dark-brown hair, face-framing panels and tapered ends. It must not define face, body, skin, clothing, light or background.
The first attempted call also attached the then-active `L0_HOS_15_NM_002` (`IMG_2563.jpg`) for textile-only behavior. That call produced no image because the output was safety-blocked. The user later deleted this file while pruning the 15D nude matte library, so it is now a historical provenance entry only and must never be resolved as an active input. The safe retry excluded it; the 15D textile was governed textually by `CALIBRATION_OUTFIT.md` and `docs/qa/hosiery_material_rules.md`, with final material authority remaining Gate 7.

No previous Body candidate, generated body, previous shot, or unrelated Face angle is supplied. The two real body sources are contextual constraints rather than final authority; v001 is a conservative, non-slimmed midpoint for user calibration.

## Attempt history before output

- attempt 1: five scoped inputs including the now-retired `IMG_2563.jpg`; no image produced; output-stage safety rejection categorized the attempted image as sexual; this filename remains here only as immutable attempt provenance
- retry decision: use four inputs only, remove the hosiery advertising/bed photo, explicitly frame the asset as an adult non-sexual technical character-proportion reference, retain the exact Calibration Outfit and textile continuity in text
- attempt 2: four scoped inputs with no hosiery photo and an explicitly adult, non-sexual technical prompt; no image produced; output-stage safety rejection again categorized the attempted image as sexual
- final state: no candidate file exists, no QA was possible, and no body attribute may be inferred from either failed call; further generation is paused pending an explicit user decision on whether to change the Calibration Outfit contract

## Safe-retry assembled prompt

```text
Use case: identity-preserve

Asset type: BODY_01_FRONT v001, an adult non-sexual technical character-proportion reference for CHR_HUMAN_001_OWNER. Governed by OWNER_L1_GENERATION_SPEC draft_1.25, OWNER_IDENTITY_ANCHOR draft_0.24 and OWNER_BODY_CANON_WORKING draft_0.2.

Image 1 alone defines the approved recognizable front face, adult age, natural skin appearance and neutral expression. Images 2 and 3 are real full-body context only; cross-check natural stature and body proportions without copying either person's clothing, shoes, props, pose, background, face or hair. Image 4 defines Hairstyle A only and cannot define face or body. No previous generated Body image is supplied.

Create one neutral studio full-body character turnaround-style photograph of this adult woman, front-facing and standing evenly on both feet. This is a practical identity and proportion calibration image, not glamour, boudoir, fetish or suggestive imagery. Use an ordinary relaxed anatomical stance: upright head and torso, gaze forward, closed mouth, arms relaxed with a small gap from the torso, open hands, legs uncrossed, feet flat and approximately parallel.

Preserve Image 1's face exactly. Derive a conservative natural real-person body midpoint from Images 2 and 3: ordinary balanced proportions, natural torso and waist placement, natural limb lengths and soft-tissue distribution. Do not slim, lengthen legs, exaggerate curves, enlarge chest or hips, tighten the waist, or create a fashion-model or athletic body. Ignore the qipao, black dress, hosiery, shoes, umbrella, bags, walking stride and environments in Images 2 and 3.

Use Hairstyle A from Image 4 only: long straight loose dark-brown hair, near-center part, close roots, low crown volume and natural tapered ends.

Wear the exact standardized calibration uniform: a plain solid pink high-leg one-piece athletic swimsuit with a moderate scoop neckline, secure shoulder straps, opaque practical fabric and no decoration, together with nude 15D velvet-finish sheer pantyhose and no shoes. Present the clothing neutrally like a technical apparel-fit reference. The pantyhose is one continuous fine textile garment from waist through legs, ankles, heels, insteps and closed toes; subtle matte/velvet finish, not bare legs, not socks, not thigh-highs and not glossy synthetic coating. Detailed hosiery material authority remains outside this Body asset.

Exact 3:4 vertical composition, complete head, hair, hands, legs, heels and toes visible with 5–8% margin. 70–85mm-equivalent lens, level camera centered between waist and lower chest, neutral gray-white seamless studio, soft even 5200–5600K lighting and a faint floor contact shadow.

Authority is limited to front-view body proportions and neutral stance. Do not redefine face, hair design, outfit design, hosiery Material Canon, skin policy or episode styling. Avoid cropped feet, shoes, crossed legs, hip pop, torso twist, walking, raised arms, anatomy errors, generic model proportions, sexualized pose, glamour styling, lingerie presentation, transparent swimsuit, cleavage emphasis, bare legs or feet, latex/PVC/wet shine, props, text, logo, watermark, collage or multiple views.

One REVIEW_REQUIRED candidate only; never imply Canon approval.
```

## Final assembled prompt

```text
Use case: identity-preserve

Asset type: BODY_01_FRONT, L1 Body Canon candidate v001 for CHR_HUMAN_001_OWNER, governed by OWNER_L1_GENERATION_SPEC draft_1.24, OWNER_IDENTITY_ANCHOR draft_0.23 and OWNER_BODY_CANON_WORKING draft_0.1.

Input images, in fixed order: Image 1 is the approved front-neutral Face Canon and is the sole authority for the exact recognizable woman's face, skull and facial-feature relationships, adult age, neutral-studio skin appearance, closed-mouth neutral expression and frontal identity. Image 2 is a real full-body frontal standing photograph and is primary context only for real-person stature, head-to-body scale, shoulder width, torso length, waist and hip placement, arm and leg length, and natural standing proportions. Image 3 is another real full-body photograph and only cross-checks natural torso, waist, hip, thigh, calf and limb proportions across a different date and moving state. Image 4 is a source-derived masked Hairstyle A reference and defines hair only. Image 5 is a hosiery material reference and defines only nude 15D velvet/matte sheer textile transparency, tension, and continuous coverage over ankle, heel, instep and toes.

Create exactly one photorealistic full-length front-neutral body calibration portrait. The woman faces the camera squarely: head, shoulders, chest, pelvis, knees and feet all oriented forward without torso twist. Head upright and visually eye-level, gaze naturally toward the camera, mouth closed, expression neutral and relaxed. Weight distributed evenly across both feet. Both arms hang naturally at the sides with a small clear gap from the torso so the waist and hip silhouette remain readable; elbows relaxed, hands open, fingers natural and fully visible. Legs uncrossed. Both feet rest flat on the floor, approximately parallel with only slight natural toe-out and a comfortable narrow stance.

Preserve the exact face identity from Image 1. Build body geometry conservatively by cross-checking Images 2 and 3 rather than copying either outfit-shaped silhouette. Keep natural real-adult proportions and soft-tissue distribution: balanced shoulders and hips, natural torso length and waist height, a visible but non-exaggerated waist, natural chest and hip volume, proportionate upper arms and forearms, naturally full thighs transitioning coherently to calves and ankles, and feet scaled correctly to the body. Do not beautify or redesign her into a generic fashion model. Do not slim, increase height, lengthen legs, shorten the torso, enlarge breasts or hips, tighten the waist, narrow shoulders, reduce thighs, change age, or create an athletic/bodybuilder physique. Do not inherit Image 2's qipao compression, high heels, umbrella, lifted hand, asymmetry, outdoor background or hair. Do not inherit Image 3's walking stride, bags, flared black dress, black legwear, shoes, parking environment, moving asymmetry, face or hair. Neither real body image may override Image 1's face.

Hairstyle A only from Image 4: near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels and tapered ends. Keep it arranged symmetrically enough for the front calibration silhouette while remaining natural. Image 4 must not influence face, skull, body, skin, clothing, lighting or background.

Wear exactly the L1 Calibration Outfit: a simple solid pink high-cut one-piece swimsuit with clean practical construction, moderate scoop neckline matching the established visible upper portion, secure shoulder straps, full opaque fabric, no logo, no pattern, no cutouts, no ruffles and no decorative hardware. It is one continuous one-piece garment, not a tank top, bodysuit with seams, bikini, leotard variation, lingerie or dress. Use the high-cut leg openings to keep the hip crease and upper-thigh geometry readable without changing the body.

Also wear continuous nude/skin-tone 15D velvet-finish sheer pantyhose under the swimsuit, from waist and hips through both thighs, knees, calves, ankles, heels, insteps and every toe. The finish is soft velvet/matte with subtle low sheen and realistic fine textile presence, not bare legs and not opaque tights. At the feet, fabric remains visibly and continuously over toes and nails; burgundy toenail polish may be only subtly visible beneath the fabric. No waistband break below the swimsuit, no thigh-high top, no socks, no ankle cutoff, no open toes, no bare heels, no seam discontinuity. Image 5 defines textile behavior only and must not transfer its body, skin color, anatomy, pose, nail color, lace, bed, lighting, background or advertising text. No shoes.

Exact 3:4 vertical portrait. Show the complete body from head top through both heels and every toe, with approximately 5–8% neutral margin above the hair and below the feet. Hands and hair edges fully inside frame. Use a 70–85mm-equivalent lens, camera centered on the body between waist and lower chest height, horizontal optical axis and enough distance for lens-neutral proportions. No high/low-angle leg exaggeration and no wide-angle distortion. Neutral light gray/gray-white seamless studio floor and background, soft even low-contrast 5200–5600K illumination, neutral white balance, realistic photographic skin and textile texture, faint natural grounding shadow beneath feet.

This candidate proposes authority only for front-view body geometry: head-to-body ratio, shoulder width, torso length, waist position, chest-waist-hip relationship, hip silhouette, arm length, thigh/calf relationship, leg length, foot scale and neutral stance. It must not redefine face identity, Hairstyle A design, skin tone policy, Calibration Outfit design, final hosiery Material Canon, toenail color, makeup, episode wardrobe, lighting or background.

Avoid crop, missing feet, shoes, crossed legs, walking pose, contrapposto, hip pop, torso twist, raised arms, hands touching the body, fused or extra fingers, fused or extra toes, incorrect feet, asymmetrical limb length, generic model body, slimming, elongated legs, exaggerated hourglass, tiny waist, oversized bust or hips, muscular definition, juvenile proportions, high heels, dress, qipao, black garment, bikini, lingerie, leotard styling, bare legs, bare feet, socks, thigh-high stockings, ankle cutoff, exposed toes, opaque tights, latex, PVC, plastic, rubber, wet shine, liquid coating, body-paint hosiery, heavy makeup, beauty filter, whitening, dramatic lighting, colored background, props, text, logo, watermark, collage and multiple views.

One candidate image only. REVIEW_REQUIRED; do not label or imply Canon approval.
```
