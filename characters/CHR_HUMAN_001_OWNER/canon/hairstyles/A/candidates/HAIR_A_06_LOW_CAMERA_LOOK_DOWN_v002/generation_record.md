# HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.164
identity_md_revision: draft_0.152
asset_id: HAIR_A_06_LOW_CAMERA_LOOK_DOWN
candidate_id: HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v002
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
rejected_candidate_pixels_used: false
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/candidates/HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v002/HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v002.png"
checksum_sha256: "16152484440428bbe5130cc4fcced4c3e702b52ca49926472fa68c7826a63faa"
qa_status: USER_REJECTED_PART_POSITION
```

## Responsibilities and exclusions

- `OWNER_FACE_FRONT_NEUTRAL_CANON_L1` (`4d657954...90fc4`) defines exact approved identity, including relatively soft/flatter facial relief; it must not define hair, eye-level projection, body, outfit, light or background.
- `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE` (`6eb98bb5...a2cd`) defines only Hair A's near-center front part, long straight loose dark-brown panels, controlled volume, density, length and tapered ends; it must not define mask, identity, body, jacket, cast or background.
- v001 and all approved/generated Hair-A pixels are excluded.

## Prompt assembly

See the exact built-in ImageGen prompt in the generation call. Core corrections: low camera plus whole-head downward flexion; preserve the approved person's softer, less sculpted facial relief; show no crown/top surface and no rearward part, allowing only a tiny frontal part trace; keep full long straight Hair-A edges and tips.

## QA status

### Attempt 1

- output moderation passed, but technical QA failed before project storage: facial relief improved, yet the image still showed extensive crown surface and a long part line.
- built-in output: `/home/verdvana/.codex/generated_images/01a09edc-9182-7031-a3e5-d4b1ec7d7e75/exec-d401ef92-72cf-4507-b4cd-513a07ed7982.png`

### Attempt 2 — crown/part targeted retry

- result: generated 1086x1448 RGB PNG, exact 3:4.
- project output: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/candidates/HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v002/HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v002.png`
- SHA-256: `16152484440428bbe5130cc4fcced4c3e702b52ca49926472fa68c7826a63faa`
- PASS: softer/flatter facial relief; no crown plane, scalp exposure or center-part line; clear below-chin upward projection; complete long straight Hair-A silhouette and tips.
- Candidate remains `REVIEW_REQUIRED`.

## User rejection

- face correction accepted as close; hairstyle rejected because the root-flow/part origin reads clearly image-right, while fixed Hairstyle A places it slightly image-left of center.
- v002 pixels are prohibited from v003 and downstream use.
