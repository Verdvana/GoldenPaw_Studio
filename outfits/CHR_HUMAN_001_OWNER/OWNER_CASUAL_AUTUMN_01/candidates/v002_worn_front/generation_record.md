# Outfit Generation Record

- asset_id: `OWNER_CASUAL_AUTUMN_01_WORN_FRONT_v002`
- outfit_id: `OWNER_CASUAL_AUTUMN_01`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- asset_level: `L2`
- asset_purpose: `worn_front`
- view_type: `full_length_front_neutral_standing`
- candidate_version: `v002`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-19`
- output_path: pending generation
- output_sha256: pending generation
- reference_budget: `5 image inputs: source-derived face context, B-hair L0, scoped B-hair Canon, face-excluded BODY_01 derivative, deterministic garment contact sheet`

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png
    checksum_sha256: d98019128bfa974a102813da52b4a2905ec4aa7c95eb5222a163e419f287e74d
    responsibility: [front face identity, facial-feature relationships, natural age, skin texture and warm-neutral tone]
    must_not_define: [hair, body, outfit, hosiery, lighting, background]
  - asset_id: L0_OWNER_006
    path: characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg
    checksum_sha256: 734458326895b48099efa0dc58c43646d8b104823c1c36c1def8f27d08d88c17
    responsibility: [Hairstyle B hairline, pulled-back front, face-framing wisps and gathered updo relationship only]
    must_not_define: [face, expression, body, skin, sweater, lighting, background]
  - asset_id: OWNER_HAIR_B_01_FRONT_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/approved/HAIR_B_01_FRONT/OWNER_HAIR_B_01_FRONT_CANON_001.png
    checksum_sha256: 3692b4e2fd6da2607fd103b14d43d28afbbf66696861171b2ff5632dd3b07c35
    responsibility: [approved HAIRSTYLE_B front structure: compact pulled-back hair, restrained center part, face-side wisps and rearward gathering]
    must_not_define: [face, facial geometry, skin, body, outfit, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    checksum_sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b
    responsibility: [168 cm/60 kg front body geometry, neutral stance, limb proportions and grounded foot placement]
    must_not_define: [face, hair, clothing, hosiery material/color, lighting, background]
  - asset_id: OWNER_CASUAL_AUTUMN_01_GARMENT_CONTACT_SHEET_v1
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_01/reference_inputs/garment_contact_sheet_v1/OWNER_CASUAL_AUTUMN_01_GARMENT_CONTACT_SHEET_v1.png
    checksum_sha256: 988e72da526dd0919dc37590cb21a5486dccce4ea99eb753ae04dce71e694a30
    responsibility: [white lace-yoke top, black layered skirt, gunmetal-silver Mary Jane flats, silver-gray sparkling pantyhose]
    must_not_define: [person, face, body, skin, hair, pose, identity, lighting, background]
```

## QA comparison only

```yaml
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    purpose: post-generation identity and face-contamination comparison only; never generation input
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    purpose: post-generation body proportion and lower-leg-axis comparison only; never generation input
```

## Reference isolation

- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`
- hairstyle: `HAIRSTYLE_B`
- body_generation_source: `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1`
- approved_ai_face_or_body_used_as_generation_input: `false`
- previous_candidate_pixels_used: `false`
- garment_reference_used_for_identity_or_body: `false`

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: L2 front worn-outfit candidate for one adult owner character.
Input images: Image 1 defines only the owner's exact front face and skin; Image 2 defines only the L0 Hairstyle-B construction; Image 3 defines only the approved scoped Hairstyle-B front structure; Image 4 defines only face-excluded BODY_01 front geometry; Image 5 defines only the outfit components. Never use Image 2 or Image 3 to define face, skin or identity.
Primary request: Create exactly one full-length straight-on front-view photograph of the owner wearing the autumn casual outfit: white fitted long-sleeve high-neck top with ruffled collar and floral lace yoke; black elastic-waist tiered ruffle mini skirt with black lace trim; silver-gray visibly sparkling sheer pantyhose; gunmetal-silver Mary Jane flats with glossy black toe caps, narrow black straps and low block heels.
Character and hair: reproduce Image 1's exact front facial relationships, natural adult age and warm-neutral skin. Use HAIRSTYLE_B only: a compact, neat, pulled-back dark-brown updo with restrained center part, fine face-framing wisps and rearward gathering. No Hairstyle A hair. Preserve Image 4's natural 168 cm/60 kg front-body geometry and grounded neutral stance but never use it for face or hair.
Legs: both lower-leg skeletal axes must be visibly almost perfectly straight and parallel in front view: knee centers, tibial shafts and ankle centers nearly collinear; outer calf edges descend continuously from the same-side outer thighs, with natural calf volume but no inward bow, outward bow, O-leg impression, crossed legs or wide gap.
Hosiery: one continuous fine silver-gray textile pantyhose from waist/hips over thighs, knees, calves, ankles, heels, insteps and toes. Make the micro-glitter clearly more noticeable than the prior subtle version: evenly distributed fine silver sparkle catches the soft studio light without becoming sequins, metallic foil, oil, plastic, latex, PVC or hard linear glare.
Composition: exact 3:4 full body, head, hands, shoes and both feet fully within frame; level 70–85mm-equivalent camera centered around lower chest; upright torso, relaxed arms, uncrossed legs, parallel flat grounded feet; neutral gray-white seamless studio and soft even 5200–5600K light.
Avoid: face drift, beauty-filter plastic skin, face patches/smudges; any person traits from garment photos; Hairstyle A, long loose hair, curls, waves, high-volume crown; generic fashion-model anatomy, exaggerated curves, tiny waist, altered scale; bare toes, detached stockings, ankle socks, opaque glitter leggings, sequins, metallic foil, oily/plastic/rubber hosiery; visible logos, text, watermark, props or collage.
```

## QA

- technical_status: `PENDING_GENERATION`
- visual_status: `PENDING_GENERATION`
- source_derived_face_method_check: `PENDING_GENERATION`
- hairstyle_b_scope_check: `PENDING_GENERATION`
- face_contamination_check: `PENDING_GENERATION`
- body01_lower_leg_axis_check: `PENDING_GENERATION`
- hosiery_sparkle_continuity_material_check: `PENDING_GENERATION`
- decision: `PENDING_USER_REVIEW`
