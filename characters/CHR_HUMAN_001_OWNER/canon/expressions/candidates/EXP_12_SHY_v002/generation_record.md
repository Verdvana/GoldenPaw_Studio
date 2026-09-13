# EXP_12_SHY_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.95
identity_md_revision: draft_0.83
asset_id: EXP_12_SHY
candidate_id: EXP_12_SHY_v002
gate: "Gate 5 — Expression Canon (user-authorized scoped revision)"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
  - OWNER_L0_EXPRESSION_SHY_LIMITED
reference_count: 3
l0_expression_reference_count: 1
previous_ai_expression_candidate_count: 0
prohibited_pixel_inputs:
  - EXP_12_SHY_v001
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_12_SHY_v002/EXP_12_SHY_v002.png"
checksum_sha256: "73f46af06f851b92810d9e77013f23c2b96517f783714a9e8f43d924b943ab7b"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/approved/EXP_12_SHY/OWNER_EXP_12_SHY_CANON_001.png"
current_promoted_checksum_sha256: "73f46af06f851b92810d9e77013f23c2b96517f783714a9e8f43d924b943ab7b"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user rejected v001 and authorized one independent v002 with exactly three directional changes: lower the head somewhat, add a subtly visible natural facial blush, and increase the closed-mouth smile slightly. v001 pixels are prohibited. The new image is reconstructed in parallel from approved Face, approved Hair-A and scoped real L0 expression motion only.

## Reference budget and responsibility plan

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` / `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4` — sole permanent identity, geometry, age, base skin tone and neutral eye-level projection; must not define shy motion, hair, outfit, blush, background or lighting.
2. `OWNER_HAIR_A_01_FRONT_CANON_001` / `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219` — approved front Hairstyle-A only; must not define face, expression, skin, body, outfit, background or lighting.
3. `L0_OWNER_011` (`13.jpg`) / `5bc0c57d0870a534814125112aef654ace4aac0616610e737559381370717d54` — slight downward/averted gaze, modest head lowering direction, restrained closed-mouth smile and shy soft-tissue direction only; must not define identity, exact head rotation, hand pose, makeup, permanent blush/skin tone, hairstyle, veil, clothing, body, lighting or background.

## Candidate authority

- authoritative_for if approved: EXP_12 transient shy action with modest downward head pitch, downward side-averted gaze, slightly clearer but still restrained closed-mouth smile, and subtle natural localized cheek blush.
- must_not_define: permanent face, eye, brow, lip, nose, jaw/chin geometry; permanent skin tone/blush; Hair-A; body; outfit; lighting; background; pose outside this Expression; or other Expressions.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 expression calibration candidate `EXP_12_SHY_v002`; one adult woman; one image; REVIEW_REQUIRED.

Generate a fresh image from the three declared sources only. Do not use or imitate v001 or any other generated Expression image. Image 1 solely defines permanent facial identity, geometry, age and base skin tone. Image 2 solely defines approved front Hairstyle A. Image 3 is real L0 expression-motion support only: use its modest downward head direction, slightly downward/averted gaze, restrained closed-mouth smile and gentle shy soft-tissue behavior; exclude its identity, exact turn, hand, wedding makeup, blush color, hairstyle, veil, clothing, background and lighting.

User corrections for v002: lower the head somewhat more than the first attempt—use a modest natural downward pitch of about 6–9 degrees, with the chin visibly but gently lowered while the face remains close to frontal and the shoulders stay level. Direct both eyes slightly downward and toward image-right, coherently following the lowered head. Add a subtly visible natural shy flush localized symmetrically over the upper cheeks, soft rose warmth with feathered edges; clearly perceptible but light, never cosmetic circles and never a whole-face/base-skin shift. Increase the smile only a little: a small warm fully closed-mouth smile with slightly clearer bilateral corner lift and gentle cheek response, still weaker than EXP_03 natural smile and with no teeth.

Keep the expression adult, natural and bashful. No deep bow, strong turn, head tilt, shoulder hunch, hand near face, wink, pout, lip bite, open mouth, teeth, broad smile, laugh, bright red face, heavy makeup blush, anime styling, childish coyness, seductive/flirtatious performance, sadness, worry, panic or surprise.

Preserve permanent identity and approved Hair-A exactly. Do not reshape eyes/brows/nose/lips/jaw/chin, change age or base skin tone, or beautify. Exact 3:4 front-oriented head-to-upper-chest portrait, 85–105mm-equivalent, neutral gray-white seamless studio and soft even 5200–5600K light. Show only the pink upper portion of the Calibration Outfit one-piece swimsuit. No hands, props, second person, text, logo, watermark, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-13`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared unique project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a099a9-4667-7253-98a6-4e3b55277abd/exec-95cd472b-b892-413e-9f2c-a93cbbffcb53.png` (default duplicate removed after checksum-verified project transfer)
- project_candidate_checksum_sha256: `73f46af06f851b92810d9e77013f23c2b96517f783714a9e8f43d924b943ab7b`
- technical_precheck: PASS. The head has a modest natural downward pitch with a visibly but gently lowered chin, while the face remains close to frontal and shoulders stay level. Both eyes coherently avert downward toward one side. The upper cheeks show a light symmetric soft-rose flush with feathered edges that is visible but not cosmetic or global; base skin tone remains stable. The fully closed-mouth smile is slightly clearer than v001 through modest bilateral corner lift and gentle cheek response, but remains restrained with no teeth or laughter. Identity, Hair-A, neutral studio and visible Calibration Outfit upper portion remain consistent. No v001 pixels, hands, head tilt, deep bow, wedding elements, heavy blush, childish coyness, seductive performance, text or watermark appear.
- promotion_status: promoted unchanged after explicit user approval

## User approval

On 2026-09-13 the user stated: “不错 合格”. The v002 PNG was moved unchanged to the unique approved path and registered as `OWNER_EXP_12_SHY_CANON_001`. Approval covers only the transient restrained shy action: modest downward head pitch, coherent downward side-averted gaze, subtle localized temporary cheek flush, slightly clearer closed-mouth smile and gentle eyelid/cheek response. It does not grant permanent face, base skin tone, hair, outfit, lighting, background or full-release authority. v001 remains rejected.
