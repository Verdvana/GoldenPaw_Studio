# BODY_01_FRONT_v024 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v024
target_canon_version: owner_v1.0
gate: Gate 3 — Body Canon
status: REVIEW_REQUIRED
approval_status: PENDING_USER_REVIEW
spec_revision: draft_1.233
identity_revision: draft_0.184
body_method_id: OWNER_BODY_01_FRONT_METHOD_V2
body_revision: draft_0.24
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
  - {asset_id: OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001, path: "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png", responsibility: "slightly-whitish continuous 15D matte/velvet sheer hosiery, toe veil and interdigital textile tension", must_not_define: "identity, body/foot anatomy, nail color, clothing, lighting or floor contact"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and face-contamination QA only"}
  - {asset_id: OWNER_BODY_01_FRONT_CANON_006, path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v017/BODY_01_FRONT_v017.png", purpose: "post-generation body comparison only"}
  - {asset_id: BODY_01_FRONT_v023, path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v023/BODY_01_FRONT_v023.png", purpose: "comparison-only; never a generation input"}
reference_count: 5
previous_generated_body_inputs: 0
authoritative_for:
  - "further front lower-leg straightness"
  - "further natural waist refinement"
  - "slightly-whitish continuous hosiery, hazy nail coverage and interdigital tension"
must_not_define:
  - "new permanent face identity or Face Canon"
  - "any AI-to-AI identity lineage"
  - "other body angles or poses"
  - "other hosiery colors, deniers or finishes"
  - "lighting/background design, props, text or watermark"
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced 1536x2048 resize"
prompt_assembly: "v017 source-recovery prompt plus user-scoped leg, waist and hosiery refinements; source-derived inputs only."
seed: null
settings: {tool: "built_in_image_gen", output: "single native candidate", preferred_resolution: "native exact 3:4"}
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v024/BODY_01_FRONT_v024.png
sha256: eff34097d903513a0f4ef225fd0a584c5d17f5ad5eca22a07dc0b5e8db34c94d
dimensions: 1086x1448
qa_status: TECHNICAL_PRECHECK_PASS_PENDING_USER_REVIEW
```

## Prompt assembly

Create exactly one non-erotic, neutral full-length front-view technical apparel-fit and posture reference of an adult woman. Image 1 alone defines the recognizable front face, facial relationships, natural skin and neutral closed-mouth expression. Images 2–3 provide real-person body context only. Image 4 defines Hairstyle A only. Image 5 defines hosiery textile behavior only. Do not use any previous generated Body image, approved Body Master, generated Face image, approved Face Canon or previous shot as an image input.

Reconstruct the same recognizable person from the source-derived face/skin input and Face method constraints: natural soft oval-to-rounded-oval face, unchanged forehead, eyes, eye spacing, eyebrows, nose, cheeks, lips, jaw and rounded chin; no generic beautification, face slimming, enlarged eyes, pointed chin, nose redesign, age change, whitening or synthetic AI-face appearance. Keep head upright in one neutral eye-level projection, neutral chin and direct gaze. Use masked Hairstyle A: flat roots, restrained near-center part, low crown, long straight dark-brown hair and wispy tapered ends.

Preserve the accepted natural 168 cm / approximately 60 kg adult proportion target, relaxed arms, square torso, even weight, uncrossed legs and flat feet. Preserve the previously accepted modestly longer upright neck and natural collarbone transition. Make the waist modestly narrower again through a smooth natural ribcage-to-waist-to-existing-hip transition; do not corset-compress, pinch, hollow or exaggerate the hourglass. Keep thighs and calves naturally full.

Hard lower-leg geometry: make both legs visibly straighter than v023. Each knee center, tibial shaft center and ankle center must be nearly collinear with the thigh axis. The outer contour of each calf must descend almost directly from the same-side outer thigh contour as a continuous near-vertical line: no outward flare, no lateral bulge, no inward bow, no tapering sharply inward toward the ankle. Keep natural calf volume and normal ankles. The inner contours leave only a narrow natural air gap; legs never fuse, overlap, cross or form an O-leg silhouette. Both feet are fully flat and weight-bearing.

Use the standard pink one-piece calibration garment and continuous pale light-nude 15D matte/velvet sheer hosiery, no shoes. The hosiery must visibly read as one continuous slightly-whitish textile veil from thighs through knees, calves, ankles, heels, insteps, forefeet and every toe. It should be subtly lighter/whiter than the underlying skin, matte and softly hazy, never bare skin, latex, PVC, plastic, wet coating or opaque painted color. Burgundy/wine-red toenail polish must be visible but softly diffused through the hosiery: muted red haze under fabric, low contrast, blurred edges, never crisp exposed nail, never bare red nail, never pink or black. Between adjacent toes, show clear but natural V-shaped converging fabric tension curves and small textile valleys; these are hosiery stretch responses, not bare toe gaps, seams or painted lines. No white toe ring, hard toe boundary, transverse band or material discontinuity.

Use native tool output at exact 3:4 portrait ratio; do not force a 1536×2048 resize. Full head, hands, heels and toes inside frame; level 70–85mm-equivalent camera centered between waist and lower chest; neutral gray-white seamless studio; soft even 5200–5600K light; no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Hard checks: source-derived face identity and no AI-to-AI contamination; neutral head/crown projection; upright neck; narrower natural waist; knee–tibia–ankle collinearity; outer calf lines following outer thigh lines without outward flare or inward bow; narrow non-fused gap; flat feet; slightly-whitish continuous hosiery; hazy burgundy polish beneath fabric; readable interdigital textile tension; no bare toe gaps, hard toe boundary or artifacts. No promotion without explicit user approval.

## Generation output

- Built-in ImageGen safety retry returned the candidate after the first attempt was blocked at output moderation.
- Repository candidate: `BODY_01_FRONT_v024.png`
- Native dimensions: `1086x1448`, exact 3:4; no resolution conversion performed.
- Initial visual precheck: slightly-whitish legwear veil, blurred burgundy-red color beneath the toe fabric and visible interdigital fabric convergence are present. Candidate remains pending user review for exact leg-axis acceptance.
