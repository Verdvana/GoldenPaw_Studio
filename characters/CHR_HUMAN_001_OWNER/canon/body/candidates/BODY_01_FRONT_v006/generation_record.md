# BODY_01_FRONT_v006 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.33
identity_md_revision: draft_0.31
body_md_revision: draft_0.8
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v006
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v006/BODY_01_FRONT_v006.png"
qa_status: FAIL
checksum_sha256: "49a7b9ea26ba2bfcf4e041dbc693f103ff5f39d19571a367f6164d5e49a62eb8"
```

## User-scoped revision

- hold the current leg-share target unchanged;
- hold the subtle broad leg sheen direction unchanged;
- make calf contours slightly straighter, with knee and ankle centers vertically aligned;
- create an unmistakable fine 15D textile haze across insteps and toes so toe clefts and burgundy polish are softened beneath fabric;
- keep the polish visible but less crisp and saturated than bare nails;
- no toe seam, reinforced toe, color boundary or opaque toe cap;
- preserve face and Hairstyle A from approved/source inputs; do not use v005 pixels.

## Reference plan

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`; exact front face identity, adult age, neutral expression and natural skin appearance only; must not define body, outfit, hosiery, lighting or background.
2. `L0_OWNER_002` (`3.jpg`) — SHA-256 `556f6d4652e1f5ac18725cdb03ea2f7e90a761450a1fc4bdd50bf4cf42aff310`; real standing proportion context only; must not define face, hair, clothing, footwear, props, asymmetry, background or retouching.
3. `L0_OWNER_003` (`4.jpg`) — SHA-256 `ca270e55c50fd168c798b0fbb20c9a8feded4c7f65e1c5af901b0c5e3601762b`; natural torso and limb-volume cross-check only; must not define walking pose, dress, legwear, shoes, face, hair, background or final body alone.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — SHA-256 `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`; Hairstyle A only; must not define face, body, skin, clothing, lighting or background.

No previous Body candidate, previous shot or hosiery photograph is supplied. Accepted v005 directions are carried forward as user-authored text only.

The first v006 call used the four active references and the detailed prompt below but produced no image because of an output-stage sexual safety rejection (`request_id: 70950448-638e-48e2-9ca8-ce6aff67fad6`). The safe retry retains the same reference plan and user-visible requirements in shorter technical language.

## Prompt assembly

```text
Create one neutral full-length technical studio reference of the adult woman in Image 1. Images 2 and 3 provide natural proportion context only; Image 4 provides the long straight Hairstyle A only. Use no previous generated image.

Keep the approved face, neutral expression, Hairstyle A, current leg proportion and subtle broad leg sheen. Stand square to camera with arms relaxed and even weight. Make both calf outlines slightly straighter: knee centers directly above ankle centers, feet below knees, parallel lower-leg axes and stable spacing. Reduce outward calf bow without making the legs unnaturally thin or rigid.

Use the standardized calibration clothing: plain opaque pink high-cut one-piece athletic swimsuit, nude 15D velvet-finish sheer pantyhose and no footwear. The pantyhose must read clearly as one continuous fine textile veil across thighs, shins, ankles, insteps and closed toes. Over the feet, the sheer weave creates gentle optical haze: toe clefts are softened and burgundy nail color is visible only as muted, slightly blurred color beneath fabric, never as crisp bare polish. Preserve the accepted faint velvet sheen along the legs. Uniform fabric color and transparency with no toe seam, reinforced toe, color line, opaque toe cap, plastic gloss or bare-looking foot.

Exact 3:4 full-body portrait with complete head, hair, hands and feet, neutral margins, 70–85mm-equivalent level camera, gray-white seamless studio and soft even neutral light. Do not copy clothing, shoes, props, movement, background, face or hair from Images 2 and 3. Avoid changing leg proportion, crossed legs, bow legs, knock-knees, converging ankles, distorted anatomy, bare feet, crisp separated toe clefts, sharply saturated bare-looking nails, textile discontinuity, dramatic styling, props, text, logo, watermark or collage.

One REVIEW_REQUIRED candidate only; not Canon.
```

## Attempt result

- generated_at: `2026-09-11`
- successful attempt: safe retry with four approved/source references
- built-in output: `/home/verdvana/.codex/generated_images/01a08f0d-f395-77a3-b936-7cedfa238706/exec-979af0e4-2b87-4726-80ed-a82622ab2510.png`
- project copy: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v006/BODY_01_FRONT_v006.png`
- result: one 3:4 image generated; seed and detailed settings were not returned
- QA: fail. Calf axes are improved and the feet/toes now read as continuously fabric-covered with softened clefts, but the foot covering is too optically dense for the target 15D behavior and the burgundy polish is no longer visibly transmitted through it. The accepted leg share and subtle leg sheen remain in direction.
- lineage: unapproved L1 candidate; prohibited as an input for another L1 candidate

## User review

Rejected on 2026-09-11. Calf axes need further straightening. The foot textile haze should remain, but its transparency must increase enough for muted burgundy polish to show beneath the fabric. v006 is prohibited from downstream use.

## Safe-retry prompt assembly

```text
Create one neutral full-length technical studio reference of the adult woman defined by Image 1. Images 2 and 3 are proportion context only; Image 4 is Hairstyle A only. Use no prior generated image.

Keep the approved face, hairstyle, current leg length and gentle leg sheen. Use a square relaxed front stance. Make the lower legs slightly straighter and parallel, with knees vertically above ankles and feet below knees; reduce outward calf curvature.

Standard calibration clothing: opaque plain pink high-cut one-piece athletic swimsuit, nude closed-foot 15D velvet sheer tights, no footwear. A visible fine-fabric haze continuously covers legs and feet, softly diffusing toe gaps and the dark-red nail color beneath it. No toe line, color band, opaque toe cap, bare-looking foot or plastic shine.

Exact 3:4 full body, complete head, hands and feet, neutral gray-white studio, soft even light and lens-neutral level camera. No proportion change, crossed legs, bow legs, distorted anatomy, props, text, logo, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.
```
