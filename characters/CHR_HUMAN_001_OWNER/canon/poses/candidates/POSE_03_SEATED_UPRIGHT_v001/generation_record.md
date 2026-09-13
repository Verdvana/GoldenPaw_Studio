# POSE_03_SEATED_UPRIGHT_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.107
identity_md_revision: draft_0.95
asset_id: POSE_03_SEATED_UPRIGHT
candidate_id: POSE_03_SEATED_UPRIGHT_v001
gate: "Gate 6 — Body / Pose Canon"
model_tool: "built-in image_gen"
status: USER_REJECTED
approval_status: REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_BODY_FRONT_CANON_L1
reference_count: 1
previous_ai_pose_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_03_SEATED_UPRIGHT_v001/POSE_03_SEATED_UPRIGHT_v001.png"
checksum_sha256: "097c9b451ba6d53fa476be5664f2a6c9a7f3a9f9cbda41adb8c3069210382d05"
qa_status: FAIL_USER_REJECTED_FACE_ITERATION_POLLUTION
```

## Authorization and lineage

The user explicitly approved POSE_02 and requested the next asset. No registered L0 seated articulation source exists. This candidate therefore uses only the approved BODY_01 Master plus a conservative written seated-joint specification. POSE_01, POSE_02 and all other generated Pose, Expression, historical Body candidate and Shot images are excluded.

## Reference responsibility

`OWNER_BODY_FRONT_CANON_L1`

- path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg`
- responsibility: approved adult identity, 168 cm / 60 kg front body geometry and proportions, visible front face, Hairstyle A, foot scale, Calibration Outfit and scoped 15D matte nude appearance.
- must_not_define: seated articulation, furniture design, other Pose components, lighting or background.

Reference budget: 1 image. Source-coverage gap: no L0 seated reference is registered, so seated articulation is a conservative design construction requiring user review.

## Authoritative candidate scope

- front-facing upright seated articulation;
- centered neutral pelvis, vertical torso and level head;
- natural hip/knee flexion, lower-leg alignment, flat foot contact and relaxed hand placement;
- stable joint relationships under the approved body identity.

## Must not define

- permanent face/body geometry, Hairstyle A, Expression Canon, skin tone or age;
- Calibration Outfit design, reusable hosiery Material Canon or episode wardrobe;
- reusable furniture/environment design, other Pose components or the complete release.

## Prompt assembly

```text
Use case: photorealistic-natural
Asset type: adult technical upright-seated joint calibration reference

Create exactly one POSE_03_SEATED_UPRIGHT candidate for adult character CHR_HUMAN_001_OWNER, following OWNER_L1_GENERATION_SPEC draft_1.107 and IDENTITY draft_0.95. Image 1 defines the approved person, natural 168 cm / 60 kg body proportions, visible front face, Hairstyle A, foot scale and established calibration clothing. It does not define the new seated articulation.

Show one straight-on full-body upright seated posture on a simple featureless neutral-gray backless studio stool. Pelvis centered and neutral on the seat, spine and torso naturally vertical without stiffness or arching, head level, gaze calmly forward and mouth naturally closed. Shoulders lowered. Upper arms rest beside the torso; forearms angle naturally forward; both empty hands rest lightly and symmetrically on the upper thighs with relaxed separated fingers.

Thighs point forward at natural hip width, approximately parallel to the floor. Both knees are naturally bent near 90 degrees and remain separated without crossing. Both lower legs descend near vertically with straight knee-shin-ankle alignment. Both feet are fully visible, uncrossed, parallel or only slightly turned out, and flat on the same studio floor. Preserve realistic seated soft-tissue compression without changing body mass, hip width, thigh volume or limb length.

Preserve the exact approved adult woman, face, Hairstyle A, 168 cm / 60 kg proportions, head-to-body scale, shoulder width, torso length, waist/hip ratio, arm/leg length, thigh/calf volume and foot size from Image 1. No slimming, elongation, head shrinking, curve exaggeration or identity redesign.

Technical studio photograph, exact 3:4 portrait, entire hair, hands, stool contact, lower legs and both feet visible with clear margins, level 70–85 mm-equivalent perspective, neutral light-gray seamless backdrop and broad soft neutral light.

Keep Image 1's established calibration clothing: plain opaque pink one-piece athletic fit garment, continuous light-nude closed-foot 15D matte/velvet sheer pantyhose, no shoes. Textile remains continuous and visible over ankles, heels, insteps and toes without ankle breaks, toe bands, bare toes, plastic gloss or body-paint appearance.

Correct ordinary adult anatomy. No crossed legs, splayed glamour pose, slouching, leaning, arched back, tiptoes, dangling feet, fused limbs, broken hips/knees/ankles, duplicated heel, extra or missing digits, chair back, armrests, props, text, watermark, collage or border. The stool is support only and defines no reusable environment or prop. This candidate defines only upright-seated articulation; it must not redefine identity, body, hair, garment or material. Status REVIEW_REQUIRED, not approved Canon.
```

## QA status

### Attempt 1

- generated_at: `2026-09-13`
- built-in output: `/home/verdvana/.codex/generated_images/01a09ab1-cec4-7f30-9bd8-80cb6ab0e147/exec-5bc0fad0-811a-416e-84fe-acddf9ead9c6.png`
- project candidate: `characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_03_SEATED_UPRIGHT_v001/POSE_03_SEATED_UPRIGHT_v001.png`
- result: one 1086×1448 exact-3:4 PNG generated and saved in the candidate directory.
- lineage: approved BODY_01 Master only; no generated Pose, Expression, historical Body candidate or Shot input.
- technical QA: pass for review; see `QA.md`.

Final current status: `REVIEW_REQUIRED`. The raster is not approved or promoted and cannot be used as Pose Canon until explicit user approval.

## User review

- decision: `REJECTED`
- user feedback: pose and other visible properties are acceptable, but the face should have been constrained directly by the dedicated approved L1 Face asset; the current face shows iterative pollution and obvious sensitive/blotchy patches.
- downstream rule: v001 must not be used as v002 input, identity source, continuity source or downstream reference. Its acceptable seated articulation is retained only as written constraints.
