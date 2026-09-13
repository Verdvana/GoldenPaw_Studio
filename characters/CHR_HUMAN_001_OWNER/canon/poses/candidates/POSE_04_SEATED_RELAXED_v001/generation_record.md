# POSE_04_SEATED_RELAXED_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.115
identity_md_revision: draft_0.103
asset_id: POSE_04_SEATED_RELAXED
candidate_id: POSE_04_SEATED_RELAXED_v001
gate: "Gate 6 — Body / Pose Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_BODY_FRONT_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
reference_count: 3
previous_ai_pose_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_04_SEATED_RELAXED_v001/POSE_04_SEATED_RELAXED_v001.png"
pixel_storage_status: "MOVED_TO_CANON"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/approved/POSE_04_SEATED_RELAXED/OWNER_POSE_04_SEATED_RELAXED_CANON_001.png"
current_promoted_checksum_sha256: "5c890e3c7abf3ad5e1b05f2bae5b61c1df079ea6eddf9869681db47a0440feff"
checksum_sha256: "5c890e3c7abf3ad5e1b05f2bae5b61c1df079ea6eddf9869681db47a0440feff"
qa_status: PASS_TECHNICAL_REVIEW_REQUIRED
```

## Authorization and lineage

The user explicitly requested the next Pose asset after approving POSE_03. No registered L0 seated-articulation source exists. This candidate is independently generated from three approved scoped L1 Masters. POSE_03 and every other generated Pose, Expression, historical Body candidate and Shot image are excluded.

## Reference responsibilities

1. `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
   - responsibility: exact approved front facial identity, clean neutral skin tone and natural even skin presentation.
   - must_not_define: body, pose, hair, outfit, hosiery, feet, chair, lighting or background.
2. `OWNER_BODY_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg`
   - responsibility: approved 168 cm / 60 kg body proportions, limb/foot scale, Calibration Outfit, continuous 15D matte nude hosiery and visible burgundy toenail context.
   - must_not_define: permanent face refinement, relaxed seated articulation, other Pose components, chair, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - responsibility: approved front Hairstyle-A part, volume, straight panels, length and tapered ends.
   - must_not_define: face, skin, body, pose, outfit, hosiery, feet, chair, lighting or background.

Reference budget: 3 approved Masters. Source-coverage gap: no L0 seated reference is registered. No previous Pose pixels are used.

## Generation attempts

- Attempt 1: rejected during output moderation (`sexual`); no image was returned or stored. The likely false-positive combination was seated articulation plus garment/material and detailed lower-limb wording. Attempt 2 uses a more explicit apparel-fit and ergonomic-evaluation context while preserving the same approved references and asset scope.
- Attempt 2: generated successfully with built-in ImageGen. The returned cache image was copied once to the authoritative candidate path; no prior Pose image was supplied.

## Authoritative candidate scope

- front-facing relaxed seated articulation distinct from POSE_03 upright sitting;
- gentle supported recline, relaxed shoulders/elbows/wrists and mild natural asymmetry;
- uncrossed knees, slightly offset flat feet and stable seated balance.

## Must not define

- permanent face/body geometry, Hairstyle A, Expression Canon, skin tone or age;
- Calibration Outfit, reusable hosiery/nail-color Canon or episode wardrobe;
- chair/furniture/environment design, other Pose components or complete release.

## Prompt assembly

```text
Use case: photorealistic-natural
Asset type: adult technical relaxed-seated joint calibration reference

Create exactly one POSE_04_SEATED_RELAXED v001 candidate for adult character CHR_HUMAN_001_OWNER, following OWNER_L1_GENERATION_SPEC draft_1.114 and IDENTITY draft_0.102. Do not use or imitate POSE_03 or any generated Pose image.

Image 1 is the sole authority for the exact approved front face, clean neutral skin and facial geometry. Image 2 defines only the approved 168 cm / 60 kg body proportions, limb and foot scale, Calibration Outfit, continuous 15D matte nude pantyhose and stable burgundy toenail context. Image 3 defines only Hairstyle A. Do not mix their duties.

Show one full-body front-facing relaxed seated posture on a simple featureless neutral-gray studio chair with a plain low back. Pelvis remains centered and stable while the torso rests back very slightly against the support; spine stays naturally long but less formal than upright POSE_03. Head remains level, calm forward gaze, mouth naturally closed. Shoulders drop comfortably. Elbows and wrists are soft. Both empty hands rest separately and lightly on the thighs at slightly different natural positions, with distinct relaxed fingers.

Thighs point generally forward at natural hip width. Knees remain comfortably separated and uncrossed, bent naturally around 90–105 degrees. Lower legs are relaxed rather than rigidly vertical. Both feet stay fully visible and flat on the same floor, with one foot only a few centimeters ahead of the other and no leg crossing. Use mild natural asymmetry without hip thrust, slouching, collapse or glamour posing. Preserve realistic seated soft-tissue compression without changing body mass or limb lengths.

Preserve the exact approved woman, face, Hairstyle A, 168 cm / 60 kg proportions and clean even skin. No sensitive blotches, dirty patches, asymmetric skin color, bruised-looking marks, acne-like artifacts, over-sharpening or plastic smoothing.

Keep the established Calibration Outfit: plain opaque pink one-piece athletic fit garment, continuous light-nude closed-foot 15D matte/velvet sheer pantyhose and no shoes. All ten toenails have restrained deep burgundy polish visible softly beneath the hosiery fibers; fingernails remain natural. No bare-toe break, ankle cutoff, toe band, reinforced toe, surface-painted polish, plastic gloss or body-paint appearance.

Technical neutral studio photograph, exact 3:4 portrait, entire hair, hands, chair contact, lower legs and both feet visible with clear margins, level 70–85 mm-equivalent perspective, neutral light-gray seamless background and broad even 5200–5600 K light.

Correct ordinary adult anatomy. No crossed legs, sensual or splayed pose, deep slouch, exaggerated recline, arched back, dangling feet, fused limbs, broken joints, duplicated heels, extra/missing digits, props, text, watermark, collage or border. Chair is support only and defines no reusable prop or environment. This candidate defines only relaxed seated articulation. Status REVIEW_REQUIRED, not approved Canon.
```

## Retry prompt assembly — attempt 2

```text
Create one professional full-body apparel-fit reference photograph of the approved adult owner character, seated front-facing on a plain gray studio chair for a neutral ergonomic posture evaluation.

Reference roles are strict: image 1 defines only the approved face and clean even skin; image 2 defines only the approved adult body proportions, limb and foot scale, and complete pink calibration garment with continuous light-nude 15D matte tights; image 3 defines only Hairstyle A. Do not use any earlier generated pose.

Pose: stable centered sitting with a small supported backward ease, relaxed shoulders and arms, hands resting separately on the upper legs, uncrossed legs, comfortable knee spacing, and both feet resting naturally on the floor with one foot slightly forward. The posture should look ordinary, balanced and relaxed, clearly less formal than an upright ID-photo sitting pose. Preserve normal anatomy and mild natural asymmetry.

Show the complete adult figure from hair to feet with clear margins in a 3:4 vertical frame. Preserve the exact approved face, Hairstyle A and 168 cm / 60 kg proportions. Skin must remain natural, clean and even, without red patches, blotches or image-generation artifacts. Preserve the complete approved calibration outfit exactly as shown by the body reference: pink one-piece fitting garment, continuous closed-foot light-nude 15D matte tights, and no shoes. The stable burgundy toenail color may remain naturally and subtly visible through the fabric; fingernails are natural.

Neutral catalog lighting, plain light-gray background, eye-level 70–85 mm perspective, realistic textile appearance, no glossy or plastic fabric, no exposed skin discontinuity at the feet, no crossed limbs, no dramatic pose, no slouch, no props beyond the support chair, no text or watermark. This is an unapproved POSE_04_SEATED_RELAXED candidate for posture and apparel-fit review only.
```

## QA status

Technical preflight passed. The supported backward ease is subtle and near the minimum of the intended relaxed range; the user explicitly accepted the candidate on 2026-09-13.

## User approval and promotion

On 2026-09-13 the user stated “批准”. The exact candidate raster and sidecar metadata were moved, not copied, to `characters/CHR_HUMAN_001_OWNER/canon/poses/approved/POSE_04_SEATED_RELAXED/OWNER_POSE_04_SEATED_RELAXED_CANON_001.png`. The checksum remains unchanged. Approval is scoped to the visible relaxed-seated articulation and does not authorize chair/environment, permanent identity/body/hair, hosiery/nail-color Canon, other poses or the full `owner_v1.0` release.
