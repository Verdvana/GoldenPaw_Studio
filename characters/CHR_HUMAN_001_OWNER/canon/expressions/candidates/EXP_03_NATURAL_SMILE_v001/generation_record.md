# EXP_03_NATURAL_SMILE_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.68
identity_md_revision: draft_0.56
asset_id: EXP_03_NATURAL_SMILE
candidate_id: EXP_03_NATURAL_SMILE_v001
gate: "Gate 5 — Expression Canon (explicit user-authorized next candidate)"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
  - OWNER_L0_EXPRESSION_NATURAL_SMILE_SINGLE
reference_count: 3
previous_ai_expression_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_03_NATURAL_SMILE_v001/EXP_03_NATURAL_SMILE_v001.png"
checksum_sha256: "cf1a904cca92ae3640f28f26e71869d520a60d5b2d050dfca8cf8dab8474df59"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/approved/EXP_03_NATURAL_SMILE/OWNER_EXP_03_NATURAL_SMILE_CANON_001.png"
current_promoted_checksum_sha256: "cf1a904cca92ae3640f28f26e71869d520a60d5b2d050dfca8cf8dab8474df59"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user requested generation of the next planned Expression component, `EXP_03_NATURAL_SMILE`. This is one new candidate only. It is reconstructed in parallel from the scoped approved identity and hair Masters plus one real L0 soft-tissue reference. No EXP_01, EXP_02, EXP_15, prior Expression candidate, failed image, Body image or shot image is supplied.

## Reference budget and responsibility plan

- Face identity: 1 approved image.
- Hairstyle: 1 approved hair-only scoped image.
- L0 expression: 1 real image.
- Body, outfit image, hosiery material, previous candidate and previous shot: 0 images.
- Total: 3 images.

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`.
   - authoritative_for: exact approved front identity, skull/face proportions, permanent eyes/brows/nose/lips/jaw/chin, skin tone, age and true eye-level projection.
   - must_not_define: target smile motion, final Hair-A length/end design, outfit, body, background or lighting artifacts.
2. Image 2 / `OWNER_HAIR_A_01_FRONT_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`; SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`.
   - authoritative_for: approved front Hairstyle-A short near-center part, controlled crown, long straight loose panels, dark-brown restrained highlights and tapered length.
   - must_not_define: face, expression, nose, lips, jaw/chin, skin, body, outfit, background or lighting.
3. Image 3 / `L0_OWNER_007` — path `characters/CHR_HUMAN_001_OWNER/source/identity/raw/9.jpg`; SHA-256 `00213373bd3338a89d40ab42893b3ad2327c07305d93103e8edd8f6c29a42f6d`.
   - authoritative_for: real same-person natural smile direction limited to bilateral lip-corner lift and natural cheek/lower-eyelid response.
   - must_not_define: visible teeth, mouth opening, exact identity geometry, lens-neutral proportions, eye size/shape, nose, jaw/chin, skin tone, hairstyle, clothing, mirror/frame, green color cast, lighting or background.

`OWNER_L0_EXPRESSION_NATURAL_SMILE_SINGLE` is a candidate-local declared set resolved from the source manifest and nearest `REFERENCE_GUIDE.md`; it contains only `L0_OWNER_007`. It does not modify the global registry before the candidate is reviewed.

## Candidate authority

- authoritative_for if approved: EXP_03 transient natural closed-mouth smile only—clear balanced lip-corner lift, moderate natural cheek rise and warm lower-eyelid response, stronger than EXP_02 but below a tooth-showing smile.
- must_not_define: permanent lip/eye/brow geometry, teeth, skull, nose, jaw/chin identity, skin tone, age, Hair-A design beyond its approved source, body, outfit, lighting or background.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 character-expression calibration candidate `EXP_03_NATURAL_SMILE_v001` for one adult woman; exactly one image; status REVIEW_REQUIRED.

Input images: Image 1 is the sole facial-identity authority. Preserve exactly the same recognizable adult person, frontal skull/face proportions, eye spacing and permanent eye shape, permanent brow design, nose bridge/tip/alar proportions, permanent upper/lower lip geometry and color, softly rounded jaw/chin relationship, skin-tone appearance and age. Image 2 is hair-only authority: preserve its approved front Hairstyle A, including the short near-center part, controlled low-to-moderate crown, long straight loose dark-brown face-framing panels, restrained highlights, fine strands and complete tapered length. Image 3 is a real same-person expression reference and may define only the natural direction and coordination of bilateral lip-corner lift, moderate cheek rise and gentle lower-eyelid response. Do not copy Image 3's visible teeth, open mouth, close-camera geometry, eye rendering, hairstyle, garment, mirror/frame, green color cast, lighting or background.

Primary request: starting from the approved neutral facial identity, create a clear, natural, friendly closed-mouth smile. Raise both lip corners naturally and symmetrically to a moderate but unforced degree. Keep the lips fully closed with no teeth and no mouth opening. Let the cheeks lift naturally and let the lower eyelids respond gently, creating warm eyes without a hard squint. Keep brows relaxed. The smile must be visibly stronger and more complete than a barely perceptible subtle smile, yet remain clearly below a tooth-showing smile, broad grin or laugh.

Preserve permanent identity exactly. Expression movement is limited to lip corners, adjacent lip soft tissue, cheeks and gentle lower-eyelid response. Do not widen the permanent mouth, plump or thin the lips, deepen nasolabial folds excessively, enlarge the eyes, reshape or raise the brows, shrink the nose, slim/widen the face, sharpen/lengthen the jaw or chin, or change age/skin tone. No teeth, mouth opening, asymmetrical smirk, pursed lips, duck face, coy/seductive affect, sadness, frown, exaggerated dimples, beauty filter or retouching.

Composition: squarely front-facing at true eye level, neutral upright head, level shoulders, 85–105mm-equivalent perspective. Exact 3:4 portrait from head top through upper chest, consistent with the Face/Expression calibration series. Neutral gray-white seamless studio and soft even 5200–5600K low-contrast light. Realistic natural skin texture. Where clothing is visible, show only the plain opaque pink upper portion of the established Calibration Outfit one-piece swimsuit. No other garment, props, text, logo, watermark, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-12`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a095f8-d792-7540-92a2-d60cb9777c57/exec-4cb0ca11-041c-4fa8-8c71-2cdde1ef2587.png` (transient default output removed after checksum-verified project transfer; no duplicate retained)
- project_candidate_checksum_sha256: `cf1a904cca92ae3640f28f26e71869d520a60d5b2d050dfca8cf8dab8474df59`
- technical_precheck: PASS. Lips remain fully closed with no teeth or mouth interior. Both lip corners rise clearly and evenly, the cheeks lift naturally, and the lower eyelids respond warmly without a hard squint. The smile reads more complete than EXP_02's barely subtle lift while remaining below a tooth-showing smile, broad grin or laugh. Brows stay relaxed and gaze remains calm/direct. Approved front identity relationships, permanent nose/lip/jaw/chin geometry, adult age and skin-tone appearance remain visually consistent. Visible front Hair-A structure, true eye-level camera, neutral studio and pink Calibration Outfit upper portion also remain consistent. Hair length extends beyond the Expression crop but is contextual and does not gain new authority.
- promotion_status: promoted unchanged after explicit user approval

## User approval

On 2026-09-12 the user stated: “可以，登记吧”. The candidate PNG was moved unchanged to the unique approved path and registered as `OWNER_EXP_03_NATURAL_SMILE_CANON_001`. Approval covers only the transient natural closed-mouth smile: balanced lip-corner lift, moderate cheek rise and warm lower-eyelid response. It does not grant permanent face, teeth, hair, outfit, lighting, background or full-release authority.
