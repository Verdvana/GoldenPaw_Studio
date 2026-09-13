# EXP_09_SAD_CONCERNED_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.86
identity_md_revision: draft_0.74
asset_id: EXP_09_SAD_CONCERNED
candidate_id: EXP_09_SAD_CONCERNED_v001
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_09_SAD_CONCERNED_v001/EXP_09_SAD_CONCERNED_v001.png"
checksum_sha256: "af5b7eaa31e63be25f42a60ed62f4ff59eb8622090c334dc4540ca893c2e6037"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/approved/EXP_09_SAD_CONCERNED/OWNER_EXP_09_SAD_CONCERNED_CANON_001.png"
current_promoted_checksum_sha256: "af5b7eaa31e63be25f42a60ed62f4ff59eb8622090c334dc4540ca893c2e6037"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user approved EXP_08 and explicitly requested the next planned Expression item. `EXP_09_SAD_CONCERNED_v001` is one independent candidate constructed only from approved Face and Hair masters. No approved or candidate Expression image, Body asset or shot image is supplied as a pixel input.

## Source-coverage review

The current Reference Guide, complete L0 manifest and registered reference sets contain no reliable sad/concerned expression photograph. Downward smile, closed-eye, surprise and wedding-smile images are not repurposed. This candidate therefore proposes a conservative text-defined transient action and remains non-Canon until explicit approval.

## Reference budget and responsibility plan

- Face identity: 1 approved image.
- Hairstyle: 1 approved hair-only scoped image.
- L0 expression motion: 0 images because coverage is absent.
- Previous Expression/Body/shot: 0 images.
- Total: 2 images.

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`.
   - authoritative_for: exact approved front identity, permanent skull/face proportions, eyes/brows/nose/lips/jaw/chin, skin tone, age and eye-level projection.
   - must_not_define: target sad/concerned motion, Hair-A design, outfit, body, background or lighting artifacts.
2. Image 2 / `OWNER_HAIR_A_01_FRONT_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`; SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`.
   - authoritative_for: approved front Hairstyle-A near-center part, controlled crown, long straight loose dark-brown panels, restrained highlights and tapered length.
   - must_not_define: face, expression, eye/brow/mouth geometry, skin, body, outfit, background or lighting.

## Candidate authority

- authoritative_for if approved: EXP_09 transient sad/concerned action—slightly raised and drawn-together inner brows, softened worried direct gaze, mildly downturned closed lip corners and minimal chin tension.
- must_not_define: permanent face, eye, brow, lip, nose, jaw/chin geometry; tears; skin; age; Hair-A; body; outfit; lighting; background; or other Expressions.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 character-expression calibration candidate `EXP_09_SAD_CONCERNED_v001` for one adult woman; exactly one image; status REVIEW_REQUIRED.

Input roles are strictly isolated and parallel. Image 1 is the sole facial-identity authority: preserve exactly the same recognizable adult person, frontal skull and face proportions, permanent natural eye shape and spacing, brow foundation, nose, lips, softly rounded jaw and chin, age, skin-tone appearance and true eye-level projection. Image 2 is hair-only authority: preserve the approved front Hairstyle A with short near-center part, controlled crown, long straight loose dark-brown face-framing panels, restrained highlights and tapered length. No real L0 source reliably covers sad/concerned motion, so create only the conservative transient action described below. Do not use, imitate or infer pixels from any generated Expression image.

Primary request: create a natural, restrained sad/concerned expression, readable as quiet worry rather than active crying. Lift both inner eyebrows slightly and draw them gently together while keeping the mid/outer brows natural or subtly lower; use only shallow forehead and glabellar tension. Keep both eyes at their approved permanent size and almond shape, with softened upper eyelids and a gentle directly forward worried gaze. Keep lips naturally closed; lower both mouth corners only slightly and symmetrically, with minimal soft chin tension and no pout. Cheeks remain relaxed. The expression should feel empathetic, troubled and subdued.

No tears, wet tear tracks, deliberately glassy eyes, crying, sobbing, pain grimace, extreme pleading, deeply arched brows, strong forehead furrows, mouth opening, quivering lip, exaggerated pout, childish wounded face, fear, surprise, anger, annoyance, concentration, sarcasm, smile or cartoon sadness. Keep the head upright, level and squarely front-facing; do not manufacture sadness with a bowed head or downward gaze.

Preserve permanent identity exactly. Expression motion is limited to small inner-brow elevation/convergence, softened eyelid attention, slight symmetric lip-corner downturn and minimal chin soft-tissue tension. Do not permanently redesign eyebrows, enlarge or reshape eyes, change gaze anatomy, reshape lips/nose, shorten the lower face, slim or widen the face, sharpen/lengthen jaw or chin, change age or skin tone, or apply beauty filtering.

Composition: squarely front-facing at true eye level, neutral upright head and level shoulders, 85–105mm-equivalent perspective. Exact 3:4 portrait from head top through upper chest. Neutral gray-white seamless studio, soft even 5200–5600K low-contrast light and realistic natural skin texture. Where clothing is visible, show only the plain opaque pink upper portion of the established Calibration Outfit one-piece swimsuit. No other garment, hands, props, second person, text, logo, watermark, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-13`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a095f8-d792-7540-92a2-d60cb9777c57/exec-94199ab6-df7a-45f1-ac32-69a0185c7452.png` (transient default output removed after checksum-verified project transfer; no duplicate retained)
- project_candidate_checksum_sha256: `af5b7eaa31e63be25f42a60ed62f4ff59eb8622090c334dc4540ca893c2e6037`
- technical_precheck: PASS. Both inner brows rise slightly and converge with shallow natural tension while mid/outer brows remain restrained. The approved almond-eye geometry is retained with softened lids and a direct worried gaze. Lips stay naturally closed with a small symmetric corner downturn and only minimal chin soft-tissue tension. The result reads as subdued sadness/concern without tears, crying, pout, pain, fear, surprise, anger, annoyance or cartoon exaggeration. Approved front identity relationships, Hair-A, upright eye-level composition, neutral studio and visible pink Calibration Outfit upper portion remain consistent. No hands, props, text, watermark or multiple views appear.
- promotion_status: promoted unchanged after explicit user approval

## User approval

On 2026-09-13 the user stated: “good,登记并开始下一项”. The candidate PNG was moved unchanged to the unique approved path and registered as `OWNER_EXP_09_SAD_CONCERNED_CANON_001`. Approval covers only the transient restrained sad/concerned action: slightly raised/converged inner brows, softened worried gaze, mild symmetric closed-lip corner downturn and minimal chin tension. It does not grant permanent face, hair, outfit, lighting, background or full-release authority.
