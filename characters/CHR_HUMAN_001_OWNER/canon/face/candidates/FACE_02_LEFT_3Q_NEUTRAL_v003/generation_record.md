# FACE_02_LEFT_3Q_NEUTRAL_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.13
identity_md_revision: draft_0.13
asset_id: FACE_02_LEFT_3Q_NEUTRAL
candidate_id: FACE_02_LEFT_3Q_NEUTRAL_v003
gate: "Gate 2 — Face Identity Canon"
model_tool: "built-in image_gen"
status: USER_REJECTED
approval_status: REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_count: 3
seed_settings: "built-in image_gen; seed and detailed settings not returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_02_LEFT_3Q_NEUTRAL_v003/FACE_02_LEFT_3Q_NEUTRAL_v003.png"
qa_status: FAIL_USER_IDENTITY_REVIEW
```

## Reference plan

| Priority | Reference ID | Responsibility | Must not define |
|---:|---|---|---|
| 1 | `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` | exact approved identity, rounded chin family, all facial-feature relationships, age, skin tone and neutral expression | new 3/4 geometry alone, body, outfit, Hairstyle B, background |
| 2 | `L0_OWNER_013` | real left-three-quarter depth, nose projection, cheek/jaw plane and ear placement | chin pointedness, smile, gaze, makeup, skin tone, light, ornaments, hair, clothing, background |
| 3 | `OWNER_HAIRSTYLE_A_FACE_MASKED_001` | Hairstyle A only | face, expression, skin, skull, body, clothing, outdoor light/color, background |

Paths are resolved from `registries/reference_sets.yaml` and the approved Face method. Reference count is three. v001 and v002 are excluded as image inputs.

## Locked user-confirmed properties

Preserve the v002-approved result only as written constraints: same identity direction, softly lowered cheekbone contour, gentle relaxed gaze, moderate left three-quarter angle, nose and near/far eye relationship, skin tone, Hairstyle A, eye-level camera, head-to-upper-chest framing, neutral studio and pink Calibration Outfit presentation.

## Single permitted change

Make the bottom contour of the chin slightly more circular and softly rounded. Modify only the terminal curvature beneath the center of the lower lip. Preserve chin vertical length, chin projection, jaw width, jaw angle, cheek volume, mouth position and every other facial feature. Do not create a broad, short, recessed, heavy, double or childlike chin.

## Final assembled prompt

Use case: identity-preserve

Asset type: `FACE_02_LEFT_3Q_NEUTRAL`, L1 Face Canon candidate v003 for `CHR_HUMAN_001_OWNER`, using `OWNER_L1_GENERATION_SPEC` draft_1.13 and `OWNER_IDENTITY_ANCHOR` draft_0.13.

Image 1 is authoritative for the exact approved identity, every facial-feature relationship, adult age, neutral-studio skin tone, natural eye geometry, soft rounded jaw/chin family and neutral expression. Image 2 is authoritative only for real left-three-quarter orbital depth, nose projection, cheek/jaw planes, visible ear placement and face-points-image-left geometry. Image 3 is authoritative only for Hairstyle A. Resolve all identity conflicts in favor of Image 1. Do not use or imitate any previous FACE_02 generated image.

Create exactly one fresh photorealistic left-three-quarter neutral portrait. Preserve the user-confirmed target as written: the same recognizable woman; softly lowered, non-prominent cheekbone contour; gentle relaxed gaze with unchanged eye geometry; moderate head turn toward image-left with the anatomical left facial plane principally visible; same nose projection, near/far eye relationship, skin tone, adult age, neutral closed mouth, Hairstyle A, eye-level camera, framing and studio presentation.

Make one and only one refinement: make the very bottom terminal curve of the chin a little more circular and softly rounded. Change only this small central chin contour beneath the lower lip. Keep the exact chin vertical length and forward projection, jaw width, jaw angle, cheek volume, lower-lip position and every other facial feature unchanged. The result must remain an adult natural rounded chin—not broad, short, recessed, heavy, doubled, swollen or childlike.

Hairstyle A only: near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels and tapered ends. No bun, updo, Hairstyle B or hybrid.

Exact 3:4 portrait; head top to upper chest; 85–105mm-equivalent perspective; eye-height camera; upright neutral head. Neutral gray-white seamless studio, soft even 5200–5600K lighting, natural skin texture. Visible clothing is only the authentic upper portion of the pink high-cut one-piece Calibration Outfit.

Avoid any change to identity, cheekbone, gaze, eyes, brows, nose, lips, age, head angle, skin tone, hairstyle, camera or composition; avoid pointed chin, wide/heavy chin, shortened chin, changed jaw, smile, squint, beauty filter, heavy makeup, wide-angle distortion, text, watermark, collage or multiple views.

One candidate only. `REVIEW_REQUIRED`; do not label or imply Canon approval.

## Generation settings/result

- generated_at: `2026-09-10T14:34:12+08:00`
- seed/settings: built-in `image_gen`; seed and detailed settings were not returned
- source output: `/home/verdvana/.codex/generated_images/01a089e9-1904-7443-9200-afbaa6608bae/exec-9e8c9343-a7ad-4453-b863-620e22abff5d.png`
- output_path: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_02_LEFT_3Q_NEUTRAL_v003/FACE_02_LEFT_3Q_NEUTRAL_v003.png`
- output_dimensions: `1086x1448`
- output_checksum: `e8e4c1be0418236a858fca59a7538471efaad8ef19605967925a17d887a6ec3a`
- QA_record: `QA.md`

## User review outcome

- verdict: rejected
- blocker: facial features drifted from the intended identity
- next method: restore the complete v001 prompt and append only the three concise cheekbone, chin and gaze constraints
- downstream/reference eligibility: none
