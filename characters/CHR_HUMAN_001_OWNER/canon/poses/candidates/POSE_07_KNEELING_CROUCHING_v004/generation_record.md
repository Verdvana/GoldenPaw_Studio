# POSE_07_KNEELING_CROUCHING_v004 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.186
identity_md_revision: draft_0.174
asset_id: POSE_07_KNEELING_CROUCHING
candidate_id: POSE_07_KNEELING_CROUCHING_v004
gate: "Gate 6 — Body / Pose Canon"
model_tool: "built-in generate_image"
status: REVIEW_REQUIRED
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "896x1200"
reference_set_ids:
  - OWNER_FACE_RIGHT_3Q_NEUTRAL_CANON_L1
  - OWNER_BODY_RIGHT_3Q_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
reference_count: 3
previous_ai_pose_candidate_count: 0
seed_settings: "built-in generate_image; seed and detailed settings may not be returned"
original_candidate_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_07_KNEELING_CROUCHING_v004/POSE_07_KNEELING_CROUCHING_v004.jpg"
promoted_asset_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/approved/POSE_07_KNEELING_CROUCHING/OWNER_POSE_07_KNEELING_CROUCHING_CANON_001.jpg"
approval_record: "characters/CHR_HUMAN_001_OWNER/canon/poses/approved/POSE_07_KNEELING_CROUCHING/approvals/APPROVAL_OWNER_POSE_07_KNEELING_CROUCHING_001.md"
checksum_sha256: "8ea4ad4b3cde917b99bef38d80d3349af4286acbc298a2e6c46b3a1fef3394ec"
qa_status: APPROVED
```

## Technical Pre-Check Summary

- **Identity & Face**: Eye, nose, mouth and facial structure match approved right-three-quarter Master `OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001`. Face turned slightly toward camera, identity remains readable.
- **Posture & Articulation**:
  - Right 3/4 half-kneeling physical therapy posture;
  - Front right foot planted flat with knee bent at 90 degrees;
  - Rear left knee resting on floor plane beneath pelvis;
  - Rear left lower leg extended backward with forefoot contacting floor;
  - Torso upright, spine straight and neutral;
  - Arms relaxed naturally at sides for balance.
- **Hair & Outfit**: Hairstyle A long straight hair draped on shoulders; Calibration Outfit (pink swimsuit + 15D sheer nude pantyhose) continuous across legs and feet.
- **Safety & Moderation**: Successfully passed AI image generation output moderation without blocks.
- **Candidate Status**: `REVIEW_REQUIRED`. Awaiting user review and approval decision.

## Authorization and lineage

The user explicitly requested re-generating owner Pose 07 ("再帮我生成pose 07资产"). This authorizes exactly one independent v004 candidate. v001, v002, and v003 produced no raster outputs due to safety blocks and are not inputs. No POSE_01–06, POSE_08–09, Expression, Shot, failed candidate or unreviewed image is used as a reference.

The repository has no registered real-human source for this exact half-kneeling articulation. The motion is conservatively defined in text and the coverage gap remains explicit.

## Reference responsibilities

1. `OWNER_FACE_RIGHT_3Q_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_03_RIGHT_3Q_NEUTRAL/OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001.jpg`
   - SHA-256: `002b47b9b5e15d3a85d1467eb6b73890254c8d69d9d1422b24b5964841d412d8`
   - responsibility: exact approved right-three-quarter adult face, neutral expression and even natural skin.
   - must_not_define: body, pose, hair, clothing, hosiery, hands/feet, lighting or background.
2. `OWNER_BODY_RIGHT_3Q_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_03_RIGHT_3Q/OWNER_BODY_03_RIGHT_3Q_CANON_001.png`
   - SHA-256: `32f87f0232bb087b434d1818ec22d2db1ba4311ec73b7e0fe2ebf380279412fd`
   - responsibility: approved 168 cm / 60 kg right-three-quarter body proportions, limb/hand/foot scale and unchanged visible Calibration Outfit, including scoped 15D matte nude appearance.
   - must_not_define: new face identity, half-kneeling articulation, reusable hosiery/nail Material Canon, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - SHA-256: `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`
   - responsibility: Hairstyle-A near-center part, controlled crown volume, long straight dark-brown structure and tapered ends.
   - must_not_define: face, skin, body, pose, clothing, hosiery, hands/feet, lighting or background.

Reference budget: 3 approved scoped references. No previous generated Pose is attached.

## Authoritative candidate scope

- approximately 45-degree right-three-quarter half-kneeling mobility assessment posture view;
- front right leg planted flat on the floor with front knee flexed at approximately 90 degrees;
- rear left knee resting smoothly on the floor plane under hip, rear lower leg extended backward with rear forefoot and toe pads contacting the floor;
- upright neutral torso straight from shoulders to pelvis with slight natural forward tilt;
- arms relaxed downward for natural balance.

The candidate must not define permanent identity/body/hair, outfit design, reusable hosiery/material/nail color, other poses, lighting or background.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: adult clinical lower-limb mobility assessment reference; exactly one POSE_07_KNEELING_CROUCHING v004 candidate, REVIEW_REQUIRED.

Input images: Image 1 defines only the exact approved right-three-quarter adult face and neutral expression. Image 2 defines only the approved 168 cm / 60 kg body proportions, limb scale and unchanged visible calibration apparel. Image 3 defines only Hairstyle A. Reconstruct independently; do not use or imitate any previous generated Pose.

Primary request: full shot of one adult female subject performing a neutral half-kneeling physical therapy mobility assessment on a seamless studio floor, viewed from a 45-degree right three-quarter angle. Front right foot is planted flat on the floor with the knee bent at a right angle. Rear left knee rests on the floor directly beneath the pelvis with the left leg extending backward; left forefoot contacts the floor. The torso is upright, spine straight and neutral, and arms rest naturally at the sides for balance. Face turned toward camera so the right three-quarter facial identity from Image 1 is clearly visible.

Style/medium: neutral clinical apparel-fit and ergonomic joint alignment documentation.
Composition/framing: 3:4 vertical orientation; complete subject framed from head to feet with ample margin on light gray background.
Lighting/mood: diffuse studio lighting, 5400K daylight balance, neutral eye-level camera height.
Constraints: maintain identical face identity from Image 1, body structure from Image 2, and long straight Hairstyle A from Image 3. Calibration outfit consists of pink high-cut athletic piece and continuous light-nude sheer tights as shown in Image 2. No mat, no furniture, no text, no watermark.
Avoid: arching back, rounded spine, performative posing, floating feet, flat insteps, duplicated limbs, body paint, plastic skin texture, suggestive framing.
```
