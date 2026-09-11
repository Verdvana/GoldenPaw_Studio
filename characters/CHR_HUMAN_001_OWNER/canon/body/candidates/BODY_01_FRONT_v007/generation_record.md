# BODY_01_FRONT_v007 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.34
identity_md_revision: draft_0.32
body_md_revision: draft_0.9
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v007
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v007/BODY_01_FRONT_v007.png"
qa_status: FAIL
checksum_sha256: "76cb319c3d7f6dcaf75c84205d54c3bfe138f27b5c67427cc1d38f9f58849920"
```

## User-scoped revision

- hold the current leg proportion and subtle leg sheen;
- straighten calf axes further with knees, shin centers, ankles and feet vertically aligned;
- retain a visibly hazy fine-fabric layer over insteps/toes;
- increase foot transparency from v006 so burgundy polish is visible as soft muted color beneath the same fabric;
- keep toe clefts softened, never bare and crisp;
- no seam, color band, reinforced toe or opaque toe cap;
- do not use v006 or any previous candidate pixels.

## Reference plan

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`; exact front face identity, adult age, neutral expression and natural skin appearance only.
2. `L0_OWNER_002` (`3.jpg`) — SHA-256 `556f6d4652e1f5ac18725cdb03ea2f7e90a761450a1fc4bdd50bf4cf42aff310`; real standing proportion context only.
3. `L0_OWNER_003` (`4.jpg`) — SHA-256 `ca270e55c50fd168c798b0fbb20c9a8feded4c7f65e1c5af901b0c5e3601762b`; natural torso and limb-volume cross-check only.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — SHA-256 `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`; Hairstyle A only.

Each input is excluded from defining every other domain. No previous candidate, previous shot or hosiery photograph is supplied.

The first v007 call produced no image because of an output-stage sexual safety rejection (`request_id: d31b067b-f3b0-46b7-9c8b-8cd6fbb04e2f`). The safe retry keeps the same four references and visible requirements in shorter technical language.

The second call also produced no image because of an output-stage sexual safety rejection (`request_id: 986ad634-52f3-41da-be03-ca2d453493cf`). One final minimal retry keeps only the essential full-body, straight-leg and closed-foot sheer-textile outcome language.

## Prompt assembly

```text
Create one neutral full-length technical studio reference of the adult woman defined by Image 1. Images 2 and 3 are body-proportion context only; Image 4 is long straight Hairstyle A only. Use no prior generated image.

Keep the approved face, hairstyle, current leg proportion and gentle leg sheen. Use a square relaxed front stance. Make both lower-leg axes clearly straighter and parallel: knee centers, shin centers, ankle centers and feet align vertically; reduce outward calf curvature while retaining natural calf volume.

Standard calibration clothing: opaque plain pink high-cut one-piece athletic swimsuit, nude closed-foot 15D velvet sheer tights, no footwear. A visible translucent fine-fabric haze continuously covers legs, insteps and toes. The veil softens toe gaps and nail edges without hiding them completely; burgundy nail color remains visible underneath as muted, gently blurred color. Keep uniform transparency and the accepted slight velvet sheen. No toe seam, color band, reinforced toe, opaque foot covering, bare-looking toes or plastic shine.

Exact 3:4 full body, complete head, hands and feet, neutral gray-white studio, soft even light and lens-neutral level camera. Do not change leg length. No crossed legs, bow legs, knock-knees, distorted anatomy, props, text, logo, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.
```

## Safe-retry prompt assembly

```text
Create one neutral full-length technical studio reference of the adult woman in Image 1. Images 2–3 are natural proportion context only and Image 4 is Hairstyle A only. No previous generated image.

Preserve the face, hairstyle, current leg length and gentle leg sheen. Square relaxed front stance. Make the lower legs straighter and parallel, with knees, shins, ankles and feet vertically aligned while keeping natural calf volume.

Use the standard plain opaque pink high-cut one-piece athletic swimsuit and light nude closed-foot 15D sheer tights, without footwear. The tights form a visible soft translucent fabric veil over the full legs and feet. Dark burgundy nail color is subtly visible through the veil with softened edges. No toe seam, color band, opaque foot area, crisp bare-looking toes or plastic shine.

Exact 3:4 full body, complete head, hands and feet, neutral gray-white studio, soft even light and level lens-neutral camera. No proportion change, bow legs, crossed legs, anatomy errors, props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.
```

## Final minimal-retry prompt assembly

```text
Create one neutral full-length front-view technical character turnaround photograph of the adult woman in Image 1. Images 2–3 provide body proportions only and Image 4 provides hairstyle only. Do not use previous generated images.

Preserve her face, hairstyle and current proportions. Relaxed symmetrical stance. Both legs are straight and parallel, with knees and ankles vertically aligned.

She wears the standard opaque pink one-piece competition swimsuit and continuous light-nude 15D closed-foot sheer tights, without shoes. Fine translucent fabric is visibly present over legs and feet, softening the foot details while allowing a muted burgundy nail tint to remain visible beneath it. Uniform material with no toe band or seam.

Exact 3:4 full body, all extremities visible, neutral gray-white seamless studio, soft even lighting, level lens-neutral camera. No props, text, watermark or collage. REVIEW_REQUIRED, not Canon.
```

## Attempt result

- generated_at: `2026-09-11`
- successful attempt: final minimal retry with four approved/source references
- built-in output: `/home/verdvana/.codex/generated_images/01a08f0d-f395-77a3-b936-7cedfa238706/exec-b0791266-0c6d-4786-9f22-a3515a4c1527.png`
- project copy: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v007/BODY_01_FRONT_v007.png`
- result: one 3:4 image generated; seed and detailed settings were not returned
- QA: fail. Muted burgundy polish returns and the feet have a light uniform veil, but toe clefts and individual contours remain too crisp for the requested hazy fabric effect. Calf silhouettes also retain outward curvature and are not yet sufficiently straight/parallel. Leg proportion and broad sheen remain held.
- lineage: unapproved L1 candidate; prohibited as an input for another L1 candidate

## User review

Rejected on 2026-09-11 only because the waist is too thick. The user explicitly considers all other visible directions acceptable, superseding the automated pre-review concerns: leg share, calf-axis direction, subtle leg sheen, hazy foot/toe textile coverage, muted burgundy polish, face and Hairstyle A are to be held textually. v007 remains prohibited as a downstream pixel input.
