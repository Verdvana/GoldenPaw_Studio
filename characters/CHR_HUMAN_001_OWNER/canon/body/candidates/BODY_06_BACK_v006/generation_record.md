# BODY_06_BACK_v006 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: BODY_06_BACK
candidate_id: BODY_06_BACK_v006
target_canon_version: owner_v1.0
gate: Gate 3 — Body Canon
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
spec_revision: draft_1.235
identity_revision: draft_0.185
body_method_id: OWNER_BODY_06_BACK_METHOD_V1
generation_tool: built_in_image_gen
use_case: identity-preserve
reference_set_ids:
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_L0_BODY_REAR_SIDE_CONTEXT
  - OWNER_HAIR_A_BACK_CANON_L1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
generation_inputs:
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", responsibility: "current Body01 Canon 007 neck-below front geometry: waist/hip relationship, torso length, leg width, outer contours, straight axes, foot scale and stance", must_not_define: "face, facial identity, hair, clothing design, hosiery material, lighting or background"}
  - {asset_id: L0_OWNER_002, path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/3.jpg", responsibility: "168 cm stature and natural body context", must_not_define: "face, hair, clothing, shoes, props or background"}
  - {asset_id: L0_OWNER_015, path: "characters/CHR_HUMAN_001_OWNER/source/identity/raw/17.jpg", responsibility: "rear/side torso depth and silhouette plausibility only", must_not_define: "front-derived leg width/outer contours, face, hair, clothing, shoes or environment"}
  - {asset_id: OWNER_HAIR_A_04_BACK_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_04_BACK/OWNER_HAIR_A_04_BACK_CANON_001.png", responsibility: "exact centered rear Hairstyle A fall only", must_not_define: "face, body, clothing, hosiery, lighting or background"}
  - {asset_id: OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001, path: "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png", responsibility: "slightly-whitish 15D matte/velvet hosiery, continuous foot coverage and heel transparency behavior", must_not_define: "identity, body/foot anatomy, clothing, nail color, pose or background"}
qa_comparison_only:
  - {asset_id: OWNER_BODY_01_FRONT_CANON_007, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png", purpose: "post-generation whole-image visual comparison only; not a generation input"}
  - {asset_id: OWNER_BODY_06_BACK_CANON_003, path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_06_BACK_v005/BODY_06_BACK_v005.png", purpose: "secondary historical back-view QA only"}
  - {asset_id: BODY_06_BACK_v005, path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_06_BACK_v005/BODY_06_BACK_v005.png", purpose: "historical comparison only; not a generation input"}
reference_count: 5
previous_ai_body_candidate_count: 0
authoritative_for:
  - "exact 180-degree rear body presentation"
  - "front-aligned torso, waist/hip and leg contour correspondence"
  - "corresponding high-cut rear one-piece opening"
  - "increased heel translucency gradient under continuous hosiery"
must_not_define:
  - "face or facial identity"
  - "any AI-to-AI identity lineage"
  - "other body angles or poses"
  - "other hosiery colors, deniers or finishes"
  - "lighting/background design, props, text or watermark"
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced 1536x2048 resize"
prompt_assembly: "v005 back-view prompt rebuilt against current Canon 007 face-excluded derivative, with corresponding rear opening and higher heel translucency."
seed: null
settings: {tool: "built_in_image_gen", output: "single native candidate", preferred_resolution: "native exact 3:4"}
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_06_BACK/OWNER_BODY_06_BACK_CANON_004.png
sha256: 7bcaec66bf4ff9c4c4c2016d7578b2f88d79e3b3f9ec8502a24d0535d3007c0b
dimensions: 1086x1448
qa_status: APPROVED_BY_USER
```

## Prompt assembly

Create exactly one neutral, non-erotic, exact 180-degree full-length back-view technical body reference of the same adult woman, fully clothed in the established pink high-cut one-piece calibration garment, continuous pale slightly-whitish 15D matte/velvet sheer hosiery and no shoes. The back of the head and body face directly away from the camera with no twist. There is no visible face; do not invent face identity.

Use Image 1 as the primary authority for every neck-below proportion and silhouette correspondence. Use Images 2–3 only to add plausible rear torso depth and natural back-side context; they must not override the front-derived waist/hip width, leg width, outer leg contours or foot scale. Use Image 4 only for exact centered rear Hairstyle A fall. Use Image 5 only for hosiery textile and heel behavior. Do not use any previous generated back image or whole approved front image as an image input.

The back silhouette must correspond to the current front Canon 007: same 168 cm / approximately 60 kg scale; same narrower natural waist and smooth waist-to-hip transition; same torso length, hip width, fuller thigh/calf volume, straight lower-leg axes, leg width and outer-contour envelope at corresponding heights. The outer edges of the back thighs and calves must continue at the same effective widths as the front-derived contour, without narrowing, bowing, inward taper or independent redesign. Keep a very narrow natural inner-leg gap, symmetric knees and ankles, uncrossed legs and both feet fully flat.

The rear one-piece opening must be a clearly raised/high-cut athletic opening whose height and side transitions correspond to the front high-cut opening: same waist-to-hip-to-upper-thigh relationship, symmetric left/right, no low brief line, skirt, shorts or separate garments. Do not make the rear opening deeper or lower than the front logic.

Hosiery must read as one continuous slightly-whitish pale 15D textile over the full legs, ankles, heels, insteps and toes, with no seams, white rings, hard bands, plastic appearance or material discontinuity. At both rear heels, increase the translucent skin gradient so the heel region is visibly more transparent than the lower calf/ankle while remaining covered by the same textile; the gradient must be smooth and gradual, with no circular edge, horizontal boundary or abrupt color step. Feet remain flat and naturally grounded.

Neutral gray-white seamless studio, soft even 5200–5600K light, level 70–85mm-equivalent camera, exact native 3:4 portrait, complete head/hair and feet visible, no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Primary checks: rear body width and outer contour at corresponding heights against the v025 face-excluded derivative; same waist/hip transition and leg volume; straight axes and flat feet; rear high-cut opening height/side transitions corresponding to the front; continuous pale hosiery; higher but smooth heel translucency with no ring/band/boundary; exact 180-degree rear direction; no identity or material contamination. No promotion without explicit user approval.

## Generation output

- Built-in ImageGen returned one native exact-3:4 candidate.
- Repository candidate: `BODY_06_BACK_v006.png`
- Native dimensions: `1086x1448`, no resolution conversion performed.
- Initial visual precheck: rear torso/leg contour follows the current front-derived geometry, rear high-cut opening is corresponding, and heel regions show increased gradual translucency. Candidate remains `REVIEW_REQUIRED`.

## Approval and promotion

- User approval: "批准，登记"
- Approved component: `OWNER_BODY_06_BACK_CANON_004`
- Promoted path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_06_BACK/OWNER_BODY_06_BACK_CANON_004.png`
- Promotion operation: moved unchanged under the single-file storage rule; no candidate raster remains in this directory.
- Approved at: `2026-09-18`
