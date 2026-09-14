# POSE_08_SEATED_LEGS_EXTENDED_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.135
identity_md_revision: draft_0.123
asset_id: POSE_08_SEATED_LEGS_EXTENDED
candidate_id: POSE_08_SEATED_LEGS_EXTENDED_v002
gate: "Gate 6 — Body / Pose Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTED_WITH_KNOWN_LIMITATIONS
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1
  - OWNER_BODY_LEFT_3Q_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 4
previous_ai_pose_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/approved/POSE_08_SEATED_LEGS_EXTENDED/OWNER_POSE_08_SEATED_LEGS_EXTENDED_CANON_001.png"
checksum_sha256: "e9ef5af93a902f39a98700400e86495754c8c60901e051291e5f43110419f1ee"
qa_status: APPROVED_WITH_KNOWN_GEOMETRY_MATERIAL_LIMITATIONS
```

## Authorization and lineage

The user rejected v001 and authorized an independent v002 with three explicit corrections: approximately 45-degree side view, naturally relaxed feet/joints, and clearly visible 15D pantyhose texture on legs and toes. v001 and every other Pose/Expression/Shot image are excluded from the generation inputs. No registered real-human source defines this seated articulation; the pose is specified in text.

## Reference responsibilities

1. `OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg`
   - SHA-256: `3f50c08e2993aa8dd406abd093d24f8a581b6e1475aa4dd57bda3884fed3b745`
   - responsibility: exact approved left-three-quarter face, calm neutral expression and even natural skin.
   - must_not_define: body, seated pose, hair, clothing, hosiery, feet, lighting or background.
2. `OWNER_BODY_LEFT_3Q_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_02_LEFT_3Q/OWNER_BODY_02_LEFT_3Q_CANON_001.png`
   - SHA-256: `f364b5c9b398c0c786964ffb8932707c7d657f997b8344abdd31a47b4322f4aa`
   - responsibility: approved 168 cm / 60 kg left-three-quarter body proportions, limb/foot scale, light-nude color baseline and unchanged Calibration Outfit.
   - must_not_define: new face identity, seated articulation, reusable material/nail Canon, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - SHA-256: `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`
   - responsibility: Hairstyle-A part, controlled crown volume, long straight dark-brown structure and tapered ends.
   - must_not_define: face, skin, body, pose, clothing, hosiery, feet, lighting or background.
4. `HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001`
   - path: `materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png`
   - SHA-256: `36fba906cfb47002f6669133b336b5d47b25c1763450db8fd4fbce7412eb8948`
   - responsibility: clearly readable sheer 15D matte/velvet textile presence, transparency, continuous leg-to-foot coverage and softened toe visibility only.
   - must_not_define: pale/white color cast, pose, body/foot anatomy, skin pigmentation, nail color, clothing, shoes, background, watermark or floor contact.

Reference budget: 4 scoped references; no v001 or other generated Pose pixels.

## Authoritative candidate scope

- approximately 45-degree left-three-quarter seated viewpoint;
- stable floor-seated pelvis and naturally upright torso;
- both legs extended forward with relaxed, unlocked knees and clear separation;
- naturally relaxed ankles, feet and toes without forced pointing or rigid dorsiflexion;
- light hand support beside the hips.

## Prompt assembly

```text
Use case: photorealistic-natural
Asset type: adult ergonomic seated range-of-motion reference

Create exactly one POSE_08_SEATED_LEGS_EXTENDED v002 REVIEW_REQUIRED candidate. Reconstruct independently from the four supplied scoped references; do not use or imitate v001 or any other generated pose.

Image 1 defines only the exact approved left-three-quarter adult face and neutral expression. Image 2 defines the approved 168 cm / 60 kg left-three-quarter body proportions, limb/foot scale, light-nude color baseline and unchanged approved calibration clothing. Image 3 defines only Hairstyle A. Image 4 defines only visibly readable sheer 15D matte textile presence, transparency, continuous coverage and softened toe detail; ignore its pale color, original pose, anatomy, skin, nail color, shoes and background.

Show the adult figure seated directly on a seamless studio floor, viewed from approximately 45 degrees at her left side. Her pelvis is stable and torso naturally upright. Both legs extend forward in the same general direction with a small lateral and depth offset so both knees, ankles and feet remain separately visible. Keep the knees naturally soft rather than locked. Let both ankles, feet and toes rest naturally and loosely, with mild individual outward fall; do not point, stretch, curl or rigidly flex the feet. Hands rest lightly on the floor beside the hips.

Keep the approved body, face, Hairstyle A and clothing unchanged. Across the full visible thighs, knees, calves, ankles, heels, insteps and toes, show a clearly perceptible but sheer light-nude 15D matte/velvet textile veil. It must visibly soften skin and toe/nail detail while remaining transparent and flesh-toned. The same textile continues without ankle cutoff, naked toes, white socks, opaque toe caps, bands, seams, sprayed-white feet, plastic gloss or body-paint appearance. Burgundy toenails may be softly visible only beneath the textile.

Full figure inside an exact 3:4 vertical frame, neutral light-gray seamless studio, soft even white-balanced light, natural 70–85 mm perspective. No chair, mat, props, crossed legs, merged feet, extreme lean, dramatic gesture, anatomy errors, text or watermark. Candidate remains REVIEW_REQUIRED.
```

## Generation attempts

### Attempt 1

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references: all four declared scoped references; no v001 or other Pose image.
- request_id: `6dbc7b57-46ae-4cfd-ab4c-81db6c74b18f`
- next action: one concise retry retaining only the 45-degree view, relaxed joints and Image-4 textile-coverage correction while inheriting approved presentation from Image 2.

### Attempt 2

- result: success; one PNG returned and stored at the declared candidate path.
- references: the same four scoped references; no v001 or other Pose image.
- prompt adjustment: concise 45-degree ergonomic pose, relaxed joints and continuous textile character inherited from Image 4.
- output: 1086×1448 exact 3:4 PNG.
- checksum_sha256: `e9ef5af93a902f39a98700400e86495754c8c60901e051291e5f43110419f1ee`

## QA status

The requested approximately 45-degree left-three-quarter view, relaxed knees/ankles/feet/toes and continuous visible textile coverage pass. The material color and optical density fail: the textile reads pale white and medium-opacity rather than light-nude 15D, and toenails read gray-white instead of muted burgundy beneath transparent fabric. Status: `FAIL_TECHNICAL_HOSIERY_COLOR_OPACITY`. Do not promote or use downstream.

## User approval and promotion

After v003 produced no output, the user explicitly instructed: “那就先登记v002吧”. v002 is approved only for the visible approximately 45-degree left-three-quarter floor-seated articulation, stable torso, separated forward legs, naturally relaxed knee/ankle/foot/toe joints and light hand support beside the hips.

Known limitations are excluded from authority: legs are not fully straight; feet are not approximately 90 degrees with sole-dominant camera presentation; hosiery is too pale/white and too opaque; toenails read gray-white. These properties must not be copied as pose, material, color, denier, foot-treatment or nail-color truth.

- approval_id: `APPROVAL_OWNER_POSE_08_SEATED_LEGS_EXTENDED_001`
- physical operation: `MOVE`
- original candidate path: `characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_08_SEATED_LEGS_EXTENDED_v002/POSE_08_SEATED_LEGS_EXTENDED_v002.png`
- current approved path: `characters/CHR_HUMAN_001_OWNER/canon/poses/approved/POSE_08_SEATED_LEGS_EXTENDED/OWNER_POSE_08_SEATED_LEGS_EXTENDED_CANON_001.png`
- original/current SHA-256: `e9ef5af93a902f39a98700400e86495754c8c60901e051291e5f43110419f1ee`
- candidate raster retained: `NO`
