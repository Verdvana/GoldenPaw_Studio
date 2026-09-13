# POSE_01_RELAXED_STANDING_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.101
identity_md_revision: draft_0.89
asset_id: POSE_01_RELAXED_STANDING
candidate_id: POSE_01_RELAXED_STANDING_v001
gate: "Gate 6 — Body / Pose Canon"
model_tool: "built-in image_gen"
status: NO_OUTPUT_MODERATION_BLOCKED
approval_status: NOT_GENERATED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "PENDING"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_BODY_FRONT_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
reference_count: 3
previous_ai_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_01_RELAXED_STANDING_v001/POSE_01_RELAXED_STANDING_v001.png"
checksum_sha256: "PENDING"
qa_status: NOT_APPLICABLE_NO_OUTPUT
```

## Authorization and lineage

The user explicitly requested the next asset after the 13-item Expression plan was completed. This candidate is constructed in parallel from three approved scoped L1 Masters. No Expression image, failed or historical candidate, previous Pose, Shot image, L0 identity photo, or unreviewed image is supplied.

## Reference budget and responsibility plan

1. `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
   - responsibility: approved front facial identity, neutral adult facial geometry and skin presentation.
   - must_not_define: pose, body proportions, Hairstyle-A, outfit, hosiery, camera, lighting or background.
2. `OWNER_BODY_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg`
   - responsibility: approved 168 cm / 60 kg front body identity, head-to-body scale, limb lengths, waist/hip ratio, feet geometry and existing 15D matte nude combination context.
   - must_not_define: the new relaxed Pose articulation, permanent face refinements, other body angles, other hosiery colors/deniers/finishes, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - responsibility: approved eye-level front Hairstyle-A part, controlled crown volume, long straight panels, dark-brown restrained highlights, complete length and tapered ends.
   - must_not_define: face, skin, expression, body, pose, outfit, hosiery, lighting or background.

Reference budget: 3 images, within the ordinary five-image budget. All inputs are approved Masters with isolated duties.

## Authoritative candidate scope

- front-view relaxed standing articulation;
- natural even or only subtly distributed weight bearing without hip thrust;
- relaxed lowered shoulders, softly extended elbows, loose hands and natural fingers;
- neutral pelvis, non-hyperextended knees and both feet fully grounded without crossing;
- stable joint relationships under the approved 168 cm / 60 kg body identity.

## Must not define

- permanent facial or body geometry, height, weight, head-to-body ratio, limb length or waist/hip ratio;
- Hairstyle-A design, Expression Canon, skin tone or age;
- Calibration Outfit design or any episode wardrobe;
- reusable hosiery color, denier, finish, weave, toe construction or Material Canon;
- lighting, background, camera style or generated artifacts;
- any other Pose component or the complete `owner_v1.0` release.

## Prompt assembly

```text
Use case: photorealistic-natural
Asset type: CHR_HUMAN_001_OWNER L1 Pose Canon candidate

[ASSET TASK]
Create exactly one POSE_01_RELAXED_STANDING L1 Canon candidate for the adult character CHR_HUMAN_001_OWNER. One 3:4 portrait image, preferred 1536x2048. This is a neutral, non-sexual technical body-joint calibration photograph and remains REVIEW_REQUIRED.

[INPUT IMAGES AND RESPONSIBILITIES]
Image 1 — OWNER_FACE_FRONT_NEUTRAL_CANON_L1, path characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg: define only the approved front facial identity and neutral adult facial geometry; do not copy its crop, clothing, hair authority, lighting, or background.
Image 2 — OWNER_BODY_FRONT_CANON_L1, path characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg: define the approved 168 cm / 60 kg front body identity, head-to-body scale, limb lengths, waist/hip ratio, feet geometry, and the existing 15D matte nude combination context; do not merely duplicate its stiff calibration stance and do not redesign any permanent body property.
Image 3 — OWNER_HAIR_A_FRONT_CANON_L1, path characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png: define only Hairstyle A — near-center short frontal part, controlled low-to-medium crown volume, long straight loose dark-brown panels, restrained highlights, complete below-chest length and natural tapered ends; do not define face, skin, expression, body, pose, outfit, lighting, or background.

[POSE AUTHORITY]
Show a full-body, straight-on relaxed standing pose. Head and neck neutral, gaze calmly forward, mouth naturally closed. Shoulders naturally lowered, arms resting beside the torso with slight breathing room, elbows soft rather than locked, wrists neutral, hands loose, five natural fingers on each hand. Pelvis neutral with no hip thrust or exaggerated contrapposto. Weight balanced or only imperceptibly relaxed between both legs; knees straight but not hyperextended. Feet uncrossed, set at a natural narrow-to-hip-width stance, toes generally forward, both heels and full weight-bearing surfaces naturally touching the same studio floor.

[IDENTITY AND BODY INVARIANTS]
Preserve the exact same adult woman, the approved soft oval facial identity, realistic 168 cm / 60 kg proportions, head size, shoulder width, torso length, waistline, waist/hip relationship, arm and leg lengths, thigh/calf volume, straight natural knee-shin-ankle axes, and foot scale. No slimming, fattening, leg lengthening, head shrinking, hourglass exaggeration, enlarged eyes, narrow template nose, pointed chin, age change, or beauty-filter redesign.

[CAMERA AND STUDIO]
Photorealistic neutral technical studio photograph. Camera level around waist to lower chest with a horizontal optical axis, 70–85 mm equivalent lens-neutral perspective. Entire body visible from hair top through both soles, with approximately 5–8% clear space above the hair and below the feet. Centered straight-on composition. Neutral light-gray seamless backdrop, neutral 5200–5600 K white balance, broad soft even lighting, low contrast, realistic skin and fabric texture, no cinematic grading.

[CALIBRATION OUTFIT AND HOSIERY]
Wear the established Calibration Outfit only: plain opaque pink high-cut one-piece swimsuit, continuous 15D nude sheer pantyhose with a realistic matte/velvet textile finish, and no shoes. Pantyhose must remain one continuous closed-toe textile garment from waist and hips through thighs, knees, calves, ankles, heels, insteps and all toes. Fabric remains subtly visible over feet and toenails; burgundy toenail polish may show softly beneath the fabric. No ankle break, toe color band, toe-root line, seam-like boundary, bare toes, socks, shoes, latex, PVC, rubber, plastic, wet gloss, liquid coating or body paint.

[ANATOMY AND NEGATIVE CONSTRAINTS]
Correct adult anatomy: two arms, two hands, five distinct natural fingers per hand, two legs, two feet, five plausible toes per foot, one normal heel per foot. No fused, duplicated or missing digits; no extra limbs; no broken wrists, elbows, knees, ankles or heels; no floating foot, support block or merged silhouette. No sensual posing, pin-up styling, arched back, pushed chest, hip pop, crossed legs, hand on hip, theatrical gesture, walking stride, smile performance, prop or furniture.

[MUST NOT DEFINE]
This image may define only the relaxed standing Pose articulation. It must not redefine permanent face or body identity, Hairstyle A, Expression Canon, Calibration Outfit design, reusable hosiery Material Canon, skin tone, lighting, background, or any other Pose asset.

[OUTPUT CONTRACT]
Exactly one image and one pose; no collage, inset, comparison sheet, text, logo, watermark or border. Full body and all hair/hand/foot edges visible. Candidate status REVIEW_REQUIRED; do not imply approval or a locked Canon release.
```

## QA status

### Attempt 1

- result: `NO_OUTPUT_MODERATION_BLOCKED`
- stage: output safety system
- request_id: `40104837-e292-4f11-b0dc-e35adc9bdc27`
- action: no image or candidate was created; retry once with a shorter prompt that states the adult, non-sexual technical fit-and-joint calibration purpose more directly while preserving the same three approved references, Pose scope, Calibration Outfit and exclusions.

### Attempt 2

- result: `NO_OUTPUT_MODERATION_BLOCKED`
- stage: output safety system
- request_id: `f07ccbe9-0e51-43aa-8547-01d48773e379`
- prompt adjustment: shortened to an explicit adult, non-sexual apparel-fit and body-joint calibration request; preserved the same three approved references and scoped constraints.
- action: stopped further prompt retries after the repeated identical safety block. No raster, metadata or QA image review exists.

Final current status: no candidate image was generated. `POSE_01_RELAXED_STANDING` remains unapproved and cannot be used downstream. The existing `BODY_01_FRONT` asset is not automatically promoted or aliased into Pose Canon.
