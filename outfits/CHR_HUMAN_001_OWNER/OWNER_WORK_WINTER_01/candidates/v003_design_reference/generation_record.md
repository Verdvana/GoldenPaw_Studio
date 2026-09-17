# Outfit Generation Record

- asset_id: `OWNER_WORK_WINTER_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_WORK_WINTER_01`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- head_policy: `not_applicable`
- candidate_version: `v003`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen edit`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/candidates/v003_design_reference/OWNER_WORK_WINTER_01_DESIGN_REFERENCE_v003.png`
- output_sha256: `9b7734cf5e6fb907c5a02e037b7cee470a6e7ed9cd0d943551e4d201899e9d63`
- reference_budget: `one approved design image used only as edit target`

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/approved/design_reference/OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED.png
    responsibility:
      - preserve clothing-only composition
      - preserve approved skirt, scarf, pearl hosiery, neutral board and general styling
    must_not_define:
      - owner identity
      - face
      - body or skin
      - hair
      - pose
```

## QA comparison only

```yaml
qa_comparison_only: []
```

## Reference isolation

- garment_references_used: none
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

```text
Use case: precise-object-edit
Asset type: clothing-only L2 winter officewear design reference.
Input images: Image 1 is the approved clothing-only design board and edit target.
Primary request: Change only the coat and boots while preserving the composition and all other items. Make the brown boots a deeper black-brown, near espresso brown with a subtle black cast. Keep them as straight-shaft boots with parallel sides from the opening down through the ankle; do not cinch, taper, gather, or narrow the shaft at the ankle. Preserve the below-knee height and approximately 5 cm wedge heel. Simplify the light-gray wool short coat: remove the two large front buttons entirely and use a clean minimal front closure with no prominent hardware. Make the coat gray slightly deeper than before, but clearly lighter than the dark-gray skirt.
Constraints: preserve the brown scarf, dark-gray skirt, light-skin 60D subtle pearl-effect hosiery swatch, neutral gray clothing-only board, product-photography lighting, layout and scale. No person, mannequin, head, face, body, hands, feet, or upper-body image.
Avoid: two large buttons, oversized visible hardware, double-breasted button layout, coat darker than skirt, black coat, light-brown boots, ankle-tapered boots, gathered shaft, slouch shaft, ankle boots, knee-over or thigh-high boots, stiletto or block heel, heel over 5 cm, oil-shine hosiery, latex/PVC/plastic/rubber, logos, labels, readable text, watermark.
```

## QA

- technical_status: `UNREVIEWED`
- visual_status: `PASS_WITH_USER_REVIEW`
- garment_reference_isolation_check: `PASS`
- face_contamination_check: `NOT_APPLICABLE`
- upper_body_absence_check: `REVIEW_REQUIRED`
- coat_button_and_gray_tone_check: `REVIEW_REQUIRED`
- boot_color_and_straight_shaft_check: `REVIEW_REQUIRED`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `PENDING_USER_REVIEW`

## Promotion provenance

- user_approval_statement: `批准，下一项上身图的时候注意丝袜要厚些，要有明显的珠光，而不是油亮丝袜的线性高光`
- approved_at: `2026-09-17`
- approved_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/approved/design_reference/OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED.png`
- promotion_operation: `moved; prior approved raster retained under design_reference_v002 history path`
