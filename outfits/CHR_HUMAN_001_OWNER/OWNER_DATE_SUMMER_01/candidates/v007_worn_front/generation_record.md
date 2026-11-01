# Outfit Generation Record

- asset_id: OWNER_DATE_SUMMER_01_WORN_FRONT_v007
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- asset_purpose: worn_fit_validation
- view_type: worn_front
- head_policy: head_present_owner_face_method_L0_only
- candidate_version: v007
- status: REVIEW_REQUIRED
- authorization: user 2026-10-31 “生成试穿图”
- generation_tool: built-in image_gen.imagegen
- generated_at: 2026-10-31
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v007_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v007.png
- output_sha256: da28c764dcec1cced19b1fb50075a743aca48404e1638d9827afd5a7c3809a81

## Validation target

Produce the requested front fitting with latest white hosiery, approved outfit construction and isolated owner sources. One candidate; preserve old approvals.

## Generation inputs / QA comparison only

```json
{
  "generation_inputs": [
    {
      "asset_id": "OWNER_DATE_SUMMER_01_SCOPED_INPUT_BOARD_Q95",
      "version": "v1 transport contact board",
      "path": "outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/reference_inputs/generation_board_v1/OWNER_DATE_SUMMER_01_SCOPED_INPUT_BOARD_Q95.jpg",
      "sha256": "34435257e271cdd81fb06ceb08c993e849d075e77853c2d3b064859b08c39105",
      "responsibility": "five isolated scoped panels; each component retains own authority, no averaging",
      "must_not_define": [
        "AI face generation from body/garment regions",
        "cross-panel identity/skin/material inheritance",
        "board layout",
        "gray padding",
        "compression artifacts",
        "scene lighting"
      ],
      "components": [
        {
          "asset_id": "OWNER_FACE_L0_013_GEOMETRY_012_SKIN_NATIVE_BOARD_001",
          "version": "v1 deterministic native montage",
          "path": "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_013_GEOMETRY_012_SKIN_NATIVE_BOARD_001.png",
          "sha256": "c2fccf2229c42206947edc41e9cacc04a0a702e9ca94f2a866b96f14d1f0ade0",
          "responsibility": "left L0 geometry only; upper-right L0 skin only",
          "must_not_define": [
            "AI identity",
            "panel borders or gray mask",
            "source hair/makeup/jewelry",
            "body",
            "outfit",
            "pose",
            "lighting",
            "background"
          ],
          "source_images": [
            {
              "asset_id": "OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001",
              "path": "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png",
              "sha256": "1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91",
              "operation": "paste at (0,0), native size; geometry only"
            },
            {
              "asset_id": "OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001",
              "path": "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png",
              "sha256": "89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd",
              "operation": "paste at (700,0), native size; skin only"
            }
          ],
          "paste_top_left": [
            0,
            0
          ]
        },
        {
          "asset_id": "OWNER_HAIRSTYLE_A_FACE_MASKED_001",
          "version": "v1",
          "path": "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png",
          "sha256": "6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd",
          "responsibility": "Hairstyle A only",
          "must_not_define": "not face/skin/body/clothes/light",
          "paste_top_left": [
            0,
            900
          ]
        },
        {
          "asset_id": "OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_TRANSPORT_Q95_v1",
          "version": "transport_v1 Q95 full-resolution",
          "path": "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/transport_v1/BODY_01_FRONT_FACE_EXCLUDED_TRANSPORT_Q95.jpg",
          "sha256": "4139759b58e20ff5a2dde3193afb1833f12103fb86a17f92c0e2ae16f74dab0e",
          "responsibility": "neck-below body proportions only",
          "must_not_define": "not face/skin/hair/garments/hosiery/light",
          "original_source_path": "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png",
          "original_source_sha256": "59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b",
          "transport_exclusion": "compression texture must not define hosiery material or fine detail",
          "paste_top_left": [
            930,
            0
          ]
        },
        {
          "asset_id": "OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v003_TRANSPORT_Q95",
          "version": "transport_v1 Q95 full-resolution",
          "path": "outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/reference_inputs/transport_v1/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v003_TRANSPORT_Q95.jpg",
          "sha256": "5fa3ece010b31cf6dd0acdba0f2a0b53b5ac0c5b82eec52969ac7e5fa74609df",
          "responsibility": "garment design only",
          "must_not_define": "not hosiery material/face/skin/body/hair",
          "original_source_path": "outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v003.png",
          "original_source_sha256": "2a88382b494f72cb4cd137d8525022e66fb36688ee37da6a8a28704a030d21ba",
          "transport_exclusion": "compression texture must not define hosiery material or fine detail",
          "paste_top_left": [
            2036,
            0
          ]
        },
        {
          "asset_id": "HOS_USER_WHITE_001_LOWER_LEG_FOOT_CROP_001",
          "version": "source_v1/crop_v1",
          "path": "materials/hosiery/reference_inputs/user_selected_white/PHOTO_1_LOWER_LEG_FOOT_MATERIAL_CROP.png",
          "sha256": "ce3b4fe1aafebe2818baae37dd3a76ca712820b1232d2ed15e06adf55002095d",
          "responsibility": "HOS_USER_SELECTED_WHITE_STRICT material-only appearance",
          "must_not_define": "not identity/anatomy/skin/nails/pose/shoes/background",
          "paste_top_left": [
            775,
            900
          ]
        }
      ]
    }
  ],
  "qa_comparison_only": [
    {
      "asset_id": "L0_HOS_USER_WHITE_001",
      "path": "materials/hosiery/source_library/raw/user_selected_white/PHOTO_1.jpg",
      "comparison_scope": "white material only"
    },
    {
      "asset_id": "OWNER_FACE_01_FRONT_NEUTRAL_CANON_001",
      "path": "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg",
      "comparison_scope": "identity drift, facial relationships, face contamination; comparison only"
    },
    {
      "asset_id": "OWNER_DATE_SUMMER_01_WORN_FRONT_v005",
      "path": "outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v005.png",
      "comparison_scope": "previous approved fit/likeness comparison only; never generation input"
    }
  ],
  "reference_budget": {
    "maximum_images": 1,
    "actual_images": 1,
    "logical_reference_panels": 5,
    "distinct_L0_face_sources": 2
  }
}
```

## Reference resolution and prompt assembly

Same original sources and scoped board as v006; reference registry HOS_USER_SELECTED_WHITE_STRICT plus nearest hosiery REFERENCE_GUIDE and board PROVENANCE.json. Face/skin derived only from the registered real L0 crops. AI Face and old worn v005 are QA-only. Body panel excludes face; cloth/material panels cannot define identity/skin/anatomy/hair. Historical generated B face recipe exception is not reused. Source paths/checksums and compression history remain in board provenance and nested input components.

Exact submitted concise prompt in PROMPT.txt; no new design choice, no candidate/failed-shot input. Reference budget: one board, five logically isolated panels, two L0 face sources. Target exact 3:4 opaque portrait; tool model/seed/quality/native output size not exposed.

## QA

- technical_status: FAIL_FACE_DRIFT_AND_MATERIAL
- fit_validation_status: UNREVIEWED
- face_contamination_check: REVIEW_REQUIRED
- face_generation_method_followed: L0-only sources and Face method prompt constraints
- previous_candidate_pixels_used: false
- previous_shot_pixels_used: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false
- lighting_or_background_taken_from_material_reference: false
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- decision: Generated, but QA rejects narrowed face/light smile and weak hosiery sheen. No approval or downstream use.

## Output

1086×1448 PNG. Tool original: /home/verdvana/.codex/generated_images/01a19227-4b9d-7881-83ba-993a94494e09/exec-f0c17b66-94d4-401e-945f-04b9ec5ff377.png. Copied unchanged into unique candidate path.
