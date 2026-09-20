# Outfit Generation Record

- asset_id: OWNER_WORK_AUTUMN_01_WORN_FRONT_v003
- outfit_id: OWNER_WORK_AUTUMN_01
- asset_level: L2
- asset_purpose: worn_fit_validation
- view_type: worn_front
- head_policy: head_present_owner_face_method
- candidate_version: v003
- status: APPROVED_SCOPED_L2
- generation_tool: built-in ImageGen
- generated_at: 2026-09-20
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_AUTUMN_01/approved/worn_front/OWNER_WORK_AUTUMN_01_WORN_FRONT.png
- output_sha256: f2dea9d7724191d5b3316c74cf8a4b90309eae8b96163c496971694b9cae2b45

## Validation target

- fit_or_design_question: Does the updated officewear preserve the owner's proportions while making the light-skin pantyhose unmistakably visible and continuous?
- acceptance_checks:
  - full head-to-feet front view, neutral pose, both hands and shoes visible
  - face from L0 source-derived method only; body proportions from the face-excluded body derivative only
  - long straight HAIRSTYLE_A fully down, no tied or half-up section
  - pale-pink blazer, cool-gray inner top, taupe-gray wide-leg trousers, black slingback pumps
  - light-skin 15D sheer matte/velvet-matte pantyhose visibly covers the exposed lower legs, ankles, insteps, heels and closed toes; it must read as a textile veil, not bare skin
  - no toe-cap seam, naked toes, hosiery break, red outsole, logo, text, watermark, or reference background

## Generation inputs

```yaml
generation_inputs:
  - asset_id: L0_OWNER_012
    path: characters/CHR_HUMAN_001_OWNER/source/identity/raw/14.jpg
    responsibility: [front-visible owner facial identity, natural facial-feature relationships, skin identity direction]
    must_not_define: [hairstyle, body, clothing, hosiery, pose, lighting, background, photography style]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    responsibility: [HAIRSTYLE_A long straight hair construction only]
    must_not_define: [face, skin, body, clothing, pose, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: [168 cm / 60 kg owner body proportion range, waist/hip, limb, lower-leg and foot scale]
    must_not_define: [face, identity, hair, clothing, hosiery material, lighting, background]
  - asset_id: OWNER_WORK_AUTUMN_01_REF_002
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_AUTUMN_01/reference_inputs/garment_references/IMG_0002_USER_AUTUMN_WORKWEAR.jpg
    responsibility: [blazer, inner top, trousers, layering, palette and drape]
    must_not_define: [model identity, face, body, skin, hair, pose, hosiery, footwear, lighting, background]
  - asset_id: OWNER_WORK_AUTUMN_01_REF_001
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_AUTUMN_01/reference_inputs/garment_references/IMG_2779.jpg
    responsibility: [black pointed-toe slingback, rear strap/buckle, slender heel]
    must_not_define: [model identity, face, body, skin, hair, pose, red outsole, branding, lighting, background]
```

Hosiery follows the registered text specification for `L0_HOS_15_NM_011`
(`materials/hosiery/source_library/raw/15d_nude_matte/1.jpg`), but is not an
attached sixth pixel input because the built-in tool accepts at most five
reference images.

## QA comparison only

```yaml
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope: [identity drift, facial-feature relationships, skin contamination, head projection, rendering artifacts]
```

## Reference isolation

- reference_budget: 5 images
- previous_candidate_pixels_used: false
- previous_shot_pixels_used: false
- AI Face Canon used as generation input: false
- AI Body Canon used as generation input: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false

## Prompt assembly

- use case: photorealistic-natural
- scene/backdrop: neutral light-gray seamless studio, no task or props
- composition: 3:4 vertical full-body front, eye-level, head-to-feet and both shoes complete
- body: preserve the owner's 168 cm / 60 kg target, waist/hip ratio and lower-leg/foot proportions from the face-excluded derivative
- hair: strict HAIRSTYLE_A, long straight dark-brown hair fully down, near-center part, no ponytail or half-up section
- outfit: pale blush-pink blazer, cool-gray sleeveless inner top, warm gray-taupe wide-leg trousers, black pointed-toe slingback pumps
- trouser hem: wide-leg trousers end 8–10 cm above the ankle to expose enough lower leg for hosiery QA while retaining the reference silhouette
- hosiery: light-skin 15D sheer matte/velvet-matte pantyhose, warm light-beige nude tint slightly distinct from bare hand skin, visibly continuous from under trousers across both exposed lower legs, ankles, insteps, heels, shoe openings and closed toes; a clear but natural fabric veil with subtle matte texture and no bare-foot reading
- avoid: bare feet, naked toes, hosiery invisible at ankles, black hosiery, toe-cap boundary, plastic/latex/rubber shine, red outsole, branding, text, watermark, warped hands, duplicated limbs, extra props
