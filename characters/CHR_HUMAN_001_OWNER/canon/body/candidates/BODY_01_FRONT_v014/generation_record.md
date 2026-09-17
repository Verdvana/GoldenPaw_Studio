# BODY_01_FRONT_v014 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.222
identity_md_revision: draft_0.39
body_md_revision: draft_0.16
method_id: OWNER_BODY_01_FRONT_METHOD_V2
user_scoped_override: "2026-09-17 source-derived Face recovery; no L1 Face raster; v014 tibial path, interdigital tension and burgundy color refinement"
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v014
gate: "Gate 3 — Body Canon"
model_tool: built-in image_gen
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
  - OWNER_L0_BODY_FRONT_CONTEXT
reference_count: 4
previous_ai_reference_count: 0
face_l1_raster_supplied: false
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v014/BODY_01_FRONT_v014.png"
qa_status: PASS_TECHNICAL_PRECHECK_REVIEW_REQUIRED
checksum_sha256: 8c0b157adc23c078b44f3a1dc508defb253d89551d1a96c7f0919b2dfc698a6b
```

## Reference responsibilities

1. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` — source-derived face/skin only; retain the current successful Face recovery method.
2. `L0_OWNER_002` (`3.jpg`) — natural stature and body-proportion context only.
3. `L0_OWNER_003` (`4.jpg`) — torso, waist, hip, thigh, calf and limb-volume cross-check only.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — retain the current successful Hairstyle A method; hair only, masked area defines nothing.

No approved Face raster, approved Body Master, BODY_01 v001–v013, previous shot or other generated image is supplied.

## Prompt assembly

```text
Use case: identity-preserve, clinical anthropometric reference.
Create exactly one neutral, non-sexual, full-length 3:4 straight-on front-view technical body-proportion calibration plate of the same adult woman. Reconstruct in parallel only from the declared source-derived references.

Image 1 is source-derived face/skin context from the FACE_01 recovery method. Preserve the current successful face reconstruction method exactly: recognizable face, natural facial relationships, realistic warm-neutral skin, direct gaze and closed mouth. Do not use any approved L1 Face image or generated face.
Image 4 is the face-masked Hairstyle A source. Preserve the current successful Hairstyle A method exactly: long straight dark-brown hair, near-center part, low crown and natural tapered lengths. The gray mask defines nothing.
Images 2–3 define body context only; ignore their faces, hair, clothing, shoes, props, environments and retouching.

Preserve the accepted 168 cm / approximately 60 kg adult proportions, torso, waist/hip ratio, natural calf volume, pink calibration one-piece, pale light-nude 15D sheer textile leg covering, flat feet and small natural inner-leg gap.

Critical tibial geometry: in the straight-on front view, each lower-leg shaft starts only slightly lateral to the corresponding knee center/upper-shin line. From the knee downward it follows one small, gentle, continuous inward curve and returns gradually to the central ankle axis. The path must be near-straight overall, with only a mild anatomical deviation. Absolutely no large outward bow, no dramatic lateral knee-to-center sweep, no O-leg silhouette, no sharp kink, no inward collapse and no displaced ankles. Keep the two paths symmetric and parallel in overall character, with ordinary adult ankle width.

Foot and hosiery QA: each foot has five normal toes. Each second toe has exactly one single intact nail plate, never duplicated, split, stacked or extra. Toenail polish is deep burgundy/wine red, clearly distinct from pink, and visible softly only beneath the sheer textile, never painted on top. The hosiery is slightly lighter than the underlying skin and continuous over every toe and onto the forefoot. Make interdigital hosiery tension visibly readable: between each pair of adjacent toes, show a subtle narrow V-shaped fabric valley/stretch line following the toe separation, with the textile visibly spanning the gap. This is fabric tension, not a seam or bare crease. No transverse line across the toe roots, no horizontal stripe, no toe-cap boundary, no hard ring, no bare gaps, no duplicated nails, no fused toes, no extra toes, no latex, PVC, plastic, wet coating or body paint.

Keep feet flat, stable, uncrossed and approximately parallel. Neutral gray-white seamless studio, soft even 5200–5600K light, level 70–85mm-equivalent camera centered between waist and lower chest. Complete head, hands, heels and toes with 5–8% breathing room, square torso, relaxed arms and neutral direct gaze. No props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.
```

## QA checklist

- current successful Face and Hairstyle A source-derived methods preserved
- no L1 Face or generated Body pixel input
- tibia starts only slightly lateral at knee and makes a mild inward curve, never a large bow
- small natural inter-leg gap preserved
- visible interdigital fabric tension without seam or toe-root line
- exactly one nail plate on each second toe and no duplicate nails
- deep burgundy/wine-red polish, not pink, beneath the fabric
- pale continuous hosiery, correct body proportions, framing and foot contact

## Attempt result and QA

- generated_at: 2026-09-17
- built-in output saved to the project candidate path as a unique candidate raster.
- lower-leg geometry: the knee-to-ankle path now begins only slightly lateral and returns with a mild continuous curve; the prior large bow is not observed in the full-frame precheck.
- hosiery/toe precheck: interdigital textile tension is visible; no duplicated second-toe nail or transverse toe-root line is observed; polish reads deep burgundy/wine red rather than pink.
- face and Hairstyle A: preserved using the successful source-derived methods.
- approval remains `REVIEW_REQUIRED`; no promotion or Canon replacement occurred.
