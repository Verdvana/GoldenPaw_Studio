# Owner L2 Wardrobe Index

```yaml
index_id: OWNER_L2_WARDROBE_INDEX
character_id: CHR_HUMAN_001_OWNER
level: L2
status: DRAFT
image_generation_status: IN_PROGRESS
```

These are reusable episode-design outfit packages. They may be reused across episodes after approval, but they do not redefine the owner's L1 face, body, hair, expression, pose, hosiery or identity.

| Outfit ID | Use / season | Planned visual package | Status |
|---|---|---|---|
| `OWNER_HOME_SLEEP_SUMMER_01` | home sleepwear / summer | design reference + worn front; footwear visible | DESIGN REFERENCE APPROVED; WORN FRONT PENDING |
| `OWNER_HOME_SLEEP_WINTER_01` | home sleepwear / winter | design reference + worn front; hood and slippers visible | DESIGN REFERENCE + WORN FRONT APPROVED |
| `OWNER_SPORT_YOGA_01` | yoga | design reference + worn front + 3/4/back if open-back fit needs verification | DESIGN REFERENCE APPROVED; WORN VIEWS PENDING |
| `OWNER_SPORT_BADMINTON_01` | badminton | design reference + worn front + 3/4; back optional | DESIGN REFERENCE APPROVED; WORN VIEWS PENDING |
| `OWNER_SPORT_SWIM_01` | swimming | design reference + worn front + 3/4; swim cap/goggles visible | DESIGN REFERENCE APPROVED; WORN VIEWS PENDING |
| `OWNER_WORK_SUMMER_01` | office / summer | design reference + worn front + 3/4; shoe detail if needed | DESIGN REFERENCE APPROVED; WORN VIEWS PENDING |
| `OWNER_WORK_WINTER_01` | office / winter | design reference + worn front + 3/4/back; boot detail if needed | DRAFT |

## Generation policy

- Each outfit is generated independently from approved L1 character references plus its written garment contract; no previous outfit candidate is a pixel input.
- For every worn reference, approved L1 face, body and permitted hairstyle files must be passed to ImageGen as actual local image inputs (`referenced_image_paths`), after verifying the paths exist. Listing reference IDs or paths in a prompt or record without attaching the images is a failed preflight and generation must stop.
- When the approved Body Master already contains the authoritative face, Hairstyle A and body proportions, use it as the single character reference for a worn-front rebuild unless a view-specific L1 asset is required. Do not attach overlapping face/body/hair identity references together without a documented need; overlapping identity inputs can cause fusion drift.
- Before reporting a worn candidate, verify that the output visibly preserves the approved owner face, hairstyle and body proportions. If identity drifts, mark the candidate `REJECTED`; never promote it or use it downstream.
- Default package: one clothing-only design reference and one worn front reference.
- Add worn 3/4/back views only when fit, rear construction, layering or footwear cannot be verified from the front.
- Material-detail references are added only for visually important fabrics or reflective/technical surfaces.
- Outfit approval is scoped to garment design, layering, fit, footwear and hosiery contract; it cannot redefine Character Canon.

## Open decisions

- `OWNER_SPORT_YOGA_01`: resolved as a white performance court shoe with small pale-pink/peach accents and a white non-marking outsole.
- `OWNER_WORK_SUMMER_01`: resolved as a black ballet-toe slingback kitten heel.
- `OWNER_SPORT_BADMINTON_01`: resolved as a white performance badminton shoe; exact model styling remains to be designed.
