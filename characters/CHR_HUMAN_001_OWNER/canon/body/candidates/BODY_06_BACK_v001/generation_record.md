# BODY_06_BACK_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.52
identity_md_revision: draft_0.46
body_md_revision: draft_0.26
asset_id: BODY_06_BACK
candidate_id: BODY_06_BACK_v001
gate: "Gate 3 — Body Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_BODY_FRONT_CANON_L1
  - OWNER_L0_BODY_REAR_SIDE_CONTEXT
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 4
previous_ai_body_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_06_BACK_v001/BODY_06_BACK_v001.png"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_06_BACK/OWNER_BODY_06_BACK_CANON_001.png"
current_promoted_checksum_sha256: "2344a37e9355bbe1fb49865b5039275cebbbe5cfb043738b7e2edb6c777add7c"
checksum_sha256: "2344a37e9355bbe1fb49865b5039275cebbbe5cfb043738b7e2edb6c777add7c"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user explicitly requested the next asset after approval of BODY_05. The ordered final Gate-3 item is BODY_06_BACK. This is a fresh parallel generation from one approved scoped Body Master, one immutable L0 rear/side context image, one registered deterministic Hairstyle-A derivative and one registered deterministic hosiery crop. No BODY_02–BODY_05 image, historical Body candidate, previous shot, mirror or episode asset is an input.

## Reference plan

1. Image 1 / `OWNER_BODY_01_FRONT_CANON_002`: defines only the approved 168 cm / 60 kg target, head/body scale, shoulder/torso/limb lengths, waist/hip relationship, natural volume, foot scale, Calibration Outfit construction and accepted 15D matte nude combination. Its visible face, frontal projection, front hair arrangement, lighting and background cannot define the new back view.
2. Image 2 / `L0_OWNER_015` (`17.jpg`): defines only coarse conservative real-person rear/side depth and silhouette plausibility. Its face, hair arrangement, skin, pose, hand placement, dress, accessories, setting, colors and low-resolution artifacts are excluded.
3. Image 3 / `OWNER_HAIRSTYLE_A_FACE_MASKED_001`: deterministic derivative of `L0_OWNER_017`; defines only Hairstyle A's dark-brown long straight loose hair, near-center part, controlled volume, broad fall, length and tapered ends. Its gray face mask, visible clothing, background, body and frontal-only arrangement are excluded. BODY_06 may show a conservative back fall but cannot become final Hair-back authority; that belongs to `HAIR_A_04_BACK`.
4. Image 4 / `OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001`: deterministic derivative of user-selected `L0_HOS_15_NM_011`; defines only visible light-nude 15D matte/velvet textile presence, opacity, continuous lower-leg-to-heel/foot coverage and muted toe visibility. Its dangling pose, anatomy, heel elevation, floor contact, skin/nail color, clothing, shoes, background, lighting and watermark are excluded.

## Candidate authority

- complete square rear body silhouette and conservative rear-depth relationship for review;
- preservation of approved 168 cm / 60 kg proportions in a neutral untwisted back standing view;
- consistent backward head orientation and conservative Hairstyle-A rear fall, without becoming final hairstyle-back authority;
- no authority for a new face identity, final reusable Gate-7 hosiery material, other views, episode wardrobe, lighting, background or Canon status.

## Prompt assembly

```text
Use case: identity-preserve. Asset: BODY_06_BACK_v001, one adult technical character-turnaround calibration reference for CHR_HUMAN_001_OWNER, Identity draft_0.46 and spec draft_1.52. Create a new image in parallel; do not use any BODY_02–BODY_05 image or prior candidate.

Image 1 (`OWNER_BODY_FRONT_CANON_L1`, approved path `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg`) defines only approved natural 168 cm / 60 kg proportions, head/body scale, shoulder/torso/limb lengths, waist/hip relationship, foot scale, pink calibration suit and general 15D nude matte combination. Image 2 (`OWNER_L0_BODY_REAR_SIDE_CONTEXT`, path `characters/CHR_HUMAN_001_OWNER/source/identity/raw/17.jpg`) defines only conservative rear/side depth; ignore its person details, pose, dress and setting. Image 3 (`OWNER_HAIRSTYLE_A_FACE_MASKED_001`, path `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`) defines only long straight loose dark-brown Hairstyle A, controlled volume, length and tapered ends; ignore the mask, clothes, body and background. Image 4 (`HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001`, path `materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png`) defines only light-nude 15D matte/velvet textile presence and continuous leg-to-foot coverage; ignore its pose, anatomy and floor relationship.

Show an exact 180-degree full-body back view. Back of head, shoulders, spine, pelvis, knees, heels and feet all face directly away from camera with no head turn, facial features, side glance or torso twist. Neutral upright stance, level shoulders and pelvis, relaxed straight arms with complete natural hands, legs uncrossed, feet parallel with a small gap and equal weight. Both ordinary anatomical heels and complete plantar surfaces contact one flat floor; no lifted heel, tiptoe, pad, wedge, platform, duplicate form or added support.

Preserve Image 1's natural 168 cm / 60 kg proportions without slimming, widening, shortening or fashion-model stylization. Use the same plain opaque pink high-cut one-piece athletic calibration suit, with a simple coverage-appropriate back construction, continuous closed-foot light-nude 15D matte/velvet-finish sheer pantyhose, and no shoes. The textile continuously covers waist/hips, legs, ankles, heels, soles, insteps and all toes. No cutoff, naked-looking foot, reinforced toe, heel seam, toe seam, color band, transparency break, plastic, rubber, wet coating or body paint.

Hairstyle A remains long, straight, loose and dark brown with restrained crown volume and natural tapered ends; show a plausible centered rear fall without inventing a new hairstyle design. Exact 3:4 portrait, complete head, hair, hands, heels and feet with 5–8% breathing room. Level 70–85mm-equivalent camera near waist/lower-chest height. Neutral gray-white seamless studio, soft even neutral lighting, natural skin and textile texture. No props, scenery, text, logo, watermark, collage or multiple views. Produce one REVIEW_REQUIRED image only.
```

## Attempt result

- generated_at: `2026-09-12`
- result: one 1086x1448 exact-3:4 PNG generated and saved at the declared project output path
- built_in_output: `/home/verdvana/.codex/generated_images/01a09467-3db0-70a2-bf86-1fb58ecbbfb6/exec-0eb9cfc8-bbec-420d-9a45-b341f520d47d.png`
- project_candidate_checksum_sha256: `2344a37e9355bbe1fb49865b5039275cebbbe5cfb043738b7e2edb6c777add7c`
- technical_precheck: exact full-back direction with no face reveal or torso twist passes; shoulders, pelvis, legs and heels are coherent and near-symmetric; both anatomical heels directly meet one floor plane with no pad or duplicate form; continuous light-nude matte hosiery coverage remains visually subtle and requires user material review; Hairstyle A forms a conservative centered rear fall without claiming final Hair-back authority
- promotion_status: promoted unchanged after explicit user approval

## User approval

On 2026-09-12 the user stated: “可以 登记吧”. The candidate was promoted unchanged to `OWNER_BODY_06_BACK_CANON_001`. Approval covers the scoped complete rear Body component, accepted aligned backward head/body orientation, conservative Hairstyle-A rear fall and visible 15D nude matte/velvet presentation within this Body asset. It does not lock the complete `owner_v1.0`, replace `HAIR_A_04_BACK`, or replace Gate-7 Hosiery/Feet Canon.
