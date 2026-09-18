# POSE_01_RELAXED_STANDING_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.103
identity_md_revision: draft_0.91
asset_id: POSE_01_RELAXED_STANDING
candidate_id: POSE_01_RELAXED_STANDING_v002
gate: "Gate 6 — Body / Pose Canon"
model_tool: "built-in image_gen"
status: NO_OUTPUT_MODERATION_BLOCKED
approval_status: NOT_GENERATED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "PENDING"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_BODY_FRONT_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
reference_count: 3
previous_ai_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_01_RELAXED_STANDING_v002/POSE_01_RELAXED_STANDING_v002.png"
checksum_sha256: "PENDING"
qa_status: NOT_APPLICABLE_NO_OUTPUT
```

## Authorization and lineage

The user explicitly requested the next asset after the prior attempt produced no image. This is a fresh parallel construction from three approved scoped L1 Masters. `POSE_01_RELAXED_STANDING_v001`, all Expression images, historical Body candidates and Shot images are excluded.

## Reference responsibilities

1. `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
   - responsibility: approved front facial identity and neutral adult facial geometry.
   - must_not_define: pose, body proportions, hair, outfit, hosiery, camera, lighting or background.
2. `OWNER_BODY_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v009/BODY_01_FRONT_v009.jpg`
   - responsibility: approved 168 cm / 60 kg body identity, head-to-body scale, limb lengths, waist/hip ratio and foot scale; its hosiery scope is limited to the existing 15D matte nude combination.
   - must_not_define: relaxed-pose articulation, new permanent geometry, any other hosiery combination, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - responsibility: approved front Hairstyle-A structure, length, volume, part and tapered ends.
   - must_not_define: face, skin, expression, body, pose, outfit, hosiery, lighting or background.

Reference budget: 3 images. All are approved Masters with isolated duties; there is no previous-candidate input.

## Authoritative candidate scope

- straight-on relaxed standing articulation;
- lowered shoulders, soft elbows, loose hands and natural fingers;
- neutral pelvis, natural two-leg support, non-hyperextended knees and uncrossed grounded feet;
- stable joint relationships under the approved body identity.

## Must not define

- permanent face or body geometry, height, weight, head-to-body ratio, limb lengths or waist/hip ratio;
- Hairstyle-A design, Expression Canon, skin tone or age;
- Calibration Outfit design or episode wardrobe;
- reusable hosiery Material Canon;
- lighting, background, camera style, artifacts, other Pose components or the complete release.

## Prompt assembly

```text
Use case: photorealistic-natural
Asset type: adult apparel-fit and body-joint calibration reference

Create exactly one POSE_01_RELAXED_STANDING candidate for adult character CHR_HUMAN_001_OWNER, following OWNER_L1_GENERATION_SPEC draft_1.103 and IDENTITY draft_0.91. Use Image 1 only for the approved front face, Image 2 only for the approved 168 cm / 60 kg body proportions and foot scale, and Image 3 only for approved Hairstyle A. Do not copy or infer any property outside those declared duties.

Show a straight-on full-body relaxed standing posture: calm closed-mouth neutral expression, level head, lowered shoulders, arms resting with small breathing room, soft elbows, neutral wrists, loose hands, neutral pelvis, balanced natural support through both legs, knees straight without locking, and uncrossed feet fully contacting one level studio floor. Preserve the same adult woman, face, body proportions, limb lengths, waist/hip ratio and foot scale from the approved references.

Technical studio reference photograph, 3:4 portrait, entire hair, hands and feet visible with clear margins, level 70–85 mm-equivalent perspective, light-gray seamless backdrop, broad neutral soft light, realistic unretouched skin and textile texture.

Keep the established calibration garment exactly: plain opaque pink one-piece fit garment, continuous sheer nude 15D matte/velvet pantyhose from waist through heels and toes, no shoes. The legwear remains visibly textile and continuous over both feet without ankle or toe boundaries, bare toes, plastic gloss or body-paint appearance.

Correct ordinary adult anatomy. No pose glamour, hip thrust, arched back, crossed legs, walking stride, props, furniture, text, logo, watermark, collage or border. This candidate defines only relaxed-standing articulation; it must not redefine identity, body, hair, expression, garment design, reusable hosiery material, lighting or background. Status REVIEW_REQUIRED, not approved Canon.
```

## QA status

### Attempt 1

- result: `NO_OUTPUT_MODERATION_BLOCKED`
- stage: output safety system
- category: `sexual`
- request_id: `1cce6480-c71d-44d3-9f51-7b34060badf5`
- prompt strategy: explicit adult apparel-fit and body-joint calibration context with the fixed three approved references and unchanged Calibration Outfit.
- action: no image or candidate was created. No CLI fallback or additional rewrite was attempted.

Final current status: no candidate raster, metadata or visual QA exists. `POSE_01_RELAXED_STANDING` remains unapproved and unusable downstream; `BODY_01_FRONT` is not promoted or aliased into Pose Canon.
