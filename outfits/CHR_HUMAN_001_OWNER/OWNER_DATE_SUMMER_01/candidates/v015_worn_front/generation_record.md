# Outfit Generation Record — v015 approved foot integration

- asset_id: OWNER_DATE_SUMMER_01_WORN_FRONT_v015
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- asset_purpose: worn_fit_validation
- view_type: worn_front
- head_policy: registered_original_face_recipe_user_scoped_override
- candidate_version: v015
- status: APPROVED
- authorization: user 2026-10-31 “脚部ok，批准，请生成全身试穿图”
- generation_tool: built-in image_gen.imagegen
- generated_at: 2026-10-31
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v015.png
- output_sha256: e9d59c10a5a269c5aeeab777bc19f65fc041d9dab54642c8a175b34cdc199b25

## Validation target

Full-body integration of explicitly approved L2 foot detail: knit veil/tension/closed toes and wrinkle-free ankles. Original accepted face recipe, original white-leg appearance, navel-through-hosiery/high waistband/no lower extra strip, straight parallel lower legs.

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
      "asset_id": "OWNER_DATE_SUMMER_01_FOOT_MATERIAL_DETAIL_v002",
      "path": "outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/foot_material_detail/OWNER_DATE_SUMMER_01_FOOT_MATERIAL_DETAIL_v002.png",
      "sha256": "02718418b7a55bd1fc44023ca5059b88b4dc5a42738f8c918458ce4a48178897",
      "version": "v002 approved L2",
      "responsibility": "approved foot textile covering/toe-nail veil/intertoe fabric tension, fine-knit surface, smooth wrinkle-free ankle; not a foot pose/identity source",
      "must_not_define": [
        "face",
        "identity",
        "skin",
        "body or foot anatomy",
        "pose",
        "new denier/color/finish",
        "camera",
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
    },
    {
      "asset_id": "OWNER_DATE_SUMMER_01_FOOT_MATERIAL_DETAIL_v002",
      "path": "outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/foot_material_detail/OWNER_DATE_SUMMER_01_FOOT_MATERIAL_DETAIL_v002.png",
      "comparison_scope": "foot integration matches user-approved veil, tension and wrinkle-free ankle"
    }
  ],
  "reference_budget": {
    "maximum_images": 5,
    "actual_images": 5,
    "material_images": 2,
    "reason": "mandatory L0 white appearance + explicitly approved L2 toe/ankle textile construction detail"
  }
}
```

## Reference resolution / provenance

Face source board retains original registered B-crop/Hair-A sources, same current user-scoped method exception, generated B origin openly declared rather than L0-only. Body torso-only crop and garment-isolation v2 keep old bowed calves/toes/lower strip out of generation. Resolve those via prior scoped provenance; raw white material from HOS_USER_SELECTED_WHITE_STRICT_WIDE_CROP_V2. New foot source from OWNER_DATE_SUMMER_01_FOOT_MATERIAL_DETAIL_APPROVED_V002, approved image moved unchanged with checksum/approval evidence before this call. It defines only reviewed L2 material behavior, no identity/anatomy/pose or L1 Canon. No failed fitting pixels used.

## Prompt/settings and isolation

Exact PROMPT.txt; seed/model/quality not exposed, defaults. Target3:4, preferably1536x2048/native higher detail, opaque. Five images, two material duties, no candidate-local raster copies. Approved foot input is legitimate user-approved material lineage, not identity lineage.

- previous_candidate_pixels_used: false (approved foot image is approved L2 input, prior failed fitting pixels absent)
- previous_shot_pixels_used: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false
- lighting_or_background_taken_from_material_reference: false

## QA

- technical_status: PASS_NATIVE_IMAGE
- fit_validation_status: APPROVED_BY_USER
- face_contamination_check: no obvious blotches; exact likeness requires user review
- face_generation_method_followed: original registered B source method, current user-scoped instruction
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- decision: Full-body candidate generated using approved foot v002; integration and straightness remain imperfect, user review required, no automatic approval or replacement.

## Actual output / initial QA

- Native dimensions: 1086×1448, exact3:4. No resize or sharpening applied.
- Original tool file: /home/verdvana/.codex/generated_images/01a19227-4b9d-7881-83ba-993a94494e09/exec-734afa54-e6b2-40b6-a6f8-e90c86b6d4c7.png
- Unique repository raster: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v015_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v015.png
- True high waistband and navel visibility retained, no obvious second lower band. Accepted original face method reused; no patch contamination observed.
- Approved foot reference was actually supplied, but textile/tension transfer to small full-body toe regions is not convincing enough; no complete foot-material pass asserted. Nails are more conspicuous than in approved close-up.
- Lower legs remain asymmetric/curved with uneven foot alignment and slight weight shift, contrary to straight parallel target. Straightness QA fails.
- Clothing generally retained; head/hands/shoes fully in frame.
- New image is REVIEW_REQUIRED and cannot be downstream input; approved foot v002 remains APPROVED independently. No old approved fitting overwritten.

## Final user approval / promotion — supersedes pending disposition

# User approval — summer date outfit worn front v015

- asset_id: OWNER_DATE_SUMMER_01_WORN_FRONT_v015
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- status: APPROVED
- approved_by: user
- approval_date: 2026-10-31
- evidence: “可以 批准，后面再用这套服装，就按照生成这张图的丝袜质感来生成”
- scope: current full-body outfit fitting as shown; specifically the HOSIERY APPEARANCE TARGET and material-generation recipe for every later use of OWNER_DATE_SUMMER_01
- current_approved_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v015.png
- current_approved_sha256: e9d59c10a5a269c5aeeab777bc19f65fc041d9dab54642c8a175b34cdc199b25
- original_candidate_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v015_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v015.png
- original_candidate_sha256: e9d59c10a5a269c5aeeab777bc19f65fc041d9dab54642c8a175b34cdc199b25
- promotion_operation: MOVED unchanged, not copied; candidate retains textual records only
- reference_rule: later use of this outfit matches v015 white hosiery color, translucency, textile sheen and visible leg/foot coverage; approved foot v002 supplies fine foot textile behavior and smooth ankle details when needed; original user L0 white source remains mandatory
- exclusions: no L1 Canon/identity/body/hair/skin authority, no permission to use generated face pixels as future face-generation input, no calf/pose/anatomy authority, no global change for other outfits, no video-keyframe approval

User approval is the final L2 review decision. Earlier agent QA concerns remain historical observations; they are not a continuing rejection or an automatic requirement to revise this approved image. Existing global reference isolation and face rules remain applicable.

- Future outfit hosiery method: `../../HOSIERY_APPEARANCE_METHOD_v015.md` relative to candidate directory. Original five inputs and exact submitted prompt remain immutable provenance; approval does not falsify the original preliminary QA.
