# Generation Record — OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v004

- asset_id: `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v004`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- head_policy: `not_applicable`
- candidate_version: `v004`
- status: `SUPERSEDED`
- generation_tool: built-in ImageGen edit
- generated_at: `2026-10-17`
- original_candidate_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v004_design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v004.png`
- historical_candidate_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v004_design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v004.png`
- output_sha256: `586fd1a26d5bfad1824187e682124c9251183e776dfe46f707301a7efba1784d`

## Validation target

- fit_or_design_question: Do the thinner, slightly sheer pantyhose and lighter skirt/slippers match the user's requested color/material adjustment while preserving the existing outfit layout?
- acceptance_checks:
  - Pantyhose is a thin, subtly sheer textile with slight natural skin tone visible through the fabric, while remaining continuous over the entire garment and feet.
  - No bare toes, hosiery gaps, abrupt opacity changes, oily shine, latex, plastic, or body paint.
  - Skirt is a lighter warm medium brown than the previous deep chocolate brown.
  - Slippers are lighter beige/tan brown than the previous version.
  - Cardigan, ivory tee, flat-lay composition, neutral background, and no-human-form presentation remain unchanged.

## Generation inputs

The existing clothing-only design reference is used only as the visual base for the requested garment-color/material edit. It defines the flat-lay composition and unchanged garments, not owner identity or body.

```yaml
generation_inputs:
  - asset_id: OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v003
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v003_design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v003.png
    responsibility:
      - preserve cardigan and tee design
      - preserve flat-lay layout and lighting
      - guide localized skirt and slipper color edits
      - guide pantyhose material edit
    must_not_define:
      - owner face
      - owner body or proportions
      - owner skin or identity
      - any human or mannequin form
```

## QA comparison only

```yaml
qa_comparison_only: []
```

## Reference isolation

- garment_references_used: `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v003` as an edit base only
- reference_budget: `1 image reference`
- previous_candidate_pixels_used: `true — edit base only; not identity lineage`
- previous_shot_pixels_used: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

Edit only three garment properties in the supplied flat-lay apparel design reference:
make the white opaque pantyhose thinner and slightly sheer, with a subtle natural
skin tone visible softly through the continuous textile; lighten the skirt from deep
chocolate brown to a lighter warm medium brown; and lighten the fuzzy mule slippers
from tan brown to a pale beige-tan. Keep the pantyhose clearly present as fabric over
all of its visible area and maintain a continuous finish; no bare toes or material
breaks. Preserve the exact garment layout, scale, folds, style, gray background,
lighting, cream-oatmeal cardigan, and ivory T-shirt. Keep the image strictly clothing
only, without any human, mannequin, leg or foot form. Avoid glossy, oily, latex,
plastic, rubber, or body-paint hosiery. Do not add labels, logos, text, or watermark.

## QA

- technical_status: `PASS`
- fit_validation_status: `PASS`
- face_contamination_check: `NOT_APPLICABLE`
- face_generation_method_followed: `not_applicable`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `PREVIOUSLY_APPROVED; SUPERSEDED_BY_v005`
- reviewer: `user`
- reviewed_at: `2026-10-17`

## Promotion provenance

- user_approval_statement: `通过 下一步` (historical approval; later superseded by v005)
- approved_at: `2026-10-17`
- approved_by: `user`
- promotion_operation: `Historical raster relocated from approved path back to its original candidate archive when v005 was approved; one raster copy retained.`
