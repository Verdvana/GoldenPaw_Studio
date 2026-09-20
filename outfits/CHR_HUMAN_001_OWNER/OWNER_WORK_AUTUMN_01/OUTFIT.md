# Outfit Design

- outfit_id: OWNER_WORK_AUTUMN_01
- level: L2
- intended_character_id: CHR_HUMAN_001_OWNER
- episode/scene scope: reusable owner autumn officewear
- character_outfit_root: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_AUTUMN_01
- garment_reference_dir: reference_inputs/garment_references/
- status: L2_COMPONENTS_APPROVED
- asset_purpose: reusable L2 outfit package
- design_reference_status: REVIEW_REQUIRED_v002
- worn_validation_status: APPROVED_v003
- approved_design_reference:
- approved_worn_views: [approved/worn_front/OWNER_WORK_AUTUMN_01_WORN_FRONT.png]

## Autumn officewear path

This is a new, reference-led design path. The supplied reference images will
define only garment silhouette, layering, palette, textile, construction, and
accessories. They will not define the owner's face, body, skin, hair, pose,
lighting, background, or photographic style.

1. **Reference intake** — place supplied images in
   `reference_inputs/garment_references/`; create one `REF_<NNN>_PROVENANCE.md`
   record per image with checksum, declared responsibilities, and exclusions.
2. **Garment contract** — translate the selected references into a concrete
   autumn office look: outer layer, inner layer, lower garment, hosiery,
   footwear, and work accessories. Unspecified design choices remain open until
   the references are reviewed.
3. **Clothing-only design candidate** — create one `design_reference` candidate
   to validate silhouette, palette, layering, and construction. It is not an
   identity or body reference.
4. **Head-present fit-validation candidate** — only after the design is
   reviewed, create `worn_front`; add `worn_3q`, `worn_back`, or detail views
   only for documented unresolved fit/material questions.
5. **Scoped review** — assess garment construction, layering, drape,
   hosiery/footwear continuity, and face-safety QA. No candidate is promoted
   without explicit user approval.

## Garment inventory and layering

The user has specified the garment contract; `REF_002` defines the jacket, inner
layer, and trousers, while `REF_001` remains a shoe-only reference.

| Layer | Asset/material ID | Construction | Color | Coverage |
|---|---|---|---|---|
| 1 | garment / `REF_002` | light blush-pink tailored blazer, open front, rolled sleeves | pale pink | upper body |
| 2 | garment / `REF_002` | soft gray satin camisole / sleeveless inner top | cool gray | upper body |
| 3 | garment / `REF_002` | high-waisted wide-leg tailored trousers, full length | warm gray-taupe | waist to ankle |
| 4 | hosiery | sheer light-skin pantyhose, continuous closed-toe construction | light nude | waist to toes |
| 5 | footwear / `REF_001` | pointed-toe slingback pump with buckle and slender high heel | black | foot |

## Hosiery and footwear contract

- hosiery_material_id: HOS_15D_NUDE_MATTE_STANDING
- denier/color/finish: light-skin 15D sheer, soft matte / velvet-matte textile finish
- toe construction: continuous closed-toe coverage; no toe-cap boundary
- footwear: black pointed-toe slingback pump with rear strap/buckle and slender high heel, using `REF_001` only for declared construction
- continuous coverage required: yes

## Non-negotiable generation boundaries

- `design_reference` is garment-only whenever practical and never defines owner identity.
- Every Owner `worn_*` validation image is head-present; its visible face must be
  generated solely from the applicable L0 inputs and source-derived Face method.
- AI Face Canon, AI Body Canon, prior outfit images, prior shots, and generated
  candidates are forbidden as face-generation inputs. Approved AI Face Canon is
  permitted only for post-generation QA comparison.
- A body reference, if needed, must be a deterministic face-excluded derivative
  with provenance, checksum, responsibility, and exclusions.
- If this path specifies pantyhose, it is one continuous textile garment from
  waist/hips through toes; reject bare toes, breaks, and plastic/rubber-like finish.

## Must not redefine

Face identity, body geometry, skin, hair, pose, Character Canon, or fixed-prop
geometry.
