# BODY_03_RIGHT_3Q_v004 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.46
identity_md_revision: draft_0.43
body_md_revision: draft_0.20
asset_id: BODY_03_RIGHT_3Q
candidate_id: BODY_03_RIGHT_3Q_v004
gate: "Gate 3 — Body Canon"
model_tool: "built-in image_gen"
status: REJECTED_TECHNICAL_QA
approval_status: REJECTED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_RIGHT_3Q_NEUTRAL_CANON_L1
  - OWNER_BODY_FRONT_CANON_L1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 3
previous_ai_body_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_03_RIGHT_3Q_v004/BODY_03_RIGHT_3Q_v004.png"
qa_status: FAIL_HEELS_RAISED_BY_MATERIAL_POSE_LEAKAGE
checksum_sha256: "ec6b55c47812268a93c52974c0bed9b26d168d9d55b73997c99f7eda2128046a"
```

## Revision brief

Reconstruct independently without any BODY_03 candidate pixels. Preserve v003's user-confirmed non-hosiery attributes only as written constraints: right-three-quarter identity/direction, 168 cm / 60 kg proportions, body geometry, Hairstyle A, outfit, neutral composition, separate normal feet, direct anatomical heel contact and absence of added heel forms or toe-base lines.

The only intended change is stronger, clearly visible but still sheer `15D nude matte/velvet` textile response across the complete legs and feet, guided by the newly ingested user-selected L0 material source.

## Reference plan

1. `OWNER_FACE_03_RIGHT_3Q_NEUTRAL_CANON_001` — face identity, adult appearance and image-right right-three-quarter direction only; excludes body, hair, outfit, hosiery and setting.
2. `OWNER_BODY_01_FRONT_CANON_002` — approved 168 cm / 60 kg proportions, limb/foot scale, waist/hip ratio, Hairstyle A and Calibration Outfit only; its 15D appearance is secondary to Image 3 for this revision. It excludes right-side depth, camera/background and other hosiery variants.
3. `L0_HOS_15_NM_011` (`materials/hosiery/source_library/raw/15d_nude_matte/1.jpg`) — authoritative only for 15D nude matte/velvet textile presence, opacity, smooth coverage over calves/ankles/insteps/toes and softened visibility of anatomy beneath fabric. It must not define owner identity, body or foot geometry, skin pigmentation, nail color, seated/dangling pose, clothing, shoes, background, lighting, watermark or floor contact.

## Prompt assembly

```text
Use case: identity-preserve
Asset type: BODY_03_RIGHT_3Q v004 adult technical character-turnaround candidate

Create one completely new photorealistic full-length right-three-quarter technical studio turnaround of the adult woman from three scoped references. Do not use any BODY_03 v001–v003 pixels, BODY_02 pixels or mirrored generated view.

Image 1 defines only the exact recognizable right-three-quarter face identity and image-right direction. Image 2 defines the approved 168 cm / 60 kg body proportions, limb and foot scale, waist/hip ratio, long straight Hairstyle A and pink one-piece Calibration Outfit. Image 3 defines only the hosiery material: reproduce its clearly visible light-nude 15D matte/velvet textile veil, softly diffused opacity, smooth continuous coverage and muted anatomy beneath fabric across calves, ankles, heels, insteps, forefeet and toes. Ignore Image 3's person, body/foot shape, skin color, nail color, seated/dangling pose, clothing, shoes, background, light, watermark and every non-material property.

Preserve the user-confirmed BODY_03 setup in intent: whole body neutrally rotated 35–40 degrees toward image-right; natural 168 cm / 60 kg proportions; no twist or fashion pose; feet separated 10–15 cm so their silhouettes do not merge. Each foot has one ordinary anatomical heel directly touching the same empty gray-white floor, with no pad, blob, wedge, platform, duplicate anatomy or other object beneath it.

Apply Image 3's material response as one continuous closed-foot pantyhose garment from waist through both legs to every toe. The fabric must be unmistakably visible over both complete feet, including heels, insteps and toes, while remaining sheer and matte/velvet rather than opaque. It softly reduces skin and nail contrast as in Image 3. Preserve the owner's burgundy toenail color only as subdued color beneath the fabric; do not copy Image 3's nail color. Do not create any transverse line, seam, crease, toe-cap edge, band, color break or opacity boundary where toes meet forefeet. No bare-foot appearance, latex, PVC, plastic, wet coating or body paint.

Keep the approved identity, body proportions, straight legs, normal grounded feet, Hairstyle A, plain pink high-cut one-piece and neutral closed-mouth expression. Exact 3:4 full-length frame, 5–8% breathing room, level 70–85mm-equivalent camera, neutral gray-white seamless studio, soft even neutral light. No shoes, props, text, watermark, collage or multiple views. Output one REVIEW_REQUIRED candidate only.
```

## Attempt result

- attempt_1_at: `2026-09-12`
- attempt_1_material_input: uncropped `L0_HOS_15_NM_011`
- attempt_1_result: `NO_OUTPUT_MODERATION_BLOCKED`
- attempt_1_request_id: `1ca9f7f0-73be-44ca-a2bc-91aaf11e0862`
- attempt_1_note: "No image was produced or saved. For the safety retry, the same user-selected L0 source is represented by deterministic material derivative OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001, which removes unrelated upper-body pixels without changing material pixels."
- attempt_2_at: `2026-09-12`
- attempt_2_built_in_output: `/home/verdvana/.codex/generated_images/01a09467-3db0-70a2-bf86-1fb58ecbbfb6/exec-58117291-80f3-4f25-8205-4fe04957a20c.png`
- generated_at: `2026-09-12`
- result: generated and saved, then rejected by technical QA
- QA: hosiery textile visibility improved substantially, but the source material's dangling/pointed foot pose leaked into the output; both heels are raised and the figure bears weight on the forefeet. v004 is rejected and excluded from v005 inputs.

## Safety retry reference substitution

Image 3 becomes `OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001`, derived from the requested `1.jpg` by the recorded crop `685x879+0+400`. Its authority and exclusions are identical to the source. The retry prompt is shortened to a neutral adult character-turnaround context while retaining the material target and foot-geometry constraints.

```text
Use case: identity-preserve
Asset type: BODY_03_RIGHT_3Q v004 adult character-turnaround calibration reference

Create one new full-length photorealistic right-three-quarter technical turnaround of the adult woman. Image 1 defines only her approved right-three-quarter face and image-right orientation. Image 2 defines her approved 168 cm / 60 kg proportions, limb/foot scale, waist/hip ratio, Hairstyle A and pink one-piece calibration garment. Image 3 is a deterministic crop from the user-selected `15d_nude_matte/1.jpg` and defines only the light-nude 15D matte/velvet pantyhose material—its clearly visible textile veil, softly diffused opacity and continuous lower-leg-to-foot coverage. Ignore Image 3's anatomy, pose, skin and nail color, shoes, background and lighting.

Neutral 35–40 degree right-three-quarter stance, feet separated and not overlapping. Both ordinary anatomical heels directly meet the same empty level floor; no object or extra geometry beneath either foot. Apply Image 3's material response continuously across both legs, ankles and complete feet. The fabric must be clearly visible over heels, insteps and toes while remaining sheer and matte. No line, seam, stripe, toe-cap edge, color break or opacity boundary across the front of either foot. Preserve subdued burgundy toenails beneath the textile.

Keep all other approved identity, proportions, hairstyle, outfit and neutral studio attributes. Exact 3:4 full figure, level camera, gray-white seamless studio, soft even neutral light. No footwear, props, text, watermark, collage or multiple views. One REVIEW_REQUIRED candidate only.
```
