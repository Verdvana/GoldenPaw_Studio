# Outfit Generation Record

- asset_id: OWNER_WORK_AUTUMN_01_WORN_FRONT_v002
- outfit_id: OWNER_WORK_AUTUMN_01
- asset_level: L2
- asset_purpose: worn_fit_validation
- view_type: worn_front
- head_policy: head_present_owner_face_method
- candidate_version: v002
- status: REVIEW_REQUIRED
- generation_tool: built-in ImageGen
- generated_at: 2026-09-20
- output_path: pending ImageGen output
- output_sha256: pending

## Validation target

- fit_or_design_question: Does the updated autumn officewear read naturally on the owner while preserving her approved body proportions and making the light-skin pantyhose unmistakably textile rather than bare feet?
- acceptance_checks:
  - full body from head to feet, neutral straight-on standing pose, both hands and both shoes visible
  - owner face uses only L0 source-derived face method inputs; no AI Face Canon, AI Body Canon, or previous candidate is a generation input
  - body proportions follow the face-excluded owner body derivative, including the 168 cm / 60 kg target, waist/hip ratio, limb scale, and lower-leg/foot proportions
  - HAIRSTYLE_A follows the face-masked L0 hair derivative only
  - pale blush-pink blazer, cool-gray inner top, warm gray-taupe wide-leg trousers, and black pointed-toe slingback pumps are unambiguous
  - light-skin 15D sheer matte/velvet-matte pantyhose is visibly present on both lower legs, ankles, insteps, and closed toes; no bare-foot appearance
  - no toe-cap seam, naked toe, hosiery break, latex/plastic/rubber appearance, warped hands, duplicated limbs, red outsole, logo, text, watermark, or copied reference background

## Generation inputs

```yaml
generation_inputs:
  - asset_id: L0_OWNER_012
    path: characters/CHR_HUMAN_001_OWNER/source/identity/raw/14.jpg
    sha256: f7a83644f202ebec95134c6d115397b9f52f12e79b5fb227a6b79182026bd788
    responsibility: [front-visible owner facial identity, natural facial-feature relationships, skin identity direction]
    must_not_define: [hairstyle, body, clothing, hosiery, pose, lighting, background, photography style]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    sha256: 6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd
    responsibility: [HAIRSTYLE_A front construction, parting, volume, side fall, length, tapered ends]
    must_not_define: [face, skin, body, clothing, pose, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b
    responsibility: [neck-below owner body geometry, 168 cm / 60 kg proportion range, waist/hip ratio, limb scale, lower-leg and foot scale]
    must_not_define: [face, facial identity, hair, clothing design, hosiery material, lighting, background]
  - asset_id: OWNER_WORK_AUTUMN_01_REF_002
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_AUTUMN_01/reference_inputs/garment_references/IMG_0002_USER_AUTUMN_WORKWEAR.jpg
    sha256: 16ed92e97ca3d3d59987f88d36903feb8af3912fe875812a4fcd315daae461d5
    responsibility: [blazer silhouette and palette, inner top, wide-leg trousers, layering and drape]
    must_not_define: [model identity, face, body, skin, hair, pose, hosiery, footwear, lighting, background, photography style]
  - asset_id: OWNER_WORK_AUTUMN_01_REF_001
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_AUTUMN_01/reference_inputs/garment_references/IMG_2779.jpg
    sha256: 855f7cac41b7a097680663b11097cdebf86360dbdb02d92e927b29315e1e3886
    responsibility: [black pointed-toe slingback silhouette, rear strap and buckle, slender heel]
    must_not_define: [model identity, face, body, skin, hair, pose, red outsole, branding, lighting, background, photography style]
```

The hosiery is constrained by the registered text specification for
`L0_HOS_15_NM_011` and its provenance record, but is not attached as a sixth
pixel input because the built-in image tool caps the reference set at five
images. This preserves face/body/garment/shoe reference isolation.

## QA comparison only

```yaml
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope: [identity drift, facial-feature relationships, skin contamination, head projection, rendering artifacts]
```

## Reference isolation

- reference_set_ids: `OWNER_L0_FACE_FRONT_NEUTRAL`, `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`
- reference_budget: 5 images
- previous_candidate_pixels_used: false
- previous_shot_pixels_used: false
- AI Face Canon used as generation input: false
- AI Body Canon used as generation input: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false
- lighting_or_background_taken_from_garment_reference: false

## Prompt assembly

- use case: photorealistic-natural
- asset type: reusable L2 worn outfit fit-validation image
- scene/backdrop: neutral light-gray seamless studio background, no task, no props, no narrative environment
- composition: 3:4 full-body straight-on front view, eye-level camera, 70–85 mm equivalent, head-to-feet visible with both shoes and hosiery-covered feet fully in frame
- pose: relaxed neutral standing, shoulders level, arms naturally down, hands visible, knees relaxed, feet naturally slightly apart and fully grounded
- face method: source-derived face recovery from L0 `14.jpg` only, with true eye-level projection and natural even skin; no AI identity image as input
- hair method: HAIRSTYLE_A from face-masked `DSC00847` derivative only
- body method: face-excluded body derivative only; preserve owner proportions and lower-leg/foot scale; do not inherit its calibration outfit
- outfit: pale blush-pink tailored blazer, cool-gray sleeveless inner top, warm gray-taupe high-waisted wide-leg tailored trousers, black pointed-toe slingback pumps with rear strap/buckle and slender heel
- hosiery: unmistakable light-skin 15D sheer matte/velvet-matte pantyhose, continuous from waist beneath trousers through both ankles, insteps, heels and closed toes; visible soft textile veil and subtle weave/opacity so feet do not read as bare skin
- constraints: garment references define clothing only; shoe reference defines shoe construction only; hosiery reference defines material only; no red outsole, no branding, no copied background or embedded text
- avoid: bare feet, naked toes, transparent airbrushed skin, hosiery disappearing at ankles, toe-cap line, black hosiery, white sweater, plastic/latex/rubber/liquid shine, cropped feet, extra person, phone, bag, jewelry, text, watermark
