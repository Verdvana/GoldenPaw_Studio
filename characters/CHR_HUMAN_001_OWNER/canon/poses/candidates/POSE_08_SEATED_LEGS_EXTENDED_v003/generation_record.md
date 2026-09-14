# POSE_08_SEATED_LEGS_EXTENDED_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.134
identity_md_revision: draft_0.122
asset_id: POSE_08_SEATED_LEGS_EXTENDED
candidate_id: POSE_08_SEATED_LEGS_EXTENDED_v003
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
  - HOS_15D_NUDE_MATTE_BAREFOOT
reference_count: 4
previous_ai_pose_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_08_SEATED_LEGS_EXTENDED_v003/POSE_08_SEATED_LEGS_EXTENDED_v003.png"
checksum_sha256: null
qa_status: NO_OUTPUT
```

## Authorization and lineage

The user clarified the intended geometry and authorized v003. v001 and v002 are user-rejected and are not supplied. This is an independent reconstruction from three approved L1 Masters plus one registered L0 hosiery material source. No previous Pose, Expression or Shot pixels are used.

## Reference responsibilities

1. `OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg`
   - SHA-256: `3f50c08e2993aa8dd406abd093d24f8a581b6e1475aa4dd57bda3884fed3b745`
   - responsibility: exact approved left-three-quarter adult face and neutral expression.
   - must_not_define: body, pose, hair, clothing, hosiery, feet, lighting or background.
2. `OWNER_BODY_LEFT_3Q_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_02_LEFT_3Q/OWNER_BODY_02_LEFT_3Q_CANON_001.png`
   - SHA-256: `f364b5c9b398c0c786964ffb8932707c7d657f997b8344abdd31a47b4322f4aa`
   - responsibility: approved 168 cm / 60 kg left-three-quarter body proportions, limb/foot scale, flesh-tone baseline and unchanged Calibration Outfit.
   - must_not_define: new face identity, seated articulation, reusable material/nail Canon, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - SHA-256: `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`
   - responsibility: Hairstyle-A part, volume, long straight dark-brown structure and tapered ends.
   - must_not_define: face, body, pose, clothing, hosiery, feet, lighting or background.
4. `HOS_15D_NUDE_MATTE_BAREFOOT`
   - path: `materials/hosiery/source_library/raw/15d_nude_matte/IMG_2562.jpg`
   - SHA-256: `2f869afc5af953b971b68621f7cbc7c3696a129774dec1838dfec0f0a0a15869`
   - responsibility: flesh-toned 15D matte/velvet textile behavior, tension and continuous coverage across heel, sole, forefoot and toe tips only.
   - must_not_define: source person, leg/foot anatomy, pose, skin identity, nail color, clothing, bed/fur, advertising text, lighting or background.

Reference budget: 4 scoped inputs; no v001/v002 or other generated Pose pixels.

## Authoritative candidate scope

- approximately 45-degree left-three-quarter torso/camera relationship;
- stable floor-seated pelvis and naturally upright torso;
- both legs fully extended and straight, knees not visibly bent;
- both ankles dorsiflexed to about 90 degrees so plantar surfaces face the camera;
- sole-dominant foot view with complete heel, arch, forefoot and toe-pad silhouettes;
- light hand support beside the hips.

## Prompt assembly

```text
Use case: photorealistic-natural
Asset type: adult ergonomic seated joint-position reference

Create exactly one POSE_08_SEATED_LEGS_EXTENDED v003 REVIEW_REQUIRED candidate independently from the four supplied references. Do not use or imitate v001, v002 or any generated pose.

Image 1 defines only the approved left-three-quarter adult face. Image 2 defines only the approved 168 cm / 60 kg body proportions, limb and foot scale, flesh-tone baseline and unchanged approved clothing. Image 3 defines only Hairstyle A. Image 4 defines only flesh-toned 15D matte textile tension and continuous coverage over heel, sole, forefoot and toe tips; ignore its person, anatomy, pose, bed, advertising text, lighting and background.

The adult figure sits on the seamless studio floor with the torso viewed from about 45 degrees on her left side. Pelvis stable and torso naturally upright; hands rest lightly beside the hips. Both legs extend straight toward the camera with knees fully extended and no visible bend. Both ankles are dorsiflexed to approximately 90 degrees: feet are perpendicular to the lower legs, and both plantar surfaces face the camera. The visible feet are sole-dominant—show both complete heels, arches, forefoot pads and toe pads; do not present the tops of the feet or toenails as the main view. Keep the two soles separate and unobstructed.

Keep the approved identity, body, Hairstyle A and clothing unchanged. Hosiery is flesh-toned, genuinely sheer 15D, matte/velvet, not white and not opaque. A subtle but readable textile veil and tension pattern continues from calves around heels across the complete soles, forefeet and toe tips. Preserve natural skin translucency beneath it. No bare soles, exposed toe pads, ankle cutoff, white socks, opaque toe cap, seam, band, painted coating, plastic gloss or body-paint appearance.

One complete figure in an exact 3:4 vertical frame, neutral light-gray seamless studio, soft even white-balanced light, natural 70–85 mm perspective. No chair, mat, props, bed, source text, watermark, bent knees, pointed feet, dropped ankles, crossed/merged legs, hidden sole, anatomy errors, logo or text. Candidate remains REVIEW_REQUIRED.
```

## Generation attempts

### Attempt 1

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references: the four declared scoped references; no v001/v002 or other Pose image.
- request_id: `f6b95047-730d-4973-854e-199bed36042e`
- next action: one concise clinical retry retaining straight legs, approximately 90-degree ankles, both soles toward camera and continuous flesh-toned 15D textile.

### Attempt 2

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references: the same four declared scoped references; no v001/v002 or other Pose image.
- request_id: `f344e5c5-48cb-4244-b329-c1c981e38262`
- decision: stop built-in retries; do not alter the requested geometry/material contract and do not switch to CLI/API without explicit user authorization.

## QA status

No raster output exists. Visual QA cannot be performed. Status: `GENERATION_BLOCKED_NO_OUTPUT`.
