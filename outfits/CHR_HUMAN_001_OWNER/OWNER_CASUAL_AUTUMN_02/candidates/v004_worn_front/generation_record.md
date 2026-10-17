# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v004

Independent L2 candidate. Use exactly the five generation inputs and three QA-only
references enumerated in `../v003_worn_front/generation_record.md`; no previous
candidate pixels are inputs.

```yaml
asset_id: OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v004
outfit_id: OWNER_CASUAL_AUTUMN_02
asset_level: L2
asset_purpose: worn_front
candidate_version: v004
status: APPROVED
approval_status: APPROVED_BY_USER
generation_tool: built-in ImageGen
generated_at: 2026-10-17
original_candidate_path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v004_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v004.png
approved_path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT.png
output_sha256: 0b25ab1fc7ed465e18fac90022f4b9db67f9238cc88970836caf19abfffc9eb4
reference_set_ids:
  - OWNER_L0_FACE_013_GEOMETRY_CROP_V1
  - OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE
reference_budget: 5 image inputs; 3 QA-only comparisons
aspect_ratio: "3:4"
seed_settings: ImageGen did not expose seed or sampler settings
```

## Generation inputs

The five generation inputs used for v004 have the same assets, versions, paths,
responsibilities and exclusions documented in `../v003_worn_front/generation_record.md`:

1. `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — L0-derived facial geometry and
   recognizable identity only; excludes hair, body, clothing and lighting.
2. `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` — L0 skin tone and texture only;
   excludes fine facial geometry, body, hair and clothing.
3. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — source Hairstyle A pixels and construction
   only; excludes face, identity, body and clothing.
4. `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — deterministic face-excluded body
   derivative for neck-below proportions and stance only; excludes face, hair,
   clothing design and hosiery appearance.
5. `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` — approved clothing design and palette
   only; excludes face, body, proportions, skin, hair, pose and identity.

## QA comparison only

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — identity, facial-feature relationships,
  contamination and framing comparison only; not a generation input.
- `OWNER_BODY_01_FRONT_CANON_007` — body proportion and stance comparison only; not a
  generation input.
- `L0_HOS_15_WSS_002` — hosiery tone, sheerness and textile response comparison only;
  not a generation input.

Generation inputs and QA-only comparisons are separate; no AI Face/Body Canon or
prior generated candidate was used to generate this image.

## Prompt assembly

Fresh, independent, photorealistic full-body front fit image, exact 3:4 portrait
framing. Head and torso face squarely forward. Use L0-derived face inputs only for
the face, Hairstyle A source derivative for hair only, and deterministic face-excluded
body derivative for neck-below proportions and stance. No AI Canon or prior generated
image may be a generation input.

Match the approved outfit: oatmeal cardigan, ivory tee, warm medium-brown wool mini
skirt, thin slightly sheer white pantyhose, pale light beige fuzzy open-toe mule
slippers. Keep skirt side seams nearly straight from hip to hem, with only a small
increase in width at the hem; no umbrella/circle/bell flare and no bodycon fit.
Pantyhose is mandatory and must be plainly visible as a continuous thin white textile
veil from waist over both legs, ankles, heels, insteps and toes. Show subtle skin tone
through sheer fabric; toes stay visibly covered by the same hosiery in the open-toe
slippers. Never show bare legs or toes. Use mild natural contrast so the fine white
textile boundary is legible against the studio background while remaining translucent.
Full head and both feet visible, soft even studio light, no text, logos or props.
One candidate only; initially REVIEW_REQUIRED, later explicitly approved by the user.

## QA

- technical_status: `PASS` (1086x1448, exact 3:4, head and feet fully visible)
- fit_validation_status: `PASS`
- face_contamination_check: `PASS` (comparison-only check; no obvious blotches or uneven patches)
- skirt_silhouette_check: `PASS` (restrained slight A-line; hem visibly more controlled than v001)
- framing_and_front_pose_check: `PASS` (front fit view; slight natural head tilt)
- outfit_fidelity_check: `PASS`
- hosiery_continuity_and_material_check: `APPROVED_BY_USER` (user approval covers the thin, slightly sheer pantyhose and visible toe coverage)
- decision: `APPROVED`
- reviewer: `Codex visual QA`
- reviewed_at: `2026-10-17`

## Promotion and approval

- candidate_original_sha256: `0b25ab1fc7ed465e18fac90022f4b9db67f9238cc88970836caf19abfffc9eb4`
- current_approved_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT.png`
- current_approved_sha256: `0b25ab1fc7ed465e18fac90022f4b9db67f9238cc88970836caf19abfffc9eb4`
- approval_status: `APPROVED`
- approved_by: `user`
- approval_date: `2026-10-17`
- approval_evidence: `批准`
- promotion_operation: `MOVED`; candidate raster moved to approved path, no duplicate retained
