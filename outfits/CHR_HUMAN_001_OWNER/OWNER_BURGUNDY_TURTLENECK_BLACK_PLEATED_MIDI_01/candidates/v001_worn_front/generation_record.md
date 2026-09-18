# Outfit Generation Record — OWNER_BURGUNDY_TURTLENECK_BLACK_PLEATED_MIDI_01

```yaml
asset_id: OWNER_BURGUNDY_TURTLENECK_BLACK_PLEATED_MIDI_01_WORN_FRONT
outfit_id: OWNER_BURGUNDY_TURTLENECK_BLACK_PLEATED_MIDI_01
character_id: CHR_HUMAN_001_OWNER
asset_level: L2
asset_purpose: worn_fit_preview
view_type: worn_front
candidate_version: v001
status: REVIEW_REQUIRED
generation_tool: built_in_image_gen
generated_at: 2026-09-18
reference_set_ids:
  - OWNER_BODY_FRONT_CANON_L1
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
  - OWNER_HAIRSTYLE_A_L0
  - HOS_15D_BLACK_HIGH_GLOSS_OVERALL
reference_budget: 5 inputs
generation_inputs:
  - asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png
    responsibility: source-derived front face and neutral skin only
    must_not_define: [hair, body, clothing, hosiery, lighting, background]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    responsibility: Hairstyle A only
    must_not_define: [face, body, clothing, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_V017_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_V017_FACE_EXCLUDED_v1/BODY_01_FRONT_V017_FACE_EXCLUDED_CROP.png
    responsibility: current Body01 neck-below proportions and straight front leg axes
    must_not_define: [face, facial identity, hair, clothing, hosiery material, lighting, background]
  - asset_id: L0_HOS_15_BHG_002
    path: materials/hosiery/source_library/raw/15d_black_high_gloss/IMG_2569.jpg
    responsibility: black 15D high-gloss textile finish and highlight behavior only
    must_not_define: [owner identity, face, body, skin, clothing, shoes, pose, background]
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    responsibility: post-generation identity drift and face contamination QA only
  - asset_id: OWNER_BODY_01_FRONT_CANON_006
    path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v017/BODY_01_FRONT_v017.png
    responsibility: post-generation Body01 proportion continuity QA only
previous_candidate_pixels_used: false
previous_shot_pixels_used: false
output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_BURGUNDY_TURTLENECK_BLACK_PLEATED_MIDI_01/candidates/v001_worn_front/OWNER_BURGUNDY_TURTLENECK_BLACK_PLEATED_MIDI_01_WORN_FRONT_v001.png
output_sha256: 3430de75a90c52c697d2abe56c6b50e81287f05565c9c5fac70ab77039c967dd
dimensions: 1086x1448
qa_status: PRELIMINARY_VISUAL_PASS_USER_REVIEW
```

## Prompt assembly

Create one photorealistic vertical 3:4 full-body front worn-fit preview of the adult owner standing neutrally in a light-gray seamless studio. Use source-derived face/skin input for the face only, masked Hairstyle A for hair only, and the deterministic face-excluded Body01 derivative for all neck-below proportions. Do not use any generated Face or Body raster as a generation input.

Outfit: fitted deep burgundy long-sleeve high-neck rib-knit sweater, black high-waisted pleated midi skirt with many narrow crisp pleats, hem ending at mid-calf, opaque enough to read as a solid black skirt. Black closed-toe round-toe flat shoes with a simple low profile. Black 15D high-gloss sheer pantyhose with continuous coverage under the skirt to the feet; use the material reference only for black glossy textile and broad soft highlights, never for its shoes, pose or photographed person.

Preserve current Body01 proportions and nearly straight front leg axes, without slimming, lengthening or reshaping the body. Neutral adult wardrobe catalog presentation, natural fit, no exaggerated curves, no exposed skin between garments and hosiery, no logos, text, watermark, props or dramatic lighting. Complete head and shoes in frame, level 70–85mm-equivalent camera, soft even neutral light, no collage.

## QA

Check Body01 neck-below proportions and straight leg axes; face contamination against the approved Face Canon comparison-only reference; sweater high-neck fit; skirt hem at mid-calf; many evenly distributed pleats; round-toe flat shoes; continuous black 15D high-gloss hosiery with realistic textile highlights and no latex/PVC/plastic/wet-body-paint appearance. Candidate remains REVIEW_REQUIRED and is not Canon.

## Generation output

- built-in ImageGen source: `/home/verdvana/.codex/generated_images/01a0b234-2506-7391-8aea-15bd3e1dab5c/exec-eff6ea9e-51be-43dd-b502-ece9e6944b59.png`
- repository candidate: `outfits/CHR_HUMAN_001_OWNER/OWNER_BURGUNDY_TURTLENECK_BLACK_PLEATED_MIDI_01/candidates/v001_worn_front/OWNER_BURGUNDY_TURTLENECK_BLACK_PLEATED_MIDI_01_WORN_FRONT_v001.png`
- visual precheck: outfit components are present; skirt hem reads at mid-calf with many narrow pleats; candidate remains unapproved pending user review.
