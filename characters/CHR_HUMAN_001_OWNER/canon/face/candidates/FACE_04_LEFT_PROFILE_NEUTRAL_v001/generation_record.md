# FACE_04_LEFT_PROFILE_NEUTRAL_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.22
identity_md_revision: draft_0.21
asset_id: FACE_04_LEFT_PROFILE_NEUTRAL
candidate_id: FACE_04_LEFT_PROFILE_NEUTRAL_v001
gate: "Gate 2 — Face Identity Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_L0_FACE_RIGHT_3Q_LIMITED
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
reference_count: 3
previous_ai_candidate_count: 0
evidence_limitation: "no matching-direction true-profile L0; L0_OWNER_012 is low-resolution three-quarter evidence only"
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_04_LEFT_PROFILE_NEUTRAL_v001/FACE_04_LEFT_PROFILE_NEUTRAL_v001.png"
pixel_storage_status: "MOVED_TO_CANON_THEN_TRANSCODED; CANDIDATE_RASTER_REMOVED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_04_LEFT_PROFILE_NEUTRAL/OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001.jpg"
qa_status: PASS_USER_APPROVED
```

## Reference plan

Inputs are supplied once, in this fixed order:

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — `canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`, SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`. Highest authority for the exact recognizable woman, skull and fine facial-feature relationships, adult age, neutral skin, rounded lower face and expression. It must not define the missing view-dependent left-profile projection by mere rotation artifacts.
2. `L0_OWNER_012` — `source/identity/raw/14.jpg`, SHA-256 `f7a83644f202ebec95134c6d115397b9f52f12e79b5fb227a6b79182026bd788`. Real same-person evidence only for face/nose pointing image-right, visible-side natural asymmetry and coarse orbit/nose/cheek/jaw depth. It must not define fine pure-profile silhouette, lens-neutral proportions, hair, clothing, makeup, skin color, lighting or background.
3. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — `canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`, SHA-256 `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`. Hairstyle A only. It must not define face, skin, skull, body, clothing, light or background.

Excluded: `FACE_05`, `FACE_03`, all other generated Face angles, every historical AI candidate, previous shots, and all mirrored images. The candidate is a conservative reconstruction with an explicit evidence gap, not a verified opposite-side profile.

## Final assembled prompt

```text
Use case: identity-preserve

Asset type: FACE_04_LEFT_PROFILE_NEUTRAL, L1 Face Canon candidate v001 for CHR_HUMAN_001_OWNER, governed by OWNER_L1_GENERATION_SPEC draft_1.22 and OWNER_IDENTITY_ANCHOR draft_0.21.

Input images, in fixed order: Image 1 is the approved front-neutral Face Canon and has highest authority for the exact recognizable woman, her skull proportions, fine facial-feature relationships, adult age, neutral-studio skin tone, rounded lower face and neutral expression. Image 2 is a low-resolution real same-person three-quarter photograph; it is authoritative only for the genuine direction with the face and nose pointing image-right, the visible-side natural asymmetry, and coarse orbit/nose/cheek/jaw depth. It is not a true-profile authority and must not determine fine profile silhouette or lens-neutral proportions. Image 3 is a source-derived masked Hairstyle A reference and is authoritative only for hair. Resolve identity conflicts in favor of Image 1.

Create exactly one new photorealistic neutral full left-profile portrait. Rotate the head about 85–90 degrees so the anatomical left facial plane is visible and the face/nose points image-right. Show a clean true profile rather than a three-quarter or near-profile view: one eye is principally visible, no far iris appears beyond the nasal bridge, and the forehead–nose–lips–chin silhouette reads clearly. The visible eye looks naturally straight ahead toward image-right, not toward the camera. Mouth naturally closed; expression gentle, neutral and relaxed.

This view has no matching-direction true-profile L0. Reconstruct it cautiously from Image 1's approved identity plus only Image 2's limited same-direction real depth evidence. Do not mirror FACE_05 or any other image. Do not copy, continue, or use FACE_03, FACE_05, another generated Face angle, any AI candidate, or a previous shot. Preserve the same recognizable woman as Image 1: soft rounded-oval face, natural medium almond eye, relaxed brow, natural nose identity, softly shaped lips, naturally full cheek volume, restrained low-soft cheekbone, rounded jaw transition, softly rounded non-pointed chin, adult age, skin tone and subtle natural asymmetry. Derive a conservative lens-neutral profile projection from the approved front dimensions and coarse Image 2 depth; do not invent a dramatic, doll-like or generically beautified profile. The nose must remain natural and moderate, never unusually tall, narrow, sharp, upturned or strongly projecting. Keep the chin rounded rather than tapered or pointed, without making it short, wide, heavy or recessed.

Do not inherit Image 2's phone-lens distortion, low resolution, camera-seeking gaze, hairstyle, black clothing, makeup, color cast, hard environment light or background. Image 3 must not influence face, skin, skull, body, clothing, light or background.

Hairstyle A only: near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels and tapered ends. Arrange the visible-side hair naturally behind the ear enough to keep the real ear, jawline and profile silhouette readable, while the remaining hair hangs loose behind the shoulder. No bun, updo, ponytail, Hairstyle B or A/B hybrid.

Exact 3:4 portrait, head top to upper chest, head approximately 65–72% of frame height, 85–105mm-equivalent portrait perspective, camera at eye height with horizontal optical axis, upright neutral head, coherent forehead/hairline/skull/crown/ear/jaw/chin projection. Do not tilt the head or create a dramatic shoulder pose. Neutral gray-white seamless studio, soft even low-contrast 5200–5600K illumination, neutral white balance and natural photographic skin texture. If clothing is visible, show only the authentic upper portion of the same pink high-cut one-piece Calibration Outfit, not a tank top or another garment.

Avoid three-quarter view, near-profile, face pointing image-left, mirroring, visible far iris, camera-seeking gaze, identity averaging, generic face, enlarged eye, high sharp cheekbone, pointed or upturned nose, excessive nose projection, pointed chin, narrowed jaw, face slimming, intense stare, smile, parted lips, age change, beauty filtering, whitening, heavy makeup, source styling leakage, updo, dramatic side light, wide-angle or top-down distortion, text, watermark, collage and multiple views.

One candidate image only. REVIEW_REQUIRED; do not label or imply Canon approval. The missing true-profile L0 evidence must remain disclosed for human review.
```

## Generation result

- generated_at: `2026-09-10T21:44:27+08:00`
- seed/settings: built-in `image_gen`; seed and detailed settings were not returned
- source output: `/home/verdvana/.codex/generated_images/01a089e9-1904-7443-9200-afbaa6608bae/exec-161c906d-2e27-46b8-b83e-f72c8eb25216.png`
- original project output: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_04_LEFT_PROFILE_NEUTRAL_v001/FACE_04_LEFT_PROFILE_NEUTRAL_v001.png` (record only; raster removed after promotion)
- output dimensions: 1086×1448, exact 3:4
- output SHA-256: `8e98187213ae2ef2a9a135611b34c5d828ff99ce9c8c3efcd7e61ecb12699c83`
- QA record: `QA.md`
- approval: subsequently approved unchanged; see Approval outcome below

## Approval outcome

- user decision: approved as Canon on `2026-09-10`
- promoted asset: `OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001`
- current approved path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_04_LEFT_PROFILE_NEUTRAL/OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_CANON_001.jpg`
- current approved JPG checksum: `b6c1d513a4ce8f32d70860de2dde2816ef5f1400c82e09f4550b96e9545798c4`
- source candidate PNG checksum: `8e98187213ae2ef2a9a135611b34c5d828ff99ce9c8c3efcd7e61ecb12699c83`
- format note: user-transcoded JPG is the active downstream Master; its accidental FACE_05 filename was corrected without re-encoding
- approval record: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_04_LEFT_PROFILE_NEUTRAL/approvals/APPROVAL_OWNER_FACE_04_LEFT_PROFILE_NEUTRAL_001.md`
- reproduction method: `characters/CHR_HUMAN_001_OWNER/canon/face/FACE_04_LEFT_PROFILE_NEUTRAL_METHOD.md`
- evidence note: approval accepts the generated profile as the current component but does not create missing matching-direction true-profile L0 evidence
- full release: `owner_v1.0` remains unlocked
