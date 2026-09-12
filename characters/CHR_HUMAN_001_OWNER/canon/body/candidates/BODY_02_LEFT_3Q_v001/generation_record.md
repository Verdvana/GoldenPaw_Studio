# BODY_02_LEFT_3Q_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.42
identity_md_revision: draft_0.39
body_md_revision: draft_0.16
asset_id: BODY_02_LEFT_3Q
candidate_id: BODY_02_LEFT_3Q_v001
gate: "Gate 3 — Body Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_LEFT_3Q_NEUTRAL_CANON_L1
  - OWNER_BODY_FRONT_CANON_L1
reference_count: 2
previous_ai_body_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_02_LEFT_3Q_v001/BODY_02_LEFT_3Q_v001.png"
pixel_storage_status: "MOVED_TO_CANON; CANDIDATE_RASTER_NOT_RETAINED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_02_LEFT_3Q/OWNER_BODY_02_LEFT_3Q_CANON_001.png"
current_promoted_checksum_sha256: "f364b5c9b398c0c786964ffb8932707c7d657f997b8344abdd31a47b4322f4aa"
qa_status: PASS_USER_APPROVED
checksum_sha256: "f364b5c9b398c0c786964ffb8932707c7d657f997b8344abdd31a47b4322f4aa"
```

## Gate and lineage decision

Gate 2 is complete and the active `BODY_01_FRONT` component is approved, so the next planned Gate-3 item is `BODY_02_LEFT_3Q`. This candidate is constructed in parallel from two approved scoped Masters. No historical Body candidate, failed/unreviewed image, previous shot, L0 personal photograph, material photograph or episode asset is supplied.

The approved front Body Master is used because the user explicitly authorized its 168 cm / 60 kg target, visible Hairstyle A, limb proportions and waist/hip ratio for other character assets. It does not define the new left-three-quarter depth geometry by itself; that geometry remains a conservative candidate interpretation subject to user review.

## Reference plan

1. `OWNER_FACE_02_LEFT_3Q_NEUTRAL_CANON_001` — authoritative only for the recognizable left-three-quarter face identity, adult age, neutral closed-mouth expression, skin appearance and orientation: anatomical left facial plane principally visible, nose pointing image-left. It must not define body geometry, pose, outfit, hosiery, hair length, lighting or background.
2. `OWNER_BODY_01_FRONT_CANON_002` — authoritative for the approved 168 cm / 60 kg physical target, head-to-body scale, shoulder/torso/waist/hip relationship, waist/hip ratio, arm and leg lengths, natural soft-tissue volume, straight lower-leg intent, foot scale, visible Hairstyle A appearance, Calibration Outfit construction and the exact `15D matte nude` hosiery appearance. It must not define left-three-quarter facial projection, unapproved side/rear depth geometry, camera angle, lighting, background, other hosiery colors/finishes/deniers or episode wardrobe.

Reference budget: two images total. Each responsibility is scoped, and no reference is allowed to redefine a domain outside the list above.

## Authoritative scope of this candidate

- candidate left-three-quarter body silhouette and depth relationship;
- preservation of the already approved 168 cm / 60 kg stature, head-to-body ratio, limb lengths and waist/hip ratio while turning as one rigid neutral body unit;
- BODY_02 neutral standing orientation and anatomy for review.

## Must not define

- a new face identity, age, skin tone, hairstyle design or hair color;
- a new front-body proportion, weight, stature or waist/hip ratio;
- final Hairstyle A Canon beyond the approved input scope;
- hosiery materials other than `15D matte nude`, or final reusable Gate-7 textile authority;
- episode wardrobe, expression, performance pose, lighting, background, right-three-quarter, side or rear body geometry;
- any downstream Canon status before explicit user approval.

## Prompt assembly

```text
Use case: identity-preserve
Asset type: BODY_02_LEFT_3Q L1 technical character-proportion calibration candidate for CHR_HUMAN_001_OWNER

Create exactly one photorealistic, non-sexual, neutral full-length left-three-quarter technical reference of the adult woman. Image 1 is authoritative only for her exact recognizable left-three-quarter face identity, natural adult age, neutral skin appearance and orientation: anatomical left facial plane principally visible, nose pointing image-left. Image 2 is authoritative for the approved 168 cm / 60 kg body target, head-to-body scale, shoulder-to-torso relationship, natural chest/waist/hip soft-tissue volume, waist/hip ratio, arm and leg lengths, straight lower-leg intent, foot scale, visible Hairstyle A appearance, Calibration Outfit construction and the exact 15D matte nude hosiery appearance. Do not use either image to redefine properties outside those declared roles.

Turn the entire head, shoulders, ribcage, pelvis, knees and feet together into a natural left three-quarter view of approximately 35–45 degrees. The anatomical left facial and body planes are principally visible and the face points toward image-left, matching Image 1. No torso twist, contrapposto, fashion pose or crossed limbs. Preserve Image 2's approved 168 cm / 60 kg stature, coherent head-to-body ratio, limb lengths, waist placement, waist/hip ratio and natural real-person volume exactly in intent; do not slim, widen, shorten, elongate, shrink the head or create a generic fashion-model body. Conservatively infer only the depth required by this view. Do not let the turn change chest, waist, hip, thigh or calf volume.

Neutral standing calibration posture: weight evenly distributed, shoulders level, arms relaxed with hands fully visible and a small readable gap from the torso, fingers natural, legs uncrossed, both feet flat and aligned with the same left-three-quarter body orientation. Keep both knee-shin-ankle chains anatomically straight and stable with natural calf volume. Head and torso share the same yaw; eyes look naturally toward the camera, mouth closed, expression neutral.

Use the exact Calibration Outfit shown by role in Image 2: plain opaque pink high-cut one-piece athletic swimsuit, continuous closed-foot light-nude 15D matte/velvet-finish sheer pantyhose, and no shoes. The textile continuously covers hips, thighs, knees, calves, ankles, heels, insteps and every toe with a subtle translucent fabric veil. Burgundy toenail polish may be softly visible beneath the textile. No toe seam, reinforced toe, ankle cutoff, bare toes, latex, PVC, plastic, wet coating, body paint or shiny synthetic skin.

Keep Hairstyle A consistent with Image 2: long straight loose dark-brown hair, near-center part, controlled low-to-moderate crown volume, long face-framing panels and tapered ends. Preserve identity from Image 1; do not average the two faces, beautify, slim the face, enlarge the eyes, sharpen the nose or point the chin.

Exact 3:4 portrait, complete head, hair, both hands, heels and toes with 5–8% breathing room. Level 70–85mm-equivalent lens-neutral camera centered between waist and lower chest. Neutral gray-white seamless studio, soft even 5200–5600K illumination, natural skin and textile texture. No props, furniture, scenery, dramatic styling, text, logo, watermark, collage or multiple views. Output one REVIEW_REQUIRED candidate only; do not label or imply Canon approval.
```

## Attempt result

- generated_at: `2026-09-12`
- built-in output: `/home/verdvana/.codex/generated_images/01a09467-3db0-70a2-bf86-1fb58ecbbfb6/exec-0bb3b1d1-fb26-4098-afec-c30c5045916f.png` (tool cache; project-authoritative candidate is saved at `output_path`)
- result: one 1086×1448 exact-3:4 PNG generated and saved as the unique project candidate raster
- QA: `AI_TECHNICAL_PRECHECK_PASS_USER_REVIEW_REQUIRED`; identity, view, body continuity, outfit and anatomy pass visual precheck. The very subtle 15D textile veil across insteps/toes remains a focused human-review item. No Canon promotion has occurred.

## User approval

On 2026-09-12, after reviewing this candidate, the user stated: “完美，下一项”. The candidate was moved unchanged to `OWNER_BODY_02_LEFT_3Q_CANON_001`. This approves the scoped left-three-quarter Body component but does not lock the complete `owner_v1.0` release.
