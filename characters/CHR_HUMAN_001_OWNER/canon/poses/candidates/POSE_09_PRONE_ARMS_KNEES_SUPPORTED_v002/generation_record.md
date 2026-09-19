# POSE_09_PRONE_ARMS_KNEES_SUPPORTED_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.138
identity_md_revision: draft_0.126
asset_id: POSE_09_PRONE_ARMS_KNEES_SUPPORTED
candidate_id: POSE_09_PRONE_ARMS_KNEES_SUPPORTED_v002
gate: "Gate 6 — Body / Pose Canon"
model_tool: "built-in image_gen"
status: GENERATION_BLOCKED_NO_OUTPUT
approval_status: NOT_GENERATED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: null
reference_set_ids:
  - OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1
  - OWNER_BODY_LEFT_3Q_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
reference_count: 3
previous_ai_pose_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_09_PRONE_ARMS_KNEES_SUPPORTED_v002/POSE_09_PRONE_ARMS_KNEES_SUPPORTED_v002.png"
checksum_sha256: null
qa_status: NO_OUTPUT
```

## Authorization and lineage

The user explicitly requested continuing generation of owner Pose 09 after the revised foot-contact contract was recorded. This authorizes exactly one independent v002 candidate. v001 returned no raster and is not an input. No POSE_01–08, Expression, Shot, failed candidate or unreviewed image is used as a reference.

The repository has no registered real-human source for this exact four-point support articulation. The motion is therefore conservatively defined in text and the coverage gap remains explicit.

## Reference responsibilities

1. `OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg`
   - SHA-256: `3f50c08e2993aa8dd406abd093d24f8a581b6e1475aa4dd57bda3884fed3b745`
   - responsibility: exact approved left-three-quarter adult face, neutral expression and even natural skin.
   - must_not_define: body, pose, hair, clothing, hosiery, hands/feet, lighting or background.
2. `OWNER_BODY_LEFT_3Q_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_02_LEFT_3Q_v001/BODY_02_LEFT_3Q_v001.png`
   - SHA-256: `f364b5c9b398c0c786964ffb8932707c7d657f997b8344abdd31a47b4322f4aa`
   - responsibility: approved 168 cm / 60 kg left-three-quarter body proportions, limb/hand/foot scale and unchanged visible Calibration Outfit, including scoped 15D matte nude appearance.
   - must_not_define: new face identity, four-point articulation, reusable hosiery/nail Material Canon, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - SHA-256: `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`
   - responsibility: Hairstyle-A near-center part, controlled crown volume, long straight dark-brown structure and tapered ends.
   - must_not_define: face, skin, body, pose, clothing, hosiery, hands/feet, lighting or background.

Reference budget: 3 approved scoped references. No previous generated Pose is attached.

## Authoritative candidate scope

- approximately 45-degree left-three-quarter four-point support view;
- both palms flat beneath the shoulders, fingers naturally separated, arms straight with relaxed elbows and no hyperextension;
- both knees on one floor plane beneath the hips, with natural pressure and no floating contact;
- both forefeet and toe pads contact that same floor; toes flex naturally at the metatarsophalangeal joints and both heels are clearly raised;
- long neutral spine close to horizontal, level pelvis and aligned head/neck;
- balanced clinical joint-calibration posture without deep lumbar arch, rounded back, hip lift or performative gesture.

The candidate must not define permanent identity/body/hair, outfit design, reusable hosiery/material/nail color, other poses, lighting or background.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: adult physical-therapy posture reference; exactly one POSE_09_PRONE_ARMS_KNEES_SUPPORTED v002 candidate, REVIEW_REQUIRED.

Input images: Image 1 defines only the exact approved left-three-quarter adult face and neutral expression. Image 2 defines only the approved 168 cm / 60 kg body proportions, limb scale and unchanged visible calibration clothing. Image 3 defines only Hairstyle A. Reconstruct independently; do not use or imitate any previous generated Pose.

Primary request: show one adult woman performing a neutral four-point physical-therapy tabletop position on a seamless studio floor, viewed from approximately 45 degrees at her left side. Both palms are flat directly beneath the shoulders with all fingers naturally separated. Arms are straight and relaxed, with no backward elbow locking. Both knees contact the same floor plane directly beneath the hips. Keep hips and knees near right angles. Both forefeet and toe pads contact the floor; toes bend naturally at the toe-base joints and both heels remain clearly raised. Do not place the insteps flat on the floor. Keep the spine long, neutral and nearly horizontal, pelvis and shoulders level, and head/neck aligned; turn the face only slightly toward camera so the approved three-quarter identity remains readable.

Style/medium: neutral photorealistic clinical apparel-fit and joint-position documentation.
Composition/framing: exact 3:4 vertical frame; full head, both hands and all fingers, both knees, both lower legs and both complete feet visible with clear space around the body.
Lighting/mood: neutral light-gray seamless studio, soft even white-balanced light, natural 70–85 mm perspective at torso height.
Constraints: preserve the approved face, body proportions, Hairstyle A and unchanged visible calibration outfit from the scoped references. Keep one continuous light-nude sheer matte textile appearance across every visible leg and complete foot region. No pose reference image, mat, furniture, props, text or watermark.
Avoid: insteps lying flat, floating toe pads, broken ankle-to-foot continuity, extra support shapes, deep back arch, rounded back, lifted pelvis, twisted torso, crossed limbs, duplicated or missing fingers/toes, merged limbs, plastic skin, dramatic styling or sexualized presentation.
```

## QA status

### Attempt 1

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references: all three declared approved scoped references; no previous Pose image.
- request_id: `e30c4dfa-7f5b-47e5-b614-3d1078302de5`
- next action: one concise retry framed only as a clinical movement assessment, preserving the four-point joint relationship and revised forefoot contact while inheriting the visible clothing from Image 2 without expanded material wording.

No reviewable raster exists after Attempt 1. Any successful retry remains a review candidate and cannot be promoted or used downstream without explicit user approval.

### Attempt 2

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references: the same three declared approved scoped references; no previous Pose image.
- request_id: `06f9d0cb-dc61-44bf-8b6f-0b7249b847f2`
- decision: stop built-in retries under the ImageGen skill; preserve the revised forefoot-contact Pose contract and do not switch to CLI/API without explicit user authorization.

Final QA status: `NO_OUTPUT`. v002 cannot be reviewed, promoted or used downstream.
