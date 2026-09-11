# GoldenPaw Studio — Project Rules

This file is binding for every human or AI agent working in this repository.

## Current phase

The project is building an asset and identity system. Do not generate video. Do not generate images in bulk. Generate a candidate only when the current approval gate explicitly permits it.

## Asset levels

| Level | Meaning | Examples | Promotion authority |
|---|---|---|---|
| L0 | Source of Truth | real human/cat photos, real material photos | ingestion only; never generated |
| L1 | approved and frozen Canon | face/body/hair canon, fixed props, calibration hosiery | user approval only |
| L2 | episode design assets | outfit, temporary prop, environment, hairstyle variation if allowed | user/design review |
| L3 | shot assets | start frame, keyframe, shot continuity image | shot QA |
| L4 | video | generated clips and edits | video QA |

No output is promoted automatically. In particular, L3 must never become L1 unless the user explicitly says “设为 Canon” or an equivalent unambiguous instruction.

## Non-negotiable reference rules

1. Never use `AI A -> AI B -> AI C` as an identity lineage.
2. Build each shot in parallel from approved master assets: character Canon + outfit + material + props + environment + shot specification.
3. A previous shot is continuity-only. It may define position, pose transition, camera direction, blocking, and object placement. It must not define face, body, skin, cat identity, fixed-prop geometry, or hosiery material.
4. Every reference has one or more declared responsibilities and explicit `must_not_define` exclusions.
5. Use the smallest relevant reference set. Do not attach every available reference.
6. A failed or unreviewed shot cannot be a downstream reference.
7. L0 files are immutable evidence: never edit, replace, upscale over, rename destructively, or overwrite them. Derivatives go elsewhere and retain provenance.

## Canon approval and freeze

- Candidate status is `DRAFT` or `REVIEW_REQUIRED`.
- Only explicit user approval changes an asset to `APPROVED`.
- A Canon release is immutable only after its version manifest has `lock_status: LOCKED`, approval evidence, approver, and date.
- Never edit a locked release. Create a new version (`v1.1` for compatible refinement, `v2.0` for identity-breaking change).
- Approval is attribute-scoped. An approved hairstyle image may define hair while explicitly not defining face, body, clothing, lighting, background, or rendering artifacts.
- `HAIRSTYLE_B_CANON` is a permitted generated-to-L1 exception only after explicit approval, and only for the declared hairstyle-B attributes.

## Owner Canon rules

- Before creating any owner L1 candidate, read `characters/CHR_HUMAN_001_OWNER/canon/OWNER_L1_GENERATION_SPEC.md` in full and use its current `spec_revision`. If a new user decision conflicts with it, update the specification and change log before generation.
- L1 calibration outfit: pink high-cut one-piece swimsuit + 15D velvet-finish sheer pantyhose + no shoes.
- This is a calibration tool, not mandatory episode wardrobe.
- Every owner L1 candidate that shows clothing must use the same Calibration Outfit, not only Gate 3. Cropped Face/Hair/Expression assets show the visible upper portion of the same pink one-piece; full-body/Pose assets show the complete outfit and hosiery; Feet/Hosiery details remain logically part of that outfit even when the swimsuit is outside frame.
- Long-term wardrobe: primarily dresses or shorts, pantyhose of specified color/finish/denier, and shot-selected bare feet/open-toe/closed shoes.
- Only `HAIRSTYLE_A` or `HAIRSTYLE_B` may be selected. Never blend them into a third hairstyle.
- `HAIRSTYLE_A` uses L0 real reference `DSC00847.jpg`. `HAIRSTYLE_B` uses L0 real reference `8.jpg`, supplemented by approved scoped L1 asset `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001`. Do not swap or blend their reference duties.
- Except for assets whose explicit purpose is `HAIRSTYLE_B`, every owner L1 asset that shows hair must use `HAIRSTYLE_A`. This includes Face, Body, Expression, Pose, Appearance, and Hosiery/Feet assets whenever the head is visible.
- Burgundy toenail polish is a stable appearance trait. It may show naturally beneath sheer hosiery and must not be forced visible beneath opaque hosiery.

## Hosiery rules

Pantyhose is one continuous textile garment across waist/hips, thighs, knees, calves, ankles, heels, insteps, and toes. Reject discontinuity, naked toes beneath supposedly closed-toe hosiery, and latex/PVC/plastic/rubber/liquid/body-paint appearance. Follow `docs/qa/hosiery_material_rules.md`.

## Cat and fixed-prop rules

- Cat QA must verify face shape, coat color, golden-shaded tipping distribution, eyes, nose, ears, and body proportions; reject drift toward another British Shorthair, orange tabby, or chinchilla type.
- Cat-sized Vision Pro and MacBook Pro are L1 Prop Canon. Their scale, structure, and use mode must not vary between episodes after lock.

## Character and recurring-location naming

- Character folders use `CHR_<TYPE>_<NNN>_<ALIAS>`, for example `CHR_HUMAN_001_OWNER` and `CHR_CAT_001_TECH_CAT`. Allocate the next unused number within the type; never reuse an ID.
- Recurring fixed locations use `ENV_<TYPE>_<NNN>_<ALIAS>`. The owner's residence is `ENV_HOME_001_OWNER_RESIDENCE`.
- The locked residence Canon controls exterior identity, interior architecture/layout, permanent finishes, openings, circulation, and stable landmarks. Episode dressing and temporary object placement remain L2.
- A previous shot may preserve object placement and camera continuity but cannot redesign the locked residence.

## Required generation record

Before any future ImageGen call, create a shot/candidate record from the templates. It must list asset IDs, versions, responsibility, exclusions, reference budget, prompt assembly, seed/settings when available, output path, and QA status. Never put personal identity photos into a material-only slot or use material photos to define identity.

Resolve references from `registries/reference_sets.yaml` and the nearest `REFERENCE_GUIDE.md` first. Re-open and re-analyze a complete L0 folder only when no named set covers the required view/property or when newly added files have not yet been cataloged.

## Privacy and repository hygiene

- Treat L0 human photos as sensitive. Do not publish or export them.
- Do not commit secrets, temporary uploads, cache files, or unapproved exports.
- Preserve existing user files and unrelated worktree changes. Do not delete or restore them without explicit instruction.

## Single-file storage and promotion

- Every visual asset or deterministic reference derivative has exactly one authoritative physical image file in the repository. Records, manifests, candidates, and reference sets point to that file by asset ID, path, and SHA-256; they must not keep additional pixel copies.
- Candidate `inputs/` directories contain provenance records only. Never copy a Canon, L0 source, material source, or reusable derivative into a candidate directory.
- Reusable deterministic derivatives live once in the nearest scoped `reference_inputs/` directory. Their provenance record names the immutable source, operation, geometry/settings, responsibility, exclusions, and checksum.
- On explicit approval, move the candidate image to its approved Canon path instead of copying it. The candidate directory retains the generation record, QA, original candidate path/checksum, current approved path/checksum, and approval record, but no second raster copy.
- If the user transcodes the promoted file, keep only the active approved file. Preserve the pre-transcode checksum as textual provenance; do not retain the old-format pixels solely as evidence.
- Do not use hard links or symlinks for Canon deduplication. A Canon path must resolve to its own ordinary immutable file so that locks, archives, Git, and external tools behave predictably.
