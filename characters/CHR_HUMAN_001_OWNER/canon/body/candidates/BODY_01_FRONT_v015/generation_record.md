# BODY_01_FRONT_v015 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.222
identity_md_revision: draft_0.39
body_md_revision: draft_0.16
method_id: OWNER_BODY_01_FRONT_METHOD_V2
user_scoped_override: "2026-09-17 source-derived Face recovery; no L1 Face raster; v015 waist transition and hosiery integration"
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v015
gate: "Gate 3 — Body Canon"
model_tool: built-in image_gen
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
  - OWNER_L0_BODY_FRONT_CONTEXT
reference_count: 4
previous_ai_reference_count: 0
face_l1_raster_supplied: false
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v015/BODY_01_FRONT_v015.png"
qa_status: PASS_USER_APPROVED
checksum_sha256: 8faa10238bb99c614f63afbc8d0aa02dbb43d3d425673afd5c1d8dab5e7ba5f4
```

## Reference responsibilities

1. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` — source-derived face/skin only; follow the current successful FACE_01 recovery method; never use L1 Face pixels.
2. `L0_OWNER_002` (`3.jpg`) — natural stature and body-proportion context only.
3. `L0_OWNER_003` (`4.jpg`) — torso, waist, hip, thigh, calf and limb-volume cross-check only.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — current successful Hairstyle A method; visible hair pixels only, masked area defines nothing.

No approved Face raster, approved Body Master, BODY_01 v001–v014, previous shot or other generated image is supplied.

## Prompt assembly

```text
Use case: identity-preserve, clinical anthropometric reference.
Create exactly one neutral, non-sexual, full-length 3:4 straight-on front-view technical body-proportion calibration plate of the same adult woman. Reconstruct in parallel only from the four source-derived references.

Image 1 is source-derived face/skin context from the FACE_01 recovery method. Preserve the current successful face method exactly: recognizable face, natural facial relationships, realistic warm-neutral skin, direct gaze and closed mouth. Do not directly reference or use any L1 Face asset image, any generated face or any previous Body image.
Image 4 is the face-masked Hairstyle A source. Preserve the current successful Hairstyle A method exactly: long straight dark-brown hair, near-center part, low crown and natural tapered lengths. The gray mask defines nothing. Images 2–3 define body context only.

Preserve the accepted 168 cm / approximately 60 kg body, current leg shape, straight mild tibial paths, small natural inner-leg gap, shoulder/chest volume and existing hip width. Make only the waist slightly narrower. The ribcage should narrow smoothly and naturally into the waist, then widen in a normal continuous transition into the existing broad hip/pelvis width. No corset effect, pinched waist, abrupt indentation, exaggerated hourglass, hip enlargement or body-width redesign.

Keep lower legs as currently accepted: each tibial shaft begins only slightly lateral to the knee center, follows a small gentle continuous inward curve, and returns gradually to the ankle center. No large bow, dramatic lateral sweep, O-leg silhouette, sharp kink or displaced ankle.

Strict hosiery integration correction: the pale light-nude 15D sheer textile must visibly continue as one uninterrupted surface from thighs through calves, ankles, forefeet and all toes. The toe area must not look like bare feet: show a soft slightly lighter-than-skin translucent textile veil over the entire toe skin and nails, with the same fine matte/velvet haze and subtle textile presence seen on the lower legs. Red-burgundy polish is visible softly beneath the fabric, never painted on top, never pink. Between adjacent toes, show visible but delicate fabric tension curves: narrow curved/V-shaped stretch valleys and translucent tension highlights that follow the interdigital separations while the fabric bridges them. These curves are hosiery deformation, not bare skin grooves, not toe-root seams and not a hard horizontal line. No bare toe appearance, no exposed nail surface, no transverse toe-root line, no toe-cap boundary, no seam, no band, no discontinuity, no latex/PVC/plastic/wet/body-paint appearance.

Feet flat, stable, uncrossed and approximately parallel. Neutral gray-white seamless studio, soft even 5200–5600K light, level 70–85mm-equivalent camera centered between waist and lower chest. Complete head, hands, heels and toes with 5–8% breathing room, square torso, relaxed arms and neutral direct gaze. No props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.
```

## QA checklist

- face generated from FACE_01 recovery method, not L1 Face raster
- Hairstyle A method preserved
- waist slightly narrower with smooth transition to existing hip width
- current leg shape and mild tibial path preserved
- toes visibly covered by the same pale hazy hosiery surface as the legs
- interdigital fabric tension curves clearly visible
- burgundy polish beneath fabric, not pink or painted on top
- no toe-root line, bare-foot appearance, seam or discontinuity

## Attempt result and QA

- generated_at: 2026-09-17
- built-in output saved to the project candidate path as a unique candidate raster.
- waist refinement: PASS preliminary; waist is slightly narrower and transitions continuously into the established hip width without corset compression.
- face and Hairstyle A: PASS preliminary; current successful source-derived methods retained.
- leg geometry: PASS preliminary; current accepted lower-leg shape retained.
- toe material: REVIEW_REQUIRED/FAIL preliminary. Burgundy polish is present, but the toe area still reads too close to bare feet and the interdigital hosiery tension curves are not sufficiently clear at full-frame review.
- user approval received: “完美，登记吧”. Candidate PNG was moved unchanged to the approved Master path as `OWNER_BODY_01_FRONT_CANON_003`.
- active approved path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_003.png`
- promoted checksum: `8faa10238bb99c614f63afbc8d0aa02dbb43d3d425673afd5c1d8dab5e7ba5f4`
