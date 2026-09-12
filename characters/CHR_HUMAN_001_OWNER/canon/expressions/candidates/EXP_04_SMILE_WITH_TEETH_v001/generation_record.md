# EXP_04_SMILE_WITH_TEETH_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.71
identity_md_revision: draft_0.59
asset_id: EXP_04_SMILE_WITH_TEETH
candidate_id: EXP_04_SMILE_WITH_TEETH_v001
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
  - OWNER_L0_EXPRESSION_SMILE_TEETH
reference_count: 3
previous_ai_expression_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_04_SMILE_WITH_TEETH_v001/EXP_04_SMILE_WITH_TEETH_v001.png"
checksum_sha256: "f116b57182e6fc656d8f3d5c883366a67054f1b298c105103daa90f4046bb2cd"
pixel_storage_status: "PROJECT_CANDIDATE_UNIQUE_MASTER; BUILT_IN_TEMP_REMOVED"
qa_status: USER_REJECTED_MISSING_RIGHT_CANINE_AND_DIMPLES
```

## Authorization and lineage

The user requested generation of the next planned Expression component, `EXP_04_SMILE_WITH_TEETH`. This is one new candidate only. It is reconstructed in parallel from the scoped approved identity and hair Masters plus the first and strongest real L0 image in the registered smile/teeth set. No approved or candidate Expression image, failed image, Body image or shot image is supplied.

## Reference budget and responsibility plan

- Face identity: 1 approved image.
- Hairstyle: 1 approved hair-only scoped image.
- L0 expression/teeth display: 1 real image selected from a registered set whose maximum is 2.
- Body, outfit image, hosiery material, previous candidate and previous shot: 0 images.
- Total: 3 images.

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`.
   - authoritative_for: exact approved front identity, skull/face proportions, permanent eyes/brows/nose/lips/jaw/chin, skin tone, age and true eye-level projection.
   - must_not_define: target smile motion or tooth exposure, final Hair-A length/end design, outfit, body, background or lighting artifacts.
2. Image 2 / `OWNER_HAIR_A_01_FRONT_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`; SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`.
   - authoritative_for: approved front Hairstyle-A short near-center part, controlled crown, long straight loose panels, dark-brown restrained highlights and tapered length.
   - must_not_define: face, expression, teeth, nose, lips, jaw/chin, skin, body, outfit, background or lighting.
3. Image 3 / `L0_OWNER_008` — path `characters/CHR_HUMAN_001_OWNER/source/identity/raw/10.jpg`; SHA-256 `7efc7fff229c3480242501a63b5b2ebf93d20ed9070baa869b38bdd973eabe2c`.
   - authoritative_for: real same-person natural tooth-showing smile dynamics, including lip-corner spread/lift, cheek and lower-eyelid response, smile-line behavior, and restrained upper-teeth exposure pattern within this expression.
   - must_not_define: permanent identity or dental Canon outside this expression, skull/face proportions, head tilt, eye/nose/jaw/chin geometry, skin tone, styled makeup, wavy hair, clothing, blue background, directional lighting or retouching.

## Candidate authority

- authoritative_for if approved: EXP_04 transient natural tooth-showing smile only—balanced lip-corner spread/lift, natural cheek and lower-eyelid response, and restrained principally upper-teeth display.
- must_not_define: permanent tooth anatomy or color outside the expression, permanent lip/eye/brow geometry, skull, nose, jaw/chin identity, skin tone, age, Hair-A design beyond its approved source, body, outfit, lighting or background.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 character-expression calibration candidate `EXP_04_SMILE_WITH_TEETH_v001` for one adult woman; exactly one image; status REVIEW_REQUIRED.

Input images: Image 1 is the sole facial-identity authority. Preserve exactly the same recognizable adult person, frontal skull/face proportions, eye spacing and permanent eye shape, permanent brow design, nose bridge/tip/alar proportions, permanent lip foundation and color, softly rounded jaw/chin relationship, skin-tone appearance and age. Image 2 is hair-only authority: preserve its approved front Hairstyle A, including the short near-center part, controlled low-to-moderate crown, long straight loose dark-brown face-framing panels, restrained highlights, fine strands and complete tapered length. Image 3 is the registered real same-person smile/teeth reference and may define only natural tooth-showing smile dynamics: coordinated bilateral lip-corner lift and spread, cheek rise, gentle lower-eyelid response, smile line, and restrained predominantly upper-teeth exposure. Do not copy Image 3's head tilt, permanent face geometry, styled makeup, wavy hairstyle, garment, blue background, lighting or retouched finish.

Primary request: create a natural, friendly, medium-intensity smile with teeth. Lift and spread both lip corners evenly, open the lips only enough to show a natural row of upper teeth, with at most a very small amount of lower teeth. Keep the jaw opening modest. Let the cheeks rise naturally and the lower eyelids warm gently without a hard squint. Keep brows relaxed and gaze calm/direct. The smile must be more open and expressive than EXP_03's closed-mouth smile but clearly below a broad grin or happy laugh.

Teeth must look anatomically plausible and naturally aligned for this real adult person, with normal off-white enamel rather than perfect bright-white cosmetic veneers. Show no dominant gums, no duplicated/fused/missing teeth, no uniform rectangular piano-key teeth, no extra rows, no distorted mouth interior, and no emphasized tongue. This Expression candidate may define the visible exposure pattern only; it must not invent a permanent dental Canon.

Preserve permanent identity exactly. Expression movement is limited to lips/lip corners, cheeks, gentle lower-eyelid response and modest jaw articulation. Do not enlarge the permanent mouth, plump or thin the lips, enlarge the eyes, reshape or raise the brows, shrink the nose, slim/widen the face, sharpen/lengthen the jaw or chin, or change age/skin tone. No asymmetrical smirk, seductive affect, grimace, surprise, shouting, laughing, exaggerated gum display, beauty filter or retouching.

Composition: squarely front-facing at true eye level, neutral upright head, level shoulders, 85–105mm-equivalent perspective. Exact 3:4 portrait from head top through upper chest, consistent with the Face/Expression calibration series. Neutral gray-white seamless studio and soft even 5200–5600K low-contrast light. Realistic natural skin texture. Where clothing is visible, show only the plain opaque pink upper portion of the established Calibration Outfit one-piece swimsuit. No other garment, props, text, logo, watermark, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-12`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a095f8-d792-7540-92a2-d60cb9777c57/exec-70803d61-2cac-4cb3-9646-fd3679303aff.png` (transient default output removed after checksum-verified project transfer; no duplicate retained)
- project_candidate_checksum_sha256: `f116b57182e6fc656d8f3d5c883366a67054f1b298c105103daa90f4046bb2cd`
- technical_precheck: PASS. The smile is natural, friendly and medium in intensity, with balanced lip-corner lift/spread, natural cheek rise and warm lower-eyelid response. The mouth opens modestly and displays principally the upper teeth, without dominant gums or laugh-level opening. Visible teeth are plausible off-white, with no obvious duplicated, fused, missing, uniformly rectangular or extra-row anatomy and no emphasized tongue. The expression is clearly more open than EXP_03 while remaining below a broad grin or happy laugh. Approved front identity relationships, permanent nose/jaw/chin geometry, adult age and skin-tone appearance remain visually consistent. Visible front Hair-A structure, true eye-level camera, neutral studio and pink Calibration Outfit upper portion also remain consistent.
- promotion_status: not promoted; user approval required

## User review — 2026-09-12

- decision: `USER_REJECTED`
- correction: the candidate omitted the subject's naturally prominent anatomical-right upper canine (image-left in a frontal view) and the natural dimple/smile-indentation response visible in real source `L0_OWNER_001` (`2.jpg`).
- lineage rule: this raster is forbidden as a downstream reference and forbidden as an input to v002 or any later L1 regeneration.
- technical note: the earlier AI precheck is superseded by the user's identity-specific correction.
