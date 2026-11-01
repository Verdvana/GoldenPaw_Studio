# Outfit Material Detail Generation Record

- asset_id: OWNER_DATE_SUMMER_01_FOOT_MATERIAL_DETAIL_v001
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- asset_purpose: material_detail
- view_type: material_detail
- head_policy: not_applicable
- candidate_version: v001
- status: REVIEW_REQUIRED
- authorization: ongoing explicit foot-material redo request; OUTFIT.md Asset package gate permits additional material/structure detail only when specific unresolved issues exist, which repeated foot-coverage failures establish
- generation_tool: built-in image_gen.imagegen
- generated_at: 2026-10-31
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v001_foot_material_detail/OWNER_DATE_SUMMER_01_FOOT_MATERIAL_DETAIL_v001.png
- output_sha256: d57b837a1171a509e4820fa33671e2c0cf7fa8d52e72d4de2621036cc0fc403a

## Validation target

Directly assess textile envelope over toe row/nails, shallow intertoe V tension bridges, continuity and ankle microfolds without silicone finish. User white source remains sole color/transparency/finish authority. This diagnostic is NOT a substitute for corrected full-body fitting and will NOT feed downstream generation before user review.

## Generation inputs / QA comparison only

```json
{
  "generation_inputs": [
    {
      "asset_id": "HOS_USER_WHITE_001_LOWER_BODY_LEG_FOOT_CROP_002",
      "path": "materials/hosiery/reference_inputs/user_selected_white/PHOTO_1_LOWER_BODY_LEG_FOOT_MATERIAL_CROP_v2.png",
      "version": "source_v1/crop_v2",
      "responsibility": "sole white color, transparency, silk-fiber finish and overall textile appearance",
      "must_not_define": [
        "identity",
        "anatomy",
        "pose",
        "skin",
        "shoes",
        "lighting",
        "car",
        "background",
        "denier"
      ],
      "sha256": "f0aeb037eba8b1a17075c85fcf3baf11329643cf01023ac8e3b38f04a1635c5b"
    },
    {
      "asset_id": "HOS_15D_NM_011_FEET_TOE_COVERAGE_CROP_002",
      "path": "materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_FEET_TOE_TEXTILE_COVERAGE_ONLY_CROP_v1.png",
      "version": "v1",
      "responsibility": "whole-toe fabric veil/enclosure, intertoe fabric tension and softened nail edges ONLY",
      "must_not_define": [
        "color",
        "finish",
        "opacity",
        "denier",
        "nail color",
        "skin",
        "anatomy",
        "pose",
        "background"
      ],
      "sha256": "4ac17d6b3a619a4a4fd0cf262c2a2fdd8a9d9c1e838c4701991cbcee782a7a4a"
    }
  ],
  "qa_comparison_only": [
    {
      "asset_id": "L0_HOS_USER_WHITE_001",
      "path": "materials/hosiery/source_library/raw/user_selected_white/PHOTO_1.jpg",
      "comparison_scope": "white textile appearance only"
    }
  ],
  "reference_budget": {
    "maximum_images": 2,
    "actual_images": 2,
    "reason": "white overall material source plus missing toe-coverage evidence"
  }
}
```

## Provenance/isolation and settings

Resolve from HOS_USER_SELECTED_WHITE_STRICT_WIDE_CROP_V2 and HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001 derivatives; named source guides and provenance sidecars declare narrow scopes. No prior candidate/shot/Face/Body pixels; anatomy, shoes and pose text only. No face visible. Original crop sources unchanged and no local input copies. PROMPT.txt is exact submitted text; model/seed/quality/native resolution not exposed, defaults; opaque. Two refs/two separate material responsibilities.

## QA

- technical_status: PASS_INITIAL_DETAIL_QA
- fit_validation_status: REVIEW_REQUIRED
- face_contamination_check: NOT_APPLICABLE
- previous_candidate_pixels_used: false
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- downstream_generation_allowed: false_until_user_review
- decision: One diagnostic candidate permitted by unresolved material-detail gate, not approved Canon or downstream input.

## Actual output

- dimensions: 1312×1199
- tool output: /home/verdvana/.codex/generated_images/01a19227-4b9d-7881-83ba-993a94494e09/exec-d63bfea4-f3b8-42e2-960e-00e7c000de87.png
- copied unchanged into unique project candidate; SHA-256 above
- result: Close-up clearly resolves fine continuous textile over nails/toe tops, shallow fabric-covered interdigital valleys, softened burgundy nails and subtle ankle flexion wrinkles. No obvious smooth silicone shell. White color/sheen/opacity and precise anatomical realism remain user review; not approved downstream input.
- No user approval, promotion or replacement. No downstream use.

## User attribute-scoped review

User: “除了脚腕处不该有褶皱，别的OK”. Other detail properties accepted; ankle wrinkles rejected. See USER_REVIEW_SCOPED.md. Overall correction pending; no L1 promotion.
