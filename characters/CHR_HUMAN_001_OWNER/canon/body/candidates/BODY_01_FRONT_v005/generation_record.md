# BODY_01_FRONT_v005 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.32
identity_md_revision: draft_0.30
body_md_revision: draft_0.7
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v005
gate: "Gate 3 — Body Canon"
model_tool: "built-in image_gen"
status: REJECTED_BY_USER
approval_status: REJECTED
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v005/BODY_01_FRONT_v005.png"
qa_status: FAIL
checksum_sha256: "20d38201a45ee6f7b5595b025eef85bceaf742ddfaf7071058aebc7bb2093c38"
```

## User-scoped revision

- keep the current leg-share target unchanged;
- make the lower legs straight rather than O-shaped, with knees directly above ankles and stable parallel spacing;
- show a clearly perceptible but delicate hazy 15D textile veil over the entire legs, feet and toes;
- add a very slight velvet textile sheen along legs without gloss, plastic or wet appearance;
- preserve burgundy toenail polish as naturally muted beneath fabric;
- no toe seam, reinforced toe or color division line;
- preserve face and Hairstyle A from approved/source inputs; do not use v004 pixels.

## Reference plan

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`; exact front face identity, adult age, neutral expression and natural skin appearance only; must not define body, outfit, hosiery, lighting or background.
2. `L0_OWNER_002` (`3.jpg`) — SHA-256 `556f6d4652e1f5ac18725cdb03ea2f7e90a761450a1fc4bdd50bf4cf42aff310`; real standing proportion context only; must not define face, hair, clothing, footwear, props, pose asymmetry, background or retouching.
3. `L0_OWNER_003` (`4.jpg`) — SHA-256 `ca270e55c50fd168c798b0fbb20c9a8feded4c7f65e1c5af901b0c5e3601762b`; natural torso and limb-volume cross-check only; must not define walking pose, dress, legwear, shoes, face, hair, background or final body alone.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — SHA-256 `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`; Hairstyle A only; must not define face, body, skin, clothing, lighting or background.

No previous Body candidate, previous shot or hosiery photograph is supplied. The accepted leg-share direction is carried forward as user-authored text only.

## Prompt assembly

```text
Create one neutral full-length technical studio reference of the adult woman in Image 1. Images 2 and 3 provide natural body-proportion context only; Image 4 provides the long straight Hairstyle A only. Use no previous generated image.

Keep the approved face, neutral expression, Hairstyle A and the current elongated-but-natural leg proportion unchanged. Stand square to camera with arms relaxed and even weight. Make both lower legs straight and parallel: knees directly above ankles, feet directly below knees, and similar spacing at knees, calves and ankles. No outward calf bow or O-shaped silhouette.

Use the standardized calibration clothing: plain opaque pink high-cut one-piece athletic swimsuit, nude 15D velvet-finish sheer pantyhose and no footwear. Make the hosiery unmistakably visible as a delicate continuous textile veil over the full legs, ankles, feet and closed toes. It gently softens skin detail and toe contours and has a very slight, broad velvet sheen along thighs, shins and insteps under soft studio light. Burgundy toenail polish remains naturally muted but visible beneath the same sheer fabric. Uniform color and transparency; no toe seam, color division, reinforced toe, bare-looking foot, plastic gloss or wet coating.

Exact 3:4 full-body portrait with complete head, hair, hands and feet, neutral margins, 70–85mm-equivalent level camera, gray-white seamless studio and soft even neutral light. Do not copy clothing, shoes, props, movement, background, face or hair from Images 2 and 3. Avoid changing leg length, distorted anatomy, crossed legs, bow legs, knock-knees, converging ankles, bare legs, bare feet, sharply separated toes, textile discontinuity, dramatic styling, props, text, logo, watermark or collage.

One REVIEW_REQUIRED candidate only; not Canon.
```

## Attempt result

- generated_at: `2026-09-11`
- built-in output: `/home/verdvana/.codex/generated_images/01a08f0d-f395-77a3-b936-7cedfa238706/exec-929fb7ac-f5d6-493e-bdbf-eefac663bfa3.png`
- project copy: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v005/BODY_01_FRONT_v005.png`
- result: one 3:4 image generated; seed and detailed settings were not returned
- QA: fail. A slight soft highlight is more visible along the legs, but the feet/toes still read as bare with sharply separated toes and insufficient hazy textile veil. The lower-leg silhouette also retains slight outward bowing rather than parallel knee-to-ankle axes. The held leg-proportion direction is not intentionally changed.
- lineage: unapproved L1 candidate; prohibited as an input for another L1 candidate

## User review

Rejected on 2026-09-11. The user accepts the current leg proportion and subtle leg sheen, but requires slightly straighter calf contours and a clearly hazy textile layer over the insteps and toes so toe clefts and burgundy polish appear softened beneath fabric. v005 is prohibited from downstream use.
