# BODY_06_BACK_v004 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.229
identity_md_revision: draft_0.181
asset_id: BODY_06_BACK
candidate_id: BODY_06_BACK_v004
gate: Gate 3 — Body Canon
model_tool: built-in image_gen
status: REVIEW_REQUIRED
approval_status: PENDING_USER_REVIEW
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_L0_BODY_REAR_SIDE_CONTEXT
  - OWNER_HAIR_A_BACK_CANON_L1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 4
previous_ai_body_candidate_count: 0
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_06_BACK_v004/BODY_06_BACK_v004.png
checksum_sha256: c801df57ee3d0bad339ec9ddded48bdd8257909ac15f880e09ff76f657038f44
dimensions: 1086x1448
qa_status: PRELIMINARY_REVIEW_REQUIRED
```

## Generation inputs and responsibilities

1. `L0_OWNER_002` / `source/identity/raw/3.jpg` — stature, torso length and natural body-volume context only; excludes face, hair, clothing, shoes, lighting and background.
2. `L0_OWNER_015` / `source/identity/raw/17.jpg` — coarse real-person rear/side depth and silhouette plausibility only; excludes face, hair arrangement, skin, clothing, pose styling, setting and colors.
3. `OWNER_HAIR_A_04_BACK_CANON_001` — approved Hairstyle-A rear fall, length, volume and tapered ends only; excludes body, skin, clothing, hosiery, lighting and background.
4. `OWNER_HOS_15D_NM_011_LOWER_FEET_CROP_001` — pale slightly-whiter 15D hosiery color, continuous foot coverage and heel-gradient material response only; excludes identity, body geometry, foot anatomy, nail color, clothing and background.

`OWNER_BODY_01_FRONT_CANON_005` and `OWNER_BODY_06_BACK_CANON_002` are `qa_comparison_only`, not generation inputs. They may be compared after generation for proportion and continuity checks.

## Prompt assembly

Create exactly one neutral, non-erotic, exact 180-degree full-length back-view technical apparel-fit and body-proportion chart of the same adult woman. The image is fully clothed in the plain opaque pink high-cut one-piece calibration garment, continuous pale hosiery and no shoes. Head, shoulders, torso, pelvis, knees, heels and feet face directly away from camera; no head turn, torso twist or crossed legs.

Match the current approved front Body Canon's proportions in back view: coherent 168 cm / approximately 60 kg adult scale, slightly narrower waist with a smooth back-ribcage-to-waist-to-hip transition, fuller natural thighs and calves, straight symmetric leg axes, and the same overall limb proportions. Preserve a relaxed neutral standing pose and full-foot grounding. The back silhouette must not become a different body, a narrow fashion model, or an exaggerated hourglass.

The rear one-piece opening must be clearly high-cut and aligned in height with the approved front opening, with a coherent side seam and natural waist-to-hip-to-upper-thigh transition. Keep rear coverage symmetric and athletic. Do not use the prior back candidate as a pixel input.

Hosiery must match the current accepted front material: one continuous pale light-nude, slightly-whiter 15D matte/velvet sheer textile from the garment line through thighs, knees, calves, ankles, heels and feet. Keep a soft hazy veil and subtle fabric presence. At both rear heels, transition gradually toward slightly more translucent fabric so the rounded heel is softly readable through the hosiery, but never expose bare skin, a white ring, hard boundary, seam, band or reinforced toe. No latex, PVC, plastic, rubber, wet coating or body paint.

Neutral gray-white seamless studio, soft even neutral light, level 70–85mm camera, exact 3:4 portrait, complete head and feet in frame, no props, text, watermark or collage. Produce one `REVIEW_REQUIRED` candidate only; not Canon.

## QA plan

Compare against `OWNER_BODY_01_FRONT_CANON_005` and `OWNER_BODY_06_BACK_CANON_002` only after generation: body volume, waist/hip ratio, fuller thigh/calf continuity, straight legs, high-cut rear opening alignment, full-foot grounding, continuous pale hosiery, gradual heel transparency and absence of rings/bands/material breaks. Do not promote automatically.

## Generation output

- Generated source: `/home/verdvana/.codex/generated_images/01a0aeda-94e0-7940-aa23-e89d1ec0cff1/exec-628207ec-74a8-43c6-9660-0a641b4ccbcd.png`
- Repository candidate: `BODY_06_BACK_v004.png`
- Visual precheck: exact rear-view orientation, coherent waist-to-hip transition, fuller leg volume, continuous pale hosiery, gradual heel transparency and flat bilateral foot contact are present for user review.
