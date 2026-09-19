# Outfit Generation Record

- asset_id: `OWNER_CASUAL_AUTUMN_01_WORN_FRONT_v001`
- outfit_id: `OWNER_CASUAL_AUTUMN_01`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- asset_level: `L2`
- asset_purpose: `worn_front`
- view_type: `full_length_front_neutral_standing`
- candidate_version: `v001`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-19`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01/candidates/v001_worn_front/OWNER_CASUAL_AUTUMN_01_WORN_FRONT_v001.png`
- output_sha256: `37895e50f464599b8fa7db2e16ccf0dda17e5cab617e98ac9d4c113b0527da51`
- reference_budget: `4 image inputs: 2 L0-derived face/hair inputs, 1 face-excluded body derivative, 1 deterministic four-source garment contact sheet`

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png
    checksum_sha256: d98019128bfa974a102813da52b4a2905ec4aa7c95eb5222a163e419f287e74d
    responsibility: [front face identity, facial-feature relationships, natural age, skin texture and warm-neutral tone]
    must_not_define: [hair, body, outfit, hosiery, lighting, background]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    checksum_sha256: 6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd
    responsibility: [Hairstyle A: near-center part, low crown, long straight loose dark-brown hair and tapered ends]
    must_not_define: [face, body, skin, outfit, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    checksum_sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b
    responsibility: [168 cm/60 kg front body geometry, neutral front stance, body proportions, limb axes and ground contact]
    must_not_define: [face, hair, clothing, hosiery material/color, lighting, background]
  - asset_id: OWNER_CASUAL_AUTUMN_01_GARMENT_CONTACT_SHEET_v1
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01/reference_inputs/garment_contact_sheet_v1/OWNER_CASUAL_AUTUMN_01_GARMENT_CONTACT_SHEET_v1.png
    checksum_sha256: 988e72da526dd0919dc37590cb21a5486dccce4ea99eb753ae04dce71e694a30
    responsibility: [black layered ruffle mini skirt, white high-neck lace-yoke long-sleeve top, gunmetal-silver Mary Jane flats, silver-gray subtly sparkling continuous pantyhose]
    must_not_define: [person, face, body, skin, hair, pose, identity, lighting, background]
```

## QA comparison only

```yaml
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    checksum_sha256: 4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4
    purpose: post-generation face identity and contamination comparison only; never generation input
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    checksum_sha256: 90e021fcf5c72416b2b3c6405cfe2abe2d43c28e49da6dbabc250f73da306978
    purpose: post-generation body proportion and stance comparison only; never face-generation input
```

## Reference isolation

- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`
- body_generation_source: `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1`
- approved_ai_face_or_body_used_as_generation_input: `false`
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- garment_reference_used_for_identity_or_body: `false`
- garment_contact_sheet_provenance: `reference_inputs/garment_contact_sheet_v1/PROVENANCE.md`

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: L2 front worn-outfit candidate for one adult owner character.
Input images: Image 1 defines only the owner's exact front face and skin; Image 2 defines only Hairstyle A; Image 3 defines only the face-excluded front body geometry and stance; Images 4–7 define only the supplied skirt, top, shoes and hosiery.
Primary request: Create exactly one full-length straight-on front-view photograph of the owner wearing the declared autumn casual outfit: white fitted long-sleeve high-neck top with a ruffled collar and floral lace yoke; black elastic-waist tiered ruffle mini skirt with black lace trim; silver-gray subtly sparkling sheer pantyhose; gunmetal-silver Mary Jane flats with glossy black toe caps, narrow black straps and low block heels.
Character: preserve the exact facial relationships, natural adult age and warm-neutral skin texture from Image 1; use only the long, straight, near-center-parted low-crown Hairstyle A from Image 2. Preserve the natural 168 cm/60 kg front-body geometry, proportions, straight aligned lower-leg axes and neutral grounded stance from Image 3; do not use Image 3 for face or hair.
Composition: exact 3:4 portrait, full head, hands, shoes and both feet inside frame, 70–85mm-equivalent level camera centered around lower chest, direct front view, upright torso, relaxed arms, uncrossed legs, feet planted naturally parallel.
Scene/backdrop: neutral gray-white seamless studio.
Lighting: soft even 5200–5600K studio illumination, realistic natural photographic skin and textile detail.
Hosiery: one continuous fine textile pantyhose from waist/hips over thighs, knees, calves, ankles, heels, insteps and toes; silver-gray restrained micro-sparkle, sheer textile—not plastic or oil. Toenails need not be visible through this gray hosiery.
Constraints: respectful natural standing fashion-reference image; all garment source images define clothing only and must not change identity, face, hair, body, skin, pose, lighting or background.
Avoid: any generated candidate or Canon as an input; face drift, skin blotches, smudges, relighting patches, beauty-filter plastic skin; HAIRSTYLE_B, bun, curls, waves, high crown; generic fashion-model anatomy, exaggerated curves, tiny waist, altered body scale, bowed legs, crossed legs, floating heels; person/mannequin traits from garment photos; bare toes, detached stockings, ankle socks, oily/latex/PVC/rubber hosiery, hard linear shine; visible logos, labels, text, watermark, props, collage.
```

## QA

- technical_status: `PASS` — PNG, 1086 × 1448 px, exact 3:4, checksum recorded
- visual_status: `PASS_WITH_USER_REVIEW`
- source_derived_face_method_check: `PASS` — only `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` and the masked L0 Hairstyle-A derivative supplied for visible face/hair; no AI Face Canon was input
- face_contamination_check: `PASS_WITH_USER_REVIEW` — no visible blotches, muddy relighting, patches or smudges; compare against approved Face Canon remains user-facing identity QA
- body_geometry_check: `PASS_WITH_USER_REVIEW` — full frontal standing figure, relaxed arms, uncrossed legs, grounded feet and near-straight lower-leg axes; compare against approved Body01 scope remains user-facing QA
- garment_fidelity_check: `PASS_WITH_USER_REVIEW` — white ruffled-collar lace-yoke top, black tiered lace-trim mini skirt, silver Mary Jane flats with black toes/straps are present
- hosiery_continuity_and_material_check: `PASS_WITH_USER_REVIEW` — silver-gray micro-sparkle textile appears continuous from skirt hem into shoes; toe coverage is partially occluded by shoes and requires user confirmation
- downstream_identity_lineage_allowed: `false`
- decision: `PENDING_USER_REVIEW`
