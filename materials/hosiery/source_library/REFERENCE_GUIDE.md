# Hosiery Reference Selection Guide

Always choose the material folder first, then choose the image that matches the visible region and footwear state. Use **one material image by default**, two only when one supplies full-leg response and the other supplies missing foot/toe continuity.

## Mandatory white hosiery selection — 2026-10-31

Every future AI image with white hosiery must use `HOS_USER_SELECTED_WHITE_STRICT`: user source `L0_HOS_USER_WHITE_001`, generation crop `HOS_USER_WHITE_001_LOWER_LEG_FOOT_CROP_001`. See [material contract and provenance](../reference_inputs/user_selected_white/MATERIAL_REFERENCE.md). The single face-free crop is the mandatory material input; never attach the full portrait for material generation. Color, translucency, sheen and visible knee-to-toe coverage only; no face/body/skin/nails/pose/shoes/background authority. Exact D number is unverified.

This takes priority over the older white front/rear selectors below and over AI outfit hosiery appearance. Older sources may fill a documented missing view only, without changing the selected material. It does not prescribe white hosiery for unrelated images.

## Quick selector

| Shot requirement | Primary image | Optional detail image |
|---|---|---|
| 15D black high-gloss, seated/open-toe | `IMG_2569.jpg` | `IMG_2568.jpg` for ankle/shoe; `IMG_2570.jpg` for crossed pose |
| 15D nude high-gloss | `IMG_2587.jpg` | none; flag limited source coverage |
| 15D nude matte, sole/underside foot | `IMG_2562.jpg` | none |
| 15D nude matte, crouched | `IMG_2579.jpg` for oblique bent-leg response | `IMG_2580.jpg` for side response |
| 15D nude matte, standing | `IMG_2581.jpg` | none |
| 15D nude matte, stronger visible leg-to-foot textile presence | `1.jpg` | use only for opacity/velvet-matte coverage and muted toe visibility; exclude its pose, anatomy, skin, nails, clothing, background and watermark |
| 15D nude soft sheen, standing | `IMG_2589.jpg` | `IMG_2591.jpg` alternate stance |
| 15D nude soft sheen, crouched | `IMG_2588.jpg` | `IMG_2590.jpg` side or `IMG_2592.jpg` complex turn |
| 15D nude soft sheen, sunlight close-up | `IMG_2601.jpg` | one standing source for overall response |
| 15D white soft sheen, front | `IMG_2604.jpg` | `IMG_2605.jpg` slight turn |
| User-selected pale sheer hosiery and plush open-toe mule | `user_selected_sheer_pale/PHOTO_2.jpg` | use only for hosiery appearance and slipper upper/opening; exclude leg anatomy, skin, pose and sole thickness |
| 15D white soft sheen, rear heel | `IMG_2606.jpg` | `IMG_2603.jpg` dynamic crossing |
| 30D black matte, full leg | `IMG_2557.JPG` | `IMG_2554.JPG` for raised foot |
| 30D black matte, foot/toe/sole | `IMG_2559.JPG` | `IMG_2557.JPG` for overall leg response |
| 30D black matte, thigh/hip | `IMG_2556.JPG` | `IMG_2558.JPG` for knee/thigh texture |
| 30D black, real-world open-toe shoe | `unnamed (1).jpg` | one true-matte studio source; this photo looks shinier |
| 30D nude high-gloss, standing | `IMG_2680.jpg` | `IMG_2679.jpg` front crouch or `IMG_2681.jpg` oblique crouch |
| 30D nude matte, barefoot/feet | `unnamed.jpg` | `IMG_2594.jpg` for real-world frontal context |
| 30D nude matte, open-toe shoes | `IMG_2594.jpg` | `IMG_2595.jpg` crossed or `IMG_2599.jpg`/`IMG_2600.jpg` alternate shoes |
| 30D nude soft sheen | `IMG_2682.jpg` | none; flag limited source coverage |

## Non-negotiable isolation

- These images define only fabric color, denier/opacity impression, finish, weave/tension, highlight behavior, coverage, and shoe interaction.
- Never import the photographed person's face, body, skin pigmentation, nail color, clothing, pose proportions, or background into the owner Canon.
- A folder label is a user-provided classification, not proof that every image is perfectly matched. `30d_black_matte/unnamed (1).jpg` visibly appears shinier than the studio matte set and must be used only for shoe interaction unless reclassified.
- For bare-foot shots with feet visible, prefer sources where instep, heel, and toes are visible. Do not rely on a shoe-obscured image to invent toe coverage.
- For thin hosiery, burgundy owner toenails are injected from Appearance Canon; material references do not determine their color.

## Current 15D nude matte pruned set

The user reduced this material folder to four active files on 2026-09-11. Route them only by the following responsibilities:

- `IMG_2562.jpg` — sole/underside-foot and toe coverage;
- `IMG_2579.jpg` — crouching, oblique bent-knee/calf/ankle response;
- `IMG_2580.jpg` — crouching, side bent-knee/calf/ankle response;
- `IMG_2581.jpg` — standing frontal full-leg color, opacity and vertical response;
- `1.jpg` — user-selected stronger 15D nude matte/velvet textile presence across legs and complete feet; it is material-only and cannot define pose, body/foot geometry, skin, nail color, clothing, background, watermark or floor contact.

Deleted files are not fallback references. If an active view is insufficient, record a coverage gap instead of resolving a removed filename.

## Same-source wider white crop option

`HOS_USER_SELECTED_WHITE_STRICT_WIDE_CROP_V2` supplies the same mandatory source's broader lower-body silky sheen and curved-leg/foot context from a native430×540 crop. Use it INSTEAD OF the narrow crop when needed, not as an additional identity/body reference. It inherits strict material-only duties and all exclusions; source unchanged, exact denier unknown. Provenance: `../reference_inputs/user_selected_white/PHOTO_1_LOWER_BODY_LEG_FOOT_MATERIAL_CROP_v2_PROVENANCE.json`. Do not copy photographed hand/pose/shoes/car or lighting.

## Outfit-scoped approved result — OWNER_DATE_SUMMER_01, 2026-10-31

For later uses of this outfit, user-approved Worn v015 is the HOSIERY appearance target. Follow `outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/HOSIERY_APPEARANCE_METHOD_v015.md` and reference set `OWNER_DATE_SUMMER_01_HOSIERY_APPEARANCE_APPROVED_V015`. The original user L0 source remains mandatory; Foot v002 supplies approved fine-foot construction. The v015 portrait's face/body are never generation authority; only the registered face-excluded material crop may transfer hosiery. This scoped decision does not replace materials of other outfits or promote a new L1 Canon.
