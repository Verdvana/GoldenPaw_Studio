# Outfit Generation Record

- asset_id: `OWNER_WORK_WINTER_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_WORK_WINTER_01`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- head_policy: `not_applicable`
- candidate_version: `v002`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen edit`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/candidates/v002_design_reference/OWNER_WORK_WINTER_01_DESIGN_REFERENCE_v002.png`
- output_sha256: `4b397716f1fab39d84d367bc2ea25e0cfd90e561837105ab41ae45dee1972b78`
- reference_budget: `one edit target; previous v001 used only as edit target`

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_WORK_WINTER_01_DESIGN_REFERENCE_v001
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/candidates/v001_design_reference/OWNER_WORK_WINTER_01_DESIGN_REFERENCE_v001.png
    responsibility:
      - preserve existing clothing-only composition
      - preserve coat, skirt, scarf, and overall product-board layout
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
- previous_candidate_pixels_used: `true` — edit target only, not identity lineage
- previous_shot_pixels_used: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

```text
Use case: precise-object-edit
Asset type: clothing-only L2 winter officewear design reference.
Input images: Image 1 is the existing clothing-only design board and edit target.
Primary request: Change only two design details while preserving the existing composition and all other garments. Replace the hosiery swatch with light-skin 60D pearl-effect hosiery: slightly transparent so the underlying light-skin tone is subtly readable, with delicate fine crystalline pearlescent sparkle distributed softly across the textile. The sparkle must look like woven pearlescent fibers under soft light, never wet, oily, glossy, plastic, latex, PVC, rubber, or liquid. Raise the brown felt straight-shaft boots so the shaft ends just below the knee, clearly not ankle-height or mid-calf, while keeping the approximately 5 cm wedge heel, brown felt material, closed toe, and straight shaft.
Constraints: preserve the light-gray oversized-lapel short coat, dark-gray wool short skirt, brown scarf, neutral gray background, no-person clothing-only presentation, product-board layout, scale, and lighting. No body, mannequin, head, face, hands, or upper-body image.
Avoid: oil-shine hosiery, mirror gloss, wet highlights, plastic coating, opaque tights, bare toes, toe-cap line, discontinuity, boots that are too low, knee-over or thigh-high boots, stiletto or block heel, heel above 5 cm, logos, labels, readable text, watermark.
```

## QA

- technical_status: `UNREVIEWED`
- visual_status: `PASS_WITH_USER_REVIEW`
- garment_reference_isolation_check: `PASS`
- face_contamination_check: `NOT_APPLICABLE`
- hosiery_material_check: `REVIEW_REQUIRED`
- footwear_height_and_heel_check: `REVIEW_REQUIRED`
- decision: `PENDING_USER_REVIEW`

## Promotion provenance

- user_approval_statement: `批准，生成上身图`
- approved_at: `2026-09-17`
- approved_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_WINTER_01/approved/design_reference/OWNER_WORK_WINTER_01_DESIGN_REFERENCE_APPROVED.png`
- promotion_operation: `moved; no raster copy retained at candidate path`
