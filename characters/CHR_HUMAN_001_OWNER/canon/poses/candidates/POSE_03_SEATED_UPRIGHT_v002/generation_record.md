# POSE_03_SEATED_UPRIGHT_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.109
identity_md_revision: draft_0.97
asset_id: POSE_03_SEATED_UPRIGHT
candidate_id: POSE_03_SEATED_UPRIGHT_v002
gate: "Gate 6 — Body / Pose Canon"
model_tool: "built-in image_gen"
status: USER_REJECTED_SCOPED_REVISION
approval_status: REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_BODY_FRONT_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
reference_count: 3
previous_ai_pose_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_03_SEATED_UPRIGHT_v002/POSE_03_SEATED_UPRIGHT_v002.png"
checksum_sha256: "fab9c2075ff26ef0f73ac75c0912a8801a2b275b52c4f7ec2bdbcb72560832e3"
qa_status: FAIL_USER_REVISION_MISSING_BURGUNDY_TOENAIL_POLISH
```

## Authorization and lineage

The user rejected v001 only for face identity/skin pollution and authorized a clean independent regeneration. v001 is not supplied. This candidate is reconstructed in parallel from three approved scoped L1 Masters; no generated Pose, Expression, historical Body candidate or Shot image is used.

## Reference responsibilities

1. `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
   - responsibility: exact approved front facial identity, facial geometry, neutral skin tone and clean natural skin presentation.
   - must_not_define: body, seated pose, hairstyle, outfit, hosiery, stool, lighting or background.
2. `OWNER_BODY_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg`
   - responsibility: approved 168 cm / 60 kg body proportions, head-to-body scale, limb lengths, waist/hip ratio, foot scale, Calibration Outfit and scoped 15D matte nude appearance.
   - must_not_define: permanent face refinement, seated articulation, other Pose components, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - responsibility: approved front Hairstyle-A part, volume, straight panels, length and tapered ends.
   - must_not_define: face, skin, body, pose, outfit, hosiery, stool, lighting or background.

Reference budget: 3 approved Masters. `POSE_03 v001` is rejected and excluded; its successful posture is represented only by written joint constraints.

## Authoritative candidate scope

- front-facing upright seated articulation;
- centered pelvis, vertical torso, natural hip/knee flexion, lower-leg alignment, flat feet and relaxed hands;
- stable joint relationships under approved identity/body/hair Masters.

## Must not define

- permanent face/body geometry, Hairstyle A, Expression Canon, skin tone or age;
- Calibration Outfit design, reusable hosiery Material Canon or episode wardrobe;
- reusable stool/environment design, other Pose components or complete release.

## Prompt assembly

```text
Use case: photorealistic-natural
Asset type: adult technical upright-seated joint calibration reference

Create exactly one new POSE_03_SEATED_UPRIGHT v002 candidate for adult character CHR_HUMAN_001_OWNER, following OWNER_L1_GENERATION_SPEC draft_1.109 and IDENTITY draft_0.97. Do not use or imitate v001.

Image 1 is the sole authority for the exact approved front face: preserve its recognizable facial geometry, feature relationships, neutral skin tone and clean natural skin presentation. Image 2 defines only the approved 168 cm / 60 kg body proportions, head-to-body scale, limb lengths, waist/hip ratio, foot scale, Calibration Outfit and scoped 15D matte nude appearance; it must not alter the face. Image 3 defines only Hairstyle A and must not alter face or skin.

Show a straight-on full-body upright seated pose on a simple featureless neutral-gray backless studio stool. Pelvis centered and neutral, torso naturally vertical, head level, gaze calmly forward, mouth naturally closed, shoulders lowered. Both empty hands rest lightly and symmetrically on the upper thighs with relaxed distinct fingers. Thighs point forward at natural hip width, knees separated and bent near 90 degrees, lower legs descend near vertically, and both uncrossed feet rest flat on one floor plane. Preserve realistic seated soft-tissue compression without changing body mass or limb lengths.

Face and skin correction: match Image 1 directly, including the approved eyes, nose, lips, jaw, chin, facial width and adult age. Maintain even neutral skin with subtle real texture. No patchy redness, sensitive blotches, dirty gray/brown areas, asymmetric color patches, mottling, bruised-looking marks, acne-like artifacts, smeared makeup, over-sharpening, plastic smoothing or inherited generated-image blemishes.

Technical studio photograph, exact 3:4 portrait, entire hair, hands, seat contact, lower legs and feet visible, level 70–85 mm-equivalent perspective, neutral light-gray seamless background and broad even 5200–5600 K light.

Use only the established calibration clothing from Image 2: plain opaque pink one-piece athletic fit garment, continuous light-nude closed-foot 15D matte/velvet sheer pantyhose, no shoes. Textile remains continuous over ankles, heels, insteps and toes without ankle breaks, toe bands, bare toes, plastic gloss or body-paint appearance.

Correct stool is support only. Correct ordinary adult anatomy; no crossed legs, splayed glamour pose, slouch, lean, arch, tiptoes, dangling feet, fused limbs, broken joints, duplicated heels, extra/missing digits, props, text, watermark, collage or border. This candidate defines only upright-seated articulation and must not redefine identity, body, hair, garment, material, stool or environment. Status REVIEW_REQUIRED, not approved Canon.
```

## QA status

### Attempt 1

- generated_at: `2026-09-13`
- built-in output: `/home/verdvana/.codex/generated_images/01a09ab1-cec4-7f30-9bd8-80cb6ab0e147/exec-e612507e-1fe2-4c13-857a-9ba83b58f1f2.png`
- project candidate: `characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_03_SEATED_UPRIGHT_v002/POSE_03_SEATED_UPRIGHT_v002.png`
- result: one 1086×1448 exact-3:4 PNG generated and saved in the candidate directory.
- lineage: approved FACE_01 + BODY_01 + HAIR_A_01 L1 Masters; no v001, other generated Pose, Expression, historical Body candidate or Shot input.
- technical QA: pass for review; see `QA.md`.

Final current status: `REVIEW_REQUIRED`. The raster is not approved or promoted and cannot be used as Pose Canon until explicit user approval.

## User review

- decision: `REVISE / NOT APPROVED`
- accepted as text-only guidance: face, clean skin, upright seated pose and all other visible attributes.
- required correction: stable burgundy toenail polish is missing; it must show naturally and softly beneath the continuous 15D nude pantyhose.
- downstream rule: v002 must not be supplied to v003 or used downstream.
