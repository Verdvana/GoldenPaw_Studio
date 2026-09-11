# FACE_05_RIGHT_PROFILE_NEUTRAL_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.19
identity_md_revision: draft_0.18
asset_id: FACE_05_RIGHT_PROFILE_NEUTRAL
candidate_id: FACE_05_RIGHT_PROFILE_NEUTRAL_v002
gate: "Gate 2 — Face Identity Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_L0_FACE_PROFILE_IMAGE_LEFT
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
reference_count: 3
previous_ai_candidate_count: 0
prompt_basis: "v001 source prompt plus one nasal-size refinement; v001 pixels excluded"
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_05_RIGHT_PROFILE_NEUTRAL_v002/FACE_05_RIGHT_PROFILE_NEUTRAL_v002.png"
pixel_storage_status: "MOVED_TO_CANON_THEN_TRANSCODED; CANDIDATE_RASTER_REMOVED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_05_RIGHT_PROFILE_NEUTRAL/OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001.jpg"
qa_status: PASS_USER_APPROVED
```

## Reference plan

Same three sources, same order and same isolated responsibilities as v001:

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`, SHA-256 `efda86babb6caeac5991515979e77ddf61e5a2776cd8e0819c9215b125d9f374`: exact identity, fine geometry, adult age, neutral skin and expression authority.
2. `L0_OWNER_009` (`11.jpg`), SHA-256 `948a092a360192af3f8718b27e35562ca5e14a21022e1161f8449be75b830a46`: real image-left-pointing right-profile silhouette, depth, ear and jaw/neck geometry only; must not define styling, makeup, skin or clothing.
3. `OWNER_HAIRSTYLE_A_FACE_MASKED_001`, SHA-256 `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`: Hairstyle A only; must not define face, skin, skull, body, clothing, light or background.

No v001 pixels, FACE_02, FACE_03, mirror, previous shot or other generated candidate is supplied.

## Single permitted change

Reduce the profile nose very slightly by decreasing only nasal tip bulk and forward projection. Preserve the nose root position, bridge length and curve, dorsum angle, alar/nostril structure, nasolabial angle, philtrum, lips, chin, jaw and every other confirmed feature. Do not make the nose narrow, sharp, upturned, shortened at the bridge, or generically beautified.

## Final assembled prompt

```text
Use case: identity-preserve

Asset type: FACE_05_RIGHT_PROFILE_NEUTRAL, L1 Face Canon candidate v002 for CHR_HUMAN_001_OWNER, governed by OWNER_L1_GENERATION_SPEC draft_1.19 and OWNER_IDENTITY_ANCHOR draft_0.18.

Input images: Image 1 is the approved front-neutral Face Canon and has highest authority for the exact recognizable woman, skull and facial-feature relationships, adult age, neutral-studio skin tone, fine facial geometry and neutral expression. Image 2 is the strongest real same-person profile photograph; it is authoritative only for her genuine right-profile geometry with the face and nose pointing image-left: forehead-to-nose bridge, orbital depth, philtrum, lips, rounded chin, jaw-to-ear relationship, visible ear placement and jaw/neck transition. Image 3 is a source-derived masked Hairstyle A reference and is authoritative only for hair. Resolve every identity conflict in favor of Image 1.

Create exactly one new photorealistic neutral full right-profile portrait. Rotate the head about 85–90 degrees so the anatomical right facial plane is visible and the face/nose points image-left. Show a clean true profile rather than a three-quarter view: one eye is principally visible, no far iris appears beside the nasal bridge, and the forehead–nose–lips–chin silhouette reads clearly. The visible eye looks naturally straight ahead toward image-left, not toward the camera. Mouth naturally closed; expression neutral, gentle and relaxed. Reconstruct from the three scoped inputs in parallel; do not mirror another Canon and do not copy or continue any AI candidate.

Preserve the same recognizable woman as Image 1: skull proportions, natural medium almond eye, brow, softly shaped lips, naturally full cheek volume, restrained cheekbone, rounded jaw transition, softly rounded non-pointed chin, adult age, skin tone and natural asymmetry. Use Image 2 only for view-dependent real profile geometry. Do not inherit Image 2's sideways/glancing eye pose, widened eye, styled updo, formal makeup, retouching, warm/pink color cast, directional studio light, black clothing or pink background. Image 3 must not influence face, skin, skull, body, clothing, light or background. Make one and only one restrained refinement relative to the documented v001 method: make the profile nose slightly smaller by reducing only the nasal tip bulk and forward projection a little. Preserve the exact nose root position, bridge length and curve, dorsum angle, alar and nostril structure, nasolabial angle, philtrum and all other features. Do not make the nose narrow, sharp, upturned, bridge-shortened or generically beautified. Keep the lips, rounded chin, chin projection, jaw, ear, eye, cheek and every non-nasal feature unchanged in design.

Hairstyle A only: near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels and tapered ends. Arrange the visible-side hair naturally behind the ear enough to keep the real ear, jawline and profile silhouette readable, while the remaining hair hangs loose behind the shoulder. No bun, updo, ponytail, Hairstyle B or A/B hybrid.

Exact 3:4 portrait, head top to upper chest, head approximately 65–72% of frame height, 85–105mm-equivalent portrait perspective, camera at eye height with horizontal optical axis, upright neutral head, coherent forehead/hairline/skull/crown/ear/jaw/chin projection. Do not tilt the head or make a dramatic shoulder pose. Neutral gray-white seamless studio, soft even low-contrast 5200–5600K illumination, neutral white balance and natural photographic skin texture. If clothing is visible, show only the authentic upper portion of the same pink high-cut one-piece Calibration Outfit, not a tank top or another garment.

Avoid three-quarter view, near-profile, face pointing image-right, mirroring, visible far iris, camera-seeking gaze, identity averaging, generic face, enlarged eye, overly small nose, narrowed nose, pointed or upturned nose, shortened bridge, pointed chin, changed jaw, high sharp cheekbone, face slimming, intense stare, smile, parted lips, age change, beauty filtering, whitening, heavy makeup, source styling leakage, updo, dramatic side light, wide-angle or top-down distortion, text, watermark, collage and multiple views.

One candidate image only. REVIEW_REQUIRED; do not label or imply Canon approval.
```

## Generation result

- generated_at: `2026-09-10T16:55:02+08:00`
- seed/settings: built-in `image_gen`; seed and detailed settings were not returned
- source output: `/home/verdvana/.codex/generated_images/01a089e9-1904-7443-9200-afbaa6608bae/exec-01bc8c62-5c77-4281-8d3f-a8ad6f5d45a2.png`
- original project output: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_05_RIGHT_PROFILE_NEUTRAL_v002/FACE_05_RIGHT_PROFILE_NEUTRAL_v002.png` (record only; raster removed after promotion)
- output dimensions: 1086×1448, exact 3:4
- output SHA-256: `7a92f8ffbf0d9a8b5baf28b8962e1ab76035800ca220c9cc4f82e9e5c904c9ea`
- QA record: `QA.md`

## Approval outcome

- user decision: approved as Canon on `2026-09-10`
- promoted asset: `OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001`
- current approved path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_05_RIGHT_PROFILE_NEUTRAL/OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_CANON_001.jpg`
- current approved JPG checksum: `de670f987d341e686f5239d6b5c7a920cd431050c2907c26de759a5cf37f6b97`
- approval record: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_05_RIGHT_PROFILE_NEUTRAL/approvals/APPROVAL_OWNER_FACE_05_RIGHT_PROFILE_NEUTRAL_001.md`
- reproduction method: `characters/CHR_HUMAN_001_OWNER/canon/face/FACE_05_RIGHT_PROFILE_NEUTRAL_METHOD.md`
- full release: `owner_v1.0` remains unlocked
