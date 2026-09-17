# BODY_06_BACK_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.224
identity_md_revision: draft_0.176
asset_id: BODY_06_BACK
candidate_id: BODY_06_BACK_v002
gate: "Gate 3 — Body Canon"
model_tool: built-in image_gen
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_L0_BODY_REAR_SIDE_CONTEXT
  - OWNER_HAIR_A_BACK_CANON_L1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 4
previous_ai_body_candidate_count: 0
generation_inputs:
  - asset_id: L0_OWNER_002
    path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/3.jpg"
    responsibility: "real-person stature, torso length and natural body-volume context"
    must_not_define: "face, hair, dress, shoes, lighting, background or final rear silhouette alone"
  - asset_id: L0_OWNER_015
    path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/17.jpg"
    responsibility: "coarse real-person rear/side depth and silhouette plausibility only"
    must_not_define: "face, hair arrangement, skin, pose, clothing, accessories, setting or colors"
  - asset_id: OWNER_HAIR_A_04_BACK_CANON_001
    path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_04_BACK/OWNER_HAIR_A_04_BACK_CANON_001.png"
    responsibility: "approved Hairstyle-A rear fall, hair volume, length and tapered ends only"
    must_not_define: "body, skin, clothing, hosiery, lighting or background"
  - asset_id: OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001
    path: "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png"
    responsibility: "pale slightly-whiter 15D hosiery color, continuous coverage and heel/foot material response only"
    must_not_define: "owner identity, body proportions, foot anatomy, pose, nail color, clothing, floor or background"
qa_comparison_only:
  - asset_id: OWNER_BODY_01_FRONT_CANON_004
    path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_004.png"
    responsibility: "post-generation comparison for the user-approved waist-to-hip, hip/upper-thigh-root and leg-contour contract"
    must_not_define: "generation lineage or any pixels"
  - asset_id: OWNER_BODY_06_BACK_CANON_001
    path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_06_BACK/OWNER_BODY_06_BACK_CANON_001.png"
    responsibility: "post-generation comparison for exact back direction, framing and continuity only"
    must_not_define: "generation lineage or any pixels"
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_06_BACK_v002/BODY_06_BACK_v002.png"
checksum_sha256: null
qa_status: PENDING
```

## Prompt assembly

Use case: identity-preserve, clinical anthropometric reference.
Asset type: Owner L1 Body Canon back-view candidate.
Input images: Image 1 provides real-person body context only; Image 2 provides coarse rear/side depth only; Image 3 provides approved Hairstyle-A back hair only; Image 4 provides hosiery material only. The approved front Body Master and current back Body Master are QA comparison-only and must not be used as generation inputs.

Create exactly one neutral, non-sexual, exact 180-degree full-length back-view technical body-proportion calibration plate of the same adult woman. Head, shoulders, spine, pelvis, knees, heels and feet face directly away from camera; no head turn, facial features, torso twist or crossed legs. Preserve the natural 168 cm / approximately 60 kg body scale, pink high-cut one-piece Calibration Outfit, Hairstyle A rear fall, level shoulders and pelvis, relaxed arms, equal weight, flat feet, small natural foot gap and complete framing. Neutral gray-white seamless studio, soft even 5200–5600K light, level 70–85mm-equivalent camera at waist-to-lower-chest height, exact 3:4, 5–8% breathing room.

Body contour correction: rebuild the back waist, pelvis and upper-thigh-root silhouette to match the newly approved front Body01 contour contract. Keep a natural smooth ribcage-to-waist narrowing, then a clear but unforced waist-to-hip transition with the accepted hip width and accurate upper-thigh roots; no pinched waist, corset compression, abrupt indentation, exaggerated hourglass or generic fashion-model shaping. Continue that same body volume through the rear gluteal/pelvic contour into the thighs, knees, calves and ankles. The back leg contours should be balanced, naturally straight and symmetric, with no O-leg bow, outward sweep, knee displacement, sharp kink or unnaturally narrow ankles.

Hosiery is one continuous pale light-nude 15D velvet-finish sheer textile, visibly slightly whiter/lighter than the underlying skin in the same way as the approved front Body01 presentation. It must cover waist/hips, thighs, knees, calves, ankles, heels, soles, insteps and all toes without a cutoff, seam, band or material break. At each rear heel, create a gradual continuous transparency gradient: the calf and ankle retain the pale hazy hosiery veil, while the fabric becomes subtly more translucent over the heel's rounded rear and lower transition so the underlying skin reads through slightly more, without exposing a naked heel or creating a ring, boundary or reinforced heel. Keep the textile matte/velvet and softly diffused, never latex, PVC, plastic, rubber, wet coating or body paint.

No props, scenery, text, watermark, collage or extra views. One REVIEW_REQUIRED candidate only; not Canon.

## QA status

- pending image generation
- mandatory review: back waist-to-hip contour, upper-thigh roots, rear leg axes, pale hosiery value, heel transparency gradient, continuous coverage and no material boundary
