# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v003

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v003
outfit_id: OWNER_CASUAL_AUTUMN_02
asset_level: L2
asset_purpose: worn_front
view_type: worn_front
head_policy: head_present_owner_face_method
candidate_version: v003
target_canon_version: owner_v1.0
spec_revision: draft_1.234
identity_revision: draft_0.187
status: REVIEW_REQUIRED
approval_status: USER_REVIEW_REQUIRED
gate: L2 outfit front fit-validation
generation_tool: built-in ImageGen
generated_at: 2026-10-17
output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v003_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v003.png
output_sha256: cfc0516392aba02e41dcd5570604a4de019290003417fb34efe32fc1fec7dcba
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

- fit_or_design_question: Does the narrower skirt fit contract read naturally in a strict 3:4 full-body frontal validation view?
- acceptance_checks:
  - Exact 3:4 portrait and full head-to-feet framing; head and torso square to camera, neutral closed-mouth face, no three-quarter head turn.
  - Skirt side seams descend nearly straight from the hip; subtle A-line only, hem modestly wider than the hip and clearly narrower than v001; no umbrella/circle/bell flare and not skin-tight.
  - Approved colors/materials, face-safe input lineage, Hairstyle A, body proportion, and continuous thin white pantyhose are otherwise unchanged.

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png
    responsibility: L0-derived facial feature geometry and recognizable identity only
    must_not_define: source makeup, hair, skin color/retouch, camera, lighting, clothing, body, background
  - asset_id: OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png
    responsibility: natural L0 skin color and texture baseline only
    must_not_define: fine facial geometry, source hair, makeup, camera, body, clothing, lighting, background
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    responsibility: L0 Hairstyle A pixels and construction only
    must_not_define: face, skin, identity, body, clothing, lighting, background, gray mask
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: neck-below front body proportions, stance and foot scale only
    must_not_define: face, facial identity, hair, clothing design, hosiery material/color, lighting, background
  - asset_id: OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png
    responsibility: approved garments, palette, layers and slippers only
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
    comparison_scope: body proportions and stance only
  - asset_id: L0_HOS_15_WSS_002
    path: materials/hosiery/source_library/raw/15d_white_soft_sheen/IMG_2604.jpg
    comparison_scope: post-generation hosiery tone, sheerness and textile response only
```

## Reference isolation

- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` prompt constraints plus the two L0-derived face/skin crops
- hairstyle: `HAIRSTYLE_A`
- approved_ai_face_or_body_used_as_generation_input: `false`
- approved_ai_face_used_qa_comparison_only: `true`
- body_reference_is_face_excluded_derivative: `true`
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- garment_reference_used_for_identity_or_body: `false`

## Prompt assembly

Create exactly one fresh, independent, photorealistic L2 front worn-fit image. The
canvas must be portrait 3:4 exactly, with the full head and both feet inside the frame;
do not use a 2:3 crop or composition. The woman's head, shoulders, torso, hips, knees
and feet face directly forward and are square to the camera; head upright, chin
neutral, eyes toward lens, mouth closed, no smile and no three-quarter turn.

Generate the face only from the two listed deterministic L0-derived face/skin crops
and the source-derived FACE_01 prompt constraints. No AI Face Canon, Body Canon,
previous candidate or generated image is a face-generation input. Preserve recognizable
natural facial feature relationships, adult age and warm-neutral skin without
beautification, facial reshaping, whitening, cooling, smudges or uneven patches. Use
the face-masked DSC00847 L0 source only for Hairstyle A: long, straight, loose dark-
brown hair, restrained near-center part, close roots and low crown. No hairstyle B
or hybrid. Use the face-excluded body derivative only for neck-below proportions and
front stance.

Wear the approved cream-oatmeal buttoned knit cardigan over a warm-ivory tee, the
lighter warm-medium-brown wool mini skirt, thin slightly sheer white pantyhose and
pale beige-tan fuzzy open-toe mule slippers. The skirt must have a slim, restrained
shape: side seams nearly straight from hip to hem; a modest, slight A-line; the bottom
hem only a little wider than the hip. Make the hem visibly narrower than the previous
wide-flared attempt. No umbrella, circle, bell or strong flare, and do not make the
skirt tight or bodycon. Keep natural wearing ease and preserve all other garment
colors, materials and lengths.

The white pantyhose remains one continuous textile from waist through legs, heels,
instep and toes. Show subtle natural skin tone through the fabric and a visible white
textile veil over toes through the open slippers. No bare-skin gaps, hard color rings,
plastic, latex, oily gloss or broken coverage. Both feet grounded and fully visible.
Neutral gray-white seamless studio, soft even 5200–5600K light and a level
70–85mm-equivalent camera. No logos, text, watermark, props, collage or extra anatomy.
One candidate only, REVIEW_REQUIRED, not Canon.

## QA

- technical_status: `PASS` (1086x1448, exact 3:4, full head-to-feet)
- fit_validation_status: `FAIL` (thin white pantyhose absent; bare legs visible)
- face_contamination_check: `PASS` (visual comparison only; no obvious blotches or relighting patches)
- face_generation_method_followed: `true`
- skirt_silhouette_check: `PASS` (hem restrained, only slightly wider than hip; no umbrella flare)
- framing_and_front_pose_check: `PASS` (front-facing head and torso; full figure in frame)
- outfit_fidelity_check: `FAIL` (required hosiery missing)
- hosiery_continuity_and_material_check: `FAIL` (bare legs and toes; no hosiery textile)
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `REJECTED`
- reviewer: `Codex visual QA`
- reviewed_at: `2026-10-17`
