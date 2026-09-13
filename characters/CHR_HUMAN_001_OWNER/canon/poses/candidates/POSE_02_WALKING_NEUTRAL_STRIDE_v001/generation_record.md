# POSE_02_WALKING_NEUTRAL_STRIDE_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.105
identity_md_revision: draft_0.93
asset_id: POSE_02_WALKING_NEUTRAL_STRIDE
candidate_id: POSE_02_WALKING_NEUTRAL_STRIDE_v001
gate: "Gate 6 — Body / Pose Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_BODY_FRONT_CANON_L1
  - OWNER_L0_WALKING_ARTICULATION
reference_count: 2
previous_ai_pose_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_02_WALKING_NEUTRAL_STRIDE_v001/POSE_02_WALKING_NEUTRAL_STRIDE_v001.png"
pixel_storage_status: "MOVED_TO_CANON"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/approved/POSE_02_WALKING_NEUTRAL_STRIDE/OWNER_POSE_02_WALKING_NEUTRAL_STRIDE_CANON_001.png"
current_promoted_checksum_sha256: "b5ae6ab402a00249897a3458c8d931c32f0882c2f74d2869e570122c74b5f42a"
checksum_sha256: "b5ae6ab402a00249897a3458c8d931c32f0882c2f74d2869e570122c74b5f42a"
qa_status: PASS_TECHNICAL_REVIEW_REQUIRED
```

## Authorization and lineage

The user explicitly authorized generation after approving the POSE_01 reuse. This candidate is generated independently from the approved BODY_01 Master and one L0 walking-articulation source. POSE_01 is not used as a continuity reference, and no failed Pose, historical Body candidate, Expression or Shot image is supplied.

## Reference responsibilities

1. `OWNER_BODY_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg`
   - responsibility: approved 168 cm / 60 kg body identity and proportions, visible front face, Hairstyle A, foot scale, Calibration Outfit and scoped 15D matte nude appearance.
   - must_not_define: walking phase, stride length, dynamic balance, other Pose components, lighting or background.
2. `OWNER_L0_WALKING_ARTICULATION` / `L0_OWNER_003`
   - path: `characters/CHR_HUMAN_001_OWNER/source/identity/raw/4.jpg`
   - responsibility: natural frontal walking stride, alternating lower-limb articulation and plausible moving balance only.
   - must_not_define: identity, permanent body proportions, hair, black dress, black tights, shoes, shopping bags, hand shape under load, camera, lighting, parking-garage environment or hosiery material.

Reference budget: 2 images, the smallest registered set covering approved identity/body and real walking articulation.

## Authoritative candidate scope

- neutral forward-walking mid-stride articulation;
- natural opposite-leg progression, modest stride length and believable dynamic weight transfer;
- restrained reciprocal arm swing with relaxed empty hands;
- stable head, torso, pelvis, knee, ankle and foot relationships under the approved body identity.

## Must not define

- permanent face/body geometry, Hairstyle A, Expression Canon, skin tone or age;
- Calibration Outfit design, reusable hosiery Material Canon or episode wardrobe;
- bags, shoes, dress, parking-garage environment or any visual property of the L0 source outside gait;
- any other Pose component or the complete release.

## Prompt assembly

```text
Use case: photorealistic-natural
Asset type: adult technical walking-gait character reference

Create exactly one POSE_02_WALKING_NEUTRAL_STRIDE candidate for adult character CHR_HUMAN_001_OWNER, following OWNER_L1_GENERATION_SPEC draft_1.105 and IDENTITY draft_0.93. Image 1 defines the approved person, 168 cm / 60 kg body proportions, visible front face, Hairstyle A, foot scale and established calibration clothing. Image 2 defines only a natural front-facing walking stride and alternating lower-limb articulation; ignore and replace all of its clothing, tights, shoes, shopping bags, hand loading, cars, parking-garage background, camera, lighting, face and body proportions.

Show one full-body front-facing mid-stride technical gait reference. Use a modest ordinary walking step: one leg advancing with a softly extended knee and heel approaching or contacting the floor, the other leg trailing naturally with heel lifting and forefoot support; hips and shoulders show only normal restrained counter-rotation. Head remains level, gaze forward, mouth naturally closed. Arms swing gently opposite the legs, elbows soft, wrists neutral, both hands empty and relaxed. Preserve believable balance and ground contact; no running, dancing, posing or exaggerated stride.

Preserve the exact approved adult woman, natural 168 cm / 60 kg proportions, head-to-body scale, torso length, waist/hip ratio, arm and leg lengths, thigh/calf volume, foot size, front face and Hairstyle A from Image 1. Do not slim, elongate, shrink the head, exaggerate curves or redesign identity.

Technical studio photograph, exact 3:4 portrait, entire hair, hands and both feet visible with 5–8% margins, level 70–85 mm-equivalent perspective, neutral light-gray seamless backdrop, broad soft neutral light and realistic unretouched texture.

Keep Image 1's established calibration clothing: plain opaque pink one-piece athletic fit garment, continuous light-nude closed-foot 15D matte/velvet sheer pantyhose, no shoes. The textile stays continuously visible from waist through ankles, heels, insteps and toes without ankle breaks, toe bands, bare toes, plastic gloss or body-paint appearance.

Correct ordinary adult anatomy and gait. No crossed or fused legs, floating foot, broken knee/ankle, duplicated heel, missing or extra fingers/toes, shopping bags, props, furniture, text, watermark, collage or border. This candidate defines only neutral walking articulation; it must not define permanent identity, body, hair, garment or material. Status REVIEW_REQUIRED, not approved Canon.
```

## QA status

### Attempt 1

- generated_at: `2026-09-13`
- built-in output: `/home/verdvana/.codex/generated_images/01a09ab1-cec4-7f30-9bd8-80cb6ab0e147/exec-53f2c170-4b5b-4c0d-94d0-63183d294773.png`
- project candidate: `characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_02_WALKING_NEUTRAL_STRIDE_v001/POSE_02_WALKING_NEUTRAL_STRIDE_v001.png`
- result: one 1086×1448 exact-3:4 PNG generated and saved in the candidate directory.
- lineage: BODY_01 Master plus `L0_OWNER_003` walking articulation only; no POSE_01, failed Pose, historical Body candidate, Expression or Shot input.
- technical QA: pass for review; see `QA.md`.

## User approval and promotion

On 2026-09-13 the user stated “批准 下一项。” The exact candidate raster was moved, not copied, to `characters/CHR_HUMAN_001_OWNER/canon/poses/approved/POSE_02_WALKING_NEUTRAL_STRIDE/OWNER_POSE_02_WALKING_NEUTRAL_STRIDE_CANON_001.png`. Its checksum remains unchanged. Approval is limited to neutral walking articulation, reciprocal arm-leg gait and dynamic floor contact; the complete `owner_v1.0` remains unlocked.
