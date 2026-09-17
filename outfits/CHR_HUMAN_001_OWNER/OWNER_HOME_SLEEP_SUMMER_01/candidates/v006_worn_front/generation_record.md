# Outfit Generation Record

- asset_id: `OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT`
- outfit_id: `OWNER_HOME_SLEEP_SUMMER_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- head_policy: `head_present_owner_face_method`
- candidate_version: `v006`
- status: `REVIEW_REQUIRED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_HOME_SLEEP_SUMMER_01/candidates/v006_worn_front/OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT_v006.png`
- output_sha256: `73c5ff63faacd0c82d1d9555150d90267e3720b4cb9787809d3130c51e6b418c`
- reference_budget: `4 inputs; source-derived face set + full-head face-masked body geometry reference + approved outfit design reference`

## Generation inputs

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png
    responsibility: [owner face identity and facial-feature relationships]
    must_not_define: [hair, body, clothing, lighting, background]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    responsibility: [Hairstyle-A presentation]
    must_not_define: [face, body, clothing, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_FULL_HEAD_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_HEAD_FACE_MASKED_v1/BODY_01_FRONT_FULL_HEAD_FACE_MASKED.png
    responsibility: [head size and outer face contour, neck-to-shoulder relationship, BODY_01 body proportions and limb scale]
    must_not_define: [facial features, facial identity, facial skin tone, skin texture, hair style, clothing, hosiery, footwear, lighting, background]
  - asset_id: OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_HOME_SLEEP_SUMMER_01/approved/design_reference/OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE.png
    responsibility: [warm-ivory floral satin sleep dress, cowl neckline, straps, short flared hem, pale-pink feather-trimmed open-toe slides, outfit hosiery contract]
    must_not_define: [owner identity, face, body, skin, hair, pose, lighting, background]
```

## QA comparison only

```yaml
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope: [identity drift, face contamination, facial projection]
```

## Reference isolation

- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- ai_face_canon_used_as_generation_input: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- head_scale_reference_used: `OWNER_BODY_01_FRONT_FULL_HEAD_FACE_MASKED_001`

## Prompt assembly

```text
Create one photorealistic, modest professional apparel-catalog fitting image of one adult owner standing neutrally in a light-gray studio, full body from head to floor, centered vertical 3:4 front view. Generate visible facial features only from the source-derived Face method inputs. Use Hairstyle-A exactly: long, straight, dark-brown hair falling naturally over both shoulders, no bun or updo.

Use the full-head face-masked BODY_01 reference as the strict geometry and scale guide: match its complete head outer silhouette, head size relative to shoulders and body, face contour, neck length, shoulder width, compact torso, waist-to-hip relationship, fuller thighs, natural calf volume, limb lengths and overall realistic adult proportions. The masked oval contains no facial identity information; do not copy its masked face, skin color or facial features. Do not create a small head, 8-head fashion-model proportion, elongated legs, O-shaped legs or X-shaped legs. Keep both knee-shin-ankle axes near vertical and feet naturally aligned.

Dress the owner in the approved summer sleepwear: warm-ivory floral satin camisole-strap short sleep dress with small pink/peach floral print, softly draped cowl neckline, fine double straps, natural satin drape and short gently flared hem; pale-pink feather-trimmed open-toe flat slide slippers. Add continuous nude 15D sheer pantyhose from waist through ankles, insteps, heels and toes beneath the open-toe slippers, with a restrained glossy soft-sheen textile response and visible fine fabric tension over the toe contours. Toes remain covered by hosiery; no exposed toenails or bare skin through the open toe.

Use a seamless neutral light-gray studio, soft even catalog lighting, normal non-glamorous apparel perspective, no props, no text, no logo, no watermark. Preserve the head/body scale from the face-masked BODY_01 geometry reference and the face identity from source-derived Face inputs only. This is an L2 clothing-fit validation image, not a Canon or video keyframe.
```

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- fit_validation_status: `REVIEW_REQUIRED`
- head_to_body_ratio_check: `PASS_WITH_USER_REVIEW`
- body_proportion_check: `PASS_WITH_USER_REVIEW`
- hairstyle_check: `PASS_WITH_USER_REVIEW`
- dress_fit_and_drape_check: `PASS_WITH_USER_REVIEW`
- hosiery_continuity_check: `REVIEW_REQUIRED`
- footwear_relationship_check: `REVIEW_REQUIRED`
- face_contamination_check: `REVIEW_REQUIRED`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `PENDING_USER_REVIEW`
