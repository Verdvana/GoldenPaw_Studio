# FACE_02_LEFT_3Q_NEUTRAL_v004 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.14
identity_md_revision: draft_0.14
asset_id: FACE_02_LEFT_3Q_NEUTRAL
candidate_id: FACE_02_LEFT_3Q_NEUTRAL_v004
gate: "Gate 2 — Face Identity Canon"
model_tool: "built-in image_gen"
status: APPROVED
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_count: 3
prompt_basis: "v001 prompt plus three concise user constraints"
seed_settings: "built-in image_gen; seed and detailed settings not returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_02_LEFT_3Q_NEUTRAL_v004/FACE_02_LEFT_3Q_NEUTRAL_v004.png"
pixel_storage_status: "MOVED_TO_CANON_THEN_TRANSCODED; CANDIDATE_RASTER_REMOVED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg"
qa_status: PASS_USER_APPROVED
```

## Reference plan

Identical to v001: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` defines approved identity; `L0_OWNER_013` defines only real left-three-quarter depth; `OWNER_HAIRSTYLE_A_FACE_MASKED_001` defines only Hairstyle A. v001, v002 and v003 are excluded as image inputs.

## Prompt delta from v001

The v001 prompt structure and wording are preserved. Other than revision/candidate labels, only three concise constraints are added: cheekbone slightly lower/softer; chin rounder without width or length change; gaze gentler without eye-geometry change.

## Final assembled prompt

Use case: identity-preserve

Asset type: `FACE_02_LEFT_3Q_NEUTRAL`, L1 Face Canon candidate v004 for `CHR_HUMAN_001_OWNER`, governed by `OWNER_L1_GENERATION_SPEC` draft_1.14 and `OWNER_IDENTITY_ANCHOR` draft_0.14.

Input images: Image 1 is the approved front-neutral Face Canon and is authoritative for the exact recognizable woman, facial-feature relationships, adult age appearance, neutral-studio skin tone and neutral expression. Image 2 is the real L0 left-three-quarter source and is authoritative only for the same person's orbital depth, nose projection, cheek-to-jaw depth, ear placement and face-points-image-left geometry. Image 3 is a source-derived masked Hairstyle A reference and is authoritative only for hair design. Resolve identity conflicts in favor of Image 1.

Primary request: Create exactly one new photorealistic left-three-quarter neutral portrait. Turn the head approximately 35–40 degrees toward image-left so the anatomical left facial plane is principally visible. Keep the eyes looking toward the camera, the mouth naturally closed and the expression neutral. Reconstruct the new angle from the three scoped master references in parallel; do not copy or continue any previous AI candidate.

Identity: Preserve exactly the same recognizable woman as Image 1, including skull proportions, eye spacing, brows, natural eye size, nose, soft lips, naturally full cheeks, rounded jaw transition, rounded chin, adult age and natural asymmetry. Image 2 may solve only real view-dependent depth. Do not inherit its smile, gaze, formal makeup, retouching, skin tone, lighting, ornaments, hairstyle, clothing or background. Image 3 must not influence face, skin, skull, body, clothing, light or background. Add only these restrained refinements while keeping all other facial features unchanged: make the cheekbone appear slightly lower with a softer contour; give the chin a softer, rounder terminal curve without changing chin length or jaw width; make the gaze gentler by relaxing eyelid tension without changing eye size, shape, spacing, canthal direction or pupil placement.

Hairstyle: `HAIRSTYLE_A` only — near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels, subtle strand irregularity and tapered ends. No bun, no updo, no Hairstyle B and no A/B hybrid.

Composition and camera: Exact 3:4 portrait; head top to upper chest; head approximately 65–72% of frame height; 85–105mm-equivalent portrait perspective; camera at eye height; horizontal optical axis; upright neutral head; visually level forehead, hairline, skull, crown, ears and jaw. No top-down or upturned-head projection and no excessive visible crown plane.

Scene and light: Neutral gray-white seamless studio; soft even low-contrast 5200–5600K light; neutral white balance; natural photographic skin texture. If clothing is visible, show only the authentic upper portion of the same pink high-cut one-piece Calibration Outfit, not a tank top or other pink garment.

Avoid: identity averaging, generic face, slimming, enlarged eyes, narrowed nose, pointed chin, high or sharply prominent cheekbone, intense stare, age change, beauty filter, whitening, heavy makeup, smile, parted lips, distorted ears, asymmetric eye errors, wide-angle distortion, dramatic styling, color cast, text, watermark, collage and multiple views.

Output: One candidate image only. `REVIEW_REQUIRED`; do not label or imply Canon approval.

## Generation settings/result

- generated_at: `2026-09-10T14:50:00+08:00`
- seed/settings: built-in `image_gen`; seed and detailed settings were not returned
- source output: `/home/verdvana/.codex/generated_images/01a089e9-1904-7443-9200-afbaa6608bae/exec-bdc4e84e-92a6-4548-9658-43e2d02bb914.png`
- original output path: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_02_LEFT_3Q_NEUTRAL_v004/FACE_02_LEFT_3Q_NEUTRAL_v004.png` (record only; raster removed after promotion)
- output_dimensions: `1086x1448`
- output_checksum: `34f1a633d37434c8bb17ba28259ff76fa0ba495abb02816979d6b2b6e8a265c3`
- QA_record: `QA.md`

## User approval outcome

- decision: APPROVED as the current `FACE_02_LEFT_3Q_NEUTRAL` L1 Canon component
- promoted_asset: `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001`
- current approved Master: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001.jpg`
- current_approved_jpg_checksum: `3f50c08e2993aa8dd406abd093d24f8a581b6e1475aa4dd57bda3884fed3b745`
- approval_record: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_02_LEFT_3Q_NEUTRAL/approvals/APPROVAL_OWNER_FACE_02_LEFT_3Q_NEUTRAL_001.md`
- reproduction_method: `characters/CHR_HUMAN_001_OWNER/canon/face/FACE_02_LEFT_3Q_NEUTRAL_METHOD.md`
- full_owner_release: remains unlocked
