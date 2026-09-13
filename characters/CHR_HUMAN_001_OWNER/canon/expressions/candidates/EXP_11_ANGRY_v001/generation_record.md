# EXP_11_ANGRY_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.90
identity_md_revision: draft_0.78
asset_id: EXP_11_ANGRY
candidate_id: EXP_11_ANGRY_v001
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_11_ANGRY_v001/EXP_11_ANGRY_v001.png"
checksum_sha256: "b7b051918515fe79db326cf145d4db3fa587b333127506d604be3a834134dec0"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/approved/EXP_11_ANGRY/OWNER_EXP_11_ANGRY_CANON_001.png"
current_promoted_checksum_sha256: "b7b051918515fe79db326cf145d4db3fa587b333127506d604be3a834134dec0"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user requested the next planned owner asset, authorizing one independent `EXP_11_ANGRY_v001` candidate. `EXP_10_FOCUSED_SERIOUS_v001` remains unapproved and is not supplied. No approved or candidate Expression image, Body asset or shot image is supplied as a pixel input.

## Source-coverage review

The current Reference Guide, complete L0 manifest and registered reference sets contain no dedicated reliable angry-expression photograph. Mild-annoyance, neutral, surprised, smiling and downward-looking images are not repurposed. This candidate therefore proposes a conservative text-defined transient angry action and must remain `REVIEW_REQUIRED` until explicit approval.

## Reference budget and responsibility plan

- Face identity: 1 approved image.
- Hairstyle: 1 approved hair-only scoped image.
- L0 expression motion: 0 images because coverage is absent.
- Previous Expression/Body/shot: 0 images.
- Total: 2 images.

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`.
   - authoritative_for: exact approved front identity, permanent skull/face proportions, eyes/brows/nose/lips/jaw/chin, skin-tone appearance, age and eye-level projection.
   - must_not_define: target angry motion, Hair-A design, outfit, body, background or lighting artifacts.
2. Image 2 / `OWNER_HAIR_A_01_FRONT_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`; SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`.
   - authoritative_for: approved front Hairstyle-A near-center part, controlled crown, long straight loose dark-brown panels, restrained highlights and tapered length.
   - must_not_define: face, expression, eye/brow/mouth geometry, skin, body, outfit, background or lighting.

## Candidate authority

- authoritative_for if approved: EXP_11 transient clear but controlled anger—bilateral inner brows drawn inward and downward, natural glabellar tension, narrowed direct angry gaze, firmly closed gently pressed lips, and mild jaw tension.
- must_not_define: permanent face, eye, brow, lip, nose, nostril, jaw/chin geometry; rage, shouting, teeth, hatred or threat; skin; age; Hair-A; body; outfit; lighting; background; or other Expressions.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 character-expression calibration candidate `EXP_11_ANGRY_v001` for one adult woman; exactly one image; status REVIEW_REQUIRED.

Input roles are strictly isolated and parallel. Image 1 is the sole facial-identity authority: preserve exactly the same recognizable adult person, frontal skull and face proportions, permanent natural almond eye shape and spacing, brow foundation, nose, lips, softly rounded jaw and chin, age, skin-tone appearance and true eye-level projection. Image 2 is hair-only authority: preserve the approved front Hairstyle A with short near-center part, controlled crown, long straight loose dark-brown face-framing panels, restrained highlights and tapered length. No real L0 source reliably covers anger, so create only the controlled transient action described below. Do not use, imitate or infer pixels from any generated Expression image.

Primary request: create a clearly readable but controlled angry expression, stronger than mild annoyance and still realistic. Draw both inner eyebrows inward and downward with moderate natural glabellar tension, while preserving the permanent brow foundation. Narrow the upper and lower eyelids moderately around a direct, steady angry gaze without changing the approved almond eye size or anatomy. Keep the mouth fully closed; press the lips together moderately with level-to-slightly-lowered corners, without thinning or reshaping them. Add only mild believable jaw and lower-face tension; keep the head upright and shoulders level.

The action must read unmistakably as anger rather than focus, worry or a generic frown, but never as rage. No shouting, scream, open mouth, exposed teeth, snarl, exaggerated nostril flare, deep permanent forehead or nose wrinkles, distorted cheeks, clenched protruding jaw, head thrust, hatred, menace, violence, cartoon fury or theatrical acting. Distinguish it from EXP_08 with stronger coordinated brow/eyelid/lip/jaw tension; distinguish it from the retired slight-frown design because anger involves the gaze, eyelids and mouth rather than only a slight brow frown.

Preserve permanent identity exactly. Do not redesign eyebrows, shrink or enlarge eyes, change eye spacing, reshape nose/nostrils/lips, shorten the lower face, slim or widen the face, sharpen/lengthen jaw or chin, change age or skin tone, add tears, flush the skin, or apply beauty filtering.

Composition: squarely front-facing at true eye level, neutral upright head and level shoulders, 85–105mm-equivalent perspective. Exact 3:4 portrait from head top through upper chest. Neutral gray-white seamless studio, soft even 5200–5600K low-contrast light and realistic natural skin texture. Where clothing is visible, show only the plain opaque pink upper portion of the established Calibration Outfit one-piece swimsuit. No other garment, hands, props, second person, text, logo, watermark, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-13`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared unique project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a099a9-4667-7253-98a6-4e3b55277abd/exec-c26c146d-fc83-43bb-b2cc-4ea48fb3d04b.png` (default duplicate removed after checksum-verified project transfer)
- project_candidate_checksum_sha256: `b7b051918515fe79db326cf145d4db3fa587b333127506d604be3a834134dec0`
- technical_precheck: PASS. Both inner brows draw clearly inward and downward with natural moderate glabellar tension; eyelids narrow around a direct angry gaze; lips remain fully closed with moderate pressure and the lower face carries mild believable tension. The coordinated action is stronger than mild annoyance and is not a brow-only slight frown. There is no open mouth, exposed teeth, snarl, exaggerated nostril flare, violent threat, head thrust or cartoon rage. Approved front identity, permanent eye/nose/lip/jaw relationships, Hair-A, upright eye-level composition, neutral studio and visible pink Calibration Outfit upper portion remain consistent. No hands, props, text, watermark or multiple views appear.
- promotion_status: promoted unchanged after explicit user approval

## User approval

On 2026-09-13 the user stated: “ok,11合格，10也合格，一起登记”. The candidate PNG was moved unchanged to the unique approved path and registered as `OWNER_EXP_11_ANGRY_CANON_001`. Approval covers only the transient clear but controlled angry action: inward-downward inner brows, natural glabellar tension, narrowed direct angry gaze, pressed closed lips and mild jaw tension. It does not grant permanent face, hair, outfit, lighting, background or full-release authority.
