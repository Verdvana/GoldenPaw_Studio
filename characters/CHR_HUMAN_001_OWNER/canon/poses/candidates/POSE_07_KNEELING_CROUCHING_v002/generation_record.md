# POSE_07_KNEELING_CROUCHING_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.127
identity_md_revision: draft_0.115
asset_id: POSE_07_KNEELING_CROUCHING
candidate_id: POSE_07_KNEELING_CROUCHING_v002
gate: "Gate 6 — Body / Pose Canon"
model_tool: "built-in image_gen"
status: GENERATION_BLOCKED_NO_OUTPUT
approval_status: NOT_GENERATED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: null
reference_set_ids:
  - OWNER_FACE_RIGHT_3Q_NEUTRAL_CANON_L1
  - OWNER_BODY_RIGHT_3Q_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
reference_count: 3
previous_ai_pose_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_07_KNEELING_CROUCHING_v002/POSE_07_KNEELING_CROUCHING_v002.png"
checksum_sha256: null
qa_status: NO_OUTPUT
```

## Authorization and lineage

The user explicitly requested regeneration of POSE_07 after v001 produced no raster output. v002 is an independent reconstruction from three approved scoped L1 Masters. v001, POSE_01–06, all generated Pose/Expression candidates and all shots are excluded.

The registered crouching-material set `HOS_15D_NUDE_MATTE_CROUCHING` still resolves to missing physical files `IMG_2579.jpg` and `IMG_2580.jpg`; neither is supplied. The approved right-three-quarter Body component and written hosiery contract provide the available in-image 15D nude matte guidance. This source-coverage gap remains disclosed.

## Reference responsibilities

1. `OWNER_FACE_RIGHT_3Q_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_03_RIGHT_3Q_NEUTRAL/OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001.jpg`
   - SHA-256: `002b47b9b5e15d3a85d1467eb6b73890254c8d69d9d1422b24b5964841d412d8`
   - responsibility: exact approved right-three-quarter facial identity, calm closed-mouth neutral expression and even natural skin.
   - must_not_define: body, pose, hair, clothing, hosiery, feet, lighting or background.
2. `OWNER_BODY_RIGHT_3Q_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_03_RIGHT_3Q/OWNER_BODY_03_RIGHT_3Q_CANON_001.png`
   - SHA-256: `32f87f0232bb087b434d1818ec22d2db1ba4311ec73b7e0fe2ebf380279412fd`
   - responsibility: approved 168 cm / 60 kg right-three-quarter body proportions, limb and foot scale, Calibration Outfit and visible 15D light-nude matte presentation.
   - must_not_define: new face identity, kneeling/crouching articulation, reusable hosiery/nail-color Canon, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - SHA-256: `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`
   - responsibility: Hairstyle-A part, controlled crown volume, long straight dark-brown structure and tapered ends.
   - must_not_define: face, skin, body, pose, clothing, hosiery, feet, lighting or background.

Reference budget: 3 approved L1 Masters; no previous Pose pixels and no missing material paths supplied.

## Authoritative candidate scope

- stable right-three-quarter half-kneeling / low-crouch transition articulation;
- front-leg hip/knee flexion and planted-foot loading;
- rear-knee floor contact, rear lower-leg fold and action-appropriate forefoot support;
- neutral torso alignment and relaxed arm counterbalance.

## Must not define

- permanent face/body geometry, Hairstyle A, Expression Canon, skin tone or age;
- Calibration Outfit design, hosiery Material Canon, nail-color Canon or episode wardrobe;
- props/environment, other Pose components, lighting, background or complete release.

## Prompt assembly

```text
Use case: photorealistic-natural
Asset type: adult clinical range-of-motion reference

Create exactly one POSE_07_KNEELING_CROUCHING v002 REVIEW_REQUIRED candidate for CHR_HUMAN_001_OWNER, following OWNER_L1_GENERATION_SPEC draft_1.127 and IDENTITY draft_0.115. Reconstruct independently from the three supplied approved Masters. Do not use or imitate v001, any previous Pose, any Expression candidate or any shot.

Image 1 defines only the exact approved right-three-quarter face, calm closed-mouth neutral expression and even natural skin. Image 2 defines only the approved 168 cm / 60 kg body proportions, limb and foot scale, and the complete established pink one-piece calibration garment with light-nude 15D matte legwear and no shoes. Image 3 defines only Hairstyle A. Preserve these responsibilities without averaging or allowing one image to redefine another domain.

Show one adult figure in a stable right-three-quarter half-kneeling position for neutral clinical joint-range documentation. The front foot is fully planted and carries weight; the front knee is near 90 degrees and aligned over the foot. The rear knee lightly touches the same floor plane; the rear lower leg extends backward and the rear foot uses natural forefoot support. Keep the pelvis level, spine neutral, torso upright with only a slight forward inclination, shoulders relaxed, and head aligned. Both arms extend comfortably forward and slightly apart for balance, with open relaxed hands that do not touch the body or floor.

Preserve the approved adult identity, body volume, proportions, limb lengths, foot scale and Hairstyle A. Hair follows gravity while retaining its approved near-center part, straight structure, dark-brown color, length and tapered ends. Keep the complete established calibration clothing unchanged. The light-nude 15D matte textile remains visibly continuous across both bent legs, ankles, heels, insteps and toes, with natural stretch at joints and no exposed-foot break, white shift, toe band, seam, plastic gloss or body-paint appearance. Burgundy toenails may appear only softly muted beneath the textile.

One complete figure with head, hands, knees and feet fully inside an exact 3:4 vertical frame. Neutral light-gray seamless studio, soft even white-balanced light and natural 70–85 mm-equivalent perspective. No prop, mat, furniture, dramatic performance, deep rounded-back squat, hip thrust, exaggerated arch, unstable balance, floating contact, duplicated support shape, extra or missing digits, text, logo or watermark. Candidate status remains REVIEW_REQUIRED and does not become Canon automatically.
```

## Generation attempts

### Attempt 1

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references: the three declared approved Masters; no previous Pose image.
- request_id: `c3238f0b-3d65-4591-b123-dc70af8ba236`
- next action: one targeted concise retry that leaves clothing unchanged from the approved Body Master and removes detailed material wording.

### Attempt 2

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references: the same three declared approved Masters; no previous Pose image.
- request_id: `32e220fa-5e67-4ae0-a325-479b5c5c30ae`
- decision: stop built-in retries; do not alter the Calibration Outfit and do not switch to CLI/API without explicit user authorization.

## QA status

No raster output exists. Visual QA cannot be performed. Status: `GENERATION_BLOCKED_NO_OUTPUT`.
