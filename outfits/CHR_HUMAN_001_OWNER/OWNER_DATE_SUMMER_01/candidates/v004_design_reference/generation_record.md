# Outfit Generation Record

- asset_id: OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v004
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- asset_purpose: design_reference
- view_type: design_reference
- head_policy: not_applicable
- candidate_version: v004
- status: REVIEW_REQUIRED
- authorization: user 2026-10-31 “那么修改一下夏季约会套装资产的两张图片吧，参考最新的白色丝袜质感”
- generation_tool: built-in image_gen.imagegen
- generated_at: 2026-10-31
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v004_design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v004.png
- output_sha256: e0ebad3bbfef07190b3c554e48598e6822a8e28d2a7e26e4bee08d6b485309b8

## Validation target

Latest required white hosiery appearance in both design and front fitting; preserve approved garment design, waist layering and shoe design. One independent candidate per requested deliverable; no bulk variants.

## Generation inputs / QA comparison only

```json
{
  "generation_inputs": [
    {
      "asset_id": "OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v003",
      "version": "v003 approved",
      "path": "outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v003.png",
      "sha256": "2a88382b494f72cb4cd137d8525022e66fb36688ee37da6a8a28704a030d21ba",
      "responsibility": "garment geometry, layout and product lighting",
      "must_not_define": "not hosiery appearance or identity"
    },
    {
      "asset_id": "HOS_USER_WHITE_001_LOWER_LEG_FOOT_CROP_001",
      "version": "source_v1/crop_v1",
      "path": "materials/hosiery/reference_inputs/user_selected_white/PHOTO_1_LOWER_LEG_FOOT_MATERIAL_CROP.png",
      "sha256": "ce3b4fe1aafebe2818baae37dd3a76ca712820b1232d2ed15e06adf55002095d",
      "responsibility": "HOS_USER_SELECTED_WHITE_STRICT material-only appearance",
      "must_not_define": "not identity/anatomy/skin/pose/shoes/background"
    }
  ],
  "qa_comparison_only": [
    {
      "asset_id": "L0_HOS_USER_WHITE_001",
      "path": "materials/hosiery/source_library/raw/user_selected_white/PHOTO_1.jpg",
      "comparison_scope": "white material only"
    }
  ],
  "reference_budget": {
    "maximum_images": 2,
    "actual_images": 2
  }
}
```

## Reference resolution and isolation

Registry HOS_USER_SELECTED_WHITE_STRICT plus the material REFERENCE_GUIDE resolve the single material crop. Outfit OUTFIT.md resolves clothing-only design v003. Worn input set also resolves OWNER_L0_FACE_013_GEOMETRY_CROP_V1, OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1, OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE and OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE. Existing derivative provenance is retained even though original L0 photos 14.jpg/15.jpg are currently absent from the worktree; no originals restored or fabricated.

- previous_candidate_pixels_used: false (approved clothing-only design is scoped garment input)
- previous_shot_pixels_used: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false
- lighting_or_background_taken_from_material_reference: false
- AI Face/AI Body/generated candidate used as face input: false
- The historical v005 B-derived face recipe was a one-candidate user exception; this request does not extend it. Use real L0-derived face/skin crops with FACE_01 method facial relationships, skin, Hair-A and projection constraints. Approved Face/v005 pixels are QA-only.
- Input physical copies: none; records refer to single authoritative files.

## Prompt assembly and settings

Exact submitted prompt in PROMPT.txt. Seed/model/quality/native resolution not exposed; built-in defaults. White crop version source_v1/crop_v1. Target aspect ratio source 2:3 portrait, opaque background. One candidate only.

## QA

- technical_status: FAIL_PRODUCT_ARTIFACTS
- fit_validation_status: UNREVIEWED
- face_contamination_check: NOT_APPLICABLE
- face_generation_method_followed: not_applicable
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- decision: Generated; material sheen improved but product QA failed on ghost navel and toe band. No approval or replacement.

## Actual output

- dimensions: 1024 × 1536
- unique repository raster: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v004_design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v004.png
- tool original: /home/verdvana/.codex/generated_images/01a19227-4b9d-7881-83ba-993a94494e09/exec-e63243b6-9eb9-4826-8036-e4412637a69c.png
- copy unchanged into workspace; default tool output kept per tool policy. No second repository raster.
