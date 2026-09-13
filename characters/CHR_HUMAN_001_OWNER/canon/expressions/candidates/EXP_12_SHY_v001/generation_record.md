# EXP_12_SHY_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.93
identity_md_revision: draft_0.81
asset_id: EXP_12_SHY
candidate_id: EXP_12_SHY_v001
gate: "Gate 5 — Expression Canon (explicit user-authorized next candidate)"
model_tool: "built-in image_gen"
status: USER_REJECTED
approval_status: USER_REJECTED
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
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_12_SHY_v001/EXP_12_SHY_v001.png"
checksum_sha256: "905c7fe164d1b9ae630dbddae8735071b9ae4741fdb15e8781b44bceaa085f21"
qa_status: USER_REJECTED_REVISION_REQUESTED
```

## Authorization and lineage

The user explicitly requested the next planned owner asset after approving EXP_10 and EXP_11. This record authorizes one independent `EXP_12_SHY_v001` candidate constructed in parallel from approved Face, approved Hair-A and one scoped real L0 expression reference. No approved or candidate Expression image, Body asset or shot image is supplied as a pixel input.

## Reference budget and responsibility plan

- Face identity: 1 approved image.
- Hairstyle: 1 approved hair-only scoped image.
- L0 expression motion: 1 limited real image.
- Previous Expression/Body/shot: 0 images.
- Total: 3 images.

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`.
   - authoritative_for: exact approved front identity, permanent skull/face proportions, eyes/brows/nose/lips/jaw/chin, skin-tone appearance, age and eye-level projection.
   - must_not_define: shy motion, Hair-A design, outfit, body, background or lighting artifacts.
2. Image 2 / `OWNER_HAIR_A_01_FRONT_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`; SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`.
   - authoritative_for: approved front Hairstyle-A near-center part, controlled crown, long straight loose dark-brown panels, restrained highlights and tapered length.
   - must_not_define: face, expression, skin, body, outfit, background or lighting.
3. Image 3 / `L0_OWNER_011` — path `characters/CHR_HUMAN_001_OWNER/source/identity/raw/13.jpg`; SHA-256 `5bc0c57d0870a534814125112aef654ace4aac0616610e737559381370717d54`.
   - authoritative_for: slight downward/averted gaze, restrained closed-mouth small smile, gentle shy eyelid/cheek soft-tissue direction.
   - must_not_define: identity, skull/face geometry, head turn or downward head pitch, hand-on-cheek pose, makeup, permanent blush/skin tone, hairstyle, veil, wedding clothing, body, gray backdrop, lighting, resolution or retouching.

## Candidate authority

- authoritative_for if approved: EXP_12 transient restrained shy action—upright head, subtly averted downward gaze, tiny closed-mouth smile, gentle eyelid/cheek response and at most extremely faint temporary cheek warmth.
- must_not_define: permanent face, eye, brow, lip, nose, jaw/chin geometry; permanent skin tone or blush; Hair-A; body; outfit; lighting; background; pose; or other Expressions.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 character-expression calibration candidate `EXP_12_SHY_v001` for one adult woman; exactly one image; status REVIEW_REQUIRED.

Input roles are isolated and parallel. Image 1 is the sole permanent facial-identity authority: preserve exactly the same recognizable adult person, frontal skull and face proportions, natural almond eye anatomy, brow foundation, nose, lips, softly rounded jaw/chin, age, skin-tone appearance and true eye-level projection. Image 2 is hair-only authority: preserve approved front Hairstyle A with short near-center part, controlled crown, long straight loose dark-brown panels, restrained highlights and tapered length. Image 3 is a real L0 expression-motion reference only: use only its slightly downward/averted gaze, restrained closed-mouth small smile and gentle shy eyelid/cheek soft-tissue direction. Never copy Image 3's head turn/downward pitch, hand-on-cheek pose, identity, face shape, makeup, permanent blush/skin tone, hair, veil, clothing, background, light or retouching. Do not use or imitate any generated Expression image.

Primary request: create a natural restrained shy expression in a square front calibration portrait. Keep the head, chin, neck and shoulders upright, level and front-facing. Move only the eyes into a subtle downward gaze angled slightly toward image-right, enough to avoid direct eye contact while keeping both irises naturally positioned and visible. Keep brows relaxed with only a tiny soft lift at the inner portions, not worried or surprised. Form a very small closed-mouth smile with gently lifted corners, much weaker than a normal smile; lips remain fully closed and retain their approved shape. Add a delicate natural softening in the lower eyelids and cheeks. If present, cheek warmth must be extremely faint, localized and temporary-looking, never cosmetic blush and never a general skin-tone shift.

The expression should read as adult shyness or bashful warmth, not childish coyness. No head tilt, bowed head, shoulder hunch, hand near face, hair touching gesture, side pose, wink, pout, lip bite, open mouth, teeth, exaggerated blush, red face, anime styling, flirtatious/seductive performance, sadness, worry, embarrassment panic, surprise, laughter or cartoon acting.

Preserve permanent identity exactly. Do not enlarge or reshape eyes, change eye spacing, redesign brows, reshape nose/lips, shorten the lower face, slim/widen the face, sharpen/lengthen jaw or chin, change age or base skin tone, or apply beauty filtering.

Composition: squarely front-facing at true eye level, neutral upright head and level shoulders, 85–105mm-equivalent perspective. Exact 3:4 portrait from head top through upper chest. Neutral gray-white seamless studio, soft even 5200–5600K low-contrast light and realistic natural skin texture. Where clothing is visible, show only the plain opaque pink upper portion of the established Calibration Outfit one-piece swimsuit. No other garment, hands, props, second person, text, logo, watermark, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-13`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared unique project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a099a9-4667-7253-98a6-4e3b55277abd/exec-0619c13a-3cfa-4a72-bed7-07d3ea81e1b7.png` (default duplicate removed after checksum-verified project transfer)
- project_candidate_checksum_sha256: `905c7fe164d1b9ae630dbddae8735071b9ae4741fdb15e8781b44bceaa085f21`
- technical_precheck: PASS. Head, chin, neck and shoulders remain upright, level and front-facing while both eyes avert subtly downward and toward one side, avoiding direct camera contact without ocular distortion. Brows remain relaxed; the mouth forms a restrained fully closed small smile weaker than a normal smile, with gentle lower-eyelid and cheek softening. The expression reads as adult bashful warmth without bowed/tilted head, hand-to-face pose, pout, lip bite, open mouth, teeth, exaggerated blush, childish coyness, seductive performance, sadness, panic, surprise or laughter. Approved permanent identity, Hair-A, base skin tone, neutral studio and visible pink Calibration Outfit upper portion remain consistent; no wedding makeup, veil, hand, garment or background from the scoped L0 reference is inherited.
- promotion_status: not promoted; explicit user approval required

## User review

On 2026-09-13 the user requested a new version with the head lowered somewhat more, a subtly visible natural blush on the face, and slightly more smile. This v001 raster is `USER_REJECTED`; it must not be used as a v002 pixel input or downstream reference. Only the user's three textual corrections and unchanged source responsibilities carry forward.
