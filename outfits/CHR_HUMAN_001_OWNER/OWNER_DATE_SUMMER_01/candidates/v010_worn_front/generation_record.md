# Outfit Generation Record — v010 targeted material/leg corrections

- asset_id: OWNER_DATE_SUMMER_01_WORN_FRONT_v010
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- asset_purpose: worn_fit_validation
- view_type: worn_front
- head_policy: head_present_registered_face_recipe_user_scoped_override
- candidate_version: v010
- status: REVIEW_REQUIRED
- authorization: user 2026-10-31 accepted v009 likeness and requested four fixes (extra lower band; oil/water highlights; bowed calves; bare-looking toes without textile tension)
- generation_tool: built-in image_gen.imagegen
- generated_at: 2026-10-31
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v010_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v010.png
- output_sha256: 97cb20cbe6d1fc42ce3b32b47e692c003a73031dfc6e1c4d06df78ebf506c22d

## Validation target

Preserve user-accepted face method; remove only accidental lower white band, NOT true high waistband. Dry fine textile microtexture and diffuse fabric sheen, straight parallel knee-tibia-ankle axes, actual continuous closed-toe fabric envelope with readable intertoe tension.

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
      "responsibility": "neck-below natural torso/hip/limb mass and scale only; lower-leg axis explicitly controlled by current straight-leg text",
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

## Method and reference provenance

Same five authoritative physical files as v009; no v009 or failed candidate image supplied. This correction continues current explicitly selected registered B-crop + masked Hair-A recipe; B-derived crop is GENERATED-origin, not falsely represented as L0. Scope remains current outfit revision only; no global rule change or L1 promotion. Approved Face and user-accepted v009 likeness are QA-only. Registry OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1 / OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE / HOS_USER_SELECTED_WHITE_STRICT and nearest REFERENCE_GUIDE resolve original references. Exact source/crop provenance remains in v009 record and scoped reference folders.

User correction supersedes extra white lower band and bare-toe artifacts in design input and lower-leg bowing in any reference. Material photo defines textile properties, never leg anatomy. No new image copies in candidate inputs.

## Prompt/settings

Exact submitted prompt PROMPT.txt. Tool model/seed/quality/settings not exposed; defaults. Prefer 1536×2048 or nearest native exact 3:4, opaque. Reference budget five images, one material source, one candidate.

## Reference isolation

- previous_candidate_pixels_used: false
- previous_shot_pixels_used: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false
- lighting_or_background_taken_from_material_reference: false

## QA

- technical_status: FAIL_CALVES_AND_TOE_FABRIC
- fit_validation_status: UNREVIEWED
- face_contamination_check: REVIEW_REQUIRED
- face_generation_method_followed: registered B recipe, user-scoped continuation
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- decision: Pending one independent correction; no automatic approval/promotion.

## Output QA

Lower extra white band removed and oil/water-like highlights reduced, but calves still visibly bowed and toes remain bare-foot-like without clear fabric tension. v010 failed overall; cannot be downstream input.
