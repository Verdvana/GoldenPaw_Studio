# POSE_06_BENDING_REACHING_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.123
identity_md_revision: draft_0.111
asset_id: POSE_06_BENDING_REACHING
candidate_id: POSE_06_BENDING_REACHING_v003
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
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 4
previous_ai_pose_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_06_BENDING_REACHING_v003/POSE_06_BENDING_REACHING_v003.png"
checksum_sha256: null
qa_status: NO_OUTPUT
```

## Authorization and lineage

The user accepted v002's action, expression and body proportions and requested three material-only corrections: one primary upper-thigh compression fold instead of several, light skin-tone/nude rather than white hosiery, and genuinely textile-diffused toes rather than painted-white toes. v003 is an independent reconstruction from approved Masters and one scoped material derivative. v001, v002 and all other Pose pixels are excluded.

## Reference responsibilities

1. `OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg`
   - responsibility: exact approved left-three-quarter facial identity, neutral expression and clean even skin.
   - must_not_define: body, pose, hair, outfit, hosiery, feet, lighting or background.
2. `OWNER_BODY_LEFT_3Q_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_02_LEFT_3Q_v001/BODY_02_LEFT_3Q_v001.png`
   - responsibility: approved 168 cm / 60 kg body proportions, limb/foot scale, Calibration Outfit and the authoritative light skin-tone/nude hosiery hue.
   - must_not_define: new identity, permanent bending pose, reusable hosiery/nail-color Canon, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - responsibility: Hairstyle-A part, controlled volume, long straight structure, color and tapered ends.
   - must_not_define: face, skin, body, pose, outfit, hosiery, feet, lighting or background.
4. `HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001`
   - path: `materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png`
   - responsibility: 15D matte/velvet textile texture, sheer opacity, continuous lower-leg-to-toe coverage, gentle tension and anatomical diffusion only.
   - must_not_define: hosiery color or white cast, identity, anatomy, skin pigmentation, nail color, pose, clothing, background, lighting or floor contact.

Reference budget: 4 images. No previous Pose candidate is used.

## Prompt assembly

```text
Create one photorealistic adult occupational-ergonomics and apparel-fit reference, exact 3:4 vertical. Independently reconstruct POSE_06 v003; do not use any previous Pose image.

Image 1 defines only the approved left-three-quarter face, calm neutral expression and clean even skin. Image 2 defines the approved 168 cm / 60 kg body proportions, limb and foot scale, pink calibration garment, and the sole authoritative light skin-tone/nude hosiery color. Image 3 defines only Hairstyle A. Image 4 defines only 15D matte textile texture, sheer opacity, continuous coverage, subtle mesh tension and soft anatomical diffusion; it must not transfer color, white cast, anatomy, pose, skin, nails, clothing, lighting or background.

Preserve the accepted action textually: left-three-quarter forward reach, stable staggered stance, softly bent knees, level pelvis, natural 25–35-degree hip hinge and long neutral spine; nearer arm reaches forward and slightly downward with an open relaxed hand, other arm balances behind. A naturally raised rear heel with stable forefoot support is valid for this Pose. Preserve the accepted calm expression and approved body proportions.

Use the pink calibration garment, no shoes, and continuous light skin-tone/nude 15D matte hosiery from waist through thighs, knees, calves, ankles, heels, insteps and all toes. The hosiery must read nude, never white, ivory or cream. At the upper-thigh garment transition under hip flexion, show smooth fabric with exactly one main deep natural diagonal compression fold on the nearer thigh; remove stacked parallel grooves, extra rings and repeated ripples.

Across every toe, show a real translucent fabric veil visibly above the anatomy: toe contours and restrained burgundy toenails remain softly muted underneath, with gentle mesh tension over toe joints. Do not paint, bleach, airbrush or chalk the toes white; no opaque white toe cap, white color patch, toe seam, band, cutoff or color break. The feet must look covered by fine nude textile rather than bare or whitened.

One complete adult figure from hair to feet, neutral light-gray seamless studio, soft even catalog lighting, clear space around hand and feet, 70–85 mm-equivalent perspective. No props, furniture, text, watermark, identity drift, extra or missing digits, glossy plastic/latex appearance, floating foot, broken heel or support artifact. Unapproved candidate for Pose review only.
```

## Generation attempts

### Attempt 1

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references: the same four declared scoped inputs; no previous Pose image.
- request_id: `5150c9a9-8956-4285-a6f9-019de39d822b`
- next action: one prompt-only retry using concise technical garment-fit wording while preserving the same responsibilities, exclusions and material corrections.

### Attempt 2

- result: output moderation rejected (`sexual`); no image was returned or stored.
- references: the same four declared scoped inputs; no previous Pose image.
- request_id: `19aafa45-5068-4fb8-aa04-78f3de0e0ef6`
- decision: stop repeated prompt retries. Candidate remains ungenerated and ineligible for promotion or downstream reference.

## QA status

No raster output exists. QA cannot be performed. Status: `GENERATION_BLOCKED_NO_OUTPUT`.
