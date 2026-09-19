# Outfit Generation Record

- asset_id: `OWNER_CASUAL_AUTUMN_01_WORN_FRONT_v003`
- outfit_id: `OWNER_CASUAL_AUTUMN_01`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- asset_level: `L2`
- asset_purpose: `worn_front`
- candidate_version: `v003`
- status: `APPROVED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-19`
- original_candidate_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01/candidates/v003_worn_front/OWNER_CASUAL_AUTUMN_01_WORN_FRONT_v003.png`
- approved_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01/approved/worn_front/OWNER_CASUAL_AUTUMN_01_WORN_FRONT.png`
- output_sha256: `a971cfb4c5e31847fd6e905826254ecd379d2c3f64ac9c7a31622b4e111563ae`
- reference_budget: `5 image inputs; independently regenerated from source/approved scoped assets, no v001/v002 pixels`

## Generation inputs

```yaml
generation_inputs:
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png, responsibility: [face identity and skin only], must_not_define: [hair, body, outfit, lighting, background]}
  - {asset_id: L0_OWNER_006, path: characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg, responsibility: [Hairstyle B L0 construction only], must_not_define: [face, skin, body, outfit, lighting, background]}
  - {asset_id: OWNER_HAIR_B_01_FRONT_CANON_001, path: characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/approved/HAIR_B_01_FRONT/OWNER_HAIR_B_01_FRONT_CANON_001.png, responsibility: [Hairstyle B front structure only], must_not_define: [face, skin, body, outfit, lighting, background]}
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png, responsibility: [BODY_01 face-excluded front geometry, proportion and stance only], must_not_define: [face, hair, clothing, hosiery material, lighting, background]}
  - {asset_id: OWNER_CASUAL_AUTUMN_01_GARMENT_CONTACT_SHEET_v1, path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01/reference_inputs/garment_contact_sheet_v1/OWNER_CASUAL_AUTUMN_01_GARMENT_CONTACT_SHEET_v1.png, responsibility: [top, skirt, silver Mary Jane flats and gray sparkling pantyhose only], must_not_define: [person, face, body, skin, hair, pose, lighting, background]}
```

## QA comparison only

```yaml
qa_comparison_only:
  - {asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001, purpose: face identity and contamination comparison only}
  - {asset_id: OWNER_BODY_01_FRONT_CANON_007, purpose: front body proportion and lower-leg-axis comparison only}
```

## Reference isolation

- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`
- hairstyle: `HAIRSTYLE_B`
- approved_ai_face_or_body_used_as_generation_input: `false`
- previous_candidate_pixels_used: `false`
- garment_reference_used_for_identity_or_body: `false`

## Prompt assembly

```text
Use case: photorealistic-natural. Create exactly one independent L2 front worn-outfit candidate, full body, not an edit and not based on any previous candidate. Image 1 defines only exact face and skin. Images 2–3 define only Hairstyle B. Image 4 defines only face-excluded BODY_01 geometry. Image 5 defines only the outfit.

Show the adult owner in the white lace-yoke high-neck long-sleeve top, black tiered lace-trim mini skirt, clearly visibly micro-sparkling silver-gray continuous sheer pantyhose, and gunmetal-silver Mary Jane flats with black patent toes and low heels. Face must exactly follow Image 1; use only the compact pulled-back dark-brown HAIRSTYLE_B with restrained center part and fine wisps from Images 2–3.

Strict front lower-leg construction: in the straight-on view, both knee centers, tibial shafts and ankle centers align on two nearly vertical, parallel axes. Each outer calf contour descends almost directly from the outer thigh edge, with natural adult calf volume but no visible inward bend or pinch at mid-calf. Each inner calf contour likewise descends almost vertically; leave a narrow, nearly uniform, natural air gap between lower legs. Do not taper, curve or angle either shin toward the other; no O-leg or X-leg appearance. Flat parallel feet, both fully grounded.

Pantyhose is a continuous woven textile from waist to closed toes, with clearly visible but fine and evenly distributed silver micro-sparkle. It is not opaque glitter leggings, sequins, foil, plastic, oil, PVC, rubber or latex.

Exact 3:4, full head/hands/shoes inside frame, level 70–85mm camera, neutral gray-white seamless studio, soft even light. Avoid long loose Hair A, face drift, skin patches/smudges, generic-model body changes, exaggerated waist/curves, bare toes, detached stockings, logos, text, watermark, props or collage.
```

## QA

- technical_status: `PASS` — PNG, 1086 × 1448 px, exact 3:4, checksum recorded
- visual_status: `PASS_WITH_USER_REVIEW`
- source_derived_face_method_check: `PASS` — source-derived face context only; no AI Face Canon supplied as an input
- hairstyle_b_scope_check: `PASS_WITH_USER_REVIEW` — compact pulled-back B updo, restrained center part and fine wisps; no long loose A hair
- strict_lower_leg_axis_check: `PASS_WITH_USER_REVIEW` — tibial silhouettes descend substantially straighter and more parallel than v002; user to make final BODY_01 fidelity call
- hosiery_sparkle_continuity_material_check: `PASS_WITH_USER_REVIEW` — visible, evenly distributed fine silver micro-sparkle; continuous silver-gray textile into closed shoes, no plastic/oily appearance
- decision: `APPROVED_BY_USER`

## Promotion provenance

- user_approval_statement: `可以，无人物和最后这个有人物的都可以登记了`
- approved_at: `2026-09-19`
- approved_by: `user`
- promotion_operation: `MOVED — candidate raster relocated unchanged; no second project raster retained`
