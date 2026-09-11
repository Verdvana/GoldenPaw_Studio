# FACE_02_LEFT_3Q_NEUTRAL_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.11
identity_md_revision: draft_0.11
asset_id: FACE_02_LEFT_3Q_NEUTRAL
candidate_id: FACE_02_LEFT_3Q_NEUTRAL_v001
gate: "Gate 2 — Face Identity Canon"
model_tool: "built-in image_gen"
status: GENERATED_REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_count: 3
seed_settings: "built-in image_gen; seed and detailed settings not returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_02_LEFT_3Q_NEUTRAL_v001/FACE_02_LEFT_3Q_NEUTRAL_v001.png"
qa_status: USER_REVISION_REQUESTED
```

## 1. Task and candidate intent

Create exactly one photorealistic L1 Face Canon candidate showing the owner in a neutral left three-quarter view. The nose points image-left and the anatomical left facial plane is the principal visible side. Record both the anatomical side and image direction in final metadata.

## 2. Reference plan

| Priority | Reference ID | Path | Responsibility | Must not define |
|---:|---|---|---|---|
| 1 | `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` | `canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.png` | approved owner identity, facial-feature relationships, adult age appearance, neutral-studio skin tone, neutral expression | new three-quarter geometry by itself, body, final outfit, Hairstyle B, episode lighting/background |
| 2 | `L0_OWNER_013` | `source/identity/raw/15.jpg` | real left-three-quarter orbital depth, nose projection, cheek-to-jaw depth, ear placement and image-left direction | smile, gaze direction, formal makeup, retouching, skin tone, directional lighting, ornaments, hairstyle, clothing, background |
| 3 | `OWNER_HAIRSTYLE_A_FACE_MASKED_001` | `canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png` | Hairstyle A near-center part, close-to-scalp roots, low crown volume, long straight loose silhouette, face-framing panels and tapered ends | face, skin, skull geometry, body, clothing, outdoor color/light, background |

Reference budget: three images. No prior Face candidate and no failed/unreviewed generated image is used. The approved Face master is combined in parallel with scoped L0 view geometry and a source-derived hair-only input; it is not an AI-candidate lineage.

## 3. Identity locks

- Preserve exactly the recognizable woman defined by `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` and `IDENTITY.md` draft_0.11.
- Preserve skull width/length relationship, eye spacing, brow character, nose, lips, cheeks, rounded jaw transition, rounded chin, adult age and natural asymmetry.
- Use `L0_OWNER_013` only to solve the real three-quarter projection of the same person; do not average its makeup, smile or photographic treatment into the result.
- Direction contract: head turned approximately 35–40 degrees toward image-left; anatomical left facial plane principally visible; eyes look toward camera.

## 4. Body and appearance locks

- Head-to-upper-chest crop only; body geometry is non-authoritative.
- Hairstyle must be `HAIRSTYLE_A`, never Hairstyle B and never a blended third style.
- Natural skin texture; no whitening, heavy retouching or beauty filtering.

## 5. Outfit and material contract

If clothing is visible, show only the authentic upper portion of the pink high-cut one-piece Calibration Outfit. It must not be reinterpreted as a tank top, dress, sweater or other garment. Hosiery is outside frame and remains logically part of the outfit but is not defined by this candidate.

## 6. Props and environment

No props. Neutral gray-white seamless studio only; the background is non-authoritative.

## 7. Camera and lighting

- 3:4 portrait; preferred 1536×2048 or the closest native 3:4 output.
- 85–105mm-equivalent portrait perspective.
- Camera at eye height with a horizontal optical axis; neutral upright head and visually level skull projection.
- Head top to upper chest; head occupies approximately 65–72% of frame height.
- Soft, even 5200–5600K neutral studio light with low contrast and readable facial structure.

## 8. Negative constraints

No identity drift, generic East Asian face, face slimming, enlarged eyes, narrowed nose, pointed chin, age change, heavy makeup, smile, parted lips, distorted ear, asymmetric eye error, top-down view, upturned head, excessive visible crown plane, wide-angle distortion, Hairstyle B, bun, updo, hybrid hairstyle, outfit substitution, dramatic lighting, color cast, text, watermark, collage or multiple views.

## 9. Output contract

One image and one angle only. Candidate remains `REVIEW_REQUIRED`; no automatic Canon promotion. Complete identity, direction, expression, hair, camera, outfit and artifact QA before user review.

## Final assembled prompt

Use case: identity-preserve

Asset type: `FACE_02_LEFT_3Q_NEUTRAL`, L1 Face Canon candidate for `CHR_HUMAN_001_OWNER`, governed by `OWNER_L1_GENERATION_SPEC` draft_1.11 and `OWNER_IDENTITY_ANCHOR` draft_0.11.

Input images: Image 1 is the approved front-neutral Face Canon and is authoritative for the exact recognizable woman, facial-feature relationships, adult age appearance, neutral-studio skin tone and neutral expression. Image 2 is the real L0 left-three-quarter source and is authoritative only for the same person's orbital depth, nose projection, cheek-to-jaw depth, ear placement and face-points-image-left geometry. Image 3 is a source-derived masked Hairstyle A reference and is authoritative only for hair design. Resolve identity conflicts in favor of Image 1.

Primary request: Create exactly one new photorealistic left-three-quarter neutral portrait. Turn the head approximately 35–40 degrees toward image-left so the anatomical left facial plane is principally visible. Keep the eyes looking toward the camera, the mouth naturally closed and the expression neutral. Reconstruct the new angle from the three scoped master references in parallel; do not copy or continue any previous AI candidate.

Identity: Preserve exactly the same recognizable woman as Image 1, including skull proportions, eye spacing, brows, natural eye size, nose, soft lips, naturally full cheeks, rounded jaw transition, rounded chin, adult age and natural asymmetry. Image 2 may solve only real view-dependent depth. Do not inherit its smile, gaze, formal makeup, retouching, skin tone, lighting, ornaments, hairstyle, clothing or background. Image 3 must not influence face, skin, skull, body, clothing, light or background.

Hairstyle: `HAIRSTYLE_A` only — near-center part, close-to-scalp roots, low controlled crown volume, long straight loose dark-brown hair, natural face-framing panels, subtle strand irregularity and tapered ends. No bun, no updo, no Hairstyle B and no A/B hybrid.

Composition and camera: Exact 3:4 portrait; head top to upper chest; head approximately 65–72% of frame height; 85–105mm-equivalent portrait perspective; camera at eye height; horizontal optical axis; upright neutral head; visually level forehead, hairline, skull, crown, ears and jaw. No top-down or upturned-head projection and no excessive visible crown plane.

Scene and light: Neutral gray-white seamless studio; soft even low-contrast 5200–5600K light; neutral white balance; natural photographic skin texture. If clothing is visible, show only the authentic upper portion of the same pink high-cut one-piece Calibration Outfit, not a tank top or other pink garment.

Avoid: identity averaging, generic face, slimming, enlarged eyes, narrowed nose, pointed chin, age change, beauty filter, whitening, heavy makeup, smile, parted lips, distorted ears, asymmetric eye errors, wide-angle distortion, dramatic styling, color cast, text, watermark, collage and multiple views.

Output: One candidate image only. `REVIEW_REQUIRED`; do not label or imply Canon approval.

## Generation settings/result

- generated_at: `2026-09-10T14:12:17+08:00`
- seed/settings: built-in `image_gen`; seed and detailed settings were not returned
- source output: `/home/verdvana/.codex/generated_images/01a089e9-1904-7443-9200-afbaa6608bae/exec-aa3b9bee-9f9c-4aef-aed8-1a25d76ba877.png`
- output_path: `characters/CHR_HUMAN_001_OWNER/canon/face/candidates/FACE_02_LEFT_3Q_NEUTRAL_v001/FACE_02_LEFT_3Q_NEUTRAL_v001.png`
- output_dimensions: `1086x1448`
- output_checksum: `57548285c19d91ffec89a66f0f6019c7ece64d5dfd23f0d8ac9893712b4dd768`
- QA_record: `QA.md`

## User review outcome

- overall direction: accepted as good
- requested refinement: cheekbone appears slightly too high
- requested refinement: chin appears slightly too pointed
- requested refinement: gaze is not soft enough
- disposition: retain as `REVIEW_REQUIRED`; create v002 from the same scoped Master references, not from this candidate
