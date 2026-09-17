# BODY_01_FRONT_v017 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v017
target_canon_version: owner_v1.0
gate: Gate 3 — Body Canon
status: REVIEW_REQUIRED
approval_status: PENDING_USER_REVIEW
spec_revision: draft_1.225
identity_revision: draft_0.177
body_method_id: OWNER_BODY_01_FRONT_METHOD_V2
body_revision: draft_0.17
generation_tool: built_in_image_gen
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_BODY_FRONT_RECOVERY_V1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 5
previous_generated_body_inputs: 0
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v017/BODY_01_FRONT_v017.png
sha256: 562e0a3a0b56886f523a39d329cac0bb15240c9c85ee0e5782f3acf18b841f8b
dimensions: 1087x1447
qa_status: PRELIMINARY_PASS_PENDING_USER_REVIEW
moderation_retry: first prompt blocked at output; neutral technical retry produced the candidate
```

## Generation inputs and responsibilities

1. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` — source-derived face/skin context only; excludes body, hair, clothing, hosiery, lighting and background.
2. `L0_OWNER_002` / `source/identity/raw/3.jpg` — real body context for stature, head-to-body scale, torso, waist/hip placement, limb length and natural stance; excludes face, hair, clothing, shoes, props and background.
3. `L0_OWNER_003` / `source/identity/raw/4.jpg` — body-volume cross-check for torso, waist, hip, thigh, calf and limbs; excludes face, hair, clothing, pose-specific styling and environment.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — Hairstyle A pixels only; masked area defines nothing.
5. `OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001` — hosiery material only: pale slightly-whiter 15D matte/velvet sheer veil, continuous toe coverage and interdigital tension; excludes identity, body geometry, skin tone, nail color, clothing and background.

`OWNER_BODY_01_FRONT_CANON_004` and the approved Face Canon are `qa_comparison_only`; neither is a generation input. Candidate v017 must be generated independently from the scoped inputs above.

## Prompt assembly

Create exactly one neutral, full-length, front-view technical character reference of an adult woman. Image 1 alone defines the recognizable front face and neutral skin appearance. Images 2–3 provide body context only. Image 4 defines Hairstyle A only. Image 5 defines hosiery textile behavior only. Do not use any previous generated Body image, approved Body Master, or previous shot as an image input.

Preserve the accepted v016 result in every respect except the requested lower-leg correction: coherent 168 cm / approximately 60 kg natural adult proportions; accepted waist/hip ratio, hip and upper-thigh-root contour, face, Hairstyle A, pink high-cut one-piece calibration swimsuit, pale slightly-whiter 15D sheer matte/velvet hosiery, toe haze, interdigital textile tension and burgundy toenail polish beneath the fabric. Correct only the front lower legs. Each tibial shaft must descend almost in line with its thigh axis from knee to ankle, with nearly no bend. The outer calf contour should continue close to the thigh outer contour without a lateral bulge. The inner calf contours should nearly meet, leaving only a very narrow natural air gap; never fuse, overlap or cross the legs. No O-leg, bow-legged silhouette, wide inter-leg gap, displaced knees/ankles, pinched ankles, slimming, lengthening or body redesign.

Use a square neutral standing posture with even weight, relaxed arms, uncrossed legs and flat parallel feet. Keep the complete head, hands, heels and toes inside a 3:4 frame. Use a level 70–85mm-equivalent camera centered between waist and lower chest, neutral gray-white seamless studio, and soft even light. Hosiery is one continuous pale sheer textile from swimsuit line through thighs, knees, calves, ankles, heels, insteps and toes; slight whitening over the skin, soft hazy coverage and local interdigital stretch are required. No seams, bands, reinforced toe, bare gaps, latex, PVC, plastic, wet coating, body paint, text, watermark or collage. One `REVIEW_REQUIRED` candidate only; not Canon.

## QA plan

Check separately: face contamination/identity drift against approved Face Canon; waist/hip and upper-thigh preservation against the approved Body Canon; knee–tibia–ankle collinearity; outer-contour continuity; near-closed but non-fused inner-leg gap; flat feet; continuous pale hosiery; interdigital tension; toe haze; burgundy polish; frame completeness. No promotion is authorized by this record.

## Generation output

- Generated source: `/home/verdvana/.codex/generated_images/01a0aeda-94e0-7940-aa23-e89d1ec0cff1/exec-d0b4a305-bfc8-4982-ba5c-0bb8222cd6cf.png`
- Repository candidate: `BODY_01_FRONT_v017.png`
- Visual precheck: lower-leg axes read nearly straight and close to the thigh axes; inner gap is narrow and remains anatomically separate; waist/hip, face, hosiery appearance and burgundy polish are retained for user review.
