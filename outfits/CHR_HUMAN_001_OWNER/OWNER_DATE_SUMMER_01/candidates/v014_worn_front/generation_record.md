# Outfit Generation Record — v014 foot textile and straight taper

- asset_id: OWNER_DATE_SUMMER_01_WORN_FRONT_v014
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- asset_purpose: worn_fit_validation
- view_type: worn_front
- head_policy: original_registered_face_recipe_user_scoped_override
- candidate_version: v014
- status: REVIEW_REQUIRED
- authorization: user 2026-10-31 “腿上的还行，脚脖子以下像是硅胶质感了。脚趾间还是没有袜面覆盖和袜面张力，小腿还是不直。重做”
- generation_tool: built-in image_gen.imagegen
- generated_at: 2026-10-31
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v014_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v014.png
- output_sha256: aee71c1f215076d387cedded38373114401c20ac70be8c89bb001b6406b53542

## Validation target

Keep leg white-fabric direction and accepted face recipe, repair ankle/foot silicone surface, visible closed-toe knit envelope and intertoe tension, straight lower-leg axes AND gently straight tapered silhouette. Navel/true high waist/no lower extra band remain mandatory.

## Generation inputs / QA comparison only

```json
{
  "generation_inputs": [
    {
      "asset_id": "OWNER_REGISTERED_B_FACE_AND_L0_HAIR_NATIVE_BOARD_001",
      "path": "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_AND_L0_HAIR_NATIVE_BOARD_001.png",
      "sha256": "f35a31a2211bc46669717c15380f6e04542687055b1c32c6f622b47a47c14ac4",
      "version": "v1 native source board",
      "responsibility": "left: original B face/skin; right: original L0 masked Hair-A; no averaging",
      "must_not_define": [
        "board layout",
        "gray missing data",
        "B hairstyle",
        "body",
        "clothes",
        "hosiery",
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
    },
    {
      "asset_id": "HOS_15D_NM_011_FEET_TOE_COVERAGE_CROP_002",
      "path": "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_FEET_TOE_TEXTILE_COVERAGE_ONLY_CROP_v1.png",
      "sha256": "4ac17d6b3a619a4a4fd0cf262c2a2fdd8a9d9c1e838c4701991cbcee782a7a4a",
      "version": "v1 deterministic feet-only crop",
      "responsibility": "supplementary visible toe fabric envelope, intertoe tension and softly veiled nail edges only",
      "must_not_define": [
        "color",
        "finish",
        "opacity/denier",
        "skin",
        "nail color",
        "anatomy",
        "pose",
        "shoes",
        "floor",
        "light",
        "background"
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
    },
    {
      "asset_id": "OWNER_DATE_SUMMER_01_WORN_FRONT_v013",
      "path": "outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v013_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v013.png",
      "comparison_scope": "user accepted leg fabric direction only; failed foot/calves excluded; not generation input"
    }
  ],
  "reference_budget": {
    "maximum_images": 5,
    "actual_images": 5,
    "material_images": 2,
    "material_reason": "mandatory white overall source plus narrowly scoped missing toe-fabric coverage detail"
  }
}
```

## Reference resolution and isolation

Registered Face method/v009 recipe + user-scoped explicit instruction remain in force; generated B-derived face origin declared, not L0-only. Native face/hair board retains exact source pixels and distinct duties; no Face Canon or failed candidate input. Body upper crop and garment-isolation v2 from registered source references. White source from HOS_USER_SELECTED_WHITE_STRICT_WIDE_CROP_V2 and nearest hosiery guide. Supplemental toe crop derives from HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001/L0_HOS_15_NM_011: only coverage/tension, not color/finish/denier. This fills the documented user-rejected foot-coverage gap; mandatory white source is not replaced. Two material inputs justified by source-library guide. Provenance/checksums/geometry sidecars retained; no candidate-local raster input copies.

## Prompt/settings

Exact PROMPT.txt. One full-body3:4 opaque candidate, preferably1536x2048/native higher detail; model/seed/quality not exposed, defaults. Budget five input files, two logical Face/Hair panels, two material responsibilities.

## QA

- technical_status: FAIL_UNRESOLVED_FOOT_AND_CALVES
- fit_validation_status: FAIL_UNRESOLVED_FOOT_AND_CALVES
- face_contamination_check: REVIEW_REQUIRED
- previous_candidate_pixels_used: false
- previous_shot_pixels_used: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false
- lighting_or_background_taken_from_material_reference: false
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- decision: Pending independent rebuild; no promotion/approval.

## Actual output

- dimensions: 1086×1448
- tool output: /home/verdvana/.codex/generated_images/01a19227-4b9d-7881-83ba-993a94494e09/exec-bd5ab999-965e-4b4d-9093-c678f009a209.png
- copied unchanged into unique project candidate; SHA-256 above
- result: Full-body output still has weak toe envelope and residual bowed calves; foot appears too smoothly coated. User leg material direction only previously accepted, no output approval.
- No user approval, promotion or replacement. No downstream use.
