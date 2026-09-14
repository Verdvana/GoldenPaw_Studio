# HAIR_A_05_HIGH_CAMERA_LOOK_UP_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.161
identity_md_revision: draft_0.149
hairstyle_document: canon/hairstyles/A/HAIRSTYLE.md
asset_id: HAIR_A_05_HIGH_CAMERA_LOOK_UP
candidate_id: HAIR_A_05_HIGH_CAMERA_LOOK_UP_v001
gate: "Gate 4 — Hairstyle Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
reference_count: 2
previous_ai_hairstyle_a_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_05_HIGH_CAMERA_LOOK_UP/OWNER_HAIR_A_05_HIGH_CAMERA_LOOK_UP_CANON_001.png"
checksum_sha256: "0f8c8f5dfbfdc017df5082b79657e23657f52e520ea4d3d3f5d612dbade4404a"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user approved HAIR_A_04 and requested the next asset. This authorizes exactly one `HAIR_A_05_HIGH_CAMERA_LOOK_UP_v001` candidate. It is built independently from the approved front-neutral Face Master and the deterministic L0 hair-only derivative. No approved `HAIR_A_01/02/03/04`, generated Hair candidate, Expression, Pose or Shot is supplied.

## Reference responsibilities

1. `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
   - SHA-256: `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`
   - responsibility: approved adult owner identity, stable facial landmarks/proportions, apparent age, natural skin tone and restrained neutral expression.
   - must_not_define: neutral eye-level camera/head projection in the output, Hairstyle-A design, body, outfit design, lighting or background; visible hair is context only.
2. `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`
   - SHA-256: `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`
   - responsibility: Hairstyle A only—near-center part, long straight loose dark-brown hair, low-to-moderate crown volume, long face-framing panels, realistic density, restrained highlights, below-chest length and tapered irregular ends.
   - must_not_define: gray mask, face/identity, skin, body, jacket, outdoor color cast, lighting or background.

Reference budget: 2 images. No previously generated Hairstyle-A raster is attached.

## Candidate authority

- only the Hairstyle-A high-camera/subject-looking-up projection: exposed upper forehead hairline, visible top/crown surface, near-center part path, crown volume, face-side panel displacement, outer silhouette and foreshortened length/ends under the specified perspective;
- no authority for standard eye-level face geometry, permanent expression, body, outfit design, other Hair-A views, Hairstyle B, lighting, background or Canon status.

## Prompt assembly

```text
Use case: identity-preserve. Create one adult technical hairstyle perspective-calibration image, HAIR_A_05_HIGH_CAMERA_LOOK_UP_v001. Generate independently from the two declared references; do not use approved HAIR_A_01/02/03/04 pixels or any generated Hair candidate.

Image 1 defines only the approved person's stable face identity, facial landmarks, proportions, apparent age, natural skin tone and restrained neutral expression. Do not preserve its eye-level camera/head projection and do not let its existing hair define the hairstyle. Image 2 defines only Hairstyle A: a near-center part, low-to-moderate natural crown volume, long straight loose dark-brown hair, long face-framing panels, realistic density, restrained highlights, below-chest length and naturally tapered irregular ends. Ignore Image 2's mask, person, identity, skin, jacket, outdoor cast and background.

The camera is clearly 25–35 degrees above the subject's eye line and pitched downward. The subject raises and extends the head naturally to look directly into the elevated lens, producing a genuine high-camera/subject-looking-up relationship rather than an eye-level portrait with only upward-pointing eyes. Keep the face near frontal with no more than 5 degrees yaw. Show increased but anatomically plausible upper-forehead hairline and top/crown surface, a readable near-center part continuing rearward across the visible crown, and realistic foreshortening of the lower face. Preserve the approved identity without enlarging eyes, shrinking the nose, sharpening the chin, narrowing the jaw or beautifying.

Project Hairstyle A into this pose: roots follow gravity and the backward head extension; the long face-side panels shift slightly backward and outward while remaining loose, straight and symmetrical enough to read both sides. Crown remains low-to-moderate and never puffy. Hair falls behind and beside the shoulders with smooth dark-brown lengths, fine irregular strands and tapered ends. Do not create bangs, waves, curls, short layers, ponytail, braid, bun, wet/plastic shine, red/purple cast, exposed bald seam or Hairstyle-B elements.

Exact 3:4 portrait, neutral gray-white seamless studio, soft even 5200–5600K lighting, technical photographic realism. Frame from clear space above the complete crown through upper waist, wide and low enough that the entire outer hair silhouette and every longest tip are visible with clear space below. Show only the upper portion of the same plain opaque pink Calibration Outfit. No jacket, jewelry, props, text, logo, watermark, collage or multiple views. Output one REVIEW_REQUIRED candidate only.
```

## QA status

### Attempt 1

- result: generated successfully from the two declared scoped references; no previously generated Hair raster was supplied.
- output: 1086x1448 RGB PNG, exact 3:4.
- built-in output: `/home/verdvana/.codex/generated_images/01a09edc-9182-7031-a3e5-d4b1ec7d7e75/exec-110c6c48-2bb9-496c-8612-f0c70273f758.png`
- project output: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/candidates/HAIR_A_05_HIGH_CAMERA_LOOK_UP_v001/HAIR_A_05_HIGH_CAMERA_LOOK_UP_v001.png`
- SHA-256: `0f8c8f5dfbfdc017df5082b79657e23657f52e520ea4d3d3f5d612dbade4404a`

## Visual QA result

- PASS: unmistakable high-camera/downward-axis and whole-head-raised relationship rather than an eye-level portrait with only upward eyes.
- PASS: near-frontal direction, strong but plausible facial foreshortening and recognizable approved identity context without overt beautification.
- PASS: upper forehead hairline, complete visible top/crown surface and rearward near-center part path are readable; crown is controlled and non-puffy.
- PASS: both long straight dark-brown face-side panels shift backward/outward consistently with the pose; restrained highlights and fine natural irregularity remain.
- PASS: complete outer silhouette and all tapered ends remain inside the frame with clear lower space; pink Calibration Outfit and neutral studio presentation are present.
- exact identity and high-camera Hairstyle-A match remain user-review decisions. Candidate stays `REVIEW_REQUIRED` and gains no Canon/downstream authority before explicit approval.

## User approval and promotion

- user statement: “批准 下一个”
- decision: `APPROVED`
- promoted asset ID: `OWNER_HAIR_A_05_HIGH_CAMERA_LOOK_UP_CANON_001`
- physical operation: `MOVE`
- current approved path/checksum: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_05_HIGH_CAMERA_LOOK_UP/OWNER_HAIR_A_05_HIGH_CAMERA_LOOK_UP_CANON_001.png` / `0f8c8f5dfbfdc017df5082b79657e23657f52e520ea4d3d3f5d612dbade4404a`
- candidate raster retained: `NO`
- full Canon lock: `NO`
