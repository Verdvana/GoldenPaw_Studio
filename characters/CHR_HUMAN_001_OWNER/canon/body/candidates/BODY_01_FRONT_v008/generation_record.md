# BODY_01_FRONT_v008 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.35
identity_md_revision: draft_0.33
body_md_revision: draft_0.10
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v008
gate: "Gate 3 — Body Canon"
model_tool: "built-in image_gen"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v008/BODY_01_FRONT_v008.png"
pixel_storage_status: "MOVED_TO_CANON_THEN_TRANSCODED; CANDIDATE_RASTER_REMOVED"
current_promoted_path: null
historical_promoted_path: "characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_001.jpg"
promoted_raster_status: "REMOVED_BY_USER_AFTER_SUPERSESSION"
qa_status: PASS
checksum_sha256: "2f7f3828feb3a2e500482812a7a24f1284f87e71406b312ea579345293012a00"
```

## User-scoped revision

- only correction: the waist in v007 is too thick;
- slightly narrow the natural waist at its smallest point and smooth the ribcage-to-waist-to-hip transition;
- do not create a tiny waist, corset compression or exaggerated hourglass;
- hold all other user-confirmed directions: face, Hairstyle A, leg share, straighter calf direction, subtle leg sheen, hazy foot/toe textile veil and muted burgundy polish beneath fabric;
- do not use v007 or any previous candidate pixels.

## Reference plan

1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — SHA-256 `4d657954098490fc39da6ae257a47d8275b6237962af6d98e3c8a715ac690fc4`; exact front face identity only.
2. `L0_OWNER_002` (`3.jpg`) — SHA-256 `556f6d4652e1f5ac18725cdb03ea2f7e90a761450a1fc4bdd50bf4cf42aff310`; real standing proportion context only.
3. `L0_OWNER_003` (`4.jpg`) — SHA-256 `ca270e55c50fd168c798b0fbb20c9a8feded4c7f65e1c5af901b0c5e3601762b`; natural torso and limb-volume cross-check only.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — SHA-256 `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`; Hairstyle A only.

Each input is excluded from defining every other domain. No previous candidate, previous shot or hosiery photograph is supplied.

## Prompt assembly

```text
Create one neutral full-length front-view technical character reference of the adult woman in Image 1. Images 2–3 provide natural body proportions only and Image 4 provides Hairstyle A only. Use no previous generated image.

Preserve the approved face, hairstyle and established natural body direction. Make only one body correction: reduce the waist width modestly at the natural waist and create a smoother, gently defined transition from lower ribcage through waist to hips. Keep realistic soft tissue and torso volume; no tiny waist, corset shape or exaggerated hourglass.

Hold the current leg length and straight parallel lower-leg direction. Standard calibration clothing: opaque plain pink high-cut one-piece athletic swimsuit, light nude closed-foot 15D velvet sheer tights, no shoes. Keep the subtle broad leg sheen and a soft translucent fabric veil over legs and feet; toe details and burgundy nail color remain gently muted beneath the fabric, with no toe seam or band.

Exact 3:4 full body, complete head, hands and feet, neutral gray-white seamless studio, soft even light and level lens-neutral camera. No other body changes, anatomy errors, props, text, watermark or collage. One REVIEW_REQUIRED candidate only; not Canon.
```

## Attempt result

- generated_at: `2026-09-11`
- built-in output: `/home/verdvana/.codex/generated_images/01a08f0d-f395-77a3-b936-7cedfa238706/exec-5402c7ab-4598-43d3-acae-fa731e57ca55.png`
- original candidate path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v008/BODY_01_FRONT_v008.png` (record only; raster removed after promotion)
- result: one 3:4 image generated; seed and detailed settings were not returned
- QA: pass for user review. Waist is modestly narrower with a natural transition and no exaggerated hourglass. The user-confirmed face, hair, leg proportion/direction, subtle sheen, hazy foot covering and muted burgundy polish direction remain present.
- lineage: approved promotion source; downstream work must use the promoted Master, while L1 recreation must use the source-derived recovery method and never this candidate's pixels

## User approval

On 2026-09-11 the user stated: “ok,可以作为canon，并记录生成的方法，保证后续输出的稳定性”. The candidate was promoted to `OWNER_BODY_01_FRONT_CANON_001`. This approval is scoped to front-view Body geometry and neutral stance; the full `owner_v1.0` remains unlocked.

The user later transcoded the approved Master to JPG. The former candidate PNG path and checksum remain textual generation/approval provenance, and the candidate raster was removed under the single-file rule. The current downstream JPG path and checksum are indexed separately.
