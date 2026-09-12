# BODY_03_RIGHT_3Q_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.43
identity_md_revision: draft_0.40
body_md_revision: draft_0.17
asset_id: BODY_03_RIGHT_3Q
candidate_id: BODY_03_RIGHT_3Q_v001
gate: "Gate 3 — Body Canon"
model_tool: "built-in image_gen"
status: REJECTED
approval_status: REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_RIGHT_3Q_NEUTRAL_CANON_L1
  - OWNER_BODY_FRONT_CANON_L1
reference_count: 2
previous_ai_body_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_03_RIGHT_3Q_v001/BODY_03_RIGHT_3Q_v001.png"
qa_status: FAIL_USER_REJECTED_HEEL_CONTACT_AND_HOSIERY_LINE
checksum_sha256: "27a4b287da1f7da044ce080502de4a72df3c92613524fa3497c5dc0451f50ead"
```

## Gate and lineage decision

The approved `BODY_02` opens the next planned Gate-3 item, `BODY_03_RIGHT_3Q`. This candidate is reconstructed independently from the approved right-three-quarter Face Master and active front Body Master. `BODY_02`, every historical Body candidate, failed/unreviewed image, previous shot and mirror operation are excluded.

## Reference plan

1. `OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001` — authoritative only for recognizable right-three-quarter face identity, adult age, neutral skin appearance and orientation: anatomical right facial plane principally visible, nose pointing image-right. It must not define body geometry, pose, outfit, hosiery, hair length, lighting or background.
2. `OWNER_BODY_01_FRONT_CANON_002` — authoritative for the approved 168 cm / 60 kg physical target, head-to-body scale, shoulder/torso/waist/hip relationship, waist/hip ratio, arm and leg lengths, natural soft-tissue volume, straight lower-leg intent, foot scale, visible Hairstyle A appearance, Calibration Outfit construction and the exact `15D matte nude` hosiery appearance. It must not define right-three-quarter facial projection, unapproved side/rear depth geometry, camera angle, lighting, background, other hosiery variants or episode wardrobe.

Reference budget: two images total. No previous generated Body view is supplied.

## Authoritative scope of this candidate

- candidate right-three-quarter body silhouette and conservative depth relationship;
- preservation of the approved 168 cm / 60 kg stature, limb lengths and waist/hip ratio through a coherent right-three-quarter turn;
- BODY_03 neutral standing orientation and anatomy for review.

## Must not define

- a new face identity, age, skin tone, hairstyle design or hair color;
- new front-body proportions, weight, stature or waist/hip ratio;
- left-three-quarter, pure side or rear body geometry;
- final Hairstyle A or Gate-7 hosiery Canon;
- episode wardrobe, expression, performance pose, lighting or background;
- Canon status before explicit user approval.

## Prompt assembly

```text
Use case: identity-preserve
Asset type: BODY_03_RIGHT_3Q L1 technical character-proportion calibration candidate for CHR_HUMAN_001_OWNER

Create exactly one photorealistic, non-sexual, neutral full-length right-three-quarter technical reference of the adult woman. Image 1 is authoritative only for her exact recognizable right-three-quarter face identity, natural adult age, neutral skin appearance and orientation: anatomical right facial plane principally visible, nose pointing image-right. Image 2 is authoritative for the approved 168 cm / 60 kg body target, head-to-body scale, shoulder-to-torso relationship, natural chest/waist/hip soft-tissue volume, waist/hip ratio, arm and leg lengths, straight lower-leg intent, foot scale, visible Hairstyle A appearance, Calibration Outfit construction and the exact 15D matte nude hosiery appearance. Do not use either image outside its declared scope. Do not use, imitate or mirror BODY_02 or any other generated Body candidate.

Turn the entire head, shoulders, ribcage, pelvis, knees and feet together into a natural right three-quarter view of approximately 35–45 degrees. The anatomical right facial and body planes are principally visible and the face points toward image-right, matching Image 1. No torso twist, contrapposto, fashion pose or crossed limbs. Preserve Image 2's approved 168 cm / 60 kg stature, coherent head-to-body ratio, limb lengths, waist placement, waist/hip ratio and natural real-person volume exactly in intent. Do not slim, widen, shorten, elongate, shrink the head or create a generic fashion-model body. Conservatively infer only the depth required by this view; do not let the turn change chest, waist, hip, thigh or calf volume.

Neutral standing calibration posture: weight evenly distributed, shoulders level, arms relaxed with hands fully visible and a small readable gap from the torso, fingers natural, legs uncrossed, both feet flat and aligned with the same right-three-quarter body orientation. Keep both knee-shin-ankle chains anatomically straight and stable with natural calf volume. Head and torso share the same yaw; eyes look naturally toward the camera, mouth closed, expression neutral.

Use the exact Calibration Outfit shown by role in Image 2: plain opaque pink high-cut one-piece athletic swimsuit, continuous closed-foot light-nude 15D matte/velvet-finish sheer pantyhose, and no shoes. The textile continuously covers hips, thighs, knees, calves, ankles, heels, insteps and every toe with a subtle translucent fabric veil. Burgundy toenail polish may be softly visible beneath the textile. No toe seam, reinforced toe, ankle cutoff, bare toes, latex, PVC, plastic, wet coating, body paint or shiny synthetic skin.

Keep Hairstyle A consistent with Image 2: long straight loose dark-brown hair, near-center part, controlled low-to-moderate crown volume, long face-framing panels and tapered ends. Preserve identity from Image 1; do not average the two faces, beautify, slim the face, enlarge the eyes, sharpen the nose or point the chin.

Exact 3:4 portrait, complete head, hair, both hands, heels and toes with 5–8% breathing room. Level 70–85mm-equivalent lens-neutral camera centered between waist and lower chest. Neutral gray-white seamless studio, soft even 5200–5600K illumination, natural skin and textile texture. No props, furniture, scenery, dramatic styling, text, logo, watermark, collage or multiple views. Output one REVIEW_REQUIRED candidate only; do not label or imply Canon approval.
```

## Attempt result

- generated_at: `2026-09-12`
- built-in output: `/home/verdvana/.codex/generated_images/01a09467-3db0-70a2-bf86-1fb58ecbbfb6/exec-882f60d9-1ee4-4785-9ee6-e03213430a47.png` (tool cache; project-authoritative candidate saved at `output_path`)
- result: one 1086×1448 exact-3:4 PNG generated and saved as the unique project candidate raster
- QA: `AI_TECHNICAL_PRECHECK_PASS_USER_REVIEW_REQUIRED`; identity direction, right-three-quarter body orientation, proportions, outfit, anatomy and neutral studio presentation pass visual precheck. The subtle 15D textile visibility over insteps/toes remains a focused human-review item. No Canon promotion has occurred.

## User rejection

On 2026-09-12 the user rejected v001 because one heel floats above the floor and a spurious transverse line appears where the toes meet the forefoot. v002 must keep both heels and plantar surfaces naturally grounded and must render uninterrupted 15D textile from ankle through instep/forefoot to toes, with no toe seam, reinforced-toe boundary or color/opacity band. v001 pixels are excluded from v002.
