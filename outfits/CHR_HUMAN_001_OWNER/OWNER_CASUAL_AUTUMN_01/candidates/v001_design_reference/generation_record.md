# Outfit Generation Record

- asset_id: `OWNER_CASUAL_AUTUMN_01_DESIGN_REFERENCE_v001`
- outfit_id: `OWNER_CASUAL_AUTUMN_01`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `clothing_only_flat_lay_design_plate`
- candidate_version: `v001`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-19`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01/candidates/v001_design_reference/OWNER_CASUAL_AUTUMN_01_DESIGN_REFERENCE_v001.png`
- output_sha256: `c8f7ed6a8191f966271882ba8bbeed719b70731c34c79e265ade480543022270`
- reference_budget: `4 garment-only references; no character, Canon, or previous-candidate image`

## Generation inputs

```yaml
generation_inputs:
  - asset_id: GARMENT_REF_IMG_2812
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01/reference_inputs/garment_references/IMG_2812.jpg
    responsibility: [black layered ruffle mini skirt, lace trim, silhouette]
    must_not_define: [person, body, legs, identity, lighting, background]
  - asset_id: GARMENT_REF_IMG_2814
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01/reference_inputs/garment_references/IMG_2814.jpg
    responsibility: [white lace-yoke high-neck long-sleeve top, fabric and trim]
    must_not_define: [person, face, body, hands, identity, lighting, background]
  - asset_id: GARMENT_REF_IMG_2816
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01/reference_inputs/garment_references/IMG_2816.JPG
    responsibility: [gunmetal-silver Mary Jane flats, black toe cap and strap, low heel]
    must_not_define: [person, feet, legs, identity, lighting, background]
  - asset_id: GARMENT_REF_IMG_2819
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01/reference_inputs/garment_references/IMG_2819.JPG
    responsibility: [silver-gray subtly sparkling sheer pantyhose material, continuous waist-to-toe garment]
    must_not_define: [person, body, skin, feet, shoe pairing, identity, lighting, background]
```

## QA comparison only

```yaml
qa_comparison_only: []
```

## Reference isolation

- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- character_or_canon_inputs_used: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

```text
Use case: product-mockup
Asset type: L2 clothing-only autumn casual outfit design reference.
Input images: Images 1–4 are garment-only references. Use each solely for its stated clothing, hosiery, and footwear properties.
Primary request: Create a clean, coherent clothing-only fashion flat-lay / ghost-form design plate for one autumn casual outfit: white fitted long-sleeve top with high ruffled collar and delicate floral lace yoke; black elastic-waist layered ruffle mini skirt with black lace trim; silver-gray subtly sparkling sheer pantyhose shown as a continuous waist-to-toe textile garment; paired gunmetal-silver Mary Jane flats with glossy black toe caps, a narrow black strap with a small round button, and very low block heels.
Scene/backdrop: neutral warm-light-gray seamless studio board.
Style/medium: high-end e-commerce product photography; accurate textiles and true-to-reference construction.
Composition/framing: portrait 3:4, centered balanced flat lay / invisible ghost form, top and skirt arranged as a complete look, a hosiery material/garment presentation, and the pair of shoes below; no labels.
Lighting/mood: soft even studio light, minimal shadow.
Materials/textures: opaque knit and fine floral lace, matte black layered ruffles and lace edging, silver-gray non-oily hosiery with restrained micro-sparkle, gunmetal glitter textile shoes with black patent toe caps.
Constraints: clothing only; retain four reference items' defining construction and colors; pantyhose must read as one continuous textile garment from waist/hips to toes.
Avoid: person, model, mannequin, head, face, torso, skin, hands, legs, feet, body form, hair, jewelry, bag, denim, belt, text, logo, watermark; stockings separated from a waistband; bare toes; latex/PVC/plastic/rubber/liquid/body-paint hosiery; oily or hard linear shine.
```

## QA

- technical_status: `PASS` — PNG, 1086 × 1448 px, checksum recorded
- visual_status: `PASS_WITH_USER_REVIEW`
- garment_reference_isolation_check: `PASS` — only four garment-only source images were supplied
- face_contamination_check: `NOT_APPLICABLE`
- human_or_mannequin_absence_check: `PASS` — no person, face, body, skin, hands, feet, or mannequin is depicted
- top_construction_check: `PASS_WITH_USER_REVIEW` — white rib-knit long sleeves, ruffled high collar and floral lace yoke are present
- skirt_construction_check: `PASS_WITH_USER_REVIEW` — black elastic waist, tiered ruffles and lace trim are present
- footwear_check: `PASS_WITH_USER_REVIEW` — gunmetal-silver Mary Jane flats have black glossy toe caps, narrow straps and low heels
- hosiery_continuity_and_material_check: `PASS_WITH_USER_REVIEW` — one waist-to-toe pantyhose garment; silver-gray micro-sparkle is non-oily and no bare toes appear
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `PENDING_USER_REVIEW`
