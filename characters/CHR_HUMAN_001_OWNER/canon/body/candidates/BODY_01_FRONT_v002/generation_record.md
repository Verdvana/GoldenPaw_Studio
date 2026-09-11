# BODY_01_FRONT_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.29
identity_md_revision: draft_0.27
body_md_revision: draft_0.4
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v002
gate: "Gate 3 — Body Canon"
model_tool: "built-in image_gen"
status: GENERATED_QA_FAIL
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_FACE_FRONT_NEUTRAL_CANON_L1
  - OWNER_L0_BODY_FRONT_CONTEXT
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
reference_count: 4
previous_ai_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v002/BODY_01_FRONT_v002.png"
qa_status: FAIL
checksum_sha256: "7babf6bb0814d901e64e3913c07c5f3e232b34e4fcca9215bb3830598f0fdce5"
```

## User authorization

On 2026-09-11 the user explicitly rejected replacing the calibration swimsuit with shorts because shorts cannot fully reveal the proportions being calibrated. The unchanged outfit contract is therefore deliberate: pink high-cut one-piece swimsuit, continuous nude 15D velvet-finish sheer pantyhose, and no shoes.

## Reference plan

Inputs are supplied once, in this fixed order:

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — approved L1 downstream Master, SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`. Defines only exact front face identity, adult age, natural skin appearance, neutral expression, and the approved frontal identity/HAIRSTYLE_A relationship. It must not define body geometry from its crop, final outfit construction, hosiery material, lighting, or background.
2. `L0_OWNER_002` (`3.jpg`) — SHA-256 `556f6d4652e1f5ac18725cdb03ea2f7e90a761450a1fc4bdd50bf4cf42aff310`. Primary real frontal standing context for stature, head-to-body scale, shoulder/torso length, waist/hip placement, arm/leg length, and natural stance range. It must not define face, hair, qipao silhouette, shoes, umbrella, pose asymmetry, background, lighting, or retouching.
3. `L0_OWNER_003` (`4.jpg`) — SHA-256 `ca270e55c50fd168c798b0fbb20c9a8feded4c7f65e1c5af901b0c5e3601762b`. Cross-checks natural torso/waist/hip/thigh/calf volume and limb proportions across a different date and moving state. It must not define walking pose, bags, black dress, black legwear, shoes, face, hair, background, camera perspective, or a final body alone.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — SHA-256 `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`. Defines Hairstyle A only: near-center part, close roots, low crown volume, long straight loose dark-brown hair, face-framing panels, and tapered ends. It must not define face, body, skin, clothing, light, or background.

No previous Body candidate, failed attempt, previous shot, or hosiery advertising image is supplied. Hosiery behavior in this Body candidate is governed textually by `CALIBRATION_OUTFIT.md` and `docs/qa/hosiery_material_rules.md`; detailed hosiery authority remains Gate 7.

## Prompt assembly

```text
Use case: identity-preserve

Asset type: BODY_01_FRONT v002, one adult non-sexual technical character-proportion reference for CHR_HUMAN_001_OWNER. Governed by OWNER_L1_GENERATION_SPEC draft_1.29, OWNER_IDENTITY_ANCHOR draft_0.27, and OWNER_BODY_CANON_WORKING draft_0.4.

Input images in fixed order: Image 1 alone defines the approved exact recognizable front face, adult age, natural skin appearance, neutral closed-mouth expression, and frontal identity. Images 2 and 3 are real full-body context only; cross-check natural stature and proportions without copying their clothing, shoes, props, pose, background, face, or hair. Image 4 defines Hairstyle A only and cannot define face or body. No previous generated Body image is supplied.

Create exactly one photorealistic, full-length, front-neutral body calibration portrait of this adult woman. This is a practical identity and proportion reference, not glamour, boudoir, fetish, or suggestive imagery. She faces the camera squarely with head, shoulders, torso, pelvis, knees, and feet oriented forward. Use an ordinary relaxed anatomical stance: upright head and torso, eye-level gaze, closed mouth, neutral expression, weight even on both feet, arms relaxed with a small gap from the torso, open hands, legs uncrossed, and feet flat and approximately parallel.

Preserve Image 1's face exactly. Derive a conservative natural real-person body midpoint from Images 2 and 3: ordinary balanced proportions, natural torso and waist placement, natural limb lengths, and natural soft-tissue distribution. Do not slim, increase height, lengthen legs, exaggerate curves, enlarge chest or hips, tighten the waist, or create a fashion-model or athletic body. Ignore the qipao, black dress, legwear, shoes, umbrella, bags, walking stride, and environments in Images 2 and 3.

Use Hairstyle A from Image 4 only: long straight loose dark-brown hair, near-center part, close roots, low crown volume, natural face-framing panels, and tapered ends.

Wear the exact standardized calibration uniform retained by explicit user decision: a plain solid pink high-cut one-piece athletic swimsuit with a moderate scoop neckline, secure shoulder straps, opaque practical fabric, and no decoration; continuous nude/skin-tone 15D velvet-finish sheer pantyhose from waist and hips through thighs, knees, calves, ankles, heels, insteps, and closed toes; no shoes. Present it neutrally as a technical apparel-fit and body-proportion reference. The pantyhose must read as one continuous fine textile garment with subtle matte/velvet finish, not bare legs, socks, thigh-highs, latex, PVC, wet coating, or body paint. Burgundy toenail polish may appear only subtly beneath the textile. Detailed hosiery material authority remains Gate 7.

Exact 3:4 vertical composition. Show the complete head, hair, hands, legs, heels, and every toe with 5–8% margin. Use a 70–85mm-equivalent lens, level camera centered between waist and lower chest, neutral gray-white seamless studio, soft even 5200–5600K lighting, neutral white balance, and a faint floor contact shadow.

Authority is limited to front-view body proportions and neutral stance. Do not redefine face, hair design, outfit design, hosiery Material Canon, skin policy, toenail color, makeup, or episode styling. Avoid crop, missing feet, shoes, crossed legs, hip pop, torso twist, walking, raised arms, anatomy errors, generic model proportions, sexualized pose, glamour styling, lingerie presentation, transparent swimsuit, cleavage emphasis, bare legs or feet, exposed toes, textile discontinuity, dramatic lighting, props, text, logo, watermark, collage, or multiple views.

One REVIEW_REQUIRED candidate only; never label or imply Canon approval.
```

## Attempt result

- generated_at: `2026-09-11`
- built-in output: `/home/verdvana/.codex/generated_images/01a08f0d-f395-77a3-b936-7cedfa238706/exec-856438b1-3289-4b68-bd91-7e5a67f1e4e9.png`
- project copy: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v002/BODY_01_FRONT_v002.png`
- result: one image generated successfully at exact 3:4 ratio; no seed or detailed settings returned
- QA: failed the hard hosiery-continuity requirement because the feet and toes visually read as bare rather than textile-covered; face and Hairstyle A also require identity review before any body approval
- lineage: the output remains an unapproved L1 candidate and must not be used as an input for another L1 candidate
