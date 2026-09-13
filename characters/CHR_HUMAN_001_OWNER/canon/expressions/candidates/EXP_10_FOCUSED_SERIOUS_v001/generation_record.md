# EXP_10_FOCUSED_SERIOUS_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.88
identity_md_revision: draft_0.76
asset_id: EXP_10_FOCUSED_SERIOUS
candidate_id: EXP_10_FOCUSED_SERIOUS_v001
gate: "Gate 5 — Expression Canon (explicit user-authorized next candidate)"
model_tool: "built-in image_gen"
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_10_FOCUSED_SERIOUS_v001/EXP_10_FOCUSED_SERIOUS_v001.png"
checksum_sha256: "6e4a34c690a856751b343710a144e8c60ede10bc0cf5819f398f2f2fb79930d4"
qa_status: PASS_TECHNICAL_PRECHECK
```

## Authorization and lineage

The user approved EXP_09 and explicitly requested the next planned Expression item. `EXP_10_FOCUSED_SERIOUS_v001` will be one independent candidate constructed only from approved Face and Hair masters. No approved or candidate Expression image, Body asset or shot image is supplied as a pixel input.

## Source-coverage review

The current Reference Guide, complete L0 manifest and registered reference sets contain no dedicated reliable focused/serious expression photograph. Annoyed, surprised, downward-looking and smiling photographs are not repurposed. This candidate therefore proposes a conservative text-defined transient action and must remain `REVIEW_REQUIRED` until explicit approval.

## Reference budget and responsibility plan

- Face identity: 1 approved image.
- Hairstyle: 1 approved hair-only scoped image.
- L0 expression motion: 0 images because coverage is absent.
- Previous Expression/Body/shot: 0 images.
- Total: 2 images.

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`.
   - authoritative_for: exact approved front identity, permanent skull/face proportions, eyes/brows/nose/lips/jaw/chin, skin tone, age and eye-level projection.
   - must_not_define: target focused/serious motion, Hair-A design, outfit, body, background or lighting artifacts.
2. Image 2 / `OWNER_HAIR_A_01_FRONT_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`; SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`.
   - authoritative_for: approved front Hairstyle-A near-center part, controlled crown, long straight loose dark-brown panels, restrained highlights and tapered length.
   - must_not_define: face, expression, eye/brow/mouth geometry, skin, body, outfit, background or lighting.

## Candidate authority

- authoritative_for if approved: EXP_10 transient calm, task-oriented focused/serious action—steady direct gaze, extremely slight eyelid engagement, nearly neutral brows with only minimal convergence/reduced relaxation, naturally closed unpressed lips and relaxed level mouth corners/jaw.
- must_not_define: permanent face, eye, brow, lip, nose, jaw/chin geometry; emotional annoyance, anger, sadness or worry; skin; age; Hair-A; body; outfit; lighting; background; or other Expressions.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 character-expression calibration candidate `EXP_10_FOCUSED_SERIOUS_v001` for one adult woman; exactly one image; status REVIEW_REQUIRED.

Input roles are strictly isolated and parallel. Image 1 is the sole facial-identity authority: preserve exactly the same recognizable adult person, frontal skull and face proportions, permanent natural almond eye shape and spacing, brow foundation, nose, lips, softly rounded jaw and chin, age, skin-tone appearance and true eye-level projection. Image 2 is hair-only authority: preserve the approved front Hairstyle A with short near-center part, controlled crown, long straight loose dark-brown face-framing panels, restrained highlights and tapered length. No real L0 source reliably covers focused/serious motion, so create only the conservative transient action described below. Do not use, imitate or infer pixels from any generated Expression image.

Primary request: create calm, stable, task-oriented focus, as if she is carefully attending to a precise task immediately beyond the camera. Keep a direct, steady, clearly focused gaze. Preserve the approved eye size and almond geometry; engage or tighten the upper and lower eyelids only extremely slightly, without squinting. Keep both brows almost neutral and balanced, allowing only minimal inward convergence or a tiny reduction of relaxed softness; do not create a visible frown. Keep lips naturally closed with normal soft contact, never pressed or thinned. Keep mouth corners level and jaw relaxed. The result should read as serious and attentive but emotionally neutral.

No impatience, irritation, hostility, anger, sadness, worry, surprise, confusion, suspicion, sarcasm, stern scowl, deep glabellar furrow, lowered brows, pressed or thinned lips, clenched jaw, side-eye, smile or head tilt. This must be clearly distinct from EXP_08: no annoyed eye tension and no lip pressure. It must also be distinct from EXP_13: no visible brow-frown as the core action.

Preserve permanent identity exactly. Expression motion is limited to a steady attentive gaze, extremely slight eyelid engagement and nearly neutral brow tone. Do not permanently redesign eyebrows, enlarge or reshape eyes, change gaze anatomy, reshape lips/nose, shorten the lower face, slim or widen the face, sharpen/lengthen jaw or chin, change age or skin tone, or apply beauty filtering.

Composition: squarely front-facing at true eye level, neutral upright head and level shoulders, 85–105mm-equivalent perspective. Exact 3:4 portrait from head top through upper chest. Neutral gray-white seamless studio, soft even 5200–5600K low-contrast light and realistic natural skin texture. Where clothing is visible, show only the plain opaque pink upper portion of the established Calibration Outfit one-piece swimsuit. No other garment, hands, props, second person, text, logo, watermark, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-13`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a095f8-d792-7540-92a2-d60cb9777c57/exec-90987e7d-4b55-4416-9176-f320c54ff935.png` (temporary default duplicate removed after checksum-verified project transfer)
- project_candidate_checksum_sha256: `6e4a34c690a856751b343710a144e8c60ede10bc0cf5819f398f2f2fb79930d4`
- technical_precheck: PASS. The gaze is direct, stable and attentive; approved almond-eye geometry is retained with only extremely slight lid engagement. Brows remain nearly neutral without a visible frown. Lips are naturally closed with soft contact, level corners and a relaxed jaw. The result reads as calm task-oriented seriousness without impatience, anger, sadness, worry, surprise, confusion, suspicion, scowl or sarcasm. It is distinct from EXP_08 because there is no annoyed lid tension or lip pressure, and distinct from EXP_13 because brow-frowning is not the core action. Approved front identity, Hair-A, upright eye-level composition, neutral studio and visible pink Calibration Outfit upper portion remain consistent. No hands, props, text, watermark or multiple views appear.
- promotion_status: not promoted; explicit user approval required
