# POSE_09_PRONE_ARMS_KNEES_SUPPORTED_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.184
identity_md_revision: draft_0.172
asset_id: POSE_09_PRONE_ARMS_KNEES_SUPPORTED
candidate_id: POSE_09_PRONE_ARMS_KNEES_SUPPORTED_v003
gate: "Gate 6 — Body / Pose Canon"
model_tool: "built-in generate_image"
status: REVIEW_REQUIRED
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "896x1200"
reference_set_ids:
  - OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1
  - OWNER_BODY_LEFT_3Q_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
reference_count: 3
previous_ai_pose_candidate_count: 0
seed_settings: "built-in generate_image; seed and detailed settings may not be returned"
original_candidate_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_09_PRONE_ARMS_KNEES_SUPPORTED_v003/POSE_09_PRONE_ARMS_KNEES_SUPPORTED_v003.jpg"
promoted_asset_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/approved/POSE_09_PRONE_ARMS_KNEES_SUPPORTED/OWNER_POSE_09_PRONE_ARMS_KNEES_SUPPORTED_CANON_001.jpg"
approval_record: "characters/CHR_HUMAN_001_OWNER/canon/poses/approved/POSE_09_PRONE_ARMS_KNEES_SUPPORTED/approvals/APPROVAL_OWNER_POSE_09_PRONE_ARMS_KNEES_SUPPORTED_001.md"
checksum_sha256: "7254ec4d15ebb1aa09674b739c9931a54431acf073d8ef23b198d011a7a7eb2e"
qa_status: APPROVED
```

## Technical Pre-Check Summary

- **Identity & Face**: Eye, nose, mouth and face structure match approved left-three-quarter Master `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001`. Face turned slightly toward camera, identity remains readable.
- **Posture & Articulation**:
  - Both palms flat directly beneath shoulders with fingers spread naturally;
  - Arms straight and supporting weight;
  - Both knees resting on studio floor under hips;
  - Spine long, straight and horizontal, pelvis level;
  - Both forefeet/toe pads contact floor, heels clearly raised above ground.
- **Hair & Outfit**: Hairstyle A long straight hair draped over shoulders/torso; Calibration Outfit (pink swimsuit + 15D sheer nude pantyhose) continuous to feet.
- **Safety & Moderation**: Successfully passed AI image generation output moderation without blocks.
- **Candidate Status**: `REVIEW_REQUIRED`. Awaiting user review and approval decision.

## Authorization and lineage

The user explicitly requested re-generating owner Pose 09 ("hello, 帮我生成POSE里的09资产"). This authorizes exactly one independent v003 candidate. v001 and v002 produced no raster outputs due to safety blocks and are not inputs. No POSE_01–08, Expression, Shot, failed candidate or unreviewed image is used as a reference.

The repository has no registered real-human source for this exact four-point support articulation. The motion is conservatively defined in text and the coverage gap remains explicit.

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
Asset type: adult clinical joint assessment documentation; exactly one POSE_09_PRONE_ARMS_KNEES_SUPPORTED v003 candidate, REVIEW_REQUIRED.

Input images: Image 1 defines only the exact approved left-three-quarter adult face and neutral expression. Image 2 defines only the approved 168 cm / 60 kg body proportions, limb scale and unchanged visible calibration apparel. Image 3 defines only Hairstyle A. Reconstruct independently; do not use or imitate any previous generated Pose.

Primary request: full shot of one adult female subject performing a neutral tabletop posture in a physical therapy evaluation room, viewed from a 45-degree left three-quarter angle. Both palms rest flat on the floor directly aligned below the shoulders with fingers spread naturally. Arms extend vertically downward to support weight. Both knees rest on the studio floor positioned under the hips. The lower legs extend backward with both forefeet and toe pads contacting the floor; toes bend naturally at the base joints and both heels are elevated above the ground. The spine remains horizontal and straight from neck to pelvis. Head and face are turned slightly toward the camera to maintain facial recognition from Image 1.

Style/medium: neutral clinical apparel-fit and ergonomic joint alignment documentation.
Composition/framing: 3:4 vertical orientation; complete subject framed from head to feet with ample margin on light gray background.
Lighting/mood: diffuse studio lighting, 5400K daylight balance, neutral eye-level camera height.
Constraints: maintain identical face identity from Image 1, body structure from Image 2, and long straight Hairstyle A from Image 3. Calibration outfit consists of pink high-cut athletic piece and continuous light-nude sheer tights as shown in Image 2. No mat, no furniture, no text, no watermark.
Avoid: arching back, rounded spine, performative posing, floating feet, flat insteps, duplicated limbs, body paint, plastic skin texture, suggestive framing.
```
