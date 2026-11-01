# Outfit Generation Record

- asset_id: OWNER_DATE_SUMMER_01_WORN_FRONT_v006
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- asset_purpose: worn_fit_validation
- view_type: worn_front
- head_policy: head_present_owner_face_method_L0_only
- candidate_version: v006
- status: DRAFT
- authorization: user 2026-10-31 “那么修改一下夏季约会套装资产的两张图片吧，参考最新的白色丝袜质感”
- generation_tool: built-in image_gen.imagegen
- generated_at: not generated (service connection failure)
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v006_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v006.png
- output_sha256: null (no output)

## Validation target

Latest required white hosiery appearance in both design and front fitting; preserve approved garment design, waist layering and shoe design. One independent candidate per requested deliverable; no bulk variants.

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

Exact submitted prompt in PROMPT.txt. Seed/model/quality/native resolution not exposed; built-in defaults. White crop version source_v1/crop_v1. Target aspect ratio 3:4 portrait, opaque background. One candidate only.

## QA

- technical_status: GENERATION_FAILED_CONNECTION
- fit_validation_status: UNREVIEWED
- face_contamination_check: REVIEW_REQUIRED
- face_generation_method_followed: L0-only source-derived method constraints
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- decision: No output due to service connection failure; no approval or replacement.

## Tool input-limit preflight

First attempted call was rejected before generation: referenced_image_paths must contain at most 5 paths. No image returned and no moderation issue. Face/skin derivatives combined into one deterministic native board with provenance, preserving separate panel responsibilities; actual generation inputs now five images.

- Five-input attempt returned connection failed / error sending request; no image returned. Same-input network retry authorized by the active task.

## Service failure

Three five-input requests returned `connection failed: error sending request`, with no image. This is a tool/network failure, not a content moderation rejection. Output absent; generation incomplete. No further unchanged retries planned.

- Final outcome this turn: connection error, no image returned. Exact prompt retained for later authorized continuation. Built-in tool unavailable for completion; no CLI fallback invoked.

## Explicit retry authorization — 2026-10-31

User: “重试”. Retry the same saved prompt and scoped inputs, one candidate per requested deliverable; output path unchanged because no previous output exists for this candidate. Status: DRAFT / RETRY_IN_PROGRESS. Prior service failures remain historical. Seed/settings: built-in defaults, not exposed.

## Retry payload adjustment

This turn: two-input design succeeded but same five-PNG worn request failed with connection error. Payload size is a hypothesis, not an established cause. Deterministic full-resolution JPEG Q95 4:4:4 transport derivatives replace only large body/garment PNG inputs; originals unchanged. Actual paths/checksums updated above before retry. Face and material inputs remain unchanged. Prompt remains unchanged; seed/settings not exposed. Prior PNG input paths/checksums remain in original_source fields.

## Single-board transport retry

Compact five-file retry still returned connection failure, so file size is not confirmed as cause. Transport the same five scoped inputs on one native-size board; no change in semantic authorities. Gray layout has no output authority. Original five-input record and prompt preserved as RETRY_FIVE_INPUTS.json / PROMPT_FIVE_INPUTS.txt; updated exact one-board prompt in PROMPT.txt. This is a transport experiment, not CLI fallback or new design variant.

## Latest explicit retry result

- User retry: design succeeded separately, worn image remains absent.
- This turn worn attempts: original five PNG references -> connection failed; five smaller transport references -> connection failed; one scoped contact board -> connection failed.
- All failures returned `image generation failed: connection failed: error sending request`. No returned image or content-moderation rejection. Cause unresolved; file size and number of inputs were hypotheses only.
- Current exact prompt: PROMPT.txt (one-board input). Prior five-input prompt/record: PROMPT_FIVE_INPUTS.txt and RETRY_FIVE_INPUTS.json. Source/transport provenance retained.
- output_path remains reserved; output does not exist. Seed/model/settings not exposed.
- status: DRAFT / GENERATION_FAILED_CONNECTION. No face or material QA possible, no promotion or replacement.
- Built-in-only workflow used. CLI/API fallback exists and requires OPENAI_API_KEY and explicit user selection; not invoked.
