# POSE_07_KNEELING_CROUCHING_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.139
identity_md_revision: draft_0.127
asset_id: POSE_07_KNEELING_CROUCHING
candidate_id: POSE_07_KNEELING_CROUCHING_v003
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_07_KNEELING_CROUCHING_v003/POSE_07_KNEELING_CROUCHING_v003.png"
checksum_sha256: null
qa_status: NO_OUTPUT
```

## Authorization and lineage

The user explicitly requested another POSE_07 generation attempt. v003 is independently reconstructed from three approved scoped L1 Masters. v001 and v002 returned no raster; no POSE_01–09, Expression, Shot, failed candidate or unreviewed image is supplied.

The registered crouching material sources `IMG_2579.jpg` and `IMG_2580.jpg` remain physically absent and are not supplied. The approved right-three-quarter Body component provides the available in-image 15D nude matte appearance; this pose-specific material coverage gap remains explicit.

## Reference responsibilities

1. `OWNER_FACE_RIGHT_3Q_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_03_RIGHT_3Q_NEUTRAL/OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001.jpg`
   - SHA-256: `002b47b9b5e15d3a85d1467eb6b73890254c8d69d9d1422b24b5964841d412d8`
   - responsibility: exact approved right-three-quarter facial identity, calm neutral expression and even natural skin.
   - must_not_define: body, pose, hair, clothing, hosiery, hands/feet, lighting or background.
2. `OWNER_BODY_RIGHT_3Q_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_03_RIGHT_3Q/OWNER_BODY_03_RIGHT_3Q_CANON_001.png`
   - SHA-256: `32f87f0232bb087b434d1818ec22d2db1ba4311ec73b7e0fe2ebf380279412fd`
   - responsibility: approved 168 cm / 60 kg right-three-quarter body proportions, limb/foot scale and unchanged Calibration Outfit, including scoped 15D matte nude appearance.
   - must_not_define: new face identity, half-kneeling articulation, reusable hosiery/nail Material Canon, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - SHA-256: `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`
   - responsibility: Hairstyle-A near-center part, controlled crown volume, long straight dark-brown structure and tapered ends.
   - must_not_define: face, skin, body, pose, clothing, hosiery, hands/feet, lighting or background.

Reference budget: 3 approved scoped references. No previous generated Pose is attached.

## Authoritative candidate scope

- stable right-three-quarter clinical half-kneeling lunge articulation;
- front foot fully planted, front knee near 90 degrees and aligned over the foot;
- rear knee lightly contacting the same floor plane, rear lower leg extending backward with natural forefoot support;
- level pelvis, long upright neutral spine and relaxed arm counterbalance.

The candidate must not define permanent identity/body/hair, outfit design, reusable hosiery/material/nail color, other poses, lighting or background.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: adult clinical half-kneeling mobility-assessment reference; exactly one POSE_07_KNEELING_CROUCHING v003 candidate, REVIEW_REQUIRED.

Input images: Image 1 defines only the exact approved right-three-quarter adult face and neutral expression. Image 2 defines only the approved 168 cm / 60 kg body proportions, limb scale and unchanged visible calibration clothing. Image 3 defines only Hairstyle A. Reconstruct independently; do not use or imitate any generated Pose.

Primary request: show one adult woman in a standard upright half-kneeling lunge assessment, viewed approximately 45 degrees from her right side. The front foot is fully planted and the front knee is near 90 degrees, aligned over the foot. The rear knee lightly contacts the same seamless floor plane; the rear lower leg extends backward and the rear forefoot supports naturally. Keep the pelvis level, torso upright, spine long and neutral, shoulders relaxed and head aligned. Hold both arms comfortably forward and slightly apart for balance with relaxed open hands.

Style/medium: neutral photorealistic clinical mobility documentation.
Composition/framing: exact 3:4 vertical frame; one complete adult figure with full head, hands, both knees, lower legs and complete feet visible with clear margins.
Lighting/mood: neutral light-gray seamless studio, soft even white-balanced light, natural 70–85 mm perspective.
Constraints: preserve the approved face, body proportions, Hairstyle A and unchanged visible calibration outfit from the scoped references. No historical Pose input, mat, furniture, props, text or watermark.
Avoid: deep squat, rounded back, exaggerated arch, hip thrust, unstable balance, floating knee or foot contact, extra support shapes, crossed or merged limbs, missing or duplicated digits, dramatic styling or sexualized presentation.
```

## QA status

### Attempt 1

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references: all three declared approved scoped references; no previous Pose image.
- request_id: `072f5c7a-62e9-4aa3-976b-d7ba60825f66`
- next action: one concise retry retaining only the upright split-kneel joint relationship and inheriting visible clothing from Image 2 without material or low-crouch wording.

No reviewable raster exists after Attempt 1.

### Attempt 2

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references: the same three declared approved scoped references; no previous Pose image.
- request_id: `653bc016-03e5-4b8a-b0d1-7abf84abed69`
- decision: stop built-in retries under the ImageGen skill; preserve the approved calibration contract and do not switch to CLI/API without explicit user authorization.

Final QA status: `NO_OUTPUT`. v003 cannot be reviewed, promoted or used downstream.
