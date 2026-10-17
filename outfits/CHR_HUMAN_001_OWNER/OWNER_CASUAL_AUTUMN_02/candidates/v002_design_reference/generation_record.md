# Generation Record — OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v002

- asset_id: `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v002`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- head_policy: `not_applicable`
- candidate_version: `v002`
- status: `REJECTED`
- generation_tool: built-in ImageGen
- generated_at: `2026-10-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v002_design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v002.png`
- output_sha256: `47b449da4f5454e55d0377cb568992ee58150935937f611c8996c50713a6534a`

## Validation target

- fit_or_design_question: Does a flat-lay, clothing-only presentation show the requested autumn outfit and the continuous white hosiery beneath open-toe fuzzy slippers without any human or mannequin form?
- acceptance_checks:
  - Cream-oatmeal crew-neck knit cardigan with small matte wood-look buttons and a plain warm-ivory tee.
  - Deep chocolate-brown simple wool-blend A-line mini skirt.
  - Thick opaque matte white pantyhose with continuous fabric over feet and toes.
  - Light tan-brown fuzzy open-toe mule slippers; fabric-covered toes remain visible.
  - Flat-lay arrangement only, with no mannequin, body, limbs, person, face, or human-shaped support.
  - No logos, readable labels, text, watermark, plastic shine, bare toes, or hosiery discontinuity.

## Generation inputs

Text-only generation from the user brief and this outfit contract. The rejected v001 image is not an input.

```yaml
generation_inputs: []
```

## QA comparison only

No comparison images used.

```yaml
qa_comparison_only: []
```

## Reference isolation

- garment_references_used: none
- reference_budget: `0 image references`
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

Photorealistic clothing-only L2 apparel design reference, portrait 3:4. Strict flat-lay
product photography on a seamless light-gray studio background, soft even neutral
lighting. Show one coordinated autumn casual outfit arranged flat on the surface with
no person, mannequin, ghost mannequin, body, limb, foot-shaped form, or human-shaped
support anywhere. Arrange: a cream-oatmeal long-sleeve crew-neck knit cardigan, gently
relaxed and waist length, narrow ribbed cuffs and hem, small matte wood-look buttons;
a plain warm-ivory crew-neck cotton tee partly tucked beneath the cardigan; a deep
chocolate-brown substantial wool-blend A-line mini skirt with a clean simple hem; one
pair of thick opaque matte white pantyhose laid flat and fully extended from waistband
to covered toes; one pair of light tan-brown plush fuzzy open-toe mule slippers placed
beside the hosiery feet, with the open toe openings clearly visible. The tights must
remain a single continuous textile garment over feet and toes; show the covered toe
sections naturally adjacent to the open slipper fronts without creating a body or
foot silhouette. Warm, cozy, wearable colors and realistic textile surfaces. No logos,
labels, text, watermark, extra accessories, naked toes, sheer hosiery, latex, PVC,
rubber, plastic gloss, wet highlights, or body paint.

## QA

- technical_status: `PASS`
- fit_validation_status: `FAIL`
- face_contamination_check: `NOT_APPLICABLE`
- face_generation_method_followed: `not_applicable`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `REJECTED — despite the flat-lay setting, the pantyhose is presented as a complete leg-shaped form, violating the no-body/no-human-shape design contract.`
- reviewer: `Codex`
- reviewed_at: `2026-10-17`
