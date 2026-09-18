# BODY_01_FRONT_v025 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v025
target_canon_version: owner_v1.0
gate: Gate 3 — Body Canon
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
spec_revision: draft_1.233
identity_revision: draft_0.184
body_method_id: OWNER_BODY_01_FRONT_METHOD_V2
body_revision: draft_0.25
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
  - {asset_id: OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001, path: "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png", responsibility: "slightly-whitish continuous 15D matte/velvet sheer hosiery and toe textile behavior", must_not_define: "identity, body/foot anatomy, nail color, clothing, lighting or floor contact"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and face-contamination QA only"}
  - {asset_id: OWNER_BODY_01_FRONT_CANON_006, path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v017/BODY_01_FRONT_v017.png", purpose: "post-generation body comparison only"}
  - {asset_id: BODY_01_FRONT_v024, path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v024/BODY_01_FRONT_v024.png", purpose: "comparison-only; never a generation input"}
reference_count: 5
previous_generated_body_inputs: 0
authoritative_for:
  - "further lower-leg straightness and outer-contour continuity"
  - "further natural waist refinement"
  - "uninterrupted toe-root hosiery color/material transition"
must_not_define:
  - "new permanent face identity or Face Canon"
  - "any AI-to-AI identity lineage"
  - "other body angles or poses"
  - "other hosiery colors, deniers or finishes"
  - "lighting/background design, props, text or watermark"
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced 1536x2048 resize"
prompt_assembly: "v017 source-recovery prompt plus user-scoped toe-root, waist and lower-leg corrections; source-derived inputs only."
seed: null
settings: {tool: "built_in_image_gen", output: "single native candidate", preferred_resolution: "native exact 3:4"}
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
sha256: 90e021fcf5c72416b2b3c6405cfe2abe2d43c28e49da6dbabc250f73da306978
dimensions: 1086x1448
qa_status: APPROVED_BY_USER
```

## Prompt assembly

Create one non-erotic, neutral full-length front-view technical apparel-fit and posture reference of an adult woman. Image 1 alone defines the recognizable front face and natural skin; Images 2–3 define real-person stature and body context; Image 4 defines long straight Hairstyle A; Image 5 defines continuous textile legwear. Never use generated or approved AI images as generation inputs. Native exact 3:4 portrait output, no forced resize.

Preserve the same adult face, natural age, facial relationships, neutral expression, upright head and direct gaze from the source-derived face input. No beautification or synthetic AI-face appearance. Use flat-rooted, low-crown, long straight dark-brown Hairstyle A from the masked source.

Use a natural 168 cm / approximately 60 kg adult proportion study, relaxed arms, square torso, even weight and flat feet. Keep the upright natural neck. Make the waist visibly narrower than v024, but only through a smooth natural lower-ribcage-to-waist-to-existing-hip transition; no corset compression, pinching, concavity, tiny waist or exaggerated hourglass. Keep hips, shoulders, chest, arms and natural thigh volume coherent.

Hard lower-leg requirement: make both legs straighter than v024. Each knee center, tibial shaft center and ankle center nearly collinear with the thigh axis. Each outer calf contour must descend almost directly from the same-side outer thigh contour as one continuous near-vertical line, with essentially no outward flare, lateral bulge, inward bow or sharp inward taper. Keep natural calf volume and normal ankles. The inner contours leave only a narrow natural air gap; legs never fuse, overlap, cross or form an O-leg silhouette. Both feet fully flat and weight-bearing.

Fully clothed in the established pink one-piece calibration garment and continuous pale slightly-whitish light-nude 15D matte/velvet sheer legwear, no shoes. The textile must remain visually uniform from calf through ankle, forefoot and toes. Absolute hard constraint: there must be no color split, white line, white ring, transverse line, reinforced-toe effect, hard edge or opacity boundary at the toe roots. The same slightly-whitish hazy textile must continue smoothly across every toe root and into each toe. Burgundy/wine-red toenail color may appear only as a muted blurred haze beneath that same uninterrupted fabric, never as exposed crisp red nail. Between toes, show natural V-shaped fabric-tension convergence and small textile valleys, never bare gaps, seams or painted lines.

Neutral gray-white studio, soft even light, level camera, complete head and feet, no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Hard checks: source-derived face identity and no AI-to-AI contamination; neutral head/crown projection; upright neck; waist clearly narrower than v024 without pinching; knee–tibia–ankle collinearity; outer calf lines nearly straight and continuous with outer thigh lines; narrow non-fused gap; flat feet; uniform pale hosiery through toe roots and toes with zero color segmentation; hazy burgundy polish beneath fabric; readable interdigital tension; no artifacts. No promotion without explicit user approval.

## Generation output

- Built-in ImageGen attempt 1: rejected during visual precheck because the pink calibration garment became a dress; not retained as the candidate raster.
- Built-in ImageGen retry: correct connected one-piece calibration garment returned.
- Repository candidate: `BODY_01_FRONT_v025.png`
- Native dimensions: `1086x1448`, exact 3:4; no resolution conversion performed.
- Initial visual precheck: no obvious toe-root color split; lower legs read straighter and the waist is narrower than v024. Candidate remains pending user review for exact hosiery and leg-axis acceptance.

## Approval and promotion

- User approval: "可以的，登记为body01正式资产"
- Approved component: `OWNER_BODY_01_FRONT_CANON_007`
- Promoted path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png`
- Promotion operation: moved unchanged under the single-file storage rule; no candidate raster remains in this directory.
- Approved at: `2026-09-18`
