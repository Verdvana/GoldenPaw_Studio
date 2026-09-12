# BODY_01_FRONT_v009 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.38
identity_md_revision: draft_0.36
body_md_revision: draft_0.13
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v009
gate: "Gate 3 — Body Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
actual_resolution: "1086x1448"
reference_set_ids:
  - OWNER_BODY_FRONT_RECOVERY_V1
reference_count: 4
previous_ai_body_candidate_count: 0
seed_settings: "built-in image_gen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v009/BODY_01_FRONT_v009.png"
pixel_storage_status: "MOVED_TO_CANON_THEN_USER_TRANSCODED_TO_JPG; PNG_REMOVED"
current_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg"
current_promoted_checksum_sha256: "964c3b9d72c6688881b8ebfa4c6fc1bcfea04c998351352fabfdc8f4951666f6"
qa_status: PASS_USER_APPROVED
checksum_sha256: "cbb08e1799a6d6d3d9e00b600ceaab294a36a2b04a170ae1a367e28578cd0164"
```

## User-scoped revision

- user-confirmed real physical baseline: 168 cm, 120 jin (approximately 60 kg);
- correct the current approximately 160 cm visual impression to a natural 168 cm stature through coherent head-to-body, torso and limb proportions, never via wide-angle, low-angle, small-head styling or image stretching;
- straighten both lower legs further: knee, shin and ankle centers should form near-vertical symmetric axes, with natural calf volume and no outward-bowed/O-leg silhouette;
- preserve the user-approved face identity, Hairstyle A and 15D velvet-finish hosiery appearance in intent;
- use no BODY_01 v001–v008 pixels and do not use the approved Body Master as an input.

## Reference plan

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — exact recognizable front face, adult age, neutral expression and neutral skin appearance only; must not define body, outfit, hosiery, lighting or background.
2. `L0_OWNER_002` (`3.jpg`) — real front standing context for natural head/body scale, shoulder/torso relation, waist/hip placement and limb articulation only; must not override the explicit 168 cm / 60 kg user measurement or define face, hair, clothing, shoes, props, asymmetry, background or retouching.
3. `L0_OWNER_003` (`4.jpg`) — natural torso, waist, hip, thigh and calf volume cross-check only; must not override the explicit 168 cm / 60 kg measurement or define walking pose, bags, dress, legwear, shoes, face, hair, environment or final body alone.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — Hairstyle A only; the mask carries no visual authority and the source must not define face, body, skin, clothing, lighting or background.

No previous Body candidate, approved Body Master, previous shot or hosiery photograph is supplied.

## Prompt assembly

```text
Use case: identity-preserve
Asset type: BODY_01_FRONT L1 technical character-proportion calibration candidate for CHR_HUMAN_001_OWNER

Create exactly one neutral full-length front-view technical reference of the adult woman whose front face identity is defined only by Image 1. Images 2–3 are real-person body-context references only, and Image 4 defines Hairstyle A only. Use no previous generated Body image and do not reconstruct the current Body Canon.

The user's explicit physical measurement is authoritative: height 168 cm, weight 60 kg (120 jin). Give her the coherent natural proportions and visual stature of a 168 cm adult woman at 60 kg—noticeably taller in proportion than an approximately 160 cm impression, while retaining realistic shoulder, chest, waist, hip, thigh and calf soft-tissue volume. Express stature through a coherent head-to-body ratio, torso length, hip/waist placement and limb lengths. Do not shrink the head, create a fashion-model body, use wide-angle or low-angle elongation, or mechanically stretch the image.

Make both legs anatomically straight in the front view. Each knee center, shin/tibial axis and ankle center should align on a natural near-vertical axis. Keep left and right axes symmetric and parallel, feet flat and approximately parallel. Preserve natural calf muscles but prevent the shin bones and outer calf silhouettes from bowing outward or creating an O-leg impression. No knock-knees, crossed legs or displaced ankles.

Preserve the approved recognizable face, neutral expression, Hairstyle A construction, natural waist direction and the existing successful hosiery appearance in intent. Standard calibration clothing: opaque plain pink high-cut one-piece athletic swimsuit; continuous light-nude closed-foot 15D velvet-finish sheer pantyhose; no shoes. Keep the subtle broad velvet sheen and soft translucent textile veil continuously over thighs, knees, calves, ankles, heels, insteps and toes. Burgundy toenail polish may remain softly muted beneath the fabric. No toe seam, color band, reinforced toe, bare toes, latex, PVC, plastic, wet coating or body-paint appearance.

Exact 3:4 portrait, complete head, hands, heels and toes with 5–8% breathing room, neutral gray-white seamless studio, soft even 5200–5600K light, level 70–85mm-equivalent lens-neutral camera centered between waist and lower chest. Square torso, even weight, relaxed arms, uncrossed legs. No other identity, hairstyle, outfit, material or anatomy changes; no props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.
```

## Attempt result

- generated_at: `2026-09-11`
- built-in output: `/home/verdvana/.codex/generated_images/01a090ea-9fa1-7d23-b3fe-9d1bbee989dd/exec-3367f536-47d2-4b31-8c53-a2709b7fa043.png` (tool cache; project-authoritative candidate saved at `output_path`)
- original candidate path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v009/BODY_01_FRONT_v009.png` (record only after promotion)
- result: one 1086×1448 exact-3:4 PNG generated, then moved to the approved Canon path after explicit user approval
- QA: `PASS_USER_APPROVED`. The user explicitly accepted face, Hairstyle A, limb proportions, waist/hip ratio, leg and foot geometry, and hosiery appearance.
- lineage: approved source-derived parallel reconstruction; downstream work uses the promoted Master, while L1 recreation uses the recovery method and never this candidate's pixels

## User approval

On 2026-09-11 the user stated: “非常好长相发型，四肢比例，腰臀比，等等，以及腿部脚部丝袜质感都合格，可以作为正式资产”. The candidate was promoted to `OWNER_BODY_01_FRONT_CANON_002`. The earlier `OWNER_BODY_01_FRONT_CANON_001` remains as a superseded historical component; the full `owner_v1.0` release remains unlocked.

The user then clarified the downstream approval scope: 168 cm / 60 kg, visible face appearance, `HAIRSTYLE_A`, limb proportions and waist/hip ratio may be referenced for other character assets and shot/video-frame image generation. Hosiery appearance is reusable only for the exact `15D matte nude` combination and must not define any other color, material/finish or denier.
