# EXP_15_MOUTH_SLIGHTLY_OPEN_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.60
identity_md_revision: draft_0.49
asset_id: EXP_15_MOUTH_SLIGHTLY_OPEN
candidate_id: EXP_15_MOUTH_SLIGHTLY_OPEN_v001
gate: "Gate 5 — Expression Canon (explicit user-authorized out-of-order candidate)"
model_tool: "built-in image_gen"
status: USER_REJECTED
approval_status: REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
reference_count: 2
previous_ai_expression_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_15_MOUTH_SLIGHTLY_OPEN_v001/EXP_15_MOUTH_SLIGHTLY_OPEN_v001.png"
checksum_sha256: "54b5c0fdd5e8aae89e1bb488914a21d3fd65b65fa5d42e154b747757bdddd6a4"
qa_status: FAIL_USER_DEFINITION_MISMATCH
```

## Authorization and lineage

The user explicitly requested that the final planned Expression asset be generated out of order. This does not mark Gate 4 complete or Gate 5 open as a whole. The candidate is constructed in parallel from two approved scoped L1 Masters; no previous Expression candidate, failed image, shot image, Body image, Hairstyle-B image or L0 expression image is supplied. The approved Face Master remains facial-identity authority; the approved Hair-A front Master supplies only the already approved front hairstyle attributes.

## Reference budget and responsibility plan

- Face identity: 1 image.
- Hairstyle: 1 image.
- L0 expression: 0 images. `OWNER_L0_EXPRESSION_SURPRISED` is intentionally excluded because its open-mouth amplitude and surprised eye/brow tension do not match this subtle expression.
- Body, hosiery material, outfit image, previous candidate and previous shot: 0 images.
- Total: 2 images.

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`.
   - authoritative_for: approved front facial identity, skull and face proportions, eye spacing/shape, brows at rest, nose geometry, lip identity and color, jaw/chin geometry, skin tone, age, true eye-level frontal projection.
   - must_not_define: target mouth opening, final Hairstyle-A length/end details, outfit design, body, background, lighting artifacts.
2. Image 2 / `OWNER_HAIR_A_01_FRONT_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`.
   - authoritative_for: approved eye-level front Hairstyle-A near-center short part, controlled crown, long straight loose face-framing panels, dark-brown restrained highlights, below-chest length and tapered ends.
   - must_not_define: face, nose, skin, expression, lips, jaw/chin, body, outfit, background or lighting.

## Candidate authority

- authoritative_for: `EXP_15_MOUTH_SLIGHTLY_OPEN` only — a subtle, relaxed natural lip separation with minimal jaw opening and anatomically plausible soft-tissue response.
- must_not_define: permanent lip shape, teeth design, skull, nose, eye geometry, brow design, jaw/chin identity, skin tone, age, Hairstyle-A design beyond the approved front scope, body, outfit, lighting or background.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 character-expression calibration candidate `EXP_15_MOUTH_SLIGHTLY_OPEN_v001` for one adult woman; one image only; status REVIEW_REQUIRED.

Input images: Image 1 is the sole facial-identity authority: `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`. Preserve exactly the same recognizable adult person, frontal skull and face proportions, natural eye shape and spacing, relaxed brow shape, nose bridge/tip/alar proportions, permanent lip shape and color, rounded jaw/chin relationship, skin tone and age. Image 2 is hair-only authority: `OWNER_HAIR_A_FRONT_CANON_L1`. Preserve its approved Hairstyle A front attributes—short near-center part, controlled low-to-moderate crown, long straight loose dark-brown face-framing panels, restrained highlights, believable fine strands, complete below-chest length and tapered ends. Image 2 must not influence face, nose, skin, expression, lips or jaw.

Primary request: create the final planned Expression asset: lips naturally and only slightly parted at rest, with a narrow soft opening between the lips and the lower jaw opened by only a few millimeters. The expression is calm and neutral-adjacent, as if just about to speak or breathing quietly. Preserve the person's permanent upper/lower lip geometry; allow only realistic local soft-tissue movement. Keep cheeks relaxed, brows neutral, eyes naturally open and looking directly at camera. No surprise, fear, smile, laugh, anger, concern, pout or seductive expression. Do not drop, lengthen, sharpen, widen or redesign the jaw or chin. No exaggerated open mouth, no broad dark oral cavity, no tongue, and no prominent teeth; at most an indistinct tiny natural glimpse inside the narrow opening.

Composition/framing: squarely front-facing, true eye-level camera, neutral head position, level shoulders, 85–105mm-equivalent portrait perspective. Exact 3:4 vertical portrait, head top through upper chest, head about 65–72% of image height. Keep all outer hair edges and the visible lower hair ends inside the frame with comfortable margin.
Scene/backdrop: neutral light gray/gray-white seamless studio.
Lighting/mood: soft even low-contrast 5200–5600K studio light; neutral technical calibration; realistic skin texture.
Outfit: where clothing is visible, show only the plain opaque pink upper portion of the established Calibration Outfit one-piece swimsuit; no other garment and no exposed cleavage emphasis.
Constraints: expression alone may change from Image 1. Preserve identity, nose size, eyes, brows, face width, jaw/chin geometry, skin tone, age and approved Hairstyle-A front design. Photorealistic natural photograph; no beauty filter, plastic skin, dramatic lighting, text, logo, watermark, props, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-12`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a09467-3db0-70a2-bf86-1fb58ecbbfb6/exec-c8b995cb-252a-45c9-bd5e-ce0b3c935bae.png` (transient source removed after project transfer; no duplicate retained)
- project_candidate_checksum_sha256: `54b5c0fdd5e8aae89e1bb488914a21d3fd65b65fa5d42e154b747757bdddd6a4`
- technical_precheck: PASS. The lips have a narrow natural resting separation with only minimal lower-jaw opening; no broad oral cavity, tongue or prominent teeth. Brows, eyes and cheeks remain neutral-adjacent without surprise, smile or seductive affect. Front identity, nose scale, face width, rounded jaw/chin, age and skin presentation remain visually aligned with the approved Face Master. The visible Hairstyle-A part, crown control, straight dark-brown panels and restrained highlights remain consistent. The image uses a true frontal eye-level technical portrait, neutral studio, and visible pink Calibration Outfit upper portion. The expression crop does not become authority for full hair length or ends; that authority remains with `OWNER_HAIR_A_01_FRONT_CANON_001`.
- promotion_status: not promoted; awaiting explicit user review

## User rejection

On 2026-09-12 the user rejected v001 because the planned expression definition was wrong. The correct EXP_15 requirement is a compound expression: frowning, eyes closed, and mouth open without being wide open. v001 remains a rejected provenance artifact and must not be supplied as pixels to v002 or any downstream generation.
