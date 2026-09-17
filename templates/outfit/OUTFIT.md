# Outfit Design

- outfit_id:
- level: L2
- intended_character_id:
- episode/scene scope:
- status: DRAFT
- asset_purpose: reusable L2 outfit package
- design_reference_status: DRAFT
- worn_validation_status: NOT_STARTED
- approved_design_reference:
- approved_worn_views: []

## Asset package contract

Every outfit package uses the same named view types. Create only the views needed
to verify this outfit; do not generate a view merely to complete a checklist.
Each generated candidate also requires `templates/outfit/GENERATION_RECORD.md`.

| View type | Required purpose | Downstream use |
|---|---|---|
| `design_reference` | Clothing-only design, layering, color and accessory coordination | Outfit design and QA; never identity lineage |
| `worn_front` | Front fit, length, tension, layering, head/neck/shoulder and headwear relationship validation; always head-present | Fit QA only; never a video keyframe reference |
| `worn_3q` | Side/shoulder/waist/hip or footwear checks not visible from front | Fit QA only; conditional |
| `worn_back` | Rear construction, back length, closures or rear layering | Fit QA only; conditional |
| `material_detail` | Important fabric surface, transparency, reflectance or finish | Material QA; conditional |
| `drape_detail` | Gravity fall, folds, hem response or movement-related drape | Drape QA; conditional |
| `construction_detail` | Seams, neckline, cuffs, fasteners, trims or shoe details | Construction QA; conditional |

`worn_*` assets are validation assets, not character Canon and not shot assets.
They must not be used as identity lineage, as a subsequent generation input, or
as a video keyframe reference. No output is promoted automatically.

All Owner `worn` validation assets are head-present by default, including outfits
without headwear. This keeps the package format uniform and allows validation of
neckline, shoulder, strap, hood, hat, headband, hair accessory, and face-adjacent
construction. A neutral head form is not permitted for Owner worn validation.
The owner's visible face must always be generated from L0 inputs and the applicable
Face method; an AI Face Canon may only be used for post-generation QA comparison.

## Garment reference inputs

Store outfit-specific real-world or supplied garment references under:

`reference_inputs/garment_references/`

The directory contains the reference image and its provenance record. A reference
may contain a model, person, background, or arbitrary lighting, but those elements
are never allowed to define the owner. Each reference must declare its garment-only
responsibilities and its `must_not_define` exclusions in `REF_<NNN>_PROVENANCE.md`.

```yaml
garment_references:
  - reference_id: REF_001
    path: reference_inputs/garment_references/REF_001.jpg
    source:
    sha256:
    responsibility:
      - garment silhouette
      - color blocking
      - construction detail
    must_not_define:
      - model identity
      - face
      - body or proportions
      - skin or hair
      - pose
      - lighting
      - background
      - photography style
    generation_use: garment_design_only
```

Never put personal identity photos into this directory. Never use a garment
reference as the sole authority for a person's body, face, skin, hair, or identity.

## Garment inventory and layering

| Layer | Asset/material ID | Construction | Color | Coverage |
|---|---|---|---|---|

## Silhouette and fit

### Validation targets

- shoulder/strap/neckline fit:
- garment length and hem position:
- waist/hip/chest tension:
- layering and coverage:
- drape/fold behavior:
- footwear and hosiery relationship:

## Hosiery and footwear contract

- hosiery_material_id:
- denier/color/finish:
- toe construction:
- footwear:
- continuous coverage required: yes/no

## Must not redefine

Face identity, body geometry, skin, or Character Canon.

## Face-safe worn-image rule

For every `worn_*` candidate where the owner's face is visible, the sole face
generation authority is the applicable source-derived Face method plus its L0
inputs. Do not supply an AI Face Canon, AI Body Canon, previous outfit, previous
shot, or generated candidate as a face-generation input. Approved AI Face Canon
may appear only under `qa_comparison_only` for post-generation contamination and
identity-drift checks.

If the face is not needed for fit validation, prefer a face-out-of-frame or
face-occluded composition. A body reference must be a deterministic face-excluded
derivative with provenance, checksum, responsibility, and exclusions.
