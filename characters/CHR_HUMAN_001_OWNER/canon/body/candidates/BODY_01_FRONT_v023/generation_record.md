# BODY_01_FRONT_v023 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v023
target_canon_version: owner_v1.0
gate: Gate 3 — Body Canon
status: REVIEW_REQUIRED
approval_status: PENDING_USER_REVIEW
spec_revision: draft_1.233
identity_revision: draft_0.184
body_method_id: OWNER_BODY_01_FRONT_METHOD_V2
body_revision: draft_0.23
generation_tool: built_in_image_gen
use_case: identity-preserve
reference_set_ids:
  - OWNER_BODY_FRONT_RECOVERY_V1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
generation_inputs:
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", responsibility: "source-derived front face/skin identity only", must_not_define: "body, hair, clothing, hosiery, lighting or background"}
  - {asset_id: L0_OWNER_002, path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/3.jpg", responsibility: "real stature, torso, waist/hip placement, limb length and stance context", must_not_define: "face, hair, clothing, shoes, props or background"}
  - {asset_id: L0_OWNER_003, path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/4.jpg", responsibility: "real torso, waist, hip, thigh, calf and limb-volume cross-check", must_not_define: "face, hair, clothing, shoes, styling or environment"}
  - {asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png", responsibility: "Hairstyle A only", must_not_define: "face, body, skin, clothing, lighting or background"}
  - {asset_id: OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001, path: "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png", responsibility: "continuous 15D pale matte/velvet sheer textile and toe coverage", must_not_define: "identity, body/foot anatomy, nail color, clothing, lighting or floor contact"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and face-contamination QA only"}
  - {asset_id: OWNER_BODY_01_FRONT_CANON_006, path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v017/BODY_01_FRONT_v017.png", purpose: "post-generation accepted-body comparison only"}
  - {asset_id: BODY_01_FRONT_v022, path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v022/BODY_01_FRONT_v022.png", purpose: "rejected-candidate comparison only; never a generation input"}
reference_count: 5
previous_generated_body_inputs: 0
authoritative_for:
  - "front lower-leg outer-contour straightness"
  - "visible burgundy-red toenail polish beneath continuous hosiery"
  - "previously authorized neck, waist and leg-volume refinements"
must_not_define:
  - "new permanent face identity or Face Canon"
  - "any AI-to-AI identity lineage"
  - "other body angles or poses"
  - "other hosiery colors, deniers or finishes"
  - "lighting/background design, props, text or watermark"
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced 1536x2048 resize"
prompt_assembly: "v017 prompt structure plus user-scoped outer-leg contour and burgundy-polish corrections; source-derived inputs only."
seed: null
settings: {tool: "built_in_image_gen", output: "single native candidate", preferred_resolution: "native exact 3:4"}
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v023/BODY_01_FRONT_v023.png
sha256: c9b86a5cbb36ea1f64faa7c76d19b9d88612dc394a2f7e3c633fbb9dec9bd4af
dimensions: 1086x1448
qa_status: TECHNICAL_PRECHECK_PASS_PENDING_USER_REVIEW
```

## Prompt assembly

Create exactly one non-erotic, neutral, full-length, front-view technical apparel-fit and posture reference of an adult woman. Image 1 alone defines the recognizable front face, facial relationships, natural skin and neutral closed-mouth expression. Images 2–3 provide real-person body context only. Image 4 defines Hairstyle A only. Image 5 defines hosiery textile behavior only. Do not use any previous generated Body image, approved Body Master, generated Face image, approved Face Canon or previous shot as an image input.

Reconstruct the same recognizable person from the source-derived face/skin input and Face method constraints: natural soft oval-to-rounded-oval face, unchanged forehead, eyes, eye spacing, eyebrows, nose, cheeks, lips, jaw and rounded chin; no generic beautification, face slimming, enlarged eyes, pointed chin, nose redesign, age change, whitening or synthetic AI-face appearance. Keep head upright in one neutral eye-level projection, neutral chin, direct gaze and no face/crown angle mismatch. Use masked Hairstyle A: flat roots, restrained near-center part, low crown, long straight dark-brown hair and wispy tapered ends.

Preserve the accepted v017 front-standing target and the user-authorized v022 refinements: coherent 168 cm / approximately 60 kg natural adult proportions, accepted shoulder width, chest and hip structure, relaxed arms, square torso, even weight, uncrossed legs and flat feet; neck modestly longer and more upright with natural collarbone transition; waist approximately 5% narrower with a smooth ribcage-to-waist-to-existing-hip transition; thighs and calves approximately 5% fuller with natural soft tissue. Do not stretch the whole body, lift the chin, change head size, widen shoulders, exaggerate hourglass shape or alter hips/arms.

Hard lower-leg geometry: the outer contour of each calf must continue downward from the same-side outer contour of the thigh almost as one continuous near-vertical line. The calf must not bow outward, flare outward, bulge laterally, or then taper inward toward the ankle. Knee center, tibial shaft center and ankle center must remain nearly collinear with the thigh axis. Keep a narrow natural inner-leg gap; legs must never fuse, overlap, cross or form an O-leg silhouette. Preserve natural calf volume without making the ankles pinched. Both feet remain fully flat and weight-bearing.

Use the standard calibration outfit: plain opaque pink high-cut one-piece garment, continuous pale slightly-whiter light-nude 15D matte/velvet sheer hosiery and no shoes. The textile must continue from thighs through knees, calves, ankles, heels, insteps, forefeet and every toe with no seam, band, white ring, hard boundary, exposed nail edge or bare gap. Burgundy/wine-red toenail polish is required and must be visibly readable as a muted red haze beneath the same continuous hosiery on multiple toes of both feet; it must not disappear, turn pink, become black, or appear as exposed bare nail. Preserve natural V-shaped fabric tension between toes.

Use native tool output at exact 3:4 portrait ratio; do not force a 1536×2048 resize. Full head, hands, heels and toes inside frame; level 70–85mm-equivalent camera centered between waist and lower chest; neutral gray-white seamless studio; soft even 5200–5600K light; no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Hard checks: source-derived face identity and no AI-to-AI contamination; neutral head/crown projection; upright natural neck; 5% waist reduction; 5% thigh/calf volume increase; outer calf lines follow outer thigh lines without outward bulge or inward bow; knee–tibia–ankle collinearity; narrow non-fused gap; flat feet; continuous hosiery; visible muted burgundy-red polish under the textile on both feet; no toe boundary or bare nail. No promotion without explicit user approval.

## Generation output

- Built-in ImageGen native output: `/home/verdvana/.codex/generated_images/01a0b245-9dec-7b83-883f-681949be624f/exec-cd77b36d-1ba5-4635-9378-055e1ffb4e4f.png`
- Repository candidate: `BODY_01_FRONT_v023.png`
- Native dimensions: `1086x1448`, exact 3:4; no resolution conversion performed.
- Initial visual precheck: burgundy-red toenail color is visible on both feet; lower-leg outer contours read closer to a continuous descent from the thigh contours than v022. Candidate remains pending user review for exact leg-axis acceptance and hosiery coverage.
