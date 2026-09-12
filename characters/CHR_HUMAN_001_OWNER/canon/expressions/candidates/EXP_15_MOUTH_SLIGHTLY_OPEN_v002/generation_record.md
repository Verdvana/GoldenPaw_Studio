# EXP_15_MOUTH_SLIGHTLY_OPEN_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.62
identity_md_revision: draft_0.50
asset_id: EXP_15_MOUTH_SLIGHTLY_OPEN
candidate_id: EXP_15_MOUTH_SLIGHTLY_OPEN_v002
gate: "Gate 5 — Expression Canon (explicit user-authorized out-of-order candidate)"
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
previous_ai_expression_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_15_MOUTH_SLIGHTLY_OPEN_v002/EXP_15_MOUTH_SLIGHTLY_OPEN_v002.png"
checksum_sha256: "3be4734a2e019d569e5fcae4eabd886a5bbe7a27c12059830de9424a65c78d36"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/approved/EXP_15_MOUTH_SLIGHTLY_OPEN/OWNER_EXP_15_MOUTH_SLIGHTLY_OPEN_CANON_001.png"
current_promoted_checksum_sha256: "3be4734a2e019d569e5fcae4eabd886a5bbe7a27c12059830de9424a65c78d36"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user rejected v001 and explicitly corrected the EXP_15 design. v002 is a fresh parallel generation from the two approved scoped Masters listed below. No v001 pixels, previous Expression candidate, failed image, shot image, Body image, Hairstyle-B image or L0 expression image is supplied. Only the user's corrected written expression definition carries forward.

## Reference budget and responsibility plan

- Face identity: 1 approved image.
- Hairstyle: 1 approved hair-only scoped image.
- L0 expression, Body, outfit image, hosiery material, previous candidate and previous shot: 0 images.
- Total: 2 images.

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`.
   - authoritative_for: approved front facial identity, skull/face proportions, eyes and brows at rest, nose, permanent lip form, jaw/chin, skin tone, age and true eye-level projection.
   - must_not_define: target transient brow/eyelid/mouth movement, final Hair-A length/end design, outfit, body, background or lighting artifacts.
2. Image 2 / `OWNER_HAIR_A_01_FRONT_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`.
   - authoritative_for: approved front Hairstyle-A part, controlled crown, long straight loose panels, dark-brown restrained highlights and tapered length.
   - must_not_define: face, brows, eyelids, expression, nose, lips, jaw/chin, skin, body, outfit, background or lighting.

## Candidate authority

- authoritative_for: EXP_15 transient expression only—natural frown, naturally closed eyes, and a restrained non-wide mouth opening.
- must_not_define: permanent brow/eye/lip shape, teeth design, skull, nose, jaw/chin identity, skin tone, age, Hair-A design beyond its approved source, body, outfit, lighting or background.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 character-expression calibration candidate `EXP_15_MOUTH_SLIGHTLY_OPEN_v002` for one adult woman; exactly one image; status REVIEW_REQUIRED. Generate independently from the two approved Masters and do not use any v001 pixels.

Image 1 is the sole facial-identity authority. Preserve exactly the same recognizable adult person, frontal skull/face proportions, eye spacing and permanent eye shape, permanent brow design, nose bridge/tip/alar proportions, permanent upper/lower lip geometry and color, rounded jaw/chin relationship, skin tone and age. Image 2 is hair-only authority. Preserve its approved front Hairstyle A: short near-center part, controlled low-to-moderate crown, long straight loose dark-brown face-framing panels, restrained highlights, fine strands and tapered length. Image 2 must not influence face or expression.

Primary request: portray all three expression actions simultaneously and clearly: (1) a natural frown, with the inner brow heads drawn moderately inward and slightly downward and a visible but realistic vertical glabellar tension; (2) both eyes naturally fully closed, upper and lower eyelids meeting without hard squeezing, winking or asymmetric closure; (3) mouth open to a restrained small-to-medium amount, clearly more than lips merely parted but definitely not wide open. Keep the mouth opening compact and anatomically natural, with only modest jaw lowering. A small natural glimpse of the dark mouth interior or upper teeth is acceptable, but no broad tooth display, tongue emphasis or cavernous opening. The three components must coexist; do not omit the frown or closed eyes.

Preserve permanent identity. Expression movement is limited to brow/glabella, eyelids, lip corners/lip soft tissue and modest jaw articulation. Do not enlarge or shrink the nose, widen or narrow the face, lengthen/drop/sharpen the jaw or chin, redesign the lips or brows, puff the cheeks, or change age/skin tone. Avoid exaggerated anguish, screaming, crying tears, surprise, laughing, smiling, yawning, singing, seductive affect, cartoon grimace or pain distortion.

Composition: squarely front-facing at true eye level, neutral upright head, level shoulders, 85–105mm-equivalent perspective. Exact 3:4 portrait from head top through upper chest, consistent with the Face/Expression calibration series. Neutral gray-white seamless studio and soft even 5200–5600K low-contrast light. Realistic skin texture. Where clothing is visible, show only the plain opaque pink upper portion of the established Calibration Outfit one-piece swimsuit. No other garment, props, text, logo, watermark, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-12`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a09467-3db0-70a2-bf86-1fb58ecbbfb6/exec-da06e466-524f-40f2-85d3-64b04ad590a2.png` (transient source removed after project transfer; no duplicate retained)
- project_candidate_checksum_sha256: `3be4734a2e019d569e5fcae4eabd886a5bbe7a27c12059830de9424a65c78d36`
- technical_precheck: PASS. All three user-defined actions visibly coexist: both inner brow heads pull inward/downward with natural glabellar furrows; both eyelids close symmetrically without a wink; and the mouth opens a restrained small-to-medium amount, clearly open but not wide. The slight upper-teeth/interior glimpse remains proportionate. There is no smile, surprise, tear, scream, yawn or cartoon pain distortion. The approved front identity, nose scale, face width, rounded jaw/chin relationship, skin tone and age remain visually consistent; the visible front Hairstyle-A attributes, true eye-level camera, neutral studio and pink Calibration Outfit upper portion also remain consistent.
- promotion_status: promoted unchanged after explicit user approval

## User approval

On 2026-09-12 the user stated: “合格，登记”. v002 was moved unchanged to the unique approved path and registered as `OWNER_EXP_15_MOUTH_SLIGHTLY_OPEN_CANON_001`. Approval covers only the compound transient expression—natural frown, both eyes naturally closed, and a restrained non-wide mouth opening. It does not grant permanent face, hair, outfit, lighting, background or full-release authority.
