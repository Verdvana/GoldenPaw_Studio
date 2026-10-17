# Generation Record — OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v001

- asset_id: `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v001`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- head_policy: `not_applicable`
- candidate_version: `v001`
- status: `REJECTED`
- generation_tool: built-in ImageGen
- generated_at: `2026-10-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v001_design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v001.png`
- output_sha256: `43288c17f88b389d4b6615bdbe3d8ee639fcdca764d67cda8e3899de97eb5dfe`

## Validation target

- fit_or_design_question: Do the five garments read as one cozy autumn casual outfit, with the requested colors and a clear hosiery-to-open-toe-slipper relationship?
- acceptance_checks:
  - Cream-oatmeal crew-neck knit cardigan with small matte wood-look buttons and a plain warm-ivory tee.
  - Deep chocolate-brown simple wool-blend A-line mini skirt.
  - Thick opaque matte white pantyhose with continuous fabric over feet and toes.
  - Light tan-brown fuzzy open-toe mule slippers; toes remain covered by the white hosiery.
  - Clothing-only presentation, no person, face, mannequin, body, logos, text, or watermark.
  - No latex, plastic, wet gloss, bare toes, or hosiery discontinuity.

## Generation inputs

Text-only generation from the approved user brief and this outfit contract; no image references supplied.

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

Create one photorealistic, clothing-only L2 outfit design reference, portrait 3:4,
on a seamless neutral light-gray studio background with soft even lighting. Arrange a
complete cozy autumn outfit as a neat apparel presentation, with no person, mannequin,
head, face, hands, body, or human-shaped form: a cream-oatmeal gently relaxed
crew-neck cardigan with long sleeves, waist-length hem, narrow ribbed cuffs and hem,
and small matte wood-look buttons; a plain warm-ivory crew-neck cotton tee as a subtle
underlayer; a deep chocolate-brown substantial wool-blend A-line mini skirt with a
simple clean hem; thick opaque matte white pantyhose shown continuously from waistband
through both covered feet and toes; and a pair of light tan-brown plush fuzzy open-toe
mule slippers. Make the fabric-covered white toes clearly visible through the open
slipper fronts so the hose continuity is unambiguous. Keep the palette warm, the
garments realistic and wearable, and surfaces textile-like. No logos, labels, text,
watermarks, extra garments, bare skin at the toes, sheer hosiery, exposed anatomy,
plastic shine, latex, or body paint.

## QA

- technical_status: `PASS`
- fit_validation_status: `FAIL`
- face_contamination_check: `NOT_APPLICABLE`
- face_generation_method_followed: `not_applicable`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `REJECTED — image uses a leg-shaped ghost mannequin, conflicting with the clothing-only/no-body design brief.`
- reviewer: `Codex`
- reviewed_at: `2026-10-17`
