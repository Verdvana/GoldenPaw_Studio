# POSE_03_SEATED_UPRIGHT_v003 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.111
identity_md_revision: draft_0.99
asset_id: POSE_03_SEATED_UPRIGHT
candidate_id: POSE_03_SEATED_UPRIGHT_v003
gate: "Gate 6 — Body / Pose Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_BODY_FRONT_CANON_L1
  - OWNER_HAIR_A_FRONT_CANON_L1
reference_count: 3
previous_ai_pose_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_03_SEATED_UPRIGHT_v003/POSE_03_SEATED_UPRIGHT_v003.png"
pixel_storage_status: "MOVED_TO_CANON"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/poses/approved/POSE_03_SEATED_UPRIGHT/OWNER_POSE_03_SEATED_UPRIGHT_CANON_001.png"
current_promoted_checksum_sha256: "7e6bbc031712a2831d3d4e473c69bd998c60438c870e46bea0812a00ab8dffb8"
checksum_sha256: "7e6bbc031712a2831d3d4e473c69bd998c60438c870e46bea0812a00ab8dffb8"
qa_status: PASS_TECHNICAL_REVIEW_REQUIRED
```

## Authorization and lineage

The user accepted the v002 face/skin, pose and other attributes but requested one correction: restore burgundy toenail polish beneath the continuous 15D nude pantyhose. v002 is not supplied. v003 is independently generated from the same three approved scoped L1 Masters; no generated Pose, Expression, historical Body candidate or Shot image is used.

## Reference responsibilities

1. `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg`
   - responsibility: exact approved front facial identity, feature relationships, neutral skin tone and clean natural skin presentation.
   - must_not_define: body, pose, hairstyle, outfit, hosiery, feet, stool, lighting or background.
2. `OWNER_BODY_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v009/BODY_01_FRONT_v009.jpg`
   - responsibility: approved 168 cm / 60 kg body proportions, limb/foot scale, Calibration Outfit, continuous 15D matte nude hosiery and visible burgundy toenail-polish context.
   - must_not_define: permanent face refinement, seated articulation, other Pose components, lighting or background.
3. `OWNER_HAIR_A_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/A/approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png`
   - responsibility: approved front Hairstyle-A part, volume, straight panels, length and tapered ends.
   - must_not_define: face, skin, body, pose, outfit, hosiery, feet, stool, lighting or background.

Reference budget: 3 approved Masters. v001/v002 and all generated Pose images are excluded.

## Authoritative candidate scope

- front-facing upright seated articulation and joint relationships;
- stable identity/body/hair under the approved Masters;
- visible compliance with the stable burgundy toenail trait beneath continuous 15D nude hosiery, without acquiring Material Canon authority.

## Must not define

- permanent face/body geometry, Hairstyle A, Expression Canon, skin tone or age;
- Calibration Outfit design, reusable hosiery Material Canon, nail-color Canon or episode wardrobe;
- reusable stool/environment design, other Pose components or complete release.

## Prompt assembly

```text
Use case: photorealistic-natural
Asset type: adult technical upright-seated joint calibration reference

Create exactly one new POSE_03_SEATED_UPRIGHT v003 candidate for adult character CHR_HUMAN_001_OWNER, following OWNER_L1_GENERATION_SPEC draft_1.111 and IDENTITY draft_0.99. Do not use or imitate v001 or v002.

Image 1 is the sole authority for the exact approved front face, clean neutral skin and facial geometry. Image 2 defines only the approved 168 cm / 60 kg body proportions, limb and foot scale, Calibration Outfit, continuous 15D matte nude pantyhose and the stable burgundy toenail-polish context. Image 3 defines only Hairstyle A. Do not mix their duties.

Show a straight-on full-body upright seated pose on a simple featureless neutral-gray backless studio stool. Pelvis centered and neutral, torso naturally vertical, head level, calm forward gaze and naturally closed mouth. Shoulders lowered. Both empty hands rest lightly and symmetrically on the upper thighs with relaxed distinct fingers. Thighs point forward at natural hip width, knees separated and bent near 90 degrees, lower legs descend near vertically, and both uncrossed feet rest flat on one floor plane. Preserve realistic seated soft-tissue compression without changing body mass or limb lengths.

Preserve the approved face exactly and keep the skin neutral, clean, naturally textured and spatially even: no sensitive red blotches, dirty gray/brown patches, asymmetric color islands, bruised-looking marks, acne-like artifacts, smeared makeup, over-sharpening or plastic smoothing.

Toenail correction: all ten toenails have restrained deep burgundy polish. The burgundy color is visible naturally through the closed-toe 15D nude pantyhose as softly muted, slightly desaturated nail color beneath the textile fibers. The pantyhose must remain visibly present above every toenail. Do not paint polish on top of the fabric, do not make it bright red, purple-black, glossy decals or unnaturally saturated, and do not add a toe band, seam, reinforced toe or fabric break. Fingernails remain natural and unpainted.

Technical studio photograph, exact 3:4 portrait, entire hair, hands, seat contact, lower legs and feet visible, level 70–85 mm-equivalent perspective, neutral light-gray seamless background and broad even 5200–5600 K light. Keep the plain opaque pink one-piece athletic fit garment, continuous light-nude closed-foot 15D matte/velvet sheer pantyhose and no shoes.

Stool is support only. Correct ordinary adult anatomy; no crossed legs, splayed glamour pose, slouch, lean, arch, dangling feet, fused limbs, broken joints, duplicated heels, extra/missing digits, props, text, watermark, collage or border. This candidate defines only upright-seated articulation and must not redefine identity, body, hair, garment, material, nail-color Canon, stool or environment. Status REVIEW_REQUIRED, not approved Canon.
```

## QA status

### Attempt 1

- generated_at: `2026-09-13`
- built-in output: `/home/verdvana/.codex/generated_images/01a09ab1-cec4-7f30-9bd8-80cb6ab0e147/exec-f2e513c9-4b6d-4b14-a9fd-56fcc360e1b5.png`
- project candidate: `characters/CHR_HUMAN_001_OWNER/canon/poses/candidates/POSE_03_SEATED_UPRIGHT_v003/POSE_03_SEATED_UPRIGHT_v003.png`
- result: one 1086×1448 exact-3:4 PNG generated and saved in the candidate directory.
- lineage: approved FACE_01 + BODY_01 + HAIR_A_01 L1 Masters; no v001/v002, other generated Pose, Expression, historical Body candidate or Shot input.
- technical QA: pass for review; see `QA.md`.

Final current status: `REVIEW_REQUIRED`. The raster is not approved or promoted and cannot be used as Pose Canon until explicit user approval.

## User approval and promotion

On 2026-09-13 the user stated “批准。记录吧。” The exact candidate raster and sidecar metadata were moved, not copied, to `characters/CHR_HUMAN_001_OWNER/canon/poses/approved/POSE_03_SEATED_UPRIGHT/OWNER_POSE_03_SEATED_UPRIGHT_CANON_001.png`. The pixel checksum remains unchanged. Approval is scoped to upright seated articulation and the compliant visible burgundy-toenail-under-15D presentation in this image; the complete `owner_v1.0` remains unlocked.
