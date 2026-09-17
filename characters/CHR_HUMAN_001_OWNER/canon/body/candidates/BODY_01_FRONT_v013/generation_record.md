# BODY_01_FRONT_v013 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.222
identity_md_revision: draft_0.39
body_md_revision: draft_0.16
method_id: OWNER_BODY_01_FRONT_METHOD_V2
user_scoped_override: "2026-09-17 source-derived Face recovery; no L1 Face raster; v013 toe anatomy and hosiery continuity correction"
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v013
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v013/BODY_01_FRONT_v013.png"
qa_status: FAIL_TOENAIL_VISIBILITY_REVIEW_REQUIRED
checksum_sha256: d7e4ea4faf28aff7f0db455cf3cf2d6f732b046ac32f86678ba13aa68cd1664e
```

## Reference responsibilities

1. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` — source-derived face/skin only; retain the current successful Face recovery method; no hair, body, clothing, lighting or background authority.
2. `L0_OWNER_002` (`3.jpg`) — natural stature and body-proportion context only.
3. `L0_OWNER_003` (`4.jpg`) — torso, waist, hip, thigh, calf and limb-volume cross-check only.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — retain the current successful Hairstyle A method; hair pixels only, masked area defines nothing.

No approved Face raster, approved Body Master, BODY_01 v001–v012, previous shot or other generated image is supplied.

## Prompt assembly

```text
Use case: identity-preserve, clinical anthropometric reference.
Create exactly one non-sexual, neutral, full-length 3:4 straight-on front-view technical body-proportion calibration plate of the same adult woman. Reconstruct in parallel only from the declared source-derived references.

Image 1 is source-derived face/skin context from the FACE_01 recovery method. Preserve the current successful face reconstruction method exactly: recognizable front-face relationships, realistic warm-neutral skin, direct gaze, closed mouth and visually neutral eye-level projection. Do not use any approved L1 Face image or any generated face. Image 4 is the face-masked Hairstyle A source reference. Preserve the current successful Hairstyle A reconstruction exactly: long straight dark-brown hair, near-center part, low crown and natural tapered lengths. The mask defines nothing. Images 2–3 define body context only and must not define face, hair, clothing, shoes, props, background or retouching.

Preserve the accepted 168 cm / approximately 60 kg adult proportions, torso, waist/hip ratio, straight lower-leg axes, small natural inter-leg gap, pink calibration swimsuit and pale light-nude 15D sheer pantyhose.

Foot and hosiery correction only: both feet must have anatomically correct toes. Each foot's second toe has exactly one single, complete, coherent nail plate beneath the hosiery. No duplicated, split, stacked or extra nail plates on either second toe or any other toe. The red-burgundy polish is visible softly through the sheer textile, never painted on top. Remove the incorrect transverse line at the toe roots: there must be no horizontal band, seam, hard boundary, ring, artificial crease or separate toe-cap line where the toes meet the forefoot. The pantyhose remains one continuous textile over every toe and from the toes onto the forefoot, with subtle realistic interdigital stretch and valley tension, no bare gaps and no material discontinuity. Material is textile, never latex, PVC, plastic, wet coating or body paint.

Keep the lower legs anatomically straight, with knee–tibial shaft–ankle centers on parallel near-vertical axes, natural calf volume and ordinary ankle width. Feet are flat, stable, uncrossed and approximately parallel with a small natural inner-leg gap. Do not change face, hairstyle, stance, body proportions or camera.

Neutral gray-white seamless studio, soft even 5200–5600K illumination, level 70–85mm-equivalent camera centered between waist and lower chest. Complete head, hands, heels and toes with 5–8% breathing room, square torso, relaxed arms and neutral direct gaze. No props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.
```

## QA checklist

- face and Hairstyle A follow the same successful source-derived method
- no L1 Face or generated Body pixel contamination
- each second toe has exactly one nail plate
- no duplicated/split/extra nail plates anywhere
- no transverse toe-root line, seam or hard boundary
- continuous pale hosiery with natural interdigital tension
- red/burgundy polish only beneath the fabric
- lower-leg axes, stance gap, body proportions and framing preserved

## Attempt result

- 2026-09-17: built-in ImageGen was rejected at output moderation with `sexual`; no image was returned.
- No candidate raster, checksum or promotion exists for v013. The failed call is not a reference and does not alter the successful Face/Hairstyle-A method.

## Successful retry and QA

- generated_at: 2026-09-17
- built-in output saved to the project candidate path as a unique candidate raster.
- face and Hairstyle A: preserved successfully using the source-derived methods.
- toe-root line and duplicated second-toe nail defects: not observed in the full-frame precheck.
- toenail polish: FAIL/weak visibility. The red-burgundy polish is too faint to verify confidently beneath the hosiery.
- status remains `REVIEW_REQUIRED`; no promotion or Canon replacement occurred.
