# Outfit Generation Record — registered Face recipe and straight calves

- asset_id: OWNER_DATE_SUMMER_01_WORN_FRONT_v009
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- asset_purpose: worn_fit_validation
- view_type: worn_front
- head_policy: head_present_registered_face_recipe_user_scoped_override
- candidate_version: v009
- status: REVIEW_REQUIRED
- authorization: user 2026-10-31 “长相要参考女主现有正面资产的生成方式。白色丝袜质感要参考我上传的图片。小腿要笔直”
- generation_tool: built-in image_gen.imagegen
- generated_at: 2026-10-31
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v009_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v009.png
- output_sha256: d3bf868e742148c5a6f56fb8846759a74880c43acb5963edd58103a59cc3a740

## Method decision and scope

The current user explicitly directs the existing approved frontal asset's production method. Re-read FACE_01_FRONT_NEUTRAL_METHOD.md, original FACE_01 v011 generation/provenance and previously user-approved worn v005 recipe. The actual successful registered input is B_FACE_SKIN_CONTEXT_NO_CROWN from a generated scoped B appearance asset; it is NOT L0. This current explicit instruction is applied as a candidate-scoped override of the global L0-only face rule, exactly as recorded for v005 under the same user direction. Do not claim L0-only compliance or alter global AGENTS/Canon rules. No approved Face, AI Body face, prior worn/failed candidate or new L0 geometry/skin board is supplied as face input. Scope: this authorized fitting revision only; no general future exception and no L1 promotion.

## Validation target

Restore approved frontal likeness via original registered recipe; strictly match user white-hosiery material; natural straight knee-tibia-ankle axes without O/X leg drift. Preserve approved garments, high waistband and continuous closed toes.

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
      "asset_id": "OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1",
      "path": "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png",
      "version": "v7",
      "sha256": "59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b",
      "responsibility": "neck-below body proportions; text enforces straight lower legs",
      "must_not_define": [
        "face",
        "skin",
        "hair",
        "clothes",
        "hosiery",
        "light",
        "background"
      ]
    },
    {
      "asset_id": "OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v003",
      "path": "outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v003.png",
      "version": "approved v003",
      "sha256": "2a88382b494f72cb4cd137d8525022e66fb36688ee37da6a8a28704a030d21ba",
      "responsibility": "garment/sandal construction only",
      "must_not_define": [
        "face",
        "skin",
        "body",
        "hair",
        "hosiery material",
        "identity",
        "lighting",
        "background"
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
    }
  ],
  "reference_budget": {
    "maximum_images": 5,
    "actual_images": 5
  }
}
```

## Reference resolution and provenance

- Face/hair: registry OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1 and original Face method/v011 provenance; B crop is 900x1000+93+350 from OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001, generated origin honestly declared. Hair input is original masked L0 DSC00847.
- Body: registry OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE, original neck-below deterministic v7 crop.
- Clothing: approved design v003 per OUTFIT.md; only garment construction, not hosiery material. Unapproved design v005 not used.
- Material: HOS_USER_SELECTED_WHITE_STRICT and hosiery REFERENCE_GUIDE. Newly uploaded attachment SHA-256 matches existing unique raw source, 34ccb3f3923b441768f69f2f22ef95eb5bde3f31adf74af8172365bf503528df; no duplicate ingestion. New attachment path: /tmp/codex-remote-attachments/01a19227-4b9d-7881-83ba-993a94494e09/E875B8EA-F3A4-4D70-93ED-C8E614360223/1-照片-1.jpg.

## Prompt assembly / settings

PROMPT.txt is exact submitted prompt. Built-in defaults; seed/model/quality not exposed. Target 3:4 opaque portrait, one candidate only. Straight calves controlled by body proportion reference plus explicit balanced bilateral knee-tibia-ankle alignment text, not material photo anatomy.

## Reference isolation

- previous_candidate_pixels_used: false
- previous_shot_pixels_used: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false
- lighting_or_background_taken_from_material_reference: false
- input raster copies: none

## QA

- technical_status: PASS (native image and framing)
- fit_validation_status: REVIEW_REQUIRED
- face_contamination_check: PASS_INITIAL_VISUAL_CHECK; exact identity remains user review
- face_generation_method_followed: registered B-crop recipe under current explicit user scope; not L0-only
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- decision: Generated; registered recipe used and requested sheen/straight-leg constraints applied. User review required; no approval/promotion/overwrite.

## Output and initial QA

- Native dimensions: 1086 × 1448, exact 3:4.
- Unique repository file: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v009_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v009.png
- Tool original: /home/verdvana/.codex/generated_images/01a19227-4b9d-7881-83ba-993a94494e09/exec-f3ccd6e5-4c6c-4b81-a169-1ae196fba900.png
- Saved unchanged into project; no duplicate repository raster.
- Face appears closer to registered frontal reference than the rejected v007 L0-board attempt; neutral mouth and natural cheek/jaw proportions, no obvious blotches or muddy patches. Exact likeness is for user review.
- White textile now has clearer elongated calf/instep highlights and milky semi-sheer coverage consistent with selected photo; no obvious contrasting toe band or plastic coating. Fine toe/nail diffusion and fabric presence need user review at full resolution.
- Both legs face front with straight near-vertical knee/tibia/ankle alignment and stable bilateral sandal support; natural calf volume remains. Exact alignment and residual outward drift need user review, not asserted as measured perfection.
- Garments/high-waist structure retained. The lower abdominal edge near denim may still read as a secondary line and should be checked by user.
- Reviewed by Codex 2026-10-31; REVIEW_REQUIRED, no Canon or outfit approval inferred.

## User attribute-scoped review

User accepted likeness only (“长相OK了”), explicitly rejected lower band, wet/oil-like hosiery response, bowed calves and bare-looking toes. Overall QA FAIL_USER_REVIEW, no promotion. New correction v010 uses original inputs, v009 pixels QA-only.
