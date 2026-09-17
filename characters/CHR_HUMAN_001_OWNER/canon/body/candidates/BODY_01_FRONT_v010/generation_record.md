# BODY_01_FRONT_v010 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.222
identity_md_revision: draft_0.39
body_md_revision: draft_0.16
method_id: OWNER_BODY_01_FRONT_METHOD_V2
user_scoped_override: "2026-09-17 source-derived Face recovery; no L1 Face raster"
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v010
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v010/BODY_01_FRONT_v010.png"
qa_status: UNREVIEWED
```

## Reference responsibilities and exclusions

1. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` — face geometry, facial-feature relationships, natural age/skin appearance and warm-neutral tone only; must not define hair, body, clothing, lighting or background.
2. `L0_OWNER_002` (`3.jpg`) — stature, head-to-body scale, shoulder/torso length, waist/hip placement, limb length and natural standing context only; must not define face, hair, clothing, shoes, props, background or retouching.
3. `L0_OWNER_003` (`4.jpg`) — natural torso, waist, hip, thigh, calf and limb-volume cross-check only; must not define face, hair, outfit, legwear, shoes, environment or final body alone.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — Hairstyle A pixels only; masked/deleted regions define no face, body, skin, clothing, lighting or background.

No approved Face raster, approved Body Master, BODY_01 v001–v009, previous shot or other generated image is supplied.

## Prompt assembly

```text
Use case: identity-preserve
Asset type: BODY_01_FRONT L1 technical character-proportion calibration candidate for CHR_HUMAN_001_OWNER
Input images: Image 1 is the source-derived face/skin context from the approved FACE_01 recovery method; Image 2 and Image 3 are real-person body-context references only; Image 4 is the face-masked Hairstyle A reference only.

Create exactly one neutral full-length front-view technical reference of the same adult woman, reconstructed in parallel from the declared source-derived inputs. Do not use or imitate any approved L1 Face raster, approved Body Master, previous Body candidate, previous shot or any other generated image. The face must follow the FACE_01_FRONT_NEUTRAL_METHOD: natural recognizable facial relationships, warm-neutral realistic skin, neutral closed mouth, direct gaze, and visually eye-level projection; no generic beautification or iterative-generation artifacts.

The user's physical baseline is authoritative: 168 cm and approximately 60 kg. Show coherent natural proportions of a relatively tall adult woman at that baseline, using head-to-body ratio, torso length, hip/waist placement and limb lengths, not a small head, wide-angle lens, low camera, mechanical stretching or fashion-model exaggeration. Preserve natural shoulder, chest, waist, hip, thigh and calf soft-tissue volume and the accepted waist-to-hip relationship.

Correct the lower legs as an anatomical geometry issue, not a pose change. In this straight-on front view, each knee center, tibial shaft and ankle center must align on one nearly vertical, symmetric axis from thigh through shin to ankle. Both lower legs are straight and parallel, with no outward bow, O-leg impression, inward collapse or displaced ankle. Keep realistic calf volume through the muscle belly; do not make the calves or ankles unnaturally narrow. The ankle should have natural adult width and a smooth transition into the foot. Feet are flat, stable, evenly weighted, uncrossed and approximately parallel.

Use Hairstyle A only, following the masked hair reference. Calibration outfit: plain opaque pink high-cut one-piece athletic swimsuit, continuous light-nude 15D velvet-finish sheer closed-foot pantyhose, no shoes. Pantyhose must remain one continuous textile from thigh to knee, calf, ankle, heel, instep and toes, with a subtle broad matte/velvet sheen and muted burgundy polish only naturally beneath the fabric. No seam, color band, reinforced toe, bare toes, latex, PVC, plastic, wet coating or body paint.

Exact 3:4 portrait, complete head, hands, heels and toes with 5–8% breathing room, neutral gray-white seamless studio, soft even 5200–5600K light, level 70–85mm-equivalent camera centered between waist and lower chest. Square torso, relaxed arms, neutral expression, no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.
```

## QA checklist

- face reconstruction follows source-derived Face method; no L1 Face pixel contamination
- face identity and eye-level/crown projection remain coherent
- 168 cm / 60 kg stature impression without lens or stretch distortion
- knee–tibia–ankle axes straight, parallel and symmetric
- calf volume and ankle width natural, not pinched
- flat bilateral foot contact and complete anatomy
- calibration outfit and continuous 15D hosiery coverage
- neutral background/light, complete framing, no text/watermark/collage

## Attempt result

- 2026-09-17: built-in ImageGen attempt 1 was rejected at output moderation with `sexual`; no image was returned.
- 2026-09-17: built-in ImageGen safety-wording retry was also rejected at output moderation with `sexual`; no image was returned.
- No candidate raster exists, no checksum exists, and no promotion occurred. These failed calls are not image references or body feedback.
