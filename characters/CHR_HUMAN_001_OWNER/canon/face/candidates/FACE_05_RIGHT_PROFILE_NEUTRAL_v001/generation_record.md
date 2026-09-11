# FACE_05_RIGHT_PROFILE_NEUTRAL_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.18
identity_md_revision: draft_0.17
asset_id: FACE_05_RIGHT_PROFILE_NEUTRAL
candidate_id: FACE_05_RIGHT_PROFILE_NEUTRAL_v001
gate: "Gate 2 — Face Identity Canon"
model_tool: "built-in image_gen"
status: GENERATED_REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_L0_FACE_PROFILE_IMAGE_LEFT
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
reference_count: 3
previous_ai_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_05_RIGHT_PROFILE_NEUTRAL_v001/FACE_05_RIGHT_PROFILE_NEUTRAL_v001.png"
qa_status: AI_TECHNICAL_PRECHECK_PASS_USER_REVIEW_REQUIRED
```

## Reference plan and fixed order

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.png`
   - SHA-256: `efda86babb6caeac5991515979e77ddf61e5a2776cd8e0819c9215b125d9f374`
   - responsibility: highest authority for the exact recognizable woman, skull and feature relationships, adult age, neutral-studio skin tone and neutral expression
   - must_not_define: profile depth alone, Hairstyle B, body, final outfit or episode setting

2. `L0_OWNER_009`
   - path: `characters/CHR_HUMAN_001_OWNER/source/identity/raw/11.jpg`
   - dimensions: 1522×1773
   - SHA-256: `948a092a360192af3f8718b27e35562ca5e14a21022e1161f8449be75b830a46`
   - responsibility: real right-profile geometry with the face/nose pointing image-left; forehead–nose–philtrum–lip–chin silhouette, orbital depth, ear placement and jaw/neck transition
   - must_not_define: identity priority, sideways eye pose, updo, makeup, retouching, pink backdrop, black clothing, skin texture, skin tone or lighting

3. `OWNER_HAIRSTYLE_A_FACE_MASKED_001`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`
   - dimensions: 769×1080
   - SHA-256: `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`
   - responsibility: Hairstyle A design only — near-center part, close roots, low crown volume, long straight loose silhouette, face-framing panels and tapered ends
   - must_not_define: face, skin, skull, body, clothing, outdoor lighting/background; the gray oval is deleted information

Reference budget is three images. No FACE_02, FACE_03, prior profile candidate, mirror, previous shot or failed image is supplied.

## Final assembled prompt

```text
Use case: identity-preserve

Asset type: FACE_05_RIGHT_PROFILE_NEUTRAL, L1 Face Canon candidate v001 for CHR_HUMAN_001_OWNER, governed by OWNER_L1_GENERATION_SPEC draft_1.18 and OWNER_IDENTITY_ANCHOR draft_0.17.

Input images: Image 1 is the approved front-neutral Face Canon and has highest authority for the exact recognizable woman, skull and facial-feature relationships, adult age, neutral-studio skin tone, fine facial geometry and neutral expression. Image 2 is the strongest real same-person profile photograph; it is authoritative only for her genuine right-profile geometry with the face and nose pointing image-left: forehead-to-nose bridge and tip silhouette, orbital depth, philtrum, lips, rounded chin, jaw-to-ear relationship, visible ear placement and jaw/neck transition. Image 3 is a source-derived masked Hairstyle A reference and is authoritative only for hair. Resolve every identity conflict in favor of Image 1.

Primary request: Create exactly one new photorealistic neutral full right-profile portrait. Rotate the head about 85–90 degrees so the anatomical right facial plane is visible and the face/nose points image-left. Show a clean true profile rather than a three-quarter view: one eye is principally visible, the far eye/iris must not appear beside the nasal bridge, and the forehead–nose–lips–chin silhouette must read clearly. The visible eye looks naturally straight ahead toward image-left, not toward the camera. Mouth naturally closed; expression neutral, gentle and relaxed. Reconstruct from the three scoped inputs in parallel; do not mirror another Canon and do not copy or continue any AI candidate.

Identity: Preserve the same recognizable woman as Image 1: skull proportions, natural medium almond eye, brow, nose identity, softly shaped lips, naturally full cheek volume, restrained cheekbone, rounded jaw transition, softly rounded non-pointed chin, adult age, skin tone and natural asymmetry. Use Image 2 only for view-dependent real profile geometry. Do not inherit Image 2's sideways/glancing eye pose, widened eye, styled updo, formal makeup, retouching, warm/pink color cast, directional studio light, black off-shoulder clothing or pink background. Image 3 must not influence face, skin, skull, body, clothing, light or background. Keep the chin softly rounded while preserving its natural vertical length and forward projection; no sharp tip, no shortened or widened chin, and no altered jaw.

Hairstyle: HAIRSTYLE_A only — near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels and tapered ends. Arrange the visible-side hair naturally behind the ear enough to keep the real ear, jawline and profile silhouette readable, while the remaining hair hangs loose behind the shoulder. No bun, updo, ponytail, Hairstyle B or A/B hybrid.

Composition and camera: exact 3:4 portrait, head top to upper chest, head approximately 65–72% of frame height, 85–105mm-equivalent portrait perspective, camera at eye height with horizontal optical axis, upright neutral head, coherent forehead/hairline/skull/crown/ear/jaw/chin projection. Do not tilt the head up or down and do not turn the shoulders into a dramatic pose.

Scene and light: neutral gray-white seamless studio; soft even low-contrast 5200–5600K illumination; neutral white balance; natural photographic skin texture. If clothing is visible, show only the authentic upper portion of the same pink high-cut one-piece Calibration Outfit, not a tank top or another garment.

Avoid: three-quarter view, near-profile, face pointing image-right, mirroring, visible far iris, cross-eyed or camera-seeking gaze, identity averaging, generic face, enlarged eye, narrowed or redesigned nose, pointed chin, shortened/widened chin, high sharp cheekbone, face slimming, intense stare, smile, parted lips, age change, beauty filtering, whitening, heavy makeup, source styling leakage, updo, dramatic side light, wide-angle or top-down distortion, text, watermark, collage and multiple views.

Output: one candidate image only. REVIEW_REQUIRED; do not label or imply Canon approval.
```

## Planned QA

1. exact identity against approved FACE_01;
2. anatomical right profile visible and face pointing image-left;
3. true 85–90° profile, clean silhouette and no far iris;
4. nose/lips/chin/ear/jaw geometry against `11.jpg` without its styling leakage;
5. rounded chin, restrained cheekbone, gentle neutral expression and adult age;
6. eye-level lens-neutral camera, exact 3:4 and consistent head scale;
7. Hairstyle A with visible ear/profile edge and Calibration Outfit upper portion;
8. no artifact, text, watermark or collage.

## Generation result

- generated_at: `2026-09-10T16:30:23+08:00`
- seed/settings: built-in `image_gen`; seed and detailed settings were not returned
- source output: `/home/verdvana/.codex/generated_images/01a089e9-1904-7443-9200-afbaa6608bae/exec-2ee5f5a0-8943-486a-9bbd-031f093e6df6.png`
- project output: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_05_RIGHT_PROFILE_NEUTRAL_v001/FACE_05_RIGHT_PROFILE_NEUTRAL_v001.png`
- output dimensions: 1086×1448, exact 3:4
- output SHA-256: `18deb156703357175e46ce7d29acf6e7fb163b4955643eb0281785feb970d290`
- QA record: `QA.md`
