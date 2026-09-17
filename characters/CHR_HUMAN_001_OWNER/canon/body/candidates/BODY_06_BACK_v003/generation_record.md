# BODY_06_BACK_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.224
identity_md_revision: draft_0.176
asset_id: BODY_06_BACK
candidate_id: BODY_06_BACK_v003
gate: "Gate 3 — Body Canon"
model_tool: built-in image_gen
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
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
    responsibility: "post-generation comparison for approved waist/hip, hip/upper-thigh-root, leg contour and high-cut swimsuit alignment"
    must_not_define: "generation lineage or any pixels"
  - asset_id: BODY_06_BACK_v002
    path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_06_BACK_v002/BODY_06_BACK_v002.png"
    responsibility: "post-generation comparison for accepted body and hosiery attributes only"
    must_not_define: "generation lineage or any pixels"
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_06_BACK/OWNER_BODY_06_BACK_CANON_002.png"
original_candidate_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_06_BACK_v003/BODY_06_BACK_v003.png"
promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_06_BACK/OWNER_BODY_06_BACK_CANON_002.png"
checksum_sha256: f5a6d6cea3259ca3247d6b035595a67f5c50ada62f7fec9f011f4915b1895e87
approval_record: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_06_BACK/approvals/APPROVAL_OWNER_BODY_06_BACK_002.md"
qa_status: PASS_USER_APPROVED
```

## Prompt assembly

Use case: identity-preserve, clinical apparel-fit and anthropometric calibration.
Asset type: Owner L1 Body Canon back-view candidate.
Input images: Image 1 provides real-person body context only; Image 2 provides coarse rear/side depth only; Image 3 provides approved Hairstyle-A back hair only; Image 4 provides hosiery material only. The approved front Body Master and v002 candidate are comparison-only and must not be used as generation inputs.

Create exactly one neutral, non-erotic, exact 180-degree full-length back-view technical apparel-fit and body-proportion chart of the same adult woman. Fully clothed in the plain opaque pink high-cut one-piece Calibration Outfit, continuous pale hosiery and no shoes. Head, shoulders, torso, pelvis, knees, heels and feet face directly away from camera; no head turn, torso twist or crossed legs. Preserve the accepted v002 body and hosiery: natural 168 cm / approximately 60 kg scale, smooth waist-to-hip transition, approved hip and upper-thigh-root contour, balanced near-straight legs, pale slightly-whiter 15D hosiery, continuous toe/heel coverage and subtle heel transparency gradient.

Correct only the swimsuit construction: the rear leg openings must be clearly high-cut and must align with the approved front Body01 high-cut swimsuit. Raise the back leg-opening/brief edge substantially from the low v002 position so the side seam rises toward the upper hip and the rear opening sits high at the gluteal crease, matching the front leg-opening height and the same hip-to-thigh transition. The swimsuit must remain a normal opaque athletic one-piece with coherent rear coverage, symmetric left/right edges, natural fabric tension and no low-cut brief line. Do not change the approved waist width, hip breadth, pelvis volume, upper-thigh roots, leg axes, hair, camera, pose, or hosiery.

Hosiery remains one continuous pale light-nude 15D velvet-finish sheer textile, slightly whiter than skin. At both rear heels retain a gradual transparency gradient within the fabric: pale hazy coverage on calf and ankle, subtly more translucent over the rounded heel and lower transition, with skin softly visible through but no bare heel, ring, seam, band or material break. No latex, PVC, plastic, rubber, wet coating or body paint.

Neutral gray-white seamless studio, soft even neutral light, level 70–85mm camera, exact 3:4 portrait, complete framing, no props, text, watermark, collage or extra views. Produce one REVIEW_REQUIRED candidate only; not Canon.

## Promotion and approval

- user approval: “非常好，登记吧用这一版”
- candidate PNG was moved unchanged to the approved Master path; no duplicate candidate raster remains
- promoted asset: `OWNER_BODY_06_BACK_CANON_002`
- promoted checksum: `f5a6d6cea3259ca3247d6b035595a67f5c50ada62f7fec9f011f4915b1895e87`
- the complete `owner_v1.0` release remains unlocked
