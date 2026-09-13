# EXP_07_CONFUSED_CURIOUS_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.81
identity_md_revision: draft_0.69
asset_id: EXP_07_CONFUSED_CURIOUS
candidate_id: EXP_07_CONFUSED_CURIOUS_v001
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
reference_count: 2
l0_expression_reference_count: 0
previous_ai_expression_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_07_CONFUSED_CURIOUS_v001/EXP_07_CONFUSED_CURIOUS_v001.png"
checksum_sha256: "4fa6efb6c9beb14769112db93576928e96856e06b54f31a73f2686170f7351e4"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/approved/EXP_07_CONFUSED_CURIOUS/OWNER_EXP_07_CONFUSED_CURIOUS_CANON_001.png"
current_promoted_checksum_sha256: "4fa6efb6c9beb14769112db93576928e96856e06b54f31a73f2686170f7351e4"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user explicitly approved EXP_06 and requested the next planned item. `EXP_07_CONFUSED_CURIOUS_v001` is one independent candidate constructed from the approved Face and Hair masters. EXP_05 remains unapproved; EXP_05, EXP_06, all other generated Expression images, Body assets and shot images are excluded as pixel inputs.

## Source-coverage review

The complete L0 identity folder and `SOURCE_MANIFEST.md` were re-opened because no named Reference Set covers confused/curious motion. Available L0 expressions cover neutral, smiles, laughter, surprise, closed eyes and downward-looking states, but none reliably shows a confused/curious expression. No mismatched L0 expression image is attached. This candidate therefore proposes a conservative text-defined transient expression; it does not establish any identity fact unless the user explicitly approves it.

## Reference budget and responsibility plan

- Face identity: 1 approved image.
- Hairstyle: 1 approved hair-only scoped image.
- L0 expression motion: 0 images because coverage is absent.
- Previous Expression/Body/shot: 0 images.
- Total: 2 images.

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`.
   - authoritative_for: exact approved front identity, permanent skull/face proportions, eyes/brows/nose/lips/jaw/chin, skin tone, age and eye-level projection.
   - must_not_define: target confused/curious motion, Hair-A length/end design, outfit, body, background or lighting artifacts.
2. Image 2 / `OWNER_HAIR_A_01_FRONT_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`; SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`.
   - authoritative_for: approved front Hairstyle-A near-center part, controlled crown, long straight loose dark-brown panels, restrained highlights and tapered length.
   - must_not_define: face, expression, eye/brow/mouth geometry, skin, body, outfit, background or lighting.

## Candidate authority

- authoritative_for if approved: EXP_07 transient confused/curious action—restrained asymmetric brow activation, attentive questioning gaze and a neutral closed or barely parted mouth.
- must_not_define: permanent face, eye, brow, lip, nose, jaw/chin geometry; teeth; dimples; skin; age; Hair-A; body; outfit; lighting; background; or other Expressions.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 character-expression calibration candidate `EXP_07_CONFUSED_CURIOUS_v001` for one adult woman; exactly one image; status REVIEW_REQUIRED.

Input roles are strictly isolated and parallel. Image 1 is the sole facial-identity authority: preserve exactly the same recognizable adult person, frontal skull/face proportions, permanent natural eye shape and spacing, brow foundation, nose, lip foundation, softly rounded jaw and chin, age, skin-tone appearance and true eye-level projection. Image 2 is hair-only authority: preserve the approved front Hairstyle A with short near-center part, controlled crown, long straight loose dark-brown face-framing panels, restrained highlights and tapered length. No L0 source reliably covers confused/curious motion, so construct only the conservative transient expression described below. Do not use, imitate or infer pixels from EXP_05, EXP_06 or any generated Expression image.

Primary request: create a natural, restrained and immediately readable confused/curious expression. Add small controlled brow asymmetry: raise the eyebrow on the image-right side moderately but naturally, while the opposite inner brow lowers and draws inward only slightly. Keep the asymmetry subtle enough to remain realistic and preserve both permanent brow shapes. The eyes stay their real approved size and almond shape, open near neutral with focused questioning attention directly toward the camera; no exaggerated widening or squinting. Keep the lips naturally closed or separated by only a hairline, with relaxed neutral corners and no visible teeth. The combined expression should feel like the subject is quietly trying to understand something, interested but uncertain.

Keep the head upright, level and squarely front-facing; do not use a head tilt, neck tilt or shoulder tilt to manufacture curiosity. Do not make the result read as surprise, fear, anger, mild annoyance, suspicion, sadness, contempt, sarcasm, amusement, smiling or laughter. No cartoonishly high single eyebrow, both brows raised, deep glabellar furrow, strong forehead wrinkles, wide round eyes, crossed eyes, side-eye, nose wrinkle, lip curl, crooked mouth, pout, smirk or grimace.

Preserve permanent identity exactly. Expression movement is limited to restrained brow/forehead activation, subtle eyelid attention and almost-neutral lips. Do not permanently redesign eyebrows, enlarge or reshape eyes, change gaze anatomy, reshape lips or nose, slim or widen the face, sharpen or lengthen the jaw/chin, change age or skin tone, add dimples in a non-smiling state, or apply beauty filtering.

Composition: squarely front-facing at true eye level, neutral upright head and level shoulders, 85–105mm-equivalent perspective. Exact 3:4 portrait from head top through upper chest. Neutral gray-white seamless studio, soft even 5200–5600K low-contrast light and realistic natural skin texture. Where clothing is visible, show only the plain opaque pink upper portion of the established Calibration Outfit one-piece swimsuit. No other garment, hands, props, second person, text, logo, watermark, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-13`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a095f8-d792-7540-92a2-d60cb9777c57/exec-a9781e8d-72cc-4a4b-920a-1d9b6c80760e.png` (transient default output removed after checksum-verified project transfer; no duplicate retained)
- project_candidate_checksum_sha256: `4fa6efb6c9beb14769112db93576928e96856e06b54f31a73f2686170f7351e4`
- technical_precheck: PASS. The image-right eyebrow rises moderately while the opposite inner brow draws slightly inward/down, creating restrained natural asymmetry. Both eyes preserve their approved almond shape and near-neutral opening while the direct gaze reads as questioning attention. Lips remain naturally closed with neutral corners. The head stays upright and squarely front-facing; the result does not read as surprise, anger, annoyance, sadness, smirk or cartoon confusion. Approved front identity relationships, Hair-A, eye-level composition, neutral studio and the visible pink Calibration Outfit upper portion remain consistent. No hands, props, text, watermark or multiple views appear.
- promotion_status: promoted unchanged after explicit user approval

## User approval

On 2026-09-13 the user stated: “很好，审核通过。之前生成的05也审核通过”. The candidate PNG was moved unchanged to the unique approved path and registered as `OWNER_EXP_07_CONFUSED_CURIOUS_CANON_001`. Approval covers only the transient restrained confused/curious action: moderate image-right eyebrow elevation, slight opposite inner-brow contraction, attentive questioning gaze and neutral closed mouth. It does not grant permanent face/brow/eye/lip, hair, outfit, lighting, background or full-release authority; the lack of a matching L0 confused/curious expression source remains recorded.
