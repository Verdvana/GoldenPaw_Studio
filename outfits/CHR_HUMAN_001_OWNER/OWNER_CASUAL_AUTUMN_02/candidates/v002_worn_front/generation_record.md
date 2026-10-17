# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v002

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v002
outfit_id: OWNER_CASUAL_AUTUMN_02
level: L2
asset_purpose: worn_front
view_type: worn_front
head_policy: head_present_owner_face_method
candidate_version: v002
target_canon_version: owner_v1.0
spec_revision: draft_1.234
identity_revision: draft_0.187
status: REJECTED
approval_status: USER_REVIEW_REQUIRED
gate: L2 outfit front fit-validation
generation_tool: built-in ImageGen
generated_at: 2026-10-17
output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v002_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v002.png
output_sha256: c18486ff91ae274653cb15cbd77269b57debd8498e115ad6dc157246b25d3e21
reference_set_ids:
  - OWNER_L0_FACE_013_GEOMETRY_CROP_V1
  - OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE
reference_budget: 5 image inputs; 3 QA-only comparisons
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4 requested"
seed_settings: ImageGen did not expose seed or sampler settings
```

## Validation target

- fit_or_design_question: Does the outfit keep the approved colors and materials while giving the wool mini skirt a visibly narrower, restrained silhouette?
- acceptance_checks:
  - Skirt side seams descend nearly straight from the hip, with a subtle A-line only; hem is modestly wider than hip and clearly less flared than v001.
  - No umbrella, circle-skirt or strong flare; skirt remains comfortable and not skin-tight.
  - Oatmeal cardigan, ivory tee, white slightly sheer hosiery and pale beige-tan fuzzy open-toe slippers remain unchanged.
  - Face generated only from deterministic L0-derived face/skin crops and the FACE_01 method constraints; no AI Face/Body or previous candidate is a generation input.
  - Face Canon is used only after generation for comparison QA; check no identity drift, skin patches, blotches, smudges or muddy relighting.
  - Hairstyle A only; body reference is the face-excluded derivative and defines neck-below proportions only.
  - Pantyhose continuously covers toes beneath both open-toe slippers, with subtle natural show-through and no material break or plastic appearance.
  - Full head-to-feet framing, relaxed standing front view, both feet grounded, no cropping, watermark, logos or extra anatomy.

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png
    responsibility: L0-derived recognizable facial feature geometry and identity only
    must_not_define: source makeup, hair, skin color/retouch, camera, lighting, clothing, body, background
  - asset_id: OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png
    responsibility: natural L0 skin color and texture baseline only
    must_not_define: fine facial geometry, source hairstyle, makeup, camera, body, clothing, lighting, background
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    responsibility: L0 Hairstyle A pixels and construction only
    must_not_define: face, skin, identity, body, clothing, lighting, background, or gray mask
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: neck-below front body geometry, proportions, stance and foot scale only
    must_not_define: face, facial identity, hair, clothing design, hosiery material/color, lighting, background
  - asset_id: OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png
    responsibility: approved garments, colors, layering and footwear; latest user text narrows the skirt hem silhouette
    must_not_define: face, body, proportions, skin, hair, identity, pose, hosiery anatomy, lighting, background
```

## QA comparison only

```yaml
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope: identity drift, facial-feature relationships, skin contamination, projection and framing
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    comparison_scope: front body proportion and stance only
  - asset_id: L0_HOS_15_WSS_002
    path: materials/hosiery/source_library/raw/15d_white_soft_sheen/IMG_2604.jpg
    comparison_scope: post-generation white tone, slight sheerness and textile response only
```

## Reference isolation

- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` prompt constraints plus source-derived L0 crops
- hairstyle: `HAIRSTYLE_A`
- approved_ai_face_or_body_used_as_generation_input: `false`
- approved_ai_face_used_qa_comparison_only: `true`
- body_reference_is_face_excluded_derivative: `true`
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- garment_reference_used_for_identity_or_body: `false`

## Prompt assembly

Create exactly one fresh independent L2 full-body front worn-outfit candidate. Do not
edit, continue, or use any previous outfit candidate image. Generate the face only
from the two listed deterministic L0 face/skin derivatives with the source-derived
FACE_01 prompt constraints; never use AI Face/Body images or prior candidates as face
inputs. Preserve natural recognizable adult face geometry, warm-neutral skin, neutral
closed-mouth expression and eye-level portrait projection. Use the face-masked L0
DSC00847 source only for Hairstyle A: long straight loose dark-brown hair, restrained
near-center part, close roots, low crown and tapered ends. No hairstyle B or hybrid.
Use the face-excluded body derivative only for neck-below proportions and stance.

Wear the approved cream-oatmeal buttoned knit cardigan over a plain warm-ivory tee,
white thin slightly sheer pantyhose, and pale beige-tan fuzzy open-toe mule slippers.
The wool mini skirt is a warm medium-brown and must be visibly less flared than the
previous worn-front attempt: slim straight mini silhouette with only a restrained
slight A-line, side seams nearly straight from hip to hem, and a hem only modestly
wider than the hip line. Do not make it an umbrella, circle skirt, bell shape, or
strong flare. Keep natural wearing ease; do not turn it into a tight bodycon skirt.
Preserve all other garment colors, materials and lengths.

Keep white pantyhose continuous from waistband through hips, legs, ankles, heels,
instep and toes; show a soft textile veil over the toes through the open slipper
fronts, with subtle natural skin tone visible through the fabric. No bare-skin gaps,
hard rings, plastic/latex gloss or material discontinuity. Natural relaxed front
stance with both feet grounded. Full head, hair, hands and slippers within frame,
neutral gray-white studio, soft even 5200–5600K light and level 70–85mm perspective.
No logos, text, watermark, props, collage or extra anatomy. One candidate only;
REVIEW_REQUIRED, not Canon.

## QA

- technical_status: `FAIL` — native output is 1024 × 1536 (2:3), not the required 3:4
- fit_validation_status: `FAIL`
- face_contamination_check: `REVIEW_REQUIRED`
- face_generation_method_followed: `true`
- skirt_silhouette_check: `PASS` — hem is markedly narrower and no longer umbrella-shaped
- outfit_fidelity_check: `REVIEW_REQUIRED`
- hosiery_continuity_and_material_check: `REVIEW_REQUIRED`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `REJECTED — skirt refinement passed, but output aspect ratio and non-frontal head angle do not meet the worn-front contract.`
- reviewer: `Codex`
- reviewed_at: `2026-10-17`
