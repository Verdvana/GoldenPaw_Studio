# Outfit Generation Record

- asset_id: `OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT`
- outfit_id: `OWNER_HOME_SLEEP_SUMMER_01`
- asset_level: `L2`
- asset_purpose: `worn_fit_validation`
- view_type: `worn_front`
- candidate_version: `v007`
- status: `NO_OUTPUT_MODERATION_BLOCKED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_HOME_SLEEP_SUMMER_01/candidates/v007_worn_front/OWNER_HOME_SLEEP_SUMMER_01_WORN_FRONT_v007.png`
- output_sha256: `none — no raster output`
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
    responsibility: [head scale and contour, BODY_01 proportions, straight lower-leg axes, feet scale and stance]
    must_not_define: [facial features, facial identity, facial skin tone, skin texture, hair style, clothing, hosiery finish, footwear design, lighting, background]
  - asset_id: OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_HOME_SLEEP_SUMMER_01/approved/design_reference/OWNER_HOME_SLEEP_SUMMER_01_DESIGN_REFERENCE.png
    responsibility: [floral satin sleep dress, cowl neckline, straps, hem, pale-pink feather open-toe slides, glossy hosiery contract]
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
- head_scale_reference_used: `OWNER_BODY_01_FRONT_FULL_HEAD_FACE_MASKED_001`
- body_geometry_reference_used: `OWNER_BODY_01_FRONT_FULL_HEAD_FACE_MASKED_001`

## Prompt assembly

```text
Create one photorealistic, modest professional apparel-catalog fitting image of one adult owner standing neutrally in a light-gray studio, full body from head to floor, centered vertical 3:4 front view. Generate visible facial features only from source-derived Face method inputs. Use Hairstyle-A: long, straight, dark-brown hair over both shoulders, no bun or updo.

Use the full-head face-masked BODY_01 reference as strict authority for head size, outer face contour, neck and shoulders, and all body proportions. Preserve its natural adult scale, compact torso, waist-to-hip relationship, fuller thighs, straight lower-leg geometry and feet scale. The lower legs must be anatomically straight in front view: each knee center, shin-bone centerline and ankle center must form an almost vertical axis with no outward bowing. No O-shaped legs, no X-shaped legs, no knees drifting outward, no inward ankles. Keep both feet separate, parallel and naturally aligned.

Dress the owner in the approved warm-ivory floral satin camisole-strap short sleep dress with small pink/peach floral print, softly draped cowl neckline, fine double straps, natural satin drape and short gently flared hem; pale-pink feather-trimmed open-toe flat slide slippers.

Add continuous nude 15D sheer glossy pantyhose from waist through thighs, knees, calves, ankles, insteps, heels and toes. The oil-sheen effect must be represented by one narrow, soft, controlled vertical highlight on the front-center of each shin and instep, with gentle feathered edges—not broad flat shine, not harsh white streaks, not plastic or wet latex. At the toe area, show real hosiery fabric tension: the same textile stretches smoothly over each toe contour and across the forefoot, with subtle fine tension lines following the toe forms, no toe-cap seam, no transverse cutoff, no broken fabric and no bare toes. Burgundy toenail polish may show only as muted, diffused dark wine-red shapes beneath the sheer hosiery, never painted on top of the fabric and never overemphasized.

Use soft even neutral catalog lighting, normal perspective, no props, no text, no logo, no watermark. This is an L2 clothing-fit validation image, not a Canon or video keyframe. Do not change the head/body scale, leg axes, body proportions, face identity, hair or outfit design.
```

## QA

- technical_status: `UNREVIEWED`
- visual_status: `REVIEW_REQUIRED`
- fit_validation_status: `REVIEW_REQUIRED`
- head_to_body_ratio_check: `REVIEW_REQUIRED`
- lower_leg_axis_check: `REVIEW_REQUIRED`
- hosiery_gloss_highlight_check: `REVIEW_REQUIRED`
- toe_hosiery_tension_check: `REVIEW_REQUIRED`
- burgundy_toenail_under_hosiery_check: `REVIEW_REQUIRED`
- face_contamination_check: `REVIEW_REQUIRED`
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `PENDING_USER_REVIEW`

## Generation attempt result

- generation_attempt_result: `BLOCKED_BY_IMAGEGEN_SAFETY_SYSTEM`
- generation_attempt_count: `2`
- generation_attempt_note: `Both full-body apparel fit-study calls were rejected at output moderation with sexual category; no v007 raster was produced. No identity, body, hosiery or footwear evidence is written back from the failed calls.`
