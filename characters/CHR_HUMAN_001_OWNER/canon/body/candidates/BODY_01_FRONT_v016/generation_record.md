# BODY_01_FRONT_v016 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.224
identity_md_revision: draft_0.176
body_md_revision: draft_0.16
method_id: OWNER_BODY_01_FRONT_METHOD_V2
user_scoped_override: "2026-09-17 regenerate current BODY_01: remove bow-leg read; pale hosiery, interdigital tension and toe veil"
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v016
gate: "Gate 3 — Body Canon"
model_tool: built-in image_gen
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_BODY_FRONT_RECOVERY_V1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 5
previous_ai_reference_count: 0
face_l1_raster_supplied: false
generation_inputs:
  - asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001
    path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png"
    responsibility: "source-derived front face/skin context only"
    must_not_define: "hair, body, clothing, hosiery, lighting, background"
  - asset_id: L0_OWNER_002
    path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/3.jpg"
    responsibility: "real-person stature, head-to-body scale, torso and natural standing body context"
    must_not_define: "face, hair, qipao, shoes, umbrella, background, retouching"
  - asset_id: L0_OWNER_003
    path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/4.jpg"
    responsibility: "real-person torso, waist, hip, thigh, calf and limb-volume cross-check"
    must_not_define: "face, hair, dress, shoes, legwear, environment, final body alone"
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png"
    responsibility: "Hairstyle A visible hair pixels only"
    must_not_define: "masked face, body, skin, clothing, lighting, background"
  - asset_id: OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001
    path: "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png"
    responsibility: "pale 15D nude matte/velvet textile coverage, toe veil and interdigital stretch response only"
    must_not_define: "owner identity, face, body proportions, foot anatomy, nail color, clothing, pose, floor or background"
qa_comparison_only:
  - asset_id: OWNER_BODY_01_FRONT_CANON_003
    path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_003.png"
    responsibility: "post-generation comparison for accepted face, body scale, torso, waist/hip, framing and component continuity"
    must_not_define: "generation lineage or any pixels"
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg"
    responsibility: "post-generation face identity and contamination comparison only"
    must_not_define: "generation lineage or any pixels"
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_004.png"
original_candidate_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v016/BODY_01_FRONT_v016.png"
promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_004.png"
checksum_sha256: eab2d082bc2a3f63137aa9caa6307cf35c8fa48ae70e1664adf7ae75c89fadac
approval_record: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/approvals/APPROVAL_OWNER_BODY_01_FRONT_004.md"
qa_status: PASS_USER_APPROVED
```

## Prompt assembly

Use case: identity-preserve, clinical anthropometric reference.
Asset type: Owner L1 Body Canon candidate.
Input images: Images 1–4 are the ordered `OWNER_BODY_FRONT_RECOVERY_V1` source inputs; Image 5 is a material-only hosiery reference. The current approved Body Master and approved Face Canon are comparison-only and must not be used to generate pixels.

Create exactly one neutral, non-sexual, full-length 3:4 straight-on front-view technical body-proportion calibration plate of the same adult woman. Preserve the approved source-derived face method, Hairstyle A, 168 cm / approximately 60 kg natural proportions, pink high-cut one-piece calibration outfit, square torso, relaxed arms, even weight, flat feet and complete framing.

Correct the lower-leg geometry decisively: both legs are anatomically straight in front view, with each knee center, tibial shaft and ankle center tracking a nearly vertical, symmetric axis. Use only a minimal natural soft-tissue curve; no outward bow, O-leg impression, lateral sweep, knee displacement, sharp kink or pose trick. Keep a small natural inner-leg gap, not a wide separation. Feet are flat, stable, uncrossed and approximately parallel.

Hosiery is one continuous pale light-nude 15D velvet-finish sheer textile, visibly slightly whiter/lighter than the underlying skin while remaining translucent and realistic. It must continue uninterrupted from thighs through calves, ankles, heels, insteps, forefeet and every toe. The toes must be covered by a soft hazy textile veil; muted deep burgundy/wine-red polish may show softly beneath the fabric, never on top. Show delicate readable fabric tension between adjacent toes as narrow curved/V-shaped translucent stretch valleys and subtle highlights that bridge the interdigital spaces. These are textile deformation responses, not bare-foot grooves, exposed toe gaps, toe-root seams, bands or hard boundaries. No bare toes, no naked-foot appearance, no duplicated or split toes/nails, no opaque toe cap, no discontinuity, no latex/PVC/plastic/rubber/wet/body-paint appearance.

Neutral gray-white seamless studio, soft even 5200–5600K light, level 70–85mm-equivalent camera centered between waist and lower chest. Exact 3:4, complete head, hands, heels and toes, 5–8% breathing room. No props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## Promotion and approval

- user approval: “登记这版本，这版本的胯和大腿根部还原的非常好”
- candidate PNG was moved unchanged to the approved Master path; no duplicate candidate raster remains
- promoted asset: `OWNER_BODY_01_FRONT_CANON_004`
- promoted checksum: `eab2d082bc2a3f63137aa9caa6307cf35c8fa48ae70e1664adf7ae75c89fadac`
- the complete `owner_v1.0` release remains unlocked
