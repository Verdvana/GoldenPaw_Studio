# EXP_08_MILDLY_ANNOYED_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.84
identity_md_revision: draft_0.72
asset_id: EXP_08_MILDLY_ANNOYED
candidate_id: EXP_08_MILDLY_ANNOYED_v001
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_08_MILDLY_ANNOYED_v001/EXP_08_MILDLY_ANNOYED_v001.png"
checksum_sha256: "416b72c35284ccb9f02fc30c42e26bf407a03dadb8449f8c1231b0b3da09c2af"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/approved/EXP_08_MILDLY_ANNOYED/OWNER_EXP_08_MILDLY_ANNOYED_CANON_001.png"
current_promoted_checksum_sha256: "416b72c35284ccb9f02fc30c42e26bf407a03dadb8449f8c1231b0b3da09c2af"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user requested the next planned Expression item after EXP_05 and EXP_07 were approved. `EXP_08_MILDLY_ANNOYED_v001` is one independent candidate constructed only from approved Face and Hair masters. No approved or candidate Expression image, Body asset or shot image is supplied as a pixel input.

## Source-coverage review

The current Reference Guide, complete L0 manifest and registered reference sets contain no reliable mildly-annoyed expression photograph. Smile, laugh, surprise, closed-eye and downward-looking images are not repurposed. This candidate therefore proposes a conservative text-defined transient action; it establishes no identity fact and is not Canon unless explicitly approved.

## Reference budget and responsibility plan

- Face identity: 1 approved image.
- Hairstyle: 1 approved hair-only scoped image.
- L0 expression motion: 0 images because coverage is absent.
- Previous Expression/Body/shot: 0 images.
- Total: 2 images.

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`.
   - authoritative_for: exact approved front identity, permanent skull/face proportions, eyes/brows/nose/lips/jaw/chin, skin tone, age and eye-level projection.
   - must_not_define: target mildly-annoyed motion, Hair-A design, outfit, body, background or lighting artifacts.
2. Image 2 / `OWNER_HAIR_A_01_FRONT_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`; SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`.
   - authoritative_for: approved front Hairstyle-A near-center part, controlled crown, long straight loose dark-brown panels, restrained highlights and tapered length.
   - must_not_define: face, expression, eye/brow/mouth geometry, skin, body, outfit, background or lighting.

## Candidate authority

- authoritative_for if approved: EXP_08 transient mildly-annoyed action—small bilateral inner-brow tension, slightly narrowed eyelids, restrained impatient direct gaze and gently pressed closed lips.
- must_not_define: permanent face, eye, brow, lip, nose, jaw/chin geometry; teeth; skin; age; Hair-A; body; outfit; lighting; background; or other Expressions.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 character-expression calibration candidate `EXP_08_MILDLY_ANNOYED_v001` for one adult woman; exactly one image; status REVIEW_REQUIRED.

Input roles are strictly isolated and parallel. Image 1 is the sole facial-identity authority: preserve exactly the same recognizable adult person, frontal skull and face proportions, permanent natural eye shape and spacing, brow foundation, nose, lips, softly rounded jaw and chin, age, skin-tone appearance and true eye-level projection. Image 2 is hair-only authority: preserve the approved front Hairstyle A with short near-center part, controlled crown, long straight loose dark-brown face-framing panels, restrained highlights and tapered length. No real L0 source reliably covers mild annoyance, so create only the conservative transient action described below. Do not use, imitate or infer pixels from any generated Expression image.

Primary request: create a natural, restrained, everyday mildly annoyed expression—clearly readable but low intensity. Draw both inner brows only slightly inward and downward, producing minimal controlled tension without a deep vertical furrow. Narrow both eyelids subtly while preserving the approved permanent almond-eye shape and size. Keep the gaze directly toward the camera with a quiet hint of impatience, not hostility. Keep lips naturally closed and gently pressed together, with corners nearly level or only imperceptibly lowered; no visible teeth. Cheeks and jaw remain relaxed. The overall feeling is a small moment of displeasure, not anger.

This must be weaker than EXP_11_ANGRY and distinct from EXP_10_FOCUSED_SERIOUS and the retired slight-frown design: include the combination of slight eyelid narrowing plus restrained lip pressing, not merely concentration and not merely a brow frown. Keep the head upright, level and squarely front-facing. No scowl, glare, strong brow lowering, deep glabellar lines, nostril flare, nose wrinkle, jaw clench, teeth, sneer, lip curl, crooked mouth, pout, eye roll, side-eye, contempt, disgust, sarcasm, sadness, worry, smile, surprise or cartoon annoyance.

Preserve permanent identity exactly. Expression motion is limited to small inner-brow tension, subtle eyelid narrowing and mild closed-lip pressure. Do not permanently redesign eyebrows, shrink or reshape eyes, change gaze anatomy, reshape lips/nose, slim or widen the face, sharpen or lengthen the jaw/chin, change age or skin tone, or apply beauty filtering.

Composition: squarely front-facing at true eye level, neutral upright head and level shoulders, 85–105mm-equivalent perspective. Exact 3:4 portrait from head top through upper chest. Neutral gray-white seamless studio, soft even 5200–5600K low-contrast light and realistic natural skin texture. Where clothing is visible, show only the plain opaque pink upper portion of the established Calibration Outfit one-piece swimsuit. No other garment, hands, props, second person, text, logo, watermark, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-13`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a095f8-d792-7540-92a2-d60cb9777c57/exec-a39a5824-f8a1-4f09-8b11-5b2f4b3581d5.png` (transient default output removed after checksum-verified project transfer; no duplicate retained)
- project_candidate_checksum_sha256: `416b72c35284ccb9f02fc30c42e26bf407a03dadb8449f8c1231b0b3da09c2af`
- technical_precheck: PASS. Both inner brows draw slightly inward/down with shallow restrained tension; eyelids narrow subtly while preserving approved almond-eye geometry. The direct gaze reads as mildly impatient rather than hostile. Lips remain naturally closed with light pressure and near-level corners; cheeks and jaw remain relaxed. The result is clearly weaker than anger and does not read as focused effort, simple brow-only frown, sadness, contempt, disgust or sarcasm. Approved front identity relationships, Hair-A, upright eye-level composition, neutral studio and visible pink Calibration Outfit upper portion remain consistent. No hands, props, text, watermark or multiple views appear.
- promotion_status: promoted unchanged after explicit user approval

## User approval

On 2026-09-13 the user stated: “合格，登记并开始下一项”. The candidate PNG was moved unchanged to the unique approved path and registered as `OWNER_EXP_08_MILDLY_ANNOYED_CANON_001`. Approval covers only the transient low-intensity mild-annoyance action: small inner-brow tension, subtle eyelid narrowing, restrained impatient gaze and gently pressed closed lips. It does not grant permanent face, hair, outfit, lighting, background or full-release authority.
