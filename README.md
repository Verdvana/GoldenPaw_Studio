# GoldenPaw Studio

GoldenPaw Studio is a long-lived AI short-video production repository built around traceable, role-scoped references. This phase establishes identity consistency, Canon governance, reference selection, and QA; it intentionally produces no final video and no batch of images.

## The workflow

```text
L0 real sources
  -> analysis and candidate brief
  -> gated L1 Canon candidates
  -> explicit human approval
  -> versioned, locked L1 Canon
  + L2 outfit/material/prop/environment designs
  + shot specification and continuity-only reference
  -> L3 shot candidate
  -> multi-domain QA
  -> eligible Image-to-Video input
  -> L4 video and edit
```

Each shot is regenerated from Master Assets rather than inheriting identity from the previous shot. Previous shots can guide blocking and motion continuity only.

## Where assets live

- `characters/<character_id>/source/identity/raw/`: L0 real identity photos. Character folders use `CHR_<TYPE>_<NNN>_<ALIAS>`.
- `characters/<character_id>/canon/`: attribute-scoped L1 candidates and approved references.
- `materials/hosiery/source_library/raw/<denier>_<material>_<color>/`: shared L0 real hosiery photos, never identity references.
- `props/<prop_id>/`: fixed or episodic props and their versioned Canon.
- `outfits/<outfit_id>/`: L2 wardrobe packages.
- `environments/<environment_id>/`: L1 recurring-location Canon or L2 episode environment packages.
- `episodes/<season>/<episode>/scenes/<scene>/shots/<shot>/`: specifications, chosen references, outputs, and QA.
- `templates/`: copy-first templates for every asset and production object.
- `registries/`: central IDs, versions, levels, statuses, and dependency records.
- `docs/`: approval, selection, prompt assembly, and QA rules.

Character directories use stable, sortable IDs: `CHR_HUMAN_001_OWNER` and `CHR_CAT_001_TECH_CAT`. Add roles as `CHR_HUMAN_002_<ALIAS>`, `CHR_CAT_002_<ALIAS>`, and so on; numbering is independent within each type and the alias may change only before assets are registered. Add every character to `registries/assets.yaml`.

Previously analyzed image choices are stored in `registries/reference_sets.yaml` and the asset-level `REFERENCE_GUIDE.md` files. Future shot planning should select a named set instead of opening every source image again.

Use `docs/reference_routing.md` to decide which category of reference is needed at each Canon or Shot stage.

## First intake

1. Place original owner photos in `characters/CHR_HUMAN_001_OWNER/source/identity/raw/`.
2. Place original cat photos in `characters/CHR_CAT_001_TECH_CAT/source/identity/raw/`.
3. Place folders of real hosiery/feet photos in `materials/hosiery/source_library/raw/`, named like `15d_velvet_nude`, `30d_matte_black`, or `80d_opaque_gray`. They define textile behavior only.
4. Place real home interior, exterior, and layout references in the matching `source/*/raw/` folders under `environments/ENV_HOME_001_OWNER_RESIDENCE/`.
5. Do not rename or modify originals after registration. Record each file in the nearest `SOURCE_MANIFEST.md` using stable IDs and checksums where practical.
6. Complete Gate 1 analysis before generating a Canon candidate.

## Recommended Canon order

For the owner: Face Identity anchors -> body/calibration outfit -> hairstyles A and B -> expressions -> body/pose anchors -> hosiery/feet Canon -> final Character Manifest and lock.

For the cat: identity/coat analysis -> neutral face views -> body/turnaround -> coat details -> core expressions/poses -> final Character Manifest and lock.

For fixed props: establish cat-relative measurements first, then approve orthographic/interaction views for `vision_pro_cat` and `macbook_pro_cat`.

Every gate requires explicit user approval. The final character and fixed-prop versions must be locked before routine episode shot production.

## Starting a future shot

Copy `templates/shot/` into the shot folder, fill `SHOT.md`, select references using `docs/reference_selection.md`, and assemble the prompt using `docs/prompt_assembly.md`. Generate only after the reference plan is reviewable. Run `QA.md` after generation; only a passing output can progress.

## Status values

Use `DRAFT`, `REVIEW_REQUIRED`, `APPROVED`, `REJECTED`, `LOCKED`, and `DEPRECATED`. `APPROVED` describes an asset decision; `LOCKED` describes an immutable version release. Neither is inferred from a filename or folder.
