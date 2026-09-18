# OWNER_WORK_SUMMER_01_WORN_UPPER_BODY_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_WORK_SUMMER_01_WORN_UPPER_BODY
outfit_id: OWNER_WORK_SUMMER_01
level: L2
candidate_version: v001
target_canon_version: owner_v1.0
spec_revision: draft_1.235
identity_revision: draft_0.185
status: REVIEW_REQUIRED
approval_status: PENDING_USER_REVIEW
gate: L2 officewear upper-body fit-validation
generation_tool: built_in_image_gen
reference_set_ids:
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
reference_budget: 3 images
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4; no forced resize"
generation_inputs:
  - {asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1, path: "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png", responsibility: "current Body01 neck-below body proportions, upright neck, shoulder/torso relation, waist placement and upper-body scale", must_not_define: "face, facial identity, hair, clothing, hosiery, lighting or background"}
  - {asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png", responsibility: "source-derived face geometry, facial relationships, natural skin and neutral expression", must_not_define: "body, hair, clothing, pose, lighting or background"}
  - {asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png", responsibility: "Hairstyle A only", must_not_define: "face, body, skin, clothing, lighting or background"}
qa_comparison_only:
  - {asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001, path: "characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg", purpose: "post-generation identity and face-contamination QA only"}
  - {asset_id: OWNER_BODY_01_FRONT_CANON_007, path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png", purpose: "post-generation body proportion comparison only"}
  - {asset_id: OWNER_WORK_SUMMER_01_DESIGN_REFERENCE_v006, path: "outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/candidates/v006_design_reference/OWNER_WORK_SUMMER_01_DESIGN_REFERENCE_v006.png", purpose: "post-generation outfit-shape comparison only; not a generation input"}
authoritative_for:
  - "L2 summer officewear worn upper-body presentation"
  - "black low-neck round-neck short-sleeve top fit over current Body01 upper-body proportions"
must_not_define:
  - "new Character Canon or permanent identity facts"
  - "AI-to-AI face or body lineage"
  - "lower-body, shoe or hosiery fit outside the crop"
output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_SUMMER_01/candidates/v001_worn_upper_body/OWNER_WORK_SUMMER_01_WORN_UPPER_BODY_v001.png
sha256: 84f1f4cbb4fb6aadf859264c65407763d21f3c2e225e1f019e4a72e3b59a2f01
dimensions: 1086x1448
qa_status: TECHNICAL_PRECHECK_PASS_PENDING_USER_REVIEW
```

## Prompt assembly

Use case: identity-preserve
Asset type: L2 summer officewear worn upper-body fit-validation candidate

Generate one fresh photorealistic frontal neutral-standing upper-body outfit-fit image of the same adult woman, framed from the top of the head to approximately mid-thigh so the face, neck, shoulders, torso, waistline and upper skirt are visible. Reference 1 defines current Body01 neck-below proportions only: upright natural neck, shoulder-to-waist relationship, torso length, waist placement and overall upper-body scale. Reference 2 defines the face and skin from source-derived recovery only. Reference 3 defines Hairstyle A only. Do not use any generated Face/Body or outfit image as a generation input.

Preserve Body01 proportions exactly. Do not slim, widen, lengthen, shorten or redesign the neck, shoulders, chest, ribcage, waist or hips. Keep the head upright, face neutral, camera eye-level, arms relaxed at the sides, no twist and no exaggerated bust or waist.

Dress the subject in the current summer officewear upper portion: a black fitted short-sleeve top with a distinctly low rounded neckline, lower than a standard crew neck but still rounded and not V-shaped. The top is close-fitting but natural, with short sleeves and clean seams. Show the upper portion of the short skirt at the waist: white shifted slightly warm toward champagne with moderately sized, moderately spaced small black polka dots, tailored slim straight-to-soft-tapered fit, not umbrella-shaped, not strongly A-line and not bodycon. Do not show shoes. Hosiery may be only minimally visible below the crop; do not invent lower-body details outside frame.

Neutral gray-white seamless studio, soft even 5200–5600K light, 70–85mm-equivalent eye-level camera, exact native 3:4 portrait, full head and upper torso in frame, no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.

## QA plan

Check source-derived face compliance and no AI contamination; Hairstyle A only; exact Body01 upper-body proportions; lowered rounded neckline; short-sleeve top fit; visible champagne-white polka-dot skirt waistband/upper panel; no shoes, no hairstyle drift, no extra anatomy. No promotion without explicit user approval.
