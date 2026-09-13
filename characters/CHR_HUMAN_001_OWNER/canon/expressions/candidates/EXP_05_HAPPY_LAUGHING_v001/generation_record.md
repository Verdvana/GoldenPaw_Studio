# EXP_05_HAPPY_LAUGHING_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.76
identity_md_revision: draft_0.64
asset_id: EXP_05_HAPPY_LAUGHING
candidate_id: EXP_05_HAPPY_LAUGHING_v001
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
  - OWNER_L0_EXPRESSION_LAUGH
  - OWNER_L0_EXPRESSION_SMILE_TEETH
reference_count: 4
previous_ai_expression_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_05_HAPPY_LAUGHING_v001/EXP_05_HAPPY_LAUGHING_v001.png"
checksum_sha256: "b3838ede4905401d442f1d3f90044bf15ef05a749c902db24f1c10bbc628dc99"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/approved/EXP_05_HAPPY_LAUGHING/OWNER_EXP_05_HAPPY_LAUGHING_CANON_001.png"
current_promoted_checksum_sha256: "b3838ede4905401d442f1d3f90044bf15ef05a749c902db24f1c10bbc628dc99"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user requested the next planned Expression component, `EXP_05_HAPPY_LAUGHING`. This is one new candidate only. It is reconstructed in parallel from approved Face and Hair masters plus two real L0 images with separate expression duties. No approved or candidate Expression image, failed image, Body image or shot image is supplied.

## Reference budget and responsibility plan

- Face identity: 1 approved image.
- Hairstyle: 1 approved hair-only scoped image.
- L0 primary laugh motion: 1 real image.
- L0 stable smile-trait support: 1 real image.
- Previous Expression/Body/shot: 0 images.
- Total: 4 images.

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`.
   - authoritative_for: exact approved front identity, skull/face proportions, permanent eyes/brows/nose/lips/jaw/chin, skin tone, age and eye-level projection.
   - must_not_define: target laugh motion, transient teeth/dimples, Hair-A length/end design, outfit, body, background or lighting artifacts.
2. Image 2 / `OWNER_HAIR_A_01_FRONT_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`; SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`.
   - authoritative_for: approved front Hairstyle-A near-center part, controlled crown, long straight loose dark-brown panels, restrained highlights and tapered length.
   - must_not_define: face, expression, teeth, dimples, skin, body, outfit, background or lighting.
3. Image 3 / `L0_OWNER_016` — path `characters/CHR_HUMAN_001_OWNER/source/identity/raw/DSC01015.JPG`; SHA-256 `0ef2749f0fcc87494332785bc23f1cae74d4a1ba64efc7d17f40098617125c46`.
   - authoritative_for: real same-person happy-laugh dynamics—clearly increased mouth opening, broad natural lip-corner lift/spread, strong cheek rise, naturally narrowed smiling eyelids, upper/lower tooth exposure relationship and spontaneous joyful energy.
   - must_not_define: permanent identity or dental Canon, camera distance, outdoor sunlight/color, body/torso proportions, pink zip jacket, hairstyle, background, skin texture or permanent geometry.
4. Image 4 / `L0_OWNER_001` — path `characters/CHR_HUMAN_001_OWNER/source/identity/raw/2.jpg`; SHA-256 `2538570559d251d0dc43ecb1b1e048605be8c9e7763c5f08ac97e3e8e2d0a5b0`.
   - authoritative_for: supplementary stable smile traits only—the subject's anatomical-right upper canine/tiger tooth located on image-left in a frontal view, and natural smile-linked dimple/cheek-indentation response, clearer on image-right.
   - must_not_define: laugh intensity or jaw opening, permanent face/dental geometry, wedding makeup/retouch, hand-to-face contact, cropped second person, bridal clothing/veil/jewelry, hairstyle, background, lighting or skin texture.

## Candidate authority

- authoritative_for if approved: EXP_05 transient happy-laugh action—natural broad open smile, stronger cheek/lower-eyelid response and greater jaw opening than EXP_04, while retaining the correctly sided subtle tiger tooth and organic dimple response.
- must_not_define: permanent face, tooth, lip, eye, brow, nose, jaw/chin or static dimple anatomy; Hair-A design; body; outfit; lighting; background; or other Expression components.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 character-expression calibration candidate `EXP_05_HAPPY_LAUGHING_v001` for one adult woman; exactly one image; status REVIEW_REQUIRED.

Use all inputs in parallel with strict role isolation. Image 1 is the sole facial-identity authority: preserve exactly the same recognizable adult person, frontal skull/face proportions, permanent eye/brow/nose/lip foundation, softly rounded jaw/chin, age, skin-tone appearance and true eye-level projection. Image 2 is hair-only authority: preserve the approved front Hairstyle A—short near-center part, controlled crown, long straight loose dark-brown face-framing panels, restrained highlights and tapered length. Image 3 is the primary real same-person laugh-motion reference and may define only a natural happy laugh: broader coordinated lip-corner spread/lift, clearly greater but anatomically plausible mouth and jaw opening, strong cheek rise, naturally narrowed smiling eyelids, visible upper and limited lower teeth, and spontaneous joyful energy. Image 4 only preserves two stable smile traits: the subject's anatomical-right upper canine, located on image-left in a frontal view, is slightly and naturally prominent; cheek rise produces an organic dimple/smile indentation, clearer on image-right.

Do not copy Image 3's outdoor sunlight/color, camera distance, hairstyle, pink zip jacket, torso/body shape or forest background. Do not copy Image 4's wedding makeup/lipstick, retouching, hand touching the face, cropped second person, bridal clothing/veil/jewelry, hairstyle, background or lighting. Neither L0 image may redefine permanent identity. Do not use, imitate or infer pixels from EXP_04 or any generated Expression image.

Primary request: create a genuinely happy, spontaneous natural laugh, clearly stronger than a medium tooth-showing smile. Open the mouth naturally to a moderate laugh aperture with visible upper teeth and a limited natural amount of lower teeth and dark mouth interior. Raise and spread both lip corners broadly, lift the cheeks strongly, and let the lower eyelids narrow from real smiling without squeezing the eyes shut. Keep brows relaxed or slightly raised only by natural joyful animation. Preserve the subject-right tiger tooth on image-left as a subtle authentic canine within one normal adult tooth row; do not elongate it or turn it into a fang. Preserve natural smile-linked dimpling/soft cheek indentation, clearest on image-right, but do not create holes, scars, static pits or mechanically mirrored dimples.

The result must read as happy laughter, not surprise, screaming, shouting, crying, pain, mania, a forced advertising grin or a cartoon face. Keep the jaw opening clearly greater than EXP_04 but not extreme. No dominant gums, protruding tongue, black cavern mouth, duplicated/fused/missing teeth, extra row, uniformly rectangular veneers or distorted oral anatomy.

Preserve permanent identity exactly. Expression movement is limited to lips/lip corners, cheeks/dimples, eyelids and natural jaw articulation. Do not enlarge the permanent mouth, reshape permanent eyes/brows/nose, slim/widen the face, sharpen/lengthen jaw or chin, change age/skin tone or apply beauty filtering.

Composition: squarely front-facing at true eye level, neutral upright head and level shoulders, 85–105mm-equivalent perspective. Exact 3:4 portrait from head top through upper chest, consistent with the Face/Expression calibration series. Neutral gray-white seamless studio, soft even 5200–5600K low-contrast light and realistic natural skin texture. Where clothing is visible, show only the plain opaque pink upper portion of the established Calibration Outfit one-piece swimsuit. No other garment, hand touching face, props, second person, text, logo, watermark, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-13`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a095f8-d792-7540-92a2-d60cb9777c57/exec-1bd06997-b9e1-484f-82d1-52f95fc54298.png` (transient default output removed after checksum-verified project transfer; no duplicate retained)
- project_candidate_checksum_sha256: `b3838ede4905401d442f1d3f90044bf15ef05a749c902db24f1c10bbc628dc99`
- technical_precheck: PASS. The expression reads as a genuine happy laugh clearly stronger and more open than EXP_04: both lip corners spread and rise broadly, cheeks lift strongly, and lower eyelids narrow naturally without the eyes closing or brows becoming surprised. The jaw opens to a moderate laugh aperture with principally upper teeth, a limited lower-tooth row and a natural dark oral cavity; there is no dominant gum, protruding tongue, scream-like opening, duplicate tooth row or obvious fused/missing tooth artifact. The subject's anatomical-right upper canine remains subtly visible on image-left without fang treatment, and a light organic smile indentation remains visible on image-right. Approved front identity relationships, Hair-A, eye-level composition, neutral studio and the pink Calibration Outfit upper portion remain consistent. No outdoor, bridal, hand, second-person, text or watermark residue is visible.
- promotion_status: promoted unchanged after explicit user approval

## User approval

On 2026-09-13 the user stated: “很好，审核通过。之前生成的05也审核通过”. The candidate PNG was moved unchanged to the unique approved path and registered as `OWNER_EXP_05_HAPPY_LAUGHING_CANON_001`. Approval covers only the transient natural happy-laugh action, stronger cheek/lower-eyelid response, moderate laugh aperture, correctly sided subtle tiger tooth and organic smile-linked dimple response. It does not grant permanent face/dental/dimple, hair, outfit, lighting, background or full-release authority.
