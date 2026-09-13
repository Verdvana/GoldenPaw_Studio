# POSE_06_BENDING_REACHING_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.118
identity_md_revision: draft_0.106
asset_id: POSE_06_BENDING_REACHING
candidate_id: POSE_06_BENDING_REACHING_v001
gate: "Gate 6 — Body / Pose Canon"
model_tool: "built-in image_gen"
status: DRAFT_READY_TO_GENERATE
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "PENDING"
reference_set_ids:
  - OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1
  - OWNER_BODY_LEFT_3Q_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
reference_count: 3
previous_ai_pose_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_06_BENDING_REACHING_v001/POSE_06_BENDING_REACHING_v001.png"
checksum_sha256: "PENDING"
qa_status: PENDING
```

## Authorization and lineage

The user requested the next planned Pose asset after approving POSE_05 reuse. No registered L0 bending/reaching motion source exists. This candidate is independently generated from three approved scoped L1 Masters. POSE_01–05 and every other generated Pose, Expression, historical Body candidate and Shot image are excluded.

## Reference responsibilities

1. `OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg`
   - responsibility: exact approved left-three-quarter facial identity, neutral feature relationships and clean even skin presentation.
   - must_not_define: body, bending/reaching articulation, hair, outfit, hosiery, feet, lighting or background.
2. `OWNER_BODY_LEFT_3Q_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_02_LEFT_3Q/OWNER_BODY_02_LEFT_3Q_CANON_001.png`
   - responsibility: approved 168 cm / 60 kg left-three-quarter body proportions, limb/foot scale, Calibration Outfit and continuous 15D matte nude hosiery context.
   - must_not_define: new identity, the bending/reaching motion, other Pose components, reusable hosiery/nail-color Canon, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - responsibility: Hairstyle-A near-center part, controlled volume, long straight loose structure, dark-brown restrained highlights and tapered ends.
   - must_not_define: face, skin, body, motion, outfit, hosiery, feet, lighting or background.

Reference budget: 3 approved Masters. Source-coverage gap: no matching L0 bending/reaching image is registered. No previous Pose pixels are used.

## Authoritative candidate scope

- left-three-quarter natural bending/reaching articulation;
- 25–35-degree hip hinge with neutral elongated spine, soft knee flexion and stable staggered feet;
- one arm reaching naturally forward/down while the other provides relaxed counterbalance.

## Must not define

- permanent face/body geometry, Hairstyle A, Expression Canon, skin tone or age;
- Calibration Outfit, reusable hosiery/nail-color Canon or episode wardrobe;
- props/environment, other Pose components, lighting, background or complete release.

## Prompt assembly

```text
Use case: photorealistic-natural
Asset type: adult apparel-fit ergonomic movement reference

Create exactly one POSE_06_BENDING_REACHING v001 candidate for the approved adult owner character. Use a neutral left-three-quarter view with the face and body pointing image-left.

Input roles are strict. Image 1 defines only the approved left-three-quarter face and clean even skin. Image 2 defines only the approved 168 cm / 60 kg left-three-quarter body proportions, limb/foot scale and complete calibration outfit. Image 3 defines only Hairstyle A. Do not use or imitate any previous Pose image.

Show a controlled everyday forward-reaching movement used for ergonomic and garment-fit evaluation. The person stands in a stable staggered stance with both feet fully supported, knees softly bent and pelvis level. Bend forward 25–35 degrees primarily from the hip joints, maintaining a naturally long neutral spine without rounding or arching. Extend the nearer arm forward and slightly downward toward an imaginary calibration point in open space at about knee height, hand open and relaxed. Keep the other arm naturally lowered and slightly behind the torso for balance. Shoulders remain down, neck follows the spine and the head lifts only enough for the approved left-three-quarter face to remain clearly visible with a calm neutral expression.

Preserve the exact approved adult identity, 168 cm / 60 kg body, limb lengths, foot scale and Hairstyle A. Hair responds naturally to gravity with a modest forward fall but keeps the approved part, straight structure, length and tapered ends. Keep skin clean, even and natural without red blotches, dirty patches, bruised-looking marks or iterative artifacts.

Preserve the complete approved calibration outfit: pink one-piece fitting garment, continuous closed-foot light-nude 15D matte tights and no shoes. Burgundy toenail color may remain naturally and subtly visible beneath the fabric; fingernails remain natural. The textile stays continuous over knees, calves, ankles, heels, insteps and toes without ankle cutoffs, toe bands, seams, glossy plastic appearance or bare-foot discontinuities.

One complete adult figure from hair to feet, exact 3:4 vertical frame, clear margins around the reaching hand and both feet, neutral light-gray seamless studio, soft even catalog lighting, waist-to-lower-chest camera height, 70–85 mm-equivalent perspective. No support object, no furniture, no lifted heel, no unstable lunge, no squat, no kneeling, no twisting collapse, no rounded back, no exaggerated arch, no dramatic performance, no identity drift, no extra/missing digits, no text or watermark. Candidate remains REVIEW_REQUIRED and may define only the bending/reaching articulation after explicit approval.
```

## QA status

Pending generation and technical review.
