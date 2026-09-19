# POSE_09_PRONE_ARMS_KNEES_SUPPORTED_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.137
identity_md_revision: draft_0.125
asset_id: POSE_09_PRONE_ARMS_KNEES_SUPPORTED
candidate_id: POSE_09_PRONE_ARMS_KNEES_SUPPORTED_v001
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_09_PRONE_ARMS_KNEES_SUPPORTED_v001/POSE_09_PRONE_ARMS_KNEES_SUPPORTED_v001.png"
checksum_sha256: null
qa_status: NO_OUTPUT
```

## Authorization and lineage

The user requested the next planned pose after approving POSE_08 v002. This authorizes one POSE_09 v001 candidate. The repository has no registered real-human source for this exact hands-and-knees articulation, so the pose is conservatively defined in text. No POSE_01–08, Expression, Shot, failed candidate or unreviewed image is used as a reference.

## Reference responsibilities

1. `OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg`
   - SHA-256: `3f50c08e2993aa8dd406abd093d24f8a581b6e1475aa4dd57bda3884fed3b745`
   - responsibility: exact approved left-three-quarter adult face, neutral expression and even natural skin.
   - must_not_define: body, pose, hair, clothing, hosiery, hands/feet, lighting or background.
2. `OWNER_BODY_LEFT_3Q_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_02_LEFT_3Q_v001/BODY_02_LEFT_3Q_v001.png`
   - SHA-256: `f364b5c9b398c0c786964ffb8932707c7d657f997b8344abdd31a47b4322f4aa`
   - responsibility: approved 168 cm / 60 kg left-three-quarter body proportions, limb/hand/foot scale and unchanged Calibration Outfit, including its scoped 15D matte nude appearance.
   - must_not_define: new face identity, quadruped articulation, reusable hosiery/nail Material Canon, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - SHA-256: `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`
   - responsibility: Hairstyle-A near-center part, controlled crown volume, long straight dark-brown structure and tapered ends.
   - must_not_define: face, skin, body, pose, clothing, hosiery, hands/feet, lighting or background.

Reference budget: 3 approved scoped references. No previous generated Pose is attached. A matching real-motion source is unavailable and this coverage gap is explicit.

## Authoritative candidate scope

- approximately 45-degree left-three-quarter hands-and-knees support view;
- both palms flat beneath the shoulders, fingers naturally separated, arms straight with relaxed elbows and no hyperextension;
- both knees on one floor plane beneath the hips, with natural pressure and no floating contact;
- lower legs directed backward, insteps resting naturally on the floor;
- long neutral spine close to horizontal, level pelvis and aligned head/neck;
- balanced, clinical joint-calibration posture without deep lumbar arch, rounded back, hip lift or performative gesture.

The candidate must not define permanent identity/body/hair, outfit design, reusable hosiery/material/nail color, other poses, lighting or background.

## Prompt assembly

```text
Use case: photorealistic adult ergonomic joint-position reference.
Asset: exactly one POSE_09_PRONE_ARMS_KNEES_SUPPORTED v001 candidate, REVIEW_REQUIRED.

Reconstruct independently from the three scoped reference images. Image 1 defines only the exact approved left-three-quarter adult face and neutral expression. Image 2 defines only the approved 168 cm / 60 kg body proportions, limb scale and unchanged approved calibration clothing. Image 3 defines only Hairstyle A. Do not use or imitate any previous generated pose.

Show one adult woman in a neutral hands-and-knees tabletop support position on a seamless studio floor, viewed from approximately 45 degrees at her left side. Both palms are flat under the shoulders with fingers naturally separated. Arms are straight and relaxed; elbows are not locked backward. Both knees contact the same floor plane directly under the hips. Hips and knees are near right angles. Both lower legs extend backward with the insteps resting naturally on the floor. Keep the spine long, neutral and nearly horizontal, pelvis level, shoulders level, and head/neck aligned; turn the face only slightly toward camera so the approved three-quarter identity remains readable.

Keep the approved face, body, Hairstyle A and calibration clothing unchanged. The light-nude sheer 15D matte textile remains one continuous garment across all visible thighs, knees, calves, ankles, heels, insteps and toes, with real translucent fabric response rather than bare skin or glossy coating.

Full head, both hands, all fingers, both knees, lower legs and both complete feet inside an exact 3:4 vertical frame. Neutral light-gray seamless studio, soft even white-balanced light, natural 70–85 mm perspective at torso height. No mat, furniture, props, text or watermark. No deep back arch, rounded back, lifted pelvis, twisted torso, crossed limbs, floating joints, duplicated or missing fingers/toes, merged limbs, plastic skin or sexualized presentation.
```

## Generation attempts

### Attempt 1

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references: all three declared approved scoped references; no previous Pose image.
- request_id: `d84ec60c-916d-43dd-b098-22228ab0f19b`
- next action: one concise retry framed as a physical-therapy tabletop posture; retain only joint placement and inherit the unchanged visible outfit from Image 2 without expanded material wording.

### Attempt 2

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references: the same three declared approved scoped references; no previous Pose image.
- request_id: `f75641b4-cfe7-448b-8324-672eb8bd0847`
- decision: stop built-in retries; preserve the requested pose and approved outfit contract, and do not switch to CLI/API without explicit user authorization.

## QA status

No raster output exists, so visual QA cannot be performed. Status: `GENERATION_BLOCKED_NO_OUTPUT`; the item cannot be reviewed, promoted or used downstream.

## Subsequent user correction

After both v001 attempts produced no output, the user changed the required foot contact for any future POSE_09 attempt:

- remove the former instep-on-floor requirement;
- both forefeet/toe pads contact the floor;
- toes flex naturally at the metatarsophalangeal joints;
- both heels remain raised;
- reject insteps lying flat, floating toe contact, broken ankle continuity or added support geometry.

This correction does not rewrite the historical v001 prompt or authorize another generation. Any future attempt must use a new candidate version and the revised `draft_1.138` pose contract.
