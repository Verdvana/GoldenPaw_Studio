# EXP_04_SMILE_WITH_TEETH_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.73
identity_md_revision: draft_0.61
asset_id: EXP_04_SMILE_WITH_TEETH
candidate_id: EXP_04_SMILE_WITH_TEETH_v002
gate: "Gate 5 — Expression Canon (user-corrected regeneration)"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/candidates/EXP_04_SMILE_WITH_TEETH_v002/EXP_04_SMILE_WITH_TEETH_v002.png"
checksum_sha256: "f14a9647c6e459362190c2db723f1f4ab2916ec8069a11cf81acef258e03d2a3"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/expressions/approved/EXP_04_SMILE_WITH_TEETH/OWNER_EXP_04_SMILE_WITH_TEETH_CANON_001.png"
current_promoted_checksum_sha256: "f14a9647c6e459362190c2db723f1f4ab2916ec8069a11cf81acef258e03d2a3"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user explicitly rejected v001 and requested regeneration after identifying two omitted stable smile traits in `2.jpg`: the subject's anatomical-right upper tiger tooth (image-left in a frontal view) and natural smile dimples. v002 is one new candidate reconstructed in parallel from approved Face and Hair masters plus that real L0 image. v001 and all other generated Expression images are excluded as pixel inputs.

## Reference budget and responsibility plan

- Face identity: 1 approved image.
- Hairstyle: 1 approved hair-only scoped image.
- L0 expression/dental/dimple evidence: 1 user-selected real image.
- Body, outfit image, previous candidate and previous shot: 0 images.
- Total: 3 images.

1. Image 1 / `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`; SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`.
   - authoritative_for: exact approved front identity, skull/face proportions, permanent eyes/brows/nose/lips/jaw/chin, skin tone, age and true eye-level projection.
   - must_not_define: target smile motion, transient dimples, visible tooth exposure, final Hair-A design, outfit, body, background or lighting artifacts.
2. Image 2 / `OWNER_HAIR_A_01_FRONT_CANON_001` — path `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`; SHA-256 `18b11d12d9834aeb4139814fd5413a43bb4e91fc26bf182718f1620f80edb219`.
   - authoritative_for: approved front Hairstyle-A short near-center part, controlled crown, long straight loose panels, dark-brown restrained highlights and tapered length.
   - must_not_define: face, expression, teeth, dimples, skin, body, outfit, background or lighting.
3. Image 3 / `L0_OWNER_001` — path `characters/CHR_HUMAN_001_OWNER/source/identity/raw/2.jpg`; SHA-256 `2538570559d251d0dc43ecb1b1e048605be8c9e7763c5f08ac97e3e8e2d0a5b0`.
   - authoritative_for: real same-person smile dynamics; the slight natural prominence and position of the subject's anatomical-right upper canine/tiger tooth, which appears on image-left in a frontal view; restrained upper-teeth exposure; cheek rise and natural dimple/smile-indentation response, more clearly visible on image-right.
   - must_not_define: permanent skull/face proportions; eye, nose, jaw or chin geometry; wedding makeup or lip color; retouched skin texture; hand-to-face contact; the cropped second person; bridal garment/veil/jewelry; hairstyle; background; lighting; camera distortion; or a permanent static cheek depression.

## Candidate authority

- authoritative_for if approved: EXP_04 transient natural tooth-showing smile only, including the correctly sided subtle tiger-tooth visibility, natural upper-teeth exposure, smile-coupled cheek rise and dimple response.
- must_not_define: permanent face geometry; tooth anatomy/color outside this expression's approved visible traits; static dimples at rest; Hair-A design beyond its approved source; body, outfit, lighting or background.

## Prompt assembly

```text
Use case: identity-preserve.
Asset type: L1 character-expression calibration candidate `EXP_04_SMILE_WITH_TEETH_v002` for one adult woman; exactly one image; status REVIEW_REQUIRED.

Input roles are strictly isolated and parallel. Image 1 is the sole facial-identity authority: preserve exactly the same recognizable adult person, frontal skull/face proportions, permanent eye/brow/nose/lip foundation, softly rounded jaw/chin, age, skin-tone appearance and true eye-level projection. Image 2 is hair-only authority: preserve its approved front Hairstyle A, with short near-center part, controlled crown, long straight loose dark-brown face-framing panels, restrained highlights and complete tapered length. Image 3 is the user-selected real same-person smile evidence and may define only smile dynamics and the following real smile traits: (a) the subject's anatomical-right upper canine, located on image-left in a frontal view, is slightly and naturally more prominent—the authentic small "tiger tooth" visible within otherwise normal adult dentition; (b) cheek rise creates natural dimple/smile-indentation response, more clearly readable on image-right; (c) the real upper-teeth exposure, lip-corner spread and warm lower-eyelid response.

Do not copy Image 3's wedding makeup, lipstick color, retouched finish, hand touching the face, the cropped second person, bridal clothing/veil/jewelry, hairstyle, background, light, camera distortion or permanent face geometry. Do not use, imitate or infer pixels from v001 or any generated Expression image.

Primary request: a natural, friendly, medium-intensity tooth-showing smile. Show principally one plausible row of naturally off-white upper teeth with modest jaw opening and little or no lower teeth or gum. Preserve the slight prominence of the subject's anatomical-right upper canine on image-left. It must read as her small authentic tiger tooth, not as a newly invented tooth: no elongated point, fang, tusk, vampire tooth, duplicate canine, extra row or broken alignment. Let both cheeks rise naturally; include the real smile-linked dimple/soft cheek indentation, clearest on image-right, with subtle organic asymmetry. It must not look like a drilled hole, deep pit, scar, wrinkle pasted onto skin, or mechanically mirrored pair. Keep brows relaxed, gaze calm/direct and lower eyelids warmly responsive without hard squinting. Stay below a broad grin or laugh.

Preserve permanent identity exactly. Expression movement is limited to lips/lip corners, cheeks/dimples, gentle lower-eyelid response and modest jaw articulation. Do not enlarge the permanent mouth, reshape the eyes/brows/nose, slim or widen the face, sharpen the jaw/chin, change age/skin tone, add beauty filtering, or turn the expression into a smirk, grimace, surprise, shout or laugh.

Composition: squarely front-facing at true eye level, neutral upright head and level shoulders, 85–105mm-equivalent perspective. Exact 3:4 portrait from head top through upper chest, consistent with the calibration series. Neutral gray-white seamless studio, soft even 5200–5600K low-contrast light and realistic natural skin texture. Where clothing is visible, show only the plain opaque pink upper portion of the established Calibration Outfit one-piece swimsuit. No other garment, hand touching face, props, second person, text, logo, watermark, collage or multiple views.
```

## Attempt result

- generated_at: `2026-09-12`
- result: one 1086x1448 exact-3:4 PNG generated and stored at the declared project candidate path
- built_in_output: `/home/verdvana/.codex/generated_images/01a095f8-d792-7540-92a2-d60cb9777c57/exec-4e3f1531-2591-43d2-8c9f-829d97c59a35.png` (transient default output removed after checksum-verified project transfer; no duplicate retained)
- project_candidate_checksum_sha256: `f14a9647c6e459362190c2db723f1f4ab2916ec8069a11cf81acef258e03d2a3`
- technical_precheck: PASS. The subject's anatomical-right upper canine is visibly and correctly located on image-left in the frontal portrait; it has a restrained authentic tiger-tooth prominence without elongation, duplicate anatomy or fang-like treatment. A subtle natural smile indentation is visible on the image-right cheek adjacent to the raised smile, without a drilled-hole, scar or mechanically mirrored appearance. The smile is friendly and medium in intensity, with principally upper-teeth display, modest jaw opening, little/no gum and no obvious duplicated/fused teeth or extra row. Approved front identity relationships, Hair-A, eye-level composition, neutral studio and the pink Calibration Outfit upper portion remain visually consistent. No wedding hand/person/veil/background residue is present.
- promotion_status: promoted unchanged after explicit user approval

## User approval

On 2026-09-12 the user stated: “可以，登记吧”. The candidate PNG was moved unchanged to the unique approved path and registered as `OWNER_EXP_04_SMILE_WITH_TEETH_CANON_001`. Approval covers only the transient natural medium tooth-showing smile, correctly sided subtle tiger-tooth visibility, restrained upper-teeth exposure, natural cheek rise and smile-linked dimple response. It does not grant permanent face, static dental/dimple, hair, outfit, lighting, background or full-release authority.
