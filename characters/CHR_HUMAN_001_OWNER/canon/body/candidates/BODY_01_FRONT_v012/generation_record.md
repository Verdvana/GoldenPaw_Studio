# BODY_01_FRONT_v012 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.222
identity_md_revision: draft_0.39
body_md_revision: draft_0.16
method_id: OWNER_BODY_01_FRONT_METHOD_V2
user_scoped_override: "2026-09-17 source-derived Face recovery; no L1 Face raster; v012 hosiery refinement"
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v012
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v012/BODY_01_FRONT_v012.png"
qa_status: PASS_TECHNICAL_PRECHECK_REVIEW_REQUIRED
checksum_sha256: 61e3c19a04e7799ef025b020d641b63e7546bb1f5469bc9ff52dcec0840660ae
```

## Reference responsibilities

1. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` — source-derived face/skin only; no hair, body, clothing, lighting or background authority.
2. `L0_OWNER_002` (`3.jpg`) — natural stature and body-proportion context only; no face, hair, clothing, shoes, props, background or retouching authority.
3. `L0_OWNER_003` (`4.jpg`) — torso, waist, hip, thigh, calf and limb-volume cross-check only; no face, hair, outfit, legwear, shoes, environment or final-body authority.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — Hairstyle A pixels only; masked area defines nothing.

No approved Face raster, approved Body Master, BODY_01 v001–v011, previous shot or other generated image is supplied.

## Prompt assembly

```text
Use case: identity-preserve, clinical anthropometric reference.
Create exactly one non-sexual, neutral, full-length 3:4 straight-on front-view technical body-proportion calibration plate of the same adult woman. Reconstruct in parallel only from the declared source-derived references. Image 1 is source-derived face/skin context from the FACE_01 recovery method and defines only recognizable front-face relationships, realistic warm-neutral skin, direct gaze and closed mouth; do not use any approved L1 Face image. Images 2–3 define body context only. Image 4 defines visible Hairstyle A hair only; its gray mask defines nothing.

Preserve the user's 168 cm and approximately 60 kg baseline, accepted natural adult shoulder, torso, waist, hip, thigh, calf and limb volume, accepted face and Hairstyle A, neutral standing pose, straight lower-leg axes and small natural inter-leg gap. Do not change body width, leg length, camera perspective, face, hair or stance geometry.

Use the project calibration clothing: plain opaque pink high-cut one-piece athletic swimsuit; continuous light-nude 15D velvet-finish sheer closed-foot pantyhose; no shoes. The pantyhose must read slightly lighter than the underlying natural skin, not darker: a soft pale nude textile veil with subtle matte/velvet sheen and realistic transparency. The red-burgundy toenail polish must be softly but clearly visible only beneath the sheer toe fabric, never painted on top. Show the textile continuously covering each toe and spanning the interdigital spaces with gentle natural fabric tension and small realistic stretch/valley response between adjacent toes; no bare gaps, no exposed nail surface, no toe seam, no color band, no reinforced toe, no discontinuity or hard line. The material is real textile, never latex, PVC, plastic, wet coating or body paint.

Keep both lower legs anatomically straight in front view: knee center, tibial shaft and ankle center aligned on each near-vertical parallel axis; natural calf volume; ordinary adult ankle width, not pinched. Feet flat, stable, uncrossed and approximately parallel with a small natural inner-leg gap.

Neutral gray-white seamless studio, soft even 5200–5600K illumination, level 70–85mm-equivalent camera centered between waist and lower chest. Complete head, hands, heels and toes with 5–8% breathing room, square torso, relaxed arms and neutral direct gaze. No props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.
```

## QA checklist

- source-derived Face method followed; no L1 Face pixel contamination
- lower-leg axes and small inter-leg gap preserved
- hosiery is lighter than skin, not darker
- red/burgundy polish visible naturally beneath toe fabric
- continuous fabric spans interdigital toe spaces with natural tension
- no seams, bands, bare toes, latex/PVC/plastic/wet/body-paint appearance
- previously accepted body, face, hair, framing and calibration outfit preserved

## Attempt result and QA

- generated_at: 2026-09-17
- built-in output saved to the project candidate path as a unique candidate raster.
- user-requested refinements are visible: hosiery reads slightly lighter than the underlying skin; red/burgundy toenail polish is visible beneath the toe fabric; the textile spans the interdigital spaces with natural tension/valley response.
- technical precheck: PASS for lower-leg straightness, small inter-leg gap, continuous hosiery appearance, foot contact and neutral presentation.
- approval remains `REVIEW_REQUIRED`; no promotion or Canon replacement occurred.
