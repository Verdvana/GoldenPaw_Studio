# HAIR_A_04_BACK_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.158
identity_md_revision: draft_0.146
hairstyle_document: canon/hairstyles/A/HAIRSTYLE.md
asset_id: HAIR_A_04_BACK
candidate_id: HAIR_A_04_BACK_v001
gate: "Gate 4 — Hairstyle Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_BODY_BACK_CANON_L1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
reference_count: 2
previous_ai_hairstyle_a_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_04_BACK/OWNER_HAIR_A_04_BACK_CANON_001.png"
checksum_sha256: "91128987bc4aade21f7b7fd3a7b9bd24d2ca3d0100847214844b702741852e53"
qa_status: PASS_USER_APPROVED
```

## Authorization and lineage

The user requested the next asset after approving `HAIR_A_03` and confirmed “继续”. This authorizes exactly one `HAIR_A_04_BACK_v001` candidate. Because the face is fully hidden in an exact rear view, the smallest relevant set uses the approved rear Body Master for orientation/shoulder-neck/outfit context and the deterministic L0 hair-only derivative for Hairstyle A. No Face pixel is necessary, and no approved `HAIR_A_01/02/03`, generated Hair candidate, Expression, Pose or Shot is supplied.

## Reference responsibilities

1. `OWNER_BODY_BACK_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_06_BACK_v001/BODY_06_BACK_v001.png`
   - SHA-256: `2344a37e9355bbe1fb49865b5039275cebbbe5cfb043738b7e2edb6c777add7c`
   - responsibility: exact 180-degree back-facing head/body alignment, approved shoulder/neck and upper-torso proportions, neutral upright posture, and the visible rear portion of the pink Calibration Outfit.
   - must_not_define: Hairstyle-A rear design, crown structure, rear hair mass, length, density, ends or highlights; also must not define face, lighting, background, lower-body crop or hosiery in this Hair candidate.
2. `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`
   - SHA-256: `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`
   - responsibility: Hairstyle A only—near-center part translated into natural top/crown flow, long straight loose dark-brown hair, low-to-moderate crown volume, believable density, smooth lengths with subtle irregularity, below-chest equivalent length, restrained highlights and naturally tapered irregular ends.
   - must_not_define: gray mask, face/identity, skin, body, pink jacket, outdoor color cast, lighting or background.

Reference budget: 2 images. No previously generated Hairstyle-A raster is attached.

## Candidate authority

- only the exact 180-degree rear Hairstyle-A structure: top-flow/crown, rear-head contour, rear mass distribution, neck/shoulder fall, outer silhouette, straight loose texture, density, tonal response, full length and tapered ends;
- no authority for face identity, skin, expression, body proportions, outfit design, other Hair-A views, Hairstyle B, lighting, background or Canon status.

## Prompt assembly

```text
Use case: identity-preserve. Asset: HAIR_A_04_BACK_v001, one adult technical hairstyle reference for CHR_HUMAN_001_OWNER, Identity draft_0.144 and spec draft_1.156. Generate independently from the two declared references; do not use approved HAIR_A_01/02/03 pixels or any generated Hair candidate.

Image 1 (`OWNER_BODY_BACK_CANON_L1`) defines only the exact 180-degree rear-facing head/body alignment, approved shoulder/neck and upper-torso proportions, neutral upright posture, and visible rear portion of the pink Calibration Outfit. Rebuild and replace all visible hair from the Hairstyle-A design below; Image 1's hair has no authority for crown, rear structure, mass, density, length or ends. Do not use its full-body framing, lower body or hosiery. Image 2 (`OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`) defines only Hairstyle A: near-center part translated into a natural crown flow, low-to-moderate non-puffy crown, long straight loose dark-brown hair, believable density, smooth lengths with fine natural strand irregularity, restrained highlights, below-chest equivalent length and naturally tapered irregular ends. Ignore its gray mask, person, identity, jacket, body, outdoor cast and background.

Show a strict centered 180-degree back view: the face, cheek, nose, eye and facial side edges are completely invisible; head and shoulders point directly away from camera with no turn or tilt. Reveal the complete top of the hairstyle and rear cranial contour at true eye level. The near-center front part is not artificially exposed from behind; instead it produces a subtle centered-to-near-centered top flow that closes naturally over the crown. Hair lies smooth and straight from crown to ends, falls freely over the upper back and partly over both shoulders, with controlled low-to-moderate volume, realistic scalp-root behavior, a broad but not helmet-like rear mass, slight natural left-right irregularity, fine flyaways, and a soft naturally tapered non-blunt lower edge. Length corresponds to the fixed front below-chest design and reaches the mid-to-lower back in this rear projection. Keep both side edges readable; no ear-tuck redesign.

Do not introduce bangs, waves, curls, short layers, U-cut or ruler-straight blunt cut, ponytail, braid, bun, extensions, excessive width/volume, teased crown, wet look, plastic shine, red/purple cast, center bald line, visible face, or any Hairstyle-B element.

Exact 3:4 portrait, true eye-level 85–105mm photographic perspective, crop from complete crown through upper waist. Frame wide and low enough to show the entire top, both outer hair edges and every longest rear hair tip with a clear 5–8% band of background or pink garment below all tips; no hair touches or exits the frame. Neutral gray-white seamless studio, soft even 5200–5600K light, realistic hair and skin, neutral color. Show only the rear upper portion of the same plain opaque pink one-piece Calibration Outfit. No props, text, logo, watermark, collage or multiple views. Hairstyle alone is under review; do not redesign body, skin or clothing. Produce one REVIEW_REQUIRED image only.
```

## QA status

Attempt 1 (2026-09-14): built-in ImageGen returned no image because output moderation classified the result as `sexual`. No raster was created or accepted. One targeted retry is authorized by the imagegen workflow; the retry keeps the same reference set and asset scope while reframing the request as a neutral, head-and-hair-centered technical archive image with minimal visible torso.

### Attempt 2 — targeted technical-archive retry

- result: generated successfully from the same two declared scoped references; no previously generated Hair raster was supplied.
- output: 1086x1448 RGB PNG, exact 3:4.
- built-in output: `/home/verdvana/.codex/generated_images/01a09edc-9182-7031-a3e5-d4b1ec7d7e75/exec-378240c8-f7ba-41da-9d88-e4db486d5a97.png`
- project output: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/candidates/HAIR_A_04_BACK_v001/HAIR_A_04_BACK_v001.png`
- SHA-256: `91128987bc4aade21f7b7fd3a7b9bd24d2ca3d0100847214844b702741852e53`

## Visual QA result

- PASS: exact 3:4 single-view composition and centered 180-degree rear direction; no face or facial side edge is visible.
- PASS: complete crown, rear-head contour and natural subtle top flow are readable without a hard artificial scalp seam.
- PASS: long predominantly straight loose dark-brown fall, restrained neutral highlights, controlled crown/rear mass, realistic density and fine irregularity are present.
- PASS: the rear projection reaches the lower back; both outer edges and all tapered mildly irregular tips remain fully visible with clear space below.
- PASS: only the rear upper pink Calibration Outfit is visible; no jacket, source outdoor background, prop, text, logo, watermark or Hairstyle-B element appears.
- exact Hairstyle-A match remains a user-review decision. Candidate stays `REVIEW_REQUIRED` and gains no Canon/downstream authority before explicit approval.

## User approval and promotion

- user statement: “批准，下一项”
- decision date: 2026-09-14
- decision: `APPROVED`
- promoted asset ID: `OWNER_HAIR_A_04_BACK_CANON_001`
- physical operation: `MOVE`
- original candidate path/checksum: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/candidates/HAIR_A_04_BACK_v001/HAIR_A_04_BACK_v001.png` / `91128987bc4aade21f7b7fd3a7b9bd24d2ca3d0100847214844b702741852e53`
- current approved path/checksum: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_04_BACK/OWNER_HAIR_A_04_BACK_CANON_001.png` / unchanged
- candidate raster retained: `NO`
- approval record: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_04_BACK/approvals/APPROVAL_OWNER_HAIR_A_04_BACK_001.md`
- full Canon lock: `NO`
