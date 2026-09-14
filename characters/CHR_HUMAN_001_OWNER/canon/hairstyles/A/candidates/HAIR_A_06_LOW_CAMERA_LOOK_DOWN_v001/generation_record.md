# HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.162
identity_md_revision: draft_0.150
asset_id: HAIR_A_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v001
gate: "Gate 4 — Hairstyle Canon"
model_tool: "built-in image_gen"
status: USER_REJECTED
approval_status: REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE]
reference_count: 2
previous_ai_hairstyle_a_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/candidates/HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v001/HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v001.png"
checksum_sha256: "3266b87456a60168005569bf5be799cdb39b7838ad9550f6c314aac02d0204ef"
qa_status: USER_REJECTED_FACE_RELIEF_AND_CROWN_VISIBILITY
```

## Authorization and lineage

The user approved HAIR_A_05 and requested the next asset. This authorizes exactly one `HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v001`. It is built independently from the approved front-neutral Face Master and deterministic L0 hair-only derivative. No approved HAIR_A_01–05, generated Hair candidate, Expression, Pose or Shot is supplied.

## Reference responsibilities

1. `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`, SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`. Defines only stable approved identity, age, facial landmarks/proportions, skin tone and restrained neutral expression. Must not define output camera/head projection, hairstyle, body, clothing, light or background.
2. `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`: `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`, SHA-256 `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`. Defines only near-center part, low-to-moderate crown, long straight loose dark-brown hair, face-side panels, density, restrained highlights, below-chest length and tapered irregular ends. Must not define mask, identity, skin, body, jacket, outdoor cast, light or background.

Reference budget: 2. Previous generated Hair pixels: 0.

## Candidate authority

- only Hairstyle-A projection under a low-camera/subject-looking-down relationship: under-jaw face-side panels, ear-side relations, gravity shift, outer silhouette, tip overlap/occlusion and visible full length;
- no authority for standard eye-level face geometry, permanent expression, body/pose, clothing, other Hair-A views, Hairstyle B, light, background or Canon status.

## Prompt assembly

```text
Use case: identity-preserve. Create one adult technical hairstyle perspective-calibration image, HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v001. Generate independently from the two references and do not use approved HAIR_A_01–05 or any generated Hair pixels.

Image 1 defines only the approved person's stable identity, face landmarks/proportions, age, skin tone and neutral closed-mouth expression. Do not preserve its eye-level projection or let its hair define the output. Image 2 defines only Hairstyle A: near-center part, controlled low-to-moderate crown, long straight loose dark-brown hair, long face-side panels, realistic density, restrained highlights, below-chest length and naturally tapered irregular ends. Ignore its mask, person, jacket, body, outdoor cast and background.

Place the camera clearly 20–30 degrees below the subject's eye line and pitch the optical axis upward. The subject lowers/flexes the whole head naturally to look directly down into the lower lens; do not keep the head neutral and move only the pupils down. Keep the face near frontal with no more than 5 degrees yaw. Show plausible low-angle/looking-down foreshortening: underside of chin is contextually readable, top/crown surface is reduced, and eyes look into the lens without beautification or identity redesign.

Project Hairstyle A naturally: gravity brings both long face-side panels slightly forward and inward beneath/beside the jaw, with readable but partly covered ear-side relations. Preserve the near-center hairline/part at the visible front while avoiding an exposed bald seam. Long straight dark-brown hair falls forward beside the shoulders; allow realistic overlap/occlusion among tips but keep the full outer silhouette and all longest tips visible. Controlled crown, fine irregular strands, restrained highlights and tapered non-blunt ends. No bangs, waves, curls, ponytail, braid, bun, wet/plastic shine, red/purple cast or Hairstyle B.

Exact 3:4 portrait, 85–105mm equivalent, neutral gray-white studio, soft even 5200–5600K light. Frame complete crown through upper waist with all hair edges and tips inside the frame and clear space below. Only the upper portion of the same opaque pink Calibration Outfit. No jacket, jewelry, props, text, logo, watermark, collage or multiple views. Output one REVIEW_REQUIRED candidate.
```

## QA status

### Attempt 1

- built-in output: `/home/verdvana/.codex/generated_images/01a09edc-9182-7031-a3e5-d4b1ec7d7e75/exec-596c1023-277d-4b91-965c-bbc8c69b1806.png`
- result: `TECHNICAL_QA_FAILED_CAMERA_HEIGHT`; not copied into the project.
- failure: the head is slightly lowered, but the camera reads near eye level or mildly high; excessive crown surface remains visible and the underside of the chin is not sufficiently projected. It therefore does not establish the required low-camera/upward-axis relationship.
- retry scope: change only the camera position/projection—place the lens clearly below the chin and pitch upward while the subject lowers the head toward it. Keep the same two references, identity scope, Hairstyle-A design, framing and exclusions.

### Attempt 2 — targeted camera retry

- result: generated successfully; 1086x1448 RGB PNG, exact 3:4.
- built-in output: `/home/verdvana/.codex/generated_images/01a09edc-9182-7031-a3e5-d4b1ec7d7e75/exec-a38cadbb-ce21-4af2-8231-48573ae5888d.png`
- project output: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/candidates/HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v001/HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v001.png`
- SHA-256: `3266b87456a60168005569bf5be799cdb39b7838ad9550f6c314aac02d0204ef`

## Visual QA result

- PASS: camera is visibly below the chin with upward optical projection; chin underside, lower jaw plane and restrained nostril bases are visible, and crown surface is reduced.
- PASS WITH REVIEW NOTE: gaze meets the lower lens; whole-head downward flexion and forward/inward panel swing are present only subtly and require user confirmation.
- PASS: near-center frontal part, controlled crown, long straight loose dark-brown panels, complete silhouette, full length and all tapered ends are readable.
- Candidate remains `REVIEW_REQUIRED`; low-angle face geometry cannot redefine identity.

## User rejection

- user feedback: facial relief is too three-dimensional for the approved person; the low-camera view cannot show this much crown part/top surface.
- decision: `USER_REJECTED`; v001 pixels are prohibited from v002 and downstream use.
