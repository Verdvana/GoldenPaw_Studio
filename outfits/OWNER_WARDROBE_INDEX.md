# Owner L2 Wardrobe Index

```yaml
index_id: OWNER_L2_WARDROBE_INDEX
character_id: CHR_HUMAN_001_OWNER
level: L2
status: DRAFT
image_generation_status: IN_PROGRESS
```

These are reusable episode-design outfit packages. They may be reused across episodes after approval, but they do not redefine the owner's L1 face, body, hair, expression, pose, hosiery or identity.

Each package follows `templates/outfit/OUTFIT.md` and keeps outfit-specific supplied
references in `reference_inputs/garment_references/`. Those references define only
the declared garment/material/construction properties. Any model, face, body, skin,
hair, pose, lighting, background, or photography style in a supplied reference is
excluded by policy.

Future candidates use `templates/outfit/GENERATION_RECORD.md`. Existing historical
records are retained as provenance, but their old input lineage must not be reused;
an asset generated under an earlier rule requires a fresh candidate before it can
serve as a future generation input.

| Outfit ID | Use / season | Planned visual package | Status |
|---|---|---|---|
| `OWNER_HOME_SLEEP_SUMMER_01` | home sleepwear / summer | design reference + worn front; footwear visible | REBUILD REQUIRED |
| `OWNER_HOME_SLEEP_WINTER_01` | home sleepwear / winter | design reference + worn front; hood and slippers visible | REBUILD REQUIRED |
| `OWNER_SPORT_YOGA_01` | yoga | design reference + worn front + 3/4/back if open-back fit needs verification | REBUILD REQUIRED |
| `OWNER_SPORT_BADMINTON_01` | badminton | design reference + worn front + 3/4; back optional | DESIGN REFERENCE + WORN FRONT APPROVED |
| `OWNER_SPORT_SWIM_01` | swimming | design reference + worn front + 3/4; swim cap/goggles visible | DESIGN_REFERENCE_APPROVED_WORN_FRONT_PENDING |
| `OWNER_WORK_SUMMER_01` | office / summer | design reference + worn front + 3/4; shoe detail if needed | REBUILD REQUIRED |
| `OWNER_WORK_WINTER_01` | office / winter | design reference + worn front + 3/4/back; boot detail if needed | REBUILD REQUIRED |

## Generation policy

- Each outfit is generated independently from the written garment contract and the smallest relevant approved/source-derived references; no previous outfit candidate, shot, or generated image is identity lineage.
- `design_reference` is clothing-only whenever practical. It defines garment silhouette, color, layering, accessories, and declared construction/material properties only.
- `worn_front`, `worn_3q`, and `worn_back` are always head-present fit-validation assets. They verify tension, length, coverage, layering, drape, footwear/hosiery relationships, and headwear or neckline/shoulder relationships. They are not video keyframe references, not Character Canon, and not valid downstream identity inputs.
- Every Owner worn asset must include the owner's head and visible face generated from L0 inputs plus the applicable source-derived Face method. AI Face Canon, AI Body Canon, previous outfit/shot/candidate, and neutral head forms are forbidden as face-generation inputs; AI Face Canon is comparison-only QA.
- For every worn candidate where the owner's face is visible, the applicable source-derived Face generation method and its L0 inputs are the sole face-generation authority. Do not pass an AI Face Canon, AI Body Canon, previous outfit, previous shot, or generated candidate as a face-generation input.
- Approved AI Face Canon images may be listed only under `qa_comparison_only`, for post-generation identity-drift and face-contamination QA. They are forbidden under `generation_inputs`.
- If the face is unnecessary for fit validation, prefer a face-out-of-frame or face-occluded composition. Any body reference must be a deterministic face-excluded derivative with provenance, checksum, responsibility, and exclusions.
- Before reporting a worn candidate, record fit QA and face-contamination QA. If either fails, mark the candidate `REJECTED`; never promote it or use it downstream.
- Default package: one clothing-only `design_reference` and one head-present `worn_front` validation view. Add 3/4, back, material, drape, or construction views only when they answer a documented validation question.
- Outfit approval is scoped to garment design, layering, fit, footwear and hosiery contract; it cannot redefine Character Canon.

## Open decisions

- `OWNER_SPORT_YOGA_01`: resolved as a white performance court shoe with small pale-pink/peach accents and a white non-marking outsole.
- `OWNER_WORK_SUMMER_01`: resolved as a black ballet-toe slingback kitten heel.
- `OWNER_SPORT_BADMINTON_01`: resolved as a white performance badminton shoe; exact model styling remains to be designed.
