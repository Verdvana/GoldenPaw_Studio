# Outfit Generation Record — v012 targeted correction

- asset_id: OWNER_DATE_SUMMER_01_WORN_FRONT_v012
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- asset_purpose: worn_fit_validation
- view_type: worn_front
- head_policy: head_present_registered_face_recipe_user_scoped_override
- candidate_version: v012
- status: REVIEW_REQUIRED
- authorization: ongoing user request to retain accepted face and fix lower band/dry textile/straight calves/toe covering
- generation_tool: built-in image_gen.imagegen
- generated_at: 2026-10-31
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v012_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v012.png
- output_sha256: 0f0378a2f15cf683e87eee32682e673e0a874f886d2e7468cecd21b1acd5ba43

## Validation target

Keep true upper waistband and sheer abdominal coverage while excluding extra lower band. Dry textile, straight parallel knee-ankle axes with non-touching feet, coherent toe envelope and V tension.

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
      "asset_id": "HOS_USER_WHITE_001_LOWER_LEG_FOOT_CROP_001",
      "path": "materials/hosiery/reference_inputs/user_selected_white/PHOTO_1_LOWER_LEG_FOOT_MATERIAL_CROP.png",
      "version": "source_v1/crop_v1",
      "sha256": "ce3b4fe1aafebe2818baae37dd3a76ca712820b1232d2ed15e06adf55002095d",
      "responsibility": "strict white color/translucency/sheen/coverage",
      "must_not_define": [
        "identity",
        "face",
        "skin",
        "hair",
        "anatomy",
        "pose",
        "clothes",
        "shoes",
        "car",
        "background",
        "scene lighting",
        "denier"
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

## Isolation and prompt/settings

Same registered B face/skin recipe under current explicit user instruction and accepted v009 face scope; generated provenance disclosed, not L0-only. No prior candidate pixels used. Body input ends at upper legs; garment-isolation v2 preserves true waistband but masks lower artifact and legs/toes. Source/derivative operations and checksums in sidecars/PROVENANCE. All refs resolve from existing Face method, scoped Body/reference registry, approved outfit v003 and HOS_USER_SELECTED_WHITE_STRICT. Exact submitted text PROMPT.txt. Reference budget five images/one material photo. Seed/model/quality not exposed, defaults; exact 3:4 opaque.

## QA

- technical_status: PASS_NATIVE_IMAGE
- fit_validation_status: FAIL_UNRESOLVED_CALF_TOE_DETAIL
- face_contamination_check: no obvious blotches; likeness still requires user confirmation
- face_generation_method_followed: registered original B recipe, user-scoped revision
- previous_candidate_pixels_used: false
- previous_shot_pixels_used: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false
- lighting_or_background_taken_from_material_reference: false
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- decision: Generated; lower band and wet highlights improved, but calf straightness and clear toe-fabric tension remain insufficient. No approval/promotion/replacement.

## Actual result

- Native output: 1086×1448, exact 3:4.
- Original tool path: /home/verdvana/.codex/generated_images/01a19227-4b9d-7881-83ba-993a94494e09/exec-87f1719b-9cc7-4b2d-a76a-621224bac9db.png
- Project output and SHA-256 recorded above. No repository duplicates.
- Extra lower white band removed, true upper waistband/sheered abdominal span retained.
- Oily/watery streaks substantially suppressed; fabric is dry with soft diffuse response, perhaps too matte compared with original sheen.
- Wider balanced foot stance reduces inward ankle drift; exact calf straightness still not fully convincing. Do not claim all leg correction passed.
- Toes still appear too individually skin-like with insufficient continuous veil/interdigital fabric tension. This is an unresolved QA failure, not approved.
- Face recipe unchanged; no new face approval inferred for changed output.
