# Outfit Generation Record

- asset_id: OWNER_WORK_AUTUMN_01_DESIGN_REFERENCE_v002
- outfit_id: OWNER_WORK_AUTUMN_01
- asset_level: L2
- asset_purpose: design_reference
- view_type: design_reference
- head_policy: not_applicable
- candidate_version: v002
- status: REVIEW_REQUIRED
- generation_tool: built-in ImageGen
- generated_at: 2026-09-20
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_AUTUMN_01/candidates/v002_design_reference/OWNER_WORK_AUTUMN_01_DESIGN_REFERENCE_v002.png
- output_sha256: ec4d7a2e72f4cd06f21f4c7bb2bd3c9cc72434440ba57b314f3f08c839e823f2

## Validation target

- fit_or_design_question: Does one clean, task-free clothing asset clearly communicate the updated autumn officewear package?
- acceptance_checks:
  - no human identity, face, hair, hands, or recognizable body is depicted
  - pale blush-pink blazer, cool-gray inner top, and warm gray-taupe wide-leg trousers are legible
  - black pointed-toe slingback pump follows REF_001 construction without red outsole or branding
  - light-skin sheer pantyhose is continuous from waist through ankles and closed toes, with soft textile response rather than plastic/latex
  - neutral studio garment-board presentation, no text, watermark, logo, phone, bag, or background copied from references

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_WORK_AUTUMN_01_REF_002
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_AUTUMN_01/reference_inputs/garment_references/IMG_0002_USER_AUTUMN_WORKWEAR.jpg
    responsibility:
      - blazer silhouette and pale blush-pink color
      - gray inner top and layering
      - warm gray-taupe wide-leg trousers
      - garment drape and officewear palette
    must_not_define:
      - model identity, face, body, skin, hair, pose, hosiery, shoes, lighting, background, photography style
  - asset_id: OWNER_WORK_AUTUMN_01_REF_001
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_AUTUMN_01/reference_inputs/garment_references/IMG_2779.jpg
    responsibility:
      - black pointed-toe slingback pump silhouette
      - rear strap and buckle construction
      - slender high heel proportion
    must_not_define:
      - model identity, face, body, skin, hair, pose, red outsole, branding, lighting, background, photography style
  - asset_id: L0_HOS_15_NM_011
    path: materials/hosiery/source_library/raw/15d_nude_matte/1.jpg
    responsibility:
      - light-skin 15D sheer matte textile response and continuous leg-to-foot coverage
    must_not_define:
      - identity, anatomy, pose, clothing, shoes, background, lighting
```

## QA comparison only

```yaml
qa_comparison_only: []
```

## Reference isolation

- reference_budget: 3 images
- previous_candidate_pixels_used: false
- previous_shot_pixels_used: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false
- lighting_or_background_taken_from_garment_reference: false

## Prompt assembly

- use case: product-mockup
- asset type: reusable L2 autumn officewear design reference
- scene/backdrop: neutral seamless studio garment board
- subject: front-facing ghost-mannequin clothing presentation only, with no visible person or body
- construction: pale blush-pink blazer with open front and softly rolled sleeves; cool-gray satin-like sleeveless inner top; high-waisted warm gray-taupe wide-leg tailored trousers
- hosiery: continuous light-skin 15D sheer matte/velvet-matte pantyhose under the trousers and through closed toes
- footwear: black pointed-toe slingback pump with rear strap and buckle, slender heel, no red outsole or branding
- constraints: use REF_002 only for garments; use REF_001 only for shoe construction; no identity lineage; no copied text, watermark, phone, bag, pose, background, or lighting
- avoid: white sweater, black hosiery, red sole, open toes, toe-cap seam, latex/PVC/plastic shine, naked ankles/toes, mannequin face, person, logo, text, watermark
