# Outfit Generation Record — v013 navel / original silky hosiery / toe envelope

- asset_id: OWNER_DATE_SUMMER_01_WORN_FRONT_v013
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- asset_purpose: worn_fit_validation
- view_type: worn_front
- head_policy: head_present_registered_face_recipe_user_scoped_override
- candidate_version: v013
- status: REVIEW_REQUIRED
- authorization: user 2026-10-31 “肚脐眼看不到了。袜面质感还是没有参考我上传的图片，丝袜脚趾间的袜面张力和覆盖脚趾的感觉还是不够”
- generation_tool: built-in image_gen.imagegen
- generated_at: 2026-10-31
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v013_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v013.png
- output_sha256: 3a7ebac31320f4a991a4f9ff9d2e57cb88388a89ea536855adf10af8abf46b5f

## Validation target

Natural navel visible through hosiery, original-source semi-sheer silky fiber sheen instead of matte overcorrection, actual closed-toe fabric envelope/knit haze and intertoe V-shaped tension valleys. Retain accepted face recipe, no lower extra band, straight shins.

## Generation inputs / QA comparison only

```json
{
  "generation_inputs": [
    {
      "asset_id": "OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001",
      "path": "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png",
      "version": "FACE_01_FRONT_NEUTRAL_METHOD_v1",
      "sha256": "d98019128bfa974a102813da52b4a2905ec4aa7c95eb5222a163e419f287e74d",
      "responsibility": "registered face feature relationships/skin only",
      "must_not_define": [
        "B hair",
        "crown",
        "source camera",
        "body",
        "pink clothes",
        "light",
        "background"
      ]
    },
    {
      "asset_id": "OWNER_HAIRSTYLE_A_FACE_MASKED_001",
      "path": "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png",
      "version": "v1",
      "sha256": "6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd",
      "responsibility": "Hairstyle A only",
      "must_not_define": [
        "face",
        "mask",
        "skin",
        "body",
        "clothes",
        "light",
        "background"
      ]
    },
    {
      "asset_id": "OWNER_BODY_TORSO_UPPER_LEGS_NO_CALVES_001",
      "path": "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_TORSO_UPPER_LEGS_NO_CALVES_CROP_v1.png",
      "version": "v1 crop",
      "sha256": "e169af72c55c5801d9932f832ed72e080d1c4ccb4b2f14a76757b19ee4c0b5bd",
      "responsibility": "neck-below torso/hip and upper-thigh volume only; calves/ankles/feet absent",
      "must_not_define": [
        "face",
        "skin",
        "hair",
        "clothes",
        "hosiery",
        "light",
        "background",
        "lower-leg bowing or leg-axis deviation"
      ]
    },
    {
      "asset_id": "OWNER_DATE_SUMMER_01_GARMENT_ISOLATED_v003_002",
      "path": "outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/reference_inputs/garment_isolation_v2/DESIGN_v003_GARMENTS_TRUE_UPPER_WAISTBAND_NO_LEGS.png",
      "version": "v2 isolated garment/true upper waistband",
      "sha256": "9035ce51b8948993076b47930fe46392d1cd05bc8c1d697064dd3cb10dd1f8aa",
      "responsibility": "blouse, shorts, sandals and true high waistband placement only; lower band/legs/toes masked",
      "must_not_define": [
        "face",
        "skin",
        "body",
        "hair",
        "hosiery material",
        "identity",
        "lighting",
        "background",
        "extra white band just above shorts",
        "toe nakedness",
        "hosiery gloss"
      ]
    },
    {
      "asset_id": "HOS_USER_WHITE_001_LOWER_BODY_LEG_FOOT_CROP_002",
      "path": "materials/hosiery/reference_inputs/user_selected_white/PHOTO_1_LOWER_BODY_LEG_FOOT_MATERIAL_CROP_v2.png",
      "version": "source_v1/crop_v2",
      "sha256": "f0aeb037eba8b1a17075c85fcf3baf11329643cf01023ac8e3b38f04a1635c5b",
      "responsibility": "HOS_USER_SELECTED_WHITE_STRICT broader original lower-body crop: white semi-sheer SILKY textile sheen and whole foot coverage, source-only responsibility",
      "must_not_define": [
        "face",
        "identity",
        "skin",
        "body/leg/foot geometry",
        "hands",
        "pose",
        "outfit",
        "shoes",
        "car",
        "background",
        "watermark",
        "scene lighting",
        "exact denier"
      ]
    }
  ],
  "qa_comparison_only": [
    {
      "asset_id": "OWNER_FACE_01_FRONT_NEUTRAL_CANON_001",
      "path": "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg",
      "comparison_scope": [
        "facial relationships",
        "skin contamination",
        "identity drift",
        "projection"
      ]
    },
    {
      "asset_id": "OWNER_DATE_SUMMER_01_WORN_FRONT_v005",
      "path": "outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v005.png",
      "comparison_scope": [
        "previous approved likeness and outfit fit only"
      ]
    },
    {
      "asset_id": "L0_HOS_USER_WHITE_001",
      "path": "materials/hosiery/source_library/raw/user_selected_white/PHOTO_1.jpg",
      "comparison_scope": [
        "white textile only"
      ]
    },
    {
      "asset_id": "OWNER_DATE_SUMMER_01_WORN_FRONT_v009",
      "path": "outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v009_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v009.png",
      "comparison_scope": [
        "user-accepted face likeness only; NOT generation input; reject its material/leg/toe defects"
      ]
    }
  ],
  "reference_budget": {
    "maximum_images": 5,
    "actual_images": 5
  }
}
```

## Reference resolution and provenance

Original registered B face/skin recipe under current user-scoped method authorization and accepted v009 likeness; B-derived input has GENERATED origin, not falsely called L0. All prior fitting images are QA-only, never generation inputs. Body torso/upper-leg crop and garment-isolation v2 exclude prior calf/toe/lower-band contamination.

Material: registry HOS_USER_SELECTED_WHITE_STRICT plus source-library REFERENCE_GUIDE and MATERIAL_REFERENCE.md. v2 deterministic crop broadens immutable original-photo coverage to include bent thigh/knee response and entire visible front foot, retaining one material input; no source reclassification, denier inference or new Canon. All source/operation/checksums and exclusions in derivative sidecar/PROVENANCE.json. Original L0 remains unchanged, no duplicate ingestion or candidate-local pixel copies.

## Prompt/settings and reference isolation

Exact submitted PROMPT.txt. Requested exact3:4, preferably1536x2048, opaque. Tool settings/model/seed not exposed, defaults. Five images total/one material input. Previous candidate/shot pixels: false. Face/body/skin/hair cannot inherit from material/garment. Original B/hair/body/clothing source responsibility unchanged.

## QA

- technical_status: PASS_NATIVE_IMAGE
- fit_validation_status: FAIL_UNRESOLVED_TOE_TENSION_AND_CALF_ALIGNMENT
- face_contamination_check: no obvious blotches; likeness pending user review
- face_generation_method_followed: original registered B recipe under explicit user-method scope
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- decision: Generated; navel is more readable and original silky material response closer, but toe textile bridges and calf straightness remain unresolved. No approval/promotion/replacement.

## Actual output and QA

- Native dimensions: 1086×1448, exact3:4. Preferred1536x2048 was not returned; no upscaling performed.
- Tool output: /home/verdvana/.codex/generated_images/01a19227-4b9d-7881-83ba-993a94494e09/exec-9d2f689e-a110-45f0-943f-9793472f144e.png
- Copied unchanged to unique project candidate path; checksum above.
- Navel: visibly recognizable as an indentation/shadow beneath translucent abdominal hosiery; upper true waistband preserved, no obvious separate lower band.
- Material: pearl-white translucency and stronger silk-like sheen return compared with matte v012, consistent with broader real-source response. Exact match and absence of residual oily appearance remain user review.
- Toe tension/covering: still not convincingly resolved at native full-body scale; toe separations/nails remain too independently skin-like. Must not declare coverage/tension QA pass.
- Calves: residual knee-to-ankle inward drift/curved contour still exists. Not a straight-calf pass.
- Face: original accepted recipe reused, no obvious blotches; no new likeness approval inferred.
- Overall: user review required / unresolved QA failure; no downstream use or automatic promotion.
