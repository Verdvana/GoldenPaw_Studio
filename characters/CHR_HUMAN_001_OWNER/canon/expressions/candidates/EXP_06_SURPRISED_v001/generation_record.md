# EXP_06_SURPRISED_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.78
identity_md_revision: draft_0.66
asset_id: EXP_06_SURPRISED
candidate_id: EXP_06_SURPRISED_v001
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
  - OWNER_L0_EXPRESSION_SURPRISED
reference_count: 3
previous_ai_expression_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_06_SURPRISED_v001/EXP_06_SURPRISED_v001.png"
checksum_sha256: "183a65e882785115e2b1b465bd564232386233346f42a3ea3c04e06854245b86"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/approved/EXP_06_SURPRISED/OWNER_EXP_06_SURPRISED_CANON_001.png"
current_promoted_checksum_sha256: "183a65e882785115e2b1b465bd564232386233346f42a3ea3c04e06854245b86"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user requested the next planned component after leaving EXP_05 unapproved. `EXP_06_SURPRISED_v001` is one independent candidate reconstructed from approved Face and Hair masters plus one real L0 surprise reference. EXP_05, all other generated Expression images, Body assets and shot images are excluded.

## Reference budget and responsibility plan

- Face identity: 1 approved image.
- Hairstyle: 1 approved hair-only scoped image.
- L0 surprise motion: 1 real image.
- Previous Expression/Body/shot: 0 images.
- Total: 3 images.

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`.
   - authoritative_for: exact approved front identity, permanent skull/face proportions, eyes/brows/nose/lips/jaw/chin, skin tone, age and eye-level projection.
   - must_not_define: target surprise motion, Hair-A length/end design, outfit, body, background or lighting artifacts.
2. Image 2 / `OWNER_HAIR_A_01_FRONT_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`; SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`.
   - authoritative_for: approved front Hairstyle-A near-center part, controlled crown, long straight loose dark-brown panels, restrained highlights and tapered length.
   - must_not_define: face, expression, eye/brow/mouth geometry, skin, body, outfit, background or lighting.
3. Image 3 / `L0_OWNER_006` — path `characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg`; SHA-256 `734458326895b48099efa0dc58c43646d8b104823c1c36c1def8f27d08d88c17`.
   - authoritative_for: real same-person natural surprise dynamics only—moderate brow lift, widened eyelids, naturally parted lips, restrained jaw drop and their soft-tissue coordination.
   - must_not_define: permanent face/eye/brow/mouth/jaw identity; HAIRSTYLE_B updo; hands touching cheeks; sweater; torso/body pose; warm color cast; garden background; lighting; skin texture; or cheerful smile dynamics.

## Candidate authority

- authoritative_for if approved: EXP_06 transient natural-surprise action—moderate brow elevation, increased eyelid opening and restrained natural mouth/jaw opening.
- must_not_define: permanent face, eye, brow, lip, nose, jaw/chin geometry; teeth; skin; age; Hair-A; body; outfit; lighting; background; or other Expressions.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 character-expression calibration candidate `EXP_06_SURPRISED_v001` for one adult woman; exactly one image; status REVIEW_REQUIRED.

Input roles are strictly isolated and parallel. Image 1 is the sole facial-identity authority: preserve exactly the same recognizable adult person, frontal skull/face proportions, permanent eye shape/spacing, brow foundation, nose, lip foundation, softly rounded jaw/chin, age, skin-tone appearance and true eye-level projection. Image 2 is hair-only authority: preserve the approved front Hairstyle A with short near-center part, controlled crown, long straight loose dark-brown face-framing panels, restrained highlights and tapered length. Image 3 is the real same-person surprise reference and may define only the coordinated transient surprise action: moderate eyebrow lift, increased eyelid opening, naturally parted lips, restrained jaw drop and alert attention.

Do not copy Image 3's HAIRSTYLE_B updo, loose updo strands, hands touching the cheeks, sweater, body pose, warm lighting/color, garden background, makeup or permanent facial geometry. Do not use, imitate or infer pixels from EXP_05 or any generated Expression image.

Primary request: create a natural, immediately readable but restrained surprised expression. Raise both eyebrows moderately and evenly with gentle forehead activation, not extremely high arches. Open the upper and lower eyelids somewhat wider than neutral while keeping the real permanent eye size and shape; do not create huge round cartoon eyes or expose excessive sclera. Part the lips naturally into a small-to-medium soft oval opening and let the jaw lower only enough for surprise, with little or no visible teeth. Keep lip corners neutral—not smiling, laughing, grimacing or pulled downward. Cheeks stay relatively neutral rather than lifted by joy. Gaze is alert and directly toward camera.

The result must not read as fear, panic, screaming, shouting, crying, pain, happy laughter, seductive open mouth or blankness. No hands, face-touching pose, gasp gesture, exaggerated forehead wrinkles, nostril flare, dominant gums, tongue, cavernous mouth or distorted teeth.

Preserve permanent identity exactly. Expression movement is limited to brows/forehead, eyelids, lips and restrained jaw articulation. Do not permanently enlarge eyes, raise/redesign brows, widen the mouth, reshape lips/nose, slim/widen the face, sharpen/lengthen jaw or chin, change age/skin tone or apply beauty filtering.

Composition: squarely front-facing at true eye level, neutral upright head and level shoulders, 85–105mm-equivalent perspective. Exact 3:4 portrait from head top through upper chest. Neutral gray-white seamless studio, soft even 5200–5600K low-contrast light and realistic natural skin texture. Where clothing is visible, show only the plain opaque pink upper portion of the established Calibration Outfit one-piece swimsuit. No other garment, hands, props, second person, text, logo, watermark, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-13`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a095f8-d792-7540-92a2-d60cb9777c57/exec-9d5188f5-f265-4b7a-997b-2aff4b8b8bd8.png` (transient default output removed after checksum-verified project transfer; no duplicate retained)
- project_candidate_checksum_sha256: `183a65e882785115e2b1b465bd564232386233346f42a3ea3c04e06854245b86`
- technical_precheck: PASS. Both brows rise moderately and evenly with restrained forehead activation; eyelids open wider than neutral while preserving the subject's permanent almond-eye geometry and avoiding excessive sclera or cartoon roundness. Lips form a small-to-medium soft opening with very limited upper-tooth visibility and a restrained jaw drop. Lip corners and cheeks remain neutral, so the expression reads as alert natural surprise rather than fear, scream or happy laugh. Approved front identity relationships, Hair-A, eye-level composition, neutral studio and pink Calibration Outfit upper portion remain consistent. No updo, cheek-touching hands, sweater, garden, text or watermark residue is visible.
- promotion_status: promoted unchanged after explicit user approval

## User approval

On 2026-09-13 the user stated: “审核通过，并且开始下一项”. The candidate PNG was moved unchanged to the unique approved path and registered as `OWNER_EXP_06_SURPRISED_CANON_001`. Approval covers only the transient natural restrained-surprise action: moderate brow elevation, increased eyelid opening, alert gaze and restrained lip/jaw opening. It does not grant permanent face, eye/brow/lip/jaw, hair, outfit, lighting, background or full-release authority.
