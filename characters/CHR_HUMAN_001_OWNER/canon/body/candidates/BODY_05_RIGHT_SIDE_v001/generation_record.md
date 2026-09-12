# BODY_05_RIGHT_SIDE_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.50
identity_md_revision: draft_0.45
body_md_revision: draft_0.24
asset_id: BODY_05_RIGHT_SIDE
candidate_id: BODY_05_RIGHT_SIDE_v001
gate: "Gate 3 — Body Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_RIGHT_PROFILE_NEUTRAL_CANON_L1
  - OWNER_BODY_FRONT_CANON_L1
  - OWNER_L0_BODY_REAR_SIDE_CONTEXT
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 4
previous_ai_body_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_05_RIGHT_SIDE_v001/BODY_05_RIGHT_SIDE_v001.png"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_05_RIGHT_SIDE/OWNER_BODY_05_RIGHT_SIDE_CANON_001.png"
current_promoted_checksum_sha256: "b71d47d932352985e0d8347ca7ddb485d86bc3b6ac3ddb8183ae02615c6a14cc"
checksum_sha256: "b71d47d932352985e0d8347ca7ddb485d86bc3b6ac3ddb8183ae02615c6a14cc"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user explicitly requested the next asset after approval of BODY_04. The ordered next Gate-3 item is BODY_05_RIGHT_SIDE. This is a fresh parallel generation from approved scoped Masters plus one immutable L0 context image and one registered deterministic hosiery crop. No BODY_02, BODY_03, BODY_04, historical Body candidate, previous shot, mirror or episode asset is an input.

## Reference plan

1. Image 1 / `OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001`: defines only the approved anatomical-right profile identity, face pointing image-left, neutral expression, profile silhouette and visible side presentation of Hairstyle A. It cannot define body geometry, pose, outfit, hosiery, feet, lighting or background.
2. Image 2 / `OWNER_BODY_01_FRONT_CANON`: defines the approved 168 cm / 60 kg target, head/body scale, torso and limb proportions, waist/hip ratio, natural volume, foot scale, Hairstyle A length, Calibration Outfit construction and accepted 15D matte nude combination. It cannot define the new right-side depth, profile face projection, camera, lighting, background, other hosiery materials or episode wardrobe.
3. Image 3 / `L0_OWNER_015` (`17.jpg`): defines only conservative real-person side/rear depth and silhouette plausibility. Its face, hair, skin, proportions, pose, hand placement, dress, accessories, setting, lighting, colors and low-resolution artifacts are excluded.
4. Image 4 / `OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001`: deterministic derivative of user-selected `L0_HOS_15_NM_011`; defines only visible light-nude 15D matte/velvet textile presence, opacity, continuous lower-leg-to-foot coverage and muted toe visibility. Its dangling pose, leg/foot anatomy, heel elevation, floor contact, skin/nail color, clothing, shoes, background, lighting and watermark are excluded.

## Candidate authority

- anatomical-right complete side silhouette and conservative depth relationship for review;
- preservation of approved 168 cm / 60 kg proportions and neutral standing geometry at 90 degrees;
- no authority for a new identity, hairstyle, frontal body proportions, reusable Gate-7 hosiery material, other views, episode wardrobe, lighting, background or Canon status.

## Prompt assembly

```text
Use case: identity-preserve. Create one photorealistic full-length adult technical character-turnaround calibration reference, BODY_05_RIGHT_SIDE v001. Use no previous Body candidate or adjacent generated view.

Image 1 defines only the approved anatomical-right profile identity and image-left orientation. Image 2 defines the approved natural 168 cm / 60 kg proportions, head/body scale, limb lengths, waist/hip relationship, Hairstyle A, pink calibration suit and general 15D nude matte combination. Image 3 defines only conservative real-person side-depth plausibility; ignore its face, hair, pose, clothing and setting. Image 4 defines only light-nude 15D matte/velvet textile presence and continuous lower-leg-to-foot coverage; ignore its pose, anatomy, heel elevation and floor relationship.

Show an exact 90-degree anatomical-right full-body profile. Face and whole body point image-left. Head, shoulders, torso, pelvis, knees and feet share one side direction, with no twist toward camera. Neutral upright stance, relaxed vertical arms, natural hands, uncrossed legs, feet slightly staggered. Both ordinary heels and forefeet directly contact one flat floor; no raised heel, tiptoe, pad, wedge, platform, duplicate anatomy or added support.

Preserve Image 2's natural 168 cm / 60 kg proportions. Use the same plain opaque pink high-cut one-piece athletic calibration suit, continuous closed-foot light-nude 15D matte/velvet-finish sheer pantyhose, and no shoes. Textile continuously covers hips, legs, ankles, heels, insteps and every toe, softly diffusing toe shapes. No ankle cutoff, naked-looking toes, open toe, reinforced toe, toe seam, line across toe roots or forefoot, color band, transparency break, plastic, rubber, wet coating or body paint.

Keep Hairstyle A long, straight, loose and dark brown with a near-center part. Exact 3:4 portrait, complete head, hair, hands, heels and toes with 5–8% breathing room. Level 70–85mm-equivalent camera near waist/lower-chest height. Neutral gray-white seamless studio, soft even lighting, natural skin and textile texture. No props, scenery, text, logo, watermark, collage or multiple views. Produce one REVIEW_REQUIRED image only.
```

## Attempt result

- generated_at: `2026-09-12`
- result: one 1086x1448 exact-3:4 PNG generated and saved at the declared project output path
- built_in_output: `/home/verdvana/.codex/generated_images/01a09467-3db0-70a2-bf86-1fb58ecbbfb6/exec-adff8c73-654a-490b-86a9-3d7221bcc2f5.png`
- project_candidate_checksum_sha256: `b71d47d932352985e0d8347ca7ddb485d86bc3b6ac3ddb8183ae02615c6a14cc`
- technical_precheck: exact right-profile direction and coherent neutral alignment pass; the near heel and both forefeet directly meet one floor plane; no pad, wedge, duplicate heel or transverse toe-root line is visible; continuous light-nude matte coverage is present but intentionally sheer and should receive user material review; the far heel is naturally occluded in exact profile and remains a focused user-review item
- promotion_status: promoted unchanged after explicit user approval

## User approval

On 2026-09-12 the user stated: “可以 登记并记录了”. The candidate was promoted unchanged to `OWNER_BODY_05_RIGHT_SIDE_CANON_001`. Approval covers the scoped anatomical-right side Body component, accepted natural exact-profile overlap and visible 15D nude matte/velvet presentation within this Body asset. It does not lock the complete `owner_v1.0` release or replace Gate-7 Hosiery/Feet Canon.
